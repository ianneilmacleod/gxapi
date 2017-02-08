from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('PLY',
                 doc="""
The :class:`PLY` object contains the definitions for one or more
polygons, and does import and export of polygon files.
""")


gx_defines = [
    Define('PLY_CLIP',
           doc="Polygon clipping mode",
           constants=[
               Constant('PLY_CLIP_NO_INTERSECT', value='0', type=Type.INT32_T,
                        doc="The polygons do not intersect")                        ,
               Constant('PLY_CLIP_INTERSECT', value='1', type=Type.INT32_T,
                        doc="The polygons do intersect")                        ,
               Constant('PLY_CLIP_A_IN_B', value='2', type=Type.INT32_T,
                        doc="Polygon A is completly inside polygon B")                        ,
               Constant('PLY_CLIP_B_IN_A', value='3', type=Type.INT32_T,
                        doc="Polygon B is completly inside polygon A")                        
           ]),

    Define('PLY_LINE_CLIP',
           doc="Polygon line clip indicator",
           constants=[
               Constant('PLY_LINE_CLIP_INSIDE', value='0', type=Type.INT32_T,
                        doc="The start point of the line is inside")                        ,
               Constant('PLY_LINE_CLIP_NO_INTERSECT', value='0', type=Type.INT32_T,
                        doc="This name is a misnomer - it should have been :def_val:`PLY_LINE_CLIP_INSIDE`, but is retained to support legacy code")                        ,
               Constant('PLY_LINE_CLIP_OUTSIDE', value='1', type=Type.INT32_T,
                        doc="The start point of the line is outside")                        ,
               Constant('PLY_LINE_CLIP_ERROR', value='2', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AddPolygon_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a polygon to the polygon file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV`."),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV`.")
               ]),

        Method('AddPolygonEx_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a polygon to the polygon file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV`."),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV`."),
                   Parameter('p4', type=Type.INT32_T,
                             doc="bExclude")
               ]),

        Method('ChangeIPJ_PLY', module='geoengine.core', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Set the projection.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` to place in the :class:`PLY`")
               ]),

        Method('Clear_PLY', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Clear/remove all polygons from the :class:`PLY`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object")
               ]),

        Method('Copy_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys a :class:`PLY` Object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc="destination"),
                   Parameter('p2', type="PLY",
                             doc="source")
               ]),

        Method('Create_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates a Polygon Object.",
               return_type="PLY",
               return_doc=":class:`PLY` Handle"),

        Method('CreateS_PLY', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`PLY` Object from a :class:`BF`",
               return_type="PLY",
               return_doc=":class:`PLY` Handle",
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` to serialize from")
               ]),

        Method('Destroy_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys a :class:`PLY` Object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object")
               ]),

        Method('Extent_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the extent of the current polygon.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Min X"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Min Y"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Max X"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Max Y")
               ]),

        Method('GetIPJ_PLY', module='geoengine.core', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Get the projection.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` in which to place the :class:`PLY` projection")
               ]),

        Method('GetPolygon_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a polygon from the :class:`PLY`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV`."),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV`."),
                   Parameter('p4', type=Type.INT32_T,
                             doc="polygon number")
               ]),

        Method('GetPolygonEx_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a polygon from the :class:`PLY`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV`."),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV`."),
                   Parameter('p4', type=Type.INT32_T,
                             doc="polygon number"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="TRUE if exclusion polygon")
               ]),

        Method('iClipArea_PLY', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Clip a polygon to an area",
               return_type=Type.INT32_T,
               return_doc=":def:`PLY_CLIP`",
               parameters = [
                   Parameter('p1', type="PLY",
                             doc="polygon to clip"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="min X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="min Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="max X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="max y")
               ]),

        Method('iClipLineInt_PLY', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="""
               Clips a line in or out of the polygons for intersections (:def_val:`GS_DOUBLE`).
               Intersections are returned as fiducials down the line stored in :class:`VV`
               starting at the first point of the line.
               Examples:
               No intersection: :def_val:`PLY_LINE_CLIP_OUTSIDE`, 0 intersections
               Starts outside, ends inside: :def_val:`PLY_LINE_CLIP_OUTSIDE`, 1 intersection
               Starts outside, intersects then ends inside or outside: :def_val:`PLY_LINE_CLIP_OUTSIDE`, 2 intersections
               Starts inside, ends inside : :def_val:`PLY_LINE_CLIP_INSIDE`, 1 intersection (gives end-of-line)
               Starts inside, ends outside : :def_val:`PLY_LINE_CLIP_INSIDE`, 1 intersection
               """,
               return_type=Type.INT32_T,
               return_doc="0, Terminates on error (you can ignore this value)",
               parameters = [
                   Parameter('p1', type="PLY",
                             doc="polygon to clip"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="min X of line to clip"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="min Y of line to clip"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="max X of line to clip"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="max y of line to clip"),
                   Parameter('p6', type="VV",
                             doc="DOUBLE :class:`VV` holding intersection fids"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="data element increment (precision)"),
                   Parameter('p8', type=Type.INT32_T, is_ref=True,
                             doc="First point value (:def:`PLY_LINE_CLIP` value)")
               ]),

        Method('iClipPLY_PLY', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Clip one polygon against another",
               return_type=Type.INT32_T,
               return_doc=":def:`PLY_CLIP`",
               parameters = [
                   Parameter('p1', type="PLY",
                             doc="polygon A"),
                   Parameter('p2', type="PLY",
                             doc="polygon B"),
                   Parameter('p3', type="PLY",
                             doc="resulting clipped region")
               ]),

        Method('IGetDescription_PLY', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`PLY` description string",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="polygon description"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="string size")
               ]),

        Method('iNumPoly_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of polygons.",
               return_type=Type.INT32_T,
               return_doc="number of polygons in the :class:`PLY`.",
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object")
               ]),

        Method('LoadTable_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Loads Polygons from a Polygon file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the polygon file File contains coordinates of one or more polygons")
               ]),

        Method('rArea_PLY', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Compute the Area of a polygon",
               return_type=Type.DOUBLE,
               return_doc="Area of a polygon",
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object")
               ]),

        Method('Rectangle_PLY', module='geoengine.core', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Creates a polygon from a rectangular area.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Max Y")
               ]),

        Method('Rotate_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Rotate a polygon about a point.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Rotation point, X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Rotation point, Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Rotation angle, CCW in degrees")
               ]),

        Method('SaveTable_PLY', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Save Polygons to a Polygon file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the polygon file")
               ]),

        Method('Serial_PLY', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Serialize an :class:`PLY` to a :class:`BF`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` object to serialize"),
                   Parameter('p2', type="BF",
                             doc=":class:`BF` to serialize to")
               ]),

        Method('SetDescription_PLY', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Set the :class:`PLY` description string",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="polygon description")
               ]),

        Method('SetIPJ_PLY', module='geoengine.core', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Set the projection.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` to place in the :class:`PLY`")
               ]),

        Method('Thin_PLY', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Thin polygons to a desired resolution",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` Object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="thining resolution")
               ])
    ]
}

