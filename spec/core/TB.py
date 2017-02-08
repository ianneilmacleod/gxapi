from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('TB',
                 doc="""
The :class:`TB` class is a high-performance table class used to
perform table-based processing, such as leveling data in
an OASIS database. The :class:`LTB` class is recommended for use
with small tables produced from short lists such as the
different geographic projections and their defining parameters.
""")


gx_defines = [
    Define('TB_SEARCH',
           doc=":class:`TB` Searching mode",
           constants=[
               Constant('TB_SEARCH_BINARY', value='0', type=Type.INT32_T,
                        doc="Random searches in a table.")                        ,
               Constant('TB_SEARCH_LINEAR', value='1', type=Type.INT32_T,
                        doc="Linear searches up or down a table (Default).")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('_SetSearchMode_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the search mode of a table.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`TB_SEARCH`")
               ]),

        Method('Create_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Loads a table into memory and return a table handle.",
               return_type="TB",
               return_doc=":class:`TB` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the table file to load")
               ]),

        Method('CreateDB_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a table from a database.",
               return_type="TB",
               return_doc=":class:`TB` Object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('CreateLTB_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a table from an :class:`LTB` database.",
               return_type="TB",
               return_doc=":class:`TB` Object",
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object")
               ]),

        Method('Destroy_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a table resource.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table Object to Destroy")
               ]),

        Method('Field_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a field handle.",
               return_type="TB_FIELD",
               return_doc="The handle to the field (must be present)",
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table"),
                   Parameter('p2', type=Type.STRING,
                             doc="Field name")
               ]),

        Method('GetString_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets a string value from a table element.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Row of element to Get"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Column of element to Get"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="returned string"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="maximum string size")
               ]),

        Method('iDataType_TB', module='geoengine.core', version='5.0.1',
               availability=Availability.PUBLIC, 
               doc="Returns the data type for the specified column.",
               return_type=Type.INT32_T,
               return_doc=":def:`DB_CATEGORY_CHAN`",
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Column of element to Get")
               ]),

        Method('IFindColByIndex_TB', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Finds a column's name by its index.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index of column to find"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Buffer for column name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of buffer")
               ]),

        Method('iFindColByName_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Finds a column's index by its name.",
               return_type=Type.INT32_T,
               return_doc="""
               Index of column.
               -1 if not found.
               """,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of column to find")
               ]),

        Method('iFormat_TB', module='geoengine.core', version='5.0.1',
               availability=Availability.PUBLIC, 
               doc="Returns the channel format for the specified column.",
               return_type=Type.INT32_T,
               return_doc=":def:`DB_CHAN_FORMAT`",
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Column of element to Get")
               ]),

        Method('iGetInt_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets an integer value from a table element.",
               return_type=Type.INT32_T,
               return_doc="Value",
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Row of element to Get"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Column of element to Get")
               ]),

        Method('iNumColumns_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the number of data fields (columns) in a table.",
               return_type=Type.INT32_T,
               return_doc="Number of columns",
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle")
               ]),

        Method('iNumRows_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the number of data rows in a table.",
               return_type=Type.INT32_T,
               return_doc="Number of rows",
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle")
               ]),

        Method('LoadDB_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Load a database into a :class:`TB`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="table"),
                   Parameter('p2', type="DB",
                             doc="database"),
                   Parameter('p3', type="DB_SYMB",
                             doc="line")
               ]),

        Method('rGetReal_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets an real value from a table element.",
               return_type=Type.DOUBLE,
               return_doc="Value",
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Row of element to Get"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Column of element to Get")
               ]),

        Method('Save_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Saves the data in a table to a file. The table header will be
               in ASCII and the data will be in BINARY format.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of File to save table into")
               ]),

        Method('SaveDB_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Save a :class:`TB` in a database line",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="table"),
                   Parameter('p2', type="DB",
                             doc="database"),
                   Parameter('p3', type="DB_SYMB",
                             doc="line")
               ]),

        Method('SaveToAscii_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Saves the data in a table to a file. The table header will be
               in ASCII and the data will be in ASCII format.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of File to save table into")
               ]),

        Method('SetInt_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets an integer value into a table element.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Row of element to set"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Column of element to set"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Value to set")
               ]),

        Method('SetReal_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets an real value into a table element.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Row of element to set"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Column of element to set"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Value to set")
               ]),

        Method('SetString_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets a string value into a table element.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc="Table handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Row of element to set"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Column of element to set"),
                   Parameter('p4', type=Type.STRING,
                             doc="Value to set")
               ]),

        Method('Sort_TB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sorts a table by a specified column.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TB",
                             doc=":class:`TB` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index of data Column to sort table by")
               ])
    ]
}

