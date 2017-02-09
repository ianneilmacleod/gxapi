from .gxdefs import SpecBase


class Class(SpecBase):
    def __init__(self, name, handle_name=None, no_gxh=False, no_csharp=False, no_cpp=False,
                 doc=None, notes=None, verbatim_gxh_defines=None):
        super().__init__()

        self.name = name
        self.handle_name = handle_name
        self.no_gxh = no_gxh
        self.no_csharp = no_csharp
        self.no_cpp = no_cpp
        self.doc = doc
        self.notes = notes
        self.verbatim_gxh_defines = verbatim_gxh_defines
