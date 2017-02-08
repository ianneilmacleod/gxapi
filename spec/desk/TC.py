from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('TC',
                 doc="""
The :class:`TC` object is used in gravitational modelling to create
a terrain correction grid from a topography grid. This is
accomplished with a call first to :func:`Grregter_TC`, which determines
the terrain correction from an input topography grid, then
to :func:`Grterain_TC`, which calculates the actual corrections at
the input positions.
""")


gx_defines = [
    Define('TC_OPT',
           doc="Optimization",
           constants=[
               Constant('TC_OPT_NONE', value='0', type=Type.INT32_T,
                        doc="(slow)    no optimization")                        ,
               Constant('TC_OPT_MAX', value='1', type=Type.INT32_T,
                        doc="""
                        (faster)  desampling and using qspline (4x4 points) interp
                        on coarser averaged grid
                        """)                        
           ]),

    Define('TC_SURVEYTYPE',
           doc="Survey Type",
           constants=[
               Constant('TC_SURVEYTYPE_GROUND', value='0', type=Type.INT32_T,
                        doc="Ground")                        ,
               Constant('TC_SURVEYTYPE_SHIPBORNE', value='1', type=Type.INT32_T,
                        doc="Shipborne")                        ,
               Constant('TC_SURVEYTYPE_AIRBORNE', value='2', type=Type.INT32_T,
                        doc="Airborne")                        
           ]),

    Define('GG_ELEMENT',
           doc="GG element",
           constants=[
               Constant('GG_ELEMENT_XX', value='0', type=Type.INT32_T,
                        doc="Gxx")                        ,
               Constant('GG_ELEMENT_YY', value='1', type=Type.INT32_T,
                        doc="Gyy")                        ,
               Constant('GG_ELEMENT_XY', value='2', type=Type.INT32_T,
                        doc="Gxy")                        ,
               Constant('GG_ELEMENT_XZ', value='3', type=Type.INT32_T,
                        doc="Gxz")                        ,
               Constant('GG_ELEMENT_YZ', value='4', type=Type.INT32_T,
                        doc="Gyz")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_TC', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Creates a Terrain Correction object",
               return_type="TC",
               return_doc=":class:`TC` Object",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="topo (DEM) grid"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="elevation unit in 1 metre (i.e. 0.3048 for feet)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="inner distance (in topo grid projection units, default in metres)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="outer distance (in topo grid projection units, default in metres)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="terrain density in g/cc"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="water density in g/cc"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="water reference elevation (in elevation unit)"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def_val:`GS_TRUE` to calculate an edge correction (compensation)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="average elevation beyond max distance (in elevation unit)"),
                   Parameter('p10', type=Type.INT32_T,
                             doc=":def:`TC_OPT`")
               ]),

        Method('CreateEx_TC', module='geogxx', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Creates a Terrain Correction object	with surveytype",
               return_type="TC",
               return_doc=":class:`TC` Object",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="topo (DEM) grid"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="elevation unit in 1 metre (i.e. 0.3048 for feet)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="inner distance (in topo grid projection units, default in metres)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="outer distance (in topo grid projection units, default in metres)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="terrain density in g/cc"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="water density in g/cc"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="water reference elevation (in elevation unit)"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def_val:`GS_TRUE` to calculate an edge correction (compensation)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="average elevation beyond max distance (in elevation unit)"),
                   Parameter('p10', type=Type.INT32_T,
                             doc=":def:`TC_OPT`"),
                   Parameter('p11', type=Type.INT32_T,
                             doc=":def:`TC_SURVEYTYPE`")
               ]),

        Method('Destroy_TC', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a table resource.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TC",
                             doc=":class:`TC` Object to Destroy")
               ]),

        Method('Grregter_TC', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create a terrain correction grid for a topo grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TC",
                             doc=":class:`TC` handle"),
                   Parameter('p2', type="IMG",
                             doc="Input :class:`IMG` (local DEM topo grid used for station elevation)"),
                   Parameter('p3', type="IMG",
                             doc="Image of output grid")
               ]),

        Method('Grterain_TC', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Calculate terrain corrections.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TC",
                             doc=":class:`TC` handle"),
                   Parameter('p2', type="VV",
                             doc="input X channel data (in topo grid projection units, default in metres)"),
                   Parameter('p3', type="VV",
                             doc="input Y channel data (in topo grid projection units, default in metres)"),
                   Parameter('p4', type="VV",
                             doc="input Elevation channel data (in elevation unit)"),
                   Parameter('p5', type="VV",
                             doc="input slope channel data"),
                   Parameter('p6', type="VV",
                             doc="output Terrain Corrected channel data"),
                   Parameter('p7', type="IMG",
                             doc="Image of input correction grid"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Terrain density (default 2.67)")
               ]),

        Method('Grterain2_TC', module='geogxx', version='6.0.0',
               availability=Availability.EXTENSION, 
               doc="Calculate terrain corrections (work for marine gravity too).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TC",
                             doc=":class:`TC` handle"),
                   Parameter('p2', type="VV",
                             doc="input X channel data (in topo grid projection units, default in metres)"),
                   Parameter('p3', type="VV",
                             doc="input Y channel data (in topo grid projection units, default in metres)"),
                   Parameter('p4', type="VV",
                             doc="input Elevation channel data (in elevation unit)"),
                   Parameter('p5', type="VV",
                             doc="input slope channel data"),
                   Parameter('p6', type="VV",
                             doc="input Water depth channel data (in metres)"),
                   Parameter('p7', type="VV",
                             doc="output Terrain Corrected channel data"),
                   Parameter('p8', type="IMG",
                             doc="Image of input correction grid"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Terrain density (default 2.67)")
               ]),

        Method('GGterain_TC', module='geogxx', version='6.0.0',
               availability=Availability.EXTENSION, 
               doc="Calculate GG terrain corrections",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TC",
                             doc=":class:`TC` handle"),
                   Parameter('p2', type="VV",
                             doc="input X channel data (in topo grid projection units, default in metres)"),
                   Parameter('p3', type="VV",
                             doc="input Y channel data (in topo grid projection units, default in metres)"),
                   Parameter('p4', type="VV",
                             doc="input Elevation channel data (in elevation unit)"),
                   Parameter('p5', type="VV",
                             doc="output Terrain Corrected channel data"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Terrain density (default 2.67)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Terrain reference level (default 0.0)"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`GG_ELEMENT`")
               ])
    ]
}

