from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('BIGRID',
                 doc="""
The Bigrid class is used to grid data using a optimized algorithm that
assumes data is collected in semi-straight lines.
""")





gx_methods = {
    'Miscellaneous': [

        Method('_Clear_BIGRID', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Clears all the parameters in a :class:`BIGRID` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BIGRID",
                             doc=":class:`BIGRID` object")
               ]),

        Method('Create_BIGRID', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create a handle to a Brigrid object",
               return_type="BIGRID",
               return_doc=":class:`BIGRID` Object"),

        Method('Destroy_BIGRID', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`BIGRID`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BIGRID",
                             doc=":class:`BIGRID` to destroy.")
               ]),

        Method('iLoadParms_BIGRID', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="""
               Retrieves a Bigrid object's control parameters from a file,
               or sets the parameters to default if the file doesn't exist.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type="BIGRID",
                             doc=":class:`BIGRID` to load parameter settings into"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of file to get the parameter settings from")
               ]),

        Method('iLoadWarp_BIGRID', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Load a warp projection.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type="BIGRID",
                             doc=":class:`BIGRID` to load parameter settings"),
                   Parameter('p2', type=Type.STRING,
                             doc="New grid title"),
                   Parameter('p3', type=Type.STRING,
                             doc="New grid cell size as a string, blank for default"),
                   Parameter('p4', type=Type.STRING,
                             doc="Warp projection file name")
               ]),

        Method('Run_BIGRID', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="""
               Executes the Bigrid program, using the input channel and
               output file parameters.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BIGRID",
                             doc="Handle to :class:`BIGRID` object (stores control parameters)"),
                   Parameter('p2', type=Type.STRING,
                             doc='not used, pass as ""'),
                   Parameter('p3', type="DAT",
                             doc="Handle to source :class:`DAT` object (from database)"),
                   Parameter('p4', type="DAT",
                             doc="Handle to output grid file :class:`DAT`")
               ]),

        Method('Run2_BIGRID', module='geogxx', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="""
               Executes the Bigrid program, using the input channel and
               output file parameters with a projection handle.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BIGRID",
                             doc="Handle to :class:`BIGRID` object (stores control parameters)"),
                   Parameter('p2', type=Type.STRING,
                             doc='not used, pass as ""'),
                   Parameter('p3', type="DAT",
                             doc="Handle to source :class:`DAT` object (from database)"),
                   Parameter('p4', type="DAT",
                             doc="Handle to output grid file :class:`DAT`"),
                   Parameter('p5', type="IPJ",
                             doc=":class:`IPJ` handle of the projection system")
               ]),

        Method('SaveParms_BIGRID', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="""
               Puts the Bigrid object's control parameters back into
               its control file.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BIGRID",
                             doc=":class:`BIGRID` object to get parameters from and put into the control file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of file to put the parameter settings into")
               ])
    ]
}

