from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('EMAP',
                 doc="""
The :class:`EMAP` class provides access to a map as displayed within
Oasis montaj, but (usually) does not change data within the map itself.
It performs functions such as setting the currently displayed area,
or drawing "tracking" lines or boxes on the map (which are not
part of the map itself).
""",
                 notes="""
To obtain access to the map itself, it is recommended practice
to begin with an :class:`EMAP` object, and use the :func:`Lock_EMAP` function to
lock the underlying map to prevent external changes. The returned
:class:`MAP` object (see :class:`MAP`) may then be safely used to make changes to the map itself.

:class:`MAP` Redraw Rules:

1. Redraws only occur at the end of the proccess (GX or SCRIPT) not during.
You can safely call other GX's and the map will not redraw. If you need the
map to redraw immediately use :func:`Redraw_EMAP` instead.

2. If the final GX calls :func:`Cancel_SYS`, the map redraw is not done. If you
need to force a redraw when the user hits cancel use the :func:`Redraw_EMAP` function.

3. You can set the redraw flag to :def_val:`EMAP_REDRAW_YES` or :def_val:`EMAP_REDRAW_NO` at any
time using :func:`SetRedrawFlag_EMAP`. This flag will only be looked at, when
the last call to :func:`UnLock_EMAP` occurs and is ignored on a :func:`Cancel_SYS`.

4. :func:`Redraw_EMAP` only works if the current map is not locked. It will do nothing
if the map is locked.  Issue an :func:`UnLock_EMAP` before using this function.


VIRTUAL :class:`EMAP` SUPPORT

These methods are only available when running in an external application.
They allow the GX to open a :class:`MAP` and then create a Virtual :class:`EMAP` from that
map. The GX can then call :func:`MakeCurrent_EMAP` and set the current :class:`EMAP` so
that code that follows sees this map as the current :class:`MAP`.

Supported methods on Virtual EMAPS are:

:func:`Current_EMAP`
:func:`CurrentNoActivate_EMAP`
:func:`MakeCurrent_EMAP`
:func:`iHaveCurrent_EMAP`
:func:`CurrentIfExists_EMAP`
:func:`Current_MAP`

:func:`Lock_EMAP`
:func:`UnLock_EMAP`
:func:`iIsLocked_EMAP`

:func:`IGetName_EMAP`
:func:`SetRedrawFlag_EMAP`
:func:`Redraw_EMAP`

:func:`iLoaded_EMAP`
:func:`Load_EMAP`
:func:`LoadNoActivate_EMAP`
:func:`UnLoadVerify_EMAP`
:func:`UnLoad_EMAP`

:func:`CreateVirtual_EMAP`
""")


