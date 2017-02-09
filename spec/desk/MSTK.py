from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MSTK',
                 doc="""
                 Multi-profile stack
                 This class is used for storing data of multiple profiles and
                 plotting profiles in a map. It is a container of :class:`STK` class objects.
                 
                 See also:         :class:`STK` class.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('AddSTK_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create and add a :class:`STK` object to :class:`MSTK`",
               notes="Index to the added :class:`STK` object is the last one in :class:`MSTK` container.",
               return_type="STK",
               return_doc=":class:`STK`, fail if error",
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc="hMSTK")
               ]),

        Method('ChanListVV_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Save channel names in VVs based on channel types",
               notes="""
               Terms 'used' and 'unused' indicate that the a channel name
               in database also 'in' and 'not in' the :class:`MSTK` object respectively
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc=":class:`MSTK` object"),
                   Parameter('p2', type="DB",
                             doc="Database handle"),
                   Parameter('p3', type="VV",
                             doc="List of names of numeric channels"),
                   Parameter('p4', type="VV",
                             doc="List of name of string channels"),
                   Parameter('p5', type="VV",
                             doc="List of channel names which can be used for X axis. Must be numeric channels but not :class:`VA` channels"),
                   Parameter('p6', type="VV",
                             doc="List of profiles with channel names in both :class:`MSTK` and :class:`DB`"),
                   Parameter('p7', type="VV",
                             doc="List of profiles with channels in :class:`MSTK` but not in database")
               ]),

        Method('Create_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create :class:`MSTK`.",
               return_type="MSTK",
               return_doc=":class:`MSTK`, aborts if creation fails"),

        Method('Destroy_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`MSTK` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc=":class:`MSTK` Handle")
               ]),

        Method('DrawProfile_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw multiple profiles in map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc=":class:`MSTK` handle"),
                   Parameter('p2', type="DB",
                             doc="Database handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Database line"),
                   Parameter('p4', type="MAP",
                             doc=":class:`MAP` handle")
               ]),

        Method('SetYAxisDirection_MSTK', module='geogxx', version='8.3.0',
               availability=Availability.LICENSED, 
               doc="Set the Y-axis direction - normal or inverted",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc=":class:`MSTK` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Y-axis direction: 0 - normal, 1 - inverted")
               ]),

        Method('FindSTK2_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find index of :class:`STK` from a string of group names and X/Y channels",
               notes="""
               Format of the input string:
               
               Map group name + " ( " + X channel name + " , " + Y channel name + " )"
               
               for example, string "DATA ( DIST , MAG )"  indicates a map group name of DATA,
               X channel name of DIST and Y channel name of MAG.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc="hMSTK"),
                   Parameter('p2', type=Type.STRING,
                             doc="Input string (see notes above). Will be modified on return"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Index to the :class:`STK` found, Must be greater than 0 if found, -1 if not found"),
                   Parameter('p4', type="VV",
                             doc="Returned :class:`VV` with names of Group, X channel and Y channel :class:`VV` type must be of STRING")
               ]),

        Method('GetSTK_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Get a specific :class:`STK` object from a :class:`MSTK` object
               (Index of 0 gets the first :class:`STK` in the :class:`MSTK`)
               """,
               return_type="STK",
               return_doc="x     - :class:`STK` Object handle",
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc="Multi-Polygon Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index to :class:`STK` to get")
               ]),

        Method('IDelete_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Delete a :class:`STK` object",
               notes="0 is the first one",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc="hMSTK"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index to :class:`STK` to delete (0 is first one)")
               ]),

        Method('IFindSTK_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find index of :class:`STK` from a string of group names and X/Y channels",
               notes="""
               Format of the input string:
               
               Map group name + " ( " + X channel name + " , " + Y channel name + " )"
               
               for example, string "DATA ( DIST , MAG )"  indicates a map group name of DATA,
               X channel name of DIST and Y channel name of MAG.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc="hMSTK"),
                   Parameter('p2', type=Type.STRING,
                             doc="Input string (see notes above). Will be modified on return"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Index to the :class:`STK` found, Must be greater than 0 if found, -1 if not found"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="output group name string"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Group string length"),
                   Parameter('p6', type=Type.STRING, is_ref=True, size_of_param='6',
                             doc="output X channel name string"),
                   Parameter('p7', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="X string length"),
                   Parameter('p8', type=Type.STRING, is_ref=True, size_of_param='8',
                             doc="output Y channel name string"),
                   Parameter('p9', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Y string length")
               ]),

        Method('iGetNumSTK_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get the number of :class:`STK` objects in a :class:`MSTK` object",
               return_type=Type.INT32_T,
               return_doc="The number of :class:`STK` objects in a :class:`MSTK` object",
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc=":class:`MSTK` Object")
               ]),

        Method('ReadINI_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Read multiple profiles parameters from an INI file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc=":class:`MSTK` handle"),
                   Parameter('p2', type="RA",
                             doc=":class:`RA` handle to an INI file")
               ]),

        Method('SaveProfile_MSTK', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Save multiple profile INI parameters in a :class:`WA` file of INI format",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MSTK",
                             doc=":class:`MSTK` handle"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` handle to an INI file")
               ])
    ]
}

