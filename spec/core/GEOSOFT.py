from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GEOSOFT',
                 no_csharp=True,
                 no_cpp=True,
                 doc="""
This is not a class but a collection of global defines. It
is used by all functions.
""",
                 notes="""
The following defines are not used by any methods but
are usefull in general:

:def:`GEO_BOOL`
:def:`GEO_VAR`
:def:`GEO_DUMMY`
:def:`GEO_LIMITS`
:def:`GEO_FULL_LIMITS`
:def:`GEO_STRING_SIZE`
""")


gx_defines = [
    Define('CRC_INIT_VALUE',
           is_constant=True,
           is_single_constant=True,
           doc="Initial value for starting a CRC",
           constants=[
               Constant('CRC_INIT_VALUE', value='4294967295', type=Type.UINT32_T,
                        doc="0xFFFFFFFF")                        
           ]),

    Define('DATE_FORMAT',
           doc="Old Date formats",
           constants=[
               Constant('DATE_FORMAT_YYYYMMDD', value='1', type=Type.INT32_T,
                        doc="Standard Date (YYYY/MM/DD, YY/MM/DD, YYYYMMDD or YYMMDD, space or / delimited)")                        ,
               Constant('DATE_FORMAT_DDMMYYYY', value='2', type=Type.INT32_T,
                        doc="Date (DD/MM/YYYY or DD/MM/YY century 20 if YY>50, DISC compliant)")                        ,
               Constant('DATE_FORMAT_MMDDYYYY', value='3', type=Type.INT32_T,
                        doc="Date (MM/DD/YYYY or MM/DD/YY century 19)")                        
           ]),

    Define('GEO_BOOL',
           doc="Boolean",
           constants=[
               Constant('GS_FALSE', value='0', type=Type.INT32_T)                        ,
               Constant('GS_TRUE', value='1', type=Type.INT32_T)                        
           ]),

    Define('GEO_DUMMY',
           is_constant=True,
           doc="Special numbers indicating NULLL",
           constants=[
               Constant('iDUMMY', value='-2147483647', type=Type.INT32_T,
                        doc="Integer Dummy (-2147483647)")                        ,
               Constant('rDUMMY', value='-1.0E32', type=Type.DOUBLE,
                        doc="Floating Point Dummy (-1.0E32)")                        
           ]),

    Define('GEO_FULL_LIMITS',
           is_constant=True,
           doc="Data ranges of all Geosoft types",
           constants=[
               Constant('GS_S1MX', value='127', type=Type.INT8_T,
                        doc="(signed char   )   127")                        ,
               Constant('GS_S1MN', value='-126', type=Type.INT8_T,
                        doc="(signed char   )  -126")                        ,
               Constant('GS_S1DM', value='-127', type=Type.INT8_T,
                        doc="(signed char   )  -127")                        ,
               Constant('GS_U1MX', value='254U', type=Type.UINT8_T,
                        doc="(unsigned char )   254U")                        ,
               Constant('GS_U1MN', value='0U', type=Type.UINT8_T,
                        doc="(unsigned char )   0U")                        ,
               Constant('GS_U1DM', value='255U', type=Type.UINT8_T,
                        doc="(unsigned char )   255U")                        ,
               Constant('GS_S2MX', value='32767', type=Type.INT16_T,
                        doc="(short         )   32767")                        ,
               Constant('GS_S2MN', value='-32766', type=Type.INT16_T,
                        doc="(short         )  -32766")                        ,
               Constant('GS_S2DM', value='-32767', type=Type.INT16_T,
                        doc="(short         )  -32767")                        ,
               Constant('GS_U2MX', value='65534U', type=Type.UINT32_T,
                        doc="(unsigned short)   65534U")                        ,
               Constant('GS_U2MN', value='0U', type=Type.UINT32_T,
                        doc="(unsigned short)   0U")                        ,
               Constant('GS_U2DM', value='65535U', type=Type.UINT32_T,
                        doc="(unsigned short)   65535U")                        ,
               Constant('GS_S4MX', value='2147483647L', type=Type.INT32_T,
                        doc="2147483647L")                        ,
               Constant('GS_S4MN', value='-2147483646L', type=Type.INT32_T,
                        doc="-2147483646L")                        ,
               Constant('GS_S4DM', value='-2147483647L', type=Type.INT32_T,
                        doc="-2147483647L")                        ,
               Constant('GS_U4MX', value='0xFFFFFFFE', type=Type.UINT32_T,
                        doc="(unsigned long )   0xFFFFFFFE")                        ,
               Constant('GS_U4MN', value='0x00000000', type=Type.UINT32_T,
                        doc="(unsigned long )   0x00000000")                        ,
               Constant('GS_U4DM', value='0xFFFFFFFF', type=Type.UINT32_T,
                        doc="(unsigned long )   0xFFFFFFFF")                        ,
               Constant('GS_S8MX', value='0x7FFFFFFFFFFFFFFF', type=Type.INT64_T,
                        doc="(__GS_INT64    )   0x7FFFFFFFFFFFFFFF")                        ,
               Constant('GS_S8MN', value='0x8000000000000001', type=Type.INT64_T,
                        doc="(__GS_INT64    )   0x8000000000000001")                        ,
               Constant('GS_S8DM', value='0x8000000000000000', type=Type.INT64_T,
                        doc="(__GS_INT64    )   0x8000000000000000")                        ,
               Constant('GS_U8MX', value='0xFFFFFFFFFFFFFFFE', type=Type.UINT64_T,
                        doc="(__GS_UINT64   )   0xFFFFFFFFFFFFFFFE")                        ,
               Constant('GS_U8MN', value='0x0000000000000000', type=Type.UINT64_T,
                        doc="(__GS_UINT64   )   0x0000000000000000")                        ,
               Constant('GS_U8DM', value='0xFFFFFFFFFFFFFFFF', type=Type.UINT64_T,
                        doc="(__GS_UINT64   )   0xFFFFFFFFFFFFFFFF")                        ,
               Constant('GS_R4MX', value='1.0E32f', type=Type.FLOAT,
                        doc="(float         )   1.0E32   (In C these must be declared as external constants:)")                        ,
               Constant('GS_R4MN', value='-0.9E32f', type=Type.FLOAT,
                        doc="(float         )  -0.9E32     const float r4min=(float)-0.9E32,")                        ,
               Constant('GS_R4DM', value='-1.0E32f', type=Type.FLOAT,
                        doc="""
                        (float         )  -1.0E32                 r4max=(float)1.0E32,
                        r4dum=(float)-1.0E32;
                        """)                        ,
               Constant('GS_R8MX', value='1.0E32', type=Type.DOUBLE,
                        doc="(double        )   1.0E32")                        ,
               Constant('GS_R8MN', value='-0.9E+32', type=Type.DOUBLE,
                        doc="(double        )  -0.9E32")                        ,
               Constant('GS_R8DM', value='-1.0E+32', type=Type.DOUBLE,
                        doc="(double        )  -1.0E32")                        ,
               Constant('GS_R4EPSILON', value='1.0E-32f', type=Type.FLOAT,
                        doc="(float         )   1.0E-32")                        ,
               Constant('GS_R8EPSILON', value='1.0E-32', type=Type.DOUBLE,
                        doc="(double        )   1.0E-32")                        
           ]),

    Define('GEO_LIMITS',
           is_constant=True,
           doc="Data ranges of numbers",
           constants=[
               Constant('iMIN', value='-2147483646', type=Type.INT32_T,
                        doc="Smallest Integer (-2147483646)")                        ,
               Constant('iMAX', value='2147483647', type=Type.INT32_T,
                        doc="Largest Integer (2147483647)")                        ,
               Constant('rMIN', value='-0.9E32', type=Type.DOUBLE,
                        doc="Smallest Floating Point (-0.9E32)")                        ,
               Constant('rMAX', value='1.0E32', type=Type.DOUBLE,
                        doc="Largest Floating Point (1.0E32)")                        
           ]),

    Define('GEO_STRING_SIZE',
           doc="""
           Default string sized for different uses
           GX's must use these unless there is a
           very good reason not to. The path strings
           here are generally larger than what is possible
           in the OS, but it is defined as such for Unicode
           conversion reasons.
           """,
           constants=[
               Constant('STR_DEFAULT', value='128', type=Type.INT32_T,
                        doc="Default Size for almost everything (128 characters)")                        ,
               Constant('STR_DEFAULT_SHORT', value='64', type=Type.INT32_T,
                        doc="Default Size for a short string (64 characters)")                        ,
               Constant('STR_DEFAULT_LONG', value='1024', type=Type.INT32_T,
                        doc="Default Size for a long string (1024 characters)")                        ,
               Constant('STR_ERROR', value='2048', type=Type.INT32_T,
                        doc="Default Size for an error string (2048 characters)")                        ,
               Constant('STR_VERY_LONG', value='16384', type=Type.INT32_T,
                        doc="Default Size for a long string (16384 characters)")                        ,
               Constant('STR_VIEW', value='2080', type=Type.INT32_T,
                        doc="Name of a View (2080)")                        ,
               Constant('STR_GROUP', value='1040', type=Type.INT32_T,
                        doc="Name of a Group (1040)")                        ,
               Constant('STR_VIEW_GROUP', value='2080', type=Type.INT32_T,
                        doc="Combined View/Group Name (2080)")                        ,
               Constant('STR_FILE', value='1040', type=Type.INT32_T,
                        doc="Name of a file (1040)")                        ,
               Constant('STR_MULTI_FILE', value='16384', type=Type.INT32_T,
                        doc="Name of multiple files (16384)")                        ,
               Constant('STR_DB_SYMBOL', value='64', type=Type.INT32_T,
                        doc="Name of database symbol (64)")                        ,
               Constant('STR_GXF', value='160', type=Type.INT32_T,
                        doc="Size of strings for GXF projection info (160).")                        ,
               Constant('STR_MAX_PATH', value='1040', type=Type.INT32_T,
                        doc="Maximum path length (1040)")                        ,
               Constant('STR_MULTI_PATH', value='16384', type=Type.INT32_T,
                        doc="Multi-file path (16384)")                        ,
               Constant('GS_MAX_PATH', value='STR_FILE', type=Type.INT32_T,
                        doc="Same as :def_val:`STR_FILE`")                        ,
               Constant('GS_MULTI_PATH', value='STR_MULTI_FILE', type=Type.INT32_T,
                        doc="Same as :def_val:`STR_MULTI_FILE`")                        
           ]),

    Define('GEO_VAR',
           doc="""
           Variable types.
           Use -X for strings of X length
           """,
           constants=[
               Constant('GS_INT', value='0', type=Type.INT32_T,
                        doc="Integer (long)")                        ,
               Constant('GS_REAL', value='1', type=Type.INT32_T,
                        doc="Floating Point (double)")                        
           ]),

    Define('GS_FORMATS',
           doc="""
           Special use data types. String are indicated by a
           negative maximum string length (including NULL).
           """,
           constants=[
               Constant('FORMAT_DECIMAL', value='0', type=Type.INT32_T,
                        doc="Standard numbers (-134.534)")                        ,
               Constant('FORMAT_SIG_DIG', value='5', type=Type.INT32_T,
                        doc="Decimals imply number of significant digits")                        ,
               Constant('FORMAT_EXP', value='1', type=Type.INT32_T,
                        doc="Exponential notation (-1.345e45)")                        ,
               Constant('FORMAT_TIME_COLON', value='2', type=Type.INT32_T,
                        doc="Standard Time (HH:MM:SS.SSSS)")                        ,
               Constant('FORMAT_TIME_HMS', value='8', type=Type.INT32_T,
                        doc="Time (HH.MMSSSSSSS)")                        ,
               Constant('FORMAT_TIME_HHMMSS', value='9', type=Type.INT32_T,
                        doc="Time (HHMMSS)")                        ,
               Constant('FORMAT_DATE_YYYYMMDD', value='3', type=Type.INT32_T,
                        doc="Standard Date (YYYY/MM/DD, YY/MM/DD, YYYYMMDD or YYMMDD, space or / delimited)")                        ,
               Constant('FORMAT_DATE_DDMMYYYY', value='6', type=Type.INT32_T,
                        doc="Date (DD/MM/YYYY or DD/MM/YY century 20 if YY>50, DISC compliant)")                        ,
               Constant('FORMAT_DATE_MMDDYYYY', value='7', type=Type.INT32_T,
                        doc="Date (MM/DD/YYYY or MM/DD/YY century 19)")                        ,
               Constant('FORMAT_GEOGRAPHIC', value='4', type=Type.INT32_T,
                        doc="Standard Geographical (DEG.MM.SS.SSS)")                        ,
               Constant('FORMAT_GEOGRAPHIC_1', value='10', type=Type.INT32_T,
                        doc="GeoGraph (DEG:MM:SS.SSS)")                        ,
               Constant('FORMAT_GEOGRAPHIC_2', value='11', type=Type.INT32_T,
                        doc="GeoGraph (DEG.MMSSSSS)")                        ,
               Constant('FORMAT_GEOGRAPHIC_3', value='12', type=Type.INT32_T,
                        doc="GeoGraph (DEGMMmmmm or DEGMM.mmmm or DEG.MM.mmmm)  (mmmm: decimal minute)")                        
           ]),

    Define('GS_TYPES',
           doc="""
           Special use data types. String are indicated by a
           negative maximum string length (including NULL).
           """,
           constants=[
               Constant('GS_BYTE', value='0', type=Type.INT32_T,
                        doc="Signed Byte")                        ,
               Constant('GS_USHORT', value='1', type=Type.INT32_T,
                        doc="Unsigned Short")                        ,
               Constant('GS_SHORT', value='2', type=Type.INT32_T,
                        doc="Signed Short")                        ,
               Constant('GS_LONG', value='3', type=Type.INT32_T,
                        doc="Signed Long")                        ,
               Constant('GS_FLOAT', value='4', type=Type.INT32_T,
                        doc="32-Bit floating point")                        ,
               Constant('GS_DOUBLE', value='5', type=Type.INT32_T,
                        doc="64-Bit floating point")                        ,
               Constant('GS_UBYTE', value='6', type=Type.INT32_T,
                        doc="Unsigned byte")                        ,
               Constant('GS_ULONG', value='7', type=Type.INT32_T,
                        doc="Unsigned Long")                        ,
               Constant('GS_LONG64', value='8', type=Type.INT32_T,
                        doc="64-Bit signed long")                        ,
               Constant('GS_ULONG64', value='9', type=Type.INT32_T,
                        doc="64-Bit unsigned long")                        ,
               Constant('GS_FLOAT3D', value='10', type=Type.INT32_T,
                        doc="3 x 32-Bit floating point")                        ,
               Constant('GS_MAXTYPE', value='10', type=Type.INT32_T,
                        doc="Maximum supported type (:def_val:`GS_FLOAT3D`)")                        ,
               Constant('GS_TYPE_DEFAULT', value='-32767', type=Type.INT32_T,
                        doc="Default. Can be used only when a method specifically allows a default type.")                        
           ]),

    Define('SYS_CRYPT_KEY',
           is_constant=True,
           doc="Special Encryption Keys",
           constants=[
               Constant('SYS_CRYPT_LICENSE_KEY', value='{***LICENSE_KEY***}', type=Type.STRING,
                        doc="Using the current license key")                        ,
               Constant('SYS_CRYPT_COMPUTER_ID', value='{***COMPUTER_ID***}', type=Type.STRING,
                        doc="Use the current computer ID")                        ,
               Constant('SYS_CRYPT_GLOBAL_ID', value='{***GLOBAL_COMPUTER_ID***}', type=Type.STRING,
                        doc="Use the non-changing computer ID")                        
           ]),

    Define('TIME_FORMAT',
           doc="Old Time formats",
           constants=[
               Constant('TIME_FORMAT_COLON', value='1', type=Type.INT32_T,
                        doc="Standard Time (HH:MM:SS.SSSS)")                        ,
               Constant('TIME_FORMAT_HMS', value='2', type=Type.INT32_T,
                        doc="Time (HH.MMSSSSSSS)")                        
           ])]


gx_methods = {
    'Miscellaneous': [

    ]
}

