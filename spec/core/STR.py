from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('STR',
                 doc="""
                 This library is not a class. Use the :class:`STR` library functions
                 to work with and manipulate string variables. Since the
                 GX Programming Language does not provide string literal
                 tokens, you must use these functions for any string operations
                 you want to perform.
                 """,
                 verbatim_gxh_defines="""
#define iCharComp_STR(A,B) (iChar_STR(A)==iChar_STR(B))
#define iCharN_STR(A,B) IiCharN_STR(A,(B),sizeof(A))
""")


gx_defines = [
    Define('FILE_EXT',
           doc="Extension option",
           constants=[
               Constant('FILE_EXT_ADD_IF_NONE', value='0', type=Type.INT32_T,
                        doc="will add the extension only if no extension is present.")                        ,
               Constant('FILE_EXT_FORCE', value='1', type=Type.INT32_T,
                        doc="will cause a renaming of the file extension to the new extension.")                        
           ]),

    Define('STR_CASE',
           doc="Case sensitivity",
           constants=[
               Constant('STR_CASE_TOLERANT', value='0', type=Type.INT32_T)                        ,
               Constant('STR_CASE_SENSITIVE', value='1', type=Type.INT32_T)                        
           ]),

    Define('STR_ESCAPE',
           doc="How to handle escape",
           constants=[
               Constant('ESCAPE_CONVERT', value='0', type=Type.INT32_T,
                        doc="Converts non-standard characters in a string to escape sequences.")                        ,
               Constant('ESCAPE_REPLACE', value='1', type=Type.INT32_T,
                        doc="Replaces escape sequences with original characters.")                        
           ]),

    Define('STR_FILE_PART',
           doc="Parts of a path string",
           constants=[
               Constant('STR_FILE_PART_NAME', value='0', type=Type.INT32_T,
                        doc="File Name")                        ,
               Constant('STR_FILE_PART_EXTENSION', value='1', type=Type.INT32_T,
                        doc="Extension")                        ,
               Constant('STR_FILE_PART_DIRECTORY', value='2', type=Type.INT32_T,
                        doc="Directory")                        ,
               Constant('STR_FILE_PART_VOLUME', value='3', type=Type.INT32_T,
                        doc="Drive")                        ,
               Constant('STR_FILE_PART_QUALIFIERS', value='4', type=Type.INT32_T,
                        doc="Qualifiers")                        ,
               Constant('STR_FILE_PART_NAME_EXTENSION', value='5', type=Type.INT32_T,
                        doc="Name and the Extension together")                        ,
               Constant('STR_FILE_PART_FULLPATH_NO_QUALIFIERS', value='6', type=Type.INT32_T,
                        doc="Full name of file with no qualifiers")                        
           ]),

    Define('STR_JUSTIFY',
           doc="String justification style",
           constants=[
               Constant('STR_JUSTIFY_LEFT', value='0', type=Type.INT32_T)                        ,
               Constant('STR_JUSTIFY_CENTER', value='1', type=Type.INT32_T)                        ,
               Constant('STR_JUSTIFY_RIGHT', value='2', type=Type.INT32_T)                        
           ]),

    Define('STR_TRIM',
           doc="What to trim",
           constants=[
               Constant('STR_TRIMRIGHT', value='1', type=Type.INT32_T)                        ,
               Constant('STR_TRIMLEFT', value='2', type=Type.INT32_T)                        ,
               Constant('STR_TRIMBOTH', value='3', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Data Input': [

        Method('iScanI_STR', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Convert a string to a GX int.",
               return_type=Type.INT32_T,
               return_doc="Resulting Integer, :def_val:`iDUMMY` is bad integer",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="String to convert to an integer")
               ]),

        Method('rScanDate_STR', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Convert a date string to a GX real.",
               notes="OLD usage, use ScanForm_STR instead.",
               return_type=Type.DOUBLE,
               return_doc="Resulting Real, :def_val:`rDUMMY` if conversion fails.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Date string"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DATE_FORMAT`")
               ]),

        Method('rScanForm_STR', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Convert a formated string to a real.",
               return_type=Type.DOUBLE,
               return_doc="Resulting Real, :def_val:`rDUMMY` if conversion fails.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Date string"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GS_FORMATS`")
               ]),

        Method('rScanR_STR', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Convert a string to a GX real.",
               return_type=Type.DOUBLE,
               return_doc="Resulting Real, :def_val:`rDUMMY` if bad string.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="String to convert to a real")
               ]),

        Method('rScanTime_STR', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Convert a time string to a GX real.",
               notes="OLD usage, use ScanForm_STR instead.",
               return_type=Type.DOUBLE,
               return_doc="Resulting Real, :def_val:`rDUMMY` if conversion fails.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Date string"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`TIME_FORMAT`")
               ])
    ],
    'File Name': [

        Method('IFileCombineParts_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Combine file parts to build a file name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="drive"),
                   Parameter('p2', type=Type.STRING,
                             doc="directory"),
                   Parameter('p3', type=Type.STRING,
                             doc="name"),
                   Parameter('p4', type=Type.STRING,
                             doc="extension"),
                   Parameter('p5', type=Type.STRING,
                             doc="qualifiers"),
                   Parameter('p6', type=Type.STRING, is_ref=True, size_of_param='p7',
                             doc="destination string, can be same as input"),
                   Parameter('p7', type=Type.INT32_T, default_length='STR_FILE',
                             doc="string length")
               ]),

        Method('IFileExt_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a file extension onto a file name string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="file name to extend"),
                   Parameter('p2', type=Type.STRING,
                             doc="extension if \"\", extenstion and '.' are stripped."),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="extended file name (can be same as input)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`FILE_EXT`"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_FILE',
                             doc="length of buffer")
               ]),

        Method('IFileNamePart_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get part of a file name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="file name"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="destination string, can be same as input"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="string length"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`STR_FILE_PART`")
               ]),

        Method('IGetMFile_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the indexed filepath from a multiple filepath string",
               notes="""
               The multifile string must use '|' as a delimiter.
               Do not pass a string after calling :func:`iTokenize_STR`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="input multifile string"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="output filepath string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="sizeof output filepath string"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="index of file")
               ]),

        Method('IRemoveQualifiers_STR', module='geoengine.core', version='7.0.1',
               availability=Availability.PUBLIC, 
               doc="Remove file qualifiers from a file name",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="input file name"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="output file name (can be same as input)"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="length of buffer")
               ])
    ],
    'Formating': [

        Method('IFormatCRC_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a GX CRC value to a string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="CRC",
                             doc="CRC value to format"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Resulting string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Size of the Resulting String"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Width of the field")
               ]),

        Method('IFormatDate_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a GX real to a date string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="date value in decimal years to format"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Resulting string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Size of the Resulting String"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Width of the field"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DATE_FORMAT`")
               ]),

        Method('IFormatI_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a GX int to a string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="value to format"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Resulting string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Size of the Resulting String"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Width of the field")
               ]),

        Method('IFormatR_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a GX real to a string with significant digits.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="value to format"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Resulting string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Size of the Resulting String"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Width of the field"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Significant digits")
               ]),

        Method('IFormatR2_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a GX real to a string with given decimals.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="value to format"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Resulting string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Size of the Resulting String"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Width of the field"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Decimals")
               ]),

        Method('IFormatReal_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a GX real to a string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="value to format"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Resulting string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Size of the Resulting String"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`GS_FORMATS`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Width of the field"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Significant digits/decimals")
               ]),

        Method('IFormatTime_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a GX real to a time string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="time value in decimal hours to format"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Resulting string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Size of the Resulting String"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Width of the field"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Decimals to format with"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`TIME_FORMAT`")
               ])
    ],
    'General': [

        Method('_Escape_STR', module='geoengine.core', version='5.0.6',
               availability=Availability.PUBLIC, 
               doc="Convert/replace escape sequences in strings.",
               notes="""
               Escape characters:
               
               \\a      bell
               \\b      backspace
               \\f      formfeed
               \\n      new line
               \\r      carriage return
               \\t      tab
               \\v      vertical tab
               \\"      quote character
               \\x      take 'x' literally
               \\      backslash
               \\ooo    octal up to 3 characters
               \\xhh    hex up to 2 characters
               
               A common use of this function is to convert double-quote characters in
               a user unput string to \\" so the string can be placed in a tokenized
               string.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="string to modify"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="string size"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`STR_ESCAPE`")
               ]),

        Method('iChar_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the ASCII value of a character.",
               return_type=Type.INT32_T,
               return_doc="ASCII value of first character in string.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="string to return ascii value of first character")
               ]),

        Method('IiCharN_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the ASCII value of the n'th character.",
               return_type=Type.INT32_T,
               return_doc="""
               ASCII value of n'th character in string.
               The first character is 0.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING),
                   Parameter('p2', type=Type.INT32_T,
                             doc="character to get"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="maximum string length (unused)")
               ]),

        Method('IJustify_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Justify a string",
               notes="""
               If the string is too big to fit in the number of display characters,
               the output string will be "**" justified as specified.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="string to justify"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="result string, can be same as input"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="justification width"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`STR_JUSTIFY`"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="maximum size of result")
               ]),

        Method('IReplaceiMatchString_STR', module='geoengine.core', version='7.0.1',
               availability=Availability.PUBLIC, 
               doc="Replaces all occurances of match string by replacement string with case insensitive.",
               notes="""
               If the replacement string is "" (NULL character)
               then the string to replace is removed from the
               input string, and the string is shortened.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Destination String"),
                   Parameter('p2', type=Type.STRING,
                             doc="match string to replace"),
                   Parameter('p3', type=Type.STRING,
                             doc="replacement string"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="size of the Destination String")
               ]),

        Method('IReplaceMatchString_STR', module='geoengine.core', version='7.0.1',
               availability=Availability.PUBLIC, 
               doc="Replaces all occurances of match string by replacement string with case sensitive.",
               notes="""
               If the replacement string is "" (NULL character)
               then the string to replace is removed from the
               input string, and the string is shortened.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Destination String"),
                   Parameter('p2', type=Type.STRING,
                             doc="match string to replace"),
                   Parameter('p3', type=Type.STRING,
                             doc="replacement string"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="size of the Destination String")
               ]),

        Method('ISetCharN_STR', module='geoengine.core', version='5.1.4',
               availability=Availability.PUBLIC, 
               doc="Set the n'th character of a string using an ASCII value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="string"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="character to set"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="maximum string length"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="ASCII value")
               ]),

        Method('ISplitString_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Splits a string in two on a character.",
               notes="""
               The original string is modified by terminating it
               at the character split.
               
               The part of the string past the character split is
               copied to the split string.
               
               Split characters in quoted strings are ignored.
               
               This function is mainly intended to separate comments
               from control file strings.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="original string"),
                   Parameter('p2', type=Type.STRING,
                             doc="split character (first character of string)"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="split string past split character."),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="maximum length of split string.")
               ]),

        Method('IStrcat_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method contatinates a string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Destination String"),
                   Parameter('p2', type=Type.STRING,
                             doc="String to add"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the Destination String")
               ]),

        Method('iStrcmp_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method compares two strings and returns these values",
               return_type=Type.INT32_T,
               return_doc="""
               A  <  B           -1
               A ==  B            0
               A  >  B            1
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="string A"),
                   Parameter('p2', type=Type.STRING,
                             doc="string B"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`STR_CASE`")
               ]),

        Method('IStrcpy_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method copies a string into another string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="destination string"),
                   Parameter('p2', type=Type.STRING,
                             doc="origin string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="size of the destination string")
               ]),

        Method('iStriMask_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Case insensitive comparison of two strings.",
               notes="""
               Mask characters '*' - matches any one or more up to
               next character
               '?' - matches one character
               
               Test is case insensitive
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if string does not match mask.
               1 if string matches mask.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="mask"),
                   Parameter('p2', type=Type.STRING,
                             doc="string to test")
               ]),

        Method('IStrins_STR', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="This method inserts a string at a specified position.",
               notes="""
               If the specified position does not fall within the current string
               the source string will simply be Concatenated.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Destination String"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Insert Position"),
                   Parameter('p3', type=Type.STRING,
                             doc="String to add"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the Destination String")
               ]),

        Method('iStrlen_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the length of a string.",
               return_type=Type.INT32_T,
               return_doc="String length.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="string to find the length of")
               ]),

        Method('iStrMask_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Case sensitive comparison of two strings.",
               notes="""
               Mask characters '*' - matches any one or more up to
               next character
               '?' - matches one character
               
               Test is case sensitive
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if string does not match mask.
               1 if string matches mask.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="mask"),
                   Parameter('p2', type=Type.STRING,
                             doc="string to test")
               ]),

        Method('iStrMin_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Remove spaces and tabs and return length",
               notes="""
               String may be modified. This function should not be
               used to determine if a file name string is defined, because
               a valid file name can contain spaces, and once "tested" the
               name will be altered. Instead, use :func:`iStrMin2_STR`, or use
               :func:`iFileExist_SYS` to see if the file actually exists.
               """,
               return_type=Type.INT32_T,
               return_doc="String length.",
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="string to find the min length of")
               ]),

        Method('iStrMin2_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Length less spaces and tabs, string unchanged.",
               return_type=Type.INT32_T,
               return_doc="String length.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="string to find the min length of")
               ]),

        Method('iStrncmp_STR', module='geoengine.core', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Compares two strings to a given number of characters.",
               return_type=Type.INT32_T,
               return_doc="""
               A  <  B           -1
               A ==  B            0
               A  >  B            1
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="string A"),
                   Parameter('p2', type=Type.STRING,
                             doc="string B"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="number of characters to compare"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`STR_CASE`")
               ]),

        Method('iStrStr_STR', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Scan a string for the occurrence of a given substring.",
               return_type=Type.INT32_T,
               return_doc="""
               -1 if the substring does not occur in the string
               Index of first matching location if found
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="string to scan"),
                   Parameter('p2', type=Type.STRING,
                             doc="string to look for"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`STR_CASE`")
               ]),

        Method('ISubstr_STR', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Extract part of a string.",
               notes="""
               The destination string length will be less than the
               requested length if the substring is not fully enclosed
               in the origin string.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="destination string"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of output string buffer"),
                   Parameter('p3', type=Type.STRING,
                             doc="origin string"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="start location"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="number of characters")
               ]),

        Method('IToLower_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a string to lower case.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="String"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Maximum Size")
               ]),

        Method('IToUpper_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a string to upper case.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="String"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Maximum Size")
               ]),

        Method('IXYZLine_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Make a valid XYZ line name from a valid :class:`DB` line name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="line name to convert"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="buffer to hold new line name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="length of buffer")
               ]),

        Method('MakeAlpha_STR', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Turns all non alpha-numeric characters into an _.",
               notes="THE STRING IS MODIFIED.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="String to trim")
               ]),

        Method('Printf_STR', module='geoengine.core', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="Variable Argument PrintF function",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="destination string"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="size of the destination string"),
                   Parameter('p3', type=Type.STRING,
                             doc="pattern string")
               ]),

        Method('ReplaceChar_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Replaces characters in a string.",
               notes="""
               If the input replacement character is "", then the
               string will be truncated at the first character to replace.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="string to modify"),
                   Parameter('p2', type=Type.STRING,
                             doc="character to replace (first character only)"),
                   Parameter('p3', type=Type.STRING,
                             doc="replacement character (first character only)")
               ]),

        Method('ReplaceChar2_STR', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Replaces characters in a string, supports simple removal.",
               notes="""
               If the replacement character is "" (NULL character)
               then the character to replace is removed from the
               input string, and the string is shortened.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="string to modify"),
                   Parameter('p2', type=Type.STRING,
                             doc="character to replace (first character only)"),
                   Parameter('p3', type=Type.STRING,
                             doc="replacement character (first character only)")
               ]),

        Method('ReplaceMultiChar_STR', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Replaces multiple characters in a string.",
               notes="""
               The number of characters to replace must equal
               the number of replacement characters.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="string to modify"),
                   Parameter('p2', type=Type.STRING,
                             doc="characters to replace"),
                   Parameter('p3', type=Type.STRING,
                             doc="replacement characters")
               ]),

        Method('ReplaceNonASCII_STR', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Replace non-ASCII characters in a string.",
               notes="""
               All characthers > 127 will be replaced by the first character
               of the replacement string.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="string to modify"),
                   Parameter('p2', type=Type.STRING,
                             doc="replacement character")
               ]),

        Method('SetChar_STR', module='geoengine.core', version='5.1.4',
               availability=Availability.PUBLIC, 
               doc="Set a string's first character using an ASCII value of a character.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="string"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="ASCII value")
               ]),

        Method('TrimQuotes_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Remove double quotes.",
               notes="""
               THE STRING IS MODIFIED.
               This method goes through the string and removes all spaces in a
               string except those enclosed in quotes. It then removes
               any quotes. It is usfull for trimming unwanted spaces from
               an input string but allows the user to use quotes as well.
               If a quote follows a backslash, the quote is retained and
               the backslash is deleted. These quotes are NOT treated as
               delimiters.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="String to trim")
               ]),

        Method('TrimSpace_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Remove leading and/or trailing whitespace.",
               notes="""
               THE STRING IS MODIFIED.
               Whitespace characters are defined as space, tab, carriage return,
               new line, vertical tab or formfeed (0x09 to 0x0D, 0x20)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="String to trim"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`STR_TRIM`")
               ]),

        Method('UnQuote_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Remove double quotes from string",
               notes="""
               THE STRING IS MODIFIED.
               The pointers will be advanced past a first character
               quote and a last character quote will be set to .\\0'.
               Both first and last characters must be quotes for the
               triming to take place.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="String to unquote")
               ])
    ],
    'Misc': [

        Method('IGenGroupName_STR', module='geoengine.map', version='5.1.4',
               availability=Availability.PUBLIC, 
               doc="""
               Generate a group name string
               from type string, database and channel(optional) strings..
               """,
               notes="""
               The output group name string is formed in the way of typestr_dbstr_chstr.
               If the database/channel strings is too long to fit the output string
               (max total length of 1040, including the NULL ending), then
               the typestr will always be kept the full length to be the first part,
               while the dbstr and/or chstr will be shortened to be the
               second and/or third part of the output string.
               """,
               see_also="GenNewGroupName_MVIEW",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="input type string (static part)"),
                   Parameter('p2', type=Type.STRING,
                             doc="input db string"),
                   Parameter('p3', type=Type.STRING,
                             doc="input ch string (could be 0 length)"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="output group name string"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_GROUP',
                             doc="output buffer lengths (maximum 32)")
               ])
    ],
    'Tokenizing': [

        Method('iCountTokens_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Counts number of tokens.",
               notes="""
               Delimiters are "soft" in that one or more delimiters
               is considered a single delimiter, and preceding and
               trailing delimiters are ignored.
               
               DO NOT use this function except in GXC code. The corresponding
               :func:`IGetToken_STR` function will not operate correctly in GX.Net code.
               """,
               return_type=Type.INT32_T,
               return_doc="Number of tokens in the string.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="string to tokenize"),
                   Parameter('p2', type=Type.STRING,
                             doc="delimiter characters")
               ]),

        Method('IGetToken_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a token from a tokenized string.",
               notes="""
               Call :func:`iTokens_STR`  to prepare the tokenized
               string.
               You MUST NOT get tokens beyond number of tokens returned
               by :func:`iTokens_STR` or :func:`iTokens2_STR`.
               The first token has index 0.
               
               DO NOT use this function except in GXC code.
               :func:`IGetToken_STR` function will not operate correctly in GX.Net code.
               """,
               see_also=":func:`iTokens_STR`, GetToken_STR",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="destination string"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="maximum destination string length"),
                   Parameter('p3', type=Type.STRING,
                             doc="tokenized string"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="token number wanted  (0 is the first!)")
               ]),

        Method('iTokenize_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Tokenize a string based on any characters.",
               notes="""
               This uses a finite state machine to tokenize on these
               rules:
               
               1. Any one character following an escape delimiter is
               treated as a normal character.
               
               2. Any characters inside a quote string are treated as
               normal characters.
               
               3. Any number of Soft delimiters in sequence without a
               hard delimiter are treated as one hard delimited.
               
               4. Any number of soft delimiters can preceed or follow
               a hard delimiter and are ignored.
               
               
               EXAMPLE
               
               Soft = [ ]   Hard = [,]   Escape = [\\]    Quote = ["]
               
               [this is a , , the "test," of   ,  \\,\\" my delimite  fi,]
               
               Results in:
               
               [this] [is] [a] [] [the] ["test,"] [of] [\\,\\"] [my] [delimite] [fi] []
               
               
               NOT use this function except in GXC code. The corresponding
               etToken_STR function will not operate correctly in GX.Net code.
               """,
               see_also="GetToken_STR",
               return_type=Type.INT32_T,
               return_doc="number of tokens",
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="str - String containing token(s)"),
                   Parameter('p2', type=Type.STRING,
                             doc="szSoft - Soft delimiters (spaces/tabs)"),
                   Parameter('p3', type=Type.STRING,
                             doc="szHard - Hard delimiters (commas)"),
                   Parameter('p4', type=Type.STRING,
                             doc="szEsc  - Escape delimiters (back-slash)"),
                   Parameter('p5', type=Type.STRING,
                             doc="szQuote- Quote delimiters  (quote characters)")
               ]),

        Method('iTokens_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Tokenize a string",
               notes="""
               Delimiters in the string are reduced to a single NULL.
               Delimiters withing double quoted strings are ignored.
               Use GetToken_STR to extract tokens.
               
               DO NOT use this function except in GXC code. The corresponding
               :func:`IGetToken_STR` function will not operate correctly in GX.Net code.
               """,
               see_also=":func:`iTokens2_STR`, GetToken_STR",
               return_type=Type.INT32_T,
               return_doc="number of tokens, maximum is 2048",
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="string to tokenize"),
                   Parameter('p2', type=Type.STRING,
                             doc="delimiter characters")
               ]),

        Method('iTokens2_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="General tokenize a string",
               notes="""
               This function is for old GX compatibility only.
               See :func:`iTokenize_STR`.
               
               DO NOT use this function except in GXC code. The corresponding
               :func:`IGetToken_STR` function will not operate correctly in GX.Net code.
               """,
               return_type=Type.INT32_T,
               return_doc="Number of Tokens",
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True,
                             doc="string to tokenize"),
                   Parameter('p2', type=Type.STRING,
                             doc="szSoft - Soft delimiters (spaces/tabs)"),
                   Parameter('p3', type=Type.STRING,
                             doc="szHard - Hard delimiters (commas)"),
                   Parameter('p4', type=Type.STRING,
                             doc="szEsc  - Escape delimiters (back-slash)"),
                   Parameter('p5', type=Type.STRING,
                             doc="szQuote- Quote delimiters  (quote characters)")
               ]),

        Method('ParseList_STR', module='geoengine.core', version='5.0.1',
               availability=Availability.PUBLIC, 
               doc="Parse a tokenized list to get a selection list.",
               notes="""
               Given a list such as "1,3,4,6-9,12", it fills the
               input buffer with 1 if the number is selected,
               0 if not. The items are delimited with spaces
               or commas, and ranges are acceptable, either using
               a "-" or ":", e.g.  3-6 and 3:6 both mean 3,4,5, and 6.
               Only values from 0 to one less than the buffer length
               are used.  Out-of-range values are ignored.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="String to be parsed"),
                   Parameter('p2', type="VV",
                             doc="Selection Buffer to fill")
               ])
    ],
    'Miscellaneous': [

    ],
    'Obsolete': [

        Method('Substr_STR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, no_gxh=True, 
               doc="Extract part of a string.",
               notes="""
               The destination string length will be less than the
               requested length if the substring is not fully enclosed
               in the origin string.
               
               The length of the destination string MUST be at least
               the requested lenth plus 1.
               
               Obsolete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="destination string"),
                   Parameter('p2', type=Type.STRING,
                             doc="origin string"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="start location"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="number of characters")
               ])
    ]
}

