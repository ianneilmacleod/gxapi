from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('EMAPTEMPLATE',
                 doc="""
                 The :class:`EMAPTEMPLATE` class provides access to a map template as displayed within
                 Oasis montaj, but does not change data within the template itself.
                 It performs functions such as setting the currently displayed area,
                 or drawing "tracking" lines or boxes on the template (which are not
                 part of the template itself).
                 """,
                 notes="""
                 To obtain access to the map template itself, it is recommended practice
                 to begin with an :class:`EMAPTEMPLATE` object, and use the Lock function to
                 lock the underlying template to prevent external changes. The returned
                 :class:`MAPTEMPLATE` object may then be safely used to make changes to the template itself.
                 
                 VIRTUAL :class:`EMAPTEMPLATE` SUPPORT
                 
                 These methods are only available when running in an external application.
                 They allow the GX to open a map template and then create a Virtual :class:`EMAPTEMPLATE` from that
                 map template. The GX can then call MakeCurrent and set the current :class:`EMAPTEMPLATE` so
                 that code that follows sees this map template as the current :class:`MAPTEMPLATE`.
                 
                 Supported methods on Virtual EMAPTEMPLATEs are:
                 
                   :func:`Current_EMAPTEMPLATE`
                   :func:`CurrentNoActivate_EMAPTEMPLATE`
                   :func:`MakeCurrent_EMAPTEMPLATE`
                   :func:`iHaveCurrent_EMAPTEMPLATE`
                   :func:`CurrentIfExists_EMAPTEMPLATE`
                 
                   :func:`Lock_EMAPTEMPLATE`
                   :func:`UnLock_EMAPTEMPLATE`
                 
                   :func:`IGetName_EMAPTEMPLATE`
                 
                   :func:`iLoaded_EMAPTEMPLATE`
                   :func:`Load_EMAPTEMPLATE`
                   :func:`LoadNoActivate_EMAPTEMPLATE`
                   :func:`UnLoadVerify_EMAPTEMPLATE`
                   :func:`UnLoad_EMAPTEMPLATE`
                 
                   :func:`CreateVirtual_EMAPTEMPLATE`
                 """)


