from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GEOSTRING',
                 doc="The :class:`GEOSTRING` class is used to read information stored in Geostring files (*.geosoft_string). Geosoft geostrings are 3D vector files that store digitized interpretations drawn on section maps. Both polygon and polyline features can be stored in the same file. This API currently only provides read access, but read/write support could be added in the future.")


gx_defines = [
    Define('GEOSTRING_OPEN',
           doc="Open Modes",
           constants=[
               Constant('GEOSTRING_OPEN_READ', value='0', type=Type.INT32_T)                        ,
               Constant('GEOSTRING_OPEN_READWRITE', value='1', type=Type.INT32_T)                        
           ]),

    Define('SECTION_ORIENTATION',
           doc="Section orientation types",
           constants=[
               Constant('SECTION_ORIENTATION_UNKNOWN', value='0', type=Type.INT32_T)                        ,
               Constant('SECTION_ORIENTATION_PLAN', value='1', type=Type.INT32_T)                        ,
               Constant('SECTION_ORIENTATION_SECTION', value='2', type=Type.INT32_T)                        ,
               Constant('SECTION_ORIENTATION_CROOKED', value='2', type=Type.INT32_T)                        ,
               Constant('SECTION_ORIENTATION_GMSYS', value='2', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Open_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Open a Geostring file",
               return_type="GEOSTRING",
               return_doc=":class:`GEOSTRING` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Geostring file name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GEOSTRING_OPEN`")
               ]),

        Method('Destroy_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`GEOSTRING` Object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object")
               ]),

        Method('GetIPJ_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the coordinate system of the Geostring.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` in which to place the Geostring coordinate system")
               ]),

        Method('GetFeatures_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the features",
               notes="List items are returned with feature GUID in name and feature name in value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetSections_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the sections",
               notes="List items are returned with section GUID in name and section name in value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetAllShapes_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the all shapes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetShapesForFeature_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get all shapes linked to a specific feature",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Feature GUID"),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetShapesForSection_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get all shapes linked to a specific section",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Section GUID"),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetShapesForFeatureAndSection_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get all shapes linked to a specific feature and section",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Feature GUID"),
                   Parameter('p3', type=Type.STRING,
                             doc="Section GUID"),
                   Parameter('p4', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetFeatureProperties_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get a feature's properties",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Feature GUID"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of Name buffer."),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='p6',
                             doc="Description"),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of Description buffer."),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc=":def:`GEO_BOOL` indicating if feature is decribed by polygons (shapes are polylines if not set)"),
                   Parameter('p8', type=Type.INT32_T, is_ref=True,
                             doc="The fill pattern number (see :func:`PatNumber_MVIEW`)"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="The fill pattern size (see :func:`PatSize_MVIEW`)"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="The fill pattern thickness (see :func:`PatThick_MVIEW`)"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="The fill pattern density (see :func:`PatDensity_MVIEW`)"),
                   Parameter('p12', type=Type.INT32_T, is_ref=True,
                             doc="The fill color (an :class:`MVIEW` color)"),
                   Parameter('p13', type=Type.INT32_T, is_ref=True,
                             doc="The fill background color (an :class:`MVIEW` color)"),
                   Parameter('p14', type=Type.INT32_T, is_ref=True,
                             doc="The line style (see :func:`LineStyle_MVIEW`)"),
                   Parameter('p15', type=Type.DOUBLE, is_ref=True,
                             doc="The line thickness (see :func:`LineThick_MVIEW`)"),
                   Parameter('p16', type=Type.DOUBLE, is_ref=True,
                             doc="The dash pattern pitch (see :func:`LineStyle_MVIEW`)"),
                   Parameter('p17', type=Type.INT32_T, is_ref=True,
                             doc="The line color (an :class:`MVIEW` color)")
               ]),

        Method('GetSectionProperties_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get a section's properties",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Section GUID"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of Name buffer."),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='p6',
                             doc="ContainerName"),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of ContainerName buffer."),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc=":def:`SECTION_ORIENTATION`"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Easting"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Northing"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Elevation"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="Azimuth"),
                   Parameter('p12', type=Type.DOUBLE, is_ref=True,
                             doc="Swing"),
                   Parameter('p13', type=Type.DOUBLE, is_ref=True,
                             doc="A in the scalar equation of best-fit plane describing the section"),
                   Parameter('p14', type=Type.DOUBLE, is_ref=True,
                             doc="B in the scalar equation of best-fit plane describing the section"),
                   Parameter('p15', type=Type.DOUBLE, is_ref=True,
                             doc="C in the scalar equation of best-fit plane describing the section"),
                   Parameter('p16', type=Type.DOUBLE, is_ref=True,
                             doc="D in the scalar equation of best-fit plane describing the section")
               ]),

        Method('GetShapeProperties_GEOSTRING', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get a shape's properties",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GEOSTRING",
                             doc=":class:`GEOSTRING` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Shape GUID"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Feature GUID"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of Feature GUID buffer."),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='p6',
                             doc="Section GUID"),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of Section GUID buffer."),
                   Parameter('p7', type="VV",
                             doc="Vertices X location"),
                   Parameter('p8', type="VV",
                             doc="Vertices Y location"),
                   Parameter('p9', type="VV",
                             doc="Vertices Z location")
               ])
    ]
}

