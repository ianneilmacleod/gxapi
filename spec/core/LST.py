from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('LST',
                 doc="""
The :class:`LST` class is used to create and retrieve lists,
and to perform specific actions on lists, including
retrieving list items, sorting lists and adding or
removing list items.
""")


gx_defines = [
    Define('LST_ITEM',
           doc=":class:`LST` data access",
           constants=[
               Constant('LST_ITEM_NAME', value='0', type=Type.INT32_T,
                        doc='Access the "Name" part of the :class:`LST` item.')                        ,
               Constant('LST_ITEM_VALUE', value='1', type=Type.INT32_T,
                        doc='Access the "Value" part of the :class:`LST` item.')                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AddItem_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Adds an item to the end of the list.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the Item"),
                   Parameter('p3', type=Type.STRING,
                             doc="Value of the Item")
               ]),

        Method('AddSymbItem_LST', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Adds a channel/line/blob name and symbol to a list.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the channel, line or blob symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="symbol handle")
               ]),

        Method('AddUniqueItem_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Adds a unique item to the end of the list.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the Item"),
                   Parameter('p3', type=Type.STRING,
                             doc="Value of the Item")
               ]),

        Method('Append_LST', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Add the items in one list to another list.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="List to modify"),
                   Parameter('p2', type="LST",
                             doc="List to append to the above :class:`LST`.")
               ]),

        Method('AssayChannel_LST', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`LST` of assay channel mask strings from file.",
               return_type="LST",
               return_doc=":class:`LST` Object"),

        Method('Clear_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Clear a list object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle")
               ]),

        Method('ConvertFromCSVString_LST', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` with items from a string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` to add items to"),
                   Parameter('p2', type=Type.STRING,
                             doc="Comma separated items")
               ]),

        Method('Copy_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy one :class:`LST` object to another.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="Destination List to copy to"),
                   Parameter('p2', type="LST",
                             doc="Source List to Copy from")
               ]),

        Method('Create_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               creates a user controllable list. The list
               is empty when created.
               """,
               return_type="LST",
               return_doc="Handle to the List Object.",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Width of the list to make. This number should be large enough for both the item name and the item value.  Must be > 2 and <= 4096.")
               ]),

        Method('CreateS_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create :class:`LST` from serialized source.",
               return_type="LST",
               return_doc=":class:`LST` object",
               parameters = [
                   Parameter('p1', type="BF")
               ]),

        Method('DelItem_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Removes an item from the list. All items below
               it are shifted up one.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Item Number to Delete")
               ]),

        Method('Destroy_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys a list object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle")
               ]),

        Method('FindItems_LST', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Searches a :class:`LST` for items in a second :class:`LST`, returns indices of those found.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` in which to search"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LST_ITEM` data to do the search on"),
                   Parameter('p3', type="LST",
                             doc="Items to search for"),
                   Parameter('p4', type="VV",
                             doc=":def_val:`GS_LONG` :class:`VV` of returned indices into the first :class:`LST`.")
               ]),

        Method('GtItem_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This places the specified item into the buffer provided.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="List object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LST_ITEM` data to retrieve"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Item Number to Get"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Buffer to Place Item Into"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the Buffer")
               ]),

        Method('GtSymbItem_LST', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Returns a channel/line/blob name and symbol from a list.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Item number to get"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Buffer to Place Symbol name into"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Size of the buffer"),
                   Parameter('p5', type="var DB_SYMB", is_ref=True,
                             doc="Symbol handle")
               ]),

        Method('IConvertToCSVString_LST', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Load a string with names from a :class:`LST`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` to get items from"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Buffer to add items to"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of buffer")
               ]),

        Method('iFindItem_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Searches the list for a specified item.",
               return_type=Type.INT32_T,
               return_doc="""
               x  - Item Number
               -1 - Not Found
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LST_ITEM` data to do the search on"),
                   Parameter('p3', type=Type.STRING,
                             doc="String to Search For")
               ]),

        Method('iFindItemMask_LST', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Searches the list for a specified item, list contains masks.",
               return_type=Type.INT32_T,
               return_doc="""
               x  - Item Number
               -1 - Not Found
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LST_ITEM` data to search"),
                   Parameter('p3', type=Type.STRING,
                             doc="String to try :class:`LST` mask items on Search For")
               ]),

        Method('iGetInt_LST', module='geoengine.core', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get an integer item.",
               return_type=Type.INT32_T,
               return_doc="integer, :def_val:`iDUMMY` if conversion fails or string is empty.",
               parameters = [
                   Parameter('p1', type="LST",
                             doc="List object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LST_ITEM` data to retrieve"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Item Number to Get")
               ]),

        Method('InsertItem_LST', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Adds an item at a given location in the list.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Item index"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of the Item"),
                   Parameter('p4', type=Type.STRING,
                             doc="Value of the Item")
               ]),

        Method('iSize_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of items in the list.",
               return_type=Type.INT32_T,
               return_doc="x - Number of items in the list.",
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle")
               ]),

        Method('LoadCSV_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Load a list with data from a CSV file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="The CSV file"),
                   Parameter('p3', type=Type.STRING,
                             doc="column label for the item name"),
                   Parameter('p4', type=Type.STRING,
                             doc="column label for the item value")
               ]),

        Method('LoadFile_LST', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Set up a list from a list file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="name of the file")
               ]),

        Method('Resource_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Load a GX List Resource into this list object.  The
               entries are placed at the end of the list and are not
               sorted.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the Resource")
               ]),

        Method('rGetReal_LST', module='geoengine.core', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get a real item.",
               return_type=Type.DOUBLE,
               return_doc="real, :def_val:`rDUMMY` if conversion fails or string is empty.",
               parameters = [
                   Parameter('p1', type="LST",
                             doc="List object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LST_ITEM` data to retrieve"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Item Number to Get")
               ]),

        Method('SaveFile_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Save a list to a file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="name of the file")
               ]),

        Method('SelectCSVStringItems_LST', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`LST` with items from a second :class:`LST` found in a CSV string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` with items to select from"),
                   Parameter('p2', type=Type.STRING,
                             doc="Comma separated item names"),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` to add selected items to")
               ]),

        Method('Serial_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Serialize :class:`LST` to a :class:`BF`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST"),
                   Parameter('p2', type="BF")
               ]),

        Method('SetItem_LST', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Place an item at a specified point in the :class:`LST`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="List object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LST_ITEM` data to insert"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Item Number to Set"),
                   Parameter('p4', type=Type.STRING,
                             doc="Item to Set")
               ]),

        Method('Sort_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sorts a list.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LST_ITEM` data to sort on"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="0 - Ascending, 1 - Decending")
               ])
    ],
    'Obsolete': [

        Method('iLoadFile_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Set up a list from a list file.",
               return_type=Type.INT32_T,
               return_doc="Always returns 0",
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="name of the file")
               ]),

        Method('iLoadProj_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="""
               Sets up a list with datum codes and their associated
               descriptions read from a projection datum file.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="name of the projection datum file (*.DTM file)")
               ]),

        Method('iLoadProjCodes_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="""
               Sets up a list with datum codes read from a projection
               datum file.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="name of the projection datum file (*.DTM file)")
               ]),

        Method('MakeREG_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Make an :class:`LST` from a :class:`REG`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="group name in the reg"),
                   Parameter('p3', type="REG")
               ])
    ]
}

