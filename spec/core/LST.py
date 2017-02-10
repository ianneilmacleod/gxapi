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
               notes="""
               A number of :class:`DB` functions return LSTs with the channel
               or line name in the "Name" part of a :class:`LST`, and the
               handle (DB_SYMB) in the value part. This function lets
               you quickly add a new item without the need of coverting
               the handle into a string value.
               """,
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
               notes="Existing items that match the name are first removed.",
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
               notes="""
               Item names and values are added using ":func:`AddUniqueItem_LST`",
               so that existing items with the same name are replaced, and if
               items are duplicated in the appended :class:`LST`, the last one will be
               the one to remain after the process is complete.
               """,
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
               notes="""
               Searches the local directory, then user\\etc, then \\etc to see
               if the file "assaylist.csv" exists.
               The file contains strings of those channel names which are
               to be interpreted as assay channels for geochemical processes.
               Items can be on the same line, separated by commas, or on
               separate lines (and combinations of both).
               If this function is used in combination with the lFindItemMask_LST
               function, then you can use mask-strings such as "*ppm"
               The following is a sample file:
               
               *ppm, *(ppm), *PPM, *(PPM), FeCl, MnO2
               "Fe %"
               FeO
               
               If the file is not found, or if no items are parsed, the list
               is returned with zero size.
               
               See the "assaylist.csv" file in the oasismontaj\\etc directory
               for more details.
               """,
               see_also=":func:`iFindItemMask_LST`",
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
               notes="""
               Items in the input buffer must be separated with
               commas.
               Both the Name and Value in the list are set to the
               item.
               """,
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
               notes="""
               This is a much more efficient way of determining if items in
               one :class:`LST` are found in a second, than by calling :func:`iFindItem_LST`
               repeatedly in a loop.
               The returned INT :class:`VV` contains the same number of items as
               the "search items" :class:`LST`, and contains -1 for items where the
               value is not found, and the index of items that are found.
               Comparisons are case-tolerant.
               """,
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
               notes='If item number is not in the list, the buffer will be "".',
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="List object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`LST_ITEM` data to retrieve"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Item Number to Get"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="Buffer to Place Item Into"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the Buffer")
               ]),

        Method('GtSymbItem_LST', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Returns a channel/line/blob name and symbol from a list.",
               notes="""
               A number of :class:`DB` functions return LSTs with the channel
               or line name in the "Name" part of a :class:`LST`, and the
               handle (DB_SYMB) in the value part. This function lets
               you quickly retrieve both the name and symbol handle
               for a given item, which needing to convert between types.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Item number to get"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Buffer to Place Symbol name into"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Size of the buffer"),
                   Parameter('p5', type="var DB_SYMB", is_ref=True,
                             doc="Symbol handle")
               ]),

        Method('IConvertToCSVString_LST', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Load a string with names from a :class:`LST`.",
               notes="""
               The list name values are put into a string,
               items separated by commas.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` to get items from"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Buffer to add items to"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of buffer")
               ]),

        Method('iFindItem_LST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Searches the list for a specified item.",
               notes="Comparisons are case-tolerant.",
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
               notes="""
               Comparsions are case-intolerant (unlike :func:`iFindItem_LST`).
               This means items in the list such as "*(ppm)" will be
               found if the input search string is "Ni (ppm)" or "Ni(ppm)",
               but not if it is "Ni (PPM)", so you should include
               both "*ppm*" and "*PPM*".
               
               It is NOT the input string that should be the mask, but
               the :class:`LST` items themselves
               
               This function was designed originally for geochemical
               processes in order to identify if a given channel name
               indicates that the channel should be given the "Assay" class.
               """,
               see_also=":func:`AssayChannel_LST`",
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
               notes="""
               Index must be 0 >= index >= list size.
               Items above the list index are shifted up one index value.
               """,
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
               notes="""
               Both the Item and Value fields must be specified.
               The CSV file must be comma delimited, and have
               a header line with the field names.
               Leading and trailing spaces are removed in the names and values.
               """,
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
               notes="""
               A list file is an ASCII file that contains list entries.
               Each line for the file contains a list item name and an
               optional list item value.  The name and value must be
               delimited by a space, tab or comma.
               If the item name or value contains spaces, tabs or commas,
               it must be contined in quotes.
               blank lines and lines that begin with a '/' character are
               ignored.
               
               The default extension is .lst.  If the file cannot
               be found in the local directory, the :class:`GEOSOFT`\\etc directory
               is searched.
               If it cannot be found, the list will be
               empty.  Not finding a file is not an error.
               
               This function replaces the :func:`iLoadFile_LST` function which
               actually always returned 0, or terminated on an error.
               """,
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
               notes="""
               A list file is an ASCII file that contains list entries.
               Each line for the file contains a list item name and an
               optional list item value.  The name and value must be
               delimited by a space, tab or comma.
               If the item name or value contains spaces, tabs or commas,
               it must be contined in quotes.
               blank lines and lines that begin with a '/' character are
               ignored.
               
               The default extension is .lst.  If the file has a full path
               it will be created as specified.  Otherwise we look for the
               file in the local then the :class:`GEOSOFT`\\etc directory.  If the file
               does not exist it will be created in the :class:`GEOSOFT`\\etc directory.
               """,
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
               notes="""
               Items in the input string must be separated with
               commas. Parsing uses the sCommaTokens_GS function.
               Both the name and value of the input :class:`LST` items whose
               name matches an item in the input string are
               copied to the output :class:`LST`.
               Items are copied in the same order they appear in the
               input string. Items in the string not found in the input :class:`LST`
               are ignored, and no error is registered.
               Item matches are case-tolerant.
               """,
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
               notes="The existing item at the given index will be replaced.",
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
               notes="""
               This function was made obsolete and replaced
               with the :func:`LoadFile_LST` function, because it
               in fact always returned 0. If an error occured
               the function terminates, it does NOT return a 1.
               
               Obsolete
               """,
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
               notes="""
               Was based on the old Mapproj.dtm file. Superceded by the current
               projection engine.
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
               notes="""
               Was based on the old Mapproj.dtm file. Superceded by the current
               projection engine.
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
               notes="Was not correctly implemented or used",
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

