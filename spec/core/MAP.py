from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MAP',
                 doc="""
                 MAPs are containers for :class:`MVIEW` objects. A view is a 3-D translation
                 and a clip window on a map. Graphic entities can be drawn in an :class:`MVIEW`.
                 It is recommended that the :class:`MAP` class be instantiated by first creating
                 an :class:`EMAP` object and calling the :func:`Lock_EMAP`() function.
                 (See the explanation on the distinction between the :class:`MAP` and :class:`EMAP` classes).
                 """)


gx_defines = [
    Define('DUPMAP',
           doc="Duplicate Modes",
           constants=[
               Constant('DUPMAP_BLANK', value='0', type=Type.INT32_T,
                        doc="Blank")                        ,
               Constant('DUPMAP_COPY', value='1', type=Type.INT32_T,
                        doc="Copy all current contents")                        ,
               Constant('DUPMAP_COPY_PRE62', value='2', type=Type.INT32_T,
                        doc="Copy all current contents and save text for pre-6.2 versions.")                        
           ]),

    Define('MAP_EXPORT_BITS',
           doc="Color Types",
           constants=[
               Constant('MAP_EXPORT_BITS_24', value='24', type=Type.INT32_T,
                        doc="24 Bit Color")                        ,
               Constant('MAP_EXPORT_BITS_GREY8', value='9', type=Type.INT32_T,
                        doc="8 Bit Gray Scale")                        ,
               Constant('MAP_EXPORT_BITS_8', value='8', type=Type.INT32_T,
                        doc="8 Bit Color")                        ,
               Constant('MAP_EXPORT_BITS_GREY4', value='5', type=Type.INT32_T,
                        doc="4 Bit Gray Scale")                        ,
               Constant('MAP_EXPORT_BITS_4', value='4', type=Type.INT32_T,
                        doc="4 Bit Color")                        ,
               Constant('MAP_EXPORT_BITS_GREY1', value='1', type=Type.INT32_T,
                        doc="1 Bit Gray Scale")                        ,
               Constant('MAP_EXPORT_BITS_DEFAULT', value='0', type=Type.INT32_T,
                        doc="Default Resolution")                        
           ]),

    Define('MAP_EXPORT_FORMAT',
           is_constant=True,
           doc="""
           Export Formats
           Format   Description                  Type
           =======  ==========================   ====
           """,
           constants=[
               Constant('MAP_EXPORT_FORMAT_PLT', value='PLT', type=Type.STRING,
                        doc='"PLT"    Geosoft Plot (*.plt)         Plot')                        ,
               Constant('MAP_EXPORT_FORMAT_SHP', value='SHP', type=Type.STRING,
                        doc='":class:`SHP`"    ArcView Shapfile (*.shp)     Plot')                        ,
               Constant('MAP_EXPORT_FORMAT_DXF12', value='DXF12', type=Type.STRING,
                        doc='"DXF12"  AutoCad12 (*.dxf)            Plot')                        ,
               Constant('MAP_EXPORT_FORMAT_DXF13', value='DXF13', type=Type.STRING,
                        doc='"DXF13"  AutoCad13 (*.dxf)            Plot')                        ,
               Constant('MAP_EXPORT_FORMAT_GTIFF', value='GTIFF', type=Type.STRING,
                        doc='"GTIFF"  GeoTIFF (*.tif),             Color Image')                        ,
               Constant('MAP_EXPORT_FORMAT_MTIFF', value='MTIFF', type=Type.STRING,
                        doc='"MTIFF"  MapInfo TIFF (*.tif)         Color Image')                        ,
               Constant('MAP_EXPORT_FORMAT_ATIFF', value='ATIFF', type=Type.STRING,
                        doc='"ATIFF"  ArcView TIFF (*.tif)         Color Image')                        ,
               Constant('MAP_EXPORT_FORMAT_GEO', value='GEO', type=Type.STRING,
                        doc='":class:`GEO`"    Geosoft COLOR grid (*.grd)   Color Image')                        ,
               Constant('MAP_EXPORT_FORMAT_ERM', value='ERM', type=Type.STRING,
                        doc='"ERM"    ER Mapper RGB (*.ers)        Color Image')                        ,
               Constant('MAP_EXPORT_FORMAT_KMZ', value='KMZ', type=Type.STRING,
                        doc='"KMZ"    Keyhole Markup (*.kmz)       Zipped XML/Image files')                        
           ]),

    Define('MAP_EXPORT_METHOD',
           doc="Dithering Methods",
           constants=[
               Constant('MAP_EXPORT_METHOD_STANDARD', value='0', type=Type.INT32_T,
                        doc="Standard Dither")                        ,
               Constant('MAP_EXPORT_METHOD_DIFFUSE', value='1', type=Type.INT32_T,
                        doc="Error Diffusion Dither")                        ,
               Constant('MAP_EXPORT_METHOD_NONE', value='2', type=Type.INT32_T,
                        doc="No Dither")                        
           ]),

    Define('MAP_EXPORT_RASTER_FORMAT',
           is_constant=True,
           doc="""
           Export Raster Formats
           .
           Format  Description                      Type           B/W  B/W  COL  B/W  COL  COL
           ======= ==========================       ===========    ===  ===  ===  ===  ===  ===
           """,
           constants=[
               Constant('MAP_EXPORT_RASTER_FORMAT_EMF', value='EMF', type=Type.STRING,
                        doc='"EMF"   Enhanced Metafile (*.emf)        Plot')                        ,
               Constant('MAP_EXPORT_RASTER_FORMAT_BMP', value='BMP', type=Type.STRING,
                        doc='"BMP"   Bitmap (*.bmp)                   Color Image     X    X    X    X    X    X')                        ,
               Constant('MAP_EXPORT_RASTER_FORMAT_JPEGL', value='JPEGL', type=Type.STRING,
                        doc='"JPEGL" JPEG Low Quality (*.jpg)         Color Image                              X')                        ,
               Constant('MAP_EXPORT_RASTER_FORMAT_JPEG', value='JPEG', type=Type.STRING,
                        doc='"JPEG" JPEG (*.jpg)                     Color Image                              X')                        ,
               Constant('MAP_EXPORT_RASTER_FORMAT_JPEGH', value='JPEGH', type=Type.STRING,
                        doc='"JPEGH" JPEG High Quality (*.jpg)        Color Image                              X')                        ,
               Constant('MAP_EXPORT_RASTER_FORMAT_GIF', value='GIF', type=Type.STRING,
                        doc='"GIF"   GIF (*.gif)                      Color Image     X    X    X    X    X')                        ,
               Constant('MAP_EXPORT_RASTER_FORMAT_PCX', value='PCX', type=Type.STRING,
                        doc='"PCX"   PCX (*.pcx)                      Color Image     X    X    X    X    X    X')                        ,
               Constant('MAP_EXPORT_RASTER_FORMAT_PNG', value='PNG', type=Type.STRING,
                        doc='"PNG"   PNG (*.png)                      Color Image     X    X    X    X    X    X')                        ,
               Constant('MAP_EXPORT_RASTER_FORMAT_EPS', value='EPS', type=Type.STRING,
                        doc='"EPS"   Encasulated PostScript (*.eps)   Color Image                    X')                        ,
               Constant('MAP_EXPORT_RASTER_FORMAT_TIFF', value='TIFF', type=Type.STRING,
                        doc='"TIFF"  TIFF (*.tif)                     Color Image     X    X    X    X    X    X')                        
           ]),

    Define('MAP_LIST_MODE',
           doc="Map List modes",
           constants=[
               Constant('MAP_LIST_MODE_ALL', value='0', type=Type.INT32_T)                        ,
               Constant('MAP_LIST_MODE_3D', value='1', type=Type.INT32_T)                        ,
               Constant('MAP_LIST_MODE_NOT3D', value='2', type=Type.INT32_T)                        
           ]),

    Define('MAP_OPEN',
           doc="Open Modes",
           constants=[
               Constant('MAP_WRITENEW', value='1', type=Type.INT32_T)                        ,
               Constant('MAP_WRITEOLD', value='2', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Export': [

        Method('ExportAllInView_MAP', module='geoengine.map', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Export the entire map in view units to an external format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name To Export"),
                   Parameter('p3', type=Type.STRING,
                             doc="View to export coordinates in"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Resolution in view units of one pixel (or dummy, will be used if DPI is dummy)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Resolution in DPI (will override view resolution if not dummy, map page size will be used to determine pixel size of output)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`MAP_EXPORT_BITS`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`MAP_EXPORT_METHOD`"),
                   Parameter('p8', type=Type.STRING,
                             doc=":def:`MAP_EXPORT_FORMAT`"),
                   Parameter('p9', type=Type.STRING,
                             doc="Extended Options String (format specific)")
               ]),

        Method('ExportAllRaster_MAP', module='geoengine.map', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Export the entire map to map to a non-geo raster format",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name To Export"),
                   Parameter('p3', type=Type.STRING,
                             doc="View to export coordinates in"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Number of Pixels in X (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Number of Pixels in Y (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Resolution in DPI (will override X and Y if not dummy, map page size will be used to determine pixel size of output)"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`MAP_EXPORT_BITS`"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`MAP_EXPORT_METHOD`"),
                   Parameter('p9', type=Type.STRING,
                             doc=":def:`MAP_EXPORT_RASTER_FORMAT`"),
                   Parameter('p10', type=Type.STRING,
                             doc="Extended Options String (format specific)")
               ]),

        Method('ExportAreaInView_MAP', module='geoengine.map', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Export an area of a map in view units to an external format",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name To Export"),
                   Parameter('p3', type=Type.STRING,
                             doc="View to export coordinates in"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Resolution in view units of one pixel (or dummy, will be used if DPI is dummy)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Resolution in DPI (will override view resolution if not dummy, map page size will be used to determine pixel size of output)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`MAP_EXPORT_BITS`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`MAP_EXPORT_METHOD`"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Area To Export Min X location in view units"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Area To Export Min Y location in view units"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Area To Export Max X location in view units"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Area To Export Max Y location in view units"),
                   Parameter('p12', type=Type.STRING,
                             doc=":def:`MAP_EXPORT_FORMAT`"),
                   Parameter('p13', type=Type.STRING,
                             doc="Extended Options String (format specific)")
               ]),

        Method('ExportAreaRaster_MAP', module='geoengine.map', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Export an area of a map to a non-geo raster format",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name To Export"),
                   Parameter('p3', type=Type.STRING,
                             doc="View to export coordinates in"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Area To Export Min X location in view units"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Area To Export Min Y location in view units"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Area To Export Max X location in view units"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Area To Export Max Y location in view units"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Number of Pixels in X (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Number of Pixels in Y (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Resolution in DPI (will override X and Y if not dummy, map page size will be used to determine pixel size of output)"),
                   Parameter('p11', type=Type.INT32_T,
                             doc=":def:`MAP_EXPORT_BITS`"),
                   Parameter('p12', type=Type.INT32_T,
                             doc=":def:`MAP_EXPORT_METHOD`"),
                   Parameter('p13', type=Type.STRING,
                             doc=":def:`MAP_EXPORT_RASTER_FORMAT`"),
                   Parameter('p14', type=Type.STRING,
                             doc="Extended Options String (format specific)")
               ]),

        Method('RenderBitmap_MAP', module='geoengine.map', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Render a map to a bitmap.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="View we exporting units in"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="MinX"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="MinY"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="MaxX"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="MaxY"),
                   Parameter('p7', type=Type.STRING,
                             doc="File to generate (ext forced to BMP)"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Maximum resolution in either direction, -1 for none (will change the pixel density of image if exceeded)")
               ])
    ],
    'Miscellaneous': [

        Method('AGGList_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a list of all aggregates in this map.",
               notes="""
               List items are returned as view/agg/layer.
               The layer name is optional
               """,
               see_also=":class:`LST` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type="LST",
                             doc="list to hold the views (allow up to 96 characters)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="0 - view/agg only 1 - view/agg/layer")
               ]),

        Method('AGGListEx_MAP', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get a list of aggregates in this map based on a mode",
               notes="""
               List items are returned as view/agg/layer.
               The layer name is optional
               """,
               see_also=":class:`LST` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type="LST",
                             doc="list to hold the views (allow up to 96 characters)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="0 - view/agg only 1 - view/agg/layer"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`MAP_LIST_MODE`")
               ]),

        Method('Clean_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Clean up empty groups in all views in map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle")
               ]),

        Method('Commit_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Commit any changes to a map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc="Map")
               ]),

        Method('CopyMapToView_MAP', module='geoengine.map', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Copy entire map into one view in output map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc="Source :class:`MAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Destination :class:`MAP` name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of View")
               ]),

        Method('CRCMap_MAP', module='geoengine.map', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Generate an XML CRC of a :class:`MAP`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="CRC returned"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of xml to generate (.zip added)")
               ]),

        Method('Create_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`MAP`.",
               return_type="MAP",
               return_doc=":class:`MAP` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`MAP` file name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MAP_OPEN`")
               ]),

        Method('Current_MAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current map opened.",
               notes="""
               If there is no current map, and running interactively,
               the user is prompted to open a map.
               """,
               return_type="MAP",
               return_doc=":class:`MAP` Object"),

        Method('DeleteView_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Deletes a view in this map.",
               notes="If the view does not exist, nothing happens.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="View Name to delete")
               ]),

        Method('Destroy_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`MAP` handle.",
               notes="All changes to the map will be committed.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle")
               ]),

        Method('Discard_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Discard all changes made to the map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc="Map")
               ]),

        Method('DupMap_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Duplicate copy of current map.",
               notes="""
               Before version 6.2. text in maps were displayed with a character set
               defining how characters above ASCII 127 would be displayed. 6.2. introduced
               Unicode in the core montaj engine that eliminated the need for such a setting and
               greatly increased the number of symbols that can be used. The only caveat
               of the new system is that text may appear corrupted (especially with GFN fonts) in
               versions prior to 6.2. for maps that was created with a version after the port.
               The constant :def_val:`DUPMAP_COPY_PRE62` provides a way to create maps that can be
               distributed to versions prior to 6.2.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc="Source :class:`MAP` object"),
                   Parameter('p2', type="MAP",
                             doc="Destination :class:`MAP` object"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DUPMAP`")
               ]),

        Method('GetLPT_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`LPT` Object of a :class:`MAP`.",
               return_type="LPT",
               return_doc=":class:`LPT` Object",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle")
               ]),

        Method('GetMapSize_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the size of the Map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X minimum in mm"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y minimun in mm"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="X maximum in mm"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y maximum in mm")
               ]),

        Method('GetMETA_MAP', module='geoengine.map', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Get the map's :class:`META`",
               notes="If the map has no :class:`META`, an empty :class:`META` will be created.",
               return_type="META",
               return_doc=":class:`META` Object",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object")
               ]),

        Method('GetREG_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the map's :class:`REG`",
               notes="If the map has no :class:`REG`, an empty :class:`REG` will be created.",
               return_type="REG",
               return_doc=":class:`REG` Object",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object")
               ]),

        Method('GroupList_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a list of all views/groups in this map.",
               notes="""
               Returns all groups in the form "ViewName\\GroupName"
               To get a :class:`LST` of groups in a specific map view, use
               the :func:`iListGroups_MVIEW` function.
               """,
               see_also="""
               :class:`LST` class.
               :func:`iListGroups_MVIEW`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type="LST",
                             doc="list to hold the view/groups.  Names may be up to 2080 characters in length.")
               ]),

        Method('GroupListEx_MAP', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get a list of views/groups in this map for this mode",
               see_also=":class:`LST` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type="LST",
                             doc="list to hold the views.  View names may be up to 2080 characters in length."),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MAP_LIST_MODE`")
               ]),

        Method('IDuplicateView_MAP', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Duplicate an entire view",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of view to duplicate"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc='Name of new view created (pass in "" and the new name is returned)'),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VIEW',
                             doc="Length of view name buffer"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Copy all groups :def:`GEO_BOOL`")
               ]),

        Method('iExistView_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Checks to see if a view exists.",
               return_type=Type.INT32_T,
               return_doc="""
               0 view does not exist.
               1 view exists.
               """,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="View name")
               ]),

        Method('IGetClassName_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a class name.",
               notes="""
               Map class names are intended to be used to record the
               names of certain view classes in the map, such as the
               "Data", "Base" and "Section" views.
               
               There can only be one name for each class, but it can
               be changed.  This lets the "Data" class name change,
               for example, so plotting can select which class to plot
               to.
               
               If a name is not set, the class name is set and
               returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="class"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="maximum name length")
               ]),

        Method('IGetFileName_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the name of the map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="returned map file name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of map name string")
               ]),

        Method('IGetMapName_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Map Name of the Map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="returned map name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of map name string")
               ]),

        Method('iPackedFiles_MAP', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="The number of packed files in the current map.",
               return_type=Type.INT32_T,
               return_doc="The number of packed files in map.",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object")
               ]),

        Method('IUnPackFilesEx_MAP', module='geoengine.map', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="UnPack all files from map to workspace.",
               notes="""
               The option to force will simply overwrite the files.
               When the non-force option is in effect the method will
               stop if any files are going to be overwritting. These
               file names will end up in the Errors string.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="(0 - Produce errors, 1 - Force overwrites)"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="List of files that are problematic returned"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_MULTI_FILE',
                             doc="Length of Error name buffer")
               ]),

        Method('IUnPackFilesToFolder_MAP', module='geoengine.map', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="UnPack all files from map to workspace.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="(0 - Produce errors, 1 - Force overwrites)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Directory to place unpacked files in."),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="List of files that are problematic returned"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_MULTI_FILE',
                             doc="Length of Error name buffer")
               ]),

        Method('PackFiles_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Pack all files in the map so that it can be mailed.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object")
               ]),

        Method('Render_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Render a map to file/device.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Plot file/device")
               ]),

        Method('ResizeAll_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Resize a map to the extents of all views.",
               notes="""
               This is the same as :func:`ResizeAllEx_MAP` with
               :def_val:`MVIEW_EXTENT_CLIP`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle")
               ]),

        Method('ResizeAllEx_MAP', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc=":func:`ResizeAll_MAP` with selection of view extent type selection.",
               notes="""
               :def_val:`MVIEW_EXTENT_VISIBLE` gives a more "reasonable" map size, and won't
               clip off labels outside a graph window.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVIEW_EXTENT`")
               ]),

        Method('rGetMapScale_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the current map scale",
               notes="""
               If there is a "Data" view, the scale is derived from
               this view.
               
               If their is no data view, the scale is derived
               from the first view that is not scaled in mm.
               otherwise, the scale is 1000 (mm).
               
               All views must be closed, or open read-only.
               """,
               return_type=Type.DOUBLE,
               return_doc="The current map scale",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle")
               ]),

        Method('SaveAsMXD_MAP', module='geoengine.map', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Save as ArcGIS :class:`MXD`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Geosoft map file name")
               ]),

        Method('SetClassName_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a class name.",
               notes="""
               Map class names are intended to be used to record the
               names of certain view classes in the map, such as the
               "Data", "Base" and "Section" views.
               
               There can only be one name for each class, but it can
               be changed.  This lets the "Data" class name change,
               for example, so plotting can select which class to plot
               to.
               
               If a name is not set, the class name is set and
               returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="class"),
                   Parameter('p3', type=Type.STRING,
                             doc="name")
               ]),

        Method('SetCurrent_MAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Sets the current map to this map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object")
               ]),

        Method('SetMapName_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Map Name of the Map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Map Name")
               ]),

        Method('SetMapScale_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the current map scale",
               notes="""
               All views in the map will be resized for the new
               map scale.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="new map scale (must be > 0).")
               ]),

        Method('SetMapSize_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the size of the Map.",
               notes="""
               The map size is area on the :class:`MAP` that contains graphics
               to be plotted.  The area can be bigger or smaller that
               the current views.  In the absense of any other information
               only the area defined by the map size is plotted.
               """,
               see_also="SetSizeViews_MAP",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X minimum in mm"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y minimun in mm"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X maximum in mm"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y maximum in mm")
               ]),

        Method('SetMETA_MAP', module='geoengine.map', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Write a :class:`META` to a map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type="META",
                             doc=":class:`META` to write to map")
               ]),

        Method('SetREG_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Write a :class:`REG` to a map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type="REG",
                             doc=":class:`REG` to write to map")
               ]),

        Method('Sync_MAP', module='geoengine.map', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Syncronize the Metadata",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Geosoft map file name")
               ]),

        Method('UnPackFiles_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="UnPack all files from map to workspace.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object")
               ]),

        Method('ViewList_MAP', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a list of all views in this map.",
               see_also=":class:`LST` class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type="LST",
                             doc="list to hold the views.  View names may be up to 2080 characters in length.")
               ]),

        Method('ViewListEx_MAP', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Get a list of views of certain types in this map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle"),
                   Parameter('p2', type="LST",
                             doc="list to hold the views.  View names may be up to 2080 characters in length."),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MAP_LIST_MODE`")
               ]),

        Method('GetDataProj_MAP', module='geoengine.map', version='8.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the projection type of the Data view of a map.",
               return_type=Type.INT32_T,
               return_doc="Project type as an integer",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` Handle")
               ])
    ]
}

