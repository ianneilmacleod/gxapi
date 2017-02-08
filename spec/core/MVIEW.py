from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MVIEW',
                 doc="""
A view (:class:`MVIEW` class) has a 2-D/3-D translation matrix, a map
projection and a clip region.  A view contains any number of
"groups", and each "group" contains one or more graphics
elements (entities).  Different types of groups will contain
different types of entities:
""",
                 notes="""
:class:`CSYMB` groups (colour symbols) contain data and rules for
presenting the data as colour symbols.  See :func:`ColSymbol_MVIEW`
and the :class:`CSYMB` class.

:class:`AGG` groups (aggregates) contain images.  See :func:`Aggregate_MVIEW`
and the :class:`AGG` class.

PAGG groups (poly-aggregates) contain images with multiple
frames that make up an animation.  See :func:`PolyAggregate_MVIEW`
and the PAGG class.

Standard groups contain symbols, lines, polylines, and polygons.
See :func:`StartGroup_MVIEW`.
""")


gx_defines = [
    Define('MAKER',
           doc="Maker defines",
           constants=[
               Constant('MAKER_GX', value='0', type=Type.INT32_T,
                        doc="GX")                        
           ]),

    Define('MVIEW_CLIP',
           doc="Boolean clipping defines",
           constants=[
               Constant('CLIP_ON', value='1', type=Type.INT32_T,
                        doc="Turn ON clipping")                        ,
               Constant('CLIP_OFF', value='0', type=Type.INT32_T,
                        doc="Turn OFF clipping")                        
           ]),

    Define('MVIEW_COLOR',
           doc="""
           24-bit color defines
           The :func:`iColor_MVIEW` function can be used to create a color int from a
           color string description.
           The iColorXXX_MVIEW macros can be used to create colors from component
           intensities.
           """,
           constants=[
               Constant('C_BLACK', value='33554432', type=Type.INT32_T,
                        doc="Black")                        ,
               Constant('C_RED', value='33554687', type=Type.INT32_T,
                        doc="Red")                        ,
               Constant('C_GREEN', value='33619712', type=Type.INT32_T,
                        doc="Green")                        ,
               Constant('C_BLUE', value='50266112', type=Type.INT32_T,
                        doc="Blue")                        ,
               Constant('C_CYAN', value='50331903', type=Type.INT32_T,
                        doc="Cyan")                        ,
               Constant('C_MAGENTA', value='50396928', type=Type.INT32_T,
                        doc="Magenta")                        ,
               Constant('C_YELLOW', value='67043328', type=Type.INT32_T,
                        doc="Yellow")                        ,
               Constant('C_GREY', value='41975936', type=Type.INT32_T,
                        doc="Grey")                        ,
               Constant('C_LT_RED', value='54542336', type=Type.INT32_T,
                        doc="Light Red")                        ,
               Constant('C_LT_GREEN', value='54526016', type=Type.INT32_T,
                        doc="Light Green")                        ,
               Constant('C_LT_BLUE', value='50348096', type=Type.INT32_T,
                        doc="Light Blue")                        ,
               Constant('C_LT_CYAN', value='50331712', type=Type.INT32_T,
                        doc="Light Cyan")                        ,
               Constant('C_LT_MAGENTA', value='50348032', type=Type.INT32_T,
                        doc="Light Magenta")                        ,
               Constant('C_LT_YELLOW', value='54525952', type=Type.INT32_T,
                        doc="Light Yellow")                        ,
               Constant('C_LT_GREY', value='54542400', type=Type.INT32_T,
                        doc="Light Grey")                        ,
               Constant('C_GREY10', value='51910680', type=Type.INT32_T,
                        doc="Grey 10%")                        ,
               Constant('C_GREY25', value='54542400', type=Type.INT32_T,
                        doc="Grey 25%")                        ,
               Constant('C_GREY50', value='41975936', type=Type.INT32_T,
                        doc="Grey 50%")                        ,
               Constant('C_WHITE', value='50331648', type=Type.INT32_T,
                        doc="White")                        ,
               Constant('C_TRANSPARENT', value='0', type=Type.INT32_T,
                        doc="Transparent or no-draw")                        
           ]),

    Define('MVIEW_CYLINDER3D',
           doc="What parts of the cylinder are closed",
           constants=[
               Constant('MVIEW_CYLINDER3D_OPEN', value='0', type=Type.INT32_T)                        ,
               Constant('MVIEW_CYLINDER3D_CLOSESTART', value='1', type=Type.INT32_T)                        ,
               Constant('MVIEW_CYLINDER3D_CLOSEEND', value='2', type=Type.INT32_T)                        ,
               Constant('MVIEW_CYLINDER3D_CLOSEALL', value='3', type=Type.INT32_T)                        
           ]),

    Define('MVIEW_DRAW',
           doc="Polygon drawing defines",
           constants=[
               Constant('MVIEW_DRAW_POLYLINE', value='0', type=Type.INT32_T,
                        doc="Draw Polylines")                        ,
               Constant('MVIEW_DRAW_POLYGON', value='1', type=Type.INT32_T,
                        doc="Draw Polygons")                        
           ]),

    Define('MVIEW_DRAWOBJ3D_ENTITY',
           doc="What types of entities to draw",
           constants=[
               Constant('MVIEW_DRAWOBJ3D_ENTITY_POINTS', value='0', type=Type.INT32_T,
                        doc="Draw 3D Points (no normals) [1 verticies per object]")                        ,
               Constant('MVIEW_DRAWOBJ3D_ENTITY_LINES', value='1', type=Type.INT32_T,
                        doc="Draw 3D Lines (no normals) [2 verticies per object]")                        ,
               Constant('MVIEW_DRAWOBJ3D_ENTITY_LINE_STRIPS', value='2', type=Type.INT32_T,
                        doc="Draw 3D Line strip (no normals) [2+x verticies per object]")                        ,
               Constant('MVIEW_DRAWOBJ3D_ENTITY_LINE_LOOPS', value='3', type=Type.INT32_T,
                        doc="Draw 3D Line loop (no normals, closes loop with first point) [2+x verticies per object]")                        ,
               Constant('MVIEW_DRAWOBJ3D_ENTITY_TRIANGLES', value='4', type=Type.INT32_T,
                        doc="Draw 3D Triangles [3 verticies per object]")                        ,
               Constant('MVIEW_DRAWOBJ3D_ENTITY_TRIANGLE_STRIPS', value='5', type=Type.INT32_T,
                        doc="Draw 3D Triangle strips [3+x verticies per object]")                        ,
               Constant('MVIEW_DRAWOBJ3D_ENTITY_TRIANGLE_FANS', value='6', type=Type.INT32_T,
                        doc="Draw 3D Triangle fans [3+x verticies per object]")                        ,
               Constant('MVIEW_DRAWOBJ3D_ENTITY_QUADS', value='7', type=Type.INT32_T,
                        doc="Draw 3D Quads (Must be in the same plane) [4 verticies per object]")                        ,
               Constant('MVIEW_DRAWOBJ3D_ENTITY_QUADS_STRIPS', value='8', type=Type.INT32_T,
                        doc="Draw 3D Quad Strips (Must be in the same plane) [4+2x verticies per object]")                        ,
               Constant('MVIEW_DRAWOBJ3D_ENTITY_POLYGONS', value='9', type=Type.INT32_T,
                        doc="Draw 3D Quad Polygones (Must be in the same plane, must be convex and cannot intersect itself)")                        
           ]),

    Define('MVIEW_DRAWOBJ3D_MODE',
           doc="What types of entities to draw",
           constants=[
               Constant('MVIEW_DRAWOBJ3D_MODE_FLAT', value='0', type=Type.INT32_T,
                        doc="Draw flat shaded faces (one normal and color per object)")                        ,
               Constant('MVIEW_DRAWOBJ3D_MODE_SMOOTH', value='1', type=Type.INT32_T,
                        doc="Draw smooth shaded faces (one normal and color per vertex)")                        
           ]),

    Define('MVIEW_EXTENT',
           doc="Types of extents defines",
           constants=[
               Constant('MVIEW_EXTENT_ALL', value='0', type=Type.INT32_T,
                        doc="All objects")                        ,
               Constant('MVIEW_EXTENT_CLIP', value='1', type=Type.INT32_T,
                        doc="Clipping regions")                        ,
               Constant('MVIEW_EXTENT_MAP', value='2', type=Type.INT32_T,
                        doc="Map extents")                        ,
               Constant('MVIEW_EXTENT_VISIBLE', value='3', type=Type.INT32_T,
                        doc="Visible objects")                        
           ]),

    Define('MVIEW_FIT',
           doc="Fit area defines",
           constants=[
               Constant('MVIEW_FIT_MAP', value='0', type=Type.INT32_T,
                        doc="Fit it to the map area")                        ,
               Constant('MVIEW_FIT_VIEW', value='1', type=Type.INT32_T,
                        doc="Fit it to the view area")                        
           ]),

    Define('MVIEW_FONT_WEIGHT',
           doc="Font weight defines",
           constants=[
               Constant('MVIEW_FONT_WEIGHT_NORMAL', value='0', type=Type.INT32_T)                        ,
               Constant('MVIEW_FONT_WEIGHT_ULTRALIGHT', value='1', type=Type.INT32_T)                        ,
               Constant('MVIEW_FONT_WEIGHT_LIGHT', value='2', type=Type.INT32_T)                        ,
               Constant('MVIEW_FONT_WEIGHT_MEDIUM', value='3', type=Type.INT32_T)                        ,
               Constant('MVIEW_FONT_WEIGHT_BOLD', value='4', type=Type.INT32_T)                        ,
               Constant('MVIEW_FONT_WEIGHT_XBOLD', value='5', type=Type.INT32_T)                        ,
               Constant('MVIEW_FONT_WEIGHT_XXBOLD', value='6', type=Type.INT32_T)                        
           ]),

    Define('MVIEW_GRID',
           doc="Grid Drawing defines",
           constants=[
               Constant('MVIEW_GRID_DOT', value='0', type=Type.INT32_T)                        ,
               Constant('MVIEW_GRID_LINE', value='1', type=Type.INT32_T)                        ,
               Constant('MVIEW_GRID_CROSS', value='2', type=Type.INT32_T)                        
           ]),

    Define('MVIEW_GROUP',
           doc="Open Group defines",
           constants=[
               Constant('MVIEW_GROUP_NEW', value='1', type=Type.INT32_T,
                        doc="New Group (destroy any existing group)")                        ,
               Constant('MVIEW_GROUP_APPEND', value='0', type=Type.INT32_T,
                        doc="Append to an existing Group")                        
           ]),

    Define('MVIEW_GROUP_LIST',
           doc="What groups to list",
           constants=[
               Constant('MVIEW_GROUP_LIST_ALL', value='0', type=Type.INT32_T,
                        doc="All the groups.")                        ,
               Constant('MVIEW_GROUP_LIST_MARKED', value='1', type=Type.INT32_T,
                        doc="Those groups marked using the various mark functions.")                        ,
               Constant('MVIEW_GROUP_LIST_VISIBLE', value='2', type=Type.INT32_T,
                        doc="Those groups checked as visible in the view/group manager.")                        
           ]),

    Define('MVIEW_HIDE',
           doc="Boolean hidding defines",
           constants=[
               Constant('HIDE_ON', value='1', type=Type.INT32_T,
                        doc="Turn ON hidding")                        ,
               Constant('HIDE_OFF', value='0', type=Type.INT32_T,
                        doc="Turn OFF hidding")                        
           ]),

    Define('MVIEW_IS',
           doc="Defines for mview types",
           constants=[
               Constant('MVIEW_IS_AGG', value='0', type=Type.INT32_T)                        ,
               Constant('MVIEW_IS_MOVABLE', value='3', type=Type.INT32_T)                        ,
               Constant('MVIEW_IS_CSYMB', value='4', type=Type.INT32_T)                        ,
               Constant('MVIEW_IS_LINKED', value='5', type=Type.INT32_T)                        ,
               Constant('MVIEW_IS_MADE', value='6', type=Type.INT32_T)                        ,
               Constant('MVIEW_IS_HIDDEN', value='7', type=Type.INT32_T)                        ,
               Constant('MVIEW_IS_CLIPPED', value='8', type=Type.INT32_T)                        ,
               Constant('MVIEW_IS_META', value='9', type=Type.INT32_T)                        ,
               Constant('MVIEW_IS_VOXD', value='10', type=Type.INT32_T)                        
           ]),

    Define('MVIEW_LABEL_BOUND',
           doc="Label Binding Defines",
           constants=[
               Constant('MVIEW_LABEL_BOUND_NO', value='0', type=Type.INT32_T,
                        doc="Label Not Bound")                        ,
               Constant('MVIEW_LABEL_BOUND_YES', value='1', type=Type.INT32_T,
                        doc="Label Bound")                        
           ]),

    Define('MVIEW_LABEL_JUST',
           doc="Label Justification Defines",
           constants=[
               Constant('MVIEW_LABEL_JUST_TOP', value='0', type=Type.INT32_T)                        ,
               Constant('MVIEW_LABEL_JUST_BOTTOM', value='1', type=Type.INT32_T)                        ,
               Constant('MVIEW_LABEL_JUST_LEFT', value='2', type=Type.INT32_T)                        ,
               Constant('MVIEW_LABEL_JUST_RIGHT', value='3', type=Type.INT32_T)                        
           ]),

    Define('MVIEW_LABEL_ORIENT',
           doc="Label Orientation Defines",
           constants=[
               Constant('MVIEW_LABEL_ORIENT_HORIZONTAL', value='0', type=Type.INT32_T)                        ,
               Constant('MVIEW_LABEL_ORIENT_TOP_RIGHT', value='1', type=Type.INT32_T)                        ,
               Constant('MVIEW_LABEL_ORIENT_TOP_LEFT', value='2', type=Type.INT32_T)                        
           ]),

    Define('MVIEW_NAME_LENGTH',
           is_constant=True,
           is_single_constant=True,
           doc="maximum length for view and group names",
           constants=[
               Constant('MVIEW_NAME_LENGTH', value='1040', type=Type.INT32_T,
                        doc="Maximum Length (1040)")                        
           ]),

    Define('MVIEW_OPEN',
           doc="Open :class:`MVIEW` define",
           constants=[
               Constant('MVIEW_READ', value='0', type=Type.INT32_T,
                        doc="Read Only - No changes")                        ,
               Constant('MVIEW_WRITENEW', value='1', type=Type.INT32_T,
                        doc="Create new :class:`MVIEW` - destroys any existing :class:`MVIEW`")                        ,
               Constant('MVIEW_WRITEOLD', value='2', type=Type.INT32_T,
                        doc="Open existing :class:`MVIEW` for read/write (must exist)")                        
           ]),

    Define('MVIEW_PJ',
           doc="Projection modes",
           constants=[
               Constant('MVIEW_PJ_OFF', value='0', type=Type.INT32_T,
                        doc="""
                        No reprojection is used and all locations and
                        attributes are assumed to be in the view coordinate
                        system.
                        """)                        ,
               Constant('MVIEW_PJ_LOCATION', value='1', type=Type.INT32_T,
                        doc="""
                        Only locations will be transformed to the view
                        coordinate system.
                        """)                        ,
               Constant('MVIEW_PJ_ALL', value='2', type=Type.INT32_T,
                        doc="""
                        Locations and attributes (sizes, thicknesses, angles)
                        will be transformed to the view coordinate system.
                        """)                        ,
               Constant('MVIEW_PJ_ON', value='3', type=Type.INT32_T,
                        doc="mode before the last :def_val:`MVIEW_PJ_OFF`.")                        
           ]),

    Define('MVIEW_RELOCATE',
           doc="Relocation Defines",
           constants=[
               Constant('MVIEW_RELOCATE_FIT', value='0', type=Type.INT32_T,
                        doc="Will fit the image to fill the specified area")                        ,
               Constant('MVIEW_RELOCATE_ASPECT', value='1', type=Type.INT32_T,
                        doc="Will maintain aspect ratio")                        ,
               Constant('MVIEW_RELOCATE_ASPECT_CENTER', value='2', type=Type.INT32_T,
                        doc="Will maintain aspect ratio and center in specified area")                        
           ]),

    Define('MVIEW_SMOOTH',
           doc="Interpolation method to use for drawing line and polygon edges",
           constants=[
               Constant('MVIEW_SMOOTH_NEAREST', value='0', type=Type.INT32_T,
                        doc="Nearest neighbour")                        ,
               Constant('MVIEW_SMOOTH_CUBIC', value='1', type=Type.INT32_T,
                        doc="Cubic Spline")                        ,
               Constant('MVIEW_SMOOTH_AKIMA', value='2', type=Type.INT32_T,
                        doc="Akima")                        
           ]),

    Define('MVIEW_TILE',
           doc="Tiling defines",
           constants=[
               Constant('MVIEW_TILE_RECTANGULAR', value='0', type=Type.INT32_T)                        ,
               Constant('MVIEW_TILE_DIAGONAL', value='1', type=Type.INT32_T)                        ,
               Constant('MVIEW_TILE_TRIANGULAR', value='2', type=Type.INT32_T)                        ,
               Constant('MVIEW_TILE_RANDOM', value='3', type=Type.INT32_T)                        
           ]),

    Define('MVIEW_UNIT',
           doc="Coordinate systems defines",
           constants=[
               Constant('MVIEW_UNIT_VIEW', value='0', type=Type.INT32_T,
                        doc="view coordinates")                        ,
               Constant('MVIEW_UNIT_PLOT', value='1', type=Type.INT32_T,
                        doc="plot hi-metric (mm*100) on the map.")                        ,
               Constant('MVIEW_UNIT_MM', value='2', type=Type.INT32_T,
                        doc="plot mm on the map.")                        ,
               Constant('MVIEW_UNIT_VIEW_UNWARPED', value='3', type=Type.INT32_T,
                        doc="view coordinates without a warp if there is one")                        
           ]),

    Define('MVIEW_EXTENT_UNIT',
           doc="""
           Types of units for extents (these map to the
           :def:`MVIEW_UNIT` defines directly)
           """,
           constants=[
               Constant('MVIEW_EXTENT_UNIT_VIEW', value='MVIEW_UNIT_VIEW', type=Type.INT32_T,
                        doc=":def_val:`MVIEW_UNIT_VIEW`")                        ,
               Constant('MVIEW_EXTENT_UNIT_PLOT', value='MVIEW_UNIT_PLOT', type=Type.INT32_T,
                        doc=":def_val:`MVIEW_UNIT_PLOT`")                        ,
               Constant('MVIEW_EXTENT_UNIT_MM', value='MVIEW_UNIT_MM', type=Type.INT32_T,
                        doc=":def_val:`MVIEW_UNIT_MM`")                        ,
               Constant('MVIEW_EXTENT_UNIT_VIEW_UNWARPED', value='MVIEW_UNIT_VIEW_UNWARPED', type=Type.INT32_T,
                        doc=":def_val:`MVIEW_UNIT_VIEW_UNWARPED`")                        
           ]),

    Define('TEXT_REF',
           doc="Text reference locations",
           constants=[
               Constant('TEXT_REF_BOTTOM_LEFT', value='0', type=Type.INT32_T)                        ,
               Constant('TEXT_REF_BOTTOM_CENTER', value='1', type=Type.INT32_T)                        ,
               Constant('TEXT_REF_BOTTOM_RIGHT', value='2', type=Type.INT32_T)                        ,
               Constant('TEXT_REF_MIDDLE_LEFT', value='3', type=Type.INT32_T)                        ,
               Constant('TEXT_REF_MIDDLE_CENTER', value='4', type=Type.INT32_T)                        ,
               Constant('TEXT_REF_MIDDLE_RIGHT', value='5', type=Type.INT32_T)                        ,
               Constant('TEXT_REF_TOP_LEFT', value='6', type=Type.INT32_T)                        ,
               Constant('TEXT_REF_TOP_CENTER', value='7', type=Type.INT32_T)                        ,
               Constant('TEXT_REF_TOP_RIGHT', value='8', type=Type.INT32_T)                        
           ]),

    Define('MVIEW_3D_RENDER',
           doc="""
           3D Geometry rendering defines. These flags only affect mixed geometry groups and not the data
           specific groups (e.g. voxels, vector voxels surfaces etc.). Each of those groups 
           has predefined optimum behaviour and any changes to these flags are ignored.
           """,
           constants=[
               Constant('MVIEW_3D_RENDER_BACKFACES', value='1', type=Type.INT32_T,
                        doc="This flag is enabled if the backfaces of geometry should be rendered")                        ,
               Constant('MVIEW_3D_DONT_SCALE_GEOMETRY', value='2', type=Type.INT32_T,
                        doc="""
                        If the exaggeration scales of the 3D view in X, Y and/or Z is set to anything other than 1.0
                        any geometric objects (spheres, cubes etc.) for 3D groups with the following flags 
                        will render untransformed while only the centers of the objects are changed.
                        This ensures the objects appear in the correct place with respect to other data being rendered (and scaled).
                        """)                        
           ])]


