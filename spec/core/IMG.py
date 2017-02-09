from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('IMG',
                 doc="""
                 The :class:`IMG` class performs read and write operations on grid
                 file data. When efficient access along both rows and columns
                 is desired the :class:`PG` class is recommended (see :class:`PG` and :class:`PGU`);
                 the :class:`IMG` is first created, then the :class:`PG` is obtained from
                 the :class:`IMG` using :func:`GetPG_IMG`.
                 """,
                 notes="""
                 The :class:`IMG` methods use the XGD DATs to access grid files in different
                 formats.  The characteristics of a grid can be controlled using
                 decorations on a grid file name.  For example:
                 
                 :func:`CreateNewFile_IMG`(:def_val:`GS_DOUBLE`,1,100,100,"mag.grd");
                 -> creates a new grid file "mag.grd" with all defaults.
                 
                 :func:`CreateNewFile_IMG`(:def_val:`GS_DOUBLE`,1,100,100,"mag.grd(GRD;comp=none)");
                 -> creates a new grid file "mag.grd" with no compression.
                 
                 :func:`CreateNewFile_IMG`(:def_val:`GS_DOUBLE`,1,100,100,"mag.grd(GRD;comp=size;type=short");
                 -> creates a new grid file "mag.grd" compressed for size, numbers
                 stored as 2-byte integers..
                 
                 See :def:`DAT_XGD`.DOC for information about file name decorations available
                 for all :class:`DAT` types.
                 
                 Different grid types support different features.  For example, not all
                 grid types support projection information.  Geosoft will always create
                 a *.gi file that is used to store all such information that we require
                 from a grid.  If the grid does support this information, both the grid
                 and the *.gi file will contain the information.
                 """)


