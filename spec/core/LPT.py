from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('LPT',
                 doc="""
This class allows access to the current default line patterns.
It does not allow the definition of individual patterns. It is
is used primarily with :class:`MAP` class functions.
""")





gx_methods = {
    'Miscellaneous': [

        Method('Create_LPT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates a line pattern object with current default patterns.",
               return_type="LPT",
               return_doc=":class:`LPT` Object"),

        Method('Destroy_LPT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys a line pattern object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LPT",
                             doc=":class:`LPT` Handle")
               ]),

        Method('GetLST_LPT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copies all pattern names into a :class:`LST` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LPT",
                             doc=":class:`LPT` Handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` Handle")
               ]),

        Method('GetStandardLST_LPT', module='geoengine.map', version='9.0',
               availability=Availability.PUBLIC, 
               doc="Copies the six standard line types into a :class:`LST` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LPT",
                             doc=":class:`LPT` Handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` Handle")
               ])
    ],
    'Obsolete': [

        Method('Copy_LPT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Copy one :class:`LPT` object to another.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LPT",
                             doc="Destination :class:`LPT` to copy to"),
                   Parameter('p2', type="LPT",
                             doc="Source :class:`LPT` to Copy from")
               ]),

        Method('iSize_LPT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Get the number of patterns in the :class:`LPT`.",
               return_type=Type.INT32_T,
               return_doc="x - Number of patterns in the :class:`LPT`.",
               parameters = [
                   Parameter('p1', type="LPT",
                             doc=":class:`LPT` Handle")
               ])
    ]
}

