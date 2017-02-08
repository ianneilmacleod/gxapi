from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GUI',
                 doc="""
These are graphical functions that typically create a
dialog-style window for a specific function. Examples include
file import wizards, and the Histogram and Scatter tools.
""")


gx_defines = [
    Define('AOI_RETURN_STATE',
           doc="AOI Query Return State",
           constants=[
               Constant('AOI_RETURN_CANCEL', value='-1', type=Type.INT32_T,
                        doc="User Canceled")                        ,
               Constant('AOI_RETURN_NODEFINE', value='0', type=Type.INT32_T,
                        doc="User chose to continue with no AOI defined or available")                        ,
               Constant('AOI_RETURN_DEFINE', value='1', type=Type.INT32_T,
                        doc="User chose to continue and defined valid AOI parameters")                        
           ]),

    Define('COORDSYS_MODE',
           doc="""
           Coordinate system wizard :class:`IPJ` types allowed on return.
           The wizard present three types of projections for selection
           by the user, Geographic (GCS), Projected (PCS), and Unknown.
           (Unknown requires only that the units be defined.)
           The Editable flag must be Yes for this option to take affect,
           and is overridden internally if the user's license does not
           allow modification of projections (e.g. the OM Viewer).
           """,
           constants=[
               Constant('COORDSYS_MODE_ALL', value='0', type=Type.INT32_T,
                        doc="Allow Geographic (GCS), Projected (PCS), and Unknown")                        ,
               Constant('COORDSYS_MODE_GCS', value='1', type=Type.INT32_T,
                        doc="Allow only Geographic (GCS)")                        ,
               Constant('COORDSYS_MODE_PCS', value='2', type=Type.INT32_T,
                        doc="Allow only Projected (PCS)")                        ,
               Constant('COORDSYS_MODE_GCS_PCS', value='3', type=Type.INT32_T,
                        doc="Allow only Geographic (GCS) and Projected (PCS)")                        ,
               Constant('COORDSYS_MODE_PCS_UNKNOWN', value='4', type=Type.INT32_T,
                        doc="Allow only Projected (PCS), or Unknown")                        
           ]),

    Define('DAT_TYPE',
           doc="Type of files (grids, images) to support",
           constants=[
               Constant('DAT_TYPE_GRID', value='0', type=Type.INT32_T,
                        doc="Display only grid formats")                        ,
               Constant('DAT_TYPE_IMAGE', value='1', type=Type.INT32_T,
                        doc="Display only image formats")                        ,
               Constant('DAT_TYPE_GRID_AND_IMAGE', value='2', type=Type.INT32_T,
                        doc="Displays both grids and image formats")                        
           ]),

    Define('FILE_FILTER',
           doc="File Filters",
           constants=[
               Constant('FILE_FILTER_ALL', value='1', type=Type.INT32_T,
                        doc="All Files              *.*                  ANYWHERE")                        ,
               Constant('FILE_FILTER_GDB', value='2', type=Type.INT32_T,
                        doc="Geosoft Database       *.gdb                LOCAL")                        ,
               Constant('FILE_FILTER_GX', value='3', type=Type.INT32_T,
                        doc="Geosoft Executable     *.gx                 :class:`GEOSOFT`")                        ,
               Constant('FILE_FILTER_GS', value='4', type=Type.INT32_T,
                        doc="Geosoft Script         *.gs                 BOTH")                        ,
               Constant('FILE_FILTER_INI', value='5', type=Type.INT32_T,
                        doc="Parameter Files        *.ini                :class:`GEOSOFT`")                        ,
               Constant('FILE_FILTER_OMN', value='6', type=Type.INT32_T,
                        doc="Oasis Menu Files       *.omn                :class:`GEOSOFT`")                        ,
               Constant('FILE_FILTER_VU', value='7', type=Type.INT32_T,
                        doc="Oasis View Files       *.vu                 LOCAL")                        ,
               Constant('FILE_FILTER_MAP', value='8', type=Type.INT32_T,
                        doc="Oasis Map Files        *.map                LOCAL")                        ,
               Constant('FILE_FILTER_PRJ', value='9', type=Type.INT32_T,
                        doc="Projection File        *.prj                LOCAL")                        ,
               Constant('FILE_FILTER_CON', value='10', type=Type.INT32_T,
                        doc="Configuration File     *.con                LOCAL")                        ,
               Constant('FILE_FILTER_MNU', value='11', type=Type.INT32_T,
                        doc="Sushi MNU Files        *.mnu                :class:`GEOSOFT`")                        ,
               Constant('FILE_FILTER_PDF', value='12', type=Type.INT32_T,
                        doc="PDF Files              *.pdf                :class:`GEOSOFT`")                        ,
               Constant('FILE_FILTER_PLT', value='13', type=Type.INT32_T,
                        doc="Geosoft PLT files      *.plt                LOCAL")                        ,
               Constant('FILE_FILTER_GWS', value='14', type=Type.INT32_T,
                        doc="Geosoft workspace      *.gws                LOCAL")                        ,
               Constant('FILE_FILTER_AGG', value='15', type=Type.INT32_T,
                        doc="Aggregate              *.agg                LOCAL")                        ,
               Constant('FILE_FILTER_TBL', value='16', type=Type.INT32_T,
                        doc="Color Table            *.tbl                :class:`GEOSOFT`")                        ,
               Constant('FILE_FILTER_ZON', value='17', type=Type.INT32_T,
                        doc="Zone                   *.zon                LOCAL")                        ,
               Constant('FILE_FILTER_ITR', value='18', type=Type.INT32_T,
                        doc="Image transform        *.itr                LOCAL")                        ,
               Constant('FILE_FILTER_DXF', value='19', type=Type.INT32_T,
                        doc="AutoCAD DXF files      *.dxf                LOCAL")                        ,
               Constant('FILE_FILTER_TIF', value='20', type=Type.INT32_T,
                        doc="TIFF files             *.tif                LOCAL")                        ,
               Constant('FILE_FILTER_EMF', value='21', type=Type.INT32_T,
                        doc="Enhanced Metafies      *.emf                LOCAL")                        ,
               Constant('FILE_FILTER_BMP', value='22', type=Type.INT32_T,
                        doc="Bitmap files           *.bmp                LOCAL")                        ,
               Constant('FILE_FILTER_LUT', value='23', type=Type.INT32_T,
                        doc="ER Mapper LUT          *.lut                :class:`GEOSOFT`")                        ,
               Constant('FILE_FILTER_PNG', value='24', type=Type.INT32_T,
                        doc="PNG Files              *.png                LOCAL")                        ,
               Constant('FILE_FILTER_JPG', value='25', type=Type.INT32_T,
                        doc="JPG Files              *.jpg                LOCAL")                        ,
               Constant('FILE_FILTER_PCX', value='26', type=Type.INT32_T,
                        doc="PCX Files              *.pcx                LOCAL")                        ,
               Constant('FILE_FILTER_GIF', value='27', type=Type.INT32_T,
                        doc="GIF Files              *.gif                LOCAL")                        ,
               Constant('FILE_FILTER_GRD', value='28', type=Type.INT32_T,
                        doc="GRD Files              *.grd                LOCAL")                        ,
               Constant('FILE_FILTER_ERS', value='29', type=Type.INT32_T,
                        doc="ERS Files              *.ers                LOCAL")                        ,
               Constant('FILE_FILTER_EPS', value='30', type=Type.INT32_T,
                        doc="EPS Files              *.eps                LOCAL")                        ,
               Constant('FILE_FILTER_SHP', value='31', type=Type.INT32_T,
                        doc="ArcView Shape Files    *.shp                LOCAL")                        ,
               Constant('FILE_FILTER_CGM', value='32', type=Type.INT32_T,
                        doc="CGM Files              *.cgm                LOCAL")                        ,
               Constant('FILE_FILTER_TAB', value='33', type=Type.INT32_T,
                        doc="MapInfo Tab Files      *.tab                LOCAL")                        ,
               Constant('FILE_FILTER_COMPS', value='34', type=Type.INT32_T,
                        doc="Software Components    Components           LOCAL")                        ,
               Constant('FILE_FILTER_CSV', value='35', type=Type.INT32_T,
                        doc="MapInfo Tab Files      *.tab                LOCAL")                        ,
               Constant('FILE_FILTER_GPF', value='36', type=Type.INT32_T,
                        doc="Geosoft Project        *.gpf                LOCAL")                        ,
               Constant('FILE_FILTER_PLY', value='37', type=Type.INT32_T,
                        doc="Geosoft Polygons       *.ply                LOCAL")                        ,
               Constant('FILE_FILTER_STM', value='38', type=Type.INT32_T,
                        doc="Scatter templates      *.stm                LOCAL")                        ,
               Constant('FILE_FILTER_TTM', value='39', type=Type.INT32_T,
                        doc="Triplot templates      *.ttm                LOCAL")                        ,
               Constant('FILE_FILTER_XYZ', value='40', type=Type.INT32_T,
                        doc="Geosoft XYZ Files      *.xyz                LOCAL")                        ,
               Constant('FILE_FILTER_BAR', value='41', type=Type.INT32_T,
                        doc="Geosoft Bar File       *.geobar             LOCAL")                        ,
               Constant('FILE_FILTER_GEOSOFT_LICENSE', value='42', type=Type.INT32_T,
                        doc="Geosoft License Files   *.geosoft_license   LOCAL")                        ,
               Constant('FILE_FILTER_XML', value='43', type=Type.INT32_T,
                        doc="XML Files              *.xml                LOCAL")                        ,
               Constant('FILE_FILTER_GXNET', value='44', type=Type.INT32_T,
                        doc="GX.NET Files           *.dll                :class:`GEOSOFT`")                        ,
               Constant('FILE_FILTER_ECW', value='45', type=Type.INT32_T,
                        doc="ECW Files              *.ecw                LOCAL")                        ,
               Constant('FILE_FILTER_J2K', value='46', type=Type.INT32_T,
                        doc="J2K JPEG 2000 Files    *.j2k                LOCAL")                        ,
               Constant('FILE_FILTER_JP2', value='47', type=Type.INT32_T,
                        doc="JP2 JPEG 2000 Files    *.jp2                LOCAL")                        ,
               Constant('FILE_FILTER_SEL', value='48', type=Type.INT32_T,
                        doc="acQuire parameters     *.sel                LOCAL")                        ,
               Constant('FILE_FILTER_SVG', value='49', type=Type.INT32_T,
                        doc="SVG File               *.svg                LOCAL")                        ,
               Constant('FILE_FILTER_SVZ', value='50', type=Type.INT32_T,
                        doc="SVG Compressed File    *.svz                LOCAL")                        ,
               Constant('FILE_FILTER_WRP', value='51', type=Type.INT32_T,
                        doc="Warp File              *.wrp                LOCAL")                        ,
               Constant('FILE_FILTER_MAPPLOT', value='52', type=Type.INT32_T,
                        doc="MAPPLOT File           *.con                LOCAL")                        ,
               Constant('FILE_FILTER_DTM', value='53', type=Type.INT32_T,
                        doc="Surpac DTM Files       *.dtm                LOCAL")                        ,
               Constant('FILE_FILTER_VOXEL', value='54', type=Type.INT32_T,
                        doc="Geosoft Voxel          *.geosoft_voxel      LOCAL")                        ,
               Constant('FILE_FILTER_MAPTEMPLATE', value='55', type=Type.INT32_T,
                        doc="Map Template File      *.geosoft_maptemplate      LOCAL")                        ,
               Constant('FILE_FILTER_ACTION', value='56', type=Type.INT32_T,
                        doc="Action Scripts         *.action             LOCAL")                        ,
               Constant('FILE_FILTER_DM', value='57', type=Type.INT32_T,
                        doc="Datamine files         *.dm                 LOCAL")                        ,
               Constant('FILE_FILTER_KML', value='58', type=Type.INT32_T,
                        doc="Google Earth KML       *.kml                LOCAL")                        ,
               Constant('FILE_FILTER_KMZ', value='59', type=Type.INT32_T,
                        doc="Google Earth Compressed KML  *.kmz          LOCAL")                        ,
               Constant('FILE_FILTER_TARGET_PLAN', value='60', type=Type.INT32_T,
                        doc="Target parameter ini file for plans      *.inp    LOCAL")                        ,
               Constant('FILE_FILTER_TARGET_SECTION', value='61', type=Type.INT32_T,
                        doc="Target parameter ini file for sections   *.ins    LOCAL")                        ,
               Constant('FILE_FILTER_TARGET_STRIPLOG', value='62', type=Type.INT32_T,
                        doc="Target parameter ini file for strip logs *.inl    LOCAL")                        ,
               Constant('FILE_FILTER_TARGET_3D', value='63', type=Type.INT32_T,
                        doc="Target parameter ini file for 3D plots   *.in3    LOCAL")                        ,
               Constant('FILE_FILTER_ARGIS_LYR', value='64', type=Type.INT32_T,
                        doc="ArcGIS Layer Files			 *.lyr    LOCAL")                        ,
               Constant('FILE_FILTER_ARGIS_MXD', value='65', type=Type.INT32_T,
                        doc="ArcGIS Map Document Files	 *.mxd    LOCAL")                        ,
               Constant('FILE_FILTER_GOCAD_TS', value='66', type=Type.INT32_T,
                        doc="GOCAD TSurf Files			 *.ts     LOCAL")                        ,
               Constant('FILE_FILTER_LST', value='67', type=Type.INT32_T,
                        doc="Geosoft list of items: names, values  *.lst     LOCAL")                        ,
               Constant('FILE_FILTER_ECS', value='68', type=Type.INT32_T,
                        doc="GM-:class:`SYS` Extern Coord Sys *.ecs               LOCAL")                        ,
               Constant('FILE_FILTER_TARGET_FENCE', value='69', type=Type.INT32_T,
                        doc="Target parameter ini file for fence sections   *.ins    LOCAL")                        ,
               Constant('FILE_FILTER_GMS3D', value='70', type=Type.INT32_T,
                        doc=":class:`GMSYS` 3D Model *.geosoft_gms3d LOCAL")                        ,
               Constant('FILE_FILTER_BT2', value='71', type=Type.INT32_T,
                        doc="GEMCOM BT2 *.bt2 LOCAL")                        ,
               Constant('FILE_FILTER_BPR', value='72', type=Type.INT32_T,
                        doc="GEMCOM BPR *.bpr LOCAL")                        ,
               Constant('FILE_FILTER_BPR2', value='73', type=Type.INT32_T,
                        doc="GEMCOM BPR2 *.bpr2 LOCAL")                        ,
               Constant('FILE_FILTER_XLS', value='74', type=Type.INT32_T,
                        doc="Excel 97-2003 Workbook		*.xls					LOCAL")                        ,
               Constant('FILE_FILTER_XLSX', value='75', type=Type.INT32_T,
                        doc="Excel 2007 Workbook 			*.xlsx				LOCAL")                        ,
               Constant('FILE_FILTER_MDB', value='76', type=Type.INT32_T,
                        doc="Access 97-2003  				*.mdb 				LOCAL")                        ,
               Constant('FILE_FILTER_ACCDB', value='77', type=Type.INT32_T,
                        doc="Access 2007 					*.accdb 				LOCAL")                        ,
               Constant('FILE_FILTER_INTERSECTION_TBL', value='78', type=Type.INT32_T,
                        doc="Levelling intersection		*.tbl					LOCAL")                        ,
               Constant('FILE_FILTER_UBC_CON', value='79', type=Type.INT32_T,
                        doc="UBC DCIP2D Conductivity model files *.con		LOCAL")                        ,
               Constant('FILE_FILTER_UBC_CHG', value='80', type=Type.INT32_T,
                        doc="UBC DCIP2D Chargeability model files *.chg	LOCAL")                        ,
               Constant('FILE_FILTER_UBC_MSH', value='81', type=Type.INT32_T,
                        doc="UBC DCIP2D Mesh files		*.msh					LOCAL")                        ,
               Constant('FILE_FILTER_UBC_MSH_DAT', value='82', type=Type.INT32_T,
                        doc="UBC DCIP2D Mesh files		*.dat					LOCAL")                        ,
               Constant('FILE_FILTER_UBC_TOPO_DAT', value='83', type=Type.INT32_T,
                        doc="UBC DCIP2D Topo files		*.dat					LOCAL")                        ,
               Constant('FILE_FILTER_UBC_TOPO_XYZ', value='84', type=Type.INT32_T,
                        doc="UBC DCIP2D Topo files		*.xyz					LOCAL")                        ,
               Constant('FILE_FILTER_XYZ_TEMPLATE_I0', value='85', type=Type.INT32_T,
                        doc="XYZ Import Templates		      *.i0				LOCAL")                        ,
               Constant('FILE_FILTER_PICO_TEMPLATE_I1', value='86', type=Type.INT32_T,
                        doc="Picodas Import Templates      *.i1				LOCAL")                        ,
               Constant('FILE_FILTER_BB_TEMPLATE_I2', value='87', type=Type.INT32_T,
                        doc="Block Binary Import Templates *.i2				LOCAL")                        ,
               Constant('FILE_FILTER_ASCII_TEMPLATE_I3', value='88', type=Type.INT32_T,
                        doc="ASCII Import Templates		   *.i3				LOCAL")                        ,
               Constant('FILE_FILTER_ODBC_TEMPLATE_I4', value='89', type=Type.INT32_T,
                        doc="ODBC Import Templates		   *.i4				LOCAL")                        ,
               Constant('FILE_FILTER_EXP', value='90', type=Type.INT32_T,
                        doc="Math expression files		   *.exp  			LOCAL")                        ,
               Constant('FILE_FILTER_SEGY', value='91', type=Type.INT32_T,
                        doc="SEGY files							*.sgy  			LOCAL")                        ,
               Constant('FILE_FILTER_DAARC500', value='92', type=Type.INT32_T,
                        doc="DAARC500 files						xYYMMDD 		   LOCAL")                        ,
               Constant('FILE_FILTER_TXT', value='93', type=Type.INT32_T,
                        doc="Text files							*.txt  			LOCAL")                        ,
               Constant('FILE_FILTER_VOXEL_INVERSION', value='94', type=Type.INT32_T,
                        doc="Voxi									*.geosoft_voxi	LOCAL")                        ,
               Constant('FILE_FILTER_GMS', value='95', type=Type.INT32_T,
                        doc="GM-:class:`SYS`									*.gms	LOCAL")                        ,
               Constant('FILE_FILTER_FLT3D', value='96', type=Type.INT32_T,
                        doc="Geosoft 3D filter Files			*.flt3d			LOCAL")                        ,
               Constant('FILE_FILTER_RESOURCE_PACK', value='97', type=Type.INT32_T,
                        doc="Geosoft Resource Update Packages *.geosoft_resource_pack LOCAL")                        ,
               Constant('FILE_FILTER_GEOSTRING', value='98', type=Type.INT32_T,
                        doc="Geostring Files *.geosoft_string LOCAL")                        ,
               Constant('FILE_FILTER_GEOSURFACE', value='99', type=Type.INT32_T,
                        doc="Geosurface Files *.geosoft_surface LOCAL")                        ,
               Constant('FILE_FILTER_GEOSOFT3DV', value='100', type=Type.INT32_T,
                        doc="Geosoft :class:`3DV` *.geosoft_3dv LOCAL")                        ,
               Constant('FILE_FILTER_VECTORVOXEL', value='101', type=Type.INT32_T,
                        doc="Geosoft Vector Voxel *.geosoft_vectorvoxel LOCAL")                        ,
               Constant('FILE_FILTER_FLT', value='102', type=Type.INT32_T,
                        doc="Geosoft Filters *.flt LOCAL")                        ,
               Constant('FILE_FILTER_XYZ_TEMPLATE_O0', value='103', type=Type.INT32_T,
                        doc="XYZ Export Templates *.o0 LOCAL")                        ,
               Constant('FILE_FILTER_GMS2D', value='104', type=Type.INT32_T,
                        doc=":class:`GMSYS` 2D Model *.geosoft_gms2d LOCAL")                        ,
               Constant('FILE_FILTER_IP_DATABASE_TEMPLATE', value='105', type=Type.INT32_T,
                        doc=":class:`IP` Database Template *.geosoft_ipdatabasetemplate LOCAL")                        ,
               Constant('FILE_FILTER_GEOSOFT_RESOURCE_MODULE', value='106', type=Type.INT32_T,
                        doc="Geosoft Resource Module *.geosoft_resources  LOCAL")                        ,
               Constant('FILE_FILTER_VT', value='107', type=Type.INT32_T,
                        doc="Shell VT Files     *.vt        LOCAL")                        ,
               Constant('FILE_FILTER_INT', value='108', type=Type.INT32_T,
                        doc="Shell INT Files     *.int      LOCAL")                        ,
               Constant('FILE_FILTER_SGT', value='109', type=Type.INT32_T,
                        doc="Shell SGT Files     *.sgt      LOCAL")                        ,
               Constant('FILE_FILTER_IMGVIEW', value='110', type=Type.INT32_T,
                        doc="Image Viewer Files  *.imgview  LOCAL")                        ,
               Constant('FILE_FILTER_ZIP', value='111', type=Type.INT32_T,
                        doc="Zip Files  *.zip  LOCAL")                        ,
               Constant('FILE_FILTER_GPS_TABLE', value='112', type=Type.INT32_T,
                        doc="GPS Table *.tbl :class:`GEOSOFT`")                        ,
               Constant('FILE_FILTER_VULCAN_TRIANGULATION', value='113', type=Type.INT32_T,
                        doc="Maptek Vulcan trianguilation file   *.tbl     LOCAL")                        ,
               Constant('FILE_FILTER_VULCAN_BLOCK_MODEL', value='114', type=Type.INT32_T,
                        doc="Maptek Vulcan block model file       *.bmf                        LOCAL")                        ,
               Constant('FILE_FILTER_PRJVIEW', value='115', type=Type.INT32_T,
                        doc="Layout Files  *.prjview  LOCAL")                        ,
               Constant('FILE_FILTER_LEAPFROG_MODEL', value='116', type=Type.INT32_T,
                        doc="Leapfrog model files  *.lfm  LOCAL")                        ,
               Constant('FILE_FILTER_IOGAS', value='117', type=Type.INT32_T,
                        doc="Reflex ioGAS files  *.gas  LOCAL")                        ,
               Constant('FILE_FILTER_ASEG_ESF', value='118', type=Type.INT32_T,
                        doc="ASEG ESF File  *.esf  LOCAL")                        ,
               Constant('FILE_FILTER_LACOSTE_DAT', value='119', type=Type.INT32_T,
                        doc="Micro-g LaCoste MGS-6 gravity files  *.:class:`DAT`  LOCAL")                        ,
               Constant('FILE_FILTER_VAR', value='120', type=Type.INT32_T,
                        doc="Geosoft variogram file  *.var  LOCAL")                        ,
               Constant('FILE_FILTER_P190', value='121', type=Type.INT32_T,
                        doc="UKOOA data exchange file  *.p190  LOCAL")                        ,
               Constant('FILE_FILTER_UBC_OBS_DAT', value='122', type=Type.INT32_T,
                        doc="UBC observation files *.dat		LOCAL")                        ,
               Constant('FILE_FILTER_UBC_LOC', value='123', type=Type.INT32_T,
                        doc="UBC location files *.loc		LOCAL")                        
           ]),

    Define('FILE_FORM',
           doc="File Form Defines",
           constants=[
               Constant('FILE_FORM_OPEN', value='0', type=Type.INT32_T,
                        doc="Open a file")                        ,
               Constant('FILE_FORM_SAVE', value='1', type=Type.INT32_T,
                        doc="Save a file")                        
           ]),

    Define('GS_DIRECTORY',
           doc="Geosoft predefined directory",
           constants=[
               Constant('GS_DIRECTORY_NONE', value='0', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_GEOSOFT', value='1', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_BIN', value='2', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_GER', value='3', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_OMN', value='4', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_TBL', value='5', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_FONTS', value='6', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_GX', value='7', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_GS', value='8', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_APPS', value='9', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_ETC', value='10', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_HLP', value='11', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_GXDEV', value='12', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_COMPONENT', value='13', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_CSV', value='14', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_LIC', value='15', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_INI', value='16', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_TEMP', value='17', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_UETC', value='18', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_UMAPTEMPLATE', value='19', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_COMPONENT_SCRIPTS', value='50', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_COMPONENT_HTML', value='51', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_IMG', value='52', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_BAR', value='53', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_GXNET', value='54', type=Type.INT32_T)                        ,
               Constant('GS_DIRECTORY_MAPTEMPLATE', value='55', type=Type.INT32_T)                        
           ]),

    Define('IMPCH_TYPE',
           doc="Import Chem defines",
           constants=[
               Constant('IMPCH_TYPE_DATA', value='0', type=Type.INT32_T)                        ,
               Constant('IMPCH_TYPE_ASSAY', value='1', type=Type.INT32_T)                        
           ]),

    Define('WINDOW_STATE',
           doc="Window State Options",
           constants=[
               Constant('WINDOW_RESTORE', value='0', type=Type.INT32_T)                        ,
               Constant('WINDOW_MINIMIZE', value='1', type=Type.INT32_T)                        ,
               Constant('WINDOW_MAXIMIZE', value='2', type=Type.INT32_T)                        
           ]),

    Define('XTOOL_ALIGN',
           doc="XTool docking alignment flags",
           constants=[
               Constant('XTOOL_ALIGN_LEFT', value='1', type=Type.INT32_T)                        ,
               Constant('XTOOL_ALIGN_TOP', value='2', type=Type.INT32_T)                        ,
               Constant('XTOOL_ALIGN_RIGHT', value='4', type=Type.INT32_T)                        ,
               Constant('XTOOL_ALIGN_BOTTOM', value='8', type=Type.INT32_T)                        ,
               Constant('XTOOL_ALIGN_ANY', value='15', type=Type.INT32_T)                        
           ]),

    Define('XTOOL_DOCK',
           doc="XTool default docking state",
           constants=[
               Constant('XTOOL_DOCK_TOP', value='1', type=Type.INT32_T)                        ,
               Constant('XTOOL_DOCK_LEFT', value='2', type=Type.INT32_T)                        ,
               Constant('XTOOL_DOCK_RIGHT', value='3', type=Type.INT32_T)                        ,
               Constant('XTOOL_DOCK_BOTTOM', value='4', type=Type.INT32_T)                        ,
               Constant('XTOOL_DOCK_FLOAT', value='5', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('CreateWNDFromHWND_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Create a standard WND object from an HWND.",
               return_type="WND",
               return_doc="x - WND object created",
               parameters = [
                   Parameter('p1', type="HWND", is_val=True,
                             doc="HWND Handle")
               ]),

        Method('Fft2SpecFilter_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Interactive :class:`FFT2` radially averaged power spectrum filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the input spectrum file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the output control file")
               ]),

        Method('GetParentWND_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Get the current parent window",
               return_type="WND",
               return_doc="Parent window."),

        Method('GetPrinterLST_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Gets a list of all printers.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="List to place into")
               ]),

        Method('iGetWindowState_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Retrieve the current state of the oasis Montaj window",
               return_type=Type.INT32_T,
               return_doc=":def:`WINDOW_STATE`"),

        Method('SetWindowState_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Changes the state of the oasis Montaj window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`WINDOW_STATE`")
               ]),

        Method('GetWindowPosition_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the oasis Montaj window's position state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T, is_ref=True,
                             doc="Window left position"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Window top position"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Window right position"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Window bottom position"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Window state :def:`WINDOW_STATE`")
               ]),

        Method('SetWindowPosition_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the oasis Montaj window's position and state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Window left position"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Window top position"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Window right position"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Window bottom position"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Window state :def:`WINDOW_STATE`")
               ]),

        Method('GetWindowArea_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="Get the location of the oasis montaj window.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T, is_ref=True,
                             doc="X Min returned"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Y Min returned"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="X Max returned"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Y Max returned")
               ]),

        Method('GetClientWindowArea_GUI', module='None', version='9.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Get the location of the oasis montaj client window.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T, is_ref=True,
                             doc="X Min returned (0)"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Y Min returned (0)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="X Max returned (width)"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Y Max returned (height)")
               ]),

        Method('GridStatHist_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Display Histogram of grid",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the grid to get stats from")
               ]),

        Method('VoxelStatHist_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Display Histogram of Voxel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the Voxel to get stats from")
               ]),

        Method('iColorForm_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Select a colour.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.INT32_T, is_ref=True,
                             doc="Colour (modified)"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Ask about :def_val:`C_TRANSPARENT` if white is selected (1: yes, 0: no)?")
               ]),

        Method('iColorTransform_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Define an :class:`ITR` of up to 8 zones.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if OK
               1 if user cancels
               """,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object (modified)"),
                   Parameter('p2', type="ST",
                             doc=":class:`ST` object (input)")
               ]),

        Method('iCoordSysWizard_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Launch the coordinate system definition/display :class:`GUI`.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Editable :class:`IPJ` (0:No, 1:Yes)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`COORDSYS_MODE`"),
                   Parameter('p4', type=Type.STRING,
                             doc="Data source label"),
                   Parameter('p5', type=Type.STRING,
                             doc="Data source")
               ]),

        Method('iCoordSysWizardLicensed_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Launch the coordinate system definition/display :class:`GUI`.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc=":class:`IPJ` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Editable :class:`IPJ` (0:No, 1:Yes)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`COORDSYS_MODE`"),
                   Parameter('p4', type=Type.STRING,
                             doc="Data source label"),
                   Parameter('p5', type=Type.STRING,
                             doc="Data source")
               ]),

        Method('iCoordSysWizardGrid_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch the coordinate system definition/display :class:`GUI`.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="original grid :class:`IPJ` object"),
                   Parameter('p2', type="IPJ",
                             doc="source (target) grid :class:`IPJ` object. This is supplied so the modified orientation can be calculated and displayed."),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Editable :class:`IPJ` (0:No, 1:Yes)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`COORDSYS_MODE`"),
                   Parameter('p5', type=Type.STRING,
                             doc="Data source label"),
                   Parameter('p6', type=Type.STRING,
                             doc="Data source"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Number of cells in X"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Number of cells in Y"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Grid orgin X (grid's own coordinate system)"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Grid orgin Y (grid's own coordinate system)"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="Grid cell size X"),
                   Parameter('p12', type=Type.DOUBLE, is_ref=True,
                             doc="Grid cell size Y"),
                   Parameter('p13', type=Type.DOUBLE, is_ref=True,
                             doc="Grid rotation angle (degrees CCW)")
               ]),

        Method('iDatabaseType_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Returns the type string of an external DAO database.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               terminates on error
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="database type (returned)"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of type string")
               ]),

        Method('iDatamineType_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Returns the type of a Datamine file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name (for display purposes only)"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True)
               ]),

        Method('iExportXYZTemplateEditor_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit XYZ export template
               using a complex dialog. The Template name
               may change during editing.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the Template (can change)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Size of the Template")
               ]),

        Method('iExportXYZTemplateEditorEx_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit an XYZ export template
               using a complex dialog. The template name
               may change during editing.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Template name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of name")
               ]),

        Method('iFileFilterIndex_GUI', module='geoguilib', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the FILE_FILTER_XXX value for a file filter string.",
               return_type=Type.INT32_T,
               return_doc=":def:`FILE_FILTER`, -1 if not found",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input filter string")
               ]),

        Method('iGCSDatumWarningSHP_GUI', module='geoguilib', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Launch the GCS Datum Warning dialogue for :class:`SHP` files.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Data source"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` object")
               ]),

        Method('iGCSDatumWarningSHPDBEx_GUI', module='geoguilib', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Launch the GCS Datum Warning dialogue for :class:`SHP` files (Database).",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="Data source names"),
                   Parameter('p2', type="LST",
                             doc="Corresponding datum names"),
                   Parameter('p3', type="LST",
                             doc="Returned corresponding LDT names"),
                   Parameter('p4', type="DB")
               ]),

        Method('iGCSDatumWarningSHPEx_GUI', module='geoguilib', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Launch the GCS Datum Warning dialogue for :class:`SHP` files.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="Data source names"),
                   Parameter('p2', type="LST",
                             doc="Corresponding datum names"),
                   Parameter('p3', type="LST",
                             doc="Returned corresponding LDT names"),
                   Parameter('p4', type="MVIEW")
               ]),

        Method('iGetAreaOfInterest_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Get the current area of interest from the application.",
               return_type=Type.INT32_T,
               return_doc=":def:`AOI_RETURN_STATE`",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Min X"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Min Y"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Max X"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Max y"),
                   Parameter('p5', type="PLY",
                             doc="AOI Bounding :class:`PLY` (Filled if available, otherwise empty)"),
                   Parameter('p6', type="IPJ",
                             doc="AOI Bounding :class:`IPJ`")
               ]),

        Method('iGetAreaOfInterest3D_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Get the current area of interest from the application in 3D.",
               return_type=Type.INT32_T,
               return_doc=":def:`AOI_RETURN_STATE`",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Min X"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Min Y"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Min Z"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Max X"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Max y"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="AOI Area Max Z"),
                   Parameter('p7', type="PLY",
                             doc="AOI Bounding :class:`PLY` (Filled if available, otherwise empty)"),
                   Parameter('p8', type="IPJ",
                             doc="AOI Bounding :class:`IPJ`")
               ]),

        Method('IGetDATDefaults_GUI', module='geoguilib', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the user default extension and qualifier for grids/images.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`DAT_TYPE`"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`FILE_FORM`"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc='Returned default extension (e.g. "grd")'),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for extension"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='5',
                             doc='Returned default qualifier (e.g. "GRD")'),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for the qualifier")
               ]),

        Method('IGetFileFilter_GUI', module='geoguilib', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the defined filter, mask, extension and directory for an input filter.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`FILE_FILTER`"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Returned file filter string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of the file filter buffer"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Returned file mask string"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of the file mask buffer"),
                   Parameter('p6', type=Type.STRING, is_ref=True, size_of_param='6',
                             doc="Returned file extension"),
                   Parameter('p7', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of the file extension buffer"),
                   Parameter('p8', type=Type.INT32_T, is_ref=True,
                             doc=":def:`GS_DIRECTORY` Returned directory.")
               ]),

        Method('IGetGSDirectory_GUI', module='geoguilib', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the directory path for value of :def:`GS_DIRECTORY`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`GS_DIRECTORY` Returned directory."),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Returned directory path"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the directory path buffer")
               ]),

        Method('iGetHWNDFromWND_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, no_gxh=True, 
               doc="Get the HWND object from WND object.",
               return_type=Type.INT32_T,
               return_doc="x - HWND object",
               parameters = [
                   Parameter('p1', type="WND",
                             doc="WND Handle")
               ]),

        Method('IiBrowseDir_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Browses for a specific directory.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the Form"),
                   Parameter('p2', type=Type.STRING,
                             doc='Default path (Can be "")'),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Result Path Buffer (default on input)"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Path Buffer Size")
               ]),

        Method('IiColorTransformEx_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Define an :class:`ITR` of up to 12 zones, with file load/save buttons.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if OK
               1 if user cancels
               """,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object (modified)"),
                   Parameter('p2', type="ST",
                             doc=":class:`ST` object (input)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Max number of zones (8 or 12)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Show file load/save buttons (TRUE or FALSE)?"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='5',
                             doc="Default colour transform file name"),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for the file name")
               ]),

        Method('IiCumulativePercent_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Define a percent-based :class:`ITR` of up to 12 zones.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if OK
               1 if user cancels
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='1',
                             doc="Default colour transform file name"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for the file name"),
                   Parameter('p3', type="ITR",
                             doc=":class:`ITR` object (returned)")
               ]),

        Method('IiDatFileForm_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Grid and Image file Open/Save Form for Multiple/Single file selections",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the Form"),
                   Parameter('p2', type=Type.STRING,
                             doc="Default value"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Where the file name(s) is returned"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_MULTI_FILE',
                             doc="Size of the File Name Buffer"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DAT_TYPE`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`FILE_FORM`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Allow Multiple file selections = TRUE Single   file selections = FALSE")
               ]),

        Method('IiGenFileForm_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="General file Open/Save Form for Multiple/Single file selections and multiple filter capability",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the Form"),
                   Parameter('p2', type="VV",
                             doc="INT :class:`VV` of file filters to use :def:`FILE_FILTER` The first one is default, can pass (:class:`VV`) 0 for to use next parameter."),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`FILE_FILTER` (ignored if parameter above is not zero)"),
                   Parameter('p4', type=Type.STRING,
                             doc="Default value"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='5',
                             doc="Where the file name(s) is returned"),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_MULTI_FILE',
                             doc="Size of the File Name Buffer"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`FILE_FORM`"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Allow Multiple file selections = TRUE Single   file selections = FALSE")
               ]),

        Method('IiImportDrillDatabaseADO2_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Same as :func:`iImportDrillDatabaseADO_GUI`, but template name is returned.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="template to make (if left blank, the created template name is returned)"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the template name string"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Name of table"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('p7', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('IiImportDrillDatabaseESRI_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Same as iImportDrillDatabaseADO2_GUI, but from an ArcGIS Geodatabase",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='External database connection string  (e.g. "d:\\Personal\\test.mdb|Table" or "d:\\File\\test.gdb|TableX|FeatureClassY)"'),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="template to make (if left blank, the created template name is returned)"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the template name string"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Name of table"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL` Geosoft Geochemistry Database?"),
                   Parameter('p8', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('IiImportDrillDatabaseODBC_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Generate a template file for importing drill holes
               from ODBC database data.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='1',
                             doc="connection string"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="size of connection string returned"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="template to make"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of template string returned"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='5',
                             doc="Name of table"),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('p8', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('IiImportDrillDatabaseODBCMaxwell_GUI', module='None', version='8.3.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Same as :func:`IiImportDrillDatabaseODBC_GUI` but customized for Maxwell.",
               return_type=Type.INT32_T,
               return_doc="0-OK 1-Cancel",
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='1',
                             doc="connection string"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="size of connection string returned"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="template to make"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of template string returned"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='5',
                             doc="Name of table"),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('p8', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('iImportAsciiWizard_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Generate a template file from a gui.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make")
               ]),

        Method('iImportChemDatabase_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Generate a template file for importing Geochems Database.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Name of table"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`IMPCH_TYPE`")
               ]),

        Method('iImportChemDatabaseADO_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Improved template creation for importing geochem database (ADO).",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Name of table"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`IMPCH_TYPE`")
               ]),

        Method('iImportDatabase_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Create template to import an external database table.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="External database file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Template to make"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Name of table imported (returned)"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table string")
               ]),

        Method('iImportDatabaseADO_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Create template to import an external database table (ADO Version).",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Template to make"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Name of table imported (returned)"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table string")
               ]),

        Method('iImportDatabaseSQL_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Create template to import an external database table,
               created using SQL.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="External database file name"),
                   Parameter('p2', type=Type.STRING,
                             doc='Text file with SQL queries to use, ("" - get from database)'),
                   Parameter('p3', type=Type.STRING,
                             doc="Import template to make"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Name of table imported (returned)"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table string")
               ]),

        Method('iImportDatabaseSQLADO_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Create template to import an external database table,
               created using SQL (New ADO Version).
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('p2', type=Type.STRING,
                             doc='Text file with SQL queries to use, ("" - get from database)'),
                   Parameter('p3', type=Type.STRING,
                             doc="Import template to make"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Name of table imported (returned)"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table string")
               ]),

        Method('iImportDrillDatabaseADO_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Generate a template file for importing drill holes.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Name of table"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of table name string"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('p6', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('iImportTemplateSQL_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Create template to import an external database table; provide query.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 Cancel
               terminates on error
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="External database file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Import template to make"),
                   Parameter('p3', type=Type.STRING,
                             doc="SQL selection query to run on database"),
                   Parameter('p4', type=Type.STRING,
                             doc="Name of Oasis table to create")
               ]),

        Method('iImportTemplateSQLADO_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Create template to import an external database table; provide query.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               terminates on error
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="External database connection string (Blank for OLEDB Wizard)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Import template to make"),
                   Parameter('p3', type=Type.STRING,
                             doc="SQL selection query to run on database"),
                   Parameter('p4', type=Type.STRING,
                             doc="Name of Oasis table to create")
               ]),

        Method('iImportXYZTemplateEditor_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit XYZ import templates
               using a complex dialog. The Template name
               may change during editing.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the Template (can change)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Size of the Template"),
                   Parameter('p4', type=Type.STRING,
                             doc="Name of the XYZ file to base it on")
               ]),

        Method('IiODBCFileConnect_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Get the connection string for a file database as well as optional table name and FileUsage attribute",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               terminates on error
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Connection string (returned)"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="size of connection string"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="File Usage (0 - ODBC drivers not queried, 1 - Directory containing tables, 2 - File containing tables)"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='5',
                             doc="Table name of file (returned if plUsage==1)"),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of table name")
               ]),

        Method('IiSymbolForm_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="- Select a symbol.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='1',
                             doc="Symbol font file name"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_FILE',
                             doc="buffer size for symbol font face name"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Geosoft font? :def:`GEO_BOOL`"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="weight :def:`MVIEW_FONT_WEIGHT`"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="symbol number"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="symbol size"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="symbol angle"),
                   Parameter('p8', type=Type.INT32_T, is_ref=True,
                             doc="edge colour"),
                   Parameter('p9', type=Type.INT32_T, is_ref=True,
                             doc="fill colour")
               ]),

        Method('iMetaDataTool_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Edit a :class:`META` object",
               return_type=Type.INT32_T,
               return_doc="""
               0         - OK
               non-zero  - Cancel
               """,
               parameters = [
                   Parameter('p1', type="META",
                             doc="Meta object"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Root Token, :def_val:`H_META_INVALID_TOKEN` for root"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Display schema information ?")
               ]),

        Method('ImportChemWizard_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Generate a template file for importing geochems.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`IMPCH_TYPE`")
               ]),

        Method('ImportDrillWizard_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Generate a template file for importing drill holes.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of table"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Size of table name string"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned :def:`DH_DATA`"),
                   Parameter('p6', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('InternetTrust_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Change the Internet Trust Relationships",
               return_type=Type.VOID),

        Method('iPatternForm_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="- Select a pattern.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.INT32_T, is_ref=True,
                             doc="Current Pattern"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Current Size,           // returned"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Current Thick (0-100)   // returned"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Current Density,        // returned"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Current Pattern Color   // passed in and returned"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="Current Background Color  // passed in and returned; can be :def_val:`C_TRANSPARENT`")
               ]),

        Method('iLinePatternForm_GUI', module='None', version='8.1.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Select a line pattern.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.INT32_T, is_ref=True,
                             doc="Current Pattern"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Current Thickness"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Current Pitch"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Current Pattern Color")
               ]),

        Method('iTwoPanelSelection_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="General purpose two-panel selection.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="All available items for selection."),
                   Parameter('p2', type="LST",
                             doc="Selections (altered on output)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Title for dialog")
               ]),

        Method('iTwoPanelSelection2_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Two-panel selection, items not sorted alphabetically.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="All available items for selection."),
                   Parameter('p2', type="LST",
                             doc="Selections (altered on output)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Title for dialog")
               ]),

        Method('iTwoPanelSelectionEx_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Two-panel selection; options for sort and ability to select no items.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="All available items for selection."),
                   Parameter('p2', type="LST",
                             doc="Selections (altered on output)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Sort items alphabetically (0:No, 1:Yes)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Allow no items selected (0:No, 1:Yes)"),
                   Parameter('p5', type=Type.STRING,
                             doc="Title for dialog")
               ]),

        Method('iTwoPanelSelectionEx2_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="Two-panel selection; extended options including a help link.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="All available items for selection."),
                   Parameter('p2', type="LST",
                             doc="Selections (altered on output)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Sort items alphabetically (0:No, 1:Yes)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Allow no items selected (0:No, 1:Yes)"),
                   Parameter('p5', type=Type.STRING,
                             doc="Title for dialog"),
                   Parameter('p6', type=Type.STRING,
                             doc="Help link")
               ]),

        Method('LaunchSingleGeoDOTNETXTool_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created .Net GEOXTOOL ensuring a single instance.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Assembly name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Control Class Name"),
                   Parameter('p3', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)")
               ]),

        Method('LaunchGeoDOTNETXTool_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created .Net GEOXTOOL.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Assembly name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Control Class Name"),
                   Parameter('p3', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)")
               ]),

        Method('LaunchGeoXTool_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created GEOXTOOL.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="DLL name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Function Name"),
                   Parameter('p3', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)")
               ]),

        Method('LaunchSingleGeoDOTNETXToolEx_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created .Net GEOXTOOL ensuring a single instance.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Assembly name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Control Class Name"),
                   Parameter('p3', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`XTOOL_ALIGN` (can specify one or more or :def_val:`XTOOL_ALIGN_ANY`)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`XTOOL_DOCK`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Default width"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Default height")
               ]),

        Method('LaunchGeoDOTNETXToolEx_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created .Net GEOXTOOL.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Assembly name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Control Class Name"),
                   Parameter('p3', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`XTOOL_ALIGN` (can specify one or more or :def_val:`XTOOL_ALIGN_ANY`)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`XTOOL_DOCK`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Default width"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Default height")
               ]),

        Method('LaunchGeoXToolEx_GUI', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Launch a user created GEOXTOOL.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="DLL name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Function Name"),
                   Parameter('p3', type="META",
                             doc=":class:`META` Handle (holding tool configuration data)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`XTOOL_ALIGN` (can specify one or more or :def_val:`XTOOL_ALIGN_ANY`)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`XTOOL_DOCK`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Default width"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Default height")
               ]),

        Method('MetaDataViewer_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="View a :class:`META` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc="Meta object"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Root Token, :def_val:`H_META_INVALID_TOKEN` for root"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Display schema information ?")
               ]),

        Method('PrintFile_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Prints a file to current printer",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Filename string")
               ]),

        Method('RenderPattern_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="- Render a pattern.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HDC", is_val=True,
                             doc="DC Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="left value of the render rect in Windows coordinates (bottom>top)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="bottom value"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="right value"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="top value"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="pattern number"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="pattern Size,           // input :def_val:`GS_R8DM` to use default"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="pattern Thick (0-100)   // input :def_val:`GS_S4DM` to use default"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="pattern Density,        // input :def_val:`GS_R8DM` to use default"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="pattern Pattern Color	  // input :def_val:`GS_S4DM` to use default"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="pattern Background Color // input :def_val:`GS_S4DM` to use default; can be :def_val:`C_TRANSPARENT`"),
                   Parameter('p12', type=Type.INT32_T,
                             doc="is this window enabled?"),
                   Parameter('p13', type=Type.INT32_T,
                             doc="is this a button?"),
                   Parameter('p14', type=Type.INT32_T,
                             doc="is this window selected?")
               ]),

        Method('RenderLinePattern_GUI', module='None', version='8.1.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Render a line pattern.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HDC", is_val=True,
                             doc="DC Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="left value of the render rect in Windows coordinates (bottom>top)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="bottom value"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="right value"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="top value"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="pattern number"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="pattern thickness"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="pattern pitch"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="pattern colour"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="is this window enabled?"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="is this a button?"),
                   Parameter('p12', type=Type.INT32_T,
                             doc="is this window selected?")
               ]),

        Method('SetParentWND_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, 
               doc="Set the current parent WND",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="WND",
                             doc="New Parent Window")
               ]),

        Method('SetPrinter_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Sets the Printer.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Printer Name")
               ]),

        Method('SetProgAlwaysOn_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Ability to set the progress bar to stay visible even
               if main application is processing messages
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL` Should progress bar remain visible")
               ]),

        Method('SetWindowArea_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="Set the location of the oasis montaj window.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="X Min"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Y Min"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="X Max"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Y Max")
               ]),

        Method('ShowDirectHist_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Display Histogram of data directly",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Min    Value to display"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Max    Value to display"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Mean   Value to display"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="StdDev Value to display"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Median Value to display"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Items  Number of items this comprises"),
                   Parameter('p7', type="VV",
                             doc=":class:`VV` holding hist counts")
               ]),

        Method('ShowHist_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, is_gui=True, 
               doc="Display Histogram of data from :class:`ST`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST",
                             doc="Statistics obj")
               ]),

        Method('SimpleMapDialog_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, is_gui=True, 
               doc="General purpose map display :class:`GUI` with no interaction.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.STRING,
                             doc="HelpID")
               ]),

        Method('ThematicVoxelInfo_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Display GX.Net thematic voxel info :class:`GUI`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOX",
                             doc=":class:`VOX` object")
               ]),

        Method('Show3DViewerDialog_GUI', module='None', version='9.2.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Display a 3D viewer dialog",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title"),
                   Parameter('p2', type=Type.STRING,
                             doc="Map name"),
                   Parameter('p3', type=Type.STRING,
                             doc="View name")
               ])
    ],
    'Obsolete': [

        Method('DefineDrillITR_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="Define colour zones for gridded data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Channel to grid"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of :class:`ITR` file")
               ]),

        Method('ExportXYZTemplateEditor_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit XYZ export template
               using a complex dialog. The Template name
               may change during editing.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the Template (can change)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Size of the Template")
               ]),

        Method('ExportXYZTemplateEditorEx_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit XYZ export template
               using a complex dialog. The Template name
               may change during editing.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Template name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of name")
               ]),

        Method('GetDapData_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, is_gui=True, 
               doc="Allow the user find DAP data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="Projection of area of interest"),
                   Parameter('p2', type="PLY",
                             doc="If exact clipping is needed, supply the :class:`PLY`. If the server is able, it will do exact clipping on this region. Can be NULL (0)."),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="DAP_CLIENT")
               ]),

        Method('IiBrowseDirEdit_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, is_gui=True, 
               doc="Browses for a specific directory, user editable.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the Form"),
                   Parameter('p2', type=Type.STRING,
                             doc='Default path (Can be "")'),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Result Path Buffer (default on input)"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Path Buffer Size")
               ]),

        Method('iImportDrillDatabase_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="Generate a template file for importing drill holes.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Name of table"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of table name string"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Type of import returned (See DH_DATA_? in dh.gxh)"),
                   Parameter('p6', type="REG",
                             doc="Drill Hole Object :class:`REG` handle")
               ]),

        Method('ImportAsciiWizard_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, is_gui=True, 
               doc="Generate a template file from a gui.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make")
               ]),

        Method('ImportXYZTemplateEditor_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, is_gui=True, 
               doc="""
               Allows the user to edit XYZ import templates
               using a complex dialog. The Template name
               may change during editing.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the Template (can change)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Size of the Template"),
                   Parameter('p4', type=Type.STRING,
                             doc="Name of the XYZ file to base it on")
               ]),

        Method('IODBCFileConnect_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="""
               Get the connection string for a file database as well as
               optional table name and FileUsage attribute
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               -1 - Cancel
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Connection string (returned)"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="size of connection string"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="File Usage (0 - ODBC drivers not queried, 1 - Directory containing tables, 2 - File containing tables)"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='5',
                             doc="Table name of file (returned if plUsage==1)"),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of table name")
               ]),

        Method('QueryIPJ_GUI', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, is_gui=True, 
               doc="Display the :class:`IPJ` wizard.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ",
                             doc="Current :class:`IPJ`")
               ]),

        Method('IIPQC_GUI', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="""
               Quality Control on an :class:`IP` database. Replaced by the modal
               dialog and lLaunchIPQCTool_IPGUI.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` obj"),
                   Parameter('p3', type=Type.STRING,
                             doc="Current line"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Selected channel (returned)"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="size of channel buffer")
               ])
    ]
}

