import importlib
import glob
import os
import itertools

from .gxdefs import Type, Availability, Constant, Define
from .gxclass import Class
from .gxmethod import Parameter, Method


# Generate a dictionary of all classes with their methods and definitions as
# a module attribute

_core_files = glob.glob(os.path.join(os.path.dirname(__file__), 'core/*.py'))
_desk_files = glob.glob(os.path.join(os.path.dirname(__file__), 'desk/*.py'))

gx_classes = {}

for file in itertools.chain(_core_files, _desk_files):
    parts = file.replace('/', '.').replace('\\', '.').split('.')
    parts.pop()
    cl = parts.pop()
    branch = parts.pop()
    mod = importlib.import_module('.{}.{}'.format(branch, cl), __package__)

    gx_class = mod.gx_class

    gx_class.branch = branch # TODO Could move and document these as class properties

    gx_class.method_groups = mod.gx_methods if hasattr(mod, 'gx_methods') else {}
    gx_class.defines = mod.gx_defines if hasattr(mod, 'gx_defines') else []

    gx_classes[cl] = gx_class

