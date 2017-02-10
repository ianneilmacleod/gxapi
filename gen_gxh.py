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

def get_gxh_type(type):
    if type == Type.DOUBLE:
        return "real"
    elif type == Type.INT32_T:
        return "int"
    elif type == Type.STRING:
        return "string"
    else:
        if '0' <= type[0] and type[0] <= '9':
            return "H" + type
        else:
            return type


class GXHParameter(Parameter):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def gxh_type(self):
        if self.is_ref:
            return 'var {}'.format(get_gxh_type(self.type))
        else:
            return get_gxh_type(self.type)

    def render_gxh_doc(self, indent_spaces):
        if self.doc:
            return self.generator.get_template(
                '{% set type_len = param.gxh_type|length %}{{ param.doc | doc_sanitize | comment(comment_first_line=True) | indent(indent_spaces-type_len, True) | indent(indent_spaces+1) }}'
            ).render(param=self, indent_spaces=indent_spaces)
        else:
            return self.generator.get_template(
                '{% set type_len = param.gxh_type|length %}{{ "//" | indent(indent_spaces-type_len, True) }}').render(param=self, indent_spaces=indent_spaces)



class GXHMethod(Method):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        return self.generator.get_template("""{% set name_len = method.exposed_name|length %} {% set ret_len = method.gxh_return_type|length %} {% set avail_len = method.availability_prefix|length %}
//-----------------------------------------------------------------------------------------------------------
// {{ method.exposed_name }} {%if method.doc %}{{ method.doc | doc_sanitize | comment(extra_spaces=name_len+1) }}{% endif %}
{% if method.return_doc %}//
// Returns {{ ' ' * (name_len - 7) }}{{ method.return_doc | doc_sanitize | comment(extra_spaces=name_len+1) }}
{% endif %}{% if method.notes %}//
// Notes {{ ' ' * (name_len - 5) }}{{ method.notes | doc_sanitize | comment(extra_spaces=name_len+1) }}
{% endif %}{% if method.see_also %}//
// See also {{ ' ' * (name_len - 8) }}{{ method.see_also | doc_sanitize | comment(extra_spaces=name_len+1) }}
{% endif %}//
// Available {{ ' ' * (name_len - 9) }}{{ method.version }}
//-----------------------------------------------------------------------------------------------------------

{{ method.availability_prefix }} {{ method.gxh_return_type }} {{ method.exposed_name }}{{ method.render_parameters() | indent(avail_len+name_len + ret_len + 2) }}
{{ method.string_macro }}""").render(method=self)

    @property
    def exposed_name(self):
        if self.external_name:
            return self.external_name
        else:
            return self.name

    @property
    def string_macro(self):
        method_name = self.exposed_name
        param_replacements = {p.size_of_param: p.name for p in self.parameters if p.size_of_param}
        if len(param_replacements) > 0:

            if method_name.startswith('I') or method_name.startswith('_'):
                macro_name = method_name[1:]
            elif method_name.startswith('iI'):
                macro_name = 'i{}'.format(method_name[2:])
            elif method_name.startswith('Gt'):
                macro_name = 'Get{}'.format(method_name[2:])
            else:
                macro_name = '_{}'.format(method_name)
            macro_params = ''
            method_params = ''

            for param in self.parameters:
                if method_params:
                    method_params += ', '
                if param.name in param_replacements:
                    method_params += 'sizeof({})'.format(param_replacements[param.name])
                else:
                    if macro_params:
                        macro_params += ', '
                    macro_params += param.name
                    method_params += param.name
            return '#define {}({}) {}({})\n'.format(macro_name, macro_params, method_name, method_params)
        else:
            return ''

    def render_parameters(self):
        max_type_len = 0
        for param in self.parameters:
            max_type_len = max(max_type_len, len(param.gxh_type))
        return self.generator.get_template("""{% for param in parameters %}{% if loop.first %}({% else %} {% endif %}{{ param.gxh_type }}{% if not loop.last %}, {{ param.render_gxh_doc(max_type_len + 2) }}
{% else %});{{ param.render_gxh_doc(max_type_len + 2) }}{% endif %}{% else %}();{% endfor %}""").render(parameters=self.parameters, max_type_len=max_type_len)

    @property
    def gxh_return_type(self):
        return get_gxh_type(self.return_type)

    @property
    def availability_prefix(self):
        if self.availability == Availability.PUBLIC:
            prefix = 'public'
        elif self.availability == Availability.EXTENSION:
            prefix = 'extended'
        else:
            prefix = 'licensed'
        if self.is_app:
            prefix += '_app'
        return '[_{}]'.format(prefix)


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