gx_defines = [
    Define('EMAP_FONT',
           doc="Font Types",
           constants=[
               Constant('EMAP_FONT_TT', value='0', type=Type.INT32_T)                        ,
               Constant('EMAP_FONT_GFN', value='1', type=Type.INT32_T)                        
           ]),

    Define('EMAP_PATH',
           doc="Four forms",
           constants=[
               Constant('EMAP_PATH_FULL', value='0', type=Type.INT32_T,
                        doc="d:\\directory\\file.gdb")                        ,
               Constant('EMAP_PATH_DIR', value='1', type=Type.INT32_T,
                        doc="\\directory\\file.gdb")                        ,
               Constant('EMAP_PATH_NAME_EXT', value='2', type=Type.INT32_T,
                        doc="file.gdb")                        ,
               Constant('EMAP_PATH_NAME', value='3', type=Type.INT32_T,
                        doc="file")                        
           ]),

    Define('EMAP_REDRAW',
           doc="Redraw Options",
           constants=[
               Constant('EMAP_REDRAW_NO', value='0', type=Type.INT32_T)                        ,
               Constant('EMAP_REDRAW_YES', value='1', type=Type.INT32_T)                        
           ]),

    Define('EMAP_REMOVE',
           doc="How to handle pending changes in document",
           constants=[
               Constant('EMAP_REMOVE_SAVE', value='0', type=Type.INT32_T)                        ,
               Constant('EMAP_REMOVE_PROMPT', value='1', type=Type.INT32_T)                        ,
               Constant('EMAP_REMOVE_DISCARD', value='2', type=Type.INT32_T)                        
           ]),

    Define('EMAP_TRACK',
           doc="Tracking Options",
           constants=[
               Constant('EMAP_TRACK_ERASE', value='1', type=Type.INT32_T,
                        doc="Erase Object after you return?")                        ,
               Constant('EMAP_TRACK_RMENU', value='2', type=Type.INT32_T,
                        doc="Allow use of right-menu")                        ,
               Constant('EMAP_TRACK_CYCLE', value='4', type=Type.INT32_T,
                        doc="If user holds down left-mouse, will return many times")                        
           ]),

    Define('EMAP_VIEWPORT',
           doc="Tracking Options",
           constants=[
               Constant('EMAP_VIEWPORT_NORMAL', value='0', type=Type.INT32_T,
                        doc="Normal map usage")                        ,
               Constant('EMAP_VIEWPORT_BROWSEZOOM', value='1', type=Type.INT32_T,
                        doc="Zoom Mode")                        ,
               Constant('EMAP_VIEWPORT_BROWSEAOI', value='2', type=Type.INT32_T,
                        doc="Change Area Of Interest Mode")                        
           ]),

    Define('EMAP_WINDOW_POSITION',
           doc="Window Positioning Options",
           constants=[
               Constant('EMAP_WINDOW_POSITION_DOCKED', value='0', type=Type.INT32_T)                        ,
               Constant('EMAP_WINDOW_POSITION_FLOATING', value='1', type=Type.INT32_T)                        
           ]),

    Define('EMAP_WINDOW_STATE',
           doc="Window State Options",
           constants=[
               Constant('EMAP_WINDOW_RESTORE', value='0', type=Type.INT32_T)                        ,
               Constant('EMAP_WINDOW_MINIMIZE', value='1', type=Type.INT32_T)                        ,
               Constant('EMAP_WINDOW_MAXIMIZE', value='2', type=Type.INT32_T)                        
           ]),

    Define('LAYOUT_VIEW_UNITS',
           doc="Base dlayout display units",
           constants=[
               Constant('LAYOUT_VIEW_MM', value='0', type=Type.INT32_T,
                        doc="Millimeters")                        ,
               Constant('LAYOUT_VIEW_CM', value='1', type=Type.INT32_T,
                        doc="Centimeters")                        ,
               Constant('LAYOUT_VIEW_IN', value='2', type=Type.INT32_T,
                        doc="Inches")                        
           ])]


