from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('KGRD',
                 doc="""
                 The :class:`KGRD` object is used as a storage place for the control
                 parameters that the Krigrid program needs to execute. The
                 Run_KGRD function executes the Krigrid program using the
                 :class:`KGRD` object.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('_Clear_KGRD', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Clears all the parameters in a :class:`KGRD` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="KGRD",
                             doc=":class:`KGRD` object")
               ]),

        Method('Create_KGRD', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create a handle to a Krigrid object",
               notes="""
               The Krigrid object is initially empty. It will store the
               control file parameters which the Krigrid program needs
               to execute. Use the LoadParms_KGRD method to get the
               control file parameters into the :class:`KGRD` object.
               """,
               return_type="KGRD",
               return_doc=":class:`KGRD` Object"),

        Method('Destroy_KGRD', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`KGRD`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="KGRD",
                             doc=":class:`KGRD` to destroy.")
               ]),

        Method('iLoadParms_KGRD', module='geogxx', version='6.0.1',
               availability=Availability.EXTENSION, 
               doc="Retrieves a Krigrid object's control parameters from a file.",
               notes="""
               If the control file name passed into this function is a file
               which does not exist, then the defaults for a Krigrid control
               file will be generated and put into the :class:`KGRD` object.
               Otherwise, the control file's settings are retrieved from
               the file and loaded into the :class:`KGRD` object.
               """,
               return_type=Type.INT32_T,
               return_doc="0 OK, 1 Error.",
               parameters = [
                   Parameter('p1', type="KGRD",
                             doc=":class:`KGRD` to load parameter settings into"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of file to get the parameter settings from")
               ]),

        Method('iRun_KGRD', module='geogxx', version='6.0.1',
               availability=Availability.EXTENSION, 
               doc="""
               Executes the Krigrid program, using the input channel and
               output file parameters.
               """,
               return_type=Type.INT32_T,
               return_doc="0 OK, 1 Error.",
               parameters = [
                   Parameter('p1', type="KGRD",
                             doc="Handle to :class:`KGRD` object (stores control parameters)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of Z Channel to perfrom gridding on"),
                   Parameter('p3', type="DAT",
                             doc="Handle to source :class:`DAT` object (from database)"),
                   Parameter('p4', type="DAT",
                             doc="Handle to output grid file :class:`DAT`"),
                   Parameter('p5', type="DAT",
                             doc="Handle to output error grid file :class:`DAT` ((:class:`DAT`)0) if no error grid required"),
                   Parameter('p6', type=Type.STRING,
                             doc="Name of input variogram file"),
                   Parameter('p7', type=Type.STRING,
                             doc="Name of output variogram file"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Flag of variogram only"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Flag of input variogram"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Flag of output variogram")
               ]),

        Method('iRun2_KGRD', module='geogxx', version='6.0.1',
               availability=Availability.EXTENSION, 
               doc="Executes the Krigrid program directly on a database.",
               return_type=Type.INT32_T,
               return_doc="0 OK, 1 Error.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Handle to a database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Y Channel"),
                   Parameter('p3', type=Type.STRING,
                             doc="X Channel"),
                   Parameter('p4', type=Type.STRING,
                             doc="Data channel"),
                   Parameter('p5', type=Type.STRING,
                             doc="KRIGRID control file."),
                   Parameter('p6', type=Type.STRING,
                             doc="(output grid name (not required if variogram analysis only))"),
                   Parameter('p7', type=Type.STRING,
                             doc='(output error file, "" for none)'),
                   Parameter('p8', type=Type.STRING,
                             doc='(input variogram file, "" for none)'),
                   Parameter('p9', type=Type.STRING,
                             doc='(output variogram file, "" for none)'),
                   Parameter('p10', type=Type.INT32_T,
                             doc="1 if Variogram Analysis Only, other wise 0")
               ]),

        Method('iRun3_KGRD', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Executes the Krigrid program directly on a database and specifies the log file",
               return_type=Type.INT32_T,
               return_doc="0 OK, 1 Error.",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Handle to a database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Y Channel"),
                   Parameter('p3', type=Type.STRING,
                             doc="X Channel"),
                   Parameter('p4', type=Type.STRING,
                             doc="Data channel"),
                   Parameter('p5', type=Type.STRING,
                             doc="KRIGRID control file."),
                   Parameter('p6', type=Type.STRING,
                             doc="(output grid name (not required if variogram analysis only))"),
                   Parameter('p7', type=Type.STRING,
                             doc='(output error file, "" for none)'),
                   Parameter('p8', type=Type.STRING,
                             doc='(input variogram file, "" for none)'),
                   Parameter('p9', type=Type.STRING,
                             doc='(output variogram file, "" for none)'),
                   Parameter('p10', type=Type.STRING,
                             doc='(log file name, "" for default)'),
                   Parameter('p11', type=Type.INT32_T,
                             doc="1 if Variogram Analysis Only, other wise 0")
               ]),

        Method('iSaveParms_KGRD', module='geogxx', version='6.0.1',
               availability=Availability.EXTENSION, 
               doc="""
               Puts the Krigrid object's control parameters back into
               its control file.
               """,
               notes="""
               If the control file did not previously exist, it will be
               created. Otherwise, the old file will be overwritten.
               """,
               return_type=Type.INT32_T,
               return_doc="0 OK, 1 Error.",
               parameters = [
                   Parameter('p1', type="KGRD",
                             doc=":class:`KGRD` object to get parameters from and put into the control file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of file to put the parameter settings into")
               ])
    ]
}

