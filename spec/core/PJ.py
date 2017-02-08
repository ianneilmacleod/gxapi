from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('PJ',
                 doc="""
The :class:`PJ` object is created from two :class:`IPJ` objects,
and is used for converting data in an OASIS database
or map object from one map coordinate (projection)
system to another.
""")


gx_defines = [
    Define('PJ_ELEVATION',
           doc="elevation correction method",
           constants=[
               Constant('PJ_ELEVATION_NONE', value='0', type=Type.INT32_T,
                        doc="elevation transform not supported.")                        ,
               Constant('PJ_ELEVATION_GEOCENTRIC', value='1', type=Type.INT32_T,
                        doc="""
                        elevation transformation uses earth-centre shift
                        and is not accurate.
                        """)                        ,
               Constant('PJ_ELEVATION_GEOID', value='2', type=Type.INT32_T,
                        doc="""
                        elevation transformation uses a geoid model
                        and is as accurate as the geoid data.
                        """)                        
           ]),

    Define('PJ_RECT',
           doc="Conversion direction",
           constants=[
               Constant('PJ_RECT_XY2LL', value='0', type=Type.INT32_T)                        ,
               Constant('PJ_RECT_LL2XY', value='1', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('ClipPLY_PJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a clip polygon from a projected area.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc=":class:`PJ` to use"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Min X (or Longitude...)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min Y (or Latitude...)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Max deviation in degrees"),
                   Parameter('p7', type="PLY",
                             doc=":class:`PLY` to be filled")
               ]),

        Method('ConvertVV_PJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert VVx/VVy from input projection to output projection.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc="Projection"),
                   Parameter('p2', type="VV",
                             doc="VVx"),
                   Parameter('p3', type="VV",
                             doc="VVy")
               ]),

        Method('ConvertVV3_PJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert VVx/VVy/VVz projections",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc="Projection"),
                   Parameter('p2', type="VV",
                             doc="VVx"),
                   Parameter('p3', type="VV",
                             doc="VVy"),
                   Parameter('p4', type="VV",
                             doc="VVz")
               ]),

        Method('ConvertXY_PJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert X, Y from input projection to output projection.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc="Projection"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X  (or Longitude)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y  (or Latitude)")
               ]),

        Method('ConvertXYFromXYZ_PJ', module='geoengine.core', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="Convert X, Y from input projection to output projection, taking Z into account",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc="Projection"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X  (or Longitude)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y  (or Latitude)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z  (or Depth - unchanged)")
               ]),

        Method('ConvertXYZ_PJ', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Convert X,Y,Z from input projection to output projection.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc="Projection"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X  (or Longitude)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y  (or Latitude)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Z  (or Depth)")
               ]),

        Method('Create_PJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method creates a projection object.",
               return_type="PJ",
               return_doc=":class:`PJ` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='Input PRJ file name, "" for geodetic'),
                   Parameter('p2', type=Type.STRING,
                             doc='Ouput PRJ file name, "" for geodetic')
               ]),

        Method('CreateIPJ_PJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method creates a projection object from IPJs.",
               return_type="PJ",
               return_doc=":class:`PJ` Object",
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="Input Projection, (:class:`IPJ`)0 for long/lat"),
                   Parameter('p2', type="IPJ",
                             doc="Output Projection, (:class:`IPJ`)0 for long/lat")
               ]),

        Method('CreateRectified_PJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a rectified :class:`PJ` from lon,lat,rotation",
               return_type="PJ",
               return_doc=":class:`PJ` Object",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="longitude  at (X,Y) origin"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="latitude   at (X,Y) origin"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="(X,Y) origin"),
                   Parameter('p4', type=Type.DOUBLE),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="coordinate Y relative to geographic N (deg azm)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="scale to convert X,Y to m."),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`PJ_RECT`")
               ]),

        Method('Destroy_PJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a projection object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc="Projection to Destroy")
               ]),

        Method('iElevation_PJ', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Get elevation correction method",
               return_type=Type.INT32_T,
               return_doc=":def:`PJ_ELEVATION`",
               parameters = [
                   Parameter('p1', type="PJ",
                             doc="Projection")
               ]),

        Method('iIsInputLL_PJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Is the input projection a lat/long.",
               return_type=Type.INT32_T,
               return_doc="""
               1 - Yes
               0 - No
               """,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc="Projection")
               ]),

        Method('iIsOutputLL_PJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Is the output projection a lat/long.",
               return_type=Type.INT32_T,
               return_doc="""
               1 - Yes
               0 - No
               """,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc="Projection")
               ]),

        Method('ProjectBoundingRectangle_PJ', module='geoengine.core', version='5.1.4',
               availability=Availability.PUBLIC, 
               doc="Project a bounding rectangle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc=":class:`PJ` to use"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Min X"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Min Y"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Max X"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Max Y")
               ]),

        Method('ProjectBoundingRectangle2_PJ', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Project a bounding rectangle with error tolerance.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc=":class:`PJ` to use"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Min X"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Min Y"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Max X"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Max Y"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="maximum allowable projection error if <= 0.0, will use 0.005% of smallest dimension")
               ]),

        Method('ProjectBoundingRectangleRes_PJ', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Project a bounding rectangle with resolution.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc=":class:`PJ` to use"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Min X"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Min Y"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Max X"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Max Y"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Resolution")
               ]),

        Method('ProjectBoundingRectangleRes2_PJ', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Project a bounding rectangle with resolution and error tolerance.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc=":class:`PJ` to use"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Min X"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Min Y"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Max X"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Max Y"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Resolution"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="maximum allowable projection error if <= 0.0, will use 0.005% of smallest dimension")
               ]),

        Method('ProjectLimitedBoundingRectangle_PJ', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Project a bounding rectangle with limits.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc=":class:`PJ` to use"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Output limited bounding region Min X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Bounding Region Min X"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Min Y"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Max X"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Max Y")
               ]),

        Method('SetupLDT_PJ', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Setup the :class:`PJ` with LDT check.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PJ",
                             doc="Projection")
               ])
    ]
}

