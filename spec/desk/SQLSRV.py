from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('SQLSRV',
                 doc="SQL Server and MSDE utility functions")


gx_defines = [
    Define('MFCSQL_DRIVER',
           doc="SQL Server Driver",
           constants=[
               Constant('MFCSQL_DRIVER_NOPROMPT', value='0', type=Type.INT32_T,
                        doc="No dialog box, Error if authentication parameters are wrong")                        ,
               Constant('MFCSQL_DRIVER_COMPLETE', value='1', type=Type.INT32_T,
                        doc="Only shows dialog box if authentication parameters are wrong")                        ,
               Constant('MFCSQL_DRIVER_PROMPT', value='2', type=Type.INT32_T,
                        doc="Always show dialog box, with option to change parameter")                        ,
               Constant('MFCSQL_DRIVER_COMPLETE_REQUIRED', value='3', type=Type.INT32_T,
                        doc="Same as :def_val:`MFCSQL_DRIVER_COMPLETE` except only missing parameters are editable")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('iAttachMDF_SQLSRV', module='geoguilib', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Attaches an MDF SQL server file to a server.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - :class:`DB` Operation Canceled
               Terminates on Error
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="SQL server to use"),
                   Parameter('p2', type=Type.STRING,
                             doc="User name (if blank assume NT Integrated Security)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Password"),
                   Parameter('p4', type=Type.STRING,
                             doc=":class:`DB` name"),
                   Parameter('p5', type=Type.STRING,
                             doc="MDF name"),
                   Parameter('p6', type=Type.STRING,
                             doc="LDF name (if blank, tries single db attach)")
               ]),

        Method('iDetachDB_SQLSRV', module='geoguilib', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Detaches a SQL Server database from a server.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - :class:`DB` Operation Canceled
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="SQL server to use"),
                   Parameter('p2', type=Type.STRING,
                             doc="User name (if blank assume NT Integrated Security)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Password"),
                   Parameter('p4', type=Type.STRING,
                             doc=":class:`DB` name")
               ]),

        Method('iGetDatabaseLanguagesLST_SQLSRV', module='geoguilib', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Get a list of the languages into :class:`LST`",
               return_type=Type.INT32_T,
               return_doc="Number of languages",
               parameters = [
                   Parameter('p1', type="LST"),
                   Parameter('p2', type=Type.STRING,
                             doc="SQL server to use"),
                   Parameter('p3', type=Type.STRING,
                             doc="User name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Password"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="0 - SQL authentication, 1 - NT integrated securty")
               ]),

        Method('iGetDatabasesLST_SQLSRV', module='geoguilib', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Get a list of the database into :class:`LST`",
               return_type=Type.INT32_T,
               return_doc="Number of database",
               parameters = [
                   Parameter('p1', type="LST"),
                   Parameter('p2', type=Type.STRING,
                             doc="SQL server to use"),
                   Parameter('p3', type=Type.STRING,
                             doc="User name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Password"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="0 - SQL authentication, 1 - NT integrated securty")
               ]),

        Method('IGetLoginGUI_SQLSRV', module='geoguilib', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Get/Test login information to SQL Server",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="SQL server to use"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="User name (default & returned)"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Length of User name"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Password (default & returned)"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Length of Password"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`MFCSQL_DRIVER`"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="Windows Authentication (default & returned)")
               ]),

        Method('iGetServersLST_SQLSRV', module='geoguilib', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Get a list of the visible servers into :class:`LST`",
               return_type=Type.INT32_T,
               return_doc="Number of servers",
               parameters = [
                   Parameter('p1', type="LST")
               ])
    ]
}

