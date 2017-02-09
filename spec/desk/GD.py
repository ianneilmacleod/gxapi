from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GD',
                 doc="""
                 This class provides access to Geosoft grid files using an old interface.
                 Only the :func:`SampleGD_DU` function uses this class.  Use the :class:`IMG` class
                 instead.
                 """)


gx_defines = [
    Define('GD_STATUS',
           doc="Grid open mode",
           constants=[
               Constant('GD_STATUS_READONLY', value='0', type=Type.INT32_T)                        ,
               Constant('GD_STATUS_NEW', value='1', type=Type.INT32_T)                        ,
               Constant('GD_STATUS_OLD', value='2', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_GD', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method creates a :class:`GD` object.",
               return_type="GD",
               return_doc="Handle to the :class:`GD` object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the Grid File"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GD_STATUS`")
               ]),

        Method('Destroy_GD', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a :class:`GD` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GD",
                             doc="Destroy a grid object")
               ])
    ]
}

