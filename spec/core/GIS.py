from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GIS',
                 doc="""
The :class:`GIS` class is used for the import, export,
and interrogation of :class:`GIS` Data stored in external formats,
such as MapInfo® TAB files.
""")


gx_defines = [
    Define('GIS_MAP2D',
           doc="View type to create",
           constants=[
               Constant('GIS_MAP2D_PLAN', value='0', type=Type.INT32_T,
                        doc="Plan view")                        ,
               Constant('GIS_MAP2D_EWSECTION', value='1', type=Type.INT32_T,
                        doc="Section view, East-West")                        ,
               Constant('GIS_MAP2D_NSSECTION', value='2', type=Type.INT32_T,
                        doc="Section view, North-South")                        
           ]),

    Define('GIS_TYPE',
           doc="Type of file",
           constants=[
               Constant('GIS_TYPE_MAPINFO', value='1', type=Type.INT32_T,
                        doc="Mapinfo Files")                        ,
               Constant('GIS_TYPE_ARCVIEW', value='2', type=Type.INT32_T,
                        doc="ArcView files")                        ,
               Constant('GIS_TYPE_DGN', value='3', type=Type.INT32_T,
                        doc="Microstation DGN files")                        ,
               Constant('GIS_TYPE_SURPAC', value='4', type=Type.INT32_T,
                        doc="Surpac :class:`STR` and DTM files")                        ,
               Constant('GIS_TYPE_DATAMINE', value='5', type=Type.INT32_T,
                        doc="Datamine DM files")                        ,
               Constant('GIS_TYPE_GEMCOM', value='6', type=Type.INT32_T,
                        doc="GEMCOM files")                        ,
               Constant('GIS_TYPE_MICROMINE', value='7', type=Type.INT32_T,
                        doc="MICROMINE files")                        ,
               Constant('GIS_TYPE_MINESIGHT', value='8', type=Type.INT32_T,
                        doc="MINESIGHT files")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_GIS', module='geoengine.interoperability', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates a :class:`GIS` Object",
               return_type="GIS",
               return_doc=":class:`GIS` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data source (file)"),
                   Parameter('p2', type=Type.STRING,
                             doc="data qualifying information if required."),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`GIS_TYPE`")
               ]),

        Method('CreateMap2D_GIS', module='geoengine.interoperability', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc=":func:`CreateMap2D_GIS`   Create a new 2D map for :class:`GIS` imports.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Map name"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Map scale (can be :def_val:`rDUMMY`)"),
                   Parameter('p4', type="IPJ",
                             doc="Projection (no orientation)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`GIS_MAP2D`")
               ]),

        Method('Destroy_GIS', module='geoengine.interoperability', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`GIS` instance",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object to destroy")
               ]),

        Method('GetBPRModelsLST_GIS', module='geoengine.interoperability', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Get a :class:`LST` of block models contained in a Gemcom BPR or BRP2 file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="BPR or BPR2 file"),
                   Parameter('p3', type="LST",
                             doc="Returned :class:`LST` of block models")
               ]),

        Method('GetIPJ_GIS', module='geoengine.interoperability', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`GIS` :class:`IPJ`",
               return_type="IPJ",
               return_doc="""
               :class:`IPJ` handle
               NULL if error
               """,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object")
               ]),

        Method('GetMETA_GIS', module='geoengine.interoperability', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`GIS` :class:`META`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type="META",
                             doc="Meta object to store :class:`GIS` meta information")
               ]),

        Method('GetRange_GIS', module='geoengine.interoperability', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the range of data in the :class:`GIS`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X min"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X max"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y min"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y max"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Z min"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Z max")
               ]),

        Method('iDatamineType_GIS', module='geoengine.interoperability', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Returns the type of a Datamine file.",
               return_type=Type.INT32_T,
               return_doc="Datamine file types - bitwise AND of types.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of input datamine file")
               ]),

        Method('IGetFileName_GIS', module='geoengine.interoperability', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Get the file name",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` Handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="returned file name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of file name string")
               ]),

        Method('iIsMIMapFile_GIS', module='geoengine.interoperability', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns TRUE if file is a MapInfo :class:`MAP` file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if not a MapInfo :class:`MAP` file
               1 if it is.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of input map file")
               ]),

        Method('iIsMIRasterTabFile_GIS', module='geoengine.interoperability', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns TRUE if file is a MapInfo Raster TAB file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if not a MapInfo Raster TAB file
               1 if it is.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of input tab file")
               ]),

        Method('iIsMIRotatedRasterTabFile_GIS', module='geoengine.interoperability', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Returns TRUE if file is a rotated MapInfo Raster TAB file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if not a rotated MapInfo Raster TAB file
               1 if it is (see conditions below).
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of input tab file")
               ]),

        Method('iIsSHPFile3D_GIS', module='geoengine.interoperability', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Returns TRUE if an ArcView :class:`SHP` file is type POINTZ, ARCZ, POLYGONZ or MULTIPOINTZ",
               return_type=Type.INT32_T,
               return_doc="""
               0 if the :class:`SHP` file is 2D
               1 if the :class:`SHP` file is of type POINTZ, ARCZ, POLYGONZ or MULTIPOINTZ
               """,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object")
               ]),

        Method('iIsSHPFilePoint_GIS', module='geoengine.interoperability', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Returns TRUE if an ArcView :class:`SHP` file is type POINT or POINTZ",
               return_type=Type.INT32_T,
               return_doc="""
               0 if the :class:`SHP` file is not points
               if the :class:`SHP` file is of type POINT or POINTZ
               """,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object")
               ]),

        Method('iNumAttribs_GIS', module='geoengine.interoperability', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="The number of attribute fields in the :class:`GIS` dataset",
               return_type=Type.INT32_T,
               return_doc="The number of attribute fields",
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object")
               ]),

        Method('iNumShapes_GIS', module='geoengine.interoperability', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="The number of shape entities in the :class:`GIS` dataset",
               return_type=Type.INT32_T,
               return_doc="The number of shape entities",
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object")
               ]),

        Method('IScanMIRasterTabFile_GIS', module='geoengine.interoperability', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Scan and set up a MapInf RASTER.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of input file"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Name of Raster file (an :class:`IMG` :class:`DAT`)"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer length for Raster file name"),
                   Parameter('p4', type="IPJ",
                             doc="Projection")
               ]),

        Method('LoadASCII_GIS', module='geoengine.interoperability', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="Save :class:`GIS` attribute table information (string fields) into a :class:`WA`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` object")
               ]),

        Method('LoadGDB_GIS', module='geoengine.interoperability', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Load :class:`GIS` table information into a GDB.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type="DB",
                             doc="database")
               ]),

        Method('LoadMAP_GIS', module='geoengine.interoperability', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Load :class:`GIS` table drawing into a :class:`MAP`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type="MVIEW",
                             doc="view in which to place :class:`GIS` drawing.")
               ]),

        Method('LoadMAPEx_GIS', module='geoengine.interoperability', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Load :class:`GIS` table drawing into a :class:`MAP`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type="MAP",
                             doc="Map handle"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of existing data view")
               ]),

        Method('LoadMetaGroupsMAP_GIS', module='geoengine.interoperability', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Load :class:`GIS` table drawing into a :class:`MAP`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS"),
                   Parameter('p2', type="MVIEW",
                             doc="view in which to place :class:`GIS` drawing."),
                   Parameter('p3', type="META"),
                   Parameter('p4', type="META_TOKEN",
                             doc="Class"),
                   Parameter('p5', type=Type.STRING,
                             doc="Group Name prefix"),
                   Parameter('p6', type=Type.STRING,
                             doc="Name field (Empty to use ID of entity)")
               ]),

        Method('LoadPLY_GIS', module='geoengine.interoperability', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Load :class:`GIS` table drawing into a Multi-Polygon object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type="PLY",
                             doc="Polygon object in which to place :class:`GIS` shapes.")
               ]),

        Method('LoadShapesGDB_GIS', module='geoengine.interoperability', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Load :class:`GIS` shapes table information into separate lines in a GDB.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type="DB",
                             doc="database")
               ]),

        Method('SetDmWireframePtFile_GIS', module='geoengine.interoperability', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Specify the wireframe point file corresponding to the input file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the wireframe point file")
               ]),

        Method('SetIPJ_GIS', module='geoengine.interoperability', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Save the :class:`IPJ` back to :class:`GIS` file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` to save")
               ]),

        Method('SetLST_GIS', module='geoengine.interoperability', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Save a :class:`LST` of items inside the :class:`GIS` object for special use.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object to save to :class:`GIS` :class:`LST`.")
               ]),

        Method('SetMETA_GIS', module='geoengine.interoperability', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Save the :class:`META` back to :class:`GIS`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type="META",
                             doc=":class:`META` object to save to :class:`GIS` meta")
               ]),

        Method('SetTriangulationObjectIndex_GIS', module='geoengine.interoperability', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Set the triangulation object index (Micromine)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GIS",
                             doc=":class:`GIS` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Triangulation object index")
               ])
    ],
    'Obsolete': [

        Method('InvertWarp_GIS', module='geoengine.interoperability', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="DO NOT USE THIS FUNCTION - IT DOES NOTHING.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="Not used"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Not used")
               ])
    ]
}

