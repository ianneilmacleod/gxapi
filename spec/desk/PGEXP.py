from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('PGEXP',
                 doc="""
The :class:`PGEXP` class is similar to the :class:`EXP` class, but is used
to apply math expressions to pagers (:class:`PG` objects).

It works only on PGs of the same dimensions.
""")





gx_methods = {
    'Miscellaneous': [

        Method('AddPager_PGEXP', module='geogxx', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="""
               This method adds an pager to the :class:`PGEXP` object with a
               variable name.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PGEXP",
                             doc=":class:`PGEXP` object"),
                   Parameter('p2', type="PG",
                             doc="pager to add"),
                   Parameter('p3', type=Type.STRING,
                             doc="Variable name")
               ]),

        Method('Create_PGEXP', module='geogxx', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="This method creates an :class:`PGEXP` object.",
               return_type="PGEXP",
               return_doc=":class:`PGEXP` Object"),

        Method('Destroy_PGEXP', module='geogxx', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a :class:`PGEXP` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PGEXP",
                             doc="Destroy a :class:`PGEXP` object")
               ]),

        Method('DoFormula_PGEXP', module='geogxx', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="This method runs a formula on the pagers.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PGEXP",
                             doc=":class:`PGEXP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Formula"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Max. Buff size")
               ])
    ]
}

