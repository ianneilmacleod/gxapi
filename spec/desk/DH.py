from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DH',
                 doc="""
                 This class is used for importing and interacting with Drill Hole
                 data files. For detailed information on Drill Hole data,
                 see the documentation for Wholeplot.
                 """,
                 notes="""
                 The :class:`DH` class has some defines not used by any functions.
                     :def_val:`DH_DEFINE_PLAN`
                     :def:`DH_DEFINE_SECT`
                 """)


gx_defines = [
    Define('DH_DEFAULT_FILENAMES',
           is_constant=True,
           doc="Default filenames",
           constants=[
               Constant('DH_DEFAULT_ROCKCODE_FILE', value='agso.csv', type=Type.STRING)                        ,
               Constant('DH_DEFAULT_STRUCTURECODE_FILE', value='structcodes.csv', type=Type.STRING)                        
           ]),

    Define('STR_DH_HOLES',
           is_constant=True,
           is_single_constant=True,
           doc="""
           This declares the size of the string used in various
           :class:`DH` GXs to store all the currently selected holes, as input to the two-panel
           selection tool. This should be big enough for 65,000 16-character hole names!
           """,
           constants=[
               Constant('STR_DH_HOLES', value='1048576', type=Type.INT32_T)                        
           ]),

    Define('DH_COMP_CHOICE',
           doc="Composition",
           constants=[
               Constant('DH_COMP_DONE', value='0', type=Type.INT32_T,
                        doc="User is done")                        ,
               Constant('DH_COMP_CANCEL', value='-1', type=Type.INT32_T,
                        doc="User canceled")                        ,
               Constant('DH_COMP_SELECT', value='1', type=Type.INT32_T,
                        doc="User chose to select an interval interactively")                        ,
               Constant('DH_COMP_REFRESH', value='2', type=Type.INT32_T,
                        doc="User chose to refresh")                        
           ]),

    Define('DH_COMPSTDB_HOLSEL',
           doc="Composite Hole Selection",
           constants=[
               Constant('DH_COMPSTDB_HOLSEL_ALL', value='0', type=Type.INT32_T)                        ,
               Constant('DH_COMPSTDB_HOLSEL_SELECTED', value='1', type=Type.INT32_T)                        
           ]),

    Define('DH_COMPSTDB_INTSEL',
           doc="Composite Interval",
           constants=[
               Constant('DH_COMPSTDB_INTSEL_FIXED', value='0', type=Type.INT32_T)                        ,
               Constant('DH_COMPSTDB_INTSEL_LITHOLOGY', value='1', type=Type.INT32_T)                        ,
               Constant('DH_COMPSTDB_INTSEL_BESTFITLITH', value='2', type=Type.INT32_T)                        ,
               Constant('DH_COMPSTDB_INTSEL_INTFILE', value='3', type=Type.INT32_T)                        
           ]),

    Define('DH_DATA',
           doc="What to import",
           constants=[
               Constant('DH_DATA_DIPAZIMUTH', value='0', type=Type.INT32_T)                        ,
               Constant('DH_DATA_EASTNORTH', value='1', type=Type.INT32_T)                        ,
               Constant('DH_DATA_FROMTO', value='2', type=Type.INT32_T)                        ,
               Constant('DH_DATA_POINT', value='3', type=Type.INT32_T)                        ,
               Constant('DH_DATA_COLLAR', value='4', type=Type.INT32_T)                        ,
               Constant('DH_DATA_UNKNOWN', value='100', type=Type.INT32_T,
                        doc="The type is not known")                        
           ]),

    Define('DH_DEFINE_PLAN',
           is_constant=True,
           is_single_constant=True,
           doc="Plans",
           constants=[
               Constant('DH_DEFINE_PLAN', value='1', type=Type.INT32_T)                        
           ]),

    Define('DH_DEFINE_SECT',
           is_constant=True,
           doc="Types of Sections",
           constants=[
               Constant('DH_DEFINE_SECT_NS', value='1', type=Type.INT32_T)                        ,
               Constant('DH_DEFINE_SECT_EW', value='2', type=Type.INT32_T)                        ,
               Constant('DH_DEFINE_SECT_ANGLED', value='3', type=Type.INT32_T)                        
           ]),

    Define('DH_EXP',
           doc="Type of Export",
           constants=[
               Constant('DH_EXP_CSV', value='0', type=Type.INT32_T)                        ,
               Constant('DH_EXP_ASCII', value='1', type=Type.INT32_T)                        ,
               Constant('DH_EXP_ACCESS', value='2', type=Type.INT32_T)                        ,
               Constant('DH_EXP_SHP', value='3', type=Type.INT32_T,
                        doc="Collars as points")                        ,
               Constant('DH_EXP_SURPAC', value='4', type=Type.INT32_T,
                        doc="To Surpace Geological database (special format ACCESS)")                        ,
               Constant('DH_EXP_SHP_TRACES', value='5', type=Type.INT32_T,
                        doc="Hole traces as polylines")                        
           ]),

    Define('DH_HOLES',
           doc="Holes to select",
           constants=[
               Constant('DH_HOLES_ALL', value='0', type=Type.INT32_T)                        ,
               Constant('DH_HOLES_SELECTED', value='1', type=Type.INT32_T)                        
           ]),

    Define('DH_MASK',
           doc="Masks",
           constants=[
               Constant('DH_MASK_APPEND', value='0', type=Type.INT32_T)                        ,
               Constant('DH_MASK_NEW', value='1', type=Type.INT32_T)                        
           ]),

    Define('DH_PLOT',
           doc="Type of Plot",
           constants=[
               Constant('DH_PLOT_PLAN', value='0', type=Type.INT32_T)                        ,
               Constant('DH_PLOT_SECTION', value='1', type=Type.INT32_T)                        ,
               Constant('DH_PLOT_STRIPLOG', value='2', type=Type.INT32_T)                        ,
               Constant('DH_PLOT_HOLE_TRACES', value='3', type=Type.INT32_T)                        ,
               Constant('DH_PLOT_3D', value='4', type=Type.INT32_T)                        ,
               Constant('DH_PLOT_SECTION_STACK', value='5', type=Type.INT32_T)                        ,
               Constant('DH_PLOT_SECTION_FENCE', value='6', type=Type.INT32_T)                        ,
               Constant('DH_PLOT_SECTION_CROOKED', value='7', type=Type.INT32_T)                        
           ]),

    Define('DH_SECT_PAGE',
           doc="Sections",
           constants=[
               Constant('DH_SECT_PAGE_SECTION', value='1', type=Type.INT32_T)                        
           ]),

    Define('DH_SURFACE',
           doc="""
           Surface selection for creation of geological
           top or bottom surfaces.
           """,
           constants=[
               Constant('DH_SURFACE_FIRST_LAYER_FROM', value='0', type=Type.INT32_T)                        ,
               Constant('DH_SURFACE_FIRST_LAYER_TO', value='1', type=Type.INT32_T)                        ,
               Constant('DH_SURFACE_SECOND_LAYER_FROM', value='2', type=Type.INT32_T)                        ,
               Constant('DH_SURFACE_SECOND_LAYER_TO', value='3', type=Type.INT32_T)                        ,
               Constant('DH_SURFACE_LAST_LAYER_FROM', value='4', type=Type.INT32_T)                        ,
               Constant('DH_SURFACE_LAST_LAYER_TO', value='5', type=Type.INT32_T)                        
           ]),

    Define('DIP_CONVENTION',
           doc="Dip convention",
           constants=[
               Constant('DIP_CONVENTION_NEGATIVE', value='-1', type=Type.INT32_T)                        ,
               Constant('DIP_CONVENTION_POSITIVE', value='1', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'ArcGIS Target Functions': [

        Method('iIsESRI_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Running inside ArcGIS?",
               return_type=Type.INT32_T,
               return_doc="""
               0 - if No
               1 - if Yes
               """)
    ],
    'Data processing/conversion methods': [

        Method('CreatChanLST_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Fills a :class:`LST` with available string and numeric channel code values.",
               notes="""
               Channel codes are in the format "[Assay] Au", where the name in
               the square brackets is descriptive part of the project database
               containing the given channel name. The above code might refer to
               the "Au" channel in the "Tutorial_Assay.gdb" database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to fill with channel code values.")
               ]),

        Method('DepthDataLST_DH', module='geodh', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Fills a :class:`LST` with available channel code values from Depth databases.",
               notes="""
               Channel codes are in the format "[Assay] Au", where the name in
               the square brackets is descriptive part of the project database
               containing the given channel name. The above code might refer to
               the "Au" channel in the "Tutorial_Assay.gdb" database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to fill with channel code values.")
               ]),

        Method('FromToDataLST_DH', module='geodh', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Fills a :class:`LST` with available string and numeric channel code values from From-To databases.",
               notes="""
               Channel codes are in the format "[Assay] Au", where the name in
               the square brackets is descriptive part of the project database
               containing the given channel name. The above code might refer to
               the "Au" channel in the "Tutorial_Assay.gdb" database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc='Assay dataset ("" for all)'),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` to fill with channel code values.")
               ]),

        Method('GetGeologyContacts_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Return XYZ locations of top or bottom geological surfaces",
               notes="""
               For the input :class:`LST` of holes, returns XYZ location of top or bottom
               contact with the input geology. Those selected holes which do NOT
               have contacts, return :def_val:`rDUMMY` for the corresponding locations.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` of holes to check"),
                   Parameter('p3', type=Type.STRING,
                             doc="Channel code"),
                   Parameter('p4', type=Type.STRING,
                             doc="Geology item"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DH_SURFACE` Surface selection (top or bottom)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Max gap to skip when compositing (:def_val:`GS_R8DM` for none)"),
                   Parameter('p7', type="VV",
                             doc="X locations of the contact"),
                   Parameter('p8', type="VV",
                             doc="Y locations of the contact"),
                   Parameter('p9', type="VV",
                             doc="Z locations of the contact")
               ]),

        Method('GetOrientedCoreDipDir_DH', module='geodh', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Converted alpha/beta values in oriented cores to dip/dip direction.",
               notes="""
               The input data are the oriented core alpha and beta values, using either
               top or bottom reference. The values for each hole in the :class:`LST` are converted
               to "absolute" dip and dip-direction values, using the resurveyed hole
               orientations at each depth.
               The alpha and beta data must be from the same database, and the output
               dip and dip/dir channels are written to the same database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type="LST",
                             doc="List of holes to process (e.g. from :func:`HoleLST_DH`)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Channel code for input alpha data"),
                   Parameter('p4', type=Type.STRING,
                             doc="Channel code for input beta data"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="1: Top of core reference 0: Bottom of core reference"),
                   Parameter('p6', type=Type.STRING,
                             doc="Channel name for output dip data"),
                   Parameter('p7', type=Type.STRING,
                             doc="Channel name for output dip direction")
               ]),

        Method('GetUniqueChannelItems_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Return a :class:`VV` with unique items in a channel.",
               notes="Finds and sorts all the unique non-dummy items for the selected channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Channel code"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Selected holes (1), All holes (0)"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` filled with items (converted to this :class:`VV` type)")
               ]),

        Method('GetUniqueChannelItemsFromCollar_DH', module='geodh', version='7.3.0',
               availability=Availability.EXTENSION, 
               doc="Return a :class:`VV` with unique items in a channel.",
               notes="Finds and sorts all the unique non-dummy items for the selected channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Channel"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Selected holes (1), All holes (0)"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` filled with items (converted to this :class:`VV` type)")
               ]),

        Method('iChanType_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Return the data type for a channel code.",
               notes="Finds and sorts all the unique non-dummy items for the selected channel.",
               return_type=Type.INT32_T,
               return_doc="Channel data type",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Channel code")
               ]),

        Method('iFindHoleIntersection_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Return XYZ locations of the intersection of a hole with a DEM grid.",
               notes="""
               Input the hole index and an :class:`IMG` object. Returns XYZ location
               of the hole intersection with the DEM. Interpolation inside the DEM
               uses the native :class:`IMG` interp method. If no intersection is found the
               returned XYZ locations are :def_val:`rDUMMY`.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               1 if intersection found
               0 if no intersection found
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Hole index"),
                   Parameter('p3', type="IMG",
                             doc="DEM Grid"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Returned X location"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Returned Y location"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Returned Z location")
               ]),

        Method('IGetChanCodeInfo_DH', module='geodh', version='7.3.0',
               availability=Availability.EXTENSION, 
               doc="Return the assay database index and channel name from a channel code string.",
               notes='The input channel code is in the form "[Assay] channel"',
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.STRING,
                             doc='Input channel code "[Assay] channel"'),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Returned assay database index"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="channel name"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Buffer size for channel name")
               ]),

        Method('iGridIntersection_DH', module='geodh', version='7.3.0',
               availability=Availability.EXTENSION, 
               doc="Algorithm to determine the intersection of a straight hole with a surface (DEM) grid.",
               notes="""
               Given a point on the hole and the straight hole dip and azimuth,
               ocate (an) intersection point with the input DEM grid.
               """,
               return_type=Type.INT32_T,
               return_doc="1 if an intersection is found, 0 if not.",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Input location on hole X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Input location on hole Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Input location on hole Z"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Dip (positive up) in degrees"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Azimuth in degrees"),
                   Parameter('p7', type=Type.STRING,
                             doc="DEM grid"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="returned intersection point X"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="returned intersection point Y"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="returned intersection point Z")
               ]),

        Method('LithoGrid3D_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Create a lithology voxel grid with lith codes mapped to single values.",
               notes="""
               Values in the input channel are assigned the index of the corresponding
               item found in the input :class:`TPAT`.
               The compositing gap refers to the size of gaps in the data (either
               a blank lithology or missing from-to interval) which will be ignored
               when compositing lithologies into contiguous from-to intervals.
               The non-contact radius is used to dummy out the level grids around holes
               where the gridded lithology is not found. If not specified (dummy) then
               half the distance to the nearest contacting hole is used.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Lithology channel code"),
                   Parameter('p3', type="TPAT",
                             doc="Codes, colours etc."),
                   Parameter('p4', type=Type.STRING,
                             doc="Name of :class:`VOX` Persistent Storage file"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Cell Size (:def_val:`GS_R8DM` for automatic calculation)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Max gap to skip when compositing (:def_val:`GS_R8DM` for none)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Non-contact radius."),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Gridding type (0: Rangrid, 1: TinGrid)"),
                   Parameter('p9', type="REG",
                             doc="Rangrid control :class:`REG` (see :class:`RGRD` class for parameters)"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Retain top/bottom grids?")
               ]),

        Method('NumericChanLST_DH', module='geodh', version='7.2.0',
               availability=Availability.EXTENSION, 
               doc="Fills a :class:`LST` with available numeric channel code values.",
               notes="""
               Channel codes are in the format "[Assay] Au", where the name in
               the square brackets is descriptive part of the project database
               containing the given channel name. The above code might refer to
               the "Au" channel in the "Tutorial_Assay.gdb" database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to fill with channel code values.")
               ]),

        Method('NumericFromToDataLST_DH', module='geodh', version='7.2.0',
               availability=Availability.EXTENSION, 
               doc="Fills a :class:`LST` with available numeric channel code values from From-To databases..",
               notes="""
               Channel codes are in the format "[Assay] Au", where the name in
               the square brackets is descriptive part of the project database
               containing the given channel name. The above code might refer to
               the "Au" channel in the "Tutorial_Assay.gdb" database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc='Assay dataset ("" for all)'),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` to fill with channel code values.")
               ]),

        Method('PunchGridHoles_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Dummy out locations in a grid around non-contact holes.",
               notes="""
               Grid is dummied out to the blanking distance around holes where
               the input Z value is dummy. If a contacting hole is closer then
               twice the blanking distance, the blanking distance is reduced
               accordingly. Distances are measured horizontally (e.g. Z is ignored).
               If the blanking distance is zero or dummy, the distance is
               automatically set to half the distance to the closest hole intersection.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type="IMG",
                             doc="DEM grid"),
                   Parameter('p3', type="VV",
                             doc="X locations of the contacts"),
                   Parameter('p4', type="VV",
                             doc="Y locations of the contacts"),
                   Parameter('p5', type="VV",
                             doc="Z locations of the contacts"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Blanking distance")
               ]),

        Method('StringChanLST_DH', module='geodh', version='7.2.0',
               availability=Availability.EXTENSION, 
               doc="Fills a :class:`LST` with available string channel code values.",
               notes="""
               Channel codes are in the format "[Assay] Au", where the name in
               the square brackets is descriptive part of the project database
               containing the given channel name. The above code might refer to
               the "Au" channel in the "Tutorial_Assay.gdb" database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to fill with channel code values.")
               ]),

        Method('StringFromToDataLST_DH', module='geodh', version='7.2.0',
               availability=Availability.EXTENSION, 
               doc="Fills a :class:`LST` with available string-type channel code values from From-To databases.",
               notes="""
               Channel codes are in the format "[Geology] Lithology", where the name in
               the square brackets is descriptive part of the project database
               containing the given channel name. The above code might refer to
               the "Lithology" channel in the "Tutorial_Geology.gdb" database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc='Assay dataset ("" for all)'),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` to fill with channel code values.")
               ])
    ],
    'Miscellaneous': [

        Method('_hAssayDB_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Database for an assay data set.",
               notes="Works for both single and multiple :class:`DB` Wholeplots.",
               return_type="DB",
               return_doc="""
               x - :class:`DB`
               :def_val:`DB_NULL` if no assay data (no error registered)
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="hDH object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Assay dataset number")
               ]),

        Method('_hAssaySymb_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Line/Group symbol for a specific assay data set hole.",
               notes="Works for both single and multiple :class:`DB` Wholeplots.",
               return_type="DB_SYMB",
               return_doc="""
               x - DB_SYMB
               :def_val:`NULLSYMB` if no survey data for this hole (no error registered)
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="hDH object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Assay dataset number"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="hole index number")
               ]),

        Method('_hCollarDB_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Database for the collar table.",
               notes="Works for both single and multiple :class:`DB` Wholeplots.",
               return_type="DB",
               return_doc="""
               x - :class:`DB`
               :def_val:`DB_NULL` if no collar table (no error registered)
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="hDH object")
               ]),

        Method('_hCollarSymb_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Line/Group symbol for the collar table.",
               notes="Works for both single and multiple :class:`DB` Wholeplots.",
               return_type="DB_SYMB",
               return_doc="""
               x - DB_SYMB
               :def_val:`NULLSYMB` if no collar table (no error registered)
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="hDH object")
               ]),

        Method('_hDipAzSurveyDB_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Database for the Dip-Azimuth survey data",
               notes="Works for both single and multiple :class:`DB` Wholeplots.",
               return_type="DB",
               return_doc="""
               x - :class:`DB`
               :def_val:`DB_NULL` if no dip-azimuth survey data (no error registered)
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object")
               ]),

        Method('_hDipAzSurveySymb_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Line/Group symbol for a specific hole Dip-Azimuth survey.",
               notes="Works for both single and multiple :class:`DB` Wholeplots.",
               return_type="DB_SYMB",
               return_doc="""
               x - DB_SYMB
               :def_val:`NULLSYMB` if no Dip-Azimuth survey data for this hole (no error registered)
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="hDH object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="hole index number")
               ]),

        Method('_hENSurveyDB_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Database for the East-North survey data",
               notes="Works for both single and multiple :class:`DB` Wholeplots.",
               return_type="DB",
               return_doc="""
               x - :class:`DB`
               :def_val:`DB_NULL` if no East-North survey data (no error registered)
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object")
               ]),

        Method('_hENSurveySymb_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Line/Group symbol for a specific hole East-North survey.",
               notes="Works for both single and multiple :class:`DB` Wholeplots.",
               return_type="DB_SYMB",
               return_doc="""
               x - DB_SYMB
               :def_val:`NULLSYMB` if no EN survey data for this hole (no error registered)
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="hDH object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="hole index number")
               ]),

        Method('AddSurveyTable_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Add a survey table for a new hole.",
               notes="""
               The information is created from the collar table info.
               If the survey info already exists, does nothing.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Hole index")
               ]),

        Method('AssayHoleLST_DH', module='geodh', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="Populate an :class:`LST` with holes in an assay database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="index of the assay database"),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` handle")
               ]),

        Method('AssayLST_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Return the :class:`LST` of from-to and point assay datasets",
               notes="""
               Assay dataset name is given as :def_val:`LST_ITEM_NAME`
               Assay dataset number is given as :def_val:`LST_ITEM_VALUE`
               Returns an empty :class:`LST` if no datasets.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to be populated")
               ]),

        Method('AutoSelectHoles_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Use automatic hole selection based on slice.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Turn on (TRUE) or off (FALSE)")
               ]),

        Method('Clean_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Delete extraneous holes from project databases.",
               notes="""
               Removes from Project databases any lines not connected to
               a line found in the collar table list.
               If all the database lines would be removed, the database is
               simply deleted.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle")
               ]),

        Method('CompositeDB_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Make a composite database",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type="DB",
                             doc="Input assay :class:`DB` object"),
                   Parameter('p3', type="DB",
                             doc="output composite :class:`DB` object"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DH_COMPSTDB_HOLSEL`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DH_COMPSTDB_INTSEL`"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="fixed interval length"),
                   Parameter('p7', type=Type.STRING,
                             doc="name of lithology cannel"),
                   Parameter('p8', type=Type.STRING,
                             doc="name of interval file"),
                   Parameter('p9', type=Type.STRING,
                             doc="name of Weight channel"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="dRej1Val for intervals short than, (:def_val:`GS_R8DM` for no action)"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="dRej2Val for intervals gap greater than, (:def_val:`GS_R8DM` for no action)"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="dRej3Val for Rej3Ch with Rej3Op, (:def_val:`GS_R8DM` for no action)"),
                   Parameter('p13', type=Type.INT32_T,
                             doc="dRej3Op: 0: >, 1: >=, 2: <, 3: <="),
                   Parameter('p14', type=Type.STRING,
                             doc="name of Rej3Ch channel")
               ]),

        Method('ComputeHoleXYZ_DH', module='geodh', version='7.3.0',
               availability=Availability.EXTENSION, 
               doc="Computes XYZ for survey and assay data for a single hole.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Hole index")
               ]),

        Method('ComputeSelExtent_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Computes the extents for selected holes.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="East Min"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="East Max"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="North Min"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="North Max"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Elev Min"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Elev Max")
               ]),

        Method('ComputeXYZ_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Computes XYZ for survey and assay data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle")
               ]),

        Method('ConvertOldLineNames_DH', module='geodh', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc='Convert old "DD001.Assay" type lines to "DD001"',
               notes="""
               The input :class:`LST` must be filled using a function like :func:`SymbLST_DB`, which
               puts the name and symbol into the :class:`LST` items.
               Any names with a period are truncated at the period, and
               the line name in the database is changed to the new name
               (just the hole name).
               The :class:`LST` is modified to have the new names.
               A value is put into the :class:`DB` :class:`REG` "DH_CONVERTED_NAMES" parameter so
               this process is done only once on a database.
               
               DO NOT use on old-style single-database Wholeplot projects.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc=":class:`DH` object"),
                   Parameter('p2', type="LST",
                             doc="Names to convert (call :func:`SymbLST_DB`).")
               ]),

        Method('Create_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create :class:`DH`.",
               return_type="DH",
               return_doc=":class:`DH` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of current database")
               ]),

        Method('CreateDefaultJob_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Create a default job from scratch.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object."),
                   Parameter('p2', type=Type.STRING,
                             doc="File name of the INI file to create (forces correct suffix)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DH_PLOT`")
               ]),

        Method('CreateExternal_DH', module='geodh', version='5.1.6',
               availability=Availability.EXTENSION, 
               doc="Create a :class:`DH` from an external process (no montaj running).",
               notes="""
               The regular :func:`Create_DH` assumes a workspace is open and creates
               the project from the databases which are currently loaded.
               This function instead creates the project from all projects
               in the input databases's directory.
               """,
               return_type="DH",
               return_doc=":class:`DH` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of example project database")
               ]),

        Method('Current_DH', module='geodh', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Creates a drill project from current environment.",
               notes="""
               If no :class:`DH` database is open the Open :class:`DH` Project :class:`GUI` will be displayed which may be
               cancelled by the user in which case the GX will terminate with cancel.
               """,
               return_type="DH",
               return_doc=":class:`DH` Object"),

        Method('DatamineToCSV_DH', module='geodh', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="Convert a Datamine drillhole file to CSV files ready for import.",
               notes="""
               Creates three CSV files and the accompanying template files
               ready for batch ASCII import into a drill project.
                  Project_Collar.csv, .i3
                  Project_Survey.csv, .i3
                  Project_Assay.csv,  .i3
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Datamine database file to import (*.dm)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Drillhole project name")
               ]),

        Method('DeleteHoles_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Delete a list of holes from the project.",
               notes="""
               Removes all lines in the input :class:`LST` from :class:`DH` project databases.
               If all the database lines would be removed, the database is
               simply deleted.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` of holes to delete")
               ]),

        Method('Destroy_DH', module='geodh', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`DH` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle")
               ]),

        Method('Export_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Exports a Drill Hole database to an external file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="File name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DH_EXP`")
               ]),

        Method('ExportGeodatabaseLST_DH', module='geodh', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Exports whole or part of a Drill Hole database to an ArcGIS Geodatabase as feature class(es).",
               notes="""
               A table with metadata about the created feature classes will be written to the Geodatabase. This table will have the same
               name with the postfix "_Metadata" attached
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="LST",
                             doc="Hole Names in the Name and Value parts of the :class:`LST`"),
                   Parameter('p3', type=Type.STRING,
                             doc="File name (.pdb folder for File Geodatabase or .sde connector for SDE)"),
                   Parameter('p4', type=Type.STRING,
                             doc="String to prefix dataset names with"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='5',
                             doc="Feature class name to export (pass empty for all or name of table, will contain the name of the output dataset for if a rename occurs)"),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Feature class name string size"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL` Overwrite existing feature classes? Pass :def_val:`GS_FALSE` to create copies.")
               ]),

        Method('ExportLAS_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Exports a Drill Hole database to a LAS v2 file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Assay database index"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Hole index"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Interval for output"),
                   Parameter('p5', type=Type.STRING,
                             doc="File name")
               ]),

        Method('ExportLST_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Exports a :class:`LST` of holes in a Drill Hole database to an external file.",
               notes="Use functions like :func:`SelectedLineLST_DB` to construct the :class:`LST`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="LST",
                             doc="Hole Names in the Name and Value parts of the :class:`LST`"),
                   Parameter('p3', type=Type.STRING,
                             doc="File name"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DH_EXP`")
               ]),

        Method('FlushSelect_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Flush all selections to database selection engine.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="Database")
               ]),

        Method('GetDatabasesVV_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Get the names of the project databases in a :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` of type -:def_val:`STR_FILE`")
               ]),

        Method('GetDatabasesSortedVV_DH', module='geodh', version='8.2.0',
               availability=Availability.EXTENSION, 
               doc="Get the names of the project databases in a :class:`VV`, same as :func:`GetDatabasesVV_DH` but the list is sorted alphabetically.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` of type -:def_val:`STR_FILE`")
               ]),

        Method('GetDataType_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Get the type of data in a Wholeplot database.",
               notes="Returns :def_val:`DH_DATA_UNKNOWN` if it can't determine the type.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` Handle"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc=":def:`DH_DATA`")
               ]),

        Method('GetDefaultSection_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Computes default section azimuths, extents for selected holes.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="azimuth of section (returned)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="corner X (Easting) of section (returned)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="corner Y (Northing) of section (returned)"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="section length (returned)"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="section width (returned)")
               ]),

        Method('GetHoleGroup_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Get the Group symbol for this hole/table combination.",
               return_type="DB_SYMB",
               return_doc="Hole Symbol",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Hole index"),
                   Parameter('p3', type=Type.STRING,
                             doc="Table Name")
               ]),

        Method('GetHoleSurvey_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Get the Survey information of a Hole.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Hole index"),
                   Parameter('p3', type="VV",
                             doc="X"),
                   Parameter('p4', type="VV",
                             doc="Y"),
                   Parameter('p5', type="VV",
                             doc="Z"),
                   Parameter('p6', type="VV",
                             doc="Depth")
               ]),

        Method('GetIPJ_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Get the project :class:`IPJ`.",
               notes="""
               The projection for the project is the projection stored
               in the DH_EAST channel in the collar table.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` Handle")
               ]),

        Method('GetMapNamesVV_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Get plotted map names.",
               notes="""
               This will return the currently plotted map name(s)
               in a :class:`VV`. This should only be called after a call
               to :func:`Wholeplot_DH`. The :class:`VV` size is set to the number
               of maps created.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type="VV",
                             doc="returned map names (string type :class:`VV`)")
               ]),

        Method('GetMap_DH', module='geodh', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="Get a plotting map",
               return_type="MAP",
               return_doc=":class:`MAP` Object",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Map Index")
               ]),

        Method('GetNumMaps_DH', module='geodh', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="Get the number plotting maps",
               return_type=Type.INT32_T,
               return_doc="Number of plotting maps",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle")
               ]),

        Method('GetREG_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Get the :class:`REG` Object used in this project.",
               return_type="REG",
               return_doc=":class:`REG` Object",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle")
               ]),

        Method('GetSelectedHolesVV_DH', module='geodh', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Populate a :class:`VV` with the indices of all selected holes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="VV",
                             doc="Returned hole indices (must be type INT)")
               ]),

        Method('GetTableDefaultChanLST_DH', module='geodh', version='7.3.0',
               availability=Availability.EXTENSION, 
               doc="Return list of default channels by collar/assay/survey table type.",
               notes="""
               Fills a :class:`LST` with the default channel names created according to
               type (Collar, Survey, Assay). Value is in the :def_val:`LST_ITEM_NAME` part.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DH_DATA`")
               ]),

        Method('HoleLST_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Populate an :class:`LST` with the list of the selected holes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` handle")
               ]),

        Method('HoleLST2_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Populate an :class:`LST` with the list of all the holes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` handle")
               ]),

        Method('iAddHole_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Add a hole and return it's index.",
               return_type=Type.INT32_T,
               return_doc="x  - Hole index",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of hole")
               ]),

        Method('iCleanWillDeleteDB_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc='See if "cleaning" will delete project databases.',
               return_type=Type.INT32_T,
               return_doc="""
               1 if calling :func:`Clean_DH` will remove all "lines" from
                   one of the :class:`DH` project databases.
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle")
               ]),

        Method('iCompositingToolGUI_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Annotate a strip log map using the compositing tool.",
               notes="If any of the input X or Y values are dummies the tool uses default values.",
               return_type=Type.INT32_T,
               return_doc=":def:`DH_COMP_CHOICE`",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="MAP",
                             doc="Current strip log map"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location on map of selected strip"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y End of hole interval in view coords"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y Other end of hole interval in view coords")
               ]),

        Method('ICreateCollarTable_DH', module='geodh', version='5.1.6',
               availability=Availability.EXTENSION, 
               doc="Create a collar table :class:`DB` with channels set up.",
               notes="""
               The database name will be of the form
               
               "d:\\directory\\Project_Collar.gdb"
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Project name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Number of channels"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Collar table name (returned)"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for collar table name")
               ]),

        Method('ICreateCollarTableDir_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Create a collar table in the specified directory.",
               notes="""
               The database name will be of the form
               
               "d:\\directory\\Project_Collar.gdb"
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Project name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Directory to create project in"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Number of channels"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Collar table name (returned)"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for collar table name")
               ]),

        Method('iDeleteWillDeleteDB_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="See if deleting holes will delete project databases.",
               return_type=Type.INT32_T,
               return_doc="""
               1 if deleting the :class:`LST` of holes will remove all "lines" from
               one of the :class:`DH` project databases.
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` of holes to delete")
               ]),

        Method('iFindHole_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Find a hole and return it's index.",
               return_type=Type.INT32_T,
               return_doc="""
               x  - Hole index
               -1 - Not found
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of hole")
               ]),

        Method('IGetCollarTableDB_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Get the name of the database containing the collar table.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="returned file name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="buffer size for the file name")
               ]),

        Method('IGetInfo_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Get Collar Information.",
               notes="""
               If the DH_ELEV channel is requested it will also
               search for the DH_RL channel, which is the new
               name for the collar elevation.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="hole index"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of information"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="buffer to place information"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of buffer")
               ]),

        Method('IGetProjectName_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Get the Wholeplot project name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="returned string"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="buffer size for the project name")
               ]),

        Method('IGetSectionID_DH', module='geodh', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Create a section ID based on its location",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Section Azimuth"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Section Easting"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Section Northing"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Section ID"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Section ID size")
               ]),

        Method('iGetTemplateBlob_DH', module='geodh', version='6.0.0',
               availability=Availability.EXTENSION, 
               doc="Retrieve the import template from the database.",
               notes="""
               The template can be retrieved in order to refresh the
               database with a call to the DHIMPORT.GX.
               
               The import types correspond to the DHIMPORT.IMPTYPE variable:
               0: ASCII, 1: Database/XLS, 2: ODBC
               
               If no template blob exists, templ
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0: No template stored in the database
               1: Template retrieved and written to a file.
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc=":class:`DB` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of template file to extract to."),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="The stored import template type :def:`DH_DATA`")
               ]),

        Method('IGetTemplateInfo_DH', module='geodh', version='6.0.0',
               availability=Availability.EXTENSION, 
               doc="Retrieve the file, :class:`DH` Table name and type from an import template.",
               notes="""
               As of version 6.0, the import templates (*.i3, *.i4) produced
               by the Wholeplot import wizards contain the following lines:
               
                FILE assay.txt  (except for ODBC)
                DRILLTYPE 3
                DRILLTABLE Assay
               
               The FILE is normally the input file name, except for ODBC, where it
               is not defined.
               The DRILLTYPE is one of DH_DATA_XXX, and the DRILLTABLE
               is the name of the Wholeplot database table; e.g. Project_Assay.gdb
               in the above case. The DRILLTABLE is only included in the template
               for :def_val:`DH_DATA_FROMTO` and :def_val:`DH_DATA_POINT`, but this function will
               return the appropriate table names (e.g. Collar, Survey, ENSurvey)
               for the other types.
               If the DRILLTYPE is NOT found in the template, a value of
               :def_val:`DH_DATA_UNKNOWN` is returned for the data type; likely an indication that this
               is not a new-style template produced by Wholeplot.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Template name"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc=":def:`DH_DATA`"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="File name (blank for ODBC, or undefined)."),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="File name buffer size"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='5',
                             doc="Table name (blank for :def_val:`DH_DATA_UNKNOWN`, or undefined)."),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Table name buffer size")
               ]),

        Method('IGetTemplateInfoEx_DH', module='geodh', version='7.3.0',
               availability=Availability.EXTENSION, 
               doc="Retrieve the file, :class:`DH` Table name, type and channel list from an import template.",
               notes="""
               As of version 6.0, the import templates (*.i3, *.i4) produced
               by the Wholeplot import wizards contain the following lines:
               
                FILE assay.txt  (except for ODBC)
                DRILLTYPE 3
                DRILLTABLE Assay
               
               The FILE is normally the input file name, except for ODBC, where it
               is not defined.
               The DRILLTYPE is one of DH_DATA_XXX, and the DRILLTABLE
               is the name of the Wholeplot database table; e.g. Project_Assay.gdb
               in the above case. The DRILLTABLE is only included in the template
               for :def_val:`DH_DATA_FROMTO` and :def_val:`DH_DATA_POINT`, but this function will
               return the appropriate table names (e.g. Collar, Survey, ENSurvey)
               for the other types.
               If the DRILLTYPE is NOT found in the template, a value of
               :def_val:`DH_DATA_UNKNOWN` is returned for the data type; likely an indication that this
               is not a new-style template produced by Wholeplot.
               This version also returns a list of the channels in the template checks can be made to
               see if the import will exceed the database channel limit.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Template name"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc=":def:`DH_DATA`"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="File name (blank for ODBC, or undefined)."),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="File name buffer size"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='5',
                             doc="Table name (blank for :def_val:`DH_DATA_UNKNOWN`, or undefined)."),
                   Parameter('p6', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Table name buffer size"),
                   Parameter('p7', type="LST",
                             doc="Channel list (returned)")
               ]),

        Method('IGetUnits_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Get the positional units and conversion factor to m.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc='Units (i.e. "m")'),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="length of Units string"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="conversion (units/m)")
               ]),

        Method('iHaveCurrent_DH', module='geodh', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Returns true if a drill project is loaded",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`"),

        Method('IiHaveCurrent2_DH', module='geodh', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Returns true if a drill project is loaded, and the collar database if it is loaded.",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='1',
                             doc="Collar table name (returned)"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Buffer size for collar table name")
               ]),

        Method('iHoles_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Return number of holes.",
               return_type=Type.INT32_T,
               return_doc="x  - Number of holes",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle")
               ]),

        Method('iHoleSelectFromListGUI_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Select/Deselect holes using the two-panel selection tool.",
               return_type=Type.INT32_T,
               return_doc="""
               0  - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="All holes"),
                   Parameter('p2', type="LST",
                             doc="Selected holes")
               ]),

        Method('iHoleSelectionToolGUI_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Select/Deselect holes using plan map tool.",
               return_type=Type.INT32_T,
               return_doc="""
               0  - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle")
               ]),

        Method('iModify3dGUI_DH', module='geodh', version='5.1.6',
               availability=Availability.EXTENSION, 
               doc="Modify parameters for a 3D plot.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name   (*.in3)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Page to open :class:`GUI` on")
               ]),

        Method('iModifyCrookedSectionHolesGUI_DH', module='geodh', version='7.2.0',
               availability=Availability.EXTENSION, 
               doc="Modify parameters to replot holes and hole data to an existing crooked section map.",
               notes="Will plot to an empty crooked section.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name (*.ins)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Tab page ID.")
               ]),

        Method('iModifyFenceGUI_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Modify parameters for a section plot.",
               notes="The fence section function.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Interactively define a fence.
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name (*.ins)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc=":def:`DH_SECT_PAGE`")
               ]),

        Method('iModifyHoleTraces3DGUI_DH', module='geodh', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Modify parameters for a hole traces plot to an existing 3D view.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Page to open :class:`GUI` on")
               ]),

        Method('iModifyHoleTracesGUI_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Modify parameters for a hole traces plot to a current map.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Page to open :class:`GUI` on")
               ]),

        Method('iModifyHoleTracesGUI2_DH', module='geodh', version='8.3.0',
               availability=Availability.EXTENSION, 
               doc="Modify parameters for a hole traces plot to a current plan or section view.",
               notes="Currently supports :def_val:`DH_PLOT_PLAN` and :def_val:`DH_PLOT_SECTION`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DH_PLOT` One of :def_val:`DH_PLOT_PLAN` or :def_val:`DH_PLOT_SECTION`"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Page to open :class:`GUI` on")
               ]),

        Method('iModifyPlanGUI_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Modify parameters for a plan plot.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name (*.inp)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc=":def:`DH_SECT_PAGE`")
               ]),

        Method('iModifyPlanHolesGUI_DH', module='geodh', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Modify parameters to replot holes and hole data to an existing plan map.",
               notes="Modifies only hole trace, hole data, topo, voxel slice data.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name (*.ins)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Tab Page ID")
               ]),

        Method('iModifyRockCodesGUI_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Modify/create a rock codes file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File name")
               ]),

        Method('iModifyRockCodesGUI2_DH', module='geodh', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Modify/create a rock codes file, channel population option.",
               notes="""
               Same as above, but passes the current database so that
               the "Populate from channel" button can be used to
               automatically populate the rock code list. The database
               should be a Wholeplot database.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="File name")
               ]),

        Method('iModifySectionGUI_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Modify parameters for a section plot.",
               notes="""
               The stacked section function uses the same control file
               format, but the plotting of profiles and plan views is
               disabled, and if multiple sections are requested, they
               are plotted in a stack on the left side of the same map,
               not to individual maps.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Interactively define a NS section
               2 - Interactively define an EW section
               3 - Interactively define an angled section
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name (*.ins)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc=":def:`DH_SECT_PAGE`")
               ]),

        Method('iModifySectionHolesGUI_DH', module='geodh', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Modify parameters to replot holes and hole data to an existing section map.",
               notes="""
               Works for both regular and stacked sections.
               Modifies only hole trace, hole data, topo, voxel slice data.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name (*.ins)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Tab page ID.")
               ]),

        Method('iModifyStackedSectionGUI_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Modify parameters for a section plot.",
               notes="""
               The stacked section function uses the same control file
               format, but the plotting of profiles and plan views is
               disabled, and if multiple sections are requested, they
               are plotted in a stack on the left side of the same map,
               not to individual maps.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Interactively define a NS section
               2 - Interactively define an EW section
               3 - Interactively define an angled section
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name (*.ins)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc=":def:`DH_SECT_PAGE`")
               ]),

        Method('iModifyStripLogGUI_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Modify parameters for a strip log plot.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Job Name   (*.inl)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc=":def:`DH_SECT_PAGE`")
               ]),

        Method('iModifyStructureCodesGUI_DH', module='geodh', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Modify/create a structure codes file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File name")
               ]),

        Method('iModifyStructureCodesGUI2_DH', module='geodh', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Modify/create a structure codes file, channel population option.",
               notes="""
               Same as above, but passes the current database so that
               the "Populate from channel" button can be used to
               automatically populate the structure code list. The database
               should be a Wholeplot database.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="File name")
               ]),

        Method('Import2_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports data into a Drill Hole Database (obsolete).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Drill project name"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` Handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Hole channel"),
                   Parameter('p5', type=Type.STRING,
                             doc="Table"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`DH_DATA`"),
                   Parameter('p7', type=Type.STRING,
                             doc="Log file name")
               ]),

        Method('ImportLAS_DH', module='geodh', version='6.0.1',
               availability=Availability.EXTENSION, 
               doc="Imports LAS Data into a :class:`DH` database",
               notes="""
               The argument for the assay database is the file name
               without the project name and underscore, e.g. for
               "Project_Assay.gdb" use "Assay"
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Assay database to use"),
                   Parameter('p3', type=Type.STRING,
                             doc="LAS file name"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Averaging/desampling interval (cm)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Interpolation method"),
                   Parameter('p6', type="WA",
                             doc="Log file handle")
               ]),

        Method('iNumAssays_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Number of assay datasets.",
               notes="Works for both single and multiple :class:`DB` Wholeplots.",
               return_type=Type.INT32_T,
               return_doc="The number of assay datasets.",
               parameters = [
                   Parameter('p1', type="DH",
                             doc="hDH object")
               ]),

        Method('iNumSelectedHoles_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Returns number of selected holes.",
               return_type=Type.INT32_T,
               return_doc="The number of selected holes",
               parameters = [
                   Parameter('p1', type="DH",
                             doc="Database")
               ]),

        Method('iQADipAzCurvatureLST_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC Curvature checking on Dip Azimuth data for holes in a :class:`LST`.",
               notes="Checks all holes with Dip-Azimuth survey data",
               return_type=Type.INT32_T,
               return_doc="The number of holes found and checked.",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` of holes (name, index)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Dip/Azimuth curvature tolerance (degree per meter)"),
                   Parameter('p4', type="WA",
                             doc=":class:`WA` Handle to write to")
               ]),

        Method('iQADipAzSurveyLST_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC on Dip/Az Survey data for holes in a :class:`LST`.",
               notes="""
               Error if no Dip-Azimuth survey database, or if
               a requested hole does not exist in the drill project.
               """,
               return_type=Type.INT32_T,
               return_doc="The number of holes found and checked.",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` of holes (Name, Index)"),
                   Parameter('p3', type="WA",
                             doc=":class:`WA` Handle to write to")
               ]),

        Method('iQAEastNorthCurvatureLST_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC Curvature checking on Dip Azimuth data for holes in a :class:`LST`.",
               notes="Checks all holes with East-North survey data",
               return_type=Type.INT32_T,
               return_doc="The number of holes found and checked.",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` of holes (name, index)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Dip/Azimuth curvature tolerance (degree per meter)"),
                   Parameter('p4', type="WA",
                             doc=":class:`WA` Handle")
               ]),

        Method('iQAEastNorthSurveyLST_DH', module='geodh', version='7.0.0',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC on East/North Survey data for holes in a :class:`LST`.",
               notes="""
               Error if no East-North survey database, or if
               a requested hole does not exist in the drill project.
               """,
               return_type=Type.INT32_T,
               return_doc="The number of holes found and checked.",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` of holes (Name, Index)"),
                   Parameter('p3', type="WA",
                             doc=":class:`WA` Handle to write to")
               ]),

        Method('iSliceSelectionToolGUI_DH', module='geodh', version='7.2.0',
               availability=Availability.EXTENSION, 
               doc="Select a slice with the holes in context. An optional 4 point area of interest (AOI) can be added to be represented in the UI too.",
               return_type=Type.INT32_T,
               return_doc="""
               0  - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="1st Corner of AOI - X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="1st Corner of AOI - Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="2nd Corner of AOI - X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="2nd Corner of AOI - Y"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="3rd Corner of AOI - X"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="3rd Corner of AOI - Y"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="4th Corner of AOI - X"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="4th Corner of AOI - Y"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Returned slice 1st point - X"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="Returned slice 1st point - Y"),
                   Parameter('p12', type=Type.DOUBLE, is_ref=True,
                             doc="Returned slice 2nd point - X"),
                   Parameter('p13', type=Type.DOUBLE, is_ref=True,
                             doc="Returned slice 2nd point - Y")
               ]),

        Method('iUpdateSurveyFromCollar_DH', module='geodh', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Update the Survey table from the collar info.",
               notes="""
               Call when the collar values are edited to update the survey table
               values. If the survey contains more than one row, then no changes
               are applied, and no warning or error is registered.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               0 - No change; there is no survey table, the table was empty, or values were same as collar
               1 - Survey table updated; values changed and there is just one row.
               2 - Survey table unchanged; there was more than one row in the table, and values were different
               """,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="hole index")
               ]),

        Method('LoadDataParametersINI_DH', module='geodh', version='6.0.0',
               availability=Availability.EXTENSION, 
               doc="Load data parameters from INI files..",
               notes="""
               Wholeplot data graphing parameters for each channel are stored
               in the channel :class:`REG`. This function lets a user transfer pre-defined
               settings to individual INI files (eg. cu.ini).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type="DB",
                             doc="Source database"),
                   Parameter('p3', type=Type.STRING,
                             doc="Directory to store INI files")
               ]),

        Method('LoadPlotParameters_DH', module='geodh', version='6.0.0',
               availability=Availability.EXTENSION, 
               doc="Load parameters from a Job into the Drill object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object."),
                   Parameter('p2', type=Type.STRING,
                             doc="The job file file to read"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DH_PLOT`")
               ]),

        Method('LoadSelect_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Load selections to from a file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('MaskPLY_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Set mask channel based on view selection polygon.",
               notes="""
               Data values inside the polygon area, and within the slice thickness
               have their mask channel values set to 1.
               If the specified mask channel does not exist, it is created.
               :def_val:`DH_MASK_NEW` --- Mask is created new for each selected hole
               :def_val:`DH_MASK_APPEND` --- Current selection is added to previous.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type="PLY",
                             doc="Masking polygon"),
                   Parameter('p3', type="IPJ",
                             doc="Projection from data to polygon coordinates"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Slice thickness - :def_val:`rDUMMY` for no limiting thickness"),
                   Parameter('p5', type=Type.STRING,
                             doc="name of mask channel"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`DH_HOLES`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`DH_MASK`")
               ]),

        Method('Open_DH', module='geodh', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Open :class:`DH` from collar database and load all associated databases.",
               return_type="DH",
               return_doc=":class:`DH` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of collar database")
               ]),

        Method('OpenJob_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Open a :class:`DH` plotting job",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="job file name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DH_PLOT`")
               ]),

        Method('PlotHoleTraces_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Plot hole traces to a regular (plan) map.",
               notes="""
               Both the hole traces and data can be plotted.
               The DHPLANHOLES GX uses the default plan map parameter file
               "_plan.inp".
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type="MAP",
                             doc="Map handle"),
                   Parameter('p3', type=Type.STRING,
                             doc="Parameter file (INI) name")
               ]),

        Method('PlotHoleTraces3D_DH', module='geodh', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Plot hole traces to an existing 3D map view.",
               notes="""
               Both the hole traces and data can be plotted.
               The DH3DHOLES GX uses the default 3D map parameter file
               "_3D.in3".
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type="MVIEW",
                             doc="Existing 3D map view"),
                   Parameter('p3', type=Type.STRING,
                             doc="Parameter file (INI) name (normally *.in3)")
               ]),

        Method('PlotSymbols3D_DH', module='geodh', version='9.1.0',
               availability=Availability.EXTENSION, 
               doc="Plot 3D symbols to an existing 3D map view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type="MVIEW",
                             doc="Existing 3D map view"),
                   Parameter('p3', type=Type.STRING,
                             doc="Parameter file (INI) name (normally *.in3)")
               ]),

        Method('QACollar_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC on Hole Collar data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` Handle")
               ]),

        Method('QACollarLST_DH', module='geodh', version='7.0.1',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC on Hole Collar data - :class:`LST` of holes.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` of holes (Name, Index)"),
                   Parameter('p3', type="WA",
                             doc=":class:`WA` Handle")
               ]),

        Method('QADipAzCurvature_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC Curvature checking on Dip Azimuth data.",
               notes="Checks all holes with Dip-Azimuth survey data",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` Handle"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Dip/Azimuth curvature tolerance (degree per meter)")
               ]),

        Method('QADipAzCurvature2_DH', module='geodh', version='6.4.2',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC Curvature checking on Dip Azimuth data for a single hole.",
               notes="Checks single hole with Dip-Azimuth survey data",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` Handle"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Dip/Azimuth curvature tolerance (degree per meter)"),
                   Parameter('p4', type=Type.STRING,
                             doc="Hole name")
               ]),

        Method('QADipAzSurvey_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC on Dip/Az Survey data.",
               notes="""
               Error if no Dip-Azimuth survey database, or if
               the requested line does not exist in the database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` Handle"),
                   Parameter('p3', type="WA",
                             doc=":class:`WA` Handle"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p5', type=Type.STRING,
                             doc="Current hole Name")
               ]),

        Method('QAEastNorthCurvature_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC Curvature checking on Dip Azimuth data.",
               notes="Checks all holes with East-North survey data",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` Handle"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Dip/Azimuth curvature tolerance (degree per meter)")
               ]),

        Method('QAEastNorthCurvature2_DH', module='geodh', version='6.4.2',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC Curvature checking on Dip Azimuth data for a single hole.",
               notes="Checks single holes with East-North survey data",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` Handle"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Dip/Azimuth curvature tolerance (degree per meter)"),
                   Parameter('p4', type=Type.STRING,
                             doc="Hole name")
               ]),

        Method('QAEastNorthSurvey_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC on East/North Survey data.",
               notes="""
               Error if no East-North survey database, or if
               the requested line does not exist in the database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` Handle"),
                   Parameter('p3', type="WA",
                             doc=":class:`WA` Handle"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p5', type=Type.STRING,
                             doc="Current hole Name")
               ]),

        Method('QAFromToData_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC on From/To data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` Handle"),
                   Parameter('p3', type="WA",
                             doc=":class:`WA` Handle"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p5', type=Type.STRING,
                             doc="Current hole Name")
               ]),

        Method('QAPointData_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Do QA/QC on Point data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` Handle"),
                   Parameter('p3', type="WA",
                             doc=":class:`WA` Handle"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p5', type=Type.STRING,
                             doc="Current hole Name")
               ]),

        Method('QAWriteUnregisteredHoles_DH', module='geodh', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Write out unregistered holes in a database.",
               notes="""
               Looks at each line in a database and sees if it is listed in
               the collar tables' hole list.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` Handle (not the collar table)"),
                   Parameter('p3', type="WA",
                             doc=":class:`WA` Handle")
               ]),

        Method('ReplotHoles_DH', module='geodh', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Replot holes on an existing drill map.",
               notes="""
               The parameter file must correspond to the plot Type.
               The hDH->hMAP value must be set first, using :func:`SetMAP_DH`().
               Overwrites existing hole and hole data groups.
               Replots the legend if the legend is enabled.
               This should only be used on a slightly modified version of the
               INI file used to create the existing map, or things may not
               work out (e.g. bad locations etc).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter (INI) name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DH_PLOT`")
               ]),

        Method('PlotHolesOnSection_DH', module='geodh', version='8.3.0',
               availability=Availability.EXTENSION, 
               doc="Plot the currently selected holes on an existing section view.",
               notes="Plot the currently selected holes to a section view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter (INI) name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DH_PLOT` Section plot type (:def_val:`DH_PLOT_SECTION` or :def_val:`DH_PLOT_SECTION_CROOKED`"),
                   Parameter('p4', type=Type.STRING,
                             doc="View name")
               ]),

        Method('ReSurveyEastNorth_DH', module='geodh', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Resurvey an East-North-RL survey.",
               notes="""
               Re-interpolates in X, Y and Z to proper depth interval
               and returns depths for each point
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Hole ID (for error messages)"),
                   Parameter('p3', type="VV",
                             doc="input East"),
                   Parameter('p4', type="VV",
                             doc="input North"),
                   Parameter('p5', type="VV",
                             doc="input RL"),
                   Parameter('p6', type="VV",
                             doc="returned depths down the hole"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="input collar East"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="input collar North"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="input collar RL"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="input top of hole depth"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="returned bottom depth")
               ]),

        Method('ReSurveyPolFit_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Use the polynomial fit resurveying method.",
               notes="""
               Uses the polynomial fit method to calculate (X, Y, Z)
               locations down the hole from azimuth, dip, depth values.
               The collar is assumed to be at zero depth, and depth is the
               measure distance down the hole (even if it's horizontal).
               A negative dip convention means vertical down is -90 degrees.
               The polynomial order must be in the range 1-20, with 5 being adequate
               for most smoothly curving holes. The order is reduced to no more than
               the number of input points.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Hole ID (used for error messages)"),
                   Parameter('p3', type="VV",
                             doc="Dip"),
                   Parameter('p4', type="VV",
                             doc="Azimuth"),
                   Parameter('p5', type="VV",
                             doc="Depth"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Collar X (easting) (depth = 0)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Collar Y (northing)(depth = 0)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Collar Z (elevation) (depth = 0)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Minimum hole depth to start output values"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Maximum hole depth for output values"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Increment for output values"),
                   Parameter('p12', type=Type.INT32_T,
                             doc=":def:`DIP_CONVENTION`"),
                   Parameter('p13', type=Type.INT32_T,
                             doc="Polynomial order"),
                   Parameter('p14', type="VV",
                             doc="X (Easting) - Output"),
                   Parameter('p15', type="VV",
                             doc="Y (Northin) - Output"),
                   Parameter('p16', type="VV",
                             doc="Z (Elevation) - Output"),
                   Parameter('p17', type="VV",
                             doc="Depths - Output")
               ]),

        Method('ReSurveyRadCurve_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Use radius of curvature resurveying method.",
               notes="""
               Uses the Radius of curvature method to calculate (X, Y, Z)
               locations down the hole from azimuth, dip, depth values.
               The collar is assumed to be at zero depth, and depth is the
               measure distance down the hole (even if it's horizontal).
               A negative dip convention means vertical down is -90 degrees.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Hole ID (used for error messages)"),
                   Parameter('p3', type="VV",
                             doc="Dip"),
                   Parameter('p4', type="VV",
                             doc="Azimuth"),
                   Parameter('p5', type="VV",
                             doc="Depth"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Collar X (easting) (depth = 0)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Collar Y (northing)(depth = 0)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Collar Z (elevation) (depth = 0)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Minimum hole depth to start output values"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Maximum hole depth for output values"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Increment for output values"),
                   Parameter('p12', type=Type.INT32_T,
                             doc=":def:`DIP_CONVENTION`"),
                   Parameter('p13', type="VV",
                             doc="X (Easting) - Output"),
                   Parameter('p14', type="VV",
                             doc="Y (Northin) - Output"),
                   Parameter('p15', type="VV",
                             doc="Z (Elevation) - Output"),
                   Parameter('p16', type="VV",
                             doc="Depths - Output")
               ]),

        Method('ReSurveyStraight_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Resurvey a straight hole.",
               notes="""
               Assumes a straight hole to calculate (X, Y, Z)
               locations down the hole from azimuth, dip, depth values.
               The collar is assumed to be at zero depth, and depth is the
               measure distance down the hole (even if it's horizontal).
               A negative dip convention means vertical down is -90 degrees.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Hole ID (used for error messages)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Collar Dip"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Collar Azimuth"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Collar X (easting) (depth = 0)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Collar Y (northing)(depth = 0)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Collar Z (elevation) (depth = 0)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Minimum hole depth to start output values"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Maximum hole depth for output values"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Increment for output values"),
                   Parameter('p11', type=Type.INT32_T,
                             doc=":def:`DIP_CONVENTION`"),
                   Parameter('p12', type="VV",
                             doc="X (Easting) - Output"),
                   Parameter('p13', type="VV",
                             doc="Y (Northin) - Output"),
                   Parameter('p14', type="VV",
                             doc="Z (Elevation) - Output"),
                   Parameter('p15', type="VV",
                             doc="Depths - Output")
               ]),

        Method('ReSurveyStraightSeg_DH', module='geodh', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Resurvey a hole with straight segments between locations.",
               notes="""
               Calculate (X, Y, Z) locations down the hole from azimuth, dip,
               depth values, assuming each segment is straight, and the hole
               bends at each successive azimuth, dip, depth value.
               The collar is assumed to be at zero depth, and depth is the
               measure distance down the hole (even if it's horizontal).
               A negative dip convention means vertical down is -90 degrees.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Hole ID (used for error messages)"),
                   Parameter('p3', type="VV",
                             doc="Dip"),
                   Parameter('p4', type="VV",
                             doc="Azimuth"),
                   Parameter('p5', type="VV",
                             doc="Depth"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Collar X (easting) (depth = 0)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Collar Y (northing)(depth = 0)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Collar Z (elevation) (depth = 0)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Minimum hole depth to start output values"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Maximum hole depth for output values"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Increment for output values"),
                   Parameter('p12', type=Type.INT32_T,
                             doc=":def:`DIP_CONVENTION`"),
                   Parameter('p13', type="VV",
                             doc="X (Easting) - Output"),
                   Parameter('p14', type="VV",
                             doc="Y (Northin) - Output"),
                   Parameter('p15', type="VV",
                             doc="Z (Elevation) - Output"),
                   Parameter('p16', type="VV",
                             doc="Depths - Output")
               ]),

        Method('SaveDataParametersINI_DH', module='geodh', version='6.0.0',
               availability=Availability.EXTENSION, 
               doc="Save data parameters to INI files..",
               notes="""
               Wholeplot data graphing parameters for each channel are stored
               in the channel :class:`REG`. This function lets a user transfer pre-defined
               settings to individual INI files (eg. cu.ini).
               As of v6.3, the :class:`DH` object is NOT required for this function, and
               is, in fact, ignored.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object   (ignored)."),
                   Parameter('p2', type="DB",
                             doc="Source database"),
                   Parameter('p3', type=Type.STRING,
                             doc="Directory to store INI files")
               ]),

        Method('SaveJob_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Save a :class:`DH` plotting job",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="job file name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DH_PLOT`")
               ]),

        Method('SaveSelect_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Saves current selections to a file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('SectionWindowSizeMM_DH', module='geodh', version='6.0.0',
               availability=Availability.EXTENSION, 
               doc="Deterine the size, in mm, of the section window",
               notes="""
               Given the current selection of windows (e.g. legend, plan),
               paper size and orientation, return the size in mm of the
               window used for plotting the section.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X size in mm."),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y size in mm.")
               ]),

        Method('SelectAllHoles_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Select all the holes in a Drill hole project.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="Database")
               ]),

        Method('SelectHoles_DH', module='geodh', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="Select holes by hole indices.",
               notes="""
               Indices less than 0 are skipped. This lets you use this function
               after a call to :func:`FindItems_LST`, which returns -1 for indices not located.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type="VV",
                             doc="INT :class:`VV` with hole indices."),
                   Parameter('p3', type=Type.INT32_T,
                             doc="0 - deselect, 1 - select")
               ]),

        Method('SelectName_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Select holes using a name mask.",
               notes="""
               Overwrite mode - all selections tested and selected or not selected
               Append mode    - only holes matching the mask are selected or not selected.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="mask"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="0 - deselect, 1 - select"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="0 - overwrite, 1 - append")
               ]),

        Method('SelectPLY_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Select all holes in :class:`PLY` (Polygon) object.",
               notes="""
               This function operates the same as the call:
               
               :func:`SelectPLY2_DH`(Drill, 1, 0, 0);
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="Database"),
                   Parameter('p2', type="PLY",
                             doc="Polygon object")
               ]),

        Method('SelectPLY2_DH', module='geodh', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Select holes in :class:`PLY` (Polygon) object with options.",
               notes="""
               The various selection options give the following results:
               
               New/Select/inside: Unselect all holes, then
                                  select all holes inside the polygon.
               New/Select/outside: Unselect all holes, then
                                  select all holes outside the polygon.
               New/Deselect/inside: Select all holes, then
                                  deselect all holes inside the polygon.
               New/Deselect/outside: Select all holes, then
                                  deselect all holes outside the polygon.
               
               Append/Select/inside: Select all holes inside the polygon.
                                     Leave selections outside as is.
               Append/Select/outside: Select all holes outside the polygon.
                                     Leave selections inside as is.
               Append/Deselect/inside: Deselect all holes inside the polygon
                                     Leave selections outside as is.
               Append/Deselect/outside: Deselect all holes outside the polygon.
                                     Leave selections inside as is.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="Database"),
                   Parameter('p2', type="PLY",
                             doc="Polygon object"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Select (0) or Deselect (1)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Region (0: inside, 1: outside)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Mode (0: Append, 1: New)")
               ]),

        Method('SetCrookedSectionIPJ_DH', module='geodh', version='7.2.0',
               availability=Availability.EXTENSION, 
               doc="Pass the Crooked projection required for plotting to a crooked section.",
               notes="This might be extracted from an existing crooked section view, or created from a database line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type="IPJ",
                             doc="Crooked Section :class:`IPJ`")
               ]),

        Method('SetCurrentViewName_DH', module='geodh', version='7.2.0',
               availability=Availability.EXTENSION, 
               doc="Set the current map view name.",
               notes="Can be used to specify the name of the view to plot into.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="View name")
               ]),

        Method('SetInfo_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Set Collar Information.",
               notes="""
               If the DH_ELEV channel is requested it will also
               search for the DH_RL channel, which is the new
               name for the collar elevation.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="hole index"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of information"),
                   Parameter('p4', type=Type.STRING,
                             doc="Information")
               ]),

        Method('SetIPJ_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Set the project :class:`IPJ`.",
               notes="""
               The projection for the project is the projection stored
               in the DH_EAST channel in the collar table. This
               function sets the projection of the (DH_EAST, DH_NORTH)
               channel pairs in each of the project databases to the
               input :class:`IPJ`.
               The input :class:`IPJ` cannot be a geographic coordinate system
               or this call will fail with an error message.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` Handle")
               ]),

        Method('SetMAP_DH', module='geodh', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Store the current :class:`MAP` to the :class:`DH` object.",
               notes="""
               Use this before calling the ReplotHoles functions,
               so that, instead of creating a new map, the plotting
               functions use the existing one.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="MAP",
                             doc=":class:`IPJ` Handle")
               ]),

        Method('SetNewIPJ_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Set a new project database projection to collar table projection.",
               notes="""
               Gets the :class:`IPJ` of the collar table current x channel and copies it
               into the named database (as long as it is in the project!)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="project database name")
               ]),

        Method('SetSelectedHolesVV_DH', module='geodh', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Set hole selection using hole indices.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="VV",
                             doc="Input hole indices (must be type INT)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="0 - overwrite, 1 - append")
               ]),

        Method('SetTemplateBlob_DH', module='geodh', version='6.0.0',
               availability=Availability.EXTENSION, 
               doc="Store the import template to the database.",
               notes="""
               The template can later be retrieved in order to refresh the
               database with a call to the DHIMPORT.GX.
               
               The import types correspond to the DHIMPORT.IMPTYPE variable:
               0: ASCII, 1: Database/XLS, 2: ODBC
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc=":class:`DB` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Import template name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DH_DATA`")
               ]),

        Method('SignificantIntersectionsDB_DH', module='geodh', version='7.2.0',
               availability=Availability.EXTENSION, 
               doc="Make a report of Significant Intersections",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Object"),
                   Parameter('p2', type="DB",
                             doc="Input assay :class:`DB` object"),
                   Parameter('p3', type="DB",
                             doc="output composite :class:`DB` object"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DH_COMPSTDB_HOLSEL`"),
                   Parameter('p5', type=Type.STRING,
                             doc="The primary assay channel."),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Minimum Cut off grade for Primary Assay"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Maximum Cut off grade for Primary Assay"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Minimum Composite Length"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Minimum Composite thickness"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Maximum Internal Dilution"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Minimum diluted grade"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="Grade for Missing Assays")
               ]),

        Method('TestImportLAS_DH', module='geodh', version='6.0.1',
               availability=Availability.EXTENSION, 
               doc="Tests import of LAS Data for problems.",
               notes="""
               See :func:`ImportLAS_DH`.
               Determines if the import of the LAS data will result in data
               being overwritten, interpolated or resampled. Warnings are written to a log
               file, as in sImportLAS_DH. Warnings are not registered in cases
               where data is merely extended at the start or the end with dummies
               to match a different interval down the hole.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Assay table name"),
                   Parameter('p3', type=Type.STRING,
                             doc="LAS file name"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="averaging/desampling interval"),
                   Parameter('p5', type="WA",
                             doc="Log file handle"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="1 returned if problems found")
               ]),

        Method('UnSelectAllHoles_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Unselect all the holes in a Drill hole project.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc="Database")
               ]),

        Method('UnSelectedHoleLST_DH', module='geodh', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="Populate an :class:`LST` with the list of the unselected holes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` handle")
               ]),

        Method('UpdateCollarTable_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Update all collar table information.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle")
               ]),

        Method('UpdateHoleExtent_DH', module='geodh', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Update extents for one hole.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="hole index")
               ]),

        Method('Wholeplot_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, 
               doc="Run a Wholeplot plot job.",
               notes="""
               The parameter file must correspond to the plot Type. The INI file
               contains settings for all of the non-database data related
               parameters (e.g. Map template, scale, boundaries,
               section definitions, hole trace parameters etc...)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Parameter (INI) name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DH_PLOT`")
               ]),

        Method('SurfaceIntersections_DH', module='geodh', version='8.3.0',
               availability=Availability.EXTENSION, 
               doc="Determine intersections of drillholes with a surface.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="DB",
                             doc="Output :class:`DB` Handle"),
                   Parameter('p3', type=Type.STRING,
                             doc="Input surface file"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Selected holes (1), All holes (0)")
               ])
    ],
    'Obsolete': [

        Method('GetSHPNamesVV_DH', module='geodh', version='5.1.8',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Get generated :class:`SHP` file names.",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object"),
                   Parameter('p2', type="VV",
                             doc="returned :class:`SHP` names (string type :class:`VV`)"),
                   Parameter('p3', type="VV",
                             doc="corresponding data frame for each :class:`SHP`")
               ]),

        Method('iIsMultiDB_DH', module='geodh', version='5.1.2',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Is this a (new-style) multi-database Wholeplot project?",
               notes="""
               As of v6.3.0, old single-database Wholeplot GDBs cannot
               be opened, so this check is obsolete. The function now always
               returns TRUE (1).
               """,
               return_type=Type.INT32_T,
               return_doc="1 if it is a new-style Wholeplot database.",
               parameters = [
                   Parameter('p1', type="DH",
                             doc=":class:`DH` object")
               ])
    ]
}

