from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VM',
                 doc="""
                 In-memory vector data methods
                 The :class:`VM` class will store vector (array) data in a memory buffer which
                 can be accessed using the :class:`VM` methods.
                 The main use for the :class:`VM` class is to store data in a single physical
                 memory location.  This memory can then be accessed by a user DLL using
                 the :func:`GetPtrVM_GEO` function defined in gx_extern.h.
                 :class:`VM` memory can be any size, but a :class:`VM` is intended for handling relatively
                 small sets of data compared to a :class:`VV`, which can work efficiently with
                 very large volumes of data.  The acceptable maximum :class:`VM` size depends on
                 the operating system and the performance requirements of an application.
                 The best performance is achieved when all :class:`VM` memory can be stored
                 comfortably within the the available system RAM.  If all :class:`VM` memory
                 will not fit in the system RAM, the operating system virtual memory
                 manager will be used to swap memory to the operations systems virtual
                 memory paging file.  Note that the operating system virtual memory
                 manager is much slower than the manager used by Geosoft when working with
                 very large arrays in a :class:`VV`.
                 
                 See :class:`VV` for methods to move data between a :class:`VM` and a :class:`VV`.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Create_VM', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`VM`.",
               notes="The :class:`VM` elements are initialized to dummies.",
               return_type="VM",
               return_doc=":class:`VM` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`GEO_VAR`"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":class:`VM` length (less than 16777215)")
               ]),

        Method('CreateExt_VM', module='geoengine.core', version='6.4.2',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`VM`, using one of the :def:`GS_TYPES` special data types.",
               notes="The :class:`VM` elements are initialized to dummies.",
               return_type="VM",
               return_doc=":class:`VM` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":class:`VM` length (less than 16777215)")
               ]),

        Method('Destroy_VM', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`VM`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VM",
                             doc=":class:`VM` to destroy.")
               ]),

        Method('iGetInt_VM', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get an integer element from a :class:`VM`.",
               return_type=Type.INT32_T,
               return_doc="""
               Element wanted, or :def_val:`iDUMMY`
               if the value is dummy or outside of the range of data.
               """,
               parameters = [
                   Parameter('p1', type="VM"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="element wanted")
               ]),

        Method('IGetString_VM', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a string element from a :class:`VM`.",
               notes="""
               Returns element wanted, or blank string
               if the value is dummy or outside of the range of data.
               
               Type conversions are performed if necessary.  Dummy values
               are converted to "*" string.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VM"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="element wanted"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="string in which to place element"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="maximum length of the string")
               ]),

        Method('iLength_VM', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns current :class:`VM` length.",
               return_type=Type.INT32_T,
               return_doc="# of elements in the :class:`VM`.",
               parameters = [
                   Parameter('p1', type="VM")
               ]),

        Method('ReSize_VM', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Re-set the size of a :class:`VM`.",
               notes="If increasing the :class:`VM` size, new elements are set to dummies.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VM",
                             doc=":class:`VM` to resize"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="new size (number of elements)")
               ]),

        Method('rGetReal_VM', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a real element from a :class:`VM`.",
               return_type=Type.DOUBLE,
               return_doc="""
               Element wanted, or :def_val:`rDUMMY`
               if the value is dummy or outside of the range of data.
               """,
               parameters = [
                   Parameter('p1', type="VM"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="element wanted")
               ]),

        Method('SetInt_VM', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set an integer element in a :class:`VM`.",
               notes="""
               Element being set cannot be < 0.
               
               If the element is > current :class:`VM` length, the :class:`VM` length is
               increased.  Reallocating :class:`VM` lengths can lead to fragmented
               memory and should be avoided if possible.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VM"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="element to set"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="value to set")
               ]),

        Method('SetReal_VM', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a real element in a :class:`VM`.",
               notes="""
               Element being set cannot be < 0.
               
               If the element is > current :class:`VM` length, the :class:`VM` length is
               increased.  Reallocating :class:`VM` lengths can lead to fragmented
               memory and should be avoided if possible.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VM"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="element to set"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="value to set")
               ]),

        Method('SetString_VM', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a string element in a :class:`VM`.",
               notes="""
               Element being set cannot be < 0.
               
               If the element is > current :class:`VM` length, the :class:`VM` length is
               increased.  Reallocating :class:`VM` lengths can lead to fragmented
               memory and should be avoided if possible.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VM"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="element to set"),
                   Parameter('p3', type=Type.STRING,
                             doc="string to set")
               ])
    ]
}

