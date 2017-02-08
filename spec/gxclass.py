import importlib
import glob
import os
import itertools
from enum import Enum

class Class:
    def __init__(self, name, handle_name=None, no_gxh=False, no_csharp=False, no_cpp=False,
                 doc=None, notes=None):
        self.name = name
        self.handle_name = handle_name
        self.no_gxh = no_gxh
        self.no_csharp = no_csharp
        self.no_cpp = no_cpp
        self.doc = doc
        self.notes = notes


