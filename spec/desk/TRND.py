from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('TRND',
                 doc="""
The :class:`TRND` methods are used to determine trend directions in database data by locating
maxima and minima along lines and joining them in a specified direction.
The resulting trend lines are appended to the database and used by gridding methods
such as Bigrid and Rangrid to enforce features in the specified direction.
""")


gx_defines = [
    Define('TRND_NODE',
           doc="Node to find",
           constants=[
               Constant('TRND_MIN', value='0', type=Type.INT32_T)                        ,
               Constant('TRND_MAX', value='1', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('GetMaxMin_TRND', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find the max/min nodes in a line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X Channel"),
                   Parameter('p2', type="VV",
                             doc="Y Channel"),
                   Parameter('p3', type="VV",
                             doc="Data Channel"),
                   Parameter('p4', type="VV",
                             doc="X MaxMin (returned)"),
                   Parameter('p5', type="VV",
                             doc="Y MaxMin (returned)"),
                   Parameter('p6', type="VV",
                             doc="Data MaxMin (returned)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="MaxMin Window"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`TRND_NODE`")
               ]),

        Method('GetMesh_TRND', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get the lines in a trend mesh.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Selected channel"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="MaxMin Window"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Maximum join length"),
                   Parameter('p5', type="VV",
                             doc=":class:`VV` of type GS_D2POINT (returned)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`TRND_NODE`")
               ]),

        Method('TrndDB_TRND', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Uses a selected channel to find data trends in a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Selected channel"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="MaxMin Window"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Preferred angle, degrees CCW from X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Allowed deviation"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Longest join"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Maximum deflection in join (can be :def_val:`rDUMMY`)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Minimum length for trend lines (can be :def_val:`rDUMMY`)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Resampling distance (can be :def_val:`rDUMMY`)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Breaking angle, degrees CCW from X (can be :def_val:`rDUMMY`)")
               ])
    ]
}

