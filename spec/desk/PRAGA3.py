from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('PRAGA3',
                 doc=":class:`PRAGA3` application methods",
                 notes="No notes")





gx_methods = {
    'Miscellaneous': [

        Method('iLaunch_PRAGA3', module='geopraga', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="This method launches the application.",
               return_type=Type.INT32_T,
               return_doc="1 - OK, 2 - Cancel")
    ]
}

