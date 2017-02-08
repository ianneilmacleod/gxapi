from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('IPJ',
                 doc="""
The :class:`IPJ` class describes a single spatial reference in the world,
defined under a coordinate system, an orientation,
and a warp (which can be used to distort the projected object
to a particular shape or boundary).
""",
                 notes="""
:class:`IPJ` objects may be attached to channels or views. Two IPJs taken
together are used to create a :class:`PJ` object, which allows for the
conversion of positions from one projection to the other.
See also the :class:`LL2` class, which creates Datum correction lookups.

See also          :class:`PJ`    Converts coordinates between projections
:class:`LL2`   Creates Datum correction lookups.
""")


gx_defines = [
    Define('IPJ_3D_FLAG',
           doc="3D Flags",
           constants=[
               Constant('IPJ_3D_FLAG_NONE', value='0', type=Type.INT32_T,
                        doc="Standard")                        ,
               Constant('IPJ_3D_FLAG_INVERTANGLES', value='1', type=Type.INT32_T,
                        doc="Invert angle rotation during matrix creation")                        ,
               Constant('IPJ_3D_FLAG_INVERTZ', value='2', type=Type.INT32_T,
                        doc="Invert the Z plane to make up down.")                        ,
               Constant('IPJ_3D_FLAG_ORDER_ROTATION', value='4', type=Type.INT32_T,
                        doc="Apply rotations in a specific order, determined by pdParm[7]")                        
           ]),

    Define('IPJ_3D_ROTATE',
           doc="3D Rotation Mode",
           constants=[
               Constant('IPJ_3D_ROTATE_DEFAULT', value='0', type=Type.INT32_T)                        ,
               Constant('IPJ_3D_ROTATE_XYZ', value='1', type=Type.INT32_T)                        ,
               Constant('IPJ_3D_ROTATE_XZY', value='2', type=Type.INT32_T)                        ,
               Constant('IPJ_3D_ROTATE_YXZ', value='3', type=Type.INT32_T)                        ,
               Constant('IPJ_3D_ROTATE_YZX', value='4', type=Type.INT32_T)                        ,
               Constant('IPJ_3D_ROTATE_ZXY', value='5', type=Type.INT32_T)                        ,
               Constant('IPJ_3D_ROTATE_ZYX', value='6', type=Type.INT32_T)                        
           ]),

    Define('IPJ_CSP',
           doc="Projection Setting",
           constants=[
               Constant('IPJ_CSP_SCALE', value='0', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_FALSEEAST', value='1', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_FALSENORTH', value='2', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_LATORIGIN', value='3', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_LONORIGIN', value='4', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_PARALLEL_1', value='5', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_PARALLEL_2', value='6', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_AZIMUTH', value='7', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_ANGLE', value='8', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_POINTLAT_1', value='9', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_POINTLON_1', value='10', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_POINTLAT_2', value='11', type=Type.INT32_T)                        ,
               Constant('IPJ_CSP_POINTLON_2', value='12', type=Type.INT32_T)                        
           ]),

    Define('IPJ_NAME',
           doc="Project Name",
           constants=[
               Constant('IPJ_NAME_PCS', value='0', type=Type.INT32_T,
                        doc="projected coordinate system name")                        ,
               Constant('IPJ_NAME_PROJECTION', value='1', type=Type.INT32_T,
                        doc="projection name")                        ,
               Constant('IPJ_NAME_METHOD', value='2', type=Type.INT32_T,
                        doc="projection method name")                        ,
               Constant('IPJ_NAME_DATUM', value='3', type=Type.INT32_T,
                        doc="datum name")                        ,
               Constant('IPJ_NAME_ELLIPSOID', value='4', type=Type.INT32_T,
                        doc="ellipsoid name")                        ,
               Constant('IPJ_NAME_LDATUM', value='5', type=Type.INT32_T,
                        doc="local datum name")                        ,
               Constant('IPJ_NAME_UNIT_ABBR', value='6', type=Type.INT32_T,
                        doc="unit abbreviation")                        ,
               Constant('IPJ_NAME_UNIT_FULL', value='7', type=Type.INT32_T,
                        doc="full unit name")                        ,
               Constant('IPJ_NAME_TYPE', value='8', type=Type.INT32_T,
                        doc="projection type description")                        ,
               Constant('IPJ_NAME_LLDATUM', value='9', type=Type.INT32_T,
                        doc="datum transform table name")                        ,
               Constant('IPJ_NAME_METHOD_PARMS', value='10', type=Type.INT32_T,
                        doc="projection method parameters in GXF order")                        ,
               Constant('IPJ_NAME_METHOD_LABEL', value='11', type=Type.INT32_T,
                        doc="projection method parameters labels")                        ,
               Constant('IPJ_NAME_DATUM_PARMS', value='12', type=Type.INT32_T,
                        doc="datum parameters (major axis, flattening, prime meridian)")                        ,
               Constant('IPJ_NAME_LDATUM_PARMS', value='13', type=Type.INT32_T,
                        doc="""
                        local datum parameters (dX,dY,dZ,rX,rY,rZ,scale)
                        See GXF revision 3 for parameter list order and
                        specifications.
                        """)                        ,
               Constant('IPJ_NAME_GEOID', value='14', type=Type.INT32_T,
                        doc="geoid name if known")                        ,
               Constant('IPJ_NAME_LDATUMDESCRIPTION', value='15', type=Type.INT32_T,
                        doc="local datum description")                        ,
               Constant('IPJ_NAME_METHOD_PARMS_NATIVE', value='16', type=Type.INT32_T,
                        doc="projection method parameters in GXF order (Native units for eastings/northings)")                        ,
               Constant('IPJ_NAME_ORIENTATION_PARMS', value='17', type=Type.INT32_T,
                        doc="orientation parameters")                        
           ]),

    Define('IPJ_ORIENT',
           doc="Projection Orientation",
           constants=[
               Constant('IPJ_ORIENT_DEFAULT', value='0', type=Type.INT32_T,
                        doc="""
                        no special orientation - plan view. All views in maps
                        created before v5.1.3 will return this value.
                        """)                        ,
               Constant('IPJ_ORIENT_PLAN', value='1', type=Type.INT32_T,
                        doc="""
                        A plan view with a reference elevation and
                        optional rotation.
                        """)                        ,
               Constant('IPJ_ORIENT_SECTION', value='2', type=Type.INT32_T,
                        doc="""
                        Has an azimuth and swing.
                        The section view projects all plotted objects
                        HORIZONTALLY onto the viewing plan in order to
                        preserve elevations, even if the section has a swing.
                        """)                        ,
               Constant('IPJ_ORIENT_SECTION_NORMAL', value='5', type=Type.INT32_T,
                        doc="""
                        Same as :def_val:`IPJ_ORIENT_SECTION`, but the projection is perpendicular
                        to the section, not horizonatl, so elevatins are not preserved
                        on swung sections.
                        """)                        ,
               Constant('IPJ_ORIENT_DEPTH_SECTION', value='3', type=Type.INT32_T,
                        doc="""
                        This simple section has no azimuth or swing defined;
                        only the depth is of importance, and it is output as
                        the Y parameter, increasing downward. Used (for instance)
                        for strip logs in Wholeplot.
                        """)                        ,
               Constant('IPJ_ORIENT_3D', value='4', type=Type.INT32_T,
                        doc="A 3D rotation/scaling/translation orientation")                        ,
               Constant('IPJ_ORIENT_3D_MATRIX', value='7', type=Type.INT32_T,
                        doc="A 3D matrix orientation")                        ,
               Constant('IPJ_ORIENT_SECTION_CROOKED', value='6', type=Type.INT32_T,
                        doc="""
                        This is a vertical section that follows a
                        curving path, like a river or survey traverse.
                        The horizontal section location is the distance along
                        the path, while the vertical axis gives the elevation.
                        """)                        
           ]),

    Define('IPJ_PARM_LST',
           doc="Projection List",
           constants=[
               Constant('IPJ_PARM_LST_COORDINATESYSTEM', value='0', type=Type.INT32_T)                        ,
               Constant('IPJ_PARM_LST_DATUM', value='1', type=Type.INT32_T)                        ,
               Constant('IPJ_PARM_LST_PROJECTION', value='2', type=Type.INT32_T)                        ,
               Constant('IPJ_PARM_LST_UNITS', value='3', type=Type.INT32_T)                        ,
               Constant('IPJ_PARM_LST_LOCALDATUMDESCRIPTION', value='4', type=Type.INT32_T)                        ,
               Constant('IPJ_PARM_LST_LOCALDATUMNAME', value='5', type=Type.INT32_T)                        ,
               Constant('IPJ_PARM_LST_UNITSDESCRIPTION', value='6', type=Type.INT32_T)                        
           ]),

    Define('IPJ_TYPE',
           doc=":class:`IPJ` Types",
           constants=[
               Constant('IPJ_TYPE_PRJ', value='0', type=Type.INT32_T,
                        doc="""
                        Read from a PRJ file:
                        string 1 - Source file name
                        string 2 and 3 are not used.
                        """)                        ,
               Constant('IPJ_TYPE_PCS', value='1', type=Type.INT32_T,
                        doc="""
                        Projected coordinate system:
                        string 1 - POSC PCS name
                        string 2 - POSC Datum transform name
                        string 3 - not used.
                        """)                        ,
               Constant('IPJ_TYPE_GCS', value='2', type=Type.INT32_T,
                        doc="""
                        Geographic coordinate system:
                        string 1 - POSC Datum name
                        string 2 - POSC Datum transform name
                        string 3 - not used.
                        """)                        ,
               Constant('IPJ_TYPE_ANY', value='3', type=Type.INT32_T,
                        doc="""
                        Custom projection
                        string 1 - POSC Datum name
                        string 2 - POSC Datum transform name
                        string 3 - POSC Transform, "" if geographic
                        """)                        ,
               Constant('IPJ_TYPE_NONE', value='4', type=Type.INT32_T,
                        doc="""
                        Not used for :func:`Read_IPJ`.  This is used for
                        :func:`iSourceType_IPJ` to indicate no projection.
                        """)                        ,
               Constant('IPJ_TYPE_WRP', value='5', type=Type.INT32_T)                        ,
               Constant('IPJ_TYPE_TEST', value='6', type=Type.INT32_T,
                        doc="""
                        tests the projection tables for internal consistency
                        and creates report files in the project directory.
                        string 1 - outout report file name
                        string 2 - ESRI coordinate strings file.  This contains one
                        ESRI coordinate string per line.  Lines that
                        start with '#' are skipped.
                        string 3 - not currently used
                        """)                        
           ]),

    Define('IPJ_UNIT',
           doc="Projection Unit Type",
           constants=[
               Constant('IPJ_UNIT_ABBREVIATION', value='0', type=Type.INT32_T)                        ,
               Constant('IPJ_UNIT_FULLNAME', value='1', type=Type.INT32_T)                        
           ]),

    Define('IPJ_WARP',
           doc="Warp (Transformation) type",
           constants=[
               Constant('IPJ_WARP_MATRIX', value='-1', type=Type.INT32_T,
                        doc="Matrix Warp")                        ,
               Constant('IPJ_WARP_NONE', value='0', type=Type.INT32_T,
                        doc="no warp")                        ,
               Constant('IPJ_WARP_TRANS1', value='1', type=Type.INT32_T,
                        doc="translate only (needs 1 point)")                        ,
               Constant('IPJ_WARP_TRANS2', value='2', type=Type.INT32_T,
                        doc="translate, rotate, normal scale (needs 2 pts)")                        ,
               Constant('IPJ_WARP_TRANS3', value='3', type=Type.INT32_T,
                        doc="translate, rotate, scale X and Y (needs 3 pts or more, least-square fit)")                        ,
               Constant('IPJ_WARP_QUAD', value='4', type=Type.INT32_T,
                        doc="quadrilateral warp (needs 4 points)")                        ,
               Constant('IPJ_WARP_MULTIPOINT', value='5', type=Type.INT32_T,
                        doc="multipoint warp (needs at least 3 points)")                        ,
               Constant('IPJ_WARP_LOG', value='6', type=Type.INT32_T,
                        doc="convert from linear to log coords in X and/or Y")                        ,
               Constant('IPJ_WARP_MULTIPOINT_Y', value='7', type=Type.INT32_T,
                        doc="multipoint warp in Y only (needs at least 3 points)")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('_ClearWarp_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Clear warp parameters (if any) from an :class:`IPJ`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

        Method('_MakeGeographic_IPJ', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Remove a projected coordinate system from an :class:`IPJ`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` to modify")
               ]),

        Method('_MakeWGS84_IPJ', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Make a WGS 84 geographic projection",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

        Method('_SetUnits_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set unit parameters",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="factor to meters, must be >= 0.0"),
                   Parameter('p3', type=Type.STRING,
                             doc='abbreviation, can be ""')
               ]),

        Method('AddExaggWarp_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a warp to :class:`IPJ` to exaggerate X, Y and Z.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X exaggeration, must be > 0.0"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y exaggeration, must be > 0.0"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z exaggeration, must be > 0.0"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X reference origin"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Y reference origin"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Z reference origin")
               ]),

        Method('AddLogWarp_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a warp to :class:`IPJ` to log one or both coordinantes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Log in X?"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Log in Y?")
               ]),

        Method('AddMatrixWarp_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a warp to :class:`IPJ` using a matrix",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Row 0 Element 0"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Row 0 Element 1"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Row 0 Element 2"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Row 0 Element 3"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Row 1 Element 0"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Row 1 Element 1"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Row 1 Element 2"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Row 1 Element 3"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Row 2 Element 0"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Row 2 Element 1"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="Row 2 Element 2"),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Row 2 Element 3"),
                   Parameter('p14', type=Type.DOUBLE,
                             doc="Row 3 Element 0"),
                   Parameter('p15', type=Type.DOUBLE,
                             doc="Row 3 Element 1"),
                   Parameter('p16', type=Type.DOUBLE,
                             doc="Row 3 Element 2"),
                   Parameter('p17', type=Type.DOUBLE,
                             doc="Row 3 Element 3")
               ]),

        Method('AddWarp_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a warp to :class:`IPJ`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`IPJ_TYPE`"),
                   Parameter('p3', type="VV",
                             doc="Old X :class:`VV` (real)"),
                   Parameter('p4', type="VV",
                             doc="Old Y :class:`VV` (real)"),
                   Parameter('p5', type="VV",
                             doc="New X :class:`VV` (real)"),
                   Parameter('p6', type="VV",
                             doc="New Y :class:`VV` (real)")
               ]),

        Method('ClearCoordinateSystem_IPJ', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Clear coordinate sytsem, except for units",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ")
               ]),

        Method('ClearOrientation_IPJ', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Clear an orientation warp from an :class:`IPJ`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

        Method('ConvertOrientationWarpVV_IPJ', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Convert X,Y and Z VVs using the orientation warp from an :class:`IPJ`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="Grid file name"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV` coordinates converted on output"),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV` coordinates converted on output"),
                   Parameter('p4', type="VV",
                             doc="Z :class:`VV` coordinates converted on output"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="1 -  Forward (raw -> coordinate) , 0 - (coordinate -> raw)")
               ]),

        Method('Copy_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy IPJs",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="source :class:`IPJ`"),
                   Parameter('p2', type="IPJ",
                             doc="destination :class:`IPJ`")
               ]),

        Method('CopyProjection_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy the projection from one :class:`IPJ` to another",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="destination"),
                   Parameter('p2', type="IPJ",
                             doc="source")
               ]),

        Method('Create_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method creates a projection object.",
               return_type="IPJ",
               return_doc=":class:`IPJ` Object"),

        Method('CreateS_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create :class:`IPJ` from serialized source.",
               return_type="IPJ",
               return_doc=":class:`IPJ` Object",
               parameters = [
                   Parameter('p1', type="BF")
               ]),

        Method('CreateXML_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`IPJ` from serialized Geosoft MetaData XML file",
               return_type="IPJ",
               return_doc=":class:`IPJ` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('Destroy_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a projection object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="Projection to Destroy")
               ]),

        Method('Get3DView_IPJ', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get 3D orientation parameters",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X location of view origin"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y location of view origin"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Z location of view origin"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation in X"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation in Y"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation in Z"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Scaling in X"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Scaling in Y"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Scaling in Z")
               ]),

        Method('Get3DViewEx_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get 3D orientation parameters with new flags",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X location of view origin"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y location of view origin"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Z location of view origin"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation in X"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation in Y"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Rotation in Z"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Scaling in X"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Scaling in Y"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Scaling in Z"),
                   Parameter('p11', type=Type.INT32_T, is_ref=True,
                             doc=":def:`IPJ_3D_ROTATE`"),
                   Parameter('p12', type=Type.INT32_T, is_ref=True,
                             doc=":def:`IPJ_3D_FLAG`")
               ]),

        Method('GetCrookedSectionViewVVs_IPJ', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the crooked section path.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type="VV",
                             doc="Section X locations (e.g. distance along the curve)"),
                   Parameter('p3', type="VV",
                             doc="True X"),
                   Parameter('p4', type="VV",
                             doc="True Y"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Use logarithmic Y-axis (usually for data profiles) 0:No, 1:Yes")
               ]),

        Method('GetList_IPJ', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a list of parameters.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`IPJ_PARM_LST`"),
                   Parameter('p2', type=Type.STRING,
                             doc='datum filter, "" for no filter'),
                   Parameter('p3', type="LST",
                             doc="list returned")
               ]),

        Method('GetOrientationInfo_IPJ', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Get :class:`IPJ` orientation parameters.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` handle"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Plane Origin X"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Plane Origin Y"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Plane Origin Z"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Plane Azimuth (section) or Rotation (plan)"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Plane Swing   (section)")
               ]),

        Method('GetPlaneEquation_IPJ', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Get the equation of a plane",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Min X of surface"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min Y of surface"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Max X of surface"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Max Y of surface"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Pitch angle (between -360 and 360)"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Yaw angle (between -360 and 360)"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Roll angles (between -360 and 360)"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="X offset of plane"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Y offset of plane"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="Z offset of plane"),
                   Parameter('p12', type=Type.DOUBLE, is_ref=True,
                             doc="X scale"),
                   Parameter('p13', type=Type.DOUBLE, is_ref=True,
                             doc="Y scale"),
                   Parameter('p14', type=Type.DOUBLE, is_ref=True,
                             doc="Z scale")
               ]),

        Method('GetPlaneEquation2_IPJ', module='geoengine.core', version='6.4.1',
               availability=Availability.PUBLIC, 
               doc="Get the equation of a plane with reprojection.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object of the input grid or view"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` object for the output values"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min X of surface (in grid coords)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Min Y of surface"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Max X of surface"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Max Y of surface"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Pitch angle (between -360 and 360) (in view coords)"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Yaw angle (between -360 and 360)"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Roll angles (between -360 and 360)"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="X offset of plane (in view coords)"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="Y offset of plane"),
                   Parameter('p12', type=Type.DOUBLE, is_ref=True,
                             doc="Z offset of plane"),
                   Parameter('p13', type=Type.DOUBLE, is_ref=True,
                             doc="X scale (in view coords)"),
                   Parameter('p14', type=Type.DOUBLE, is_ref=True,
                             doc="Y scale"),
                   Parameter('p15', type=Type.DOUBLE, is_ref=True,
                             doc="Z scale")
               ]),

        Method('iCompareDatums_IPJ', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Compare the datums of two coordinate systems?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Datums are different
               1 - Datums are the same, but different LDT
               2 - Datums and LTD are the same
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` 1"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` 2")
               ]),

        Method('iConvertWarp_IPJ', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Converts a point X, Y, Z to the new :class:`IPJ` plane.",
               return_type=Type.INT32_T,
               return_doc="0 if ok - 1 otherwise",
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="Grid file name"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinates converted on output"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y coordinates converted on output"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Z coordinates converted on output"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="1 -  Forward (raw -> coordinate) , 0 - (coordinate -> raw)")
               ]),

        Method('iConvertWarpVV_IPJ', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Converts a set of X & Y VVs to the new :class:`IPJ` plane. The Z is assumed to be 0",
               return_type=Type.INT32_T,
               return_doc="0 if ok - 1 otherwise",
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="Grid file name"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV` coordinates converted on output"),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV` coordinates converted on output"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="1 -  Forward (raw -> coordinate) , 0 - (coordinate -> raw)")
               ]),

        Method('iCoordinateSystemsAreTheSame_IPJ', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Are these two coordinate systems the same?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` 1"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` 2")
               ]),

        Method('iCoordinateSystemsAreTheSameWithinASmallTolerance_IPJ', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Same as :func:`iCoordinateSystemsAreTheSame_IPJ`, but allows for small numerical differences",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` 1"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` 2")
               ]),

        Method('IGetDisplayName_IPJ', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get a name for display purposes from :class:`IPJ`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="name returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="maximum name size")
               ]),

        Method('IGetESRI_IPJ', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Store coordinate system in an ESRI prj coordinate string",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="ESRI projection string returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="string length, should be at least 1024")
               ]),

        Method('IGetGXF_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Store coordinate system in GXF style strings.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='6',
                             doc="projection name"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='6',
                             doc="datum name, major axis, elipticity"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='6',
                             doc="method name, parameters"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='6',
                             doc="unit name, factor"),
                   Parameter('p6', type=Type.STRING, is_ref=True, size_of_param='6',
                             doc="local transform name,dX,dY,dZ,rX,rY,rZ,Scale"),
                   Parameter('p7', type=Type.INT32_T, default_length='STR_GXF',
                             doc="maximum length of all strings")
               ]),

        Method('IGetMICoordSys_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Store coordinate system in MapInfo coordsys pair",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="MapInfo coordsys string returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="coordsys string length"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="MapInfo unit string returned"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="unit string length")
               ]),

        Method('IGetName_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get an :class:`IPJ` name",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`IPJ_NAME`"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="name returned"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="maximum name size")
               ]),

        Method('iGetOrientation_IPJ', module='geoengine.core', version='5.1.4',
               availability=Availability.PUBLIC, 
               doc="Get :class:`IPJ` orientation in space.",
               return_type=Type.INT32_T,
               return_doc=":def:`IPJ_ORIENT`",
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

        Method('IGetOrientationName_IPJ', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get a name for display purposes from :class:`IPJ`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="name returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="maximum name size")
               ]),

        Method('IGetUnits_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get unit parameters",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="factor to meters"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="abbreviation"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="length of string")
               ]),

        Method('IGetXML_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get an Geosoft Metadata XML string from an :class:`IPJ`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="XML string returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="string length, should be at least 1024")
               ]),

        Method('iHasProjection_IPJ', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Does the :class:`IPJ` object contain a projection?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

        Method('iIs3DInverted_IPJ', module='geoengine.core', version='6.3.1',
               availability=Availability.PUBLIC, 
               doc="Is this 3D View inverted ?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes (inverted)
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` Object")
               ]),

        Method('iIs3DInvertedAngles_IPJ', module='geoengine.core', version='6.3.1',
               availability=Availability.PUBLIC, 
               doc="Are the angles in this 3D View inverted ?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes (inverted)
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` Object")
               ]),

        Method('iIsGeographic_IPJ', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="See if this projection is geographic",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

        Method('iOrientationsAreTheSame_IPJ', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Are these two orientations the same?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` 1"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` 2")
               ]),

        Method('iOrientationsAreTheSameWithinASmallTolerance_IPJ', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Same as :func:`iOrientationsAreTheSame_IPJ`, but allows for small numerical differences",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` 1"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` 2")
               ]),

        Method('iHasSectionOrientation_IPJ', module='geoengine.core', version='8.3.0',
               availability=Availability.PUBLIC, 
               doc="Does this projection contain an orientation used by section plots?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="IPJ")
               ]),

        Method('iProjectionTypeIsFullySupported_IPJ', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Is the projection type fully supported?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="IPJ")
               ]),

        Method('iSetGXF_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Same as :func:`SetGXF_IPJ`, but fails gracefully.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - error in setting :class:`IPJ`, input :class:`IPJ` unchanged.
               1 - success: :class:`IPJ` set using input values.
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING,
                             doc='"projection name" or PCS_NAME from ipj_pcs.csv (datum / projection) or EPSG coordinate system code number or "<file.prj>" projection file name or "<file.wrp>" warp file name'),
                   Parameter('p3', type=Type.STRING,
                             doc='"datum name"[, major axis, elipticity, prime meridian] or DATUM from datum.csv or EPSG datum code number'),
                   Parameter('p4', type=Type.STRING,
                             doc='"method name", parameters (P1 through P8) or "projection name"[,"method name","Units",P1,P2...] or TRANSFORM from transform.csv or EPSG transform method code number'),
                   Parameter('p5', type=Type.STRING,
                             doc='"unit name", convertion to metres or UNIT_LENGTH from units.csv'),
                   Parameter('p6', type=Type.STRING,
                             doc='"local transform name"[,dX,dY,dZ,rX,rY,rZ,Scale] or DATUM_TRF from datumtrf.csv or AREA_OF_USE from ldatum.csv or EPSG local datum transform code number')
               ]),

        Method('iSourceType_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get :class:`IPJ` source type",
               return_type=Type.INT32_T,
               return_doc=":def:`IPJ_TYPE`",
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

        Method('iSupportDatumTransform_IPJ', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Can we transform between these two datums?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes, either because both CS are on the same datum,
               or because a local datum transform is defined
               for each coordinate system.
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` 1"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` 2")
               ]),

        Method('IUnitName_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a unit name given a scale factor",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="factor to meters"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`IPJ_UNIT`"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc='name returned, "" if cannot find unit'),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="length of string")
               ]),

        Method('iWarped_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Does :class:`IPJ` contain a warp?",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

        Method('iWarpsAreTheSame_IPJ', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Are these two warps the same?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` 1"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` 2")
               ]),

        Method('iWarpsAreTheSameWithinASmallTolerance_IPJ', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Same as :func:`iWarpsAreTheSame_IPJ`, but allows for small numerical differences",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` 1"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` 2")
               ]),

        Method('iWarpType_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Obtain the warp type of an :class:`IPJ`.",
               return_type=Type.INT32_T,
               return_doc=":def:`IPJ_WARP`",
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

        Method('MakeProjected_IPJ', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Create a default projected coordinate system from lat-long ranges.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` to modify"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="minimum longitude"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="minimum latitude"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="maximum longitude"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="maximum latitude")
               ]),

        Method('NewBoxResolution_IPJ', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Determine a data resolution in a new coordinate system",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="original :class:`IPJ`"),
                   Parameter('p2', type="IPJ",
                             doc="new :class:`IPJ`"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="data resolution in original :class:`IPJ`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X minimum of bounding box in new :class:`IPJ`"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y minimum"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="X maximum"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Y maximum"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="minimum data resolution in new :class:`IPJ`,"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="maximum data resolution in new :class:`IPJ`"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="diagonal data resolution in new :class:`IPJ`")
               ]),

        Method('Read_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Read and define an :class:`IPJ` from a standard file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`IPJ_TYPE`"),
                   Parameter('p3', type=Type.STRING,
                             doc="string 1"),
                   Parameter('p4', type=Type.STRING,
                             doc="string 2"),
                   Parameter('p5', type=Type.STRING,
                             doc="string 3")
               ]),

        Method('rGetMethodParm_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get projection method parameter",
               return_type=Type.DOUBLE,
               return_doc="Parameter setting, :def_val:`rDUMMY` if dot used",
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`IPJ_CSP`")
               ]),

        Method('rGetNorthAzimuth_IPJ', module='geoengine.core', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="Return the azimuth of geographic North at a point.",
               return_type=Type.DOUBLE,
               return_doc="Azimuth (degrees CW) of geographic north from grid north at a location.",
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="input X location"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="input Y location")
               ]),

        Method('rUnitScale_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a unit scale (m/unit) given a name",
               return_type=Type.DOUBLE,
               return_doc="Scale factor m/unit",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="unit name, abbreviation or full name"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="default to return if name not found")
               ]),

        Method('Serial_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Serialize :class:`IPJ` to a :class:`BF`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ"),
                   Parameter('p2', type="BF")
               ]),

        Method('SerialFGDCXML_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Write the :class:`IPJ` as a FDGC MetaData XML object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of file to export to")
               ]),

        Method('SerialISOXML_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Write the :class:`IPJ` as a ISO MetaData XML object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of file to export to")
               ]),

        Method('SerialXML_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Write the :class:`IPJ` as a Geosoft MetaData XML object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of file to export to")
               ]),

        Method('Set3DInverted_IPJ', module='geoengine.core', version='6.3.1',
               availability=Availability.PUBLIC, 
               doc="Set whether a view is inverted (must be 3D already)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Inverted (0 or 1)")
               ]),

        Method('Set3DInvertedAngles_IPJ', module='geoengine.core', version='6.3.1',
               availability=Availability.PUBLIC, 
               doc="Set whether the angles in this view are inverted (must be 3D already)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Inverted (0 or 1)")
               ]),

        Method('Set3DView_IPJ', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set 3D orientation parameters",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location of view origin"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y location of view origin"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z location of view origin"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Rotation in X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Rotation in Y"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Rotation in Z"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Scaling in X"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Scaling in Y"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Scaling in Z")
               ]),

        Method('Set3DViewEx_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set 3D orientation parameters with new flags",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location of view origin"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y location of view origin"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z location of view origin"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Rotation in X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Rotation in Y"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Rotation in Z"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Scaling in X"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Scaling in Y"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Scaling in Z"),
                   Parameter('p11', type=Type.INT32_T,
                             doc=":def:`IPJ_3D_ROTATE`"),
                   Parameter('p12', type=Type.INT32_T,
                             doc=":def:`IPJ_3D_FLAG`")
               ]),

        Method('Set3DViewFromAxes_IPJ', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Set 3D orientation parameters",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location of view origin"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y location of view origin"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z location of view origin"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X axis X component"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="X axis Y component"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="X axis Z component"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Y axis X component"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Y axis Y component"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Y axis Z component"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Scaling in X"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="Scaling in Y"),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Scaling in Z")
               ]),

        Method('SetCrookedSectionView_IPJ', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Set up the crooked section view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type="VV",
                             doc="Section X locations (e.g. distance along the curve)"),
                   Parameter('p3', type="VV",
                             doc="True X"),
                   Parameter('p4', type="VV",
                             doc="True Y"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Use logarithmic Y-axis (usually for data profiles) 0:No, 1:Yes")
               ]),

        Method('SetDepthSectionView_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set depth section orientation parameters",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="View Y value for Depth = 0.0.")
               ]),

        Method('SetESRI_IPJ', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Set coordinate system from an ESRI prj coordinate string",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="ESRI prj format projection string")
               ]),

        Method('SetGXF_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set coordinate system from GXF style strings.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING,
                             doc='"projection name" or PCS_NAME from ipj_pcs.csv (datum / projection) or EPSG coordinate system code number or "<file.prj>" projection file name or "<file.wrp>" warp file name'),
                   Parameter('p3', type=Type.STRING,
                             doc='"datum name"[, major axis, elipticity, prime meridian] or DATUM from datum.csv or EPSG datum code number'),
                   Parameter('p4', type=Type.STRING,
                             doc='"method name", parameters (P1 through P8) or "projection name"[,"method name","Units",P1,P2...] or TRANSFORM from transform.csv or EPSG transform method code number'),
                   Parameter('p5', type=Type.STRING,
                             doc='"unit name", convertion to metres or UNIT_LENGTH from units.csv'),
                   Parameter('p6', type=Type.STRING,
                             doc='"local transform name"[,dX,dY,dZ,rX,rY,rZ,Scale] or DATUM_TRF from datumtrf.csv or AREA_OF_USE from ldatum.csv or EPSG local datum transform code number')
               ]),

        Method('SetMethodParm_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set projection method parameter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`IPJ_CSP`"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="parameter value")
               ]),

        Method('SetMICoordSys_IPJ', module='geoengine.core', version='5.1.4',
               availability=Availability.PUBLIC, 
               doc="Set coordinate system from a MapInfo coordsys command",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="MapInfo Coordinate System"),
                   Parameter('p3', type=Type.STRING,
                             doc="MapInfo Units")
               ]),

        Method('SetNormalSectionView_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set normal section orientation parameters",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location of view origin"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y location of view origin"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z location of view origin"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Section azimuth - degrees CCW from north"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Section swing -90 < swing < 90.")
               ]),

        Method('SetPlanView_IPJ', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Set plan orientation parameters.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location of view origin"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y location of view origin"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z location of view origin"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="rotation CCW from normal XY coords")
               ]),

        Method('SetSectionView_IPJ', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Set section orientation parameters",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location of view origin"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y location of view origin"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z location of view origin"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Section azimuth - degrees CCW from north"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Section swing -90 < swing < 90.")
               ]),

        Method('SetWMSCoordSys_IPJ', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Set coordinate system from a WMS coordsys string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="WMS style coordinate string"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="minimum X bounding box"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="minimum Y"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="maximum X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="maximum Y")
               ]),

        Method('SetXML_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set an :class:`IPJ` from a Geosoft Metadata XML string",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="XML string to set")
               ]),

        Method('Get3DMatrixOrientation_IPJ', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Gets the coefficients of a 3D matrix orientation.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Row 0 Element 0"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Row 0 Element 1"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Row 0 Element 2"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Row 0 Element 3"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Row 1 Element 0"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Row 1 Element 1"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Row 1 Element 2"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Row 1 Element 3"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Row 2 Element 0"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="Row 2 Element 1"),
                   Parameter('p12', type=Type.DOUBLE, is_ref=True,
                             doc="Row 2 Element 2"),
                   Parameter('p13', type=Type.DOUBLE, is_ref=True,
                             doc="Row 2 Element 3"),
                   Parameter('p14', type=Type.DOUBLE, is_ref=True,
                             doc="Row 3 Element 0"),
                   Parameter('p15', type=Type.DOUBLE, is_ref=True,
                             doc="Row 3 Element 1"),
                   Parameter('p16', type=Type.DOUBLE, is_ref=True,
                             doc="Row 3 Element 2"),
                   Parameter('p17', type=Type.DOUBLE, is_ref=True,
                             doc="Row 3 Element 3")
               ]),

        Method('Set3DMatrixOrientation_IPJ', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Apply a 3D orientation directly using matrix coefficients.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Row 0 Element 0"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Row 0 Element 1"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Row 0 Element 2"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Row 0 Element 3"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Row 1 Element 0"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Row 1 Element 1"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Row 1 Element 2"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Row 1 Element 3"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Row 2 Element 0"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Row 2 Element 1"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="Row 2 Element 2"),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Row 2 Element 3"),
                   Parameter('p14', type=Type.DOUBLE,
                             doc="Row 3 Element 0"),
                   Parameter('p15', type=Type.DOUBLE,
                             doc="Row 3 Element 1"),
                   Parameter('p16', type=Type.DOUBLE,
                             doc="Row 3 Element 2"),
                   Parameter('p17', type=Type.DOUBLE,
                             doc="Row 3 Element 3")
               ]),

        Method('ReprojectSectionGrid_IPJ', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Reproject a section grid",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="Initial projected :class:`IPJ`, optionally including an orientation"),
                   Parameter('p2', type="IPJ",
                             doc="""
                             Reprojected :class:`IPJ` on input (need not include an orientation). On output contains the same
                             						type of orientation as the initial :class:`IPJ`, adjusted to be in the same location.
                             """),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X origin of grid (input initial value, output new value)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y origin of grid (input initial value, output new value)"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="X cell size of grid (input initial value, output new value)"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Y cell size of grid (input initial value, output new value)"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Grid rotation (degrees CCW) (input initial value, output new value)")
               ])
    ],
    'Obsolete': [

        Method('ClearProjection_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Clear a projection except for units",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` to clear")
               ]),

        Method('iEquivalent_IPJ', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Compare if two IPJs the equivalent (allows for small numerical differences)",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               
               Notes			 This does not compare LDT information in the :class:`IPJ`, use :func:`iCompareDatums_IPJ` for a full comparison.
               This function does not act like :func:`iSame_IPJ` in that it will return 0 if the one :class:`IPJ` is IPJ_CS_UNKNOWN
               and not the other.
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` 1"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` 2")
               ]),

        Method('iSame_IPJ', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Compare if two IPJs are identical or if either is undefined",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - If the IPJs are the same, or if either :class:`IPJ` is IPJ_CS_UNKNOWN.
               
               Notes			 This does not compare LDT information in the :class:`IPJ`, use :func:`iCompareDatums_IPJ` for a full comparison.
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` 1"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` 2")
               ]),

        Method('iSupported_IPJ', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Is this coordinate system fully supported?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="IPJ")
               ])
    ]
}

