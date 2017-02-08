from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('STRINGS',
                 doc="The :class:`STRINGS` class is used for displaying digitization tools for interpretations")





gx_methods = {
    'Miscellaneous': [

        Method('LaunchDigitizationUI_STRINGS', module='geostrings', version='7.5.0',
               availability=Availability.PUBLIC, 
               doc="Launch Digitization modeless window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="string file"),
                   Parameter('p2', type=Type.STRING,
                             doc="definition guid")
               ])
    ]
}

