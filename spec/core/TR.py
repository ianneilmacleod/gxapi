from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('TR',
                 doc="""
The :class:`TR` object contains trend information about a grid or
grid pager. Currently, it is used only in conjunction with
the :func:`GetTR_IMG`, :func:`SetTR_IMG`, and :func:`Trend_PGU` functions.
""")





gx_methods = {
    'Miscellaneous': [

        Method('Create_TR', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Creates a Trend object",
               return_type="TR",
               return_doc=":class:`TR` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Trend order (must >=0 and <=3)")
               ]),

        Method('Destroy_TR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a table resource.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TR",
                             doc="Trend Object to Destroy")
               ]),

        Method('Copy_TR', module='geoengine.core', version='8.1.0',
               availability=Availability.PUBLIC, 
               doc="This method copies a table resource to another trend table resource.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TR",
                             doc="Destination Trend Object"),
                   Parameter('p2', type="TR",
                             doc="Source Trend Object to Copy")
               ])
    ]
}

