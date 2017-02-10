from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('REG',
                 doc="""
                 The :class:`REG` class is used for storing and retrieving named
                 variables. Many classes contain :class:`REG` objects for storing
                 information particular to the class.  The :class:`META` class supersedes
                 the :class:`REG` class and is gradually replacing the use of the
                 :class:`REG` class in newer applications.
                 """,
                 verbatim_gxh_defines="#define GetString_REG(A,B,C) Get_REG(A,B,C,sizeof(C))")


gx_defines = [
    Define('REG_MERGE',
           doc=":class:`REG` merge options",
           constants=[
               Constant('REG_MERGE_REPLACE', value='0', type=Type.INT32_T,
                        doc="Replace Values")                        ,
               Constant('REG_MERGE_ADD', value='1', type=Type.INT32_T,
                        doc="Only append values")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Clear_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Clears all the parameters in a :class:`REG` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc=":class:`REG` object")
               ]),

        Method('Copy_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc="destination"),
                   Parameter('p2', type="REG",
                             doc="source")
               ]),

        Method('Create_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a handle to a :class:`REG` object",
               return_type="REG",
               return_doc=":class:`REG` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc='maximum size of "parameter=setting" string.')
               ]),

        Method('CreateS_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a handle to a :class:`REG` object from a :class:`BF`",
               return_type="REG",
               return_doc=":class:`REG` Object",
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle for file containing serialized :class:`REG`")
               ]),

        Method('Destroy_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`REG`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc=":class:`REG` to destroy.")
               ]),

        Method('Get_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets a string for a specified parameter in the :class:`REG` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc="Handle to :class:`REG` object (stores control parameters)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the parameter"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="String to get"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Length of destination string")
               ]),

        Method('GetInt_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets an int for a specified parameter in the :class:`REG` object",
               notes="If parameter is not present in :class:`REG`, :def_val:`iDUMMY` is returned.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc="Handle to :class:`REG` object (stores control parameters)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the parameter"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Int to get")
               ]),

        Method('GetOne_REG', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Gets n-th entry of the :class:`REG` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc="Handle to :class:`REG` object (stores control parameters)"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="sequential number of :class:`REG` entry"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="String to put parameter name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of parameter String"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='p6',
                             doc="String to put data into."),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of Data String")
               ]),

        Method('GetReal_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets an real for a specified parameter in the :class:`REG` object",
               notes="If parameter is not present in :class:`REG`, :def_val:`rDUMMY` is returned.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc="Handle to :class:`REG` object (stores control parameters)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the parameter"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Real to get")
               ]),

        Method('iEntries_REG', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Get the number of parms in a :class:`REG` object",
               return_type=Type.INT32_T,
               return_doc="Number of parms in a :class:`REG` object.",
               parameters = [
                   Parameter('p1', type="REG",
                             doc=":class:`REG` object")
               ]),

        Method('LoadINI_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Load a registry from an INI file.",
               notes='Items are loaded into the :class:`REG` in the format "GROUP.ITEM".',
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG"),
                   Parameter('p2', type=Type.STRING,
                             doc="INI file name")
               ]),

        Method('MatchString_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Replace a string with reg settings.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc="Handle to :class:`REG` object (stores control parameters)"),
                   Parameter('p2', type=Type.STRING,
                             doc="String to Replace"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Output Buffer"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the Output Buffer")
               ]),

        Method('Merge_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Merge",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc="destination"),
                   Parameter('p2', type="REG",
                             doc="source"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`REG_MERGE`")
               ]),

        Method('SaveINI_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Save a :class:`REG` to an INI file.",
               notes="""
               Only :class:`REG` parameters in the form "GROUP.ITEM" are
               dumped to the INI file, because they match the INI format
               which groups items under [GROUP] headings.
               Single-word items (without a separating period) are skipped.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG"),
                   Parameter('p2', type=Type.STRING,
                             doc="INI file name")
               ]),

        Method('Serial_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Serialize a :class:`REG` object into a file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc=":class:`REG` object"),
                   Parameter('p2', type="BF",
                             doc=":class:`BF` to serialize :class:`REG` into")
               ]),

        Method('Set_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets a string parameter in the :class:`REG` object",
               notes="""
               To remove a parameter completely, use one of the
               following:
               
               :func:`SetInt_REG`(Reg, sParam, :def_val:`iDUMMY`);
               or
               :func:`SetReal_REG`(Reg, sParam, :def_val:`rDUMMY`);
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc="Handle to :class:`REG` object (stores control parameters)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the parameter"),
                   Parameter('p3', type=Type.STRING,
                             doc="String to set it to An empty string sets the setting to an empty string, but does NOT remove the parameter from the :class:`REG`.")
               ]),

        Method('SetInt_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets an int for a specified parameter in the :class:`REG` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc="Handle to :class:`REG` object (stores control parameters)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the parameter"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Int to set, :def_val:`iDUMMY` to remove the parameter")
               ]),

        Method('SetReal_REG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets an real for a specified parameter in the :class:`REG` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc="Handle to :class:`REG` object (stores control parameters)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the parameter"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Real to set, :def_val:`rDUMMY` to remove the parameter")
               ])
    ]
}

