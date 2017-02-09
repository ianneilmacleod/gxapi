from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DU',
                 doc="""
                 :class:`DU` functions provide a variety of common utilities that can be applied
                 efficiently to the contents of a database. Most :class:`DU` library functions take
                 as their first argument a :class:`DB` object, and apply standard processes to data
                 stored in an OASIS database, including import and export functions.
                 """,
                 notes="""
                 The following defines are used by GX functions but are not required
                 for any methods:
                 
                 :def:`DU_LINES`
                 """)


gx_defines = [
    Define('DB_DUP',
           doc="Duplicate Types",
           constants=[
               Constant('DB_DUP_FIRST', value='1', type=Type.INT32_T)                        ,
               Constant('DB_DUP_AVERAGE', value='2', type=Type.INT32_T)                        ,
               Constant('DB_DUP_MINIMUM', value='3', type=Type.INT32_T)                        ,
               Constant('DB_DUP_MAXIMUM', value='4', type=Type.INT32_T)                        ,
               Constant('DB_DUP_MEDIAN', value='5', type=Type.INT32_T)                        ,
               Constant('DB_DUP_LAST', value='6', type=Type.INT32_T)                        
           ]),

    Define('DB_DUPEDIT',
           doc="Duplicate Edit Flags",
           constants=[
               Constant('DB_DUPEDIT_SINGLE', value='0', type=Type.INT32_T)                        ,
               Constant('DB_DUPEDIT_ALL', value='1', type=Type.INT32_T)                        
           ]),

    Define('DU_CHANNELS',
           doc="Channels to Display",
           constants=[
               Constant('DU_CHANNELS_DISPLAYED', value='0', type=Type.INT32_T)                        ,
               Constant('DU_CHANNELS_ALL', value='1', type=Type.INT32_T)                        
           ]),

    Define('DU_EXPORT',
           doc="Export Type",
           constants=[
               Constant('DU_EXPORT_CSV', value='0', type=Type.INT32_T)                        ,
               Constant('DU_EXPORT_ODDF', value='1', type=Type.INT32_T)                        ,
               Constant('DU_EXPORT_POST_PC', value='2', type=Type.INT32_T)                        ,
               Constant('DU_EXPORT_POST_UNIX', value='3', type=Type.INT32_T)                        
           ]),

    Define('DU_FILL',
           doc="Filling Options",
           constants=[
               Constant('DU_FILL_INSIDE', value='0', type=Type.INT32_T)                        ,
               Constant('DU_FILL_OUTSIDE', value='1', type=Type.INT32_T)                        
           ]),

    Define('DU_IMPORT',
           doc="Import Mode",
           constants=[
               Constant('DU_IMPORT_APPEND', value='0', type=Type.INT32_T)                        ,
               Constant('DU_IMPORT_REPLACE', value='1', type=Type.INT32_T)                        ,
               Constant('DU_IMPORT_MERGE', value='2', type=Type.INT32_T)                        ,
               Constant('DU_IMPORT_MERGE_APPEND', value='3', type=Type.INT32_T)                        
           ]),

    Define('DU_INTERP',
           doc="Inside Interpolation Method",
           constants=[
               Constant('DU_INTERP_NEAREST', value='1', type=Type.INT32_T)                        ,
               Constant('DU_INTERP_LINEAR', value='2', type=Type.INT32_T)                        ,
               Constant('DU_INTERP_CUBIC', value='3', type=Type.INT32_T)                        ,
               Constant('DU_INTERP_AKIMA', value='4', type=Type.INT32_T)                        ,
               Constant('DU_INTERP_PREDICT', value='5', type=Type.INT32_T)                        
           ]),

    Define('DU_INTERP_EDGE',
           doc="Edge Interpolation Method",
           constants=[
               Constant('DU_INTERP_EDGE_NONE', value='0', type=Type.INT32_T)                        ,
               Constant('DU_INTERP_EDGE_SAME', value='1', type=Type.INT32_T)                        ,
               Constant('DU_INTERP_EDGE_NEAREST', value='2', type=Type.INT32_T)                        ,
               Constant('DU_INTERP_EDGE_LINEAR', value='3', type=Type.INT32_T)                        
           ]),

    Define('DU_LAB_TYPE',
           doc="File Types",
           constants=[
               Constant('DU_LAB_TYPE_FREE', value='1', type=Type.INT32_T,
                        doc="""
                        The delimiter string identifies
                        characters to be used as delimiters.  Use C style escape
                        sequences to identify non-printable characters.  The
                        default delimiters for FREE format files are " \\t,".
                        """)                        ,
               Constant('DU_LAB_TYPE_COMMA', value='2', type=Type.INT32_T,
                        doc="""
                        For COMMA type files, the delimiter string identifies
                        characters to be removed before comma delimiting.  The
                        default for COMMA delimited files is " \\t".
                        """)                        
           ]),

    Define('DU_LEVEL',
           doc="Leveling Options",
           constants=[
               Constant('DU_LEVEL_LINES', value='0', type=Type.INT32_T,
                        doc="extract line corrections")                        ,
               Constant('DU_LEVEL_TIES', value='1', type=Type.INT32_T,
                        doc="extract tie corrections")                        ,
               Constant('DU_LEVEL_ALL', value='2', type=Type.INT32_T,
                        doc="extract all corrections")                        
           ]),

    Define('DU_LINEOUT',
           doc="Lineout Options (du.h)",
           constants=[
               Constant('DU_LINEOUT_SINGLE', value='0', type=Type.INT32_T)                        ,
               Constant('DU_LINEOUT_MULTIPLE', value='1', type=Type.INT32_T)                        
           ]),

    Define('DU_FEATURE_TYPE_OUTPUT',
           doc="Export to geodatabase feature type (du.h)",
           constants=[
               Constant('DU_FEATURE_TYPE_OUTPUT_POINT', value='0', type=Type.INT32_T)                        ,
               Constant('DU_FEATURE_TYPE_OUTPUT_LINE', value='1', type=Type.INT32_T)                        
           ]),

    Define('DU_GEODATABASE_EXPORT_TYPE',
           doc="Export to geodatabase overwrite mode(du.h)",
           constants=[
               Constant('DU_GEODATABASE_EXPORT_TYPE_OVERWRITE_GEODATABASE', value='0', type=Type.INT32_T)                        ,
               Constant('DU_GEODATABASE_EXPORT_TYPE_OVERWRITE_FEATURECLASS', value='1', type=Type.INT32_T)                        ,
               Constant('DU_GEODATABASE_EXPORT_TYPE_APPEND', value='2', type=Type.INT32_T)                        
           ]),

    Define('DU_LINES',
           doc="Lines to display",
           constants=[
               Constant('DU_LINES_DISPLAYED', value='0', type=Type.INT32_T)                        ,
               Constant('DU_LINES_SELECTED', value='1', type=Type.INT32_T)                        ,
               Constant('DU_LINES_ALL', value='2', type=Type.INT32_T)                        
           ]),

    Define('DU_LOADLTB',
           doc="Load table options",
           constants=[
               Constant('DU_LOADLTB_REPLACE', value='0', type=Type.INT32_T)                        ,
               Constant('DU_LOADLTB_APPEND', value='1', type=Type.INT32_T)                        
           ]),

    Define('DU_LOOKUP',
           doc="Lookup Mode",
           constants=[
               Constant('DU_LOOKUP_EXACT', value='0', type=Type.INT32_T,
                        doc="""
                        Requires an exact match in all indexes.
                        Results will dummy if Indexes are not found.
                        """)                        ,
               Constant('DU_LOOKUP_NEAREST', value='1', type=Type.INT32_T,
                        doc="""
                        Requires that the first index match exactly.
                        The nearest second index will be used for the finding
                        the lookup value.
                        The results will be dummy only if the first index
                        does not have a match.
                        """)                        ,
               Constant('DU_LOOKUP_INTERPOLATE', value='2', type=Type.INT32_T,
                        doc="""
                        The same as _NEAREST, except that the value will
                        be interpolated between the two nearest
                        framing values in the table.
                        """)                        ,
               Constant('DU_LOOKUP_NEARESTCLOSE', value='3', type=Type.INT32_T,
                        doc="""
                        Same as _NEAREST mode except that the target
                        value must be within the CLOSE distance to a
                        table value.
                        a) the primary index channel for single index
                        lookups;
                        b) the secondary index channel for
                        double index lookups.
                        Values not in data spacing are dummy.
                        """)                        ,
               Constant('DU_LOOKUP_INTERPCLOSE', value='4', type=Type.INT32_T,
                        doc="""
                        Same as _INTERPOLATE mode except that the target
                        value must be within the CLOSE distance to a
                        table value.
                        a) the primary index channel for single index
                        lookups;
                        b) the secondary index channel for
                        double index lookups.
                        Values not in data spacing are dummy.
                        """)                        ,
               Constant('DU_LOOKUP_INTERPOLATE_DUMMYOUTSIDE', value='5', type=Type.INT32_T,
                        doc="Interpolate between values, dummy beyond two ends")                        ,
               Constant('DU_LOOKUP_INTERPOLATE_CONSTOUTSIDE', value='6', type=Type.INT32_T,
                        doc="Interpolate between values, constant end values beyond two ends")                        ,
               Constant('DU_LOOKUP_INTERPOLATE_EXTPLOUTSIDE', value='7', type=Type.INT32_T,
                        doc="Interpolate between values, extrapolate beyond two ends")                        ,
               Constant('DU_LOOKUP_MAXOPTION', value='8', type=Type.INT32_T,
                        doc="Maximum option value")                        
           ]),

    Define('DU_MASK',
           doc="Masking Options",
           constants=[
               Constant('DU_MASK_INSIDE', value='0', type=Type.INT32_T)                        ,
               Constant('DU_MASK_OUTSIDE', value='1', type=Type.INT32_T)                        
           ]),

    Define('DU_MERGE',
           doc="Merge flags",
           constants=[
               Constant('DU_MERGE_APPEND', value='0', type=Type.INT32_T)                        
           ]),

    Define('DU_MODFID',
           doc="Fid Update Options",
           constants=[
               Constant('DU_MODFID_INSERT', value='0', type=Type.INT32_T,
                        doc="""
                        Will insert fid range by moving data.  Inserted
                        range will always be dummied out.  If the insertion point
                        is before start of data, the fid start is changed.
                        """)                        ,
               Constant('DU_MODFID_DELETE', value='1', type=Type.INT32_T,
                        doc="Will delete the range of fids.")                        ,
               Constant('DU_MODFID_APPEND', value='2', type=Type.INT32_T,
                        doc="""
                        Is like INSERT, except that it is only used to
                        add fids to the start or end of the existing data.  The
                        data is not moved with repect to the current fid locations.
                        """)                        
           ]),

    Define('DU_MOVE',
           doc="Move Style",
           constants=[
               Constant('DU_MOVE_ABSOLUTE', value='0', type=Type.INT32_T,
                        doc="move input to absolute value in control channel")                        ,
               Constant('DU_MOVE_MINUS', value='1', type=Type.INT32_T,
                        doc="subtract control channel from input channel")                        ,
               Constant('DU_MOVE_PLUS', value='2', type=Type.INT32_T,
                        doc="add control channel to input channel")                        ,
               Constant('DU_MOVE_INTERP', value='3', type=Type.INT32_T,
                        doc="""
                        data is NOT moved, but dummies in the input are interpolated
                        based on the control channel, assuming both the input and control
                        vary linearly inside the gaps
                        """)                        
           ]),

    Define('DU_REFID',
           doc="Interpolation mode",
           constants=[
               Constant('DU_REFID_LINEAR', value='0', type=Type.INT32_T,
                        doc="0")                        ,
               Constant('DU_REFID_MINCUR', value='1', type=Type.INT32_T,
                        doc="1")                        ,
               Constant('DU_REFID_AKIMA', value='2', type=Type.INT32_T,
                        doc="2")                        ,
               Constant('DU_REFID_NEAREST', value='3', type=Type.INT32_T,
                        doc="3")                        
           ]),

    Define('DU_SORT',
           doc="Sort Direction",
           constants=[
               Constant('DU_SORT_ASCENDING', value='0', type=Type.INT32_T)                        ,
               Constant('DU_SORT_DESCENDING', value='1', type=Type.INT32_T)                        
           ]),

    Define('DU_SPLITLINE',
           doc="Sort Direction",
           constants=[
               Constant('DU_SPLITLINE_XYPOSITION', value='0', type=Type.INT32_T)                        ,
               Constant('DU_SPLITLINE_SEQUENTIAL', value='1', type=Type.INT32_T)                        ,
               Constant('DU_SPLITLINE_TOVERSIONS', value='2', type=Type.INT32_T)                        
           ]),

    Define('DU_STORAGE',
           doc="Storage Type",
           constants=[
               Constant('DU_STORAGE_LINE', value='0', type=Type.INT32_T)                        ,
               Constant('DU_STORAGE_GROUP', value='1', type=Type.INT32_T)                        
           ]),

    Define('QC_PLAN_TYPE',
           doc="Type Plan",
           constants=[
               Constant('QC_PLAN_SURVEYLINE', value='0', type=Type.INT32_T)                        ,
               Constant('QC_PLAN_TIELINE', value='1', type=Type.INT32_T)                        ,
               Constant('QC_PLAN_BOTHLINES', value='2', type=Type.INT32_T)                        
           ]),

    Define('DU_DISTANCE_CHANNEL_TYPE',
           doc="Distance channel direction type",
           constants=[
               Constant('DU_DISTANCE_CHANNEL_MAINTAIN_DIRECTION', value='0', type=Type.INT32_T,
                        doc="Zero distance is always at the start of the line.")                        ,
               Constant('DU_DISTANCE_CHANNEL_CARTESIAN_COORDINATES', value='1', type=Type.INT32_T,
                        doc="Put zero at the end of the line with min X if X changes most, or min Y if Y changes most")                        
           ]),

    Define('DU_DIRECTGRID_METHOD',
           doc="How to calculate the cell values for direct gridding.",
           constants=[
               Constant('DU_DIRECTGRID_MIN', value='0', type=Type.INT32_T)                        ,
               Constant('DU_DIRECTGRID_MAX', value='1', type=Type.INT32_T)                        ,
               Constant('DU_DIRECTGRID_MEAN', value='2', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('_TableLook1_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a new channel using a single reference table",
               notes="""
               Fails if table does not contain requested fields.
               The nominal data sample spacing for the CLOSE options is
               calculated by finding the fiducial increment the
               - primary index channel for Lookup1C_DU;
               - secondary index channel for Lookup2C_DU, LookupIValC_DU
               and LookupRValC_DU
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Lookup reference channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output Channel Token     [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.STRING,
                             doc="Reference field name in table"),
                   Parameter('p6', type=Type.STRING,
                             doc="Lookup output name in table"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`DU_LOOKUP`"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="CLOSE lookup distance. If 0.0, distance is calculated from lookup reference channel."),
                   Parameter('p9', type="TB",
                             doc=":class:`TB` table Object")
               ]),

        Method('_TableLook2_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a new channel using a double reference  table.",
               notes="""
               Fails if table does not contain requested fields.
               The nominal data sample spacing for the CLOSE options is
               calculated by finding the fiducial increment the
               - primary index channel for Lookup1C_DU;
               - secondary index channel for Lookup2C_DU, LookupIValC_DU
               and LookupRValC_DU
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Primary reference channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Secondary reference channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Output channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type=Type.STRING,
                             doc="Primary reference field name in table"),
                   Parameter('p7', type=Type.STRING,
                             doc="Secondary reference field name in table"),
                   Parameter('p8', type=Type.STRING,
                             doc="Lookup result field name in table"),
                   Parameter('p9', type=Type.INT32_T,
                             doc=":def:`DU_LOOKUP`"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="CLOSE lookup distance.  If 0.0, distance is calculated from secondary reference channel."),
                   Parameter('p11', type="TB",
                             doc="Table Object")
               ]),

        Method('_TableLookI2_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Create a new channel using constant integer primary
               reference and a secondary reference table.
               """,
               notes="""
               Fails if table does not contain requested fields.
               The nominal data sample spacing for the CLOSE options is
               calculated by finding the fiducial increment the
               - primary index channel for Lookup1C_DU;
               - secondary index channel for Lookup2C_DU, LookupIValC_DU
               and LookupRValC_DU
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Lookup primary reference value"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Lookup secondary reference channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Output Channel Token [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type=Type.STRING,
                             doc="Primary reference field name in table"),
                   Parameter('p7', type=Type.STRING,
                             doc="Secondary reference field name in table"),
                   Parameter('p8', type=Type.STRING,
                             doc="Lookup result field name in table"),
                   Parameter('p9', type=Type.INT32_T,
                             doc=":def:`DU_LOOKUP`"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="CLOSE lookup distance.  If 0.0, distance calculated from secondary reference channel."),
                   Parameter('p11', type="TB",
                             doc="Table Object")
               ]),

        Method('_TableLookR2_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Create a new channel using a constant real primary
               reference and a secondary reference table.
               """,
               notes="""
               Fails if table does not contain requested fields.
               The nominal data sample spacing for the CLOSE options is
               calculated by finding the fiducial increment the
               - primary index channel for Lookup1C_DU;
               - secondary index channel for Lookup2C_DU, LookupIValC_DU
               and LookupRValC_DU
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Primary reference value"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Secondary reference value [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Output Channel Token [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type=Type.STRING,
                             doc="Primary reference field name in table"),
                   Parameter('p7', type=Type.STRING,
                             doc="Secondary reference field name in table"),
                   Parameter('p8', type=Type.STRING,
                             doc="Lookup result field name in table"),
                   Parameter('p9', type=Type.INT32_T,
                             doc=":def:`DU_LOOKUP`"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="CLOSE lookup distance.  If 0.0, distance calculated from secondary reference channel."),
                   Parameter('p11', type="TB",
                             doc="Table Object")
               ]),

        Method('ADOTableNames_DU', module='geogxx', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Scans a ADO-compliant database and returns the table names in a :class:`VV`",
               notes="""
               The :class:`VV` must be created to hold strings of length
               :def_val:`STR_DB_SYMBOL`; i.e. use
               Creat_VV(-:def_val:`STR_DB_SYMBOL`, 0), or it will assert.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database connection string"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` to return names in")
               ]),

        Method('AnSig_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate the Analytic Signal of a channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Input channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output Analytic Signal channel [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('Append_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Append a source database onto a destination database.",
               notes="""
               If the source database and destination database have channels
               with the same name, then data is appended onto the end
               of the channel in lines which have the same number.
               
               If a channel in the destination database is not also in the source
               database, it is ignored.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Source Database"),
                   Parameter('p2', type="DB",
                             doc="Destination Database"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Ignore write protection on channels? (TRUE or FALSE)")
               ]),

        Method('AvgAzimuth_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Returns average azimuth of selected lines.",
               notes="""
               Direction in degrees azimuth (clockwise relative
               the +Y direction). The result is in the range
               -90 < azimuth <= 90. The method handles lines going
               in opposite directions (they do not average to 0!)
               The method takes a precision, which is used to generate
               a series of "test" angles.
               The dot product of the line directions is taken
               with each of the test angles, and the absolute values summed.
               The maximum value occurs at the angle which most closely
               approximates the trend direction of the lines.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Precision in degrees (1 to 45)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Azimuth value returned")
               ]),

        Method('BaseData_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               This method corrects an entire database line using a
               time-based correction table. It is given 2 input channel
               tokens and 1 output channel token as well as the table
               object to use.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle to apply correction to"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Input Channel Token  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Time Channel Token   [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Output Channel Token [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type="TB",
                             doc="Table Object (a Date/Time/Correction Table)")
               ]),

        Method('BaseDataEx_DU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="""
               This method corrects an entire database line using a
               time-based correction table. It is given 2 input channel
               tokens and 1 output channel token as well as the table
               object to use (table sort flag=1 for sort, =0 for no sort).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle to apply correction to"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Input Channel Token  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Time Channel Token   [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Output Channel Token [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type="TB",
                             doc="Table Object (a Date/Time/Correction Table)"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Table sort flag: 0 - do not sort, 1 - do sort.")
               ]),

        Method('BoundLine_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Set map boundary clip limits.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Channel   [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Channel   [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="PLY",
                             doc="Polygon Object to use")
               ]),

        Method('BPFilt_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               This method applies a band-pass filter to the specified
               line/channel and places the output in the output channel.
               """,
               notes="""
               If the short and long wavelengths are <= 0, the input channel
               is simply copied to the output channel without filtering.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Input channel to filter [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output filtered channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Short wavelength cutoff, 0 for highpass"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Long wavelength cutoff, 0 for lowpass"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Filter Length, 0 for default length")
               ]),

        Method('BreakLine_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Break up a line based on line numbers in a channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel containing line numbers [:def_val:`DB_LOCK_READONLY`]")
               ]),

        Method('BreakLine2_DU', module='geogxx', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Break up a line based on line numbers in a channel.",
               notes="The same as BreakLine, but with an option to reset each line's starting fiducial to zero.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel containing line numbers [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Reset starting fiducials to zero (0: No, 1: Yes)")
               ]),

        Method('BreakLineToGroups_DU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Break up a line into group-lines based on a channel.",
               notes="""
               The original line will be deleted.
               This is similar to :func:`BreakLine_DU`, but the output lines
               are "group" lines, without the line type letters at the
               start. (See db.gxh for information of Group Lines).
               All channels are associated with each group line, and the
               input class name is assigned to each group.
               Class names for
               groups ensure that (for instance) if you add a new channel to
               one group of a given class, it will get added to all other
               groups in the same class. If the class name is left empty, then
               this will NOT be true. (Groups without class names are treated
               as isolated entities for the purposes of channel loading).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel containing line numbers [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type=Type.STRING,
                             doc='Class name for new group lines (can be "")')
               ]),

        Method('BreakLineToGroups2_DU', module='geogxx', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Break up a line into group-lines based on a channel.",
               notes="The same as BreakLineToGroups, but with an option to reset each line's starting fiducial to zero.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel containing line numbers [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type=Type.STRING,
                             doc='Class name for new group lines (can be "")'),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Reset starting fiducials to zero (0: No, 1: Yes)")
               ]),

        Method('BSpline_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="B-spline Interpolate a Channel.",
               see_also=":func:`Trend_DU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel to interpolate [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output interpolated channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Data error (Std Dev > 0.0)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Roughness (Rou > 0.0)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Tension (0.<= Tension <=1.)")
               ]),

        Method('ClosestPoint_DU', module='geogxx', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Return closest data point to input location.",
               notes="""
               Selected lines are scanned for the (X, Y) location
               which is closest to the input location.
               The line and fiducial of the point are returned.
               
               Will register an error if no valid (X, Y) locations
               are found.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="located X location"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="located Y location"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="line for located point"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="fiducial of located point")
               ]),

        Method('CopyLine_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Copy a line.",
               notes="""
               Existing channels in the output line will be replaced
               by copied channels.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Input Line  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Output Line [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('CopyLineAcross_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Copy a line from one database to another.",
               notes="""
               Existing channels in the output line will be replaced
               by copied channels.
               """,
               see_also=":func:`CopyLineChanAcross_DU` function",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Input Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Input Line  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB",
                             doc="Output Database"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output Line [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('CopyLineChanAcross_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Copy a list of channels in a line from one database to another.",
               notes="""
               Existing channels in the output line will be replaced
               by copied channels.
               """,
               see_also=":func:`CopyLineAcross_DU` function",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Input Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Input Line   [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` containing a list of channel symbols, must be of INT"),
                   Parameter('p4', type="DB",
                             doc="Output Database"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Output Line  [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('CopyLineMasked_DU', module='geogxx', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Copy a line, prune items based on a mask channel",
               notes="""
               The input line's channel data is ReFidded to the mask
               channel, and then pruned from the output line data,
               based on the value of the VVU_PRUNE_XXX variable.
               For :def_val:`VVU_PRUNE_DUMMY`, only those items where the mask channel
               value is not a dummy are retained, while the complement
               is retained for VV_PRUNE_VALID.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Input  Line Symbol [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Mask Channel Symbol [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`VVU_PRUNE`"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Output Line Symbol [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('DAOTableNames_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Scans a DAO-compliant database and returns the table names in a :class:`VV`",
               notes="""
               The :class:`VV` must be created to hold strings of length
               :def_val:`STR_DB_SYMBOL`; i.e. use
               Creat_VV(-:def_val:`STR_DB_SYMBOL`, 0), or it will assert.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Database Type"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` to return names in")
               ]),

        Method('Decimate_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Copy and decimate a channel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Origin Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Destination Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Decimation factor")
               ]),

        Method('Diff_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate differences within a channel.",
               notes="""
               Differences with dummies result in dummies.
               An even number of differences locates data accurately.
               An odd number of differences locates result 1/2 element lower
               in the :class:`VV`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Origin Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Destination Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Number of differences")
               ]),

        Method('Distance_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a distance channel from X and Y.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Output Distance channel [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('Distance3D_DU', module='geogxx', version='8.1.0',
               availability=Availability.LICENSED, 
               doc="Create a distance channel from XY or XYZ with direction options.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Z channel [:def_val:`DB_LOCK_READONLY`] (can be :def_val:`NULLSYMB`)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`DU_DISTANCE_CHANNEL_TYPE`"),
                   Parameter('p7', type="DB_SYMB",
                             doc="Output Distance channel [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('Distline_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate cummulative distance for a line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Cummulative distance (retruned)")
               ]),

        Method('DupChanLocks_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Duplicate all channels protect-info from input :class:`DB`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Input Database handle"),
                   Parameter('p2', type="DB",
                             doc="Output Database handle.")
               ]),

        Method('DupChans_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Duplicate all channels from input :class:`DB`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Input Database handle"),
                   Parameter('p2', type="DB",
                             doc="Output Database handle.")
               ]),

        Method('EditDuplicates_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Edit duplicate readings at individual location",
               notes="""
               All the channels must be of the same fid incr/start and length.
               Protected channels are modified automatically.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel X, unlocked"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Channel Y, unlocked"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DB_DUP`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`DB_DUPEDIT`"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Fiducial number (required if :def_val:`DB_DUPEDIT_SINGLE`)")
               ]),

        Method('Export_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Export to a specific format.",
               notes="""
               For databases with both groups and lines:
               If both lines and groups are selected, save only the lines.
               If no lines are selected, (only groups), save the current line
               if it is (1) a group and (2) selected, else save the first selected
               group. ---
               Option to filter out data where one of the channels has a dummy in it.
               Option to allow a header with the channel names.
               
               The :def_val:`DU_CHANNELS_DISPLAYED` option can be used to export any selection of
               channels, listed by the symbols (DB_SYMB) values, cast to int values and
               stored in a :class:`VV`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DU_EXPORT`"),
                   Parameter('p3', type=Type.STRING,
                             doc="Current line"),
                   Parameter('p4', type="VV",
                             doc="list of channels - channel symbols stored as INT"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DU_CHANNELS`"),
                   Parameter('p6', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Write out dummies?"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Include a header with channel names?")
               ]),

        Method('Export2_DU', module='geogxx', version='5.1.6',
               availability=Availability.LICENSED, 
               doc="Like :func:`Export_DU`, but include line names as data.",
               notes="""
               See :func:`Export_DU`.
               The line names are printed as the first column of data exported.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DU_EXPORT`"),
                   Parameter('p3', type=Type.STRING,
                             doc="Current line"),
                   Parameter('p4', type="VV",
                             doc="list of channels - channel symbols stored as INT"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DU_CHANNELS`"),
                   Parameter('p6', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Write out dummies?"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Include a header with channel names?"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Include line names as data?")
               ]),

        Method('ExportAMIRA_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Export to database an AMIRA data file.",
               notes="""
               Other defined FIELDS stored in the database (see :func:`ImportAMIRA_DU` function)
               will be automatically included in the export
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="WA",
                             doc="AMIRA data file handle"),
                   Parameter('p3', type=Type.STRING,
                             doc="Single column channel names, supporting comma (,) separated names of multiple channels, maximum 32 channels"),
                   Parameter('p4', type=Type.STRING,
                             doc=":class:`VA` channel name, required"),
                   Parameter('p5', type=Type.STRING,
                             doc="Optional Time   channel name (must be :class:`VA` channel and same array size as above :class:`VA` channel)"),
                   Parameter('p6', type=Type.STRING,
                             doc="Optional Errors channel name (must be :class:`VA` channel and same array size as above :class:`VA` channel)"),
                   Parameter('p7', type=Type.STRING,
                             doc="Mandatory fields: DATATYPE"),
                   Parameter('p8', type=Type.STRING,
                             doc="UNITS"),
                   Parameter('p9', type=Type.STRING,
                             doc="CONFIG"),
                   Parameter('p10', type=Type.STRING,
                             doc="INSTRUMENT"),
                   Parameter('p11', type=Type.STRING,
                             doc="FREQUENCY")
               ]),

        Method('ExportAseg_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Export to ASEG-GDF format file(s).",
               notes="""
               At least one of the header file
               or data file names must be set. (Unset names will get the
               same file name, but with the extensions .dfn (header) or
               .dat (data).
               For databases with both groups and lines:
               If both lines and groups are selected, save only the lines.
               If no lines are selected, (only groups), save the current line
               if it is (1) a group and (2) selected, else save the first selected
               group. ---
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Current line"),
                   Parameter('p3', type="VV",
                             doc="Displayed channels"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DU_CHANNELS`"),
                   Parameter('p5', type=Type.STRING,
                             doc="header file name"),
                   Parameter('p6', type=Type.STRING,
                             doc="data file name")
               ]),

        Method('ExportAsegProj_DU', module='geogxx', version='5.0.1',
               availability=Availability.LICENSED, 
               doc="Export to ASEG-GDF format file(s) (supports projections).",
               notes="""
               At least one of the header file
               or data file names must be set. (Unset names will get the
               same file name, but with the extensions .dfn (header) or
               .dat (data).
               For databases with both groups and lines:
               If both lines and groups are selected, save only the lines.
               If no lines are selected, (only groups), save the current line
               if it is (1) a group and (2) selected, else save the first selected
               group. ---
               
               This version supports projections
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Current line"),
                   Parameter('p3', type="VV",
                             doc="Displayed channels"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DU_CHANNELS`"),
                   Parameter('p5', type=Type.STRING,
                             doc="export header file name"),
                   Parameter('p6', type=Type.STRING,
                             doc="export data file name"),
                   Parameter('p7', type=Type.STRING,
                             doc="export projection file name"),
                   Parameter('p8', type="IPJ",
                             doc="Projection handle")
               ]),

        Method('ExportChanCRC_DU', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Export a channel as XML and compute a CRC value.",
               notes="""
               The output file is an XML describing the channel. The
               CRC is of the channel data ONLY. To compute a CRC of the
               full channel (include metadata) do a CRC of the generated
               file.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="CRC Value returned"),
                   Parameter('p4', type=Type.STRING,
                             doc="File name to generate with XML")
               ]),

        Method('ExportCSV_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Export to a CSV file.",
               notes="""
               For databases with both groups and lines:
               If both lines and groups are selected, save only the lines.
               If no lines are selected, (only groups), save the current line
               if it is (1) a group and (2) selected, else save the first selected
               group. ---
               Option to filter out data where one of the channels has a dummy in it.
               Option to allow a header with the channel names.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Current line"),
                   Parameter('p3', type="VV",
                             doc="Displayed channels"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DU_CHANNELS`"),
                   Parameter('p5', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Write out dummies?"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Include a header with channel names?")
               ]),

        Method('ExportDatabaseCRC_DU', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Export a channel as XML and compute a CRC value.",
               notes="""
               The output file is an XML describing the channel. The
               CRC is of the channel data ONLY. To compute a CRC of the
               full channel (include metadata) do a CRC of the generated
               file.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="CRC Value returned"),
                   Parameter('p3', type=Type.STRING,
                             doc="File name to generate with XML")
               ]),

        Method('ExportGBN_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Export to a GBN data file.",
               notes="""
               The iDispChanList_DBE or :func:`iSymbList_DB` methods can be
               used to obtain a list of channels.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="VV",
                             doc="List of channels to export"),
                   Parameter('p3', type=Type.STRING,
                             doc="export data file name")
               ]),

        Method('ExportMDB_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Export to a Microsoft Access Database (MDB) file.",
               notes="""
               Similar to :func:`ExportGBN_DU`, with the addition that
               Groups go to individual tables, and lines go to
               a single table, or individual tables, based on the
               value of :def:`DU_LINEOUT`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Current line"),
                   Parameter('p3', type="VV",
                             doc="Displayed channels"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DU_CHANNELS`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DU_LINEOUT`"),
                   Parameter('p6', type=Type.STRING,
                             doc="export data file name")
               ]),

        Method('ExportGeodatabase_DU', module='geogxx', version='8.0.0',
               availability=Availability.LICENSED, 
               doc="Export to a ESRI Geodatabase file.",
               notes="""
               Similar to :func:`ExportGBN_DU`, with the addition that
               Groups go to individual tables, and lines go to
               a single table, or individual tables, based on the
               value of :def:`DU_LINEOUT`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Feature class name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Current line"),
                   Parameter('p4', type="VV",
                             doc="Displayed channels"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DU_CHANNELS`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`DU_FEATURE_TYPE_OUTPUT`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`DU_LINEOUT`"),
                   Parameter('p8', type=Type.STRING,
                             doc="export data file name")
               ]),

        Method('GetExistingFeatureClassesInGeodatabase_DU', module='geogxx', version='8.0.0',
               availability=Availability.LICENSED, 
               doc="Searches the geodatabases for an existing Feature class.",
               notes="Searches the geodatabases for an existing Feature class",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Feature class does not exist
               1 - Feature class exists
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="File geodatabase"),
                   Parameter('p3', type="LST",
                             doc="Feature class names to verify"),
                   Parameter('p4', type="VV",
                             doc="Output list of existing feature class names")
               ]),

        Method('ExportSHP_DU', module='geogxx', version='6.1.0',
               availability=Availability.LICENSED, 
               doc="Export to a shape file or files.",
               notes="""
               Similar to :func:`ExportMDB_DU`, with the addition that groups go to indiviual files
               with group name suffixes, and lines go to a single file, or multiple files
               with line name suffixes, based on the value of :def:`DU_LINEOUT`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Current line"),
                   Parameter('p3', type="VV",
                             doc="Displayed channels"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DU_CHANNELS`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DU_LINEOUT`"),
                   Parameter('p6', type=Type.STRING,
                             doc="export shape file name or base filename (shp assumed if no extension given)"),
                   Parameter('p7', type="LST",
                             doc=":class:`LST` object will be filled with shape files created")
               ]),

        Method('ExportXYZ_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Export XYZdata from a database to an XYZ file.",
               notes="""
               1. The export template can be in the local directory or the :class:`GEOSOFT`
               directory.  The import data file must include the path if it is not
               in the local directory.
               
               2. Both the import template and data file must exist.
               
               3. Sample Template file
               
               [EXPORT XYZ]
               EXPORT     CHAN {,FORMAT} {,WIDTH} {,DECIMAL}
               WRITEDUMMY YES
               CLIPMAP    YES
               MAXPOINTS  1000
               INCREMENT  .5
               
               4. This can be used to export a group, but the group must be the
               currently displayed line, and only that group will be exported.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="export data file name"),
                   Parameter('p3', type=Type.STRING,
                             doc="export template name")
               ]),

        Method('ExportXYZ2_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Export XYZdata from a database to an XYZ file, using file handles.",
               see_also=":func:`ExportXYZ_DU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="WA",
                             doc="export data file :class:`WA` handle"),
                   Parameter('p3', type="RA",
                             doc="export template file :class:`RA` handle")
               ]),

        Method('FFT_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Apply an :class:`FFT` to space data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="space Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="real Channel  [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="imaginary Channel [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('Filter_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Apply a convolution filter to a channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Input channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output filtered channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type="FILTER",
                             doc="Filter handle (:class:`FLT`)")
               ]),

        Method('GenLev_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Generate a Level table from an Intersection Table.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Input Table file Name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output Table file Name"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Max. gradient"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DU_LEVEL`")
               ]),

        Method('GenLevDB_DU', module='geogxx', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="Generate a Level table from an Intersection Database",
               notes="""
               Requires channels with the following names:
               
               ine, TFid, TZ, TDZ
               Line, LFid, LZ, LDZ
               Mask
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Input intersection database object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output Table File Name"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Max. gradient"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DU_LEVEL`")
               ]),

        Method('GenXYZTemp_DU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Generate default XYZ template for a XYZ file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="xyz file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template file name to create")
               ]),

        Method('GetXYZNumFields_DU', module='geogxx', version='9.1.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of fields in the XYZ file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="xyz file name"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="returned number of fields")
               ]),

        Method('GetChanDataLST_DU', module='geogxx', version='6.1.0',
               availability=Availability.LICENSED, 
               doc="Populate a :class:`LST` with unique items in a channel.",
               notes="""
               Items from all selected lines are collected,
               sorted, and duplicates removed. The output
               :class:`LST` name and value are set to the item values.
               Non-string channels are converted internally to
               string values using Copy_VV,
               so results may differ from what
               you may expect given the current channel's display
               width and number of decimals.
               If a mask channel is selected, then only those items
               where the mask channel is not a dummy are collected.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Data Channel"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Mask Channel  (can be :def_val:`NULLSYMB`)"),
                   Parameter('p4', type="LST",
                             doc=":class:`LST` object to populate")
               ]),

        Method('GetChanDataVV_DU', module='geogxx', version='6.1.0',
               availability=Availability.LICENSED, 
               doc="Populate a :class:`VV` with unique items in a channel.",
               notes="""
               Items from all selected lines are collected,
               sorted, and duplicates removed.
               The data is collected in the channel's data type,
               so normal :func:`Sort_VV` rules apply.
               If the output :class:`VV` and channel type are not the
               same, then the data is converted using the
               Copy_VV function, so see that for conversion rules.
               If a mask channel is selected, then only those items
               where the mask channel is not a dummy are collected.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Mask Channel  (can be :def_val:`NULLSYMB`)"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` object to populate")
               ]),

        Method('Gradient_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               This method takes 4 channels from input database and
               duplicats each line twice to output database)
               (input and Output can be the same channel).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database InPut"),
                   Parameter('p2', type="DB",
                             doc="DAtabase Output"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Input Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Input Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Z Input Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p6', type="DB_SYMB",
                             doc="G Input Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p7', type="DB_SYMB",
                             doc="X Output Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p8', type="DB_SYMB",
                             doc="Y Output Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p9', type="DB_SYMB",
                             doc="Z Output Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Angle"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Width")
               ]),

        Method('GravDrift_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate base loop closure and correct for drift.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line                    [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="date                    [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="local time (on date)    [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="reading                 [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p6', type="DB_SYMB",
                             doc="base                    [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p7', type="DB_SYMB",
                             doc="closure error           [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('GravTide_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate earth tide gravity correction.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line"),
                   Parameter('p3', type="DB_SYMB",
                             doc="lat  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="long [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="date [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p6', type="DB_SYMB",
                             doc="local time (on date) [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="GMT difference (added to time to give GMT)"),
                   Parameter('p8', type="DB_SYMB",
                             doc="calculated tide [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('GridLoad_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Load grid data to a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="IMG",
                             doc="grid img"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="X decimation factor"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Y decimation factor"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="0 trim leading/trailing dummies (default), 1 trim all dummies, 2 leave all dummies"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="flag for creating index channel: 0 no (default), 1 yes.")
               ]),

        Method('GridLoadXYZ_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Load grid data to a database using specified channels",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="IMG",
                             doc="grid img"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Channel"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Channel"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Z Channel"),
                   Parameter('p6', type="DB_SYMB",
                             doc="Data Channel"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="X decimation factor"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Y decimation factor"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="0 trim leading/trailing dummies (default), 1 trim all dummies, 2 leave all dummies"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="flag for creating index channel: 0 no (default), 1 yes.")
               ]),

        Method('Head_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Applies a heading correction.",
               notes="""
               Updates channel with Direction in degrees azimuth (counter-clockwise
               relative the +Y direction).
               :def_val:`GS_R8DM` if the line has no data, or if there is a
               problem.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line Symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="channel to correct [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="corrected channel  [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type="TB",
                             doc="heading table"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="line direction")
               ]),

        Method('IImportBIN3_DU', module='geogxx', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="Same as :func:`ImportBIN2_DU`, but returns the name of the imported line.",
               notes="""
               See :func:`ImportBIN2_DU`. Because the name of the created line is
               not necessarily the value passed in (and the value passed in
               can be blank), this version returns the name of the line
               to which the data is actually imported.
               """,
               see_also=":func:`ImportBIN2_DU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="import data file name"),
                   Parameter('p3', type=Type.STRING,
                             doc="import template name"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Optional Line name (on return, the actual line)"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Buffer size for line name"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Optional Flight number"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Optional date"),
                   Parameter('p8', type="WA")
               ]),

        Method('ImpCBPly_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Import concession boundary polygon file into a database",
               notes="The polygon file is provided by Ana Christina in Brasil.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="PJ",
                             doc="Projection Files Object"),
                   Parameter('p3', type=Type.STRING,
                             doc="import data file name"),
                   Parameter('p4', type="DB_SYMB",
                             doc="X channel handle"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Y channel handle")
               ]),

        Method('ImportADO_DU', module='geogxx', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Import an external database table into a group using ADO.",
               notes="""
               1. The import template can be in the local directory or the :class:`GEOSOFT`
               directory.
               
               2. Only the import template must be specified. The database connection string,
               the database table and Oasis line name are normally taken from the template
               file itself, but if these values are provided, they will override those found in the template.
               
               3. If the line already exists, the data will overwrite the existing data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="import database connection string       (overrides template value)"),
                   Parameter('p3', type=Type.STRING,
                             doc="imported table in database file (overrides template value)"),
                   Parameter('p4', type=Type.STRING,
                             doc="import template name"),
                   Parameter('p5', type=Type.STRING,
                             doc="Oasis montaj line name to create (overrides template value)")
               ]),

        Method('ImportAllADO_DU', module='geogxx', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Import an entire external database using ADO.",
               notes="""
               1. For group storage, the table names are imported "as is". For line storage,
               if the table names are valid Geosoft line names, they are used as is.
               Otherwise, line names will be created with type LINE_NORMAL, starting at
               L0 and incrementing by 10 (L10, L20 etc.)
               
               2. If the line exists, the data will overwrite the existing data.
               
               3. All tables and fields will be imported.
               
               4. If connection string is of type "FILENAME=..." the connection will attempt to resolve
               it as a file database. (see also ODBCFileConnect_GUI)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="import database connection string"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DU_STORAGE`")
               ]),

        Method('ImportAllDAO_DU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Import an entire external database using DAO.",
               notes="""
               1. The file is assumed to be a DAO compliant database.
               
               2. The import data file must include the path if it is not
               in the local directory.
               
               3. For group storage, the table names are imported "as is". For line storage,
               if the table names are valid Geosoft line names, they are used as is.
               Otherwise, line names will be created with type LINE_NORMAL, starting at
               L0 and incrementing by 10 (L10, L20 etc.)
               
               4. If the line exists, the data will overwrite the existing data.
               
               5. All tables and fields will be imported.
               
               6. The following are valid type strings for DAO:
               
               MSJET       : Microsoft Access
               ODBC        : ODBC source
               dBASE III
               dBASE IV
               dBASE 5
               FoxPro 2.0
               FoxPro 2.5
               FoxPro 2.6
               Paradox 3.x
               Paradox 4.x
               Paradox 5.x
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="import data file name"),
                   Parameter('p3', type=Type.STRING,
                             doc="database type"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DU_STORAGE`")
               ]),

        Method('ImportAMIRA_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Import an AMIRA data file.",
               notes="""
               All the constant declarations are stored within the database
               under \\TEM\\CONSTANTS. The format is as follows:
               
               1. Lines stored in the file beginning with "/" are comments
               2. Each constant occupies a line in the file. It uses the format:
               CONSTANT=VALUE
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="RA",
                             doc="AMIRA data file handle"),
                   Parameter('p3', type="WA",
                             doc="Log file handle")
               ]),

        Method('ImportAseg_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Import an ASEG-GDF data file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="template file name"),
                   Parameter('p3', type=Type.STRING,
                             doc="header file name"),
                   Parameter('p4', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p5', type=Type.STRING,
                             doc="Flight Line Channel name"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Number of channels to import at one time")
               ]),

        Method('ImportAsegProj_DU', module='geogxx', version='5.0.1',
               availability=Availability.LICENSED, 
               doc="Import an ASEG-GDF data file (supports projections).",
               notes="This version supports projections",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="template file name"),
                   Parameter('p3', type=Type.STRING,
                             doc="header file name"),
                   Parameter('p4', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p5', type=Type.STRING,
                             doc="Flight Line Channel name"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Number of channels to import at one time"),
                   Parameter('p7', type=Type.STRING,
                             doc="projection file name"),
                   Parameter('p8', type=Type.STRING,
                             doc="Channel pair to associate projection"),
                   Parameter('p9', type=Type.STRING,
                             doc="Channel pair to associate projection")
               ]),

        Method('ImportBIN_DU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Import blocked binary or archive ASCII data",
               notes="""
               1. Binary import templates have extension .I2 by convention.  See
               BINARY.I2 for a description of the template format.
               Archive import templates have extension .I3 by convention. See
               ARCHIVE.I3 for a description of the template format.
               
               2. Both the import template and data file must exist.
               
               3. If a line already exists in the database, a new version is created
               unless a line name is passed in.  In this case, the specified name
               is used and the imported channels on the previous line will be
               destroyed.
               """,
               see_also=":func:`LabTemplate_DU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="import data file name"),
                   Parameter('p3', type=Type.STRING,
                             doc="import template name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Optional Line name (see note 3.)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Optional Flight number"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Optional date")
               ]),

        Method('ImportBIN2_DU', module='geogxx', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Import blocked binary or archive ASCII data with data error display",
               notes="""
               1. Binary import templates have extension .I2 by convention.  See
               BINARY.I2 for a description of the template format.
               Archive import templates have extension .I3 by convention. See
               ARCHIVE.I3 for a description of the template format.
               
               2. Both the import template and data file must exist.
               
               3. If a line already exists in the database, a new version is created
               unless a line name is passed in.  In this case, the specified name
               is used and the imported channels on the previous line will be
               destroyed.
               """,
               see_also=":func:`LabTemplate_DU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="import data file name"),
                   Parameter('p3', type=Type.STRING,
                             doc="import template name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Optional Line name (see note 3.)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Optional Flight number"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Optional date"),
                   Parameter('p7', type="WA")
               ]),

        Method('ImportBIN4_DU', module='geogxx', version='9.1.0',
               availability=Availability.PUBLIC, 
               doc="Same as :func:`ImportBIN2_DU` but with an import mode",
               notes="Same as :func:`ImportBIN2_DU` but with an import mode",
               see_also=":func:`ImportBIN2_DU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DU_IMPORT`"),
                   Parameter('p3', type=Type.STRING,
                             doc="import data file name"),
                   Parameter('p4', type=Type.STRING,
                             doc="import template name"),
                   Parameter('p5', type=Type.STRING,
                             doc="Optional Line name (see note 3.)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Optional Flight number"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Optional date"),
                   Parameter('p8', type="WA")
               ]),

        Method('ImportDAARC500Serial_DU', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Import Serial data from the RMS Instruments DAARC500.",
               notes="""
               Imports data stored in a serial channel recorded
               by the RMS Instruments DAARC500 instrument, and outputs the data to
               a line in the database. The channels created depend on the input data type
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Output line (:def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of file to import"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Channel to import, 1-8"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`GU_DAARC500_DATATYPE`")
               ]),

        Method('ImportDAARC500SerialGPS_DU', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="Import Serial GPS data from the RMS Instruments DAARC500.",
               notes="""
               Imports GPS data stored in a serial channel recorded
               by the RMS Instruments DAARC500 instrument, and outputs the data to
               a line in the database. Makes the following channels:
               
               Fid, UTC_Time, Latitude, Longitude, Altitude, GPS_Quality,
               NumSat (Number of satellites), GPS_HDOP (Horizontal Dilution of Position),
               Undulation, GPS_DiffAge (Age of differential channel).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Output line (:def_val:`DB_LOCK_READWRITE`)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of file to import"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Channel to import, 1-8")
               ]),

        Method('ImportDAO_DU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Import an external database table into a group using DAO.",
               notes="""
               1. The import template can be in the local directory or the :class:`GEOSOFT`
               directory.  The import data file must include the path if it is not
               in the local directory.
               
               2. Only the import template must be specified. The database file name,
               file type, the database table and Oasis line name are normally
               taken from the template file itself, but if these values are provided,
               they will override those found in the template.
               
               3. If the line already exists, the data will overwrite the existing data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="import database file name   (overrides template value)"),
                   Parameter('p3', type=Type.STRING,
                             doc="import data file type       (overrides template value)"),
                   Parameter('p4', type=Type.STRING,
                             doc="imported table in database file (overrides template value)"),
                   Parameter('p5', type=Type.STRING,
                             doc="import template name"),
                   Parameter('p6', type=Type.STRING,
                             doc="Oasis Montaj line name to create (overrides template value)")
               ]),

        Method('ImportESRI_DU', module='geogxx', version='7.1.0',
               availability=Availability.PUBLIC, 
               doc="Import an ArcGIS Geodatabase table or feature class into a GDB group",
               notes="""
               1. The import template can be in the local directory or the :class:`GEOSOFT`
               directory.
               
               2. Only the import template must be specified. The Geodatabase connection string
               and Oasis line name are normally taken from the template file itself,
               but if these values are provided, they will override those found in the template.
               
               3. If the line already exists, the data will overwrite the existing data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc='import database connection string (e.g. "d:\\Personal\\test.mdb|Table" or "d:\\File\\test.gdb|FeatureClass, overrides template value)'),
                   Parameter('p3', type=Type.STRING,
                             doc="import template name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Oasis montaj line name to create (overrides template value)")
               ]),

        Method('ImportGBN_DU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Import GBN data file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="File name of the GBN file to import")
               ]),

        Method('ImportODDF_DU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Import ODDF data file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="File name of the ODDF file to import")
               ]),

        Method('ImportPico_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Import a Picodas data file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="template file name"),
                   Parameter('p3', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Number of channels to import at one time")
               ]),

        Method('ImportUBCModMsh_DU', module='geogxx', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Import UBC Mod and Msh files.",
               notes="""
               Each slice in X,Y or Z is imported to its own line in the database
               beginning with L0.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Mesh file"),
                   Parameter('p3', type=Type.STRING,
                             doc='1-5 Mod files, delimited with "|"'),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Import slice direction (0-2 for X,Y and Z)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Value to interpret as dummy")
               ]),

        Method('ImportUSGSPost_DU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Import USGS Post data file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="File name of the USGS post file to import")
               ]),

        Method('ImportXYZ_DU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Import XYZ data into the database.",
               notes="""
               1. The import template can be in the local directory or the :class:`GEOSOFT`
               directory.  The import data file must include the path if it is not
               in the local directory.
               
               2. Both the import template and data file must exist.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DU_IMPORT`"),
                   Parameter('p3', type=Type.STRING,
                             doc="import data file name"),
                   Parameter('p4', type=Type.STRING,
                             doc="import template name")
               ]),

        Method('ImportXYZ2_DU', module='geogxx', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Import XYZ data into the database.",
               notes="""
               1. The import template can be in the local directory or the :class:`GEOSOFT`
               directory.  The import data file must include the path if it is not
               in the local directory.
               
               2. Both the import template and data file must exist.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DU_IMPORT`"),
                   Parameter('p3', type=Type.STRING,
                             doc="import data file name"),
                   Parameter('p4', type=Type.STRING,
                             doc="import template name"),
                   Parameter('p5', type="WA")
               ]),

        Method('ImportIoGAS_DU', module='geogxx', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Import data columns from an ioGAS data file.",
               notes="""
               1. All columns in the speficied ioGAS data file will be imported.
               2. If a line already exists, the data will overwrite the existing data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.STRING,
                             doc="Input data.csv file name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Input template file name")
               ]),

        Method('IndexOrder_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Change the order of a channel using an index channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="ordered index channel (should be int) [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="channel to reorder [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('Interp_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Replace all dummies by interpolating from valid data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel to interpolate [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output interpolated channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DU_INTERP`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`DU_INTERP_EDGE`")
               ]),

        Method('InterpGap_DU', module='geogxx', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Replace all dummies by interpolating from valid data.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel to interpolate [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output interpolated channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DU_INTERP`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`DU_INTERP_EDGE`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Maximum gap to interpolate (fiducials)"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Maximum items to extend at ends.")
               ]),

        Method('Intersect_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create Tie Line & Normal Line intersect table.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Y Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Z Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Intersection tolerance"),
                   Parameter('p6', type=Type.STRING,
                             doc="Output Table file Name")
               ]),

        Method('IntersectAll_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create line intersect table from all lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Y Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Z Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Intersection tolerance"),
                   Parameter('p6', type=Type.STRING,
                             doc="Output Table file Name")
               ]),

        Method('IntersectGDBtoTBL_DU', module='geogxx', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="Create a new intersection table from an intersection database.",
               notes="If the TBL exists, it is overwritten.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input Intersection Database name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output intersection TBL")
               ]),

        Method('IntersectOld_DU', module='geogxx', version='5.1.4',
               availability=Availability.LICENSED, 
               doc="Use existing intersection table and re-calculate miss-ties.",
               notes="""
               Reads intersection information from an existing intersect
               table and looks up the values at the intersections for the
               input Z channel. This makes it unnecessary to re-calculate
               the intersections every time if you want to determine
               miss-ties using different Z channels, or the same Z channel
               after processing levelling corrections. Existing intersections
               whose locations do not exist in the database are ignored.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Y Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Z Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type=Type.STRING,
                             doc="Input Table file name"),
                   Parameter('p6', type=Type.STRING,
                             doc="Output Table file Name")
               ]),

        Method('IntersectTBLtoGDB_DU', module='geogxx', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="Create a new intersection database from an intersection table.",
               notes="""
               If the GDB exists, it is deleted, so it should not
               be loaded.
               The database is split by Tie lines (or whatever lines are found in column 3
               of the TBL file.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input intersection TBL"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output Intersection Database name")
               ]),

        Method('LabTemplate_DU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Makes a default template from a lab assay file.",
               notes="""
               The template can be used to import the file using
               sImportBIN_DU.
               
               The first column is assumed to be the sample number.
               
               If the unit label line is the same as the column label
               line, column labels are assummed to be followed by
               unit labels using the format "Au-ppm", "Au ppm" or
               "Au(ppm)".
               
               The number of channels is determined from the number of
               columns in the data channel.  If there are more column
               labels or unit labels, the last labels are assumed to
               be correct.  If there are fewer line labels, default
               labels "Col_n", where n is the column number, will be
               created and no unit labels will be defined.
               """,
               see_also=":func:`ImportBIN_DU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="new template name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DU_LAB_TYPE`"),
                   Parameter('p4', type=Type.STRING,
                             doc="delimiter string"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Offset to column labels line (0 for first line)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Offset to unit labels line, -1 if none"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Offset to first line that contains data"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Sample channel element type, recommend -10 for 10-character ASCII, or :def_val:`GS_LONG` for numbers."),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Default channel element type, recommend :def_val:`GS_FLOAT`")
               ]),

        Method('LoadGravity_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Load a gravity survey file",
               notes="""
               See GRAVITY.:class:`DAT` for a description of the file format.
               
               Existing data in the line will be replaced.
               
               The following :class:`REG` parameters will be set if they appear
               in the data file:
               default
               OPERATOR             ""
               DATE                 none
               INSTRUMENT           ""
               INSTRUMENT_SCALE     "1.0"
               BASE_GRAVITY         "0.0"
               FORMULA              "1967"
               GMT_DIFF             "0.0"
               DISTANCE_UNITS       "m"
               DENSITY_EARTH        "2.67"
               DENSITY_WATER        "1.0"
               DENSITY_ICE          "0.95"
               MAP_PROJECTION       ""
               
               If the corresponding constant is not specified and the
               :class:`REG` already has the constant defined, it is not changed.
               If the constant is not defined and it is not already in
               the :class:`REG`, the indicated default will be set.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="REG",
                             doc=":class:`REG` to hold constant data"),
                   Parameter('p3', type="DB_SYMB",
                             doc="line in which to load data"),
                   Parameter('p4', type=Type.STRING,
                             doc="gravity data file")
               ]),

        Method('LoadLTB_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Load :class:`LTB` into a database line.",
               notes="""
               A new channel will be created for all :class:`LTB` fields
               that do not already exist.
               The :class:`LTB` field type will be double if all entries can be
               converted to double, otherwise it will be a string type
               set to the larger of 16 characters or the longest string
               in the field.
               
               For _APPEND, the :class:`LTB` data is simply added the end of each
               channel.  :func:`ReFidAllCh_DU` can be used to re-fid data to
               match a specifc channel and there-by case all channels to be
               the same length before appending data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line"),
                   Parameter('p3', type="LTB",
                             doc="table"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DU_LOADLTB`")
               ]),

        Method('MakeFid_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Make a fiducial channel based on an existing channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line Symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="base channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="new fiducial channel [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('Mask_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Mask dummies in one channel against another.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel to mask [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Mask channel [:def_val:`DB_LOCK_READONLY`]")
               ]),

        Method('Math_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Apply an expression to the database",
               notes="""
               The MATH_DU method will READWRITE lock channels on the left
               side of expressions and READONLY lock channels on the right
               side of expressions.  Channels are unlocked before returning.
               Therefore, channels on the left side of an expression cannot
               be locked READONLY because the :func:`Math_DU` attempt to lock the
               channel READWRITE will fail.  Similarly, channels on the right
               side of an expression cannot be locked READWRITE because
               :func:`Math_DU`'s attempt to lock the channels READONLY will fail.
               
               If this is confusing, just make sure no channels used in the
               expression are locked before calling :func:`Math_DU`.
               """,
               see_also=":class:`EXP`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line handle"),
                   Parameter('p3', type="EXP",
                             doc="math expression object (:class:`EXP`)")
               ]),

        Method('MergeLine_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Merge a line a the fiducial and copies any data past
               that fiducial into the new line.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Input Line1 [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Input Line2 [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output Line [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DU_MERGE`")
               ]),

        Method('ModFidRange_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Insert/Append/Delete a range of fids.",
               notes="""
               Channels that do not have the same fid start or fid
               increment are not processed.
               
               Protected channels are modified automatically.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="base fid start"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="base fid increment"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="start index (can be negative)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="number of fids"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`DU_MODFID`")
               ]),

        Method('Move_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Move/correct a channel to a control channel.",
               notes="""
               The input channel is moved to the absolute location
               of the control channel.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle to Apply this to"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Input channel   [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Control channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Result channel  [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`DU_MOVE`")
               ]),

        Method('NLFilt_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               This method applies a non-linear filter to the specified
               line/channel and places the output in the output channel.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel to filter [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Output filtered channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Filter Width"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Filter Tolerance, 0 for 10% of Std. Dev.")
               ]),

        Method('Normal_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Set fid of all channels to match a specified channel.",
               see_also=":func:`ReFidAllCh_DU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Base Channel for normalization.  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Ignore write protection on channels? :def:`GEO_BOOL`")
               ]),

        Method('PolyFill_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Fill using a polygon with a value of 1.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Channel to fill [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type="PLY",
                             doc="Polygon Object to use"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`DU_FILL`")
               ]),

        Method('PolyMask_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Mask against a polygon.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Channel to mask [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type="PLY",
                             doc="Polygon Object to use"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`DU_MASK`")
               ]),

        Method('ProjectData_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Project X,Y channels",
               notes="Output channels can be the same as input channels",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle to project"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Input Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Input Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="X Output Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type="DB_SYMB",
                             doc="Y Output Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p7', type="PJ",
                             doc="Projection object to Apply")
               ]),

        Method('ProjectXYZ_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Project X,Y,Z channels from one system to another.",
               notes="Output channels can be the same as input channels",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle to project"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Input Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Input Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Z Input Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p6', type="DB_SYMB",
                             doc="X Output Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p7', type="DB_SYMB",
                             doc="Y Output Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p8', type="DB_SYMB",
                             doc="Z Output Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p9', type="PJ",
                             doc="Projection object to Apply")
               ]),

        Method('ProjPoints_DU', module='geogxx', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Project X,Y(Z) channels with different projections",
               notes="Output channels can be the same as input channels",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle to project"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Input Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Input Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Z Input Channel  [:def_val:`DB_LOCK_READONLY`] (can be DB_NULL_SYMB)"),
                   Parameter('p6', type="DB_SYMB",
                             doc="X Output Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p7', type="DB_SYMB",
                             doc="Y Output Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p8', type="DB_SYMB",
                             doc="Z Output Channel [:def_val:`DB_LOCK_READWRITE`] (can be DB_NULL_SYMB)"),
                   Parameter('p9', type="DB_SYMB",
                             doc="Input Name Channel   [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p10', type="DB_SYMB",
                             doc="Input Datum Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p11', type="DB_SYMB",
                             doc="Input Method Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p12', type="DB_SYMB",
                             doc="Input Unit Channel   [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p13', type="DB_SYMB",
                             doc="Input Local Datum Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p14', type="DB_SYMB",
                             doc="Output Name Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p15', type="DB_SYMB",
                             doc="Output Datum Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p16', type="DB_SYMB",
                             doc="Output Method Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p17', type="DB_SYMB",
                             doc="Output Unit Channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p18', type="DB_SYMB",
                             doc="Output Local Datum Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p19', type="DB_SYMB",
                             doc="Error Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p20', type=Type.INT32_T,
                             doc="Force Local Datum Shifts?")
               ]),

        Method('QCInitSeparation_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Creates the nearest line channels for line separation QC.",
               notes="""
               This must be called before QCSeparation_DU. It uses a pager to
               establish the relative positions of the selected lines, then,
               for every point determines the closest point in another line to
               the left and to the right (as determined by looking in the
               direction of the line.) These distances are stored to two new
               channels in the database, "Closest_Left" and "Closest_Right"
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Nominal Line separation"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Nominal Line direction")
               ]),

        Method('QCSurveyPlan_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a database containing proposed survey plan in a :class:`PLY`",
               notes="""
               The LINE on which has the reference (X,Y) will have the starting Line number
               The lines on the right hand side of the reference line (while looking
               into azimuth of ref. line) have increasing line numbers. The lines
               on the left hand side have the decreasing line numbers from the starting
               number. Returns an error code or 0 (if successful)
               """,
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database to save proposed survey plan"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` to save survey plan summary"),
                   Parameter('p3', type="PLY",
                             doc="Boundary :class:`PLY`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Survey line spacing"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Survey line azimuth"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Survey line reference X coordinate"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Survey line reference Y coordinate"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Survey line starting number of LINES"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Line number increment for survey line"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Tie line spacing"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Tie line azimuth"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="Tie line reference X coordinate"),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Tie line reference Y coordinate"),
                   Parameter('p14', type=Type.INT32_T,
                             doc="Tie line starting number of LINES"),
                   Parameter('p15', type=Type.INT32_T,
                             doc="Line number increment for Tie line"),
                   Parameter('p16', type=Type.INT32_T,
                             doc=":def:`QC_PLAN_TYPE`"),
                   Parameter('p17', type=Type.DOUBLE,
                             doc="Sample spacing (spacing between points in lines)"),
                   Parameter('p18', type=Type.DOUBLE,
                             doc="Spacing to extend lines outside polygon")
               ]),

        Method('rDirection_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Returns the direction of a line.",
               notes="""
               The direction is calculated from the first and last
               non-dummy locations in the X and Y reference channels.
               """,
               return_type=Type.DOUBLE,
               return_doc="""
               direction in degrees azimuth (clockwise relative
               the +Y direction).
               :def_val:`GS_R8DM` if the line has no data, or if there is a
               problem.  Problems will register errors.
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X reference channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y reference channel [:def_val:`DB_LOCK_READONLY`]")
               ]),

        Method('ReFid_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Re-fid a channel based on a reference channel",
               notes="""
               The original channel can be an array channel, in which case
               the columns (up to the number of columns available in the output)
               are individually interpolated. If the number of
               columns in the output channel is more than the input channel,
               the remaining columns are dummied.
               
               This function is fundamentally different in behaviour from :func:`ReFidCh_DU`.
               The values in the Reference channel in :func:`ReFid_DU` are the "X" locations
               corresponding to the "Y" locations in the "Original Channel". Output
               Channel values are calculated at the new "X" locations specified by
               the Start Fid and the Fid Increment.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc='Original Channel [:def_val:`DB_LOCK_READONLY`]  "Y" values'),
                   Parameter('p4', type="DB_SYMB",
                             doc='Reference Channel [:def_val:`DB_LOCK_READONLY`] "X" locations'),
                   Parameter('p5', type="DB_SYMB",
                             doc="Output Channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`DU_REFID`"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Start Fid, if :def_val:`GS_R8DM`, use ref channel minimum"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Fid increment, if :def_val:`GS_R8DM` use nominal spacing of the reference channel."),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Maximum gap to interpolate across")
               ]),

        Method('ReFidAllCh_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Simple re-fid of all channels based on a reference channel",
               notes="""
               Channels can be array channels, in which case
               the columns are individually re-fidded.
               """,
               see_also=":func:`Normal_DU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Reference Channel [:def_val:`DB_LOCK_READONLY`]")
               ]),

        Method('ReFidCh_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Simple re-fid of a channel based on a reference channel",
               notes="""
               The original channel can be an array channel, in which case
               the columns are individually re-fidded.
               
               :func:`ReFidCh_DU` resamples the "Channel to refid" to the "Reference Channel" Fid
               range and increment.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Reference Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Channel to refid  [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('Rotate_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Rotate coordinates.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="input X channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="input Y channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="output X channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type="DB_SYMB",
                             doc="output Y channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="X point about which to rotate"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Y of point about which to rotate"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="angle in degrees CCW")
               ]),

        Method('SampleGD_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Sample a :class:`GD` at a specified X and Y.",
               notes="Values in result channel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle to sample"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Input Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Input Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Z Output Channel sampled from :class:`GD` [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type="GD",
                             doc="Grid handle")
               ]),

        Method('SampleIMG_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Sample a :class:`IMG` at a specified X and Y.",
               notes="Values in result channel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle to sample"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Input Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Input Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Z Output Channel sampled from :class:`IMG` [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type="IMG",
                             doc=":class:`IMG` handle")
               ]),

        Method('SampleIMGLineLST_DU', module='geogxx', version='8.3.0',
               availability=Availability.LICENSED, 
               doc="Sample an :class:`IMG` at a specified X and Y, for a :class:`LST` of lines.",
               notes="Values in result channel",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` of (Line Name, Line Handle) values to sample"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Input Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Input Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Z Output Channel sampled from :class:`IMG` [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type="IMG",
                             doc=":class:`IMG` handle")
               ]),

        Method('ScanADO_DU', module='geogxx', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Scans an external ADO database and generates a default template.",
               notes="All the channels are listed",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database connection string"),
                   Parameter('p2', type=Type.STRING,
                             doc="Database Table Name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Template file name to Create")
               ]),

        Method('ScanAseg_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               This method scans an ASEG-GDF file and generates a default
               template listing all the channels and all the ALIAS lines.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="header file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Flight Line Channel name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Template file name to Create")
               ]),

        Method('ScanDAO_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Scans an external DAO database and generates a default template.",
               notes="All the channels are listed",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Database Type"),
                   Parameter('p3', type=Type.STRING,
                             doc="Database Table Name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Template file name to Create")
               ]),

        Method('ScanPico_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               This method scans a picodas file and generates a default
               template listing all the channels and all the ALIAS lines.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Data file Name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Template file name to Create")
               ]),

        Method('Sort_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Sort the contents of a channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="channel to sort [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DU_SORT`")
               ]),

        Method('SortIndex_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create an ordered index of the contents of a channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="channel to sort [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="output index channel (should be int) [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`DU_SORT`")
               ]),

        Method('SortIndex2_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create an ordered index from two channels",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line symbol"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Sort by this channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`DU_SORT`"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Then by this channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`DU_SORT`"),
                   Parameter('p7', type="DB_SYMB",
                             doc="output index channel (should be int) [:def_val:`DB_LOCK_READWRITE`]")
               ]),

        Method('SplitLine_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Splits a line a the fiducial and copies any data past
               that fiducial into the new line.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Input Line, will be reduced at fid  [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Output Line, will take data above fid [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Fid number of split")
               ]),

        Method('SplitLine2_DU', module='geogxx', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="""
               Splits a line a the fiducial and copies any data past
               that fiducial into the new line.
               """,
               notes="The same as SplitLine, but with an option to reset each line's starting fiducial to zero.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Input Line, will be reduced at fid  [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Output Line, will take data above fid [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Fid number of split"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Reset starting fiducials to zero (0: No, 1: Yes)")
               ]),

        Method('SplitLineXY_DU', module='geogxx', version='8.3.0',
               availability=Availability.LICENSED, 
               doc="""
               Break up a line based on tolerance of lateral and horizontal distance, with
               options for the output line names.
               """,
               notes="The original line will be deleted.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel X [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Channel Y [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Line direction, 0-any, 1-X, 2-Y."),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Lateral tolerance, DUMMY for the default (10% of the separation between the first two points."),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Downline Tolerance, DUMMY for none"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`DU_SPLITLINE`"),
                   Parameter('p9', type=Type.INT32_T, is_ref=True,
                             doc="First line in the sequence, for :def_val:`DU_SPLITLINE_SEQUENTIAL`. On return, the next line in the sequence."),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Increment in the line number sequence, for :def_val:`DU_SPLITLINE_SEQUENTIAL`")
               ]),

        Method('SplitLineXY2_DU', module='geogxx', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="""
               Break up a line based on tolerance of lateral and horizontal distance, with
               options for the output line names.
               """,
               notes="The same as SplitLineXY, but with an option to reset each line's starting fiducial to zero.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel X [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Channel Y [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Line direction, 0-any, 1-X, 2-Y."),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Lateral tolerance, DUMMY for the default (10% of the separation between the first two points."),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Downline Tolerance, DUMMY for none"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`DU_SPLITLINE`"),
                   Parameter('p9', type=Type.INT32_T, is_ref=True,
                             doc="First line in the sequence, for :def_val:`DU_SPLITLINE_SEQUENTIAL`. On return, the next line in the sequence."),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Increment in the line number sequence, for :def_val:`DU_SPLITLINE_SEQUENTIAL`"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="Reset starting fiducials to zero (0: No, 1: Yes)")
               ]),

        Method('SplitLineXY3_DU', module='geogxx', version='9.0.0',
               availability=Availability.LICENSED, 
               doc="""
               Break up a line based on tolerance of lateral and horizontal distance, with
               options for the output line names.
               """,
               notes="The same as SplitLineXY2, but with the option to maintain line types when outputting sequentially numbered lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel X [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Channel Y [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Line direction, 0-any, 1-X, 2-Y."),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Lateral tolerance, DUMMY for the default (10% of the separation between the first two points."),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Downline Tolerance, DUMMY for none"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`DU_SPLITLINE`"),
                   Parameter('p9', type=Type.INT32_T, is_ref=True,
                             doc="First line in the sequence, for :def_val:`DU_SPLITLINE_SEQUENTIAL`. On return, the next line in the sequence."),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Increment in the line number sequence, for :def_val:`DU_SPLITLINE_SEQUENTIAL`"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="Maintain line types for :def_val:`DU_SPLITLINE_SEQUENTIAL`  (0: No, 1: Yes)"),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Reset starting fiducials to zero (0: No, 1: Yes)")
               ]),

        Method('SplitLineByDirection_DU', module='geogxx', version='8.5.0',
               availability=Availability.LICENSED, 
               doc="""
               The line is split when the heading (calculated from the current X and Y channels) changes by more than a specified amount over
               a specified distance. Additional options to discard too-short lines
               """,
               notes="Split a line based on changes in heading.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READWRITE`]."),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Channel [:def_val:`DB_LOCK_READWRITE`]."),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Maximum angular change allowed (degrees)..."),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="...over a distance of"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Delete lines shorter than (can be :def_val:`rDUMMY`)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Break on data XY separation greater than (can be :def_val:`rDUMMY`)"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="GEO_BOOLGS_TRUE to save too-short segments as special lines, :def_val:`GS_FALSE` to discard"),
                   Parameter('p10', type=Type.INT32_T,
                             doc=":def:`DU_SPLITLINE` ONLY DU_SPLITLINEXY_SEQUENTIAL and DU_SPLITLINEXY_VERSIONS"),
                   Parameter('p11', type=Type.INT32_T, is_ref=True,
                             doc="First line in the sequence, for :def_val:`DU_SPLITLINE_SEQUENTIAL`. On return, the next line in the sequence."),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Increment in the line number sequence, for :def_val:`DU_SPLITLINE_SEQUENTIAL`"),
                   Parameter('p13', type=Type.INT32_T,
                             doc="Reset starting fiducials to zero (0: No, 1: Yes)")
               ]),

        Method('SplitLineByDirection2_DU', module='geogxx', version='9.0.0',
               availability=Availability.LICENSED, 
               doc="The same as SplitLineByDirection, but with the option to maintain line types when outputting sequentially numbered lines.",
               notes="Split a line based on changes in heading.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READWRITE`]."),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Channel [:def_val:`DB_LOCK_READWRITE`]."),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Maximum angular change allowed (degrees)..."),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="...over a distance of"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Delete lines shorter than (can be :def_val:`rDUMMY`)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Break on data XY separation greater than (can be :def_val:`rDUMMY`)"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="GEO_BOOLGS_TRUE to save too-short segments as special lines, :def_val:`GS_FALSE` to discard"),
                   Parameter('p10', type=Type.INT32_T,
                             doc=":def:`DU_SPLITLINE` ONLY DU_SPLITLINEXY_SEQUENTIAL and DU_SPLITLINEXY_VERSIONS"),
                   Parameter('p11', type=Type.INT32_T, is_ref=True,
                             doc="First line in the sequence, for :def_val:`DU_SPLITLINE_SEQUENTIAL`. On return, the next line in the sequence."),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Increment in the line number sequence, for :def_val:`DU_SPLITLINE_SEQUENTIAL`"),
                   Parameter('p13', type=Type.INT32_T,
                             doc="Maintain line types for :def_val:`DU_SPLITLINE_SEQUENTIAL`  (0: No, 1: Yes)"),
                   Parameter('p14', type=Type.INT32_T,
                             doc="Reset starting fiducials to zero (0: No, 1: Yes)")
               ]),

        Method('Stat_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Add a data channel to a statistics object.",
               notes="""
               If the input channel is a :class:`VA` (array) channel, then the columns set using
               :func:`SetVAWindows_DB`() are used in the statistics; all columns are used by default.
               """,
               see_also=":class:`ST`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel handle [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="ST",
                             doc="Statistics handle")
               ]),

        Method('TableLineFid_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Place a Line/Fid information into a Channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Output channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Reference channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="TB",
                             doc="Table to Use"),
                   Parameter('p5', type="TB_FIELD",
                             doc="Table field wanted")
               ]),

        Method('TableSelectedLinesFid_DU', module='geogxx', version='9.1.0',
               availability=Availability.LICENSED, 
               doc="Place a Line/Fid information into a Channel for the selected lines in the database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Output channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Reference channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="TB",
                             doc="Table to Use"),
                   Parameter('p5', type="TB_FIELD",
                             doc="Table field wanted")
               ]),

        Method('TimeConstant_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate TEM time constant (Tau)",
               notes="""
               When DU_TIME_LOG option is used, Time channel will be converted
               with logarithmic before calculating time constant.
               Logarthmic conversion is always applied to the response channel.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database, required"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle, required"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Response channel, required [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Time channel, required [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Output Time constant (Tau) channel, required [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p6', type="DB_SYMB",
                             doc="Output Intercept channel, no output if :def_val:`NULLSYMB` [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p7', type="DB_SYMB",
                             doc="Output predicted response channel, no output if :def_val:`NULLSYMB` [:def_val:`DB_LOCK_READWRITE`] Result is based on least square fit from Tau and Intercept"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Log option applied to time channel: 0 - linear, 1 - log10")
               ]),

        Method('Trend_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculates an n'th order trend of a data channel.",
               see_also=":func:`BSpline_DU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle to Apply this to"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Input channel  [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Result channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Trend Order, 0 to 9")
               ]),

        Method('UpdateIntersectDB_DU', module='geogxx', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="Update the Z and DZ values in an intersection database, using the current database.",
               notes="""
               Updates the TZ, TDZ, LZ and LDZ channels at the intersections,
               using the current flight database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Flight Database Object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READONLY`] (for location info)"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Z Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB",
                             doc="Intersection database to update")
               ]),

        Method('VoxelSection_DU', module='geogxx', version='6.4.0',
               availability=Availability.LICENSED, 
               doc="Slice a voxel to a grid under a database line.",
               notes="""
               Takes the first and XY locations in a line (using the
               current X and Y channels) and defines a section grid
               as a slice through a voxel file.
               The grid cell sizes can be left as :def_val:`GS_R8DM`, in which
               case an attempt will be made to match the voxel cell
               size, based on the line azimuth, voxel rotation, etc.
               
               If the slice does NOT intersect the voxel, or if
               there are fewer than 2 valid locations in the line,
               then no grid file is created, but there is no error.
               (This is to simplify creating multiple grids from
               at once, where not all may intersect).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Input  Line Symbol [READWRITE]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Channel (DB_NO_SYMB if LineDir==0)"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Channel (DB_NO_SYMB if LineDir==0)"),
                   Parameter('p5', type="VOX",
                             doc="Voxel to slice"),
                   Parameter('p6', type=Type.STRING,
                             doc="Output grid name"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="X cell size (horizontal)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Y cell size (vertical)"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Interp: 1 - linear, 0 - nearest")
               ]),

        Method('WriteWA_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Write data to an ASCII file.",
               notes="""
               Channels to be written should be placed in a :class:`LST` object.
               
               Channels are written in the order of the list.  Only the
               channel names in the list are used.
               
               Data is formated as in the channel definition and
               channels are separated by a single space character.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="line symbol"),
                   Parameter('p3', type="LST",
                             doc="list of channel names to write"),
                   Parameter('p4', type="WA",
                             doc=":class:`WA` to write to")
               ]),

        Method('XyzLine_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Break up a line based on tolerance of lateral distance.",
               notes="The original line will be deleted.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel X"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Channel Y"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Line direction, 0-any, 1-X, 2-Y."),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Tolerance, DUMMY for the default (10% of the separation between the first two points.")
               ]),

        Method('XyzLine2_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Break up a line based on tolerance of lateral and horizontal distance.",
               notes="The original line will be deleted.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel X [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Channel Y [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Line direction, 0-any, 1-X, 2-Y."),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Tolerance, DUMMY for the default (10% of the separation between the first two points."),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Downline Tolerance, DUMMY for none")
               ]),

        Method('XyzLine3_DU', module='geogxx', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Break up a line based on tolerance of lateral and horizontal distance.",
               notes="The same as XyzLine2, but with an option to reset each line's starting fiducial to zero.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to be broken up [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel X [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Channel Y [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Line direction, 0-any, 1-X, 2-Y."),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Tolerance, DUMMY for the default (10% of the separation between the first two points."),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Downline Tolerance, DUMMY for none"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Reset starting fiducials to zero (0: No, 1: Yes)")
               ]),

        Method('ZMask_DU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Mask dummies in one channel against another(Z) with the range Zmin/Zmax.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line Handle"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Channel to mask [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Mask Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Min value of mask range"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Max value of mask range")
               ]),

        Method('RangeXY_DU', module='geogxx', version='8.5.0',
               availability=Availability.LICENSED, 
               doc="Find the range of X, and Y in the selected lines.",
               notes="""
               Returns the range in X and Y of the current X and Y channels.
               Returned values are dummy if no valid items are found.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum X (returned)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum Y (returned)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum X (returned)"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum Y (returned)")
               ]),

        Method('RangeXYZ_DU', module='geogxx', version='8.5.0',
               availability=Availability.LICENSED, 
               doc="Find the range of X, Y and Z in selected lines.",
               notes="""
               The X, Y and Z channels should be normal (not array) channels.
               Only locations where all values are non-dummy are included in the calculation.
               If no non-dummy values are found, Dummy values are returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Y Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Z Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum X (returned)"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum Y (returned)"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum Z (returned)"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum X (returned)"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum Y (returned)"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum Z (returned)"),
                   Parameter('p11', type=Type.INT32_T, is_ref=True,
                             doc="Number of data values (returned)")
               ]),

        Method('RangeXYZData_DU', module='geogxx', version='8.1.0',
               availability=Availability.LICENSED, 
               doc="Find the range of X, Y, Z and Data values in selected lines.",
               notes="""
               The Z and Data channels may be array channels, but both must have
               the same number of columns.
               Only values where all channels are non-dummy (or, for :class:`VA` channels,
               where the Z or Data value are defined) are included in the calculation.
               If no non-dummy values are found, Dummy values are returned.
               This function is optimized for cases where Z and Data are array channels
               with many columns (e.g. 32 or more columns).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Y Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Z Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Data Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum X (returned)"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum Y (returned)"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum Z (returned)"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum Data value (returned)"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum X (returned)"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum Y (returned)"),
                   Parameter('p12', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum Z (returned)"),
                   Parameter('p13', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum Data value (returned)"),
                   Parameter('p14', type=Type.INT32_T, is_ref=True,
                             doc="Number of data values (returned)")
               ]),

        Method('CreateDrillholeParameterWeightConstraintDatabase_DU', module='geogxx', version='8.2.0',
               availability=Availability.LICENSED, 
               doc="Used for weighting inversion models.",
               notes="""
               Control parameters are passed in the :class:`REG` (to allow for future expansion without
               the need to modify the wrappers).
               The input drillhole database must contain current X, Y and Z channels.
               Drillhole data should be equally spaced (or nearly so) down the hole.
               Weights are calculated on a circle perpendicular to the hole at each point.
               
               RADIUS - Maximum radius from drillhole to create weighting points (Default = 100).
               INCRMENENT - Grid cell size in weighting circle (Default = 10).
               MINIMUM - the minimum weighting value to apply, at the radius (Default = 0.0001).
               POWER - Exponential power to use in the weighting function (negative of this is used) (Default = 2).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database (selected lines used)"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Property channel handle [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="REG",
                             doc="Parameters (see notes)"),
                   Parameter('p4', type=Type.STRING,
                             doc="Output database")
               ]),

        Method('CalculateDrapedSurveyAltitude_DU', module='geogxx', version='8.3.0',
               availability=Availability.LICENSED, 
               doc="Calculate a draped flight path, enforcing maximum descent and ascent rates.",
               notes="""
               Calculate a draped flight path, enforcing maximum descent and ascent rates. Additional Inputs are the sample distance along the line
               and a topography grid.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="IMG",
                             doc="Topography grid"),
                   Parameter('p6', type="DB_SYMB",
                             doc="Output draped altitude channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Maximum rate of ascent (%)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Maximum rate of descent (%)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Minimum terrain clearance (drape height)"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Number of times to apply Hanning Filter"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Width of Hanning Filter"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="Minimum radius of curvature down slopes and at valley bottoms (:def_val:`rDUMMY` to disable)")
               ]),

        Method('CalculateDrapedSurveyAltitude2_DU', module='geogxx', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Calculate a draped flight path, enforcing maximum descent and ascent rates.",
               notes="""
               Calculate a draped flight path, enforcing maximum descent and ascent rates.
               Set both a nominal and minimum drape height.
               Additional Inputs are the sample distance along the line
               and a topography grid.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="IMG",
                             doc="Topography grid"),
                   Parameter('p6', type="DB_SYMB",
                             doc="Output DEM channel [:def_val:`DB_LOCK_READWRITE`] (can be :def_val:`NULLSYMB` if not required)"),
                   Parameter('p7', type="DB_SYMB",
                             doc="Output draped altitude channel [:def_val:`DB_LOCK_READWRITE`]"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Maximum rate of ascent (%)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Maximum rate of descent (%)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Nominal terrain clearance (drape height)"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Minimum terrain clearance (hard minimum drape height)"),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Number of times to apply Hanning Filter"),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Width of Hanning Filter"),
                   Parameter('p14', type=Type.DOUBLE,
                             doc="Minimum radius of curvature down slopes and at valley bottoms (:def_val:`rDUMMY` to disable)")
               ]),

        Method('DirectGridDataToVoxel_DU', module='geogxx', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Create a voxel using direct gridding.",
               notes="The Z and Data channels may be array channels. If they are, the array sizes must match.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="X channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Y channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Z channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Data channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p6', type=Type.STRING,
                             doc="Output voxel filename"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Voxel origin X"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Voxel origin Y"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Voxel origin Z"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Voxel cell count X"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="Voxel cell count Y"),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Voxel cell count Z"),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Voxel cell size X"),
                   Parameter('p14', type=Type.DOUBLE,
                             doc="Voxel cell size Y"),
                   Parameter('p15', type=Type.DOUBLE,
                             doc="Voxel cell size Z"),
                   Parameter('p16', type=Type.INT32_T,
                             doc=":def:`DU_DIRECTGRID_METHOD`")
               ]),

        Method('DirectGridItemCountsToVoxel_DU', module='geogxx', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Create a voxel using direct gridding containing the number of data points in each cell.",
               notes="The Z and Data channels may be array channels. If they are, the array sizes must match.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="X channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Y channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Z channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Data channel [:def_val:`DB_LOCK_READONLY`]"),
                   Parameter('p6', type=Type.STRING,
                             doc="Output voxel filename"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Voxel origin X"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Voxel origin Y"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Voxel origin Z"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Voxel cell count X"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="Voxel cell count Y"),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Voxel cell count Z"),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Voxel cell size X"),
                   Parameter('p14', type=Type.DOUBLE,
                             doc="Voxel cell size Y"),
                   Parameter('p15', type=Type.DOUBLE,
                             doc="Voxel cell size Z"),
                   Parameter('p16', type=Type.INT32_T,
                             doc="Replace zero values in output with DUMMY? :def:`GEO_BOOL`")
               ])
    ]
}

