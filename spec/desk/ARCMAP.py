from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('ARCMAP',
                 doc="""
                 This library is not a class. It contains various utilities
                 used in maps and layers by the Geosoft extensions for ArcGIS.
                 """)


gx_defines = [
    Define('ARCMAP_LOAD_FLAGS',
           doc="Flags that can be combined and passed to iLoadMap_ARCMAP",
           constants=[
               Constant('ARCMAP_LOAD_DELFRAME', value='1', type=Type.INT32_T,
                        doc="If an exisiting frame is found delete it")                        ,
               Constant('ARCMAP_LOAD_DELLAYER', value='2', type=Type.INT32_T,
                        doc="If an exisiting layer is found delete it")                        ,
               Constant('ARCMAP_LOAD_EXISTFRAME', value='4', type=Type.INT32_T,
                        doc="If an exisiting frame is found add new layers to it")                        ,
               Constant('ARCMAP_LOAD_COPYLAYER', value='8', type=Type.INT32_T,
                        doc="If an exisiting layer is found make a copy")                        ,
               Constant('ARCMAP_LOAD_HIDESIBLINGS', value='16', type=Type.INT32_T,
                        doc="Hide all other existing layers in frame")                        ,
               Constant('ARCMAP_LOAD_PREFIXMAPFRAME', value='32', type=Type.INT32_T,
                        doc="Prefix the map filename part as part of the frame name")                        ,
               Constant('ARCMAP_LOAD_PREFIXMAPLAYER', value='64', type=Type.INT32_T,
                        doc="Prefix the map filename part as part of the layer name")                        ,
               Constant('ARCMAP_LOAD_MERGETOSINGLEVIEW', value='128', type=Type.INT32_T,
                        doc="Will render all views in single layer with the data view defining the coordinate system")                        ,
               Constant('ARCMAP_LOAD_INTOCURRENTFRAME', value='256', type=Type.INT32_T,
                        doc="Load everything into the current data frame")                        ,
               Constant('ARCMAP_LOAD_NOMAPLAYERS', value='512', type=Type.INT32_T,
                        doc="Use the map only for sizing data frames in layout, only load extra datasets.")                        ,
               Constant('ARCMAP_LOAD_ACTIVATE', value='1024', type=Type.INT32_T,
                        doc="Activates the main quickmap layer when done (e.g. 3D Viewer)")                        ,
               Constant('ARCMAP_LOAD_NEW', value='2048', type=Type.INT32_T,
                        doc="New method for loading maps introduced in 7.1. Will mimic what happens in montaj (i.e. base groups and 3D become graphics and views gets split into separate LYRs).")                        ,
               Constant('ARCMAP_LOAD_NAMETAGISPREFIX', value='4096', type=Type.INT32_T,
                        doc="Use a provided name tag as prefix when naming a newly created map layer.")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('ChangeSize_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Changes the custom page size of the ArcGIS Map document.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="X Size (mm)"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y Size (mm)")
               ]),

        Method('DisplayIn3DView_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Display a file in 3D view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('ExportFeatureLayerByNameTo3DFile_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Exports the shapes from a feature layer of the ArcMap document to a 3D File.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`MXD` filename"),
                   Parameter('p2', type=Type.STRING,
                             doc="Dataframe name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Layer name"),
                   Parameter('p4', type=Type.STRING,
                             doc="output file name")
               ]),

        Method('ExportSelectedFeatureLayerTo3DFile_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Exports the shapes from the currently selected feature layer (if any) in ArcMap to a 3D file (only on oriented frames i.e. sections).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="output file name")
               ]),

        Method('GetCurrentDocumentInfo_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Get some info on the current :class:`MXD` in ArcMap and selected layer (if any)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc=":class:`MXD` filename"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Selected Layer name (If a layer is selected)"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Dataframe name containing selected layer (If a layer is selected)"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of strings")
               ]),

        Method('GetSelectedLayerInfo_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the name info on the specified selected layer",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Selected layer number"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Selected Layer name"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Dataframe name containing selected layer"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of strings")
               ]),

        Method('iGetNumberOfSelectedLayers_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Get the number of selected layers in the TOC
               
               Returns									 The number of layers selected.
               """,
               return_type=Type.INT32_T),

        Method('iLoadMAP_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Loads a Geosoft map into the ArcMap document.",
               notes="""
               The extra datasets CSV should contain the the following fields:
               
                ID          -  Unique identifier
                DATASOURCE  -  Filename
                TYPE        -  RASTER and SHAPE supported
                MAPMATCH    -  Map to associate with (used for grouping logic)
                VIEWMATCH   -  View to match with in associated map (used for grouping logic)
                ZONEFILE    -  Used for type RASTER
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               -1 - Canceled
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Map File Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Optional Extra Datasets CSV Filename (Rasters and shape files to display with layers)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Optional frame/layer tag (suffix)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Combination of :def:`ARCMAP_LOAD_FLAGS`")
               ]),

        Method('iLoadMAPEx_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Loads a Geosoft map into the ArcMap document, specifying which View to use as Data view.",
               notes="""
               The extra datasets CSV should contain the the following fields:
               
                ID          -  Unique identifier
                DATASOURCE  -  Filename
                TYPE        -  RASTER and SHAPE supported
                MAPMATCH    -  Map to associate with (used for grouping logic)
                VIEWMATCH   -  View to match with in associated map (used for grouping logic)
                ZONEFILE    -  Used for type RASTER
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               -1 - Canceled
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Map File Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="View Name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Optional Extra Datasets CSV Filename (Rasters and shape files to display with layers)"),
                   Parameter('p4', type=Type.STRING,
                             doc="Optional frame/layer tag (suffix)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Combination of :def:`ARCMAP_LOAD_FLAGS`")
               ]),

        Method('iLoadShape_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Load a shape file into ArcMap.",
               return_type=Type.INT32_T,
               return_doc="0- OK, 1 - Error, -1 - Cancel",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="shape file to load"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="delete existing layers?")
               ]),

        Method('iLoadSPF_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Load all the shape files generated by importing a SPF into ArcMap.",
               return_type=Type.INT32_T,
               return_doc="0- OK, 1 - Error, -1 - Cancel",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="list of shape files to load"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="number of shape files")
               ]),

        Method('LoadLYR_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Load a LYR file to the current data frame",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('LoadMap_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Loads a Geosoft map into the current ArcMap document",
               notes="""
               The extra datasets CSV should contain the the following fields:
               
                   ID          -  Unique identifier
                   DATASOURCE  -  Filename
                   TYPE        -  RASTER and SHAPE supported
                   MAPMATCH    -  Map to associate with (used for grouping logic)
                   VIEWMATCH   -  View to match with in associated map (used for grouping logic)
                   ZONEFILE    -  Used for type RASTER
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Map File Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="View Name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Optional Extra Datasets CSV Filename (Rasters and shape files to display with layers)"),
                   Parameter('p4', type=Type.STRING,
                             doc="Optional frame/layer tag (suffix)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Fit to map size; one of :def:`GEO_BOOL`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Activate view (3D); one of :def:`GEO_BOOL`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Layer name tag is prefix; one of :def:`GEO_BOOL`")
               ]),

        Method('LoadMapView_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Load a Geosoft Map as a layer into the current data frame",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Map File Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="View Name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Layer Name"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Pass TRUE to also render other views in map (Use second parameter view for location)")
               ]),

        Method('LoadRaster_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Load a raster file to the current data frame",
               notes="""
               Loads any file type recognized as "raster" formats by ARC :class:`GIS`.
               This includes geosoft GRD files.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('LoadShape_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Load a :class:`SHP` file to the current data frame",
               notes="""
               The input layer name is created using the (optional) prefix and suffix as follows:
               
               Prefix_NAME_Suffix
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Layer Name Prefix: An underscore is added automatically"),
                   Parameter('p3', type=Type.STRING,
                             doc="Layer Name Suffix  An underscore is added automatically")
               ]),

        Method('MapViewToShape_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Create :class:`SHP` file(s) from a Geosoft Map view.",
               notes="""
               The output :class:`SHP` file name(s) are made up as follows
               (where NAME is the input :class:`SHP` file name):
               
                     NAME_pt.shp    (point objects)
                     NAME_ln.shp    (line or arc objects)
                     NAME_pg.shp    (polygon objects)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Map File Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="View Name"),
                   Parameter('p3', type=Type.STRING,
                             doc=":class:`SHP` File Name"),
                   Parameter('p4', type="LST",
                             doc="List to fill with shape files created")
               ]),

        Method('QuerySize_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Querie the page size in mm of the entire map page.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE, is_ref=True,
                             doc="X Size (mm)"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Y Size (mm)")
               ]),

        Method('ShowLayerByNameIn3D_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Shows a layer in ArcMap in a 3D view in an :class:`MXD`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`MXD` filename"),
                   Parameter('p2', type=Type.STRING,
                             doc="Dataframe name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Layer name")
               ]),

        Method('ShowSelectedLayersIn3D_ARCMAP', module='geoarcgis', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Shows the selected layers in ArcMap in a 3D view",
               return_type=Type.VOID),

        Method('GetIPJForPredefinedEsriGCS_ARCMAP', module='geoarcgis', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="Fills an :class:`IPJ` with a predefined ESRI GCS",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` to fill"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Predefined ESRI GCS Code")
               ]),

        Method('GetIPJForPredefinedEsriPCS_ARCMAP', module='geoarcgis', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="Fills an :class:`IPJ` with a predefined ESRI PCS",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` to fill"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Predefined ESRI PCS Code")
               ])
    ]
}

