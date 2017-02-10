from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('UNC',
                 doc="""
                 This library is not a class. Use the :class:`UNC` library functions
                 to work with Unicode characters and strings. Since version 6.2
                 all strings are represented internally in the the GX engine
                 as UTF-8. The character set concept was discarded as a way to
                 work with characters that does not fall within the normal
                 ASCII range 0x01-0x7F. The utilities here aids with any new
                 functionality that is now possible (e.g. an expanded symbol range
                 with TrueType fonts).
                 """)


gx_defines = [
    Define('UTF8',
           doc="UTF-8 Defines",
           constants=[
               Constant('UTF8_MAX_CHAR', value='5', type=Type.INT32_T,
                        doc="Maximum width of a single Unicode code point as a :def:`UTF8` string, including terminator (5)")                        
           ])]


gx_methods = {
    'UTF': [

        Method('iIsValidUTF16Char_UNC', module='geogxx', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Check if the UTF-16 value is a valid Unicode character code point.",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="UTF-16 value (32-bit int, lower 16 bits used, upper bits reserved for future use)")
               ]),

        Method('iValidSymbol_UNC', module='geogxx', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="See if a Symbol number is valid in a particular font.",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Face name (undecorated)"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Geosoft font? :def:`GEO_BOOL`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="symbol number")
               ]),

        Method('UTF16ValToSTR_UNC', module='geogxx', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Convert a UTF-16 value to a UTF-8 encoded string.",
               notes="An empty string will be returned for invalid symbols",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="UTF-16 value (32-bit int, lower 16 bits used, upper bits reserved for future use)"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Converted string"),
                   Parameter('p3', type=Type.INT32_T, default_length='UTF8_MAX_CHAR',
                             doc=":def:`UTF8` Size of string.")
               ]),

        Method('ValidateSymbols_UNC', module='geogxx', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="""
               High performance method to see if a set of symbols
               are valid in a particular font.
               """,
               notes="Invalid symbols in the :class:`VV` will be set to -1 by this call. :class:`VV` has to be of type :def_val:`GS_LONG`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` of symbols"),
                   Parameter('p2', type=Type.STRING,
                             doc="Face name (undecorated)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Geosoft font? :def:`GEO_BOOL`")
               ])
    ],
    'Miscellaneous': [

    ]
}

