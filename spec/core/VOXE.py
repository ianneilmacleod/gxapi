from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VOXE',
                 doc="""
:class:`VOX` evaluator class. Used to sample values from
the voxel.
""")


gx_defines = [
    Define('VOXE_EVAL',
           doc="Voxel Evaluation modes",
           constants=[
               Constant('VOXE_EVAL_NEAR', value='0', type=Type.INT32_T,
                        doc="Nearest value")                        ,
               Constant('VOXE_EVAL_INTERP', value='1', type=Type.INT32_T,
                        doc="Linear Interpolation")                        ,
               Constant('VOXE_EVAL_BEST', value='2', type=Type.INT32_T,
                        doc="Best Interpolation")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_VOXE', module='geoengine.core', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Create a handle to an :class:`VOXE` object",
               return_type="VOXE",
               return_doc=":class:`VOXE` handle, terminates if creation fails",
               parameters = [
                   Parameter('p1', type="VOX",
                             doc=":class:`VOX` Object")
               ]),

        Method('Destroy_VOXE', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`VOXE`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOXE",
                             doc=":class:`VOXE` to destroy.")
               ]),

        Method('Profile_VOXE', module='geoengine.core', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Extract a profile of data along points provided.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOXE",
                             doc=":class:`VOXE` object"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV` (must be double)"),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV` (must be double)"),
                   Parameter('p4', type="VV",
                             doc="Z :class:`VV` (must be double)"),
                   Parameter('p5', type="VV",
                             doc="D :class:`VV` (must be double)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`VOXE_EVAL`")
               ]),

        Method('rValue_VOXE', module='geoengine.core', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Get a value at a specific point",
               return_type=Type.DOUBLE,
               return_doc="Value at the point or DUMMY if not valid",
               parameters = [
                   Parameter('p1', type="VOXE",
                             doc=":class:`VOXE` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X Location"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y Location"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z Location"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`VOXE_EVAL`")
               ]),

        Method('Vector_VOXE', module='geoengine.core', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Extract a profile of data along a vector",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOXE",
                             doc=":class:`VOXE` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X Origin"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y Origin"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z Origin"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X Delta"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Y Delta"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Z Delta"),
                   Parameter('p8', type="VV",
                             doc="Data :class:`VV` (must be double)"),
                   Parameter('p9', type=Type.INT32_T,
                             doc=":def:`VOXE_EVAL`")
               ])
    ]
}