gx_defines = [
    Define('EMAPTEMPLATE_PATH',
           doc="Four forms",
           constants=[
               Constant('EMAPTEMPLATE_PATH_FULL', value='0', type=Type.INT32_T,
                        doc="d:\\directory\\file.gdb")                        ,
               Constant('EMAPTEMPLATE_PATH_DIR', value='1', type=Type.INT32_T,
                        doc="\\directory\\file.gdb")                        ,
               Constant('EMAPTEMPLATE_PATH_NAME_EXT', value='2', type=Type.INT32_T,
                        doc="file.gdb")                        ,
               Constant('EMAPTEMPLATE_PATH_NAME', value='3', type=Type.INT32_T,
                        doc="file")                        
           ]),

    Define('EMAPTEMPLATE_TRACK',
           doc="Tracking Options",
           constants=[
               Constant('EMAPTEMPLATE_TRACK_ERASE', value='1', type=Type.INT32_T,
                        doc="Erase Object after you return?")                        ,
               Constant('EMAPTEMPLATE_TRACK_RMENU', value='2', type=Type.INT32_T,
                        doc="Allow use of right-menu")                        ,
               Constant('EMAPTEMPLATE_TRACK_CYCLE', value='4', type=Type.INT32_T,
                        doc="If user holds down left-mouse, will return many times")                        
           ]),

    Define('EMAPTEMPLATE_WINDOW_POSITION',
           doc="Window Positioning Options",
           constants=[
               Constant('EMAPTEMPLATE_WINDOW_POSITION_DOCKED', value='0', type=Type.INT32_T)                        ,
               Constant('EMAPTEMPLATE_WINDOW_POSITION_FLOATING', value='1', type=Type.INT32_T)                        
           ]),

    Define('EMAPTEMPLATE_WINDOW_STATE',
           doc="Window State Options",
           constants=[
               Constant('EMAPTEMPLATE_WINDOW_RESTORE', value='0', type=Type.INT32_T)                        ,
               Constant('EMAPTEMPLATE_WINDOW_MINIMIZE', value='1', type=Type.INT32_T)                        ,
               Constant('EMAPTEMPLATE_WINDOW_MAXIMIZE', value='2', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Drag-and-drop methods': [

        Method('iDragDropEnabled_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Is drag-and-drop enabled for the map?",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object")
               ]),

        Method('SetDragDropEnabled_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set whether drag-and-drop is enabled for the map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Enables/disables drag-and-drop :def:`GEO_BOOL`")
               ])
    ],
    'General': [

        Method('Current_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited map template.",
               return_type="EMAPTEMPLATE",
               return_doc=":class:`EMAPTEMPLATE` Object"),

        Method('CurrentNoActivate_EMAPTEMPLATE', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited map template.",
               notes="""
               This function acts just like :func:`Current_EMAPTEMPLATE` except that the document is not activated (brought to foreground) and no
               guarantee is given about which document is currently active.
               """,
               return_type="EMAPTEMPLATE",
               return_doc=":class:`EMAPTEMPLATE` Object"),

        Method('CurrentIfExists_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited map.",
               return_type="EMAPTEMPLATE",
               return_doc="""
               :class:`EMAPTEMPLATE` Object to current edited map. If there is no current map,
               the user is not prompted for a map, and 0 is returned.
               """),

        Method('Destroy_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Destroy :class:`EMAPTEMPLATE` handle.",
               notes="This does not unload the map, it simply deletes the gx resource handle",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` to destroy")
               ]),

        Method('iGetMapTemplatesLST_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load the file names of open maps into a :class:`LST`.",
               return_type=Type.INT32_T,
               return_doc="""
               The number of documents loaded into the :class:`LST`.
               The :class:`LST` is cleared first.
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` to load"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EMAPTEMPLATE_PATH`")
               ]),

        Method('IGetName_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the name of the map object of this :class:`EMAPTEMPLATE`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Name returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the String")
               ]),

        Method('iHaveCurrent_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns whether a current map is loaded",
               return_type=Type.INT32_T,
               return_doc="""
               0 - no current map.
               1 - current map
               """),

        Method('iIGetSpecifiedMapName_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Find a loaded map that has a setting in its reg.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - No Map Found
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`REG` field name"),
                   Parameter('p2', type=Type.STRING,
                             doc=":class:`REG` field value to find"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="buffer for map name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size")
               ]),

        Method('iIsLocked_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Is this MapTemplate locked",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object")
               ]),

        Method('iLoaded_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns 1 if a map is loaded .",
               return_type=Type.INT32_T,
               return_doc="1 if map is loaded, 0 otherwise.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="map name")
               ]),

        Method('GetWindowPosition_EMAPTEMPLATE', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the map window's position and dock state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Window left position"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Window top position"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Window right position"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Window bottom position"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="Window state :def:`EMAPTEMPLATE_WINDOW_STATE`"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="Docked or floating :def:`EMAPTEMPLATE_WINDOW_POSITION`")
               ]),

        Method('SetWindowPosition_EMAPTEMPLATE', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the map window's position and dock state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Window left position"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Window top position"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Window right position"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Window bottom position"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Window state :def:`EMAPTEMPLATE_WINDOW_STATE`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Docked or floating :def:`EMAPTEMPLATE_WINDOW_POSITION`")
               ]),

        Method('iReadOnly_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Checks if a map is currently opened in a read-only mode.",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE")
               ]),

        Method('Load_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads maps into the editor.",
               notes="""
               The last map in the list will be the current map.
               
               Maps may already be loaded.
               
               Only the first file in the list may have a directory path.
               All other files in the list are assumed to be in the same
               directory as the first file.
               """,
               return_type="EMAPTEMPLATE",
               return_doc=":class:`EMAPTEMPLATE` Object to edited map.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="list of maps (';' or '|' delimited) to load.")
               ]),

        Method('LoadNoActivate_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads documents into the workspace",
               notes="""
               This function acts just like :func:`Load_EMAPTEMPLATE` except that the document(s) is not activated (brought to foreground) and no
               guarantee is given about which document is currently active.
               """,
               return_type="EMAPTEMPLATE",
               return_doc="""
               Handle to current edited document, which will be the last
               database in the list if multiple files were provided.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="list of documents (';' or '|' delimited) to load.")
               ]),

        Method('Lock_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method locks the Edited map.",
               return_type="MAPTEMPLATE",
               return_doc=":class:`MAPTEMPLATE` Object to map associated with edited map.",
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object")
               ]),

        Method('MakeCurrent_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Makes this :class:`EMAPTEMPLATE` object the current active object to the user.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` to make active")
               ]),

        Method('UnLoad_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads a map template.",
               notes="""
               If the map template is not loaded, nothing happens.
               Same as :func:`UnLoadVerify_EMAPTEMPLATE` with FALSE to prompt save.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the map to unload")
               ]),

        Method('UnLoadAll_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads all opened maps",
               return_type=Type.VOID),

        Method('UnLoadVerify_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads an edited map, optional prompt to save.",
               notes="""
               If the map is not loaded, nothing happens.
               If "FALSE", map is saved without a prompt.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of map to unload"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="prompt :def:`GEO_BOOL`")
               ]),

        Method('UnLock_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method unlocks the Edited map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object")
               ])
    ],
    'Input': [

        Method('iGetBox_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of a user selected box.",
               notes="""
               The coordinates are returned in the current template units
               (See GetUnits and SetUnits in :class:`MAPTEMPLATE`)
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if point returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X minimum in current view user units."),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="X maximum"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Y")
               ]),

        Method('iGetLine_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the end points of a line.",
               notes="""
               The coordinates are returned in the current template units
               (See GetUnits and SetUnits in :class:`MAPTEMPLATE`)
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if line returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X1 in view user units"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y1"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="X2"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Y2")
               ]),

        Method('iGetPoint_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of a user selected point.",
               notes="""
               The coordinates are returned in the current template units
               (See GetUnits and SetUnits in :class:`MAPTEMPLATE`)
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if point returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinate in current view user units."),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y")
               ]),

        Method('iGetRect_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of a user selected box starting at a corner.",
               notes="""
               The coordinates are returned in the current template units
               (See GetUnits and SetUnits in :class:`MAPTEMPLATE`)
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if point returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X minimum in current view user units.   (defines corner)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="X maximum"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Y")
               ]),

        Method('iTrackPoint_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get point without prompt or cursor change with tracking",
               return_type=Type.INT32_T,
               return_doc="""
               0 if point returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EMAPTEMPLATE_TRACK`"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinate in current view user units."),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y")
               ])
    ],
    'Selection Methods': [

        Method('iGetItemSelection_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Gets info about the current selected item",
               notes="If nothing is selected the string will be empty and the function will return :def_val:`GS_FALSE`;",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL` Is item a view?",
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="returned item name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of item name")
               ]),

        Method('SetItemSelection_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.LICENSED, is_app=True, 
               doc="Sets the current selected item",
               notes="An empty string will unselect everything.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="item name")
               ])
    ],
    'View Window': [

        Method('GetDisplayArea_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the area you are currently looking at.",
               notes="""
               The coordinates are based on the current template units
               (See GetUnits and SetUnits in :class:`MAPTEMPLATE`)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X Min returned"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y Min returned"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="X Max returned"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y Max returned")
               ]),

        Method('GetTemplateLayoutProps_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the base layout view properties.",
               notes="""
               This affects the display units and other related properties for the base
               view of a map.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc=":def:`GEO_BOOL` Snap to grid"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Snapping distance (always in mm)"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="View Grid"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="View Rulers"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc=":def:`LAYOUT_VIEW_UNITS` View Units"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="Grid Red Component (0-255)"),
                   Parameter('p8', type=Type.INT32_T, is_ref=True,
                             doc="Grid Green Component (0-255)"),
                   Parameter('p9', type=Type.INT32_T, is_ref=True,
                             doc="Grid Blue Component (0-255)")
               ]),

        Method('iGetWindowState_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Retrieve the current state of the map window",
               return_type=Type.INT32_T,
               return_doc=":def:`EMAPTEMPLATE_WINDOW_STATE`",
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE")
               ]),

        Method('SetDisplayArea_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the area you wish to see.",
               notes="""
               The coordinates are based on the current template units
               (See GetUnits and SetUnits in :class:`MAPTEMPLATE`)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X Min"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y Min"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X Max"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y Max")
               ]),

        Method('SetTemplateLayoutProps_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the base layout view properties.",
               notes="""
               This affects the display units and other related properties for the base
               view of a map.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL` Snap to grid"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Snapping distance (always in mm)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="View Grid"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="View Rulers"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`LAYOUT_VIEW_UNITS` View Units"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Grid Red Component (0-255)"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Grid Green Component (0-255)"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Grid Blue Component (0-255)")
               ]),

        Method('SetWindowState_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Changes the state of the map window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EMAPTEMPLATE_WINDOW_STATE`")
               ])
    ],
    'Obsolete': [

        Method('SetWindowArea_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Set the location of the map window within the frame.",
               notes="""
               The Coordinates are pixels with 0,0 being the bottom
               left corner Oasis montaj frame window.
               
               if the max values are equal or less than the min values
               the window will be mimimized. If any Min values are :def_val:`iMIN`
               or any Max values are :def_val:`iMAX`, the window is maximized.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="X Min"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Y Min"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="X Max"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Y Max")
               ]),

        Method('GetWindowArea_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Get the location of the map window within the frame.",
               notes="""
               The Coordinates are pixels with 0,0 being the bottom
               left corner Oasis montaj frame window.
               
               If the window is minimized, the max values will be
               equal to the min values. If the window is maximized
               X Min and Y min will be :def_val:`iMIN` and X max and Y max
               will be :def_val:`iMAX`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAPTEMPLATE",
                             doc=":class:`EMAPTEMPLATE` object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="X Min returned"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Y Min returned"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="X Max returned"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Y Max returned")
               ])
    ],
    'Virtual': [

        Method('CreateVirtual_EMAPTEMPLATE', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Makes this :class:`EMAPTEMPLATE` object the current active object to the user.",
               return_type="EMAPTEMPLATE",
               return_doc=":class:`EMAPTEMPLATE` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of map to create a virtual EMAMTEMPLATE from")
               ])
    ],
    'Miscellaneous': [

    ]
}