gx_defines = [
    Define('IMG_NULL',
           is_null_handle=True,
           doc="Image Null"),

    Define('IMG_FILE',
           doc="Image open modes",
           constants=[
               Constant('IMG_FILE_READONLY', value='0', type=Type.INT32_T,
                        doc="Reading only")                        ,
               Constant('IMG_FILE_READWRITE', value='2', type=Type.INT32_T,
                        doc="Reading and writting")                        ,
               Constant('IMG_FILE_READORWRITE', value='3', type=Type.INT32_T,
                        doc="""
                        Allows you to open read-only grids to change the
                        projection or location information.  If you can write
                        to the original grid (dat), the changed projection
                        or location information will be passed on to the grid,
                        otherwise changes will only occur in the .gi file.
                        """)                        
           ]),

    Define('IMG_QUERY',
           doc="Information to Query",
           constants=[
               Constant('IMG_QUERY_iWRITE', value='0', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_iPG', value='1', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_iWRITEPG', value='2', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_iIMGTYPE', value='3', type=Type.INT32_T,
                        doc="The element type used to open the :class:`IMG`.")                        ,
               Constant('IMG_QUERY_iDATTYPE', value='4', type=Type.INT32_T,
                        doc="""
                        DATTYPE is the native element type of the :class:`DAT`.
                        Types are:   0 - byte
                        1 - unsigned 16-bit short
                        2 - 16-bit short
                        3 - 32-bit long
                        4 - 32-bit float
                        5 - 64-bit double
                        """)                        ,
               Constant('IMG_QUERY_iRENDER', value='5', type=Type.INT32_T,
                        doc="""
                        Render modes are:    0 - interpolate
                        1 - pixelate
                        2 - colour
                        """)                        ,
               Constant('IMG_QUERY_iKX', value='6', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_iNX', value='7', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_iNY', value='8', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_iNV', value='9', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_iNE', value='10', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_rXO', value='11', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_rYO', value='12', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_rDX', value='13', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_rDY', value='14', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_rROT', value='15', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_rBASE', value='16', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_rMULT', value='17', type=Type.INT32_T)                        ,
               Constant('IMG_QUERY_rCOMPRESSION_RATIO', value='18', type=Type.INT32_T)                        
           ]),

    Define('IMG_RELOCATE',
           doc="Relocation Style",
           constants=[
               Constant('IMG_RELOCATE_FIT', value='0', type=Type.INT32_T,
                        doc="will fit the image to fill the specified area")                        ,
               Constant('IMG_RELOCATE_ASPECT', value='1', type=Type.INT32_T,
                        doc="will maintain aspect ratio")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Average2_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Reduce the dimensions in a 2D pager by a factor of 2",
               notes="""
               This method is useful for reducing the dimensions in a 2D pager by a factor of 2.
               The output pager retains the same origin, but the X and Y spacing is double that of the original. Essentially,
               the process removes all the even-indexed rows and columns, while leaving the locations of all the remaining
               data points in the "odd" rows and columns unchanged.
               
               The output values at the output data locations are created by performing an average of the original data point and
               its valid surrounding data points; what is essentially a 3x3 smoothing filter.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of source Grid"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of output Grid")
               ]),

        Method('Copy_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy IMGs.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="source :class:`IMG`"),
                   Parameter('p2', type="IMG",
                             doc="target :class:`IMG`")
               ]),

        Method('Create_IMG', module='geoengine.core', version='5.0.3',
               availability=Availability.PUBLIC, 
               doc="Creates an :class:`IMG` not tied to a file at all",
               notes="Once destroyed all the data in this :class:`IMG` is lost.",
               return_type="IMG",
               return_doc=":class:`IMG` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Data type :def:`GS_TYPES`"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Grid orientation (KX): 1 (rows in X) -1 (rows in Y)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Grid width"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Grid height")
               ]),

        Method('CreateFile_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates an Image object tied to a grid file.",
               notes="""
               When the :def_val:`GS_DOUBLE` data type is chosen the actual on-disk
               type of the input image will be used instead of :def_val:`GS_DOUBLE`
               if the on-disk values represent colour data as opposed
               to real numbers.
               """,
               return_type="IMG",
               return_doc=":class:`IMG` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Data type, :def:`GS_TYPES` or :def_val:`GS_TYPE_DEFAULT` to use native :class:`DAT` type."),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the Grid to link to"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Grid File Open Mode :def:`IMG_FILE`")
               ]),

        Method('CreateMem_IMG', module='geoengine.core', version='5.0.6',
               availability=Availability.PUBLIC, 
               doc="Creates an :class:`IMG` object that is backed only by memory.",
               notes="Once destroyed all the data is lost. This is temporary.",
               return_type="IMG",
               return_doc=":class:`IMG` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Data type, :def:`GS_TYPES`"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Grid orientation (KX): 1 (rows in X) -1 (rows in Y)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Grid width"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Grid height")
               ]),

        Method('CreateNewFile_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates an output image file using User defined info.",
               notes="""
               Special Note for developers who use this function and
               related functions to output ERMapper image (ERS, ECW) files:
               
               This function internally called ERMapper plugin to create ERS header
               files. To find the location of ERMapper plugin library, a registry setting
               needs to set. The key in the registry is HKEY_LOCAL_MACHINE\\SOFTWARE\\"MyProgram(libversion7.0)"
               and in that key register a string BASE_PATH = D:\\Oasismontaj\\plugins\\er_mapper.
               MyProgram is the name of your application and D:\\Oasismontaj\\plugins\\er_mapper
               is the location of ERMapper library.
               
               It is recommended that this registry key is set during the installation
               of your application.
               """,
               return_type="IMG",
               return_doc=":class:`IMG` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Data type, :def:`GS_TYPES` Cannot be :def_val:`GS_TYPE_DEFAULT`"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Grid orientation (KX): 1 (rows in X) -1 (rows in Y)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Grid width"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Grid height"),
                   Parameter('p5', type=Type.STRING,
                             doc="Name of the Grid to link to")
               ]),

        Method('CreateOutFile_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates an output image file using input image info.",
               notes="""
               When the :def_val:`GS_DOUBLE` data type is chosen the actual on-disk
               type of the input image will be used instead of :def_val:`GS_DOUBLE`
               if the on-disk values represent colour data as opposed
               to real numbers.
               """,
               return_type="IMG",
               return_doc=":class:`IMG` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Data type, :def:`GS_TYPES` or :def_val:`GS_TYPE_DEFAULT`"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the Grid to link to"),
                   Parameter('p3', type="IMG",
                             doc="Input Image for new image creation")
               ]),

        Method('CreateProjected_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Applies a projection to an image.",
               notes="""
               The :class:`IMG` now appears to be in the projected coordinate
               system space.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input image to project"),
                   Parameter('p2', type="IPJ",
                             doc="Projection to apply")
               ]),

        Method('CreateProjected2_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Applies a projection to an image, specify cell size.",
               notes="""
               The :class:`IMG` now appears to be in the projected coordinate
               system space, with the specified cell size. If the cell
               size is :def_val:`rDUMMY` (:def_val:`GS_R8DM`), one is automatically calculated,
               as with :func:`CreateProjected_IMG`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input image to project"),
                   Parameter('p2', type="IPJ",
                             doc="Projection to apply"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Cell size")
               ]),

        Method('CreateProjected3_IMG', module='geoengine.core', version='6.3.1',
               availability=Availability.PUBLIC, 
               doc="Same as :func:`CreateProjected2_IMG`, but set expansion of bounds.",
               notes="""
               The :class:`IMG` now appears to be in the projected coordinate
               system space, with the specified cell size. If the cell
               size is :def_val:`rDUMMY` (:def_val:`GS_R8DM`), one is automatically calculated,
               as with :func:`CreateProjected_IMG`.
               The expansion percent expands the bounds of the projected grid
               in order to allow for the curving of bounding edges. Normally,
               edges are sampled in order to allow for curving, but this
               parameter is set to 1.0 (for 1 percent) in the :func:`CreateProjected_IMG`
               and :func:`CreateProjected2_IMG` wrappers, and will generally create a
               white/dummy border around the new grid. This new method allows
               you to specify the expansion, or turn it off (by setting it to 0).
               If the value is set to :def_val:`rDUMMY`, then expansion is left at 1.0,
               the legacy behaviour.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input image to project"),
                   Parameter('p2', type="IPJ",
                             doc="Projection to apply"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Cell size"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Expansion percent (>=0).")
               ]),

        Method('Destroy_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a table resource.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Image Object to Destroy")
               ]),

        Method('GethPG_IMG', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Get the actual pager of a grid.",
               see_also=":func:`GetPG_IMG` to get just a copy of the grid's pager.",
               return_type="PG",
               return_doc=":class:`PG` Object",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` object")
               ]),

        Method('GetInfo_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Retrieves location information about this image.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Image Object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X element separation"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y element separation"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="X location of first point"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y location of first point"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="grid X axis rotation deg. CCW from reference X")
               ]),

        Method('GetIPJ_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the projection of a grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` object"),
                   Parameter('p2', type="IPJ",
                             doc="Projection of the grid")
               ]),

        Method('GetMETA_IMG', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Get the metadata of a grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` object"),
                   Parameter('p2', type="META",
                             doc="Metadata of the grid")
               ]),

        Method('GetPG_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a copy of the pager of a grid.",
               see_also=":func:`GethPG_IMG` to get the actual pager of the grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` object"),
                   Parameter('p2', type="PG",
                             doc=":class:`PG` object to hold pager of the grid")
               ]),

        Method('GetProjectedCellSize_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns default cell size from projected image.",
               notes="""
               Returns the cell size calculated by CreateProjected_PJIMG, or by
               :func:`CreateProjected2_IMG` when
               :def_val:`GS_R8DM` is entered as the optional cell size. No inheritance
               is actually performed to the input :class:`IMG`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input image to project"),
                   Parameter('p2', type="IPJ",
                             doc="Projection to apply"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Returned cell size")
               ]),

        Method('GetTR_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the trend information from a grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` object"),
                   Parameter('p2', type="TR",
                             doc="Trend information from the grid")
               ]),

        Method('iElementType_IMG', module='geoengine.core', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Returns the element type.",
               return_type=Type.INT32_T,
               return_doc="Element type",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="0 for XGD, 1 for :class:`IMG`")
               ]),

        Method('iEType_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the element type.",
               notes="Same as sElementType_IMG(img,1)",
               return_type=Type.INT32_T,
               return_doc="Element type",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Image Object")
               ]),

        Method('iGetDefITR_IMG', module='geoengine.core', version='5.0.2',
               availability=Availability.PUBLIC, 
               doc="Get default transform, if it exists",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Okay
               1 - No default possible/available
               """,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="image"),
                   Parameter('p2', type="ITR",
                             doc="transform")
               ]),

        Method('iIsColour_IMG', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Is this a Geosoft colour grid?",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` to query on")
               ]),

        Method('iIsValidIMGFile_IMG', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Is this a valid :class:`IMG` file?",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File to check")
               ]),

        Method('iIsValidIMGFileEx_IMG', module='geoengine.core', version='8.0.1',
               availability=Availability.PUBLIC, 
               doc="Is this a valid :class:`IMG` file? Returns error message if it cannot be opened for any reason.",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File to check"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Error message registered if unable to open"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Error message Buffer Size")
               ]),

        Method('iNE_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the # of elements in the optimal KX direction.",
               return_type=Type.INT32_T,
               return_doc="# of elements in the optimal KX direction",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="source :class:`IMG`")
               ]),

        Method('Inherit_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Inherit a projection/new cell size on the :class:`IMG`.",
               notes="""
               If cell size is :def_val:`GS_R8DM`, then "nice" values for the cell
               size of the new projected grid will be determined so that
               the new grid has about the same number of cells as the old.
               If the cell size is specified, the inheritance will always
               work, even if the input :class:`IPJ` is identical to the original
               :class:`IPJ`, and the cell boundaries will be forced to be aligned
               with the new cell size.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Image"),
                   Parameter('p2', type="IPJ",
                             doc="Projection"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Optional cell size")
               ]),

        Method('InheritIMG_IMG', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Make a grids match in size and coordinate system",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` to make match source :class:`IMG`"),
                   Parameter('p2', type="IMG",
                             doc="source :class:`IMG`")
               ]),

        Method('iNV_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the # of vectors in the optimal KX direction.",
               return_type=Type.INT32_T,
               return_doc="# of vectors in the optimal KX direction",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="source :class:`IMG`")
               ]),

        Method('iNX_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the # of X elements.",
               return_type=Type.INT32_T,
               return_doc="# of X elements.",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="source :class:`IMG`")
               ]),

        Method('iNY_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the # of Y elements.",
               return_type=Type.INT32_T,
               return_doc="# of Y elements.",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="source :class:`IMG`")
               ]),

        Method('iQuery_IMG', module='geoengine.core', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Query information about the :class:`IMG`",
               notes="""
               You can call either funtion to retrieve any data,
               int or real.
               """,
               return_type=Type.INT32_T,
               return_doc="Information requested, dummy if unknown or invalid.",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`IMG_QUERY`")
               ]),

        Method('iQueryKX_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Asks the :class:`IMG` for the most efficient way to access the data.",
               return_type=Type.INT32_T,
               return_doc="""
               -1  - by Columns
               0  - Rows or Columns are equally efficient.
               1  - by Rows
               """,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Image Object")
               ]),

        Method('iSetDefITR_IMG', module='geoengine.core', version='5.0.2',
               availability=Availability.PUBLIC, 
               doc="Set default transform",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Okay
               1 - No default possible/available
               """,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="image"),
                   Parameter('p2', type="ITR",
                             doc="transform")
               ]),

        Method('iUserPreferenceToPlotAsColourShadedGrid_IMG', module='geoengine.core', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Returns the global setting.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - User wishes to plot grids as regular (flat) grid
               1 - User wishes to plot grids as colour-shaded grids
               """),

        Method('LoadIMG_IMG', module='geoengine.core', version='5.0.6',
               availability=Availability.PUBLIC, 
               doc="Loads an :class:`IMG` into a master :class:`IMG`.",
               notes="The Cell sizes and projections must be the same.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="master :class:`IMG`"),
                   Parameter('p2', type="IMG",
                             doc=":class:`IMG` to load")
               ]),

        Method('LoadIntoPager_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Load :class:`IMG` data from file into a pager to increase
               access time.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` object")
               ]),

        Method('OptKX_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Force optimal KX as desired.",
               notes="""
               This will force loading an image into a :class:`PG` if it is not already
               accessible in the direction requested.
               
               Subsequent calls to methods that use the optimal KX will use the
               KX set here.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Image Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="KX -1 by column 1 by row")
               ]),

        Method('ReadV_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Read a vector in the optimal KX direction.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Vector to Read"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="begining element # to read (0 is the first)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="# elements to read (0 for whole vector)"),
                   Parameter('p5', type="VV",
                             doc=":class:`VV` handle")
               ]),

        Method('ReadX_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Read a column (constant X)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="X column"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="start Y to read"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="# Y to read (0 for whole vector)"),
                   Parameter('p5', type="VV")
               ]),

        Method('ReadY_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Read a row (constant Y)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Y row"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="start X to read"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="# X to read (0 for whole vector)"),
                   Parameter('p5', type="VV")
               ]),

        Method('RefreshGI_IMG', module='geoengine.core', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Refresh the GI of a grid after it has moved or changed.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="grid name")
               ]),

        Method('Relocate_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Re-locate a grid image.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="image to relocate"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="area X minimum"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="area Y minimum"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="area X maximum"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="area Y maximum"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`IMG_RELOCATE`")
               ]),

        Method('Report_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Writes grid info report to a file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Grid name"),
                   Parameter('p2', type="WA",
                             doc="Text file to write to"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="recalc statistics (0 - no; 1 - yes)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="number of decimals to put in results"),
                   Parameter('p5', type=Type.STRING,
                             doc="Title for report")
               ]),

        Method('ReportCSV_IMG', module='geoengine.core', version='6.4.2',
               availability=Availability.PUBLIC, 
               doc="Writes grid info as a line to a CSV file",
               notes="""
               Appends the stats as a CSV line to the input text file.
               The header line should only be written to a new text file.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Grid name"),
                   Parameter('p2', type="WA",
                             doc="Text file to write to"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="recalc statistics (0 - no; 1 - yes)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="number of decimals to put in results"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Write header line (0 - no; 1 - yes)?")
               ]),

        Method('rGetZ_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Gets the grid value at a point",
               return_type=Type.DOUBLE,
               return_doc="Grid value",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="source :class:`IMG`"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location in the grid projection"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y location in the grid projection")
               ]),

        Method('rQuery_IMG', module='geoengine.core', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Query information about the :class:`IMG`",
               notes="""
               You can call either funtion to retrieve any data,
               int or real.
               """,
               return_type=Type.DOUBLE,
               return_doc="Information requested, dummy if unknown or invalid.",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`IMG_QUERY`")
               ]),

        Method('SetGridUnchanged_IMG', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Mark the grid as unchanged so it will not output lineage",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG")
               ]),

        Method('SetInfo_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets location information about this image.",
               notes="""
               Calls to this function should be made BEFORE calls to :func:`SetIPJ_IMG`,
               as the latter function sets up the bounding rectangle in the metadata.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Image Object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X element separation"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y element separation"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X location of first point"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y location of first point"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="grid X axis rotation deg. CCW from reference X")
               ]),

        Method('SetIPJ_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the projection of a grid.",
               notes="""
               Calls to this function should be made AFTER calls to :func:`SetInfo_IMG`,
               as :func:`SetIPJ_IMG` sets up the bounding rectangle in the metadata.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="source :class:`IMG`"),
                   Parameter('p2', type="IPJ",
                             doc="Projection")
               ]),

        Method('SetMETA_IMG', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Set the metadata of a grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="source :class:`IMG`"),
                   Parameter('p2', type="META",
                             doc="Metadata to add to the grid")
               ]),

        Method('SetPG_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy a pager into the pager of a grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` object"),
                   Parameter('p2', type="PG",
                             doc="Pager object to copy into the pager of the grid")
               ]),

        Method('SetTR_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the trend information to a grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` object"),
                   Parameter('p2', type="TR",
                             doc="Trend information to set for the grid")
               ]),

        Method('Sync_IMG', module='geoengine.core', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Syncronize the Metadata for this Grid",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="grid name")
               ]),

        Method('WriteV_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Write a vector in the optimal KX direction.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="vector to write"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="begining element to write (0 is the first)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="# elements to write (0 for whole vector)"),
                   Parameter('p5', type="VV",
                             doc=":class:`VV` handle")
               ]),

        Method('WriteX_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Write a column (constant X)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="X column"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="start Y to write"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="# Y to write (0 for whole vector)"),
                   Parameter('p5', type="VV")
               ]),

        Method('WriteY_IMG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Write a row (constant Y)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Y row"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="start X to write"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="# X write (0 for whole vector)"),
                   Parameter('p5', type="VV")
               ]),

        Method('SetRealParameter_IMG', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Store a real parameter in an :class:`IMG` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter name (case insensitive)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Parameter value to store")
               ]),

        Method('rGetRealParameter_IMG', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Store a real parameter in an :class:`IMG` object",
               return_type=Type.DOUBLE,
               return_doc="Parameter value, :def_val:`rDUMMY` if not found.",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc=":class:`IMG` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter name (case insensitive)")
               ])
    ],
    'Obsolete': [

        Method('iDiffImage_IMG', module='geoengine.core', version='6.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Compute the Difference of two images",
               return_type=Type.INT32_T,
               return_doc="x - Number of pixels different",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Bitmap 1"),
                   Parameter('p2', type=Type.STRING,
                             doc="Bitmap 2"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output Image")
               ])
    ]
}

