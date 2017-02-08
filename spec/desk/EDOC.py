from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('EDOC',
                 doc="""
The :class:`EDOC` class provides access to a generic documents views as loaded within
Oasis montaj.
""")


gx_defines = [
    Define('EDOC_PATH',
           doc="Four forms",
           constants=[
               Constant('EDOC_PATH_FULL', value='0', type=Type.INT32_T,
                        doc="d:\\directory\\file.gdb")                        ,
               Constant('EDOC_PATH_DIR', value='1', type=Type.INT32_T,
                        doc="\\directory\\file.gdb")                        ,
               Constant('EDOC_PATH_NAME_EXT', value='2', type=Type.INT32_T,
                        doc="file.gdb")                        ,
               Constant('EDOC_PATH_NAME', value='3', type=Type.INT32_T,
                        doc="file")                        
           ]),

    Define('EDOC_TYPE',
           doc="Avaialable generic document types",
           constants=[
               Constant('EDOC_TYPE_GMS3D', value='0', type=Type.INT32_T,
                        doc=":class:`GMSYS` 3D Model")                        ,
               Constant('EDOC_TYPE_VOXEL', value='1', type=Type.INT32_T,
                        doc="Voxel")                        ,
               Constant('EDOC_TYPE_VOXEL_INVERSION', value='2', type=Type.INT32_T,
                        doc="Voxel Inversion")                        ,
               Constant('EDOC_TYPE_GMS2D', value='3', type=Type.INT32_T,
                        doc=":class:`GMSYS` 2D Model")                        
           ]),

    Define('EDOC_UNLOAD',
           doc="What type of prompt",
           constants=[
               Constant('EDOC_UNLOAD_NO_PROMPT', value='0', type=Type.INT32_T)                        ,
               Constant('EDOC_UNLOAD_PROMPT', value='1', type=Type.INT32_T)                        
           ]),

    Define('EDOC_WINDOW_POSITION',
           doc="Window Positioning Options",
           constants=[
               Constant('EDOC_WINDOW_POSITION_DOCKED', value='0', type=Type.INT32_T)                        ,
               Constant('EDOC_WINDOW_POSITION_FLOATING', value='1', type=Type.INT32_T)                        
           ]),

    Define('EDOC_WINDOW_STATE',
           doc="Window State Options",
           constants=[
               Constant('EDOC_WINDOW_RESTORE', value='0', type=Type.INT32_T)                        ,
               Constant('EDOC_WINDOW_MINIMIZE', value='1', type=Type.INT32_T)                        ,
               Constant('EDOC_WINDOW_MAXIMIZE', value='2', type=Type.INT32_T)                        
           ]),

    Define('GMS3D_MODELTYPE',
           doc="Avaialable model types",
           constants=[
               Constant('GMS3D_MODELTYPE_DEPTH', value='0', type=Type.INT32_T,
                        doc="Depth Model")                        ,
               Constant('GMS3D_MODELTYPE_TIME', value='1', type=Type.INT32_T,
                        doc="Time Model")                        
           ]),

    Define('GMS2D_MODELTYPE',
           doc="Avaialable model types",
           constants=[
               Constant('GMS2D_MODELTYPE_DEPTH', value='0', type=Type.INT32_T,
                        doc="Depth Model")                        ,
               Constant('GMS2D_MODELTYPE_TIME', value='1', type=Type.INT32_T,
                        doc="Time Model")                        
           ])]


