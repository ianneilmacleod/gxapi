from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DAT',
                 doc="""
                 The :class:`DAT` object is used to access data from an variety of data sources
                 using the same access functions. The :class:`DAT` interface supports data access
                 on a point-by-point, of line-by-line basis.  For example,
                 the :func:`Run_BIGRID` function uses 2 :class:`DAT` objects - one :class:`DAT` associated with the
                 input data source, which is read line-by-line, and a second associated with
                 the output grid file output grid file.
                 
                 Use a specific :class:`DAT` creation method for an associated
                 information source in order to make a :class:`DAT` as required
                 by a specific processing function.  The gridding methods all use DATs.
                 """)


gx_defines = [
    Define('DAT_FILE',
           doc="Type of grid",
           constants=[
               Constant('DAT_FILE_GRID', value='1', type=Type.INT32_T)                        ,
               Constant('DAT_FILE_IMAGE', value='2', type=Type.INT32_T)                        
           ]),

    Define('DAT_FILE_FORM',
           doc="Type of form",
           constants=[
               Constant('DAT_FILE_FORM_OPEN', value='0', type=Type.INT32_T)                        ,
               Constant('DAT_FILE_FORM_SAVE', value='1', type=Type.INT32_T)                        
           ]),

    Define('DAT_XGD',
           doc=":class:`DAT` Open modes",
           constants=[
               Constant('DAT_XGD_READ', value='0', type=Type.INT32_T)                        ,
               Constant('DAT_XGD_NEW', value='1', type=Type.INT32_T)                        ,
               Constant('DAT_XGD_WRITE', value='2', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('CreateDB_DAT', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a handle to a database :class:`DAT` object",
               return_type="DAT",
               return_doc=":class:`DAT` Object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Handle to database which :class:`DAT` is connected with"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of X channel in database"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of Y channel in database"),
                   Parameter('p4', type=Type.STRING,
                             doc="Name of Z channel in database")
               ]),

        Method('CreateXGD_DAT', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a handle to a grid file :class:`DAT` object",
               return_type="DAT",
               return_doc=":class:`DAT` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of grid file to associate :class:`DAT` with"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DAT_XGD`")
               ]),

        Method('Destroy_DAT', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`DAT`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DAT",
                             doc=":class:`DAT` to destroy.")
               ]),

        Method('GetLST_DAT', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Put available :class:`DAT` filters and qualifiers in a :class:`LST`",
               notes="""
               The filters displayed in the Grid/Image file browse dialog are put
               in the "Name" of the :class:`LST`, while the file qualifiers are stored in
               the "Value".
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` object to populate"),
                   Parameter('p2', type=Type.STRING,
                             doc=':class:`DAT` interface name ("XGD" only support option currently)'),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DAT_FILE`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DAT_FILE_FORM`")
               ]),

        Method('RangeXYZ_DAT', module='geoengine.core', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="Determine the range in X, Y and Z in the :class:`DAT` source",
               notes="Terminates if unable to open an RPT :class:`DAT` interface.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DAT",
                             doc=":class:`DAT` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum X (:def_val:`rMAX` if none)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum Y (:def_val:`rMAX` if none)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum Z (:def_val:`rMAX` if none)"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum X (:def_val:`rMIN` if none)"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum Y (:def_val:`rMIN` if none)"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum Z (:def_val:`rMIN` if none)"),
                   Parameter('p8', type=Type.INT32_T, is_ref=True,
                             doc="Number of non-dummy XYZ.")
               ])
    ]
}

