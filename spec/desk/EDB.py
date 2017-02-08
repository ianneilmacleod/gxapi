from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('EDB',
                 doc="""
The :class:`EDB` class provides access to a database as displayed within
Oasis montaj, but does not change data within the database itself.
It performs functions such as setting the current line.
""",
                 notes="""
To obtain access to the database itself, it is recommended practice
to begin with an :class:`EDB` object, and use the :func:`Lock_EDB` function to
lock the underlying map to prevent external changes. The returned
:class:`DB` object (see :class:`DB`) may then be safely used to make changes to the map itself.
""")


gx_defines = [
    Define('MAX_PROF_WND',
           is_constant=True,
           is_single_constant=True,
           doc="The following value should be kept synchronized with the value defined in src\\geoguilib\\stdafx.h",
           constants=[
               Constant('MAX_PROF_WND', value='5', type=Type.INT32_T)                        
           ]),

    Define('EDB_PATH',
           doc="Four forms",
           constants=[
               Constant('EDB_PATH_FULL', value='0', type=Type.INT32_T,
                        doc="d:\\directory\\file.gdb")                        ,
               Constant('EDB_PATH_DIR', value='1', type=Type.INT32_T,
                        doc="\\directory\\file.gdb")                        ,
               Constant('EDB_PATH_NAME_EXT', value='2', type=Type.INT32_T,
                        doc="file.gdb")                        ,
               Constant('EDB_PATH_NAME', value='3', type=Type.INT32_T,
                        doc="file")                        
           ]),

    Define('EDB_PROF',
           doc="Profile data",
           constants=[
               Constant('EDB_PROF_I_CHANNEL', value='0', type=Type.INT32_T,
                        doc="DB_SYMB")                        ,
               Constant('EDB_PROF_I_LINE_STYLE', value='1', type=Type.INT32_T,
                        doc="""
                        0 - no line
                        1 - solid
                        2 - long dash
                        3 - short dash
                        """)                        ,
               Constant('EDB_PROF_I_LINE_WEIGHT', value='2', type=Type.INT32_T,
                        doc="""
                        0 - no line
                        1 - normal
                        2 - medium
                        3 - heavy
                        """)                        ,
               Constant('EDB_PROF_I_SYMBOL', value='3', type=Type.INT32_T,
                        doc="""
                        0 - no symbol
                        1 - rectangle
                        2 - circle
                        3 - triangle
                        4 - diamond
                        5 - x
                        6 - +
                        """)                        ,
               Constant('EDB_PROF_I_SYMBOL_WEIGHT', value='4', type=Type.INT32_T,
                        doc="""
                        0 - normal
                        1 - large
                        """)                        ,
               Constant('EDB_PROF_I_COLOR', value='5', type=Type.INT32_T,
                        doc=":class:`MVIEW` Color Value")                        ,
               Constant('EDB_PROF_I_WRAP', value='6', type=Type.INT32_T,
                        doc="0-no, 1-yes")                        ,
               Constant('EDB_PROF_I_BREAK_ON_DUMMY', value='7', type=Type.INT32_T,
                        doc="0-no, 1-yes")                        ,
               Constant('EDB_PROF_I_GRID_LINE', value='8', type=Type.INT32_T,
                        doc="0-no, 1-yes")                        ,
               Constant('EDB_PROF_R_GRID_LINE_INTERVAL', value='9', type=Type.INT32_T,
                        doc="0-no, 1-yes")                        ,
               Constant('EDB_PROF_I_LOG', value='10', type=Type.INT32_T,
                        doc="0-Linear, 1-Log, 2-LogLinear")                        ,
               Constant('EDB_PROF_R_LOG_MINIMUM', value='11', type=Type.INT32_T,
                        doc="Minimum Value")                        ,
               Constant('EDB_PROF_I_SAMESCALE', value='12', type=Type.INT32_T,
                        doc="0-no, 1-yes")                        ,
               Constant('EDB_PROF_I_SOURCELINE', value='13', type=Type.INT32_T,
                        doc="""
                        0 - current line
                        -1 - previous line
                        -2 - next line
                        """)                        ,
               Constant('EDB_PROF_I_SCALEOPTION', value='14', type=Type.INT32_T,
                        doc="""
                        0 - scale to fit for each line
                        1 - fix the range
                        2 - fix the scale, center the range
                        """)                        ,
               Constant('EDB_PROF_I_SAMERANGE', value='15', type=Type.INT32_T,
                        doc="0-no, 1-yes")                        
           ]),

    Define('EDB_PROFILE_SCALE',
           doc="Profile Scale Options",
           constants=[
               Constant('EDB_PROFILE_SCALE_LINEAR', value='0', type=Type.INT32_T)                        ,
               Constant('EDB_PROFILE_SCALE_LOG', value='1', type=Type.INT32_T)                        ,
               Constant('EDB_PROFILE_SCALE_LOGLINEAR', value='2', type=Type.INT32_T)                        
           ]),

    Define('EDB_REMOVE',
           doc="How to handle pending changes in document",
           constants=[
               Constant('EDB_REMOVE_SAVE', value='0', type=Type.INT32_T)                        ,
               Constant('EDB_REMOVE_PROMPT', value='1', type=Type.INT32_T)                        ,
               Constant('EDB_REMOVE_DISCARD', value='2', type=Type.INT32_T)                        
           ]),

    Define('EDB_UNLOAD',
           doc="What type of prompt",
           constants=[
               Constant('EDB_UNLOAD_NO_PROMPT', value='0', type=Type.INT32_T)                        ,
               Constant('EDB_UNLOAD_SINGLE_PROMPT', value='1', type=Type.INT32_T)                        ,
               Constant('EDB_UNLOAD_MULTI_PROMPT', value='2', type=Type.INT32_T,
                        doc="Obsolete")                        
           ]),

    Define('EDB_WINDOW_POSITION',
           doc="Window Positioning Options",
           constants=[
               Constant('EDB_WINDOW_POSITION_DOCKED', value='0', type=Type.INT32_T)                        ,
               Constant('EDB_WINDOW_POSITION_FLOATING', value='1', type=Type.INT32_T)                        
           ]),

    Define('EDB_WINDOW_STATE',
           doc="Window State Options",
           constants=[
               Constant('EDB_WINDOW_RESTORE', value='0', type=Type.INT32_T)                        ,
               Constant('EDB_WINDOW_MINIMIZE', value='1', type=Type.INT32_T)                        ,
               Constant('EDB_WINDOW_MAXIMIZE', value='2', type=Type.INT32_T)                        
           ]),

    Define('EDB_YAXIS_DIRECTION',
           doc="Window State Options",
           constants=[
               Constant('EDB_YAXIS_NORMAL', value='0', type=Type.INT32_T)                        ,
               Constant('EDB_YAXIS_INVERTED', value='1', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('ApplyFormulaInternal_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Apply a formula to selected cells of the
               current line. (Do not use this wrapper if you
               want to apply a formula across multiple lines)
               
               Notes:
               
               The current selection must be on cell(s) of
               a channel or on the a channel header.
               
               If the selection is on cell(s) of a channel,
               the formula is applied to only these cells.
               
               If the selection is on a channel header, the
               formula is applied to every cell in the channel.
               
               The given formula string must be of the form:
               "<NameOfCurrentChannel>=<SomeExpression>;"
               e.g. "x=y+1;"
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc='Formula ("<NameOfCurrentChannel>=<SomeExpression>;")')
               ]),

        Method('Current_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited Database.",
               return_type="EDB",
               return_doc=":class:`EDB` Object"),

        Method('CurrentNoActivate_EDB', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited Database.",
               return_type="EDB",
               return_doc=":class:`EDB` Object"),

        Method('CurrentIfExists_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited Database.",
               return_type="EDB",
               return_doc="""
               :class:`EDB` Object to current edited database. If there is no current database,
               the user is not prompted for a database, and 0 is returned.
               """),

        Method('DelLine0_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Delete Line 0.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('Destroy_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Destroy :class:`EDB` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` to destroy")
               ]),

        Method('DestroyView_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Removes the view from the workspace.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDB_REMOVE`")
               ]),

        Method('GetCurChanSymb_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the currently marked channel symbol.",
               return_type="DB_SYMB",
               return_doc="""
               Currently channel symbol.
               :def_val:`NULLSYMB` if the mark is not in a channel.
               """,
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('GetCurLineSymb_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get current line symbol.",
               return_type="DB_SYMB",
               return_doc="""
               Currently displayed line symbol.
               :def_val:`NULLSYMB` if no line displayed.
               """,
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('GetDisplFidRange_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Return the displayed fiducial start index & number of cells",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="fiducial start"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="number of fiducials")
               ]),

        Method('GetFidRange_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns currently displayed fid range",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="fiducial start"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="fiducial increment"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="number of fiducials")
               ]),

        Method('GetNextLineSymb_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the next line symbol.",
               return_type="DB_SYMB",
               return_doc="""
               The next line symbol of currently displayed line.
               :def_val:`NULLSYMB` if no line displayed.
               """,
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('GetPrevLineSymb_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the previous line symbol.",
               return_type="DB_SYMB",
               return_doc="""
               The previous line symbol of currently displayed line.
               :def_val:`NULLSYMB` if no line displayed.
               """,
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('GetProfileRangeX_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile X range and X channel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="minimum x"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="maximum x"),
                   Parameter('p4', type="var DB_SYMB", is_ref=True,
                             doc="X axis channel, :def_val:`NULLSYMB` if none")
               ]),

        Method('GetProfileRangeY_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile Y range and display option",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="profile number in window (see :func:`iWindowProfiles_EDB` which returns number of profiles in a window)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="minimum y"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="maximum y"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc=":def:`EDB_PROFILE_SCALE`")
               ]),

        Method('GetProfileSplit_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile split for 3 windows.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="split d1 (profile window 0 height / entire profile window height)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="split d2 (profile window 1 height / entire profile window height)")
               ]),

        Method('GetProfileSplit5_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile split for 5 windows.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="split d1 (profile window 0 height / entire profile window height)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="split d2 (profile window 1 height / entire profile window height)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="split d3 (profile window 2 height / entire profile window height)"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="split d4 (profile window 3 height / entire profile window height)")
               ]),

        Method('GetProfileSplitVV_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile window splits.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type="VV",
                             doc="split :class:`VV` (REAL) (profile window heights / entire profile window height)")
               ]),

        Method('GetProfileVerticalGridLines_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile grid vertical line info.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="vertical grid lines?"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="vertical grid interval")
               ]),

        Method('GetProfileWindow_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get profile window size",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="window x size in pixels"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="window y size in pixels")
               ]),

        Method('GotoColumn_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Move the channel marker to a specific column.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="channel column number, 0 is first -1 for first column without data")
               ]),

        Method('GotoElem_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Goto an element in the current line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Element number")
               ]),

        Method('GotoLine_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Goto to a line symbol in the editor.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol to goto to")
               ]),

        Method('Histogram_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Create histogram stats.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type="ST",
                             doc=":class:`ST` handle to update"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="histogram minimum"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="histogram increment"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="number of increments")
               ]),

        Method('iAllChanList_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get a list of the all channels but in the way they are displayed.",
               return_type=Type.INT32_T,
               return_doc="""
               Number of symbols in the list.
               Terminates GX if there was an error.
               """,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` (INT) in which to place the list.")
               ]),

        Method('iChannels_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns number of displayed channels",
               return_type=Type.INT32_T,
               return_doc="x - number of displayed channels",
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('iDispChanList_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get a list of the displayed channel symbols.",
               return_type=Type.INT32_T,
               return_doc="""
               Number of symbols in the list.
               Terminates GX if there was an error.
               """,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` (INT) in which to place the list.")
               ]),

        Method('iDispChanLST_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get a list of the displayed channel names.",
               return_type=Type.INT32_T,
               return_doc="""
               Number of channels in the list.
               Terminates GX if there was an error.
               """,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('iDispClassChanLST_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get a list of the displayed channels in a given channel class.",
               return_type=Type.INT32_T,
               return_doc="""
               Number of channels in the list.
               Terminates GX if there was an error.
               """,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object"),
                   Parameter('p3', type=Type.STRING,
                             doc='class name ("" for all)')
               ]),

        Method('iFindChannelColumn_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Find the column that contains a channel",
               return_type=Type.INT32_T,
               return_doc="""
               Column number that contains a specific channel
               :def_val:`iDUMMY` of channel not loaded
               """,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="channel")
               ]),

        Method('iFindNearest_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               Find the nearest point on the current line based
               on X,Y and Z and their projection.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               x - Nearest point
               -1 - Not available
               """,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X - Modified with true point"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y - Modified with true point"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Z - Modified with true point"),
                   Parameter('p5', type="IPJ",
                             doc="Projection of X,Y,Z")
               ]),

        Method('IGetCurChan_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get current channel name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Where to put the name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Length of the Buffer")
               ]),

        Method('IGetCurFidString_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               This method returns the currently selected value
               at the current fid (if available).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="String returned here"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Size")
               ]),

        Method('IGetCurLine_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get current line name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Where to put the name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Length of the Buffer")
               ]),

        Method('iGetCurMark_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns the current data mark info.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - if data is marked.
               1 - if data is not currently marked.
               """,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="start fiducial"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="end fiducial"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="fiducial increment")
               ]),

        Method('IGetCurrentSelection_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get current selection information.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Database name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Length of the database name"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Name of Selected channel"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Length of the channel name"),
                   Parameter('p6', type=Type.STRING, is_ref=True, size_of_param='6',
                             doc="Selected lines buffer"),
                   Parameter('p7', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Length of the lines buffer"),
                   Parameter('p8', type=Type.STRING, is_ref=True, size_of_param='8',
                             doc="Fiducial range"),
                   Parameter('p9', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Length of the range buffer")
               ]),

        Method('iGetDatabasesLST_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load the file names of open databases into a :class:`LST`.",
               return_type=Type.INT32_T,
               return_doc="""
               The number of documents loaded into the :class:`LST`.
               The :class:`LST` is cleared first.
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` to load"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDB_PATH`")
               ]),

        Method('iGetMarkChanVV_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get channel data for the current mark.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if successful.
               1 if failed, or if entire database is marked.
               """,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` in which to place the data."),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel symbol to retrieve.")
               ]),

        Method('iGetMarkChanVA_EDB', module='None', version='8.2.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get channel data for the current mark.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if successful.
               1 if failed, or if entire database is marked.
               """,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type="VA",
                             doc=":class:`VA` in which to place the data."),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel symbol to retrieve.")
               ]),

        Method('IGetName_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the name of the database object of this :class:`EDB`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Name returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the String")
               ]),

        Method('iGetProfileParm_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get integer profile parameter",
               return_type=Type.INT32_T,
               return_doc="Data Value (See notes)",
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="profile number in window (see :func:`GetProfileRangeY_EDB`)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`EDB_PROF`")
               ]),

        Method('iGetWindowState_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Retrieve the current state of the database window",
               return_type=Type.INT32_T,
               return_doc=":def:`EDB_WINDOW_STATE`",
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('iHaveCurrent_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns true if a database is loaded",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`"),

        Method('iIsLocked_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Is this Database locked",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` object")
               ]),

        Method('iLoaded_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns 1 if a database is loaded .",
               return_type=Type.INT32_T,
               return_doc="1 if database is loaded, 0 otherwise.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="database name")
               ]),

        Method('iProfileOpen_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Return TRUE or FALSE if profile window is open",
               return_type=Type.INT32_T,
               return_doc="""
               TRUE if window is open
               FALSE if window is closed
               """,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number: 0 is the top window 1 is the middle window 2 is the bottom window")
               ]),

        Method('iReadOnly_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Checks if a database is currently opened in a read-only mode.",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('GetWindowPosition_EDB', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the map window's position and dock state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Window left position"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Window top position"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Window right position"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Window bottom position"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="Window state :def:`EDB_WINDOW_STATE`"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="Docked or floating :def:`EDB_WINDOW_POSITION`")
               ]),

        Method('SetWindowPosition_EDB', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the map window's position and dock state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Window left position"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Window top position"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Window right position"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Window bottom position"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Window state :def:`EDB_WINDOW_STATE`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Docked or floating :def:`EDB_WINDOW_POSITION`")
               ]),

        Method('iShowProfileName_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Show a profile in the profile window",
               return_type=Type.INT32_T,
               return_doc="Profile ID if loaded, -1 for error",
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of the channel")
               ]),

        Method('iGetWindowYAxisDirection_EDB', module='None', version='8.3.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the y-axis direction for a window",
               return_type=Type.INT32_T,
               return_doc=":def:`EDB_YAXIS_DIRECTION`",
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)")
               ]),

        Method('iWindowProfiles_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get number of profiles in a window",
               return_type=Type.INT32_T,
               return_doc="Number of profiles in a window",
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)")
               ]),

        Method('LaunchHistogram_EDB', module='geochimera', version='5.0.6',
               availability=Availability.PUBLIC, 
               doc="Launch histogram tool on a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="First chan name")
               ]),

        Method('LaunchScatter_EDB', module='geochimera', version='5.0.6',
               availability=Availability.PUBLIC, 
               doc="Launch scatter tool on a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object")
               ]),

        Method('Load_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads a list of databases into the workspace",
               return_type="EDB",
               return_doc="""
               Handle to current edited database, which will be the last
               database in the list.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="list of databases (';' or '|' delimited) to load.")
               ]),

        Method('LoadNoActivate_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads documents into the workspace",
               return_type="EDB",
               return_doc="""
               Handle to current edited document, which will be the last
               database in the list if multiple files were provided.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="list of documents (';' or '|' delimited) to load.")
               ]),

        Method('LoadAllChans_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load all channels into current database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('LoadChan_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load a channel into current database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="channel name")
               ]),

        Method('LoadNew_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads a database into the workspace, flags as new.",
               return_type="EDB",
               return_doc="Handle to the current edited database.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database to load.")
               ]),

        Method('LoadPass_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads a database into the editor with login and password.",
               return_type="EDB",
               return_doc="Handle to current edited database.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of database to load"),
                   Parameter('p2', type=Type.STRING,
                             doc="Login Name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Password")
               ]),

        Method('LoadWithView_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load an :class:`EDB` with the view from a current :class:`EDB`.",
               return_type="EDB",
               return_doc="New :class:`EDB` handle.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Source :class:`DB` name"),
                   Parameter('p2', type="EDB",
                             doc=":class:`EDB` to use as the source view")
               ]),

        Method('Lock_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method locks the Edited Database.",
               return_type="DB",
               return_doc="Handle to database associated with edited database.",
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('MakeCurrent_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Makes this :class:`EDB` object the current active object to the user.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` to make active")
               ]),

        Method('RemoveProfile_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Remove a profile from the profile window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="profile number in window (see :func:`GetProfileRangeY_EDB`)")
               ]),

        Method('rGetCurFid_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               This method returns the currently selected fiducial if
               the user is selecting a fiducial. If not, it returns
               a dummy.
               """,
               return_type=Type.DOUBLE,
               return_doc="""
               x     - Fiducial
               DUMMY - No Selected Fiducial
               """,
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('rGetProfileParm_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get real profile parameter",
               return_type=Type.DOUBLE,
               return_doc="Real profile parameter",
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="profile number in window (see :func:`GetProfileRangeY_EDB`)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`EDB_PROF`")
               ]),

        Method('rGetSplit_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get split ratio between spreadsheet and profile sections.",
               return_type=Type.DOUBLE,
               return_doc="""
               d = (spreadsheet window height/
               (spreadsheet window height + entire profile window height))
               """,
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('RunChannelMaker_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Run the maker for a single channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.STRING,
                             doc="channel name")
               ]),

        Method('RunChannelMakers_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Recreate channels with makers.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('SetCurLine_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the current line name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="line name")
               ]),

        Method('SetCurLineNoMessage_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set Line but do not send a message.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="line name")
               ]),

        Method('SetCurMark_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set the current mark.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="start fiducial"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="end fiducial")
               ]),

        Method('SetProfileParmI_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set integer profile parameter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="profile number in window (see :func:`GetProfileRangeY_EDB`)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`EDB_PROF`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="setting")
               ]),

        Method('SetProfileParmR_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set real profile parameter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="profile number in window (see :func:`GetProfileRangeY_EDB`)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`EDB_PROF`"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="setting")
               ]),

        Method('SetProfileRangeX_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set profile X range and X channel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="minimum x, :def_val:`rDUMMY` for data minimum"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="maximum x, :def_val:`rDUMMY` for data maximum"),
                   Parameter('p4', type="DB_SYMB",
                             doc="X axis channel, :def_val:`NULLSYMB` to use fids")
               ]),

        Method('SetProfileRangeY_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set profile Y range and display option",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="profile number in window (see :func:`GetProfileRangeY_EDB`)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="minimum y"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="maximum y"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`EDB_PROFILE_SCALE`")
               ]),

        Method('SetProfileSplit_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set profile split for 3 windows.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="split d1 (profile window 0 height / entire profile window height)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="split d2 (profile window 1 height / entire profile window height)")
               ]),

        Method('SetProfileSplit5_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set profile split for 5 windows.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="split d1 (profile window 0 height / entire profile window height)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="split d2 (profile window 1 height / entire profile window height)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="split d3 (profile window 2 height / entire profile window height)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="split d4 (profile window 3 height / entire profile window height)")
               ]),

        Method('SetProfileSplitVV_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set profile splits",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type="VV",
                             doc="split :class:`VV` (REAL) (relative sizes of each profile window)")
               ]),

        Method('SetSplit_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Set split ratio between spreadsheet and profile sections.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="split d (0.0 <= d <= 1.0).")
               ]),

        Method('SetWindowState_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Changes the state of the database window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDB_WINDOW_STATE`")
               ]),

        Method('ShowProfile_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Show a profile in the profile window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="profile window number (0 to :def_val:`MAX_PROF_WND`-1, see :func:`iProfileOpen_EDB`)"),
                   Parameter('p3', type="DB_SYMB",
                             doc="channel symbol")
               ]),

        Method('Statistics_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Add all currently selected data to the :class:`ST`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type="ST",
                             doc=":class:`ST` handle to update")
               ]),

        Method('UnLoad_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads an edited database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of database to unload")
               ]),

        Method('UnLoadAll_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads all opened databases",
               return_type=Type.VOID),

        Method('UnLoadAllChans_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unload all channels into current database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB")
               ]),

        Method('UnLoadChan_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unload a channel into current database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="channel name")
               ]),

        Method('UnLoadDiscard_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads a database in the workspace, discards changes.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of database to unload")
               ]),

        Method('UnLoadVerify_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads an edited database, optional prompt to save.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of database to unload"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDB_UNLOAD`")
               ]),

        Method('UnLock_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method unlocks the Edited Database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB")
               ])
    ],
    'External Window': [

        Method('LoadControl_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, no_cpp=True, 
               doc="",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database filename"),
                   Parameter('p2', type="HWND", is_val=True,
                             doc="Window handle to receive document")
               ]),

        Method('LoadNewControl_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, no_cpp=True, 
               doc="",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database filename"),
                   Parameter('p2', type="HWND", is_val=True,
                             doc="Window handle to receive document")
               ]),

        Method('LoadPassControl_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, no_cpp=True, 
               doc="",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database filename"),
                   Parameter('p2', type=Type.STRING,
                             doc="Login name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Password"),
                   Parameter('p4', type="HWND", is_val=True,
                             doc="Window handle to receive document")
               ]),

        Method('LoadWithViewControl_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, no_gxh=True, no_cpp=True, 
               doc="",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database filename"),
                   Parameter('p2', type="EDB",
                             doc=":class:`EDB` handle to use as the source view"),
                   Parameter('p3', type="HWND", is_val=True,
                             doc="Window handle to receive document")
               ])
    ],
    'Obsolete': [

        Method('NoLoad_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Makes a database the Edited Database without loading it.",
               return_type="EDB",
               return_doc="Handle to current edited database",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='single databases to "not" load')
               ]),

        Method('ReadDataViewBF_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Retrieve view info from the database via a :class:`BF`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line or group symbol"),
                   Parameter('p3', type="BF",
                             doc=":class:`BF` (returned)")
               ]),

        Method('WriteDataViewBF_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Write the View info from a :class:`BF` into the database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB",
                             doc=":class:`EDB` object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line or group symbol"),
                   Parameter('p3', type="BF",
                             doc=":class:`BF` (input)")
               ]),

        Method('SetWindowArea_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Set the location of the database window within the frame.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="X Min"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Y Min"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="X Max"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Y Max")
               ]),

        Method('GetWindowArea_EDB', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Get the location of the database window within the frame.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDB"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="X Min returned"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Y Min returned"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="X Max returned"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Y Max returned")
               ])
    ]
}

