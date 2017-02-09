import os
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap

class GXHConstant(Constant):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        if self.type == Type.STRING:
            return self.generator.get_template('#define {{ constant.name }} "{{ constant.value }}"').render(constant=self)
        else:
            return self.generator.get_template('#define {{ constant.name }} {{ constant.value }}').render(constant=self)

class GXHDefine(Define):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        return self.generator.get_template("""
//===========================================================================================================
//
// Define {{ define.name }}
//
// {% if define.doc %}{{ define.doc | doc_sanitize | comment }}{% endif %}
//
{%- for constant in define.constants %}
// {{ constant.name }}
// {% if constant.doc %}{{ constant.doc | doc_sanitize | comment }}{% endif %}
//
{%- endfor %}
//===========================================================================================================
{% for constant in define.constants %}
{{ constant.render() }}
{%- endfor %}

""").render(define=self)


class GXHParameter(Parameter):
    def __init__(self, other):
        super().construct_copy(other)


class GXHMethod(Method):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        return self.generator.get_template("""
//-----------------------------------------------------------------------------------------------------------
// {{ method.name }} {%if method.doc %}{{ method.doc | doc_sanitize | comment(extra_spaces=method.name|length+1) }}{% endif %}
{% if method.see_also %}//-----------------------------------------------------------------------------------------------------------
// See also
//
// {{ method.see_also | doc_sanitize | comment }}
//
{% endif %}{% if method.notes %}//-----------------------------------------------------------------------------------------------------------
// Notes
//
// {{ method.notes | doc_sanitize | comment }}
//
{% endif %}//-----------------------------------------------------------------------------------------------------------
""").render(method=self)



class GXHClass(Class):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        return self.generator.get_template("""
{{- cl.header -}}
{{- cl.gxh_definitions -}}
{{- cl.gxh_methods -}}
{{- cl.footer -}}
""").render(cl=self)

    @property
    def header(self):
        return self.generator.get_template("""
//===========================================================================================================
//
// Class {{ cl.name }}
//
//-----------------------------------------------------------------------------------------------------------
//
// {{ cl.doc | doc_sanitize | comment }}
//
{% if cl.notes %}//-----------------------------------------------------------------------------------------------------------
// Notes
//
// {{ cl.notes | doc_sanitize | comment }}
//
{% endif %}//-----------------------------------------------------------------------------------------------------------

#ifndef H{{ cl.name }}_GXH_DEFINED
#define H{{ cl.name }}_GXH_DEFINED

{% if cl.verbatim_gxh_defines %}{{ cl.verbatim_gxh_defines }}{% endif %}

""").render(cl=self)

    @property
    def footer(self):
        return self.generator.get_template('#endif').render(cl=self)

    @property
    def gxh_definitions(self):
        return self.generator.get_template("""
{% for _, define in cl.defines.items() %}
{{ define.render() }}
{% endfor %}
""").render(cl=self)

    @property
    def gxh_methods(self):
        if len(self.method_groups) == 1:
            method_group = next(iter(self.method_groups.values()))
            return self.render_method_group(method_group)
        else:
            return self.generator.get_template("""
{% for key, method_group in cl.method_groups.items() %}
//===========================================================================================================
//
// {{ key }}
//
//===========================================================================================================

{{ cl.render_method_group(method_group) }}
{% endfor %}
""").render(cl=self)

    def render_method_group(self, method_group):
        return self.generator.get_template("""
{% for method in methods %}
{{ method.render() }}
{% endfor %}
""").render(methods=method_group)

class GXHCodeGenerator(CodeGeneratorBase):
    def doc_sanitize(self, s):
        s = self.re_class.sub(r'\1', s)
        s = self.re_def.sub(r'\1', s)
        s = self.re_func.sub(r'\1', s)
        s = self.re_def_val.sub(r'\1', s)

        return textwrap.dedent(s).strip()

    def __init__(self):
        super().__init__(constant_type=GXHConstant, define_type=GXHDefine, parameter_type=GXHParameter,
                         method_type=GXHMethod, class_type=GXHClass)
        self._remove_no_gxh_classes_and_methods()
        self.j2env.filters['doc_sanitize'] = self.doc_sanitize

    def _remove_no_gxh_classes_and_methods(self):
        classes_to_remove = [ key for key, cl in self.classes.items() if cl.no_gxh ]
        for key in classes_to_remove:
            self.classes.pop(key, None)
        for _, cl in self.classes.items():
            for g_k, methods in cl.method_groups.items():
                cl.method_groups[g_k] = [m for m in methods if not m.no_gxh]
