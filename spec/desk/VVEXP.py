from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VVEXP',
                 doc="""
                 The :class:`VVEXP` class is similar to the :class:`IEXP` class, but is used
                 to apply math expressions to :class:`VV` objects.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('AddVV_VVEXP', module='geogxx', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="""
               This method adds a :class:`VV` to the :class:`VVEXP` object with a
               variable name.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VVEXP",
                             doc=":class:`VVEXP` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` to add"),
                   Parameter('p3', type=Type.STRING,
                             doc="Variable name")
               ]),

        Method('Create_VVEXP', module='geogxx', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="This method creates an :class:`VVEXP` object.",
               return_type="VVEXP",
               return_doc=":class:`VVEXP` Object"),

        Method('Destroy_VVEXP', module='geogxx', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a :class:`VVEXP` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VVEXP",
                             doc="Destroy a :class:`VVEXP` object")
               ]),

        Method('DoFormula_VVEXP', module='geogxx', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="This method runs a formula on the grids.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VVEXP",
                             doc=":class:`VVEXP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Formula"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Max. Buff size")
               ])
    ]
}