gx_methods = {
    'Drag-and-drop methods': [

        Method('DropMapClipData_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Drop Map clipboard data on this :class:`EMAP`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Handle to Global Clipboard data")
               ]),

        Method('iDragDropEnabled_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Is drag-and-drop enabled for the map?",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object")
               ]),

        Method('SetDragDropEnabled_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set whether drag-and-drop is enabled for the map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Enables/disables drag-and-drop :def:`GEO_BOOL`")
               ])
    ],
    'Drawing': [

        Method('CopyToClip_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Copy entire map to clipboard.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object")
               ]),

        Method('DrawLine_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Draws a line on the current map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X1"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y1"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X2"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y2")
               ]),

        Method('DrawRect_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Draws a rect on the current map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X1"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y1"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X2"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y2")
               ]),

        Method('DrawRect3D_EMAP', module='None', version='9.1.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Plot a square symbol on a section view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X - True X location"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y - True Y location"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z - True Z location"),
                   Parameter('p5', type=Type.INT32_T,
                             doc='Size in pixels ("radius")')
               ]),

        Method('GetDisplayArea_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the area you are currently looking at.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X Min returned"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y Min returned"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="X Max returned"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y Max returned")
               ]),

        Method('GetDisplayAreaRaw_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the area you are currently looking at in raw map units",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X Min returned"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y Min returned"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="X Max returned"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y Max returned")
               ]),

        Method('GetMapLayoutProps_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the base layout view properties.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
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

        Method('GetMapSnap_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get current snapping distance in MM",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Snap value in MM (returned)")
               ]),

        Method('iGetWindowState_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Retrieve the current state of the map window",
               return_type=Type.INT32_T,
               return_doc=":def:`EMAP_WINDOW_STATE`",
               parameters = [
                   Parameter('p1', type="EMAP")
               ]),

        Method('SetDisplayArea_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the area you wish to see.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X Min"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y Min"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X Max"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y Max")
               ]),

        Method('SetMapLayoutProps_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the base layout view properties.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
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

        Method('SetMapSnap_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set current snapping distance in MM",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Snap value in MM")
               ]),

        Method('SetWindowState_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Changes the state of the map window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EMAP_WINDOW_STATE`")
               ])
    ],
    'General': [

        Method('ActivateGroup_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Activates a group and associated tools.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc='"View/Group"')
               ]),

        Method('ActivateView_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Activates a view and associated tools.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc='"View"')
               ]),

        Method('Current_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited map.",
               return_type="EMAP",
               return_doc=":class:`EMAP` Object"),

        Method('CurrentNoActivate_EMAP', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited map.",
               return_type="EMAP",
               return_doc=":class:`EMAP` Object"),

        Method('CurrentIfExists_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited map.",
               return_type="EMAP",
               return_doc="""
               :class:`EMAP` Object to current edited map. If there is no current map,
               the user is not prompted for a map, and 0 is returned.
               """),

        Method('Destroy_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Destroy :class:`EMAP` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` to destroy")
               ]),

        Method('DestroyView_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Removes the view from the workspace.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EMAP_REMOVE`")
               ]),

        Method('FontLST_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="List all Windows and geosoft fonts.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` Object"),
                   Parameter('p2', type="LST",
                             doc="List Object"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`EMAP_FONT`")
               ]),

        Method('iChangeCurrentView_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Change the current working view.",
               return_type=Type.INT32_T,
               return_doc="0 if view set, 1 if view does not exist.",
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="view name")
               ]),

        Method('iCreateGroupSnapshot_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Loads an :class:`LST` with the current view/group names
               existing in a map. Typically used to track group
               changes that are about to occur.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if :class:`LST` filled properly
               1 if not
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object to fill")
               ]),

        Method('IGet3DViewName_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the name of a 3D view if the current view is 3D.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Name returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Size of the String")
               ]),

        Method('IGetCurrentGroup_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the current group name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="returned group name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VIEW_GROUP',
                             doc="length of the name string passed in")
               ]),

        Method('IGetCurrentView_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the current view name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="returned view name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VIEW',
                             doc="length of the name string passed in")
               ]),

        Method('iGetMapsLST_EMAP', module='None', version='5.0.0',
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
                             doc=":def:`EMAP_PATH`")
               ]),

        Method('IGetName_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the name of the map object of this :class:`EMAP`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Name returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the String")
               ]),

        Method('iHaveCurrent_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns whether a current map is loaded",
               return_type=Type.INT32_T,
               return_doc="""
               0 - no current map.
               1 - current map
               """),

        Method('iIGetSpecifiedMapName_EMAP', module='None', version='5.0.0',
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
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="buffer for map name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size")
               ]),

        Method('iIsGrid_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Is the map a grid map?",
               return_type=Type.INT32_T,
               return_doc="1 - Yes, 0 - No",
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object")
               ]),

        Method('ReloadGrid_EMAP', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Reloads a grid document.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Source file name")
               ]),

        Method('iIs3DView_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Is the current view a 3D view.",
               return_type=Type.INT32_T,
               return_doc="1 - Yes, 0 - No",
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object")
               ]),

        Method('iIsLocked_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Is this Map locked",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object")
               ]),

        Method('iLoaded_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns 1 if a map is loaded .",
               return_type=Type.INT32_T,
               return_doc="1 if map is loaded, 0 otherwise.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="map name")
               ]),

        Method('iReadOnly_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Checks if a map is currently opened in a read-only mode.",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="EMAP")
               ]),

        Method('GetWindowPosition_EMAP', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the map window's position and dock state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Window left position"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Window top position"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Window right position"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Window bottom position"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="Window state :def:`EMAP_WINDOW_STATE`"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="Docked or floating :def:`EMAP_WINDOW_POSITION`")
               ]),

        Method('SetWindowPosition_EMAP', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the map window's position and dock state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Window left position"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Window top position"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Window right position"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Window bottom position"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Window state :def:`EMAP_WINDOW_STATE`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Docked or floating :def:`EMAP_WINDOW_POSITION`")
               ]),

        Method('iRealizeGroupSnapshot_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               The :class:`LST` passed in must contain View\\Group strings in
               the Name field only. The function will compare with
               a more current :class:`LST` and zoom the map to the new entry.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 if zoom proceeded ok
               1 if error
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object used for comparison")
               ]),

        Method('iSetCurrentView_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the current working view.",
               return_type=Type.INT32_T,
               return_doc="0 if view set, 1 if view does not exist.",
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="view name")
               ]),

        Method('GetViewIPJ_EMAP', module='None', version='9.1.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get a view's :class:`IPJ`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="view name"),
                   Parameter('p3', type="IPJ",
                             doc=":class:`IPJ` in which to place the view :class:`IPJ`")
               ]),

        Method('Load_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads maps into the editor.",
               return_type="EMAP",
               return_doc=":class:`EMAP` Object to edited map.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="list of maps (';' or '|' delimited) to load.")
               ]),

        Method('LoadNoActivate_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads documents into the workspace",
               return_type="EMAP",
               return_doc="""
               Handle to current edited document, which will be the last
               database in the list if multiple files were provided.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="list of documents (';' or '|' delimited) to load.")
               ]),

        Method('LoadWithView_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load an :class:`EMAP` with the view from a current :class:`EMAP`.",
               return_type="EMAP",
               return_doc="New :class:`EMAP` handle.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Source Map name"),
                   Parameter('p2', type="EMAP",
                             doc=":class:`EMAP` to use as the source view")
               ]),

        Method('Lock_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method locks the Edited map.",
               return_type="MAP",
               return_doc=":class:`EMAP` Object to map associated with edited map.",
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object")
               ]),

        Method('MakeCurrent_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Makes this :class:`EMAP` object the current active object to the user.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` to make active")
               ]),

        Method('Print_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Print the current map to current printer.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="lEntireMap  (0 or 1)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="lScaleToFit 0 - use scale factor 1 - fit to media 2 - fit to roll media"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="lPrintToFile(0 or 1)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="lAllPages   (0 or 1)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="lCentre     (0 or 1)"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="lCopies"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="lFirstPage"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="lLastPage"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="dScaleFactor (2.0 doubles plot size)"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="lOverlapSize (mm)"),
                   Parameter('p12', type=Type.INT32_T,
                             doc="lOffsetX     (mm)"),
                   Parameter('p13', type=Type.INT32_T,
                             doc="lOffsetY     (mm)"),
                   Parameter('p14', type=Type.STRING,
                             doc="szFile       (if lPrintToFile==1)")
               ]),

        Method('Redraw_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Redraw the map immediately.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object")
               ]),

        Method('SelectGroup_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Select a group.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc='"View/Group"')
               ]),

        Method('SetRedrawFlag_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the redraw flag.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EMAP_REDRAW`")
               ]),

        Method('UnLoad_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads a :class:`MAP`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the map to unload")
               ]),

        Method('UnLoadAll_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads all opened maps",
               return_type=Type.VOID),

        Method('UnLoadVerify_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads an edited map, optional prompt to save.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of map to unload"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Prompt? :def:`GEO_BOOL`")
               ]),

        Method('UnLock_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method unlocks the Edited map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object")
               ])
    ],
    'Input': [

        Method('GetCurPoint_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of the currently selected point in view coordinates",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinate in current user units."),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y")
               ]),

        Method('GetCurPointMM_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of the currently selected point in mm on map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinate in map mm"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y")
               ]),

        Method('GetCursor_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of the last known cursor location",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinate in current view user units"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y")
               ]),

        Method('GetCursorMM_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of the last known cursor location in mm on map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinate in map mm"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y")
               ]),

        Method('iDigitize_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Digitise points from the current map and place in a :class:`WA`.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if user digitized some points.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` in which to write digitized points"),
                   Parameter('p3', type="IMG",
                             doc=":class:`IMG` for Z value, or :def_val:`IMG_NULL` for no Z."),
                   Parameter('p4', type=Type.INT32_T,
                             doc="number of significant digits to use, 0 for all."),
                   Parameter('p5', type=Type.STRING,
                             doc="Command line prompt string"),
                   Parameter('p6', type=Type.STRING,
                             doc="New line prefix string"),
                   Parameter('p7', type=Type.STRING,
                             doc="Delimiter"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="0 for no newline 1 for automatic newline at each point")
               ]),

        Method('iDigitize2_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Digitise points from the current map and place in VVs.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if user digitized some points.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type="VV",
                             doc="real X :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="real Y :class:`VV`"),
                   Parameter('p4', type="VV",
                             doc="real Z :class:`VV`"),
                   Parameter('p5', type="IMG",
                             doc=":class:`IMG` for Z value, or :def_val:`IMG_NULL` for no Z."),
                   Parameter('p6', type=Type.STRING,
                             doc="Command line prompt string"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="0 for no newline 1 for automatic newline at each point")
               ]),

        Method('iDigitizePeaks_EMAP', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Digitise points from the current map and place in VVs.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if user digitized some points.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type="VV",
                             doc="real X :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="real Y :class:`VV`"),
                   Parameter('p4', type="VV",
                             doc="real Z :class:`VV`"),
                   Parameter('p5', type="IMG",
                             doc=":class:`IMG` for Z value, or :def_val:`IMG_NULL` for no Z."),
                   Parameter('p6', type=Type.STRING,
                             doc="Command line prompt string"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="0 for no newline 1 for automatic newline at each point")
               ]),

        Method('iDigitizePolygon_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Same as iDigitze2_EMAP, but automatically close polygons.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if user digitized some points.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type="VV",
                             doc="real X :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="real Y :class:`VV`"),
                   Parameter('p4', type="VV",
                             doc="real Z :class:`VV`"),
                   Parameter('p5', type="IMG",
                             doc=":class:`IMG` for Z value, or :def_val:`IMG_NULL` for no Z."),
                   Parameter('p6', type=Type.STRING,
                             doc="Command line prompt string"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="0 for no newline 1 for automatic newline at each point"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="close the polygon if the selected location is within this radius in screen pixels.")
               ]),

        Method('iGetBox_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of a user selected box.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if point returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
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

        Method('iGetBox2_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of a user selected box in a warped view.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if point returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X1 bottom left corner"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y1"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="X2 bottom right corner"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Y2"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="X3 top right corner"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Y3"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="X4 top left corner"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Y4")
               ]),

        Method('iGetGrid_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Position and size a grid on a map.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if line returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Number of elements along primary axis to draw."),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Number of elements along secondary axis to draw."),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Angle of primary axis in degrees"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Grid origin X"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Grid origin Y"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Primary axis length"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Secondary axis length")
               ]),

        Method('iGetLine_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the end points of a line.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if line returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
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

        Method('iGetLineEx_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the end points of a line.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if line returned.
               1 - Right Mouse
               2 - Escape/Cancel
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
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

        Method('iGetLineXYZ_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the end points of a line in X,Y and Z",
               return_type=Type.INT32_T,
               return_doc="""
               0 if line returned.
               1 - Right Mouse
               2 - Escape/Cancel
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X1 in view user units"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y1"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Z1"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="X2"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Y2"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Z2")
               ]),

        Method('iGetPoint_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of a user selected point.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if point returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinate in current view user units."),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y")
               ]),

        Method('iGetPointEx_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of a user selected point.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if point returned.
               1 if user used right mouse and then Done.
               2 if user cancelled.
               3 if capture is lost.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinate in current view user units."),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y")
               ]),

        Method('iGetPoint3D_EMAP', module='None', version='9.1.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of a user selected point.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if point returned.
               1 if user used right mouse and then Done.
               2 if user cancelled.
               3 if capture is lost.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinate in current view user units."),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Z")
               ]),

        Method('iGetPolyLine_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns a polyline.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if line returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type="VV",
                             doc="X"),
                   Parameter('p4', type="VV",
                             doc="Y")
               ]),

        Method('iGetPolyLineXYZ_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns a polyline.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if line returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="user prompt string"),
                   Parameter('p3', type="VV",
                             doc="X"),
                   Parameter('p4', type="VV",
                             doc="Y"),
                   Parameter('p5', type="VV",
                             doc="Z")
               ]),

        Method('iGetRect_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the coordinates of a user selected box starting at a corner.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if point returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
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

        Method('iTrackPoint_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get point without prompt or cursor change with tracking",
               return_type=Type.INT32_T,
               return_doc="""
               0 if point returned.
               1 if user cancelled.
               """,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EMAP_TRACK`"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X coordinate in current view user units."),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y")
               ])
    ],
    'Map Viewport Mode Methods': [

        Method('GetAOIArea_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the area of interest.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X Min returned"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y Min returned"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="X Max returned"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y Max returned")
               ]),

        Method('SetAOIArea_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the area of interest.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X Min"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y Min"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X Max"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y Max")
               ]),

        Method('SetViewportMode_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the viewport mode.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EMAP_VIEWPORT`")
               ])
    ],
    'Tracking Methods': [

        Method('GetSelectedVertices_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the verticies of selected object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` Handle"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV` Handle"),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV` Handle")
               ])
    ],
    'Virtual': [

        Method('CreateVirtual_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Makes this :class:`EMAP` object the current active object to the user.",
               return_type="EMAP",
               return_doc=":class:`EMAP` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of map to create a virtual :class:`EMAP` from")
               ])
    ],
    'External Window': [

        Method('LoadControl_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, no_cpp=True, 
               doc="",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Map filename"),
                   Parameter('p2', type="HWND", is_val=True,
                             doc="Window handle to receive document")
               ]),

        Method('LoadWithViewControl_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, no_cpp=True, 
               doc="",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Map filename"),
                   Parameter('p2', type="EMAP",
                             doc=":class:`EMAP` handle to use as the source view"),
                   Parameter('p3', type="HWND", is_val=True,
                             doc="Window handle to receive document")
               ])
    ],
    'Obsolete': [

        Method('ExportAllInView_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Export the entire Map in view units to an external format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name To Export"),
                   Parameter('p3', type=Type.STRING,
                             doc="View to export coordinates in"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Resolution in view units of one pixel"),
                   Parameter('p5', type=Type.STRING,
                             doc="EMAP_EXPORT_FORMAT"),
                   Parameter('p6', type=Type.STRING,
                             doc="Extended Options String (format specific)")
               ]),

        Method('ExportAllInView2_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Same as above with colour depth set.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name To Export"),
                   Parameter('p3', type=Type.STRING,
                             doc="View to export coordinates in"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Resolution in view units of one pixel"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="EMAP_EXPORT_BITS"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="EMAP_EXPORT_METHOD"),
                   Parameter('p7', type=Type.STRING,
                             doc="EMAP_EXPORT_FORMAT"),
                   Parameter('p8', type=Type.STRING,
                             doc="Extended Options String (format specific)")
               ]),

        Method('ExportAllRaster_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Export the entire Map to an external format without units.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name To Export"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Number of Pixels in X (X or Y should be specified the other )"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Number of Pixels in Y (should be 0 and computed by export)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="EMAP_EXPORT_BITS"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="EMAP_EXPORT_METHOD"),
                   Parameter('p7', type=Type.STRING,
                             doc="EMAP_EXPORT_RASTER_FORMAT"),
                   Parameter('p8', type=Type.STRING,
                             doc="Extended Options String (format specific)")
               ]),

        Method('ExportAreaInView_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Export an area of a Map in view units to an external format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name To Export"),
                   Parameter('p3', type=Type.STRING,
                             doc="View to export coordinates in"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Resolution in view units of one pixel"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Area To Export Min X location in view units"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Area To Export Min Y location in view units"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Area To Export Max X location in view units"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Area To Export Max Y location in view units"),
                   Parameter('p9', type=Type.STRING,
                             doc="EMAP_EXPORT_FORMAT"),
                   Parameter('p10', type=Type.STRING,
                             doc="Extended Options String (format specific)")
               ]),

        Method('ExportAreaInView2_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Same as above with colour depth set.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name To Export"),
                   Parameter('p3', type=Type.STRING,
                             doc="View to export coordinates in"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Resolution in view units of one pixel"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="EMAP_EXPORT_BITS"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="EMAP_EXPORT_METHOD"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Area To Export Min X location in view units"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Area To Export Min Y location in view units"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Area To Export Max X location in view units"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Area To Export Max Y location in view units"),
                   Parameter('p11', type=Type.STRING,
                             doc="EMAP_EXPORT_FORMAT"),
                   Parameter('p12', type=Type.STRING,
                             doc="Extended Options String (format specific)")
               ]),

        Method('ExportAreaRaster_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Export an area of a Map to an external plot format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name To Export"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Area To Export Min X location in mm"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Area To Export Min Y location in mm"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Area To Export Max X location in mm"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Area To Export Max Y location in mm"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Number of Pixels in X (X or Y should be specified the other )"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Number of Pixels in Y (should be 0 and computed by export)"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="EMAP_EXPORT_BITS"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="EMAP_EXPORT_METHOD"),
                   Parameter('p11', type=Type.STRING,
                             doc="EMAP_EXPORT_RASTER_FORMAT"),
                   Parameter('p12', type=Type.STRING,
                             doc="Extended Options String (format specific)")
               ]),

        Method('GetWindowArea_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Get the location of the map window within the frame.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="X Min returned"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Y Min returned"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="X Max returned"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Y Max returned")
               ]),

        Method('SetWindowArea_EMAP', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Set the location of the map window within the frame.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EMAP",
                             doc=":class:`EMAP` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="X Min"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Y Min"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="X Max"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Y Max")
               ])
    ]
}

