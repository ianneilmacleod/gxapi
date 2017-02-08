from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GEO',
                 no_gxh=True,
                 no_csharp=True,
                 doc=":class:`GEO` Utility functions")





gx_methods = {
    'Miscellaneous': [

        Method('iCheckError_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Test if Geosoft function has terminated with an error",
               return_type=Type.INT32_T,
               return_doc="""
               0 if no errors.
               1 if an error has occured.
               """),

        Method('iCheckTerminate_SYS', module='geoengine.core', version='9.1.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Test if a Geosoft function has terminated with an error",
               return_type=Type.INT32_T,
               return_doc="""
               0 continue
               1 terminate
               """,
               parameters = [
                   Parameter('p1', type=Type.INT32_T, is_ref=True,
                             doc="Termination reason (0 = normal, -1 = cancel, 1 = error)")
               ]),

        Method('ShowError_GEO', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Shows any errors to stdout or to gui if gui app",
               return_type=Type.VOID),

        Method('sGetError_GEO', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Gets the error string for 1 error.",
               return_type="short",
               return_doc="""
               0 - no error
               1 - error found
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='1',
                             doc="Module name buffer (should be at least 64 bytes)"),
                   Parameter('p2', type=Type.INT32_T, is_val=True, default_length='STR_DEFAULT',
                             doc="Size of module name buffer"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Error buffer (should be at least 2048 bytes)"),
                   Parameter('p4', type=Type.INT32_T, is_val=True, default_length='STR_ERROR',
                             doc="Size of error buffer"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Error number")
               ]),

        Method('GetPtrVM_GEO', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Gets the pointer of a :class:`VM` object's data.",
               return_type="void*",
               return_doc="Pointer",
               parameters = [
                   Parameter('p1', type="VM",
                             doc=":class:`VM` object")
               ]),

        Method('GetPtrVV_GEO', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Gets the pointer of a :class:`VV` object's data.",
               return_type="void*",
               return_doc="Pointer to the base of the :class:`VV` memory image.",
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` object")
               ]),

        Method('pGetInternalGXXPointer_GEO', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Innternal use only.",
               return_type="void*",
               return_doc="Pointer.",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Handle of GXX resource")
               ]),

        Method('sCheckTerminate_GEO', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Check to see if terminate has been called by a wrapper.",
               return_type="short",
               return_doc="""
               0 - No
               1 - Yes
               """),

        Method('RegisterResourceTracking_GEO', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Register a Resource Tracking function",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Handle of resource to track"),
                   Parameter('p2', type="void*",
                             doc="pInfo handle to pass to destructor"),
                   Parameter('p3', type="void (_stdcall *param3)(void*)",
                             doc="Destructor function")
               ]),

        Method('UnregisterResourceTracking_GEO', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Unregister a Resource Tracking function",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Handle of resource to track"),
                   Parameter('p2', type="void*",
                             doc="pInfo handle to pass to destructor"),
                   Parameter('p3', type="void (_stdcall *param3)(void*)",
                             doc="Destructor function")
               ])
    ]
}