gx_methods = {
    '3D Entity': [

        Method('Box3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D box",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Min Z"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Max Z")
               ]),

        Method('CRCView_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Generate an XML CRC of a View",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="CRC returned"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of xml to generate (.zip added)")
               ]),

        Method('CRCViewGroup_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Generate an XML CRC of a Group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of Group"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="CRC returned"),
                   Parameter('p4', type=Type.STRING,
                             doc="Name of xml to generate (.zip added)")
               ]),

        Method('Cylinder3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D cylinder",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Start X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Start Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Start Z"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="End X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="End Y"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="End Z"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Start Radius (can be zero)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="End Radius (can be zero)"),
                   Parameter('p10', type=Type.INT32_T,
                             doc=":def:`MVIEW_CYLINDER3D`")
               ]),

        Method('DrawObject3D_MVIEW', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D object optimized for rendering",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_DRAWOBJ3D_ENTITY`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MVIEW_DRAWOBJ3D_MODE`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Number of Objects"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Default Count (if variable and not specified)"),
                   Parameter('p6', type="VV",
                             doc="Verticies X"),
                   Parameter('p7', type="VV",
                             doc="Verticies Y"),
                   Parameter('p8', type="VV",
                             doc="Verticies Z"),
                   Parameter('p9', type="VV",
                             doc="Normals X (can be NULL)"),
                   Parameter('p10', type="VV",
                             doc="Normals Y (can be NULL)"),
                   Parameter('p11', type="VV",
                             doc="Normals Z (can be NULL)"),
                   Parameter('p12', type="VV",
                             doc="Colors :class:`VV` (can be NULL)"),
                   Parameter('p13', type="VV",
                             doc="Index  :class:`VV` (can be NULL)"),
                   Parameter('p14', type="VV",
                             doc="Count  :class:`VV` (can be NULL)")
               ]),

        Method('DrawSurface3DEx_MVIEW', module='geoengine.map', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D object built from triangles",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name"),
                   Parameter('p3', type="VV",
                             doc="Vertices X (:def_val:`GS_REAL`)"),
                   Parameter('p4', type="VV",
                             doc="Vertices Y (:def_val:`GS_REAL`)"),
                   Parameter('p5', type="VV",
                             doc="Vertices Z (:def_val:`GS_REAL`)"),
                   Parameter('p6', type="VV",
                             doc="Normals X (:def_val:`GS_REAL`)"),
                   Parameter('p7', type="VV",
                             doc="Normals Y (:def_val:`GS_REAL`)"),
                   Parameter('p8', type="VV",
                             doc="Normals Z (:def_val:`GS_REAL`)"),
                   Parameter('p9', type="VV",
                             doc="Colors :class:`VV` (:def_val:`GS_INT`) [can be NULL]"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Color used if above :class:`VV` is NULL [0 for :class:`MVIEW`'s fillcolor]"),
                   Parameter('p11', type="VV",
                             doc="Triangles Point 1 (:def_val:`GS_INT`)"),
                   Parameter('p12', type="VV",
                             doc="Triangles Point 2 (:def_val:`GS_INT`)"),
                   Parameter('p13', type="VV",
                             doc="Triangles Point 3 (:def_val:`GS_INT`)"),
                   Parameter('p14', type="IPJ",
                             doc="Native :class:`IPJ` of 3D object")
               ]),

        Method('DrawSurface3DFromFile_MVIEW', module='geoengine.map', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D object from a surface file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Surface file")
               ]),

        Method('FontWeightLST_MVIEW', module='geoengine.map', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Fill a :class:`LST` with the different font weights.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('GetAGGFileNames_MVIEW', module='geoengine.map', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Get the names of grid files stored in an :class:`AGG`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="group name"),
                   Parameter('p3', type="VV",
                             doc="returned string :class:`VV` of type -:def_val:`STR_FILE`")
               ]),

        Method('IGetMeta_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Retrieves Metadata from a group",
               return_type="META",
               return_doc=":class:`META` Object",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Meta name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Length of Meta name variable")
               ]),

        Method('MeasureText_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Compute the bounding rectangle in view units of the text using the current attributes.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Text string"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X minimum"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y minimum"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="X maximum"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Y maximum")
               ]),

        Method('Point3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D point.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z")
               ]),

        Method('PolyLine3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D polyline.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type="VV",
                             doc="X coordinates."),
                   Parameter('p3', type="VV",
                             doc="Y coordinates."),
                   Parameter('p4', type="VV",
                             doc="Z coordinates.")
               ]),

        Method('RelocateGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Re-locate a group in a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="view"),
                   Parameter('p2', type=Type.STRING,
                             doc="group name"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="area X minimum"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="area Y minimum"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="area X maximum"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="area Y maximum"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`MVIEW_RELOCATE`")
               ]),

        Method('SetMeta_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Update the :class:`META` in this group with the new meta object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p3', type="META",
                             doc=":class:`META` object"),
                   Parameter('p4', type=Type.STRING,
                             doc="Meta name of Object")
               ]),

        Method('Sphere3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Draw a 3D sphere",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Center X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Center Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Center Z"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Radius")
               ]),

        Method('UpdateMETAfromGroup_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Fill the :class:`META` with group dataset information",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p3', type="META",
                             doc=":class:`META` object to fill")
               ])
    ],
    '3D Plane': [

        Method('DeletePlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Delete a plane in a view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="plane number to delete"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="TRUE to delete all groups on the plane")
               ]),

        Method('GetPlaneClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Plane Clip Region",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('p3', type="PLY",
                             doc="Clip Region")
               ]),

        Method('GetPlaneEquation_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get the equation of a plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation about X (Y toward Z +ve, between -360 and 360)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation about Y (Z toward X +ve, between -360 and 360)"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation about Z (Y toward X +ve, between -360 and 360)"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="X offset of plane"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Y offset of plane"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Z offset of plane"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="X scale"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Y scale"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="Z scale")
               ]),

        Method('GetViewPlaneEquation_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get the View's Plane Equation",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Angle in X"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Angle in Y"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Angle in Z"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Offset in X"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Offset in Y"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Offset in Z"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Scale in X"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Scale in Y"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Scale in Z")
               ]),

        Method('iCreatePlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Create a 3D Plane for 2D Groups",
               return_type=Type.INT32_T,
               return_doc="x - Index of plane",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of Plane")
               ]),

        Method('iFindPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Find a plane in a view",
               return_type=Type.INT32_T,
               return_doc="Plane number, -1 if not found",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="name of the plane")
               ]),

        Method('IGetDefPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get the default drawing plane.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="maximum name length")
               ]),

        Method('iIsView3D_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Is the view 3D?",
               return_type=Type.INT32_T,
               return_doc="TRUE if view is 3D",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object")
               ]),

        Method('iIsSection_MVIEW', module='geoengine.map', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Is the view a section view?",
               return_type=Type.INT32_T,
               return_doc="TRUE if view is a section view.",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object")
               ]),

        Method('ListPlaneGroups_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="List all groups in a specific plane of a 3D view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="plane number"),
                   Parameter('p3', type="LST",
                             doc="List of plane names and numbers")
               ]),

        Method('ListPlanes_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="List all planes in a 3D view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type="LST",
                             doc="List of plane names and numbers")
               ]),

        Method('SetAllGroupsToPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set all groups to be within one plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Plane Index to set all groups to")
               ]),

        Method('SetAllNewGroupsToPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set all groups that are not in any plane to this plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Plane Index to set all groups to")
               ]),

        Method('SetDefPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the default drawing plane.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="name")
               ]),

        Method('SetGroupToPlane_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set a group to a plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Plane Index to set all groups to"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of group to set")
               ]),

        Method('SetH3DN_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the :class:`3DN` object for this view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type="3DN",
                             doc=":class:`3DN` to set (NULL for 2D view)")
               ]),

        Method('SetPlaneClipPLY_MVIEW', module='geoengine.map', version='5.1.4',
               availability=Availability.PUBLIC, 
               doc="Set the Plane Clip Region",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('p3', type="PLY",
                             doc="Clip Region")
               ]),

        Method('SetPlaneEquation_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the equation of a plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Rotation about X (Z toward Y +ve, between -360 and 360)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Rotation about Y (Z toward X +ve, between -360 and 360)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Rotation about Z (Y toward X +ve, between -360 and 360)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="X offset of plane"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Y offset of plane"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Z offset of plane"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="X scale"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Y scale"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Z scale")
               ]),

        Method('SetPlaneSurface_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the surface image of a plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('p3', type=Type.STRING,
                             doc="Optional surface image/grid name, can be NULL")
               ]),

        Method('SetPlaneSurfInfo_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the surface information",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Sample rate (>=1)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Base"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Scale"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Min"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Max")
               ])
    ],
    '3D Rendering 2D': [

        Method('DefinePlane3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Define a 2D drawing plane based on point and normal",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Center point X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Center point Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Center point Z"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X Vector X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="X Vector Y"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="X Vector Z"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Y Vector X"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Y Vector Y"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Y Vector Z")
               ]),

        Method('DefineViewerAxis3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="""
               Define a 2D drawing plane based on the user's view that
               oriented around the vector.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Center point X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Center point Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Center point Z"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Directional Point X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Directional Point Y"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Directional Point Z")
               ]),

        Method('DefineViewerPlane3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Define a 2D drawing plane based on the user's view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Center point X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Center point Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Center point Z")
               ])
    ],
    'Clipping': [

        Method('_ClipPolyEx_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a polygon to the clip region.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Exclude")
               ]),

        Method('_ClipRectEx_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a rectangle to the clip region.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X minimum"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y minimum"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X maximum"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y maximum"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Exclude")
               ]),

        Method('ClipClear_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Remove/clear the view clip region.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle")
               ]),

        Method('ClipGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Clipping mode on/off for all groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_CLIP`")
               ]),

        Method('ClipMarkedGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Clipping mode on/off for marked groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_CLIP`")
               ]),

        Method('ClipPoly_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a polygon to the clip region.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`")
               ]),

        Method('ClipRect_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a rectangle to the clip region.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X minimum"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y minimum"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X maximum"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y maximum"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`")
               ]),

        Method('DeleteExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Deletes an extended clip :class:`PLY` object used by this view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Extended ClipPLY number")
               ]),

        Method('ExtClipPLYList_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the names of existing extended clip :class:`PLY` objects in this view as list.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type="LST")
               ]),

        Method('GetClipPLY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get clipping polygons, in the user projection",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type="PLY",
                             doc="Poly")
               ]),

        Method('GetExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get an extended clip :class:`PLY` object used by this view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Extended ClipPLY number"),
                   Parameter('p3', type="PLY",
                             doc=":class:`PLY` object to get")
               ]),

        Method('GetGroupExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets extended clip information for group in view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Extended :class:`PLY` number (returned, -1 if not set)")
               ]),

        Method('GetPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get clipping polygons, in the base projection",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type="PLY",
                             doc="Poly")
               ]),

        Method('GroupClipMode_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Clipping mode on or off for new groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_CLIP`")
               ]),

        Method('IGetNameExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the name of the extended clip :class:`PLY` object in this view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Extended ClipPLY number"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Length of Name variable")
               ]),

        Method('iNumExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of extended clip :class:`PLY` objects in this view.",
               return_type=Type.INT32_T,
               return_doc="Number of PLYs",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object")
               ]),

        Method('iSetExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Set an extended clip :class:`PLY` object used by this view.",
               return_type=Type.INT32_T,
               return_doc="Index of new or changed :class:`PLY`, -1 on error",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Extended ClipPLY number, If  >= :func:`iNumExtClipPLY_MVIEW`(View) it will be added to the end of the current list"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name (Has to be unique, otherwise error will be returned)"),
                   Parameter('p4', type="PLY",
                             doc=":class:`PLY` object to set, use (:class:`PLY`)0 to rename an existing object")
               ]),

        Method('SetClipPLY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set clipping region to a :class:`PLY`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type="PLY",
                             doc="Poly")
               ]),

        Method('SetGroupExtClipPLY_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets extended clip information for group in view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Extended :class:`PLY` number (-1 to clear)")
               ])
    ],
    'Color': [

        Method('Color2RGB_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Convert to RGB values.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Color value"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Red"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Green"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Blue")
               ]),

        Method('ColorDescr_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a colour to a colour string label",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="COL_ANY variable"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="colour descriptor returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="length of the string")
               ]),

        Method('iColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a color from a colour string label",
               return_type=Type.INT32_T,
               return_doc="colour int",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="colour name string")
               ]),

        Method('iColorCMY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return CMY color.",
               return_type=Type.INT32_T,
               return_doc="colour int based on color model.",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Cyan"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Magenta"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Yellow")
               ]),

        Method('iColorHSV_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return HSV color.",
               return_type=Type.INT32_T,
               return_doc="colour int based on color model.",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Hue"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Saturation"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Color")
               ]),

        Method('iColorRGB_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return RGB color.",
               return_type=Type.INT32_T,
               return_doc="colour int based on color model.",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Red"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Green"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Blue")
               ])
    ],
    'Drawing Attribute': [

        Method('ClipMode_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the view clipping mode on or off.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_CLIP`")
               ]),

        Method('FillColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the fill color.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="color")
               ]),

        Method('LineColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the line color.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Color")
               ]),

        Method('LineSmooth_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set the line edge smoothing.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_SMOOTH`")
               ]),

        Method('LineStyle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the style of a line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Line Style #, see default.lpt"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Pitch in view units")
               ]),

        Method('LineThick_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the line thickness.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="line thickness in view space units")
               ]),

        Method('PatAngle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the pattern angle",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Angle")
               ]),

        Method('PatDensity_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the tiling density.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Relative density (default = 1).")
               ]),

        Method('PatNumber_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the pattern number",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Pattern number")
               ]),

        Method('PatSize_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the pattern unit cell size (X)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Pattern size in view units")
               ]),

        Method('PatStyle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the tiling method (i.e. rectangle, triangle)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_TILE`")
               ]),

        Method('PatThick_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the pattern line thickness",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Line thickness as fraction of pattern size (ie. 0.05)")
               ]),

        Method('SymbAngle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Symb angle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="angle in degrees CCW from +X")
               ]),

        Method('SymbColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Symbol color.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="color")
               ]),

        Method('SymbFillColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Symbol color fill.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Color")
               ]),

        Method('SymbFont_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the symbol font and style.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="face name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Geosoft font? :def:`GEO_BOOL`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`MVIEW_FONT_WEIGHT`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Italic font? :def:`GEO_BOOL`")
               ]),

        Method('SymbNumber_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Symbol number.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="symbol number")
               ]),

        Method('SymbSize_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Symb size.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="size in view units")
               ]),

        Method('TextAngle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the text angle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="angle in degrees CCW from +X")
               ]),

        Method('TextColor_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Text color.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="color")
               ]),

        Method('TextFont_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the text font.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Font face name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Geosoft font? (TRUE or FALSE)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`MVIEW_FONT_WEIGHT`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Italic font? (TRUE or FALSE)")
               ]),

        Method('TextRef_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the text plot reference point.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`TEXT_REF`")
               ]),

        Method('TextSize_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the text size.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="size in view units")
               ]),

        Method('Transparency_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the transparency for new objects.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Transparency (1.0 - Opaque, 0.0 - Transparent)")
               ]),

        Method('ZValue_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets Z-value info.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Z-Value")
               ])
    ],
    'Drawing Entity': [

        Method('Arc_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw an arc.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="center x"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="center y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="radius"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="ratio x/y"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="angle"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="start angle"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="end angle")
               ]),

        Method('Chord_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a filled arc.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="center x"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="center y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="radius"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="ratio x/y"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="angle"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="start angle"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="end angle")
               ]),

        Method('ClassifiedSymbols_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Plot classified symbols",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('p4', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="scale factor to convert mm to view units"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Classified minimum Z to plot"),
                   Parameter('p7', type=Type.STRING,
                             doc="comma delimited list of Z maximums"),
                   Parameter('p8', type=Type.STRING,
                             doc="comma delimited list of sizes in mm"),
                   Parameter('p9', type=Type.STRING,
                             doc="comma delimited list of colour strings")
               ]),

        Method('ComplexPolygon_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a polygon with holes in it.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` of type int holding the number of points for each polygon"),
                   Parameter('p3', type="VV",
                             doc="X coordinates."),
                   Parameter('p4', type="VV",
                             doc="Y coordinates.")
               ]),

        Method('Ellipse_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw an ellipse",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="center x"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="center y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="radius"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="ratio x/y"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="angle")
               ]),

        Method('Line_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="x0"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="y0"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="x1"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="y1")
               ]),

        Method('LineVV_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw line segments stored in a GS_D2LINE :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` for GS_D2LINE")
               ]),

        Method('PolygonDm_MVIEW', module='geoengine.map', version='5.0.6',
               availability=Availability.PUBLIC, 
               doc="Like PolyLineDm, but draw polygons.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type="VV",
                             doc="X coordinates."),
                   Parameter('p3', type="VV",
                             doc="Y coordinates.")
               ]),

        Method('PolygonPLY_MVIEW', module='geoengine.map', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Draw a complex polygon from :class:`PLY`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type="PLY")
               ]),

        Method('PolyLine_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a polyline or polygon (dummies deleted).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_DRAW`"),
                   Parameter('p3', type="VV",
                             doc="X coordinates."),
                   Parameter('p4', type="VV",
                             doc="Y coordinates.")
               ]),

        Method('PolyLineDm_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a polyline with gaps defined by dummies in X/Y VVs",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type="VV",
                             doc="X coordinates."),
                   Parameter('p3', type="VV",
                             doc="Y coordinates.")
               ]),

        Method('PolyWrap_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw wrapped polylines from X and Y :class:`VV`'s.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type="VV",
                             doc="X coordinates."),
                   Parameter('p3', type="VV",
                             doc="Y coordinates.")
               ]),

        Method('Rectangle_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a rectangle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="x0"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="y0"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="x1"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="y1")
               ]),

        Method('Segment_MVIEW', module='geoengine.map', version='5.0.7',
               availability=Availability.PUBLIC, 
               doc="Draw a filled segment of an ellipse.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="center x"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="center y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="radius"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="ratio x/y"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="angle"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="start angle"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="end angle")
               ]),

        Method('SizeSymbols_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Plot sized symbols",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="VV",
                             doc="X"),
                   Parameter('p3', type="VV",
                             doc="Y"),
                   Parameter('p4', type="VV",
                             doc="symbol sizes (in view units)")
               ]),

        Method('Symbol_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Plot a symbol",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y")
               ]),

        Method('Symbols_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Plot symbols",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="VV",
                             doc="X"),
                   Parameter('p3', type="VV",
                             doc="Y")
               ]),

        Method('SymbolsITR_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Plot symbols using an :class:`ITR`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc=":class:`ITR` file name (ZON or :class:`ITR`)"),
                   Parameter('p3', type="VV",
                             doc="X"),
                   Parameter('p4', type="VV",
                             doc="Y"),
                   Parameter('p5', type="VV",
                             doc="Z")
               ]),

        Method('Text_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw text.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="text to plot"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="x location of text"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="y location of text")
               ])
    ],
    'Drawing Object': [

        Method('Aggregate_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add an aggregate to a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="AGG",
                             doc="Aggregate"),
                   Parameter('p3', type=Type.STRING,
                             doc="Aggregate name Maximum length is :def_val:`MVIEW_NAME_LENGTH`")
               ]),

        Method('ChangeLineMessage_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Change the specified line in a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Change to this line")
               ]),

        Method('ColSymbol_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a colored symbol object to a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the color symbol group"),
                   Parameter('p3', type="CSYMB",
                             doc=":class:`CSYMB` object")
               ]),

        Method('DATALINKD_MVIEW', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Add a Data Link Display (:class:`DATALINKD`) object to the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="DATALINKD"),
                   Parameter('p3', type=Type.STRING,
                             doc="name Maximum length is :def_val:`MVIEW_NAME_LENGTH`")
               ]),

        Method('EasyMaker_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Used for GX makers which use both maps and databases.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Maker name, used in menu prompt"),
                   Parameter('p3', type=Type.STRING,
                             doc='INI groups (terminate each with a ";")')
               ]),

        Method('EMFObject_MVIEW', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Add an EMF file data object to the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('p6', type=Type.STRING,
                             doc="EMF File holding data")
               ]),

        Method('ExternalStringObject_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add an external string data object to the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('p6', type=Type.STRING,
                             doc="name of external object"),
                   Parameter('p7', type=Type.STRING,
                             doc="class of external object"),
                   Parameter('p8', type=Type.STRING,
                             doc="string data of external object")
               ]),

        Method('Link_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Make a link to a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type="DB",
                             doc="Database handle"),
                   Parameter('p3', type=Type.STRING,
                             doc="Link name")
               ]),

        Method('Maker_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Generates a Maker for the database and/or map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Database required? (0 = No, 1 = Yes)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Map required?      (0 = No, 1 = Yes)"),
                   Parameter('p4', type=Type.STRING,
                             doc="Program name"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`MAKER`"),
                   Parameter('p6', type=Type.STRING,
                             doc="Maker name, used in menu prompt"),
                   Parameter('p7', type=Type.STRING,
                             doc='INI groups (terminate each with a ";")')
               ]),

        Method('Meta_MVIEW', module='geoengine.map', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Store Metadata in a group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type="META",
                             doc=":class:`META` object"),
                   Parameter('p3', type=Type.STRING,
                             doc="Menu name of Object")
               ]),

        Method('VOXD_MVIEW', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Add a Voxel Display (:class:`VOXD`) object to the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="VOXD"),
                   Parameter('p3', type=Type.STRING,
                             doc="name Maximum length is :def_val:`MVIEW_NAME_LENGTH`")
               ]),

        Method('GetVOXD_MVIEW', module='geoengine.map', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Get an existing :class:`VOXD` object from the view.",
               return_type="VOXD",
               return_doc=":class:`VOXD` object - cache only - use immediately.",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="group number")
               ]),

        Method('DrawVectorVoxelVectors_MVIEW', module='geoengine.map', version='7.6.0',
               availability=Availability.PUBLIC, 
               doc="Display vectors from a vector voxel in the view.",
               return_type=Type.VOID,
               return_doc="Each data value in a vector voxel contains X, Y and Z components of a vector. The amplitudes do NOT necessarily correspond to the spatial size of the voxel.",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="VOX"),
                   Parameter('p3', type=Type.STRING,
                             doc="view group name Maximum length is :def_val:`MVIEW_NAME_LENGTH`"),
                   Parameter('p4', type="ITR",
                             doc="Image transform - must contain zones"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Vector length scale factor - w.r.t. the voxel minimum horizontal cell size (default 1)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Ratio of the vector cone height to its base (default 4)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Ratio of maximum base size to minimum horizontal cell size (default 0.25)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Cutoff value - do not plot vectors with amplitudes less than this value (:def_val:`rDUMMY` or 0 to plot all)"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Maximum number of vectors - decimate as required to reduce (:def_val:`iDUMMY` to plot all)")
               ]),

        Method('DrawVectors3D_MVIEW', module='geoengine.map', version='8.0.1',
               availability=Availability.PUBLIC, 
               doc="Display vectors in the view.",
               return_type=Type.VOID,
               return_doc="Plot vectors as cones scaled in area to the maximum amplitude",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="view group name Maximum length is :def_val:`MVIEW_NAME_LENGTH`"),
                   Parameter('p3', type="VV",
                             doc="X locations"),
                   Parameter('p4', type="VV",
                             doc="Y locations"),
                   Parameter('p5', type="VV",
                             doc="Z locations"),
                   Parameter('p6', type="VV",
                             doc="Vector X component"),
                   Parameter('p7', type="VV",
                             doc="Vector Y component"),
                   Parameter('p8', type="VV",
                             doc="Vector Z component"),
                   Parameter('p9', type="ITR",
                             doc="Image transform - must contain zones"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="""
                             Scale factor for the longest vector in map units / vector units. Vector lengths for the rest of the vectors scale by the square root of the vector amplitudes.
                             This results in the apparent (viewed) area of the vector being proportional to the amplitude.
                             """),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Ratio of the vector cone height to its base (default 4)"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="Maximum base size in view units. Leave blank (dummy) for no limit. If applied this can make larger vectors skinnier, but does not reduce the length, so they don't obscure other vectors as much.")
               ])
    ],
    'Group Methods': [

        Method('CopyMarkedGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copies all marked groups from one view into another view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="Source :class:`MVIEW`"),
                   Parameter('p2', type="MVIEW",
                             doc="Destination :class:`MVIEW`")
               ]),

        Method('CopyRawMarkedGroups_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Copies all marked groups raw from one view into another",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="Source :class:`MVIEW`"),
                   Parameter('p2', type="MVIEW",
                             doc="Destination :class:`MVIEW`")
               ]),

        Method('CRCGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Compute CRC for a group.",
               return_type="CRC",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="view"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name"),
                   Parameter('p3', type="CRC",
                             doc="CRC to start (use :def_val:`CRC_INIT_VALUE`)")
               ]),

        Method('DeleteGroup_MVIEW', module='geoengine.map', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Delete a group.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('DelMarkedGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete marked groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle")
               ]),

        Method('GetGroupExtent_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get extent of a group in a view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="group name"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum X, returned"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum Y, returned"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum X, returned"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum Y, returned"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`")
               ]),

        Method('GetGroupTransparency_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the transparency value of group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Transparency (1.0 - Opaque, 0.0 - Transparent)")
               ]),

        Method('GroupToPLY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Save all polygons in group into :class:`PLY` obj.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="view"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name"),
                   Parameter('p3', type="PLY",
                             doc=":class:`PLY` to add to")
               ]),

        Method('HideMarkedGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Hide/Show marked groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_HIDE`")
               ]),

        Method('HideShadow2DInterpretations_MVIEW', module='geoengine.map', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Hide/Show 2d shadow interpretations.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_HIDE`")
               ]),

        Method('iExistGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Checks to see if a group exists.",
               return_type=Type.INT32_T,
               return_doc="""
               0  - group does not exist.
               1  - group exists.
               """,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('IGenNewGroupName_MVIEW', module='geoengine.map', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="""
               Generate the name of a group from a base name that
               is new. (always unique and won't overwrite existing
               objects).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Base Name of group"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="New Name of group"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_GROUP',
                             doc="Size of buffer.")
               ]),

        Method('iIsGroup_MVIEW', module='geoengine.map', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Query a status or characteristic of a group",
               return_type=Type.INT32_T,
               return_doc="TRUE or FALSE (1 or 0)",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="group name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MVIEW_IS`")
               ]),

        Method('iIsGroupEmpty_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Is the group empty?",
               return_type=Type.INT32_T,
               return_doc="TRUE or FALSE (1 or 0)",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="group name")
               ]),

        Method('iIsMovable_MVIEW', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Is this view movable?",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="MVIEW")
               ]),

        Method('iIsVisible_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Is this view visible?",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="MVIEW")
               ]),

        Method('iListGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a list of the groups in a view.",
               return_type=Type.INT32_T,
               return_doc="Number of groups in the list",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type="LST",
                             doc="list"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MVIEW_GROUP_LIST`")
               ]),

        Method('iRenderOrder_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Query the view render order",
               return_type=Type.INT32_T,
               return_doc="Render order",
               parameters = [
                   Parameter('p1', type="MVIEW")
               ]),

        Method('MarkAllGroups_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Mark or unmark all groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="0 - unmark, 1 - mark")
               ]),

        Method('MarkEmptyGroups_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Mark/unmark all empty groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="0 - unmark, 1 - mark")
               ]),

        Method('MarkGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Mark or unmark a specific group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="group name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="0 - unmark, 1 - mark")
               ]),

        Method('MoveGroupBackward_MVIEW', module='geoengine.map', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Move the group backward one position (render sooner).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('MoveGroupForward_MVIEW', module='geoengine.map', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Move the group forward one position (render later).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('MoveGroupToBack_MVIEW', module='geoengine.map', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Move the group to the back (render first).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('MoveGroupToFront_MVIEW', module='geoengine.map', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Move the group to the front (render last).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('RenameGroup_MVIEW', module='geoengine.map', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Rename a group.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Old group name"),
                   Parameter('p3', type=Type.STRING,
                             doc="New group name")
               ]),

        Method('SetGroupMoveable_MVIEW', module='geoengine.map', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Set the movable attribute of a group.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="group name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="0 - not movable, 1 - movable")
               ]),

        Method('SetGroupTransparency_MVIEW', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the transparency value of group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Transparency  (1.0 - Opaque, 0.0 - Transparent)")
               ]),

        Method('SetMarkMoveable_MVIEW', module='geoengine.map', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Set the movable attribute of marked groups.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="0 - not movable, 1 - movable")
               ]),

        Method('SetMovability_MVIEW', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Set the view movability",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL`")
               ]),

        Method('SetRenderOrder_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set the view render order",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Render order")
               ]),

        Method('SetVisibility_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set the view visibility",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL`")
               ]),

        Method('StartGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Start a group.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name, can be NULL, Maximum length is :def_val:`MVIEW_NAME_LENGTH`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MVIEW_GROUP`")
               ])
    ],
    'Projection': [

        Method('_SetWorkingIPJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the working projection of the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="IPJ",
                             doc="The input projection")
               ]),

        Method('ClearESRILDTs_MVIEW', module='geoengine.map', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Clear ESRI local datum transformations currently in use.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View")
               ]),

        Method('iIsProjectionEmpty_MVIEW', module='geoengine.map', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns 1 if the view projection and view user projection are both empty (undefined).",
               return_type=Type.INT32_T,
               return_doc="1 if the view projection and view user projection are both empty.",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object")
               ]),

        Method('GetIPJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the projection of the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` in which to place the view :class:`IPJ`")
               ]),

        Method('GetUserIPJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the user projection of the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` in which to place the view :class:`IPJ`")
               ]),

        Method('ModePJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the working projection mode",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_PJ`")
               ]),

        Method('rNorth_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns North direction at center of view.",
               return_type=Type.DOUBLE,
               return_doc="North direction id deg. azimuth relative to view Y.",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object")
               ]),

        Method('SetIPJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the projection of the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` to place in the view")
               ]),

        Method('SetUserIPJ_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the user projection of the view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` to place in the view")
               ])
    ],
    'Render': [

        Method('iGet3DGroupFlags_MVIEW', module='geoengine.map', version='9.1.0',
               availability=Availability.PUBLIC, 
               doc="Get a 3D geometry group's 3D rendering flags.",
               return_type=Type.INT32_T,
               return_doc="Combination of :def:`MVIEW_3D_RENDER` flags or 0",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Group number")
               ]),

        Method('Set3DGroupFlags_MVIEW', module='geoengine.map', version='9.1.0',
               availability=Availability.PUBLIC, 
               doc="Set a 3D geometry group's 3D rendering flags.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Combination of :def:`MVIEW_3D_RENDER` flags or 0")
               ]),

        Method('_GetGroupFreezeScale_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get a scale freezing value for the group (:def_val:`rDUMMY` for disabled).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Variable to fill with freeze scale")
               ]),

        Method('_SetFreezeScale_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Set a scale freezing value into stream (:def_val:`rDUMMY` for disabled).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Freeze Scale value")
               ]),

        Method('_SetGroupFreezeScale_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Set a scale freezing value for the group (:def_val:`rDUMMY` for disabled).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Group number"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Variable to fill with freeze scale")
               ]),

        Method('iFindGroup_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Find a Group by name.",
               return_type=Type.INT32_T,
               return_doc="Group Number.",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name")
               ]),

        Method('IGroupName_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get a group name",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="group number, error if not valid"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Group Name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="maximum name length")
               ]),

        Method('Render_MVIEW', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, no_gxh=True, 
               doc="Render a specified area of view onto a Windows DC handle",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` Handle"),
                   Parameter('p2', type="HDC", is_val=True,
                             doc="DC Handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="left value of the render rect in Windows coordinates (bottom>top)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="bottom value"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="right value"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="top value"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="area X minimum"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="area Y minimum"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="area X maximum"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="area Y maximum")
               ])
    ],
    'Utility Drawing': [

        Method('_SetUFac_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the unit conversion of a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View to set UFac to"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="New UFac value")
               ]),

        Method('AxisX_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw an X axis",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="view"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y location in view units"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="left  X"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="right X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="major tick interval"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="minor tick interval (half size of major)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="tick size in view units (negative for down ticks)")
               ]),

        Method('AxisY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a  Y axis",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="view"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location in view units"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="bottom Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="top    Y"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="major tick interval"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="minor tick interval (half size of major)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="tick size in view units (negative for left ticks)")
               ]),

        Method('Grid_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Draw a grid in the current window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="view"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X grid increment"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y grid increment"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="dX dot increment/cross X size"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="dY dot increment/cross Y size"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`MVIEW_GRID`")
               ]),

        Method('LabelFid_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Label fiducials on a profile",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="view"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="fiducial start"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="fiducial increment"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="fiducial label interval, default 100.0"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Y location in view unit"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Y scale")
               ]),

        Method('LabelX_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Label annotations on the X axis",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="view"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y location in view units"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="left  X"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="right X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="label interval"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_JUST`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_BOUND`"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_ORIENT`")
               ]),

        Method('LabelY_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Label annotations on the Y axis",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="view"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location in view units"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="bottom Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="top    Y"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="label interval"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_JUST`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_BOUND`"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`MVIEW_LABEL_ORIENT`")
               ]),

        Method('OptimumTick_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Return a default optimum tick interval",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="minimum of range"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="maximum"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="optimum interval")
               ])
    ],
    'View': [

        Method('Create_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create :class:`MVIEW`.",
               return_type="MVIEW",
               return_doc=":class:`MVIEW`, aborts if creation fails",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` on which to place the view"),
                   Parameter('p2', type=Type.STRING,
                             doc="View name (maximum :def_val:`MVIEW_NAME_LENGTH`)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MVIEW_OPEN`")
               ]),

        Method('CreateCrookedSection_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Creates a new crooked section view.",
               return_type="MVIEW",
               return_doc=":class:`MVIEW`, aborts if creation fails",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Object"),
                   Parameter('p2', type="IPJ",
                             doc="Geographic projection of input X, Y locations below (without orientation)"),
                   Parameter('p3', type=Type.STRING,
                             doc="View Name"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Base view bottom left corner X (mm)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Base view bottom left corner Y (mm)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Base view size in X (mm)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Base view size in Y (mm)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Map horizontal scale (X-axis)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Vertical exaggeration (1.0 is normal, must be >0.0)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Starting distance at the left side of the view."),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Elevation at TOP of the view"),
                   Parameter('p12', type="VV",
                             doc="Cumulative distances along the secton"),
                   Parameter('p13', type="VV",
                             doc="True X locations along the section"),
                   Parameter('p14', type="VV",
                             doc="True Y locations along the section")
               ]),

        Method('CreateCrookedSectionDataProfile_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Creates a new crooked section data profile view.",
               return_type="MVIEW",
               return_doc=":class:`MVIEW`, aborts if creation fails",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Object"),
                   Parameter('p2', type="IPJ",
                             doc="Geographic projection of input X, Y locations below (without orientation)"),
                   Parameter('p3', type=Type.STRING,
                             doc="View Name"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Base view bottom left corner X (mm)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Base view bottom left corner Y (mm)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Base view size in X (mm)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Base view size in Y (mm)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Map horizontal scale (X-axis)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Starting distance at the left side of the view."),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Data value at bottom of the view"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Data value at top of the view"),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Make logarithmic Y-axis (0:No, 1:Yes)?"),
                   Parameter('p13', type="VV",
                             doc="Cumulative distances along the secton"),
                   Parameter('p14', type="VV",
                             doc="True X locations along the section"),
                   Parameter('p15', type="VV",
                             doc="True Y locations along the section")
               ]),

        Method('Destroy_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`MVIEW` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` Handle")
               ]),

        Method('Extent_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the view extents",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_EXTENT`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MVIEW_EXTENT_UNIT`"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="X minimum"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y minimum"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="X maximum"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Y maximum")
               ]),

        Method('GetMAP_MVIEW', module='geoengine.map', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`MAP` of the view.",
               return_type="MAP",
               return_doc="The :class:`MAP` of the View.",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View handle")
               ]),

        Method('GetREG_MVIEW', module='geoengine.map', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`REG` of the view.",
               return_type="REG",
               return_doc="The :class:`REG` of the View.",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View handle")
               ]),

        Method('IGetName_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the name of a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="view name returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VIEW',
                             doc="view name string size")
               ])
    ],
    'View Control': [

        Method('_PlotToView_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a plot coordinate in mm to a VIEW coordinate.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X in plot mm, returned in View coordinates"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y in plot mm, returned in View coordinates")
               ]),

        Method('_SetThinRes_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set polyline/polygon thinning resolution",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Thinning resolution in mm, -1.0 to turn off.")
               ]),

        Method('_ViewToPlot_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a VIEW coordinate to a plot coordinate in mm.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X in View, returned in mm from plot origin"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y in View, returned in mm from plot origin")
               ]),

        Method('BestFitWindow_MVIEW', module='geoengine.map', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="""
               Fit an area in ground coordinates centered to an area in mm on map or vise versa
               keeping X and Y scales the same.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X minimum (mm) of the area in map relative to map origin"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y minimum  .."),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="X maximum  .."),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y maximum  .."),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="min X in ground coordinate to fit to the area defined above"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="min Y in ground coordinate .."),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="max X in ground coordinate .."),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="max Y in ground coordinate .."),
                   Parameter('p10', type=Type.INT32_T,
                             doc=":def:`MVIEW_FIT`")
               ]),

        Method('FitMapWindow3D_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the 2D view window for a 3D view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View (3D)"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X minimum (mm) of the area in map relative to map origin"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y minimum  .."),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X maximum  .."),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y maximum  .."),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="min X in ground coordinate to fit to the area defined above"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="min Y in ground coordinate .."),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="max X in ground coordinate .."),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="max Y in ground coordinate ..")
               ]),

        Method('FitWindow_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Fit an area in ground coordinates to an area in mm on map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X minimum (mm) of the area in map relative to map origin"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y minimum  .."),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X maximum  .."),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y maximum  .."),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="min X in ground coordinate to fit to the area defined above"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="min Y in ground coordinate .."),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="max X in ground coordinate .."),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="max Y in ground coordinate ..")
               ]),

        Method('IGetClassName_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get a class name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="class"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="maximum name length")
               ]),

        Method('MapOrigin_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the map origin from a view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Returned map origin - X"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Returned map origin - Y")
               ]),

        Method('ReScale_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Change the scale of a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="scale factor (> 0.0)")
               ]),

        Method('rGetMapScale_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the current map scale of the view",
               return_type=Type.DOUBLE,
               return_doc="The current map scale to 6 significant digits",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` Handle")
               ]),

        Method('rScaleMM_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the horizontal scale in view X units/mm",
               return_type=Type.DOUBLE,
               return_doc="Returns horizontal scale in view X units/mm",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` Handle")
               ]),

        Method('rScalePjMM_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get horizontal scale in projected user units/mm",
               return_type=Type.DOUBLE,
               return_doc="Returns horizontal scale in projected user units/mm",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` Handle")
               ]),

        Method('rScaleYMM_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the vertical scale in Y units/mm",
               return_type=Type.DOUBLE,
               return_doc="Returns vertical scale in view Y units/mm",
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` Handle")
               ]),

        Method('ScaleAllGroup_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Scale all groups (except for GRID) in a view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X scale"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y scale")
               ]),

        Method('ScaleWindow_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Assign view coordinates to define a window.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X minimum in view coordinates"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y minimum"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X maximum"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y maximum"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="X minimum in plot coordinates"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Y minimum"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="horizontal scale (view unit/plot unit in mm)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="vertical scale")
               ]),

        Method('SetClassName_MVIEW', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set a class name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="class"),
                   Parameter('p3', type=Type.STRING,
                             doc="name")
               ]),

        Method('SetWindow_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the view window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X minimum"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y minimum"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X maximum"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y maximum"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`MVIEW_UNIT`")
               ]),

        Method('TranScale_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the view translation and scaling",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X origin (user X to be placed at map 0)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y origin (user Y to be placed at map 0)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X mm/user unit"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y mm/user unit")
               ]),

        Method('UserToView_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a USERplot in mm to a VIEW coordinate",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X in USER, returned in View coordinates"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y in USER, returned in View coordinates")
               ]),

        Method('ViewToUser_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert a VIEW coordinate to a USER coordinate.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X in View, returned in user coordinates"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y in View, returned in user coordinates")
               ])
    ],
    'Miscellaneous': [

    ],
    'Obsolete': [

        Method('Draw3D_MVIEW', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Draw a 3D object built from triangles",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type="VV",
                             doc="Verticies X"),
                   Parameter('p3', type="VV",
                             doc="Verticies Y"),
                   Parameter('p4', type="VV",
                             doc="Verticies Z"),
                   Parameter('p5', type="VV",
                             doc="Normals X"),
                   Parameter('p6', type="VV",
                             doc="Normals Y"),
                   Parameter('p7', type="VV",
                             doc="Normals Z"),
                   Parameter('p8', type="VV",
                             doc="Colors :class:`VV` or COL_ANY (can be NULL)"),
                   Parameter('p9', type="VV",
                             doc="long :class:`VV` of triangle indexes,3 per triangle")
               ]),

        Method('GetPlaneIPJ_MVIEW', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Get the Plane Projection",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('p3', type="IPJ",
                             doc="Projection object returning Plane Projection")
               ]),

        Method('GetStatusXYZ_MVIEW', module='geoengine.map', version='5.1.5',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Get current XYZ status display parameters.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="enable XYZ in for status bar display"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Z value in viewed section coordinates (dummy if not defined).")
               ]),

        Method('PolyAggregate_MVIEW', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Add a PolyAggregate to a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="PAGG",
                             doc="PolyAggregate"),
                   Parameter('p3', type=Type.STRING,
                             doc="PolyAggregate name (Maximum length is :def_val:`MVIEW_NAME_LENGTH`)")
               ]),

        Method('SetPlaneIPJ_MVIEW', module='geoengine.map', version='5.1.4',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Set the Plane Projection",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Plane index"),
                   Parameter('p3', type="IPJ",
                             doc="Projection")
               ]),

        Method('SetStatusXYZ_MVIEW', module='geoengine.map', version='5.1.5',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Set parameters to enable XYZ status display.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc=":class:`MVIEW` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="enable XYZ in for status bar display"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Z value in viewed section coordinates")
               ]),

        Method('Surface_MVIEW', module='geoengine.map', version='5.0.5',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Add an 3d Surface to a view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="SUR",
                             doc="Surface"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min X of locatin on map"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Min Y of locatin on map"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Max X of locatin on map"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Max Y of locatin on map"),
                   Parameter('p7', type=Type.STRING,
                             doc="Surface name (Maximum length is :def_val:`MVIEW_NAME_LENGTH`)")
               ]),

        Method('DrawSurface3D_MVIEW', module='geoengine.map', version='7.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Draw a 3D object built from triangles",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW"),
                   Parameter('p2', type=Type.STRING,
                             doc="Group name"),
                   Parameter('p3', type="VV",
                             doc="Vertices X (:def_val:`GS_REAL`)"),
                   Parameter('p4', type="VV",
                             doc="Vertices Y (:def_val:`GS_REAL`)"),
                   Parameter('p5', type="VV",
                             doc="Vertices Z (:def_val:`GS_REAL`)"),
                   Parameter('p6', type="VV",
                             doc="Normals X (:def_val:`GS_REAL`)"),
                   Parameter('p7', type="VV",
                             doc="Normals Y (:def_val:`GS_REAL`)"),
                   Parameter('p8', type="VV",
                             doc="Normals Z (:def_val:`GS_REAL`)"),
                   Parameter('p9', type="VV",
                             doc="Colors :class:`VV` (:def_val:`GS_INT`) [can be NULL]"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Color used if above :class:`VV` is NULL [0 for :class:`MVIEW`'s fillcolor]"),
                   Parameter('p11', type="VV",
                             doc="Triangles Point 1 (:def_val:`GS_INT`)"),
                   Parameter('p12', type="VV",
                             doc="Triangles Point 2 (:def_val:`GS_INT`)"),
                   Parameter('p13', type="VV",
                             doc="Triangles Point 3 (:def_val:`GS_INT`)")
               ])
    ]
}

