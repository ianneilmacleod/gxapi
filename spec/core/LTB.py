from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('LTB',
                 doc="""
An :class:`LTB` object is typically created from a CSV (comma-separated values)
file, and is a table of information that may be accessed by row
or column. The :class:`LTB` class is recommended for use with small tables
produced from short lists (of the order of 1000's or records) such
as the different geographic projections and their defining parameters.
Large tables, such as those required for table-lookup functions, should
be accessed using the :class:`TB` class.
""",
                 notes="""
An :class:`LTB` ASCII table file has the following structure:

/ comments
key_name,col_1,col_2,col_3,etc...    /field names
key_1,token,token,token,etc...       /data lines
key_2,token,token,token,etc...
etc...

The first column must be the key column (all entries unique).

The header line is optional and can be used to find entries.

Comment and empty lines are ignored.
""")


gx_defines = [
    Define('LTB_CASE',
           doc="Case handling of :class:`LTB` strings",
           constants=[
               Constant('LTB_CASE_INSENSITIVE', value='0', type=Type.INT32_T,
                        doc="Ignore case")                        ,
               Constant('LTB_CASE_SENSITIVE', value='1', type=Type.INT32_T,
                        doc="Case is used")                        
           ]),

    Define('LTB_CONLST',
           doc="Matching types",
           constants=[
               Constant('LTB_CONLST_EXACT', value='0', type=Type.INT32_T)                        ,
               Constant('LTB_CONLST_ANY', value='1', type=Type.INT32_T)                        
           ]),

    Define('LTB_DELIM',
           doc="Types of :class:`LTB` Delimiters",
           constants=[
               Constant('LTB_DELIM_SPACE', value='0', type=Type.INT32_T,
                        doc="Spaces")                        ,
               Constant('LTB_DELIM_COMMA', value='1', type=Type.INT32_T,
                        doc="Commas")                        ,
               Constant('LTB_DELIM_SPACECOMMA', value='2', type=Type.INT32_T,
                        doc="Spaces and Commas")                        
           ]),

    Define('LTB_TYPE',
           doc="Types of :class:`LTB` Headers",
           constants=[
               Constant('LTB_TYPE_HEADER', value='0', type=Type.INT32_T,
                        doc="Has a header")                        ,
               Constant('LTB_TYPE_NOHEADER', value='1', type=Type.INT32_T,
                        doc="Has no header")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AddRecord_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a new record.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="key name"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="returned record number")
               ]),

        Method('Contract_LTB', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Contract the contents of two same-key and same-fields tables.",
               return_type="LTB",
               return_doc="""
               x    - Handle to :class:`LTB` object
               NULL - Error of some kind
               """,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc="Master :class:`LTB`"),
                   Parameter('p2', type="LTB",
                             doc="Contract :class:`LTB`")
               ]),

        Method('Create_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates a :class:`LTB` object from a file.",
               return_type="LTB",
               return_doc="""
               x    - Handle to :class:`LTB` object
               NULL - Error of some kind
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="file name, .csv assumed, searched locally then in :class:`GEOSOFT`."),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LTB_TYPE`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`LTB_DELIM`"),
                   Parameter('p4', type=Type.STRING,
                             doc='Key to find if only one record required, "" to read entire table.')
               ]),

        Method('CreateCrypt_LTB', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Creates a :class:`LTB` object from an encrypted file.",
               return_type="LTB",
               return_doc="""
               x    - Handle to :class:`LTB` object
               NULL - Error of some kind
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="file name, .csv assumed, searched locally then in :class:`GEOSOFT`."),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LTB_TYPE`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`LTB_DELIM`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`LTB_CASE`"),
                   Parameter('p5', type=Type.STRING,
                             doc='Key to find if only one record required, "" to read entire table.'),
                   Parameter('p6', type=Type.STRING,
                             doc="Decryption Key :def:`SYS_CRYPT_KEY`")
               ]),

        Method('CreateEx_LTB', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="Creates a :class:`LTB` object from a file.",
               return_type="LTB",
               return_doc="""
               x    - Handle to :class:`LTB` object
               NULL - Error of some kind
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="file name, .csv assumed, searched locally then in :class:`GEOSOFT`."),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LTB_TYPE`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`LTB_DELIM`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`LTB_CASE`"),
                   Parameter('p5', type=Type.STRING,
                             doc='Key to find if only one record required, "" to read entire table.')
               ]),

        Method('DeleteRecord_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete a record.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="record number to delete")
               ]),

        Method('Destroy_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object to destroy")
               ]),

        Method('GetConLST_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Populate a :class:`LST` with :class:`LTB` names from matching fields.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="field"),
                   Parameter('p3', type=Type.STRING,
                             doc="string to match to field, must be lower-case"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`LTB_CONLST`"),
                   Parameter('p5', type="LST",
                             doc="list to populate")
               ]),

        Method('GetLST_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Populate an :class:`LST` with :class:`LTB` names",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="field to get, 0 for key field"),
                   Parameter('p3', type="LST",
                             doc="list to populate")
               ]),

        Method('GetLST2_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Populate an :class:`LST` with :class:`LTB` names and values",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="field for names, 0 for key field"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="field for values, 0 for key field"),
                   Parameter('p4', type="LST",
                             doc="list to populate")
               ]),

        Method('iFields_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get number of fields.",
               return_type=Type.INT32_T,
               return_doc="number of fields in the :class:`LTB`.",
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object")
               ]),

        Method('iFindField_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the field number for the specified field.",
               return_type=Type.INT32_T,
               return_doc="""
               -1 if field does not exist.
               field number if field does exist.
               """,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="field name")
               ]),

        Method('iFindKey_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the key index of a record.",
               return_type=Type.INT32_T,
               return_doc="""
               -1 if key does not exist.
               record number if key does exist.
               """,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="key name")
               ]),

        Method('IGetField_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a field name by index.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="field number"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="returned field name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="maximum field name string length")
               ]),

        Method('iGetInt_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a int entry from the :class:`LTB`",
               return_type=Type.INT32_T,
               return_doc="""
               If the record or field are out of range,
               an empty string or dummy value is returned.
               """,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="record number"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="field number")
               ]),

        Method('IGetString_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get an entry from the :class:`LTB`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="record number"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="field number"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="returned field token"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="maximum field token string length")
               ]),

        Method('IGetEnglishString_LTB', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the English entry from the :class:`LTB`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="record number"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="field number"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="returned field token"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="maximum field token string length")
               ]),

        Method('iRecords_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get number of records in :class:`LTB`.",
               return_type=Type.INT32_T,
               return_doc="number of records in the :class:`LTB`.",
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object")
               ]),

        Method('iSearch_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Search for a record containing field value",
               return_type=Type.INT32_T,
               return_doc="""
               -1 if search failed.
               record number if search succeeds
               """,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="search start record"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="field number"),
                   Parameter('p4', type=Type.STRING,
                             doc="search string (case sensitive)")
               ]),

        Method('Merge_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Merge the contents of two same-key tables.",
               return_type="LTB",
               return_doc="""
               x    - Handle to :class:`LTB` object
               NULL - Error of some kind
               """,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc="Master :class:`LTB`"),
                   Parameter('p2', type="LTB",
                             doc="Child :class:`LTB`")
               ]),

        Method('rGetReal_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a real entry from the :class:`LTB`",
               return_type=Type.DOUBLE,
               return_doc="""
               If the record or field are out of range,
               an empty string or dummy value is returned.
               """,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="record number"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="field number")
               ]),

        Method('Save_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Save :class:`LTB` changes to existing or new file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB"),
                   Parameter('p2', type=Type.STRING,
                             doc='file name, .csv assumed.  If "", save to original file.')
               ]),

        Method('SaveCrypt_LTB', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Save :class:`LTB` to a new file using encryption",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB"),
                   Parameter('p2', type=Type.STRING,
                             doc='file name, .csv assumed.  If "", save to original file.'),
                   Parameter('p3', type=Type.STRING,
                             doc="encryption key  :def:`SYS_CRYPT_KEY`")
               ]),

        Method('SetInt_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a long entry",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="record number"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="field number"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="entry")
               ]),

        Method('SetReal_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a double entry",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="record number"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="field number"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="entry")
               ]),

        Method('SetString_LTB', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set an entry",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LTB",
                             doc=":class:`LTB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="record number"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="field number"),
                   Parameter('p4', type=Type.STRING,
                             doc="entry")
               ])
    ]
}

