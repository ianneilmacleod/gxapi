from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('SYS',
                 doc="""
                 The :class:`SYS` library functions perform a wide range functions,
                 including the storage and retrieval of named parameters
                 from the current workspace; writing messages to the user;
                 display of progress bars; retrieving file, date and time
                 information from the operating system; and providing warning
                 and error handling functions.
                 """,
                 notes="""
                 PARAMETER CONTROL FUNCTIONS
                 
                 Parameters can be named with an index extension.
                 For example, a parameter could be named as "PARM[1]".
                 The index can be a positive number, or it can be a '*'.
                 
                 If the index is a '*' in ":func:`SetString_SYS`", then the value string
                 will be parsed into multiple values. Commas are assumed to be delimiters.
                 
                 E.g.
                 
                 :func:`SetString_SYS`("group1",
                 "multiparm[*]",
                 "value1,\\"value,2\\",\\"value 3\\",  value4  ,\\"value 5 \\"");
                 
                 This call will set   multiparm[0] ="value1"
                 multiparm[1] ="value,2"
                 multiparm[2] ="value 3"
                 multiparm[3] ="value4"
                 multiparm[4] ="value 5"
                 
                 To read a parameter, name the parameter with the index.  Thre is no
                 looped-reading ability.  For example:
                 
                 GetString_SYS("group1","multiparm[3]",sSetting);
                 
                 returns sSetting = "value4"
                 """,
                 verbatim_gxh_defines="""
#define Prompt_SYS(A,B)						IiPrompt_SYS(A,B,sizeof(B))
#define Destroy_SYS(A)						Destr_SYS((HANDLE)(A))
#define iFindPathNameEx_SYS(A,B,C,D)	iFindPathEx_SYS(A,B,C,D,sizeof(D))
#define GetDotNetGXEntries_SYS(a,b)  IiGetDotNetGXEntries_SYS(a,b,sizeof(b))
#define iFindPathName_SYS(A,B,C)  iFindPath_SYS(A,B,C,sizeof(C))
""")


