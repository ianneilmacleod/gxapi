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
               notes="""
               For Geosoft functions that do not return an error
               condition (all of them except those specifically designed
               for DLL use) you must call this function to test if an
               error has occured in the Geosoft function.  If an error
               has occured, just clean-up and return.  Error messages
               will have been registered by the Geosoft function.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if no errors.
               1 if an error has occured.
               """),

        Method('iCheckTerminate_SYS', module='geoengine.core', version='9.1.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Test if a Geosoft function has terminated with an error",
               notes="""
               Check if a script should be terminated. The reason for termination could
                                   be due to errors or due to calls like :func:`Cancel_SYS` or Exit_SYS.
               """,
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
               notes="""
               The :class:`VV` must be a memory based :class:`VV` for this method to work.
               
               Normal VVs are optimised to prevent thrashing, and to
               efficiently support many extremely large VVs, although
               there is a small performance penalty.
               This function is intended for :class:`VV`'s that you know can be
               handled by the operating system virtual memory manager,
               and will be used heavily.  By using a memory based :class:`VV`, you
               can achieve some performance improvements provided your
               application does not cause the memory manager to "thrash".
               
               External programs that use the GX API may prefer to use
               memory-based :class:`VV`'s because you can get direct access to
               the :class:`VV` through the :func:`GetPtrVV_GEO` function (see gx_extern.h).
               
               Note that you can only read and write to this memory up to
               the declared or current size of the :class:`VV`.  You should use the
               :func:`SetLen_VV` functions to change the size of a :class:`VV`, after which
               you should always call :func:`GetPtrVV_GEO` to determine the new base
               memory pointer.
               """,
               see_also=":func:`MakeMemBased_VV`",
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
               notes="""
               When this resource is destroyed, your
               function will be called and passed your
               pInfo pointer to cleanup.
               """,
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
               notes="This removes the tracking controls",
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