gx_methods = {
    'GMSYS 3D Models': [

        Method('CreateNewGMS3D_EDOC', module='None', version='5.0.0',
               availability=Availability.EXTENSION, is_app=True, 
               doc="Creates a new :class:`GMSYS` 3D Model into the workspace, flags as new.",
               return_type="EDOC",
               return_doc="Handle to the newly created edited model.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Document to load."),
                   Parameter('p2', type=Type.INT32_T,
                             doc="X Size"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Y Size"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`GMS3D_MODELTYPE`")
               ])
    ],
    'Miscellaneous': [

        Method('Current_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited Document.",
               return_type="EDOC",
               return_doc=":class:`EDOC` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('CurrentNoActivate_EDOC', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited Document.",
               return_type="EDOC",
               return_doc=":class:`EDOC` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('CurrentIfExists_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method returns the Current Edited Document.",
               return_type="EDOC",
               return_doc="""
               :class:`EDOC` Object to current edited document. If there is no current document,
               the user is not prompted for a document, and 0 is returned.
               """,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('Destroy_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Destroy :class:`EDOC` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDOC",
                             doc=":class:`EDOC` to destroy")
               ]),

        Method('iGetDocumentsLST_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Load the file names of open documents into a :class:`LST`.",
               return_type=Type.INT32_T,
               return_doc="""
               The number of documents loaded into the :class:`LST`.
               The :class:`LST` is cleared first.
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` to load"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDOC_PATH`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('IGetName_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the name of the document object of this :class:`EDOC`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDOC"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Name returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of the String")
               ]),

        Method('iGetWindowState_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Retrieve the current state of the document window",
               return_type=Type.INT32_T,
               return_doc=":def:`EDOC_WINDOW_STATE`",
               parameters = [
                   Parameter('p1', type="EDOC")
               ]),

        Method('iHaveCurrent_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns true if a document is loaded",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('iLoaded_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Returns 1 if a document is loaded .",
               return_type=Type.INT32_T,
               return_doc="1 if document is loaded, 0 otherwise.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="document name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('GetWindowPosition_EDOC', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the map window's position and dock state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDOC"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Window left position"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Window top position"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Window right position"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Window bottom position"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="Window state :def:`EDOC_WINDOW_STATE`"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="Docked or floating :def:`EDOC_WINDOW_POSITION`")
               ]),

        Method('SetWindowPosition_EDOC', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Get the map window's position and dock state",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDOC"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Window left position"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Window top position"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Window right position"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Window bottom position"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Window state :def:`EDOC_WINDOW_STATE`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Docked or floating :def:`EDOC_WINDOW_POSITION`")
               ]),

        Method('iReadOnly_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Checks if a document is currently opened in a read-only mode.",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="EDOC")
               ]),

        Method('Load_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads a list of documents into the workspace",
               return_type="EDOC",
               return_doc="""
               Handle to current edited document, which will be the last
               document in the list.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="list of documents (';' or '|' delimited) to load."),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('LoadNoActivate_EDOC', module='None', version='9.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Loads a list of documents into the workspace",
               return_type="EDOC",
               return_doc="""
               Handle to current edited document, which will be the last
               document in the list.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="list of documents (';' or '|' delimited) to load."),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('MakeCurrent_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Makes this :class:`EDOC` object the current active object to the user.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDOC",
                             doc=":class:`EDOC` to make active")
               ]),

        Method('SetWindowState_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Changes the state of the document window",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDOC"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDOC_WINDOW_STATE`")
               ]),

        Method('Sync_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Syncronize the Metadata of a document that is not currently open",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Document file name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('SyncOpen_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Syncronize the Metadata of a document",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDOC")
               ]),

        Method('UnLoad_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads an edited document.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of document to unload"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('UnLoadAll_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads all opened documents",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('UnLoadDiscard_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads a document in the workspace, discards changes.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of document to unload"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ]),

        Method('UnLoadVerify_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Unloads an edited document, optional prompt to save.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of document to unload"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`EDOC_UNLOAD`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`EDOC_TYPE`")
               ])
    ],
    'Obsolete': [

        Method('GetWindowArea_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Get the location of the document window within the frame.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDOC"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="X Min returned"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Y Min returned"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="X Max returned"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Y Max returned")
               ]),

        Method('SetWindowArea_EDOC', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, is_app=True, 
               doc="Set the location of the document window within the frame.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EDOC"),
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

