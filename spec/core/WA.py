from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('WA',
                 doc="The :class:`WA` class enables you to access and write data to ASCII files.")


gx_defines = [
    Define('WA_ENCODE',
           doc=":class:`WA` Encode defines",
           constants=[
               Constant('WA_ENCODE_ANSI', value='0', type=Type.INT32_T,
                        doc="""
                        Current Ansi Code Page (Conversion from UTF-8 data, if an exisiting BOM header found with :def_val:`WA_APPEND`,
                        encoding will switch to :def_val:`WA_ENCODE_UTF8`)
                        """)                        ,
               Constant('WA_ENCODE_RAW', value='1', type=Type.INT32_T,
                        doc="Write all data without any conversion check")                        ,
               Constant('WA_ENCODE_UTF8', value='2', type=Type.INT32_T,
                        doc=":def:`UTF8` (If no exisiting BOM header found with :def_val:`WA_APPEND`, encoding will switch to :def_val:`WA_ENCODE_ANSI`)")                        ,
               Constant('WA_ENCODE_UTF8_NOHEADER', value='3', type=Type.INT32_T,
                        doc=":def:`UTF8` w.o. header (will assume :def:`UTF8` encoding if :def_val:`WA_APPEND` is used)")                        ,
               Constant('WA_ENCODE_UTF16_NOHEADER', value='4', type=Type.INT32_T,
                        doc="UTF16 w.o. header (will assume UTF16 encoding if :def_val:`WA_APPEND` is used)")                        
           ]),

    Define('WA_OPEN',
           doc=":class:`WA` Open defines",
           constants=[
               Constant('WA_NEW', value='0', type=Type.INT32_T,
                        doc="Create new file")                        ,
               Constant('WA_APPEND', value='1', type=Type.INT32_T,
                        doc="Append to existing file")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('_Puts_WA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Writes a string to the file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="WA",
                             doc=":class:`WA` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="String to write")
               ]),

        Method('Create_WA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates an ASCII file to write to.",
               notes="ANSI Encoding is assumed, See :func:`CreateEx_WA` to override this.",
               return_type="WA",
               return_doc=":class:`WA` Handle",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the File"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`WA_OPEN`")
               ]),

        Method('CreateEx_WA', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Creates an ASCII file to write to.",
               notes="""
               Before version 6.2. text in on the GX API level were handled as characters in the current ANSI code page
               defining how characters above ASCII 127 would be displayed. 6.2. introduced Unicode in the core
               montaj engine that greatly increased the number of symbols that can be used. The :def:`WA_ENCODE` constants
               were introduce that controls how text are written to files on disk with the :class:`WA` class.
               """,
               return_type="WA",
               return_doc=":class:`WA` Handle",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the File"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`WA_OPEN`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`WA_ENCODE`")
               ]),

        Method('CreateSBF_WA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates an ASCII file to write to in an :class:`SBF`.",
               notes="See sbf.gxh. ANSI Encoding is assumed, See :func:`CreateSBFEx_WA` to override this.",
               return_type="WA",
               return_doc=":class:`WA` Handle",
               parameters = [
                   Parameter('p1', type="SBF",
                             doc="Storage"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the File"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`WA_OPEN`")
               ]),

        Method('CreateSBFEx_WA', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Creates an ASCII file to write to in an :class:`SBF`.",
               notes="""
               Also see sbf.gxh
               Before version 6.2. text in on the GX API level were handled as characters in the current ANSI code page
               defining how characters above ASCII 127 would be displayed. 6.2. introduced Unicode in the core
               montaj engine that greatly increased the number of symbols that can be used. The :def:`WA_ENCODE` constants
               were introduce that controls how text are written to files on disk with the :class:`WA` class.
               """,
               return_type="WA",
               return_doc=":class:`WA` Handle",
               parameters = [
                   Parameter('p1', type="SBF",
                             doc="Storage"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the File"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`WA_OPEN`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`WA_ENCODE`")
               ]),

        Method('Destroy_WA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys a :class:`WA` Object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="WA",
                             doc=":class:`WA` Object")
               ]),

        Method('NewLine_WA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Forces a new line in the :class:`WA` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="WA",
                             doc=":class:`WA` Object")
               ])
    ]
}

