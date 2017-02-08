from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('ST2',
                 doc="""
Bi-variate statistics. The :class:`ST2` class accumulates statistics
on two data vectors simultaneously in order to compute correlation
information. Statistics are accumulated using the :func:`DataVV_ST2` function.
See also :class:`ST` (mono-variate statistics).
""")


gx_defines = [
    Define('ST2_CORRELATION',
           doc="Correlation style",
           constants=[
               Constant('ST2_CORR', value='0', type=Type.INT32_T,
                        doc="Simple correlation")                        ,
               Constant('ST2_PCORR', value='1', type=Type.INT32_T,
                        doc="Pearson's correlation (normalized to standard deviations)")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_ST2', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Creates a statistics object which is used to accumulate statistics.",
               return_type="ST2",
               return_doc=":class:`ST2` Object"),

        Method('DataVV_ST2', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Add all the values in VVx and VVy to :class:`ST2` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST2",
                             doc=":class:`ST2` Handle"),
                   Parameter('p2', type="VV",
                             doc="VVx handle"),
                   Parameter('p3', type="VV",
                             doc="VVy handle")
               ]),

        Method('Destroy_ST2', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys the statistics object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST2",
                             doc=":class:`ST2` Handle")
               ]),

        Method('iItems_ST2', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Gets Number of items",
               return_type=Type.INT32_T,
               return_doc="Number of items in :class:`ST2`",
               parameters = [
                   Parameter('p1', type="ST2",
                             doc=":class:`ST2` Handle")
               ]),

        Method('Reset_ST2', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Resets the Statistics.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST2",
                             doc=":class:`ST2` Handle")
               ]),

        Method('rGet_ST2', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Gets correlation coeff. from the :class:`ST2` object.",
               return_type=Type.DOUBLE,
               return_doc="""
               Data you asked for
               :def_val:`GS_R8DM` for none
               """,
               parameters = [
                   Parameter('p1', type="ST2",
                             doc=":class:`ST2` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`ST2_CORRELATION`")
               ])
    ]
}

