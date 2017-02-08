from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('RA',
                 doc="""
The :class:`RA` class is used to access ASCII files sequentially or
by line number. The files are opened in read-only mode, so no
write operations are defined
""")





gx_methods = {
    'Miscellaneous': [

        Method('Create_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates :class:`RA`",
               return_type="RA",
               return_doc=":class:`RA` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of the file")
               ]),

        Method('CreateSBF_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates :class:`RA` on an :class:`SBF`",
               return_type="RA",
               return_doc=":class:`RA` Object",
               parameters = [
                   Parameter('p1', type="SBF",
                             doc="Storage"),
                   Parameter('p2', type=Type.STRING,
                             doc="name of the file")
               ]),

        Method('Destroy_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`RA`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="RA",
                             doc=":class:`RA` to destroy")
               ]),

        Method('IiGets_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get next full line from :class:`RA`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - End of file
               """,
               parameters = [
                   Parameter('p1', type="RA",
                             doc=":class:`RA` handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="buffer in which to place string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="maximum length of the string buffer")
               ]),

        Method('iLen_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the total number of lines in :class:`RA`",
               return_type=Type.INT32_T,
               return_doc="# of lines in the :class:`RA`.",
               parameters = [
                   Parameter('p1', type="RA",
                             doc=":class:`RA` handle")
               ]),

        Method('iLine_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns current line #, 0 is the first",
               return_type=Type.INT32_T,
               return_doc="The current read line location.",
               parameters = [
                   Parameter('p1', type="RA",
                             doc=":class:`RA` handle")
               ]),

        Method('iSeek_RA', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Position next read to specified line #",
               return_type=Type.INT32_T,
               return_doc="""
               0 if seeked line is within the range of lines,
               1 if outside range, line pointer will not be moved.
               """,
               parameters = [
                   Parameter('p1', type="RA",
                             doc=":class:`RA` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="line #, 0 is the first.")
               ])
    ]
}

