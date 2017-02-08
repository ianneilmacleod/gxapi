from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GMSYS',
                 doc="The :class:`GMSYS` Methods")





gx_methods = {
    'Miscellaneous': [

        Method('Launch_GMSYS', module='geogxx', version='5.0.1',
               availability=Availability.PUBLIC, 
               doc="Launch :class:`GMSYS` with extension",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Model name")
               ])
    ]
}