gx_defines = [
    Define('ARC_LICENSE',
           doc="ArcGIS platform types",
           constants=[
               Constant('ARC_LICENSE_ENGINENOTPRESENT', value='0', type=Type.INT32_T,
                        doc="The Engine or any qualifying ArcGIS product is missing")                        ,
               Constant('ARC_LICENSE_DESKTOPENGINE', value='1', type=Type.INT32_T,
                        doc="Desktop Engine")                        ,
               Constant('ARC_LICENSE_ARCVIEW', value='2', type=Type.INT32_T,
                        doc="ArcView")                        ,
               Constant('ARC_LICENSE_ARCEDITOR', value='3', type=Type.INT32_T,
                        doc="ArcEditor")                        ,
               Constant('ARC_LICENSE_ARCINFO', value='4', type=Type.INT32_T,
                        doc="ArcInfo")                        ,
               Constant('ARC_LICENSE_ARCSERVER', value='5', type=Type.INT32_T,
                        doc="ArcServer")                        
           ]),

    Define('GEO_DIRECTORY',
           doc="Geosoft directory defines",
           constants=[
               Constant('GEO_DIRECTORY_NONE', value='0', type=Type.INT32_T,
                        doc="None")                        ,
               Constant('GEO_DIRECTORY_GEOSOFT', value='1', type=Type.INT32_T,
                        doc="Geosoft\\")                        ,
               Constant('GEO_DIRECTORY_BIN', value='2', type=Type.INT32_T,
                        doc="Geosoft\\bin")                        ,
               Constant('GEO_DIRECTORY_GER', value='3', type=Type.INT32_T,
                        doc="Geosoft\\ger")                        ,
               Constant('GEO_DIRECTORY_OMN', value='4', type=Type.INT32_T,
                        doc="Geosoft\\omn")                        ,
               Constant('GEO_DIRECTORY_TBL', value='5', type=Type.INT32_T,
                        doc="Geosoft\\tbl")                        ,
               Constant('GEO_DIRECTORY_FONTS', value='6', type=Type.INT32_T,
                        doc="Geosoft\\fonts")                        ,
               Constant('GEO_DIRECTORY_GX', value='7', type=Type.INT32_T,
                        doc="Geosoft\\gx")                        ,
               Constant('GEO_DIRECTORY_GS', value='8', type=Type.INT32_T,
                        doc="Geosoft\\gs")                        ,
               Constant('GEO_DIRECTORY_APPS', value='9', type=Type.INT32_T,
                        doc="Geosoft\\apps")                        ,
               Constant('GEO_DIRECTORY_ETC', value='10', type=Type.INT32_T,
                        doc="Geosoft\\user\\etc and then Geosoft\\etc")                        ,
               Constant('GEO_DIRECTORY_HLP', value='11', type=Type.INT32_T,
                        doc="Geosoft\\hlp")                        ,
               Constant('GEO_DIRECTORY_USER_CSV', value='14', type=Type.INT32_T,
                        doc="Geosoft\\user\\csv")                        ,
               Constant('GEO_DIRECTORY_USER_LIC', value='15', type=Type.INT32_T,
                        doc="Geosoft\\user\\lic")                        ,
               Constant('GEO_DIRECTORY_USER_INI', value='16', type=Type.INT32_T,
                        doc="Geosoft\\user\\ini")                        ,
               Constant('GEO_DIRECTORY_USER_TEMP', value='17', type=Type.INT32_T,
                        doc="Geosoft\\temp (or where the user put it)")                        ,
               Constant('GEO_DIRECTORY_USER_ETC', value='18', type=Type.INT32_T,
                        doc="Geosoft\\user\\etc")                        ,
               Constant('GEO_DIRECTORY_IMG', value='19', type=Type.INT32_T,
                        doc="Geosoft\\img")                        ,
               Constant('GEO_DIRECTORY_BAR', value='20', type=Type.INT32_T,
                        doc="Geosoft\\bar")                        ,
               Constant('GEO_DIRECTORY_MAPTEMPLATE', value='22', type=Type.INT32_T,
                        doc="Geosoft\\maptemplate")                        ,
               Constant('GEO_DIRECTORY_USER_MAPTEMPLATE', value='23', type=Type.INT32_T,
                        doc="Geosoft\\user\\maptemplate")                        ,
               Constant('GEO_DIRECTORY_PYGX', value='24', type=Type.INT32_T,
                        doc="Geosoft\\pygx")                        ,
               Constant('GEO_DIRECTORY_USER_PYGX', value='25', type=Type.INT32_T,
                        doc="Geosoft\\user\\pygx")                        ,
               Constant('GEO_DIRECTORY_USER_GX', value='26', type=Type.INT32_T,
                        doc="Geosoft\\user\\gx")                        
           ]),

    Define('REG_DOMAIN',
           doc="Registry key domains",
           constants=[
               Constant('REG_DOMAIN_MACHINE', value='0', type=Type.INT32_T,
                        doc="same as HKEY_LOCAL_MACHINE in Windows")                        ,
               Constant('REG_DOMAIN_USER', value='1', type=Type.INT32_T,
                        doc="same as HKEY_CURRENT_USER in Windows")                        
           ]),

    Define('SHELL_EXECUTE',
           doc="Shell execute defines",
           constants=[
               Constant('SW_HIDE', value='0', type=Type.INT32_T)                        ,
               Constant('SW_SHOWNORMAL', value='1', type=Type.INT32_T)                        ,
               Constant('SW_SHOWMINIMIZED', value='2', type=Type.INT32_T)                        ,
               Constant('SW_SHOWMAXIMIZED', value='3', type=Type.INT32_T)                        ,
               Constant('SW_SHOWNOACTIVATE', value='4', type=Type.INT32_T)                        ,
               Constant('SW_SHOW', value='5', type=Type.INT32_T)                        ,
               Constant('SW_MINIMIZE', value='6', type=Type.INT32_T)                        ,
               Constant('SW_SHOWMINNOACTIVE', value='7', type=Type.INT32_T)                        ,
               Constant('SW_SHOWNA', value='8', type=Type.INT32_T)                        ,
               Constant('SW_RESTORE', value='9', type=Type.INT32_T)                        ,
               Constant('SW_SHOWDEFAULT', value='10', type=Type.INT32_T)                        ,
               Constant('SW_FORCEMINIMIZE', value='11', type=Type.INT32_T)                        
           ]),

    Define('SYS_DIR',
           doc=":class:`SYS` Directory locations",
           constants=[
               Constant('SYS_DIR_LOCAL', value='0', type=Type.INT32_T,
                        doc="is the workspace working directory")                        ,
               Constant('SYS_DIR_GEOSOFT', value='1', type=Type.INT32_T,
                        doc="is the geosoft installation directory (read-only)")                        ,
               Constant('SYS_DIR_USER', value='2', type=Type.INT32_T,
                        doc="""
                        is the geosoft installation directory that
                        contains user read/write files.
                        """)                        ,
               Constant('SYS_DIR_GEOTEMP', value='3', type=Type.INT32_T,
                        doc="Geosoft Temp folder")                        ,
               Constant('SYS_DIR_WINDOWS', value='4', type=Type.INT32_T,
                        doc="Windows folder")                        ,
               Constant('SYS_DIR_SYSTEM', value='5', type=Type.INT32_T,
                        doc="Windows SYSTEM folder")                        ,
               Constant('SYS_DIR_LICENSE', value='6', type=Type.INT32_T,
                        doc="Where the license file is stored")                        ,
               Constant('SYS_DIR_RESOURCEFILES', value='7', type=Type.INT32_T,
                        doc="User RESOURCEFILES Folder")                        ,
               Constant('SYS_DIR_GEOSOFT_BAR', value='100', type=Type.INT32_T,
                        doc="BAR folder")                        ,
               Constant('SYS_DIR_GEOSOFT_BIN', value='101', type=Type.INT32_T,
                        doc="BIN folder")                        ,
               Constant('SYS_DIR_GEOSOFT_CSV', value='102', type=Type.INT32_T,
                        doc="CSV folder")                        ,
               Constant('SYS_DIR_GEOSOFT_CSV_ALIASES', value='103', type=Type.INT32_T,
                        doc="CSV ALIASES folder")                        ,
               Constant('SYS_DIR_GEOSOFT_DATA', value='104', type=Type.INT32_T,
                        doc="DATA folder")                        ,
               Constant('SYS_DIR_GEOSOFT_DBG', value='105', type=Type.INT32_T,
                        doc="DBG folder")                        ,
               Constant('SYS_DIR_GEOSOFT_ENCRYPTEDFILES', value='106', type=Type.INT32_T,
                        doc="Encrypted Files folder")                        ,
               Constant('SYS_DIR_GEOSOFT_ETC', value='107', type=Type.INT32_T,
                        doc="ETC folder")                        ,
               Constant('SYS_DIR_GEOSOFT_FONTS', value='108', type=Type.INT32_T,
                        doc="FONTS folder")                        ,
               Constant('SYS_DIR_GEOSOFT_GER', value='109', type=Type.INT32_T,
                        doc=":class:`GER` folder")                        ,
               Constant('SYS_DIR_GEOSOFT_GS', value='110', type=Type.INT32_T,
                        doc="GS folder")                        ,
               Constant('SYS_DIR_GEOSOFT_GX', value='111', type=Type.INT32_T,
                        doc="GX folder")                        ,
               Constant('SYS_DIR_GEOSOFT_HLP', value='112', type=Type.INT32_T,
                        doc="HLP folder")                        ,
               Constant('SYS_DIR_GEOSOFT_IMG', value='113', type=Type.INT32_T,
                        doc=":class:`IMG` folder")                        ,
               Constant('SYS_DIR_GEOSOFT_INI', value='114', type=Type.INT32_T,
                        doc="INI folder")                        ,
               Constant('SYS_DIR_GEOSOFT_MAPTEMPLATE', value='115', type=Type.INT32_T,
                        doc=":class:`MAPTEMPLATE` folder")                        ,
               Constant('SYS_DIR_GEOSOFT_OMN', value='116', type=Type.INT32_T,
                        doc="OMN folder")                        ,
               Constant('SYS_DIR_GEOSOFT_PAGE', value='117', type=Type.INT32_T,
                        doc="PAGE folder")                        ,
               Constant('SYS_DIR_GEOSOFT_SCHEMA', value='118', type=Type.INT32_T,
                        doc="SCHEMA folder")                        ,
               Constant('SYS_DIR_GEOSOFT_SPEC_INI', value='119', type=Type.INT32_T,
                        doc="SPEC INI older")                        ,
               Constant('SYS_DIR_GEOSOFT_STYLESHEETS', value='120', type=Type.INT32_T,
                        doc="STYLE SHEETS folder")                        ,
               Constant('SYS_DIR_GEOSOFT_TBL', value='121', type=Type.INT32_T,
                        doc="TBL folder")                        ,
               Constant('SYS_DIR_USER_CSV', value='200', type=Type.INT32_T,
                        doc="User CSV Folder")                        ,
               Constant('SYS_DIR_USER_ETC', value='201', type=Type.INT32_T,
                        doc="User ETC Folder")                        ,
               Constant('SYS_DIR_USER_GS', value='202', type=Type.INT32_T,
                        doc="User GS Folder")                        ,
               Constant('SYS_DIR_USER_HLP', value='203', type=Type.INT32_T,
                        doc="User HLP Folder")                        ,
               Constant('SYS_DIR_USER_INI', value='204', type=Type.INT32_T,
                        doc="User INI Folder")                        ,
               Constant('SYS_DIR_USER_LIC', value='205', type=Type.INT32_T,
                        doc="User LIC Folder")                        ,
               Constant('SYS_DIR_USER_MAPTEMPLATE', value='206', type=Type.INT32_T,
                        doc="User :class:`MAPTEMPLATE` Folder")                        ,
               Constant('SYS_DIR_USER_OMN', value='207', type=Type.INT32_T,
                        doc="User OMN Folder")                        ,
               Constant('SYS_DIR_USER_BAR', value='214', type=Type.INT32_T,
                        doc="User BAR Folder")                        ,
               Constant('SYS_DIR_USER_IMG', value='215', type=Type.INT32_T,
                        doc="User :class:`IMG` Folder")                        ,
               Constant('SYS_DIR_USER_STACKS', value='209', type=Type.INT32_T,
                        doc="User STACKS Folder")                        ,
               Constant('SYS_DIR_USER_TEMP', value='210', type=Type.INT32_T,
                        doc="User TEMP Folder")                        ,
               Constant('SYS_DIR_USER_SERVICES', value='211', type=Type.INT32_T,
                        doc="User SERVICES Folder")                        ,
               Constant('SYS_DIR_USER_STYLESHEETS', value='212', type=Type.INT32_T,
                        doc="User STYLESHEETS Folder")                        
           ]),

    Define('SYS_FONT',
           doc="Font types",
           constants=[
               Constant('SYS_FONT_GFN', value='1', type=Type.INT32_T,
                        doc="Geosoft GFN fonts.")                        ,
               Constant('SYS_FONT_TT', value='0', type=Type.INT32_T,
                        doc="available TrueType fonts")                        
           ]),

    Define('SYS_INFO',
           doc="System information",
           constants=[
               Constant('SYS_INFO_VERSION_MAJOR', value='0', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_VERSION_MINOR', value='1', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_VERSION_SP', value='2', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_BUILD_NUMBER', value='3', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_BUILD_LABEL', value='4', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_VERSION_LABEL', value='5', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_PRODUCTNAME', value='6', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_SERVERNAME', value='7', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_LEGALCOPYRIGHT', value='8', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_REGISTRY', value='9', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_REGISTRY_ENVIRONMENT', value='10', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_REGISTRY_SUPPORT', value='11', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_REGISTRY_INTERAPP', value='12', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_OIS_REGISTRY', value='13', type=Type.INT32_T)                        ,
               Constant('SYS_INFO_TEST_REGISTRY', value='14', type=Type.INT32_T)                        
           ]),

    Define('SYS_LINEAGE_SOURCE',
           doc="Type of lineage sources",
           constants=[
               Constant('SYS_LINEAGE_SOURCE_MAP', value='0', type=Type.INT32_T)                        ,
               Constant('SYS_LINEAGE_SOURCE_MXD', value='1', type=Type.INT32_T)                        ,
               Constant('SYS_LINEAGE_SOURCE_DB', value='2', type=Type.INT32_T)                        ,
               Constant('SYS_LINEAGE_SOURCE_MAPTEMPLATE', value='3', type=Type.INT32_T)                        ,
               Constant('SYS_LINEAGE_SOURCE_GRID', value='4', type=Type.INT32_T)                        ,
               Constant('SYS_LINEAGE_SOURCE_VOXEL', value='5', type=Type.INT32_T)                        
           ]),

    Define('SYS_MENU_CLEAR',
           doc="Font types",
           constants=[
               Constant('SYS_MENU_CLEAR_ALL', value='0', type=Type.INT32_T,
                        doc="""
                        Clear all menus excluding the coremenus.omn
                        but including any default menus specified in the settings (these will not come back in this project).
                        """)                        ,
               Constant('SYS_MENU_CLEAR_DEFAULT', value='1', type=Type.INT32_T,
                        doc="""
                        Clear all menus excluding the coremenus.omn
                        but reload any default menus specified in the settings (essentially this is a refresh
                        back to the default state again).
                        """)                        
           ]),

    Define('SYS_PATH',
           doc="""
           Get specific Geosoft paths. The path name will
           have a directory separator at the end.
           """,
           constants=[
               Constant('SYS_PATH_LOCAL', value='0', type=Type.INT32_T,
                        doc="is the workspace working directory")                        ,
               Constant('SYS_PATH_GEOSOFT', value='1', type=Type.INT32_T,
                        doc="is the geosoft installation directory (read-only)")                        ,
               Constant('SYS_PATH_GEOSOFT_USER', value='2', type=Type.INT32_T,
                        doc="""
                        is the geosoft installation directory that
                        contains user read/write files.
                        """)                        ,
               Constant('SYS_PATH_GEOTEMP', value='3', type=Type.INT32_T,
                        doc="Geosoft Temp folder")                        ,
               Constant('SYS_PATH_WINDOWS', value='4', type=Type.INT32_T,
                        doc="Windows folder")                        ,
               Constant('SYS_PATH_SYSTEM', value='5', type=Type.INT32_T,
                        doc="System folder")                        ,
               Constant('SYS_PATH_LICENSE', value='6', type=Type.INT32_T,
                        doc="Where the license file is stored")                        ,
               Constant('SYS_PATH_RESOURCEFILES', value='7', type=Type.INT32_T,
                        doc="User RESOURCEFILES Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_BAR', value='100', type=Type.INT32_T,
                        doc="BAR folder")                        ,
               Constant('SYS_PATH_GEOSOFT_BIN', value='101', type=Type.INT32_T,
                        doc="BIN folder")                        ,
               Constant('SYS_PATH_GEOSOFT_CSV', value='102', type=Type.INT32_T,
                        doc="CSV folder")                        ,
               Constant('SYS_PATH_GEOSOFT_CSV_ALIASES', value='103', type=Type.INT32_T,
                        doc="CSV ALIASES folder")                        ,
               Constant('SYS_PATH_GEOSOFT_DATA', value='104', type=Type.INT32_T,
                        doc="DATA folder")                        ,
               Constant('SYS_PATH_GEOSOFT_DBG', value='105', type=Type.INT32_T,
                        doc="DBG folder")                        ,
               Constant('SYS_PATH_GEOSOFT_ENCRYPTEDFILES', value='106', type=Type.INT32_T,
                        doc="Encrypted Files folder")                        ,
               Constant('SYS_PATH_GEOSOFT_ETC', value='107', type=Type.INT32_T,
                        doc="ETC folder")                        ,
               Constant('SYS_PATH_GEOSOFT_FONTS', value='108', type=Type.INT32_T,
                        doc="FONTS folder")                        ,
               Constant('SYS_PATH_GEOSOFT_GER', value='109', type=Type.INT32_T,
                        doc=":class:`GER` folder")                        ,
               Constant('SYS_PATH_GEOSOFT_GS', value='110', type=Type.INT32_T,
                        doc="GS folder")                        ,
               Constant('SYS_PATH_GEOSOFT_PYGX', value='126', type=Type.INT32_T,
                        doc="PYGX folder")                        ,
               Constant('SYS_PATH_GEOSOFT_GX', value='111', type=Type.INT32_T,
                        doc="GX folder")                        ,
               Constant('SYS_PATH_GEOSOFT_HLP', value='112', type=Type.INT32_T,
                        doc="HLP folder")                        ,
               Constant('SYS_PATH_GEOSOFT_IMG', value='113', type=Type.INT32_T,
                        doc=":class:`IMG` folder")                        ,
               Constant('SYS_PATH_GEOSOFT_INI', value='114', type=Type.INT32_T,
                        doc="INI folder")                        ,
               Constant('SYS_PATH_GEOSOFT_MAPTEMPLATE', value='115', type=Type.INT32_T,
                        doc=":class:`MAPTEMPLATE` folder")                        ,
               Constant('SYS_PATH_GEOSOFT_OMN', value='116', type=Type.INT32_T,
                        doc="OMN folder")                        ,
               Constant('SYS_PATH_GEOSOFT_PAGE', value='117', type=Type.INT32_T,
                        doc="PAGE folder")                        ,
               Constant('SYS_PATH_GEOSOFT_SCHEMA', value='118', type=Type.INT32_T,
                        doc="SCHEMA folder")                        ,
               Constant('SYS_PATH_GEOSOFT_SPEC_INI', value='119', type=Type.INT32_T,
                        doc="SPEC INI older")                        ,
               Constant('SYS_PATH_GEOSOFT_STYLESHEETS', value='120', type=Type.INT32_T,
                        doc="STYLE SHEETS folder")                        ,
               Constant('SYS_PATH_GEOSOFT_TBL', value='121', type=Type.INT32_T,
                        doc="TBL folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_CSV', value='200', type=Type.INT32_T,
                        doc="User CSV Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_ETC', value='201', type=Type.INT32_T,
                        doc="User ETC Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_GS', value='202', type=Type.INT32_T,
                        doc="User GS Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_GX', value='217', type=Type.INT32_T,
                        doc="User GX Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_PYGX', value='216', type=Type.INT32_T,
                        doc="User PYGX Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_HLP', value='203', type=Type.INT32_T,
                        doc="User HLP Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_INI', value='204', type=Type.INT32_T,
                        doc="User INI Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_LIC', value='205', type=Type.INT32_T,
                        doc="User LIC Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_MAPTEMPLATE', value='206', type=Type.INT32_T,
                        doc="User :class:`MAPTEMPLATE` Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_OMN', value='207', type=Type.INT32_T,
                        doc="User OMN Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_STACKS', value='209', type=Type.INT32_T,
                        doc="User STACKS Folder")                        ,
               Constant('SYS_PATH_GEOSOFT_USER_TEMP', value='210', type=Type.INT32_T,
                        doc="User TEMP Folder")                        ,
               Constant('SYS_PATH_USER_SERVICES', value='211', type=Type.INT32_T,
                        doc="User SERVICES Folder")                        ,
               Constant('SYS_PATH_USER_STYLESHEETS', value='212', type=Type.INT32_T,
                        doc="User STYLESHEETS Folder")                        
           ]),

    Define('SYS_RUN_DISPLAY',
           doc="""
           Windows Display Options
           Determine how applications are started.
           These options are not yet implemented.
           """,
           constants=[
               Constant('SYS_RUN_DISPLAY_WINDOW', value='0', type=Type.INT32_T,
                        doc="In a window  (default)")                        ,
               Constant('SYS_RUN_DISPLAY_MINIMIZE', value='8', type=Type.INT32_T,
                        doc="Maximized")                        ,
               Constant('SYS_RUN_DISPLAY_FULLSCREEN', value='16', type=Type.INT32_T,
                        doc="Full Screen")                        
           ]),

    Define('SYS_RUN_HOLD',
           doc="""
           DOS Console Options
           These options determine if and when the DOS/EXE
           console window is held. These options only work
           on DOS and EXE programs.
           """,
           constants=[
               Constant('SYS_RUN_HOLD_NEVER', value='0', type=Type.INT32_T,
                        doc="Don't wait (Default)")                        ,
               Constant('SYS_RUN_HOLD_ONERROR', value='512', type=Type.INT32_T,
                        doc="Hold the screen if there is an error")                        ,
               Constant('SYS_RUN_HOLD_ALWAYS', value='1024', type=Type.INT32_T,
                        doc="Always hold the screen")                        
           ]),

    Define('SYS_RUN_TYPE',
           doc="Type of application to run",
           constants=[
               Constant('SYS_RUN_TYPE_DOS', value='1', type=Type.INT32_T,
                        doc="Things such as .BAT files, copy commands, etc. (A console window is created)")                        ,
               Constant('SYS_RUN_TYPE_EXE', value='0', type=Type.INT32_T,
                        doc="Any program (.EXE) (a console window is created)")                        ,
               Constant('SYS_RUN_TYPE_WINDOWS', value='2', type=Type.INT32_T,
                        doc="Windows applications that do not require a console window.")                        
           ]),

    Define('SYS_RUN_WIN',
           doc="""
           Windows Options
           Should we wait for the application to
           finish or should we continue executing. If you wait
           for another program, Oasis montaj will not
           redraw or respond. We always wait for EXE and DOS programs.
           """,
           constants=[
               Constant('SYS_RUN_WIN_NOWAIT', value='0', type=Type.INT32_T,
                        doc="Never wait (default)")                        ,
               Constant('SYS_RUN_WIN_WAIT', value='2048', type=Type.INT32_T,
                        doc="Always wait")                        
           ]),

    Define('SYS_SEARCH_PATH',
           doc="Find File define",
           constants=[
               Constant('FIND_LOCAL_GEOSOFT', value='0', type=Type.INT32_T,
                        doc="Local and then Geosoft directory")                        ,
               Constant('FIND_GEOSOFT', value='1', type=Type.INT32_T,
                        doc="Geosoft directory")                        ,
               Constant('FIND_LOCAL', value='2', type=Type.INT32_T,
                        doc="Local directory")                        ,
               Constant('FIND_SHORT', value='1024', type=Type.INT32_T,
                        doc="Make the name short (FLAG that is added on)")                        
           ]),

    Define('SYS_ENCRYPTION_KEY',
           doc="How to encrypt a string. Determines the portability of the encrypted string.",
           constants=[
               Constant('SYS_ENCRYPTION_KEY_GEOSOFT_ID', value='0', type=Type.INT32_T,
                        doc="""
                        Encrypt string to currently signed-in user. The string can be decrypted
                        by the same user on any machine.
                        """)                        ,
               Constant('SYS_ENCRYPTION_KEY_GLOBAL_ID', value='1', type=Type.INT32_T,
                        doc="""
                        Encrypt string to current machine. The string can be decrypted by any
                        user on the same machine.
                        """)                        
           ])]


gx_methods = {
    'Date/Time': [

        Method('BreakDate_SYS', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Breaks a decimal date value into year, month and day.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="date value to break"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="year"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="month (0-11)"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="day   (0-30)")
               ]),

        Method('iDatetoLong_SYS', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="""
               Converts a double date to a value representing total
               days elapsed since day 0 of year 0. This uses the
               Numerical Receipies Julian function.
               """,
               return_type=Type.INT32_T,
               return_doc="x - Days",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="date")
               ]),

        Method('iTimetoLong_SYS', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Converts decimal hours to seconds in a day.",
               return_type=Type.INT32_T,
               return_doc="x - Seconds (integer)",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Time")
               ]),

        Method('rDate_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the current date in decimal years.",
               notes="""
               The FormatDate_STR function can be used to convert a date to
               a string.
               """,
               return_type=Type.DOUBLE,
               return_doc="Date in decimal years."),

        Method('rLongtoDate_SYS', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="""
               Converts a value representing total days elapsed since
               day 0 of year 0 to a geosoft date. This uses the
               Numerical Receipies Julian function.
               """,
               return_type=Type.DOUBLE,
               return_doc="x - Date",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="day")
               ]),

        Method('rLongtoTime_SYS', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Converts seconds to decimal hours.",
               return_type=Type.DOUBLE,
               return_doc="x - Time",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="seconds")
               ]),

        Method('rMakeDate_SYS', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Returns the decimal date given the year, month and day.",
               return_type=Type.DOUBLE,
               return_doc="Date in decimal years.",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="year"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="month (0-11)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="day   (0-30)")
               ]),

        Method('rSecondstoTime_SYS', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Converts fractional seconds to decimal hours.",
               return_type=Type.DOUBLE,
               return_doc="x - Time",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="seconds")
               ]),

        Method('rTime_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the current time in decimal hours.",
               notes="""
               The FormatTime_STR function can be used to convert a time to
               a string.
               """,
               return_type=Type.DOUBLE,
               return_doc="Time in decimal hours."),

        Method('rTimetoSeconds_SYS', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Converts decimal hours to seconds in a day fractional",
               return_type=Type.DOUBLE,
               return_doc="x - Number of seconds with fractions",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Time")
               ]),

        Method('rUTCDate_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the current UTC date in decimal years.",
               notes="""
               The FormatDate_STR function can be used to convert a date to
               a string.
               """,
               return_type=Type.DOUBLE,
               return_doc="Date in decimal years."),

        Method('rUTCTime_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the current UTC time in decimal hours.",
               notes="""
               The FormatTime_STR function can be used to convert a time to
               a string.
               """,
               return_type=Type.DOUBLE,
               return_doc="Time in decimal hours.")
    ],
    'Environment': [

        Method('iExistEnv_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Check if setting exists in environment.",
               return_type=Type.INT32_T,
               return_doc="""
               1 - Yes
               0 - No
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="setting")
               ]),

        Method('IGetEnv_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get an environment setting.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="setting"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="value string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="sizeof string")
               ]),

        Method('SetEnv_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set an environment setting.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="setting"),
                   Parameter('p2', type=Type.STRING,
                             doc="value")
               ])
    ],
    'Error Handling': [

        Method('iClearErrAP_SYS', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="This method is called at to clear all registered errors.",
               return_type=Type.INT32_T,
               return_doc="0 - Successful"),

        Method('iGetTopErrorAP_SYS', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the error number of the last registered error.",
               return_type=Type.INT32_T,
               return_doc="The top error number registered, 0 if none registered."),

        Method('IGetErrorMessageAP_SYS', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Return the error message text as a string.",
               notes="""
               This wrapper is mostly for use outside of GXs,
               because in general if an error is registered in a GX
               the GX would terminate before it could be called.
               Use :func:`iNumErrorsAP_SYS` to get the number of registered errors.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="the error index (0 to N-1, where N=number of registered errors)"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Buffer to return message in"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Length of buffer")
               ]),

        Method('iNumErrorsAP_SYS', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the number of registered errors.",
               notes="""
               This wrapper is mostly for use outside of GXs,
               because in general if an error is registered in a GX
               the GX would terminate before it could be called.
               """,
               see_also="GetErrorMessageAP_SYS",
               return_type=Type.INT32_T,
               return_doc="The number of registered errors."),

        Method('SetServerMessagesAP_SYS', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Control the server message handling.",
               notes="""
               Should be set to false when dialogs should not
               appear. This setting is thread specific.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="1 - Display messages, 0 - messages reported as errors")
               ])
    ],
    'Execution': [

        Method('iRun_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Run a command line process.",
               notes="""
               The Default option for each define below is the first one
               and is set to 0.
               
               We look for the command object in the following order:
               
               1. the local working directory
               2. the <geosoft>\\bin directory
               3. the system path
               """,
               return_type=Type.INT32_T,
               return_doc="""
               -1 if failed to execute task
               Exit status of the task
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="command name"),
                   Parameter('p2', type=Type.STRING,
                             doc="command line arguments"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Flags :def:`SYS_RUN_TYPE` :def:`SYS_RUN_DISPLAY` :def:`SYS_RUN_HOLD` :def:`SYS_RUN_WIN`")
               ]),

        Method('iRunGS_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Run a GS.",
               see_also=":func:`SetInteractive_SYS`, :func:`iRunGX_SYS`",
               return_type=Type.INT32_T,
               return_doc="""
               Exit status of the GS
               -1 cancelled
               0 success
               1 ended with an error.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of GS to run.")
               ]),

        Method('iRunGX_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_gui=True, 
               doc="Run a GX.",
               notes="""
               If the called GX returns an error, they will not be
               displayed until the "top" calling GX terminates, unless you
               call :func:`ShowError_SYS`().
               """,
               see_also=":func:`iRunGXEx_SYS`, :func:`SetInteractive_SYS` and :func:`iRunGS_SYS`",
               return_type=Type.INT32_T,
               return_doc="""
               Exit status of the GX:
               -1 cancelled
               0 success
               1 ended with an error.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of GX to run.")
               ]),

        Method('iRunGXEx_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_gui=True, 
               doc="Run a GX.",
               see_also=":func:`iRunGX_SYS`, :func:`SetReturn_SYS`",
               return_type=Type.INT32_T,
               return_doc="""
               Exit status of the GX:
               -1 cancelled
               0 success
               1 ended with an error.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of GX to run."),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="return value set in the child GX (0 by default)")
               ]),

        Method('iRunPDF_SYS', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Run a PDF.",
               notes="""
               The group name of the PDF variables will be "group_pdf",
               where "group" is the name given in the first argument,
               and "pdf" is the root PDF file name.
               """,
               return_type=Type.INT32_T,
               return_doc="Exit status of the task, 0 usually means success.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='group name, can be "".'),
                   Parameter('p2', type=Type.STRING,
                             doc="pdf name    (.pdf assumed)")
               ]),

        Method('iShellExecute_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="MS ShellExecute function",
               notes="""
               Examples
               
               :func:`iShellExecute_SYS`(open;http://www.geosoft.com);
               :func:`iShellExecute_SYS`(open;"mailto:geonet@lists.geosoft.com");
               :func:`iShellExecute_SYS`(open;"mailto:majordomo@lists.geosoft.com?body=UNSUBSCRIBE%20gxnet");
               """,
               see_also=":func:`DoCommand_SYS`",
               return_type=Type.INT32_T,
               return_doc="""
               return value of ShellExecute command
               
               See                ShellExecute description in MSDN
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Verb"),
                   Parameter('p2', type=Type.STRING,
                             doc="File"),
                   Parameter('p3', type=Type.STRING,
                             doc="Parameters"),
                   Parameter('p4', type=Type.STRING,
                             doc="Directory"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`SHELL_EXECUTE`")
               ]),

        Method('SetReturn_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the return value of a GX.",
               notes="This value is returned in the :func:`iRunGXEx_SYS` call only.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Return Value")
               ])
    ],
    'External DLL': [

        Method('DoCommand_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Execute an Oasis montaj command.",
               notes="""
               Commands syntax:  "[type] command"
               
               type     command
               ----     -------
               ID       Internal Menu Command
               See "Internal Menu Commands" in GX Developer documentation.
               GX       gx file name
               GS       gs file name
               DOTNET   dll file name
               Use qualifiers to specify class and method e.g. [DOTNET] geogxnet.dll(Geosoft.GX.NewGDB.NewGDB;Run)
               PDF      pdf file name
               DOS      DOS style command
               HLP      help file name
               
               The must be ONE space between the "]" and the command.  For example:
               
               :func:`DoCommand_SYS`("[ID] ID_EDIT_SELECT");  // bring up the line edit tool
               """,
               see_also="ShellExecute_SYS",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Command")
               ]),

        Method('Error_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Register an error message",
               notes="""
               Use this function to register your own error
               messages when an error occurs in your code.  Your
               errors can be provided in your own :class:`GER` file.  See
               :class:`GEOSOFT`.:class:`GER` for an example of the :class:`GER` file format.
               
               If the error # is not found in your error file, the
               OE32.:class:`GER` file, then the :class:`GEOSOFT`.:class:`GER` file will be
               searched.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='your error file name, "" if none.'),
                   Parameter('p2', type=Type.STRING,
                             doc="module name in which error occured."),
                   Parameter('p3', type=Type.INT32_T,
                             doc="error number")
               ]),

        Method('ErrorTag_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set an error message tag string",
               notes="""
               Use this method to replace tag strings in your error
               message text with run-time information.  For example,
               Geosoft error messages often use the tag strings "%1",
               "%2", etc. as place holders to be replaced by a string
               which is only known at run-time.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='tag string, ie "%1".'),
                   Parameter('p2', type=Type.STRING,
                             doc="string to replace the tag.")
               ]),

        Method('iAssertGX_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="DLL function argument error assertion",
               notes="""
               Use this function to evaluate errors in passed
               function arguments.  Functions called by GX programs
               should be tolerant of all errors in the passed argument
               list.  The :func:`iAssertGX_SYS` can be used to test each
               argument before doing any work in the function.  If
               an assertion fails, an error will be registered with
               the name of the function and the parameter name and
               a 1 will be returned.  The caller should immediatley
               cleaning up (if necessary) and return.
               
               You could also test the validity of arguments and call
               the :func:`Error_SYS`, :func:`ErrorTag_SYS` and :func:`Terminate_SYS`
               functions if you would like to provide a more specific
               error message.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 assertion passed
               1 assertion failed
               """,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="boolean expression (ie. (dB != 0.0) )"),
                   Parameter('p2', type=Type.STRING,
                             doc="module name"),
                   Parameter('p3', type=Type.STRING,
                             doc="argument name")
               ]),

        Method('iOLEAutomation_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Call OLE Automation designed to be called from Montaj.",
               return_type=Type.INT32_T,
               return_doc="Return from automation engine.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Object Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Info String"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Info Int")
               ]),

        Method('SaveLog_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Saves the main log file to another file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="output file name")
               ]),

        Method('ShowError_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Display any errors to the user.",
               notes="""
               If you call a GX from another GX using :func:`iRunGX_SYS`, and
               the called GX registers errors, they will not be displayed
               until after the "top" GX exits.
               If you wish to continue without exiting, call this function
               so that errors are displayed immediately to the user. For
               instance, when creating a new map from inside another GX:
               
               --- Run NEWMAP wizard. Keep trying if something is wrong (like a
               too-small map scale), but exit if the user cancels (iRet==-1) ---
               
               do {
               iRet = :func:`iRunGX_SYS`("newmap.gx");
               if(iRet==1) :func:`ShowError_SYS`();     // Dump errors.
               } while(iRet==1);
               
               This wrapper is not intended for use outside a GX, because it
               uses the GX run-time machinery to display the error messages.
               """,
               return_type=Type.VOID),

        Method('Terminate_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="DLL error termination",
               notes="""
               Call this function immediately before returning to
               the caller after an error has occured inside the
               DLL.  If an error has occured, you should clean-up
               (free memory, close files), call :func:`Error_SYS` to register
               your own error messages, call :func:`ErrorTag_SYS` to set any
               error message tags, call :func:`Terminate_SYS` and return.
               
               Geosoft functions that detect an error will have
               already registered their own errors and called
               :func:`Terminate_SYS`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="module name")
               ])
    ],
    'File System': [

        Method('CRCFile_SYS', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Compute the CRC of a file",
               return_type="CRC",
               return_doc="CRC Value",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('CRCFileOffset_SYS', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Compute the CRC of a file with an Offset",
               return_type="CRC",
               return_doc="CRC Value",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Offset in the file (0 for start)")
               ]),

        Method('FileRen_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Rename a file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Old file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="New file name")
               ]),

        Method('FindFilesVV_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Fill a :class:`VV` with files matching an input file mask.",
               notes="""
               Fill a :class:`VV` with files matching the input file mask.
               The :class:`VV` should be of string type.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File mask to match")
               ]),

        Method('IAbsoluteFileName_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Convert an abbreviated path name to a full path name.",
               notes="""
               This is mainly intended to convert ".\\name" to a full
               name at run-time.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input file name to resolve"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Output name, can be the same as input"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of output name")
               ]),

        Method('iCopyFile_SYS', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Copy a file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if file copied ok.
               1 if unable to copy file or source file not found.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="source file"),
                   Parameter('p2', type=Type.STRING,
                             doc="destination file")
               ]),

        Method('iDeleteFile_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete a file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if file deleted.
               1 if unable to find file or delete file.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of file to delete")
               ]),

        Method('iDeleteGIFile_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete the GI file associated with a grid.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if file deleted.
               1 if file is not found, or found but could not be deleted.
               
               This is a "one-line" function to take a grid file name,
               remove the qualifiers, add the ".gi" and delete the file.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of grid file to delete")
               ]),

        Method('iDeleteGridFile_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete a grid file and its associated GI and XML files.",
               notes="""
               Deletes the grid file first, and, if they exist, the associated GI
               and XML files.
               No error is registered if a file is not found or cannot be deleted.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if grid file deleted.
               1 if grid file not found or if one or more files is found but could not be deleted.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of grid file to delete")
               ]),

        Method('iDirExist_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Check to see if a directory exists",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Directory doesn't exist
               1 - Directory exists
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of directory to check")
               ]),

        Method('iFileExist_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Check to see if a file exists",
               notes="""
               Use the FULL path for the file name. If the full
               path is not specified, then the current working
               directory is used for the path.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - File doesn't exist
               1 - File exists
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of file to check")
               ]),

        Method('iFileSize_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns size of a file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 none/error
               x Size
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of file")
               ]),

        Method('iFileWritable_SYS', module='geoengine.core', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="""
               Check if a file can be created or opened in read-write mode
               at a specific location
               """,
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File path name to check")
               ]),

        Method('iFindPath_SYS', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Get full path for a file with Geosoft subdirectory parameter.",
               notes="""
               Directories can be resolved from the Environment section of the
               Geosoft registry, or from system environment variables that are
               not defined in the Geosoft Environment registry.  The following
               file prefixes will be replaced by the environment settings:
               
               <geosoft>      the main Geosoft installation directory
               <geosoft2>     the secondary Geosoft installation directory
               <geotemp>      the Geosoft temporary file directory
               <windows>      the operating system Windows directory
               <system>       the operating system system directory
               <other>        other environment variables
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if file found.
               1 if file not found.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File to get path name for"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`SYS_SEARCH_PATH`"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Buffer to place path name into"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of Buffer")
               ]),

        Method('iFindPathEx_SYS', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Get full path for a file.",
               notes="""
               Directories can be resolved from the Environment section of the
               Geosoft registry, or from system environment variables that are
               not defined in the Geosoft Environment registry.  The following
               file prefixes will be replaced by the environment settings:
               
               <geosoft>      the main Geosoft installation directory
               <geosoft2>     the secondary Geosoft installation directory
               <geotemp>      the Geosoft temporary file directory
               <windows>      the operating system Windows directory
               <system>       the operating system system directory
               <other>        other environment variable
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if file found.
               1 if file not found.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File to get path name for"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`SYS_SEARCH_PATH`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`GEO_DIRECTORY`"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="Buffer to place path name into"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of Buffer")
               ]),

        Method('IGetDirectory_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a directory path",
               notes="The path will always end with the file separator character",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`SYS_DIR`"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="returned directory path string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the string")
               ]),

        Method('IGetPath_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a Geosoft path",
               notes="The path name will have a directory separator at the end.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`SYS_PATH`"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="string in which to place path"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Maximum string size")
               ]),

        Method('IGetWindowsDir_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Windows directory path",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="Buff for directory path string"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the buff")
               ]),

        Method('iMakeDir_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a directory.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Directory made
               1 - Directory cannot be made
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of directory")
               ]),

        Method('iMakeFileReadonly_SYS', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set a file's read-only attribute.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if read-only attribute successfully set,
               1 if attribute change fails.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of file")
               ]),

        Method('iMakeFileWritable_SYS', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Removes a file's read-only attribute.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if read-only attribute successfully removed,
               1 if attribute change fails.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of file")
               ]),

        Method('IRelativeFileName_SYS', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Convert a file name to a relative abbreviated path name",
               notes="""
               This will produce relative paths based on the workspace
               directory into ".\\name".
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input file name to resolve"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Output name, can be the same as input"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of output name")
               ]),

        Method('IShortPathFileName_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Obtains the short path form of a specified input path.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input file name to resolve"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Output name, can be the same as input"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of output name")
               ]),

        Method('ITempFileExt_SYS', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Generate a unique file name for this extension in the temp directory.",
               notes="This is useful for created a unique tempory name for a file in the Geosoft temporary directory.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input Extesion (without .)"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Output name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of output name")
               ]),

        Method('ITempFileName_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Generate a file name for this file in the temp directory.",
               notes="""
               This is useful for created a unique tempory name for a file in the Geosoft temporary directory.
               
               From version 7.0 The file extension will match the input file, but the
               filename itself will be a process and thread unique value to ensure that
               clashes does not happen.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input file name to resolve (path is removed)"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Output name, can be the same as input"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of output name")
               ]),

        Method('ITransferPath_SYS', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Transfers file path to new file name.",
               notes="""
               The path and volume of from the input string is added to
               file name from the output string.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="input file path/name"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="output file name with path transfered"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="maximum length of output string")
               ]),

        Method('iValidFileName_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Check to see if a file name valid",
               notes="""
               Use the FULL path for the file name. If the full
               path is not specified, then the current working
               directory is used for the path.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - File name is not valid
               1 - File name is valid
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of file to check")
               ]),

        Method('iWriteInDir_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Can I create files in this directory ?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Directory doesn't allow write of does not exist
               1 - Directory allows writes
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of directory to check")
               ]),

        Method('rFileDate_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="File creation date in decimal years.",
               notes="""
               The FormatDate_STR function can be used to convert a date
               to a string.
               """,
               return_type=Type.DOUBLE,
               return_doc="Date in decimal years, :def_val:`rDUMMY` if the file does not exist.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="file name")
               ]),

        Method('rFileTime_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="File creation time in decimal hours.",
               notes="""
               The FormatTime_STR function can be used to convert a time
               to a string.
               """,
               return_type=Type.DOUBLE,
               return_doc="Date in decimal hours, :def_val:`rDUMMY` if the file does not exist.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="file name")
               ]),

        Method('rUTCFileDate_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="File creation UTC date in decimal years.",
               notes="""
               The FormatDate_STR function can be used to convert a date
               to a string.
               """,
               return_type=Type.DOUBLE,
               return_doc="Date in decimal years, :def_val:`rDUMMY` if the file does not exist.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="file name")
               ]),

        Method('rUTCFileTime_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="File creation UTC time in decimal hours.",
               notes="""
               The FormatTime_STR function can be used to convert a time
               to a string.
               """,
               return_type=Type.DOUBLE,
               return_doc="Date in decimal hours, :def_val:`rDUMMY` if the file does not exist.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="file name")
               ])
    ],
    'Global Parameter': [

        Method('GetSettingsMETA_SYS', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the settings metadata object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` object to store the settings metadata in")
               ]),

        Method('GlobalReset_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Reset the global parameters.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='new INI file name, if "", use default.')
               ]),

        Method('GlobalSet_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a global parameter setting.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the Parameter"),
                   Parameter('p2', type=Type.STRING,
                             doc="Setting")
               ]),

        Method('GlobalWrite_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Modify the global parameters.",
               notes="""
               If the global parameters have been changed, use
               this function to make the changes permanent,
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='Global INI file, if "" use default.')
               ]),

        Method('IiGlobal_SYS', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Get a global parameter setting.",
               notes="""
               The returned string will be empty if the parameter is
               not found.
               
               Parameters are derived from :class:`GEOSOFT`.INI.
               This is a standard Windows style INI
               file that contains [GROUPS], PARAMETERS and SETTINGS
               as follows
               
               [GROUP1]
               PARAM1=setting1
               PARAM2 setting2
               PARAM3 "setting3 is text"
               
               To retrieve an entry, specify the group.parameter.  For
               example, iGlobal_SYS("GROUP1.PARAM3",sSetting) will
               retrieve the string "setting is text".  The double
               quotes will not appear in the setting.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if parameter found.
               1 if parameter not found or not set.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the Parameter"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Setting returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the buffer")
               ]),

        Method('ResetSettings_SYS', module='None', version='5.1.8',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Resets the GX_HELP settings in the geosoft.ini file
               after changes have been made.
               """,
               return_type=Type.VOID),

        Method('SetSettingsMETA_SYS', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the settings metadata object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` object")
               ])
    ],
    'Licensing': [

        Method('iCheckArcLicense_SYS', module='geoengine.map', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Check to see if a ESRI ArcEngine or ArcView license is available",
               return_type=Type.INT32_T,
               return_doc="""
               1 - Licenced
               0 - Not licenced
               """),

        Method('iCheckArcLicenseEx_SYS', module='geoengine.map', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Check to see if a ESRI ArcEngine or ArcView license is available, returns type and version of available engine.",
               return_type=Type.INT32_T,
               return_doc=":def:`ARC_LICENSE`",
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="Version String"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of Version String")
               ]),

        Method('iCheckIntrinsic_SYS', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Check to see if an intrinsic object is licensed",
               return_type=Type.INT32_T,
               return_doc="""
               1 - Licenced
               0 - Not licenced
               """,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Intrinsic Class Number"),
                   Parameter('p2', type=Type.STRING,
                             doc="Intrinsic Name (must be exact)")
               ]),

        Method('iGetGeodist_SYS', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="""
               Gets a global flag that indicates whether we are
               running within the geodist library
               """,
               return_type=Type.INT32_T,
               return_doc="0 - Geodist not loaded, 1 - Geodist loaded"),

        Method('IGetLicenseClass_SYS', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="Get the current application license class.",
               notes="""
               String may be one of :  "ArcGIS"
               "OasisMontaj"
               "DapServer"
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="Class String"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Size of Class String")
               ]),

        Method('IGetLicensedUser_SYS', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the licensed user name and Company",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="User Name"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of user name"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Company Name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of Company name")
               ])
    ],
    'Lineage': [

        Method('AddLineageParameter_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a parameter to the current lineage object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Paramter Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Value")
               ]),

        Method('AddLineageSource_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a source to the current lineage object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`SYS_LINEAGE_SOURCE`"),
                   Parameter('p2', type=Type.STRING,
                             doc="Source Name")
               ]),

        Method('ClearLineageParameters_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Clear all the lineage parameters",
               return_type=Type.VOID),

        Method('ClearLineageSources_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Clear all the lineage sources",
               return_type=Type.VOID),

        Method('CopyGeoFile_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Copy a Geosoft data file and all associated files to a new folder",
               notes="""
               Grids are copied and the GI's are maintained - note that support
               for non-geosoft grids is limited since this method does not
               guarantee all grid files besides the main one are copied.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="target directory")
               ]),

        Method('IBackupGeoFile_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Backup a Geosoft data file and all associated files to a temporary folder.",
               notes="""
               Grids are copied and the GI's are maintained - note that support
               for non-geosoft grids is limited since this method does not
               guarantee all grid files besides the main one are copied.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Buffer to place the target name into"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the Buffer")
               ]),

        Method('RemoveLineageOutput_SYS', module='geoengine.core', version='7.0.1',
               availability=Availability.PUBLIC, 
               doc="Remove an output from the current lineage object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Source Name")
               ]),

        Method('RemoveLineageParameter_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Remove a parameter in the current lineage object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Paramter Name")
               ]),

        Method('RemoveLineageSource_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Remove a source from the current lineage object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Source Name")
               ]),

        Method('RestoreGeoFile_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Backup a Geosoft data file and all associated files to original location",
               notes="""
               Grids are copied and the GI's are maintained - note that support
               for non-geosoft grids is limited since this method does not
               guarantee all grid files besides the main one are copied.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Backup File Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Original file name")
               ]),

        Method('SetLineageDescription_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the description for the current lineage object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Description")
               ]),

        Method('SetLineageDisplayName_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the display name for the current lineage object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="DisplayName")
               ]),

        Method('SetLineageName_SYS', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the name for the current lineage object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name")
               ])
    ],
    'Menus and Toolbar': [

        Method('ClearMenus_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Clear all menus",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`SYS_MENU_CLEAR`")
               ]),

        Method('GetLoadedMenus_SYS', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the loaded menus.",
               notes="""
               The names of the LSTs contain the menus and the values contain any exclusions. Exlusions 
               are semicolon separated top level menu names and/or toolbar.geobar file names.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="default menus (typically a single entry based on product)"),
                   Parameter('p2', type="LST",
                             doc="loaded menus"),
                   Parameter('p3', type="LST",
                             doc="loaded user menus")
               ]),

        Method('SetLoadedMenus_SYS', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load a list of menus",
               notes="""
               The names of the LSTs contain the menus and the values contain any exclusions. Exlusions 
               are semicolon separated top level menu names and/or toolbar.geobar file names.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="default menus (typically a single entry based on product, do not change the name returned by :func:`GetLoadedMenus_SYS`)"),
                   Parameter('p2', type="LST",
                             doc="loaded menus"),
                   Parameter('p3', type="LST",
                             doc="loaded user menus")
               ]),

        Method('GetEntitlementRights_SYS', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Entitlement Rights",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="Rights")
               ])
    ],
    'Misc': [

        Method('GenerateGUID_SYS', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Genrates a GUID string (e.g. {4FEDE8BF-CDAB-430A-8026-1CCC0EC0A2EB})",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="GUID"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="Size of GUID buffer.")
               ]),

        Method('ClipboardToFile_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy text from the clipboard to a file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File name to place it into")
               ]),

        Method('CreateClipboardRA_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`RA` to read text from the clipboard.",
               notes="""
               Destroy the :class:`RA` as soon as possible. As long as it
               open the clipboard is not accessible from any
               application.
               """,
               return_type="RA",
               return_doc=":class:`RA` to use for reading."),

        Method('CreateClipboardWA_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`WA` to write text on the clipboard.",
               notes="""
               Destroy the :class:`WA` as soon as possible. As long as it
               open the clipboard is not accessible from any
               application.
               """,
               return_type="WA",
               return_doc=":class:`WA` to use for reading."),

        Method('Destr_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_cpp=True, 
               doc="Destroy ANY object made with a Create_? method",
               notes="""
               You can use this method instead of the Destroy_? methods
               which are specific to each object.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HANDLE",
                             doc="Handle to object to delete")
               ]),

        Method('EMFObjectSize_SYS', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the size of an EMF object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="EMF File holding data"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Size X"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Size Y")
               ]),

        Method('FileToClipboard_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy a text file onto the clipboard as text.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File place into clipboard")
               ]),

        Method('FontLST_SYS', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="List all Windows and geosoft fonts.",
               notes="""
               To get TT and GFN fonts, call twice with the same list
               and :def_val:`SYS_FONT_TT`, then :def_val:`SYS_FONT_GFN`, or vice-versa to
               change order of listing.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="List Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`SYS_FONT`")
               ]),

        Method('IiGetDotNetGXEntries_SYS', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="""
               Get the list of entry points that this assembly has
               exposed to Oasis montaj.
               """,
               notes="""
               The list of entry points are passed back as one
               string with each entry point seperated by a semi-colon.
               For example: NewGDB|Run;NewGDB|RunEx
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0  success
               1  error.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="name of .NET GX assembly"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="buffer to place list of entries in"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="sizeof buffer")
               ]),

        Method('SendGeneralMessage_SYS', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Send a general information message to all listners",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Message Class"),
                   Parameter('p2', type=Type.STRING,
                             doc="Message Info")
               ]),

        Method('WriteDebugLog_SYS', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method writes out information to the output
               debugging log file (in temp folder) or output window.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="String to Write out")
               ])
    ],
    'Multithreading': [

        Method('iGetThreadID_SYS', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Get the ID the current thread.",
               notes="In a single threaded application this will always be 0.",
               return_type=Type.INT32_T,
               return_doc="x - ID"),

        Method('RunMultiUserScript_SYS', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Execute a script using multithreaded users",
               notes="""
               No access is provided in the script to EMAPS
               or EDBS. Users must ensure that the resources
               that are shared are protected.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Script to run"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Number of users to run"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Number of iterations to run (for each user)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Minimum wait time between iterations (0 for none)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Maximum wait time between iterations (0 for none)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Ramp up time for users (0 for all users start immediatly)")
               ])
    ],
    'Parameter': [

        Method('ClearGroup_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Clear current contents of a group",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="group to clear")
               ]),

        Method('ClearGroupParm_SYS', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Clears all paramters in a specified group.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING)
               ]),

        Method('ClearParm_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Clears all paramters.",
               return_type=Type.VOID),

        Method('DefaultInt_SYS', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Allows a default int to be set.",
               notes="""
               The value will only be set if there is no existing
               setting.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Int Value to Set")
               ]),

        Method('DefaultReal_SYS', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Allows a default real to be set.",
               notes="""
               The value will only be set if there is no existing
               setting.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Real Value to Set")
               ]),

        Method('DefaultString_SYS', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Allows a default string to be set.",
               notes="""
               The value will only be set if there is no existing
               setting.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name"),
                   Parameter('p3', type=Type.STRING,
                             doc="String to Set it To")
               ]),

        Method('GetPattern_SYS', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Gets pattern parameters from the parameter block.",
               notes="""
               Gets all the user-definable pattern parameters from
               a specified group. Parameters are:
               "PAT_NUMBER"    0 is solid fill (default)
               "PAT_SIZE"      pattern tile size in mm. (can return :def_val:`iDUMMY`)
               "PAT_THICKNESS" pattern line thickness in percent of the tile size.
               valid range is 0-100.
               "PAT_DENSITY"   Tile spacing. A value of 1 means tiles are laid with no overlap.
               A value of 2 means they overlap each other.
               "PAT_COLOR"     The colour value.
               "PAT_BACKCOLOR" Background colour value.
               
               Returned values may be DUMMY, but will be acceptable for use with
               the :func:`iColorForm_GUI` function, to set defaults.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input group name"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Pattern"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Size,"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Thick (0-100)"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Density,"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="Pattern Color"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="Background Color")
               ]),

        Method('GetREG_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get :class:`REG` parameters.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc=":class:`REG` to add parameters to"),
                   Parameter('p2', type=Type.STRING,
                             doc="group name wanted")
               ]),

        Method('GtString_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method returns a string in the parameter block.",
               notes="""
               If the setting exits it is placed in the buffer, otherwise
               the buffer will have zero length
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Buffer to place the string into"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the Buffer")
               ]),

        Method('iExistInt_SYS', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="This method checks to see if a int parameter exists.",
               return_type=Type.INT32_T,
               return_doc="""
               1 - Yes
               0 - No
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name")
               ]),

        Method('iExistReal_SYS', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="This method checks to see if a real parameter exists.",
               return_type=Type.INT32_T,
               return_doc="""
               1 - Yes
               0 - No
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name")
               ]),

        Method('iExistString_SYS', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="This method checks to see if a string parameter exists.",
               return_type=Type.INT32_T,
               return_doc="""
               1 - Yes
               0 - No
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name")
               ]),

        Method('iGetInt_SYS', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="This method returns an int from the parameter block.",
               return_type=Type.INT32_T,
               return_doc="Int Value, :def_val:`iDUMMY` if the parameter is not set.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name")
               ]),

        Method('iGetYesNo_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Check a YES/NO Setting",
               return_type=Type.INT32_T,
               return_doc="""
               1 - if first char in setting is a "Y" or"y"
               0 - Otherwise
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name")
               ]),

        Method('IReplaceString_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc='Replace "% %" tokens in a string with parameter values',
               notes="""
               If parameter does not exist, the token is removed.  Full parameter names,
               such as "%group.name%", are used as-is.  Partial parameter names, such as
               "%name%" will have the default group attached.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="String to filter replace"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Output string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Output string length"),
                   Parameter('p4', type=Type.STRING,
                             doc="Default group name")
               ]),

        Method('LoadParm_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Reads parameters from a file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the File to read from"),
                   Parameter('p2', type=Type.STRING,
                             doc='Group Name to write read ("" for all groups)')
               ]),

        Method('rGetReal_SYS', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="This method returns a real from the parameter block.",
               return_type=Type.DOUBLE,
               return_doc="Real Value, :def_val:`rDUMMY` if parameter not set.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name")
               ]),

        Method('SaveParm_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Writes out one group (or all groups) to a file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the File"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="0 - New file, 1 - Append"),
                   Parameter('p3', type=Type.STRING,
                             doc='Group Name to write out ("" for all groups)')
               ]),

        Method('FilterParmGroup_SYS', module='geoengine.core', version='9.1.0',
               availability=Availability.PUBLIC, 
               doc="Controls filtering of specific group during logging.",
               notes="This is useful to prevent certain utility GX parameters from being recorded during GS script runs where the parameters does not influence the actual script execution.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="0 - Clear filter, 1 - Add filter")
               ]),

        Method('SetInt_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method sets an int in the parameter block.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Int Value to Set")
               ]),

        Method('SetPattern_SYS', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Sets pattern parameters in the parameter block.",
               notes="""
               Sets all the user-definable pattern parameters to
               a specified group. Parameters are:
               "PAT_NUMBER"    0 is solid fill
               "PAT_SIZE"      pattern tile size in mm.
               "PAT_THICKNESS" pattern line thickness in percent of the tile size.
               valid range is 0-100.
               "PAT_DENSITY"   Tile spacing. A value of 1 means tiles are laid with no overlap.
               A value of 2 means they overlap each other.
               "PAT_COLOR"     The colour value.
               "PAT_BACKCOLOR" Background colour value.
               
               Input values may be DUMMY.
               
               Designed for use along with the sPatternForm_GUI function.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Pattern"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Size. Input :def_val:`GS_R8DM` to use default"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Thickness (0-100).  Input :def_val:`GS_S4DM` to use default"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Density. Input :def_val:`GS_R8DM` to use default"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Pattern Color"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Background Color. Can be :def_val:`C_TRANSPARENT`")
               ]),

        Method('SetReal_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method Sets a real in the parameter block.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Real")
               ]),

        Method('SetREG_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy contents of a :class:`REG` to current parameters.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc=":class:`REG` object")
               ]),

        Method('SetString_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method sets a string in the parameter block.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name"),
                   Parameter('p3', type=Type.STRING,
                             doc="String to Set it To")
               ])
    ],
    'Progress Control': [

        Method('iCheckStop_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method is called at convenient points in the
               GX code to check if the user has asked the script
               to stop running. This method should be called by
               any GX program that may take a while to complete.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes, Terminate processing.
               """),

        Method('iProgState_SYS', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Return current progress state (On/Off)",
               notes="""
               This is useful, for instance, when calling one GX from another,
               especially if it is called multiple times in a loop.
               The called GX may turn the progress ON/OFF on its own, which
               means any progress tracking in the calling GX is disrupted.
               The called GX should use this function to determine the original
               progress state, and not turn off progress if it was already on.
               
               Returns				 0 - Progress is on
               - Progress is off
               """,
               return_type=Type.INT32_T),

        Method('ProgName_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method allows you to name the current process being
               displayed by the progress bar. This method has no affect
               if no progress bar exists.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="New Process Name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="0 - Change the Name but do not change the percentage 1 - Change the Name and Reset Percent to 0 2 - Change the Name but no Percent Bar")
               ]),

        Method('Progress_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method allows you to turn on the Progress BAR ON/OFF.
               Once the progress bar is on, use the UpdateProg method
               to drive it.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="0 - Turn Progress Bar OFF 1 - Turn Progress Bar ON")
               ]),

        Method('ProgUpdate_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method drives the Progress Bar. It is passed
               a percentage and will update the bar to reflect that
               percentage.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Percentage Completed (0-100).")
               ]),

        Method('ProgUpdateL_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Updates progress bar based on count and maxcount.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="count"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="max count >= count")
               ])
    ],
    'Registry': [

        Method('IGetSysInfo_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get system information",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`SYS_INFO`"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="returned setting"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="size of string")
               ]),

        Method('IiRegistryGetVal_SYS', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Get a registry value",
               return_type=Type.INT32_T,
               return_doc="""
               0 if value exists
               1 if value does not exist
               """,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`REG_DOMAIN`"),
                   Parameter('p2', type=Type.STRING,
                             doc="Key to set"),
                   Parameter('p3', type=Type.STRING,
                             doc="Value name within key"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="String for value data"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="size of String")
               ]),

        Method('iRegistryDeleteKey_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete a registry value",
               notes="All sub-keys and values will be deleted if they exist.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`REG_DOMAIN`"),
                   Parameter('p2', type=Type.STRING,
                             doc="Key to delete")
               ]),

        Method('iRegistryDeleteVal_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete a registry value",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`REG_DOMAIN`"),
                   Parameter('p2', type=Type.STRING,
                             doc="Key"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of value to delete")
               ]),

        Method('RegistrySetVal_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set/create a registry value",
               notes="""
               This function will create the subkey and key if either do not
               already exist.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`REG_DOMAIN`"),
                   Parameter('p2', type=Type.STRING,
                             doc="Key to set"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of Subkey within key"),
                   Parameter('p4', type=Type.STRING,
                             doc="Value for Subkey")
               ])
    ],
    'Temporary File': [

        Method('DestroyPTMP_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy PTMP.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PTMP",
                             doc="PTMP object to destroy")
               ]),

        Method('GetPTMP_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get temporary saves copy of parameter block.",
               see_also=":func:`SavePTMP_SYS`, :func:`DestroyPTMP_SYS`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PTMP",
                             doc="saved with Save_PTMP_SYS")
               ]),

        Method('SavePTMP_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Save a temporary copy of the parameter block.",
               notes="All PTMP instances will be destroyed on exit.",
               see_also=":func:`GetPTMP_SYS`, :func:`DestroyPTMP_SYS`",
               return_type="PTMP",
               return_doc="PTMP handle.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='Group Name to save, "" for everything.')
               ])
    ],
    'Termination': [

        Method('_Abort_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method terminates the execution of a script. A message
               giving the reason for the abort will be displayed along with
               the line number where we stopped in the script.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Message to display")
               ]),

        Method('_Assert_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Abort with GX line number if not true.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Expression to evaluate (0 aborts)")
               ]),

        Method('_Exit_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method terminates the execution of a script in  a regular
               fashion with no error messages displayed.
               """,
               return_type=Type.VOID),

        Method('Cancel_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               This method indicates that the GX program terminated without
               doing anything of interest and should be ignored.  In
               particular, the GX will not be logged in a recorded GS.
               """,
               return_type=Type.VOID)
    ],
    'Timing': [

        Method('iDelay_SYS', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Idle delay method.",
               return_type=Type.INT32_T,
               return_doc="success if the delay has elapsed.",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Decimal Seconds to delay")
               ]),

        Method('iGetTimer_SYS', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="return the elapsed time since the established time.",
               notes="""
               1st time through call the method with a flag of 1 to identify
               the count start time, subsequent times the time will be the time
               elapsed since the queried start time.  Do so by settign the flag to 0.
               """,
               return_type=Type.INT32_T,
               return_doc="success if the delay has elapsed.",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="1 - set start time, 0 - return elapsed time"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="start time in seconds"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="elapsed time in seconds")
               ])
    ],
    'User Interaction': [

        Method('DisplayHelp_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Display the help dialog with the specified topic highlighted",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group string to lookup in gxhelp.ini"),
                   Parameter('p2', type=Type.STRING,
                             doc="Index string to lookup in gxhelp.ini")
               ]),

        Method('DisplayHelpTopic_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Display the help dialog without topic lookup in INI files",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Help File (blank for default)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Help Topic")
               ]),

        Method('DisplayInt_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Display an integer.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the Window"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="number")
               ]),

        Method('DisplayMessage_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Display a user message.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the Window"),
                   Parameter('p2', type=Type.STRING,
                             doc="Message String")
               ]),

        Method('DisplayReal_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Display a real number.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the Window"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Number")
               ]),

        Method('iDisplayQuestion_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Display a YES/NO type question. This method waits
               for the user to hit YES or NO.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - user selected No
               1 - user selected YES
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the window"),
                   Parameter('p2', type=Type.STRING,
                             doc="Message String")
               ]),

        Method('iDisplayQuestionWithCancel_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Display a YES/NO/CANCEL type question. This method waits
               for the user to hit YES or NO or CANCEL.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - user selected No
               1 - user selected YES
               2 - user selected CANCEL
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the window"),
                   Parameter('p2', type=Type.STRING,
                             doc="Message String")
               ]),

        Method('iInteractive_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Checks to see if you should run interactively.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Run in batch mode only
               1 - Run Interactively only
               """),

        Method('IiPrompt_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Asks the User to enter a string.",
               notes="""
               The User string is displayed as the default value in the prompt.
               Empty the user string if no default is needed.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - User hit OK
               1 - user hit CANCEL
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the window"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Buffer to place the user's string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the buffer")
               ]),

        Method('iScript_SYS', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Checks to see if we are running inside OMS (script mode)",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Normal mode
               1 - Scripting mode
               
               A number of functions can only be run from inside Oasis montaj
               (such as :func:`GetDisplayAreaRaw_EMAP`), because they require an actual
               window object, such as an editable database or map. Use this
               function to prevent calls
               """),

        Method('iScriptRecord_SYS', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Checks to see if we are in scripting recording mode",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Normal mode
               1 - Recording mode
               """),

        Method('SetCursor_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the cursor on the display.",
               notes="""
               Possible Cursors:
               Normal, Horiz, Vert, Moving, Cross, Hand, NoEdit, Sun,
               View, Group, ViewSel, GroupSel, BoxSelect, Shadow, Link,
               Line, PolyLine, Polygon, Ellipse, Rectangle, Text, Symbol,
               Zoom, Pan, Rotate, InteractiveZoom, PolyFill, GetFill,
               SnapPoint, SnapLine, SnapOnPoint, SnapOnLine, NPolygon,
               ExcludeRect, ExcludePoly, ExcludeNPoly, AddVertex, DelVertex, GeneralAdd and GeneralDelete
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Cursor Names")
               ]),

        Method('SetInfoLine_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Display a message on the information line at the left
               bottom corner of the OAISIS montaj application.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Message String")
               ]),

        Method('SetInteractive_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the interactive mode.",
               notes="""
               Call to :func:`iInteractive_SYS` will return the value
               set here.
               """,
               see_also=":func:`iInteractive_SYS`, :func:`iRunGX_SYS` and :func:`iRunGS_SYS`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="0 - interactive off 1 - interative on")
               ])
    ],
    'Workspace': [

        Method('GetWorkspaceREG_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a copy of the workspace :class:`REG`;",
               notes="""
               The workspace :class:`REG` is separate from the reg used
               to store :class:`SYS` parameters.
               
               Because :func:`GetWorkspaceREG_SYS` returns a copy of the
               workspace :class:`REG`, and not the workspace :class:`REG` itself,
               you must call :func:`SetWorkspaceREG_SYS` if you make changes
               to your own :class:`REG` object and you wish them to take
               effect in the workspace :class:`REG`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc=":class:`REG` object")
               ]),

        Method('SetWorkspaceREG_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the workspace :class:`REG`;",
               notes="""
               The workspace :class:`REG` is separate from the reg used
               to store :class:`SYS` parameters.
               
               Because :func:`GetWorkspaceREG_SYS` returns a copy of the
               workspace :class:`REG`, and not the workspace :class:`REG` itself,
               you must call :func:`SetWorkspaceREG_SYS` if you make changes
               to your own :class:`REG` object and you wish them to take
               effect in the workspace :class:`REG`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="REG",
                             doc=":class:`REG` object")
               ])
    ],
    'String Encryption': [

        Method('EncryptString_SYS', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Encrypts a string for secure storage in configuration files
               or in the workspace parameters.
               """,
               return_type=Type.VOID,
               return_doc="Nothing.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input string for encryption."),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Output buffer for encrypted result."),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of output buffer."),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`SYS_ENCRYPTION_KEY`")
               ]),

        Method('DecryptString_SYS', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Decrypts a string that has been previously encrypted by :func:`EncryptString_SYS`().",
               return_type=Type.VOID,
               return_doc="Nothing.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input string for decryption."),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Output buffer for decrypted result."),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of output buffer."),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`SYS_ENCRYPTION_KEY`")
               ]),

        Method('IsEncryptedString_SYS', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Checks whether the specified string was encrypted by :func:`EncryptString_SYS`().",
               return_type=Type.INT32_T,
               return_doc="0 (false) or non-zero (true)",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input string to inspect.")
               ])
    ],
    'Miscellaneous': [

    ],
    'Obsolete': [

        Method('iGetMenuList_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Get a list of loaded menus",
               return_type=Type.INT32_T,
               return_doc="The number of loaded menus",
               parameters = [
                   Parameter('p1', type="LST",
                             doc="menu list")
               ]),

        Method('LoadMenuList_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Load a list of menus",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="menu list to load")
               ]),

        Method('LoadMenus_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Load menus with semicolon between them.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="menu to load")
               ]),

        Method('LoadCustomBar_SYS', module='None', version='5.1.5',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Load a custom toolbar into the project",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Full path to .geobar file")
               ]),

        Method('ClearCustomBar_SYS', module='None', version='5.1.5',
               availability=Availability.LICENSED, is_obsolete=True, is_app=True, 
               doc="Clear the workspaces custom toolbar",
               notes="Obsolete",
               return_type=Type.VOID),

        Method('DisplayQuestion_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="""
               Display a YES/NO type question. This method waits
               for the user to hit YES or NO.
               """,
               notes="Obsolete, use :func:`iDisplayQuestion_SYS`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - user selected No
               1 - user selected YES
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the window"),
                   Parameter('p2', type=Type.STRING,
                             doc="Message String")
               ]),

        Method('DisplayQuestionWithCancel_SYS', module='None', version='5.1.8',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="""
               Display a YES/NO/CANCEL type question. This method waits
               for the user to hit YES or NO or CANCEL.
               """,
               notes="Obsolete, use :func:`iDisplayQuestionWithCancel_SYS`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - user selected No
               1 - user selected YES
               2 - user selected CANCEL
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the window"),
                   Parameter('p2', type=Type.STRING,
                             doc="Message String")
               ]),

        Method('iCheckLicense_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Check to see if a product is licenced",
               notes="Obsolete",
               return_type=Type.INT32_T,
               return_doc="""
               1 - Product licenced
               0 - Not licenced
               """,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Product Number  (one of LIC_? defined in license.gxh)")
               ]),

        Method('iExist_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="This method checks to see if a parameter exists.",
               return_type=Type.INT32_T,
               return_doc="""
               1 - Yes
               0 - No
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Group Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter Name")
               ]),

        Method('IGetLicenseInfo_SYS', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Retrieve information about the license",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="SYS_LIC"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Buffer to place string into"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of Buffer")
               ]),

        Method('iGetParentWnd_SYS', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Get the current parent window",
               return_type=Type.INT32_T,
               return_doc="Previous parent window."),

        Method('iListDocuments_SYS', module='None', version='5.0.5',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Load the open databases or maps into a :class:`VV`.",
               notes="Obsolete",
               return_type=Type.INT32_T,
               return_doc="The number of documents listed in the :class:`VV`.",
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` of type -:def_val:`STR_FILE`"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="DOCUMENT_TYPES")
               ]),

        Method('IPrompt_SYS', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Asks the User to enter a string.",
               notes="Obsolete, use :func:`IiPrompt_SYS`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - User hit OK
               1 - user hit CANCEL
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Title of the window"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Buffer to place the user's string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the buffer")
               ]),

        Method('iSetEnvPath_SYS', module='geoengine.core', version='5.1.2',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="""
               Appends a PATH string to the existing system
               environment variable.
               """,
               notes="""
               1. This function is only supported on Windows NT 3.5,
               3.51, 4.0 and 2000 operating systems.
               2. User must have administrative priveleges in order
               to use this function.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="value to append to existing Path")
               ]),

        Method('SetParentWnd_SYS', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Set the parent window for all dialogs",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="New Parent Window")
               ])
    ],
    'GX Debugger': [

        Method('DisableGXDebugger_SYS', module='geogxdbg', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Disable GX Debugger :class:`GUI` if active",
               notes="All breakpoints will be cleared by this call.",
               return_type=Type.VOID),

        Method('EnableGXDebugger_SYS', module='geogxdbg', version='5.0.0',
               availability=Availability.PUBLIC, is_gui=True, 
               doc="Enable GX Debugger :class:`GUI`",
               notes="""
               Takes as input two strings one a path that will be scanned
               recursively for GXC source files and a second string without
               a path of the GX where the first breakpoint should be set in (i.e. "gxname.gx").
               The source of the GX should be found in the path (e.g. <path>\\somewhere\\gxname.gxc)
               and a breakpoint will be set on the first executing line of this GX. Make sure the
               GX binary is newer than the source file, otherwise unexpected results may occur. As
               soon as the GX is run the :class:`GUI` will become visible and it will be possible to set more
               breakpoints in any of the GXC files found in the path.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="path that will be scanned recursively for GXC source files"),
                   Parameter('p2', type=Type.STRING,
                             doc="name of gx where first breakpoint should be set")
               ])
    ]
}

