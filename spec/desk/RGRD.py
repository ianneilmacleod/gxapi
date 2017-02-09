from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('RGRD',
                 doc="""
                 The :class:`RGRD` object is used as a storage place for the control
                 parameters which the Rangrid (minimum curvature) program needs to execute. The
                 Run_RGRD function executes the Rangrid program using the :class:`RGRD` object.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('_Clear_RGRD', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Clears all the parameters in a :class:`RGRD` object",
               notes="DLL name :func:`_Clear_RGRD`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="RGRD",
                             doc=":class:`RGRD` object to clear")
               ]),

        Method('Create_RGRD', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create a handle to a Rangrid object",
               notes="""
               The Rangrid object is initially empty. It will store the
               control file parameters which the Rangrid program needs
               to execute. Use the LoadParms_RGRD method to get the
               control file parameters into the :class:`RGRD` object.
               """,
               return_type="RGRD",
               return_doc=":class:`RGRD` Object"),

        Method('CreateIMG_RGRD', module='geogxx', version='7.0.1',
               availability=Availability.EXTENSION, 
               doc="Run Rangrid directly on XYZ :class:`VV` data, output to an :class:`IMG`.",
               notes="""
               If the grid file name is defined, the :class:`IMG` is tied to a new output file.
               If the grid file name is not defined, the :class:`IMG` is memory-based; not
               tied to a file.
               """,
               return_type="IMG",
               return_doc=":class:`IMG` object",
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X data (any numeric :class:`VV` type)"),
                   Parameter('p2', type="VV",
                             doc="Y data (any numeric :class:`VV` type)"),
                   Parameter('p3', type="VV",
                             doc="Z (grid value) data (any numeric :class:`VV` type)"),
                   Parameter('p4', type="IPJ",
                             doc="Projection to apply to the output :class:`IMG`"),
                   Parameter('p5', type=Type.STRING,
                             doc="RANGRID control file."),
                   Parameter('p6', type=Type.STRING,
                             doc="output grid name (optional)")
               ]),

        Method('Destroy_RGRD', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`RGRD`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="RGRD",
                             doc=":class:`RGRD` to destroy.")
               ]),

        Method('iDefault_RGRD', module='geogxx', version='6.0.1',
               availability=Availability.EXTENSION, 
               doc="Set the defaults.",
               return_type=Type.INT32_T,
               return_doc="0 OK, 1 Error.",
               parameters = [
                   Parameter('p1', type="RGRD",
                             doc="Handle to :class:`RGRD` object (stores control parameters)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of Z Channel to perfrom gridding on"),
                   Parameter('p3', type="DAT",
                             doc="Handle to source :class:`DAT` object (from database)")
               ]),

        Method('iLoadParms_RGRD', module='geogxx', version='6.0.1',
               availability=Availability.EXTENSION, 
               doc="""
               Retrieves a Rangrid object's control parameters from a file,
               or sets the parameters to default if the file doesn't exist.
               """,
               notes="""
               If the control file name passed into this function is a file
               which does not exist, then the defaults for a Rangrid control
               file will be generated and put into the :class:`RGRD` object.
               Otherwise, the control file's settings are retrieved from
               the file and loaded into the :class:`RGRD` object.
               """,
               return_type=Type.INT32_T,
               return_doc="0 OK, 1 Error.",
               parameters = [
                   Parameter('p1', type="RGRD",
                             doc=":class:`RGRD` to load parameter settings into"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of file to get the parameter settings from")
               ]),

        Method('iRun_RGRD', module='geogxx', version='6.0.1',
               availability=Availability.EXTENSION, 
               doc="""
               Executes the Rangrid program, using the input channel and
               output file parameters.
               """,
               return_type=Type.INT32_T,
               return_doc="0 OK, 1 Error.",
               parameters = [
                   Parameter('p1', type="RGRD",
                             doc="Handle to :class:`RGRD` object (stores control parameters)"),
                   Parameter('p2', type="DAT",
                             doc="Handle to source :class:`DAT` object (from database)"),
                   Parameter('p3', type="DAT",
                             doc="Handle to output grid file :class:`DAT`")
               ]),

        Method('iRun2_RGRD', module='geogxx', version='6.0.1',
               availability=Availability.EXTENSION, 
               doc="Executes the Rangrid program directly on a database.",
               return_type=Type.INT32_T,
               return_doc="0, always.",
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
                             doc="RANGRID control file."),
                   Parameter('p6', type=Type.STRING,
                             doc="output grid name")
               ]),

        Method('iSaveParms_RGRD', module='geogxx', version='6.0.1',
               availability=Availability.EXTENSION, 
               doc="""
               Puts the Rangrid object's control parameters back into
               its control file.
               """,
               notes="""
               If the control file did not previously exist, it will be
               created. Otherwise, the old file will be overwritten.
               """,
               return_type=Type.INT32_T,
               return_doc="0 OK, 1 Error.",
               parameters = [
                   Parameter('p1', type="RGRD",
                             doc=":class:`RGRD` object to get parameters from and put into the control file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of file to put the parameter settings into")
               ]),

        Method('RunVV_RGRD', module='geogxx', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="Executes the Rangrid program directly on input data VVs.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X data"),
                   Parameter('p2', type="VV",
                             doc="Y data"),
                   Parameter('p3', type="VV",
                             doc="Z (grid value) data"),
                   Parameter('p4', type="IPJ",
                             doc="Projection to put into grid"),
                   Parameter('p5', type=Type.STRING,
                             doc="RANGRID control file."),
                   Parameter('p6', type=Type.STRING,
                             doc="output grid name")
               ])
    ]
}

