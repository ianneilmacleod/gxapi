from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VVU',
                 doc="""
                 These methods are not a class. Utility methods perform
                 various operations on :class:`VV` objects, including pruning,
                 splining, clipping and filtering.
                 """)


gx_defines = [
    Define('QC_CRITERION',
           doc="Criterion",
           constants=[
               Constant('QC_CRITERION_1', value='0', type=Type.INT32_T)                        ,
               Constant('QC_CRITERION_2', value='1', type=Type.INT32_T)                        ,
               Constant('QC_CRITERION_12', value='2', type=Type.INT32_T)                        
           ]),

    Define('TEM_ARRAY',
           doc="Array Type",
           constants=[
               Constant('TEM_ARRAY_VERTICALSOUNDING', value='0', type=Type.INT32_T)                        ,
               Constant('TEM_ARRAY_PROFILING', value='1', type=Type.INT32_T)                        ,
               Constant('TEM_ARRAY_BOREHOLE', value='2', type=Type.INT32_T)                        
           ]),

    Define('VV_DUP',
           doc="Duplicate handling mode",
           constants=[
               Constant('VV_DUP_AVERAGE', value='0', type=Type.INT32_T,
                        doc="average numeric values (for strings, same as :def_val:`VV_DUP_1`)")                        ,
               Constant('VV_DUP_1', value='1', type=Type.INT32_T,
                        doc="Use first value of the pair")                        ,
               Constant('VV_DUP_2', value='2', type=Type.INT32_T,
                        doc="Use second value of the pair")                        ,
               Constant('VV_DUP_DUMMY', value='3', type=Type.INT32_T,
                        doc="Set to dummy")                        ,
               Constant('VV_DUP_SAMPLE', value='4', type=Type.INT32_T,
                        doc='Set to "3" (cannot use with string data :class:`VV`)')                        
           ]),

    Define('VV_XYDUP',
           doc="Sample handling",
           constants=[
               Constant('VV_XYDUP_AVERAGE', value='0', type=Type.INT32_T)                        ,
               Constant('VV_XYDUP_SUM', value='1', type=Type.INT32_T)                        
           ]),

    Define('VVU_CASE',
           doc="String case handling",
           constants=[
               Constant('VVU_CASE_TOLERANT', value='0', type=Type.INT32_T)                        ,
               Constant('VVU_CASE_SENSITIVE', value='1', type=Type.INT32_T)                        
           ]),

    Define('VVU_CLIP',
           doc="Type of clipping",
           constants=[
               Constant('VVU_CLIP_DUMMY', value='0', type=Type.INT32_T,
                        doc="clip replaces clipped values with a dummy.")                        ,
               Constant('VVU_CLIP_LIMIT', value='1', type=Type.INT32_T,
                        doc="clip replaces clipped values with the limit.")                        
           ]),

    Define('VVU_DUMMYREPEAT',
           doc="How to deal with repeats",
           constants=[
               Constant('VVU_DUMMYREPEAT_FIRST', value='0', type=Type.INT32_T,
                        doc="dummies all but first point.")                        ,
               Constant('VVU_DUMMYREPEAT_LAST', value='1', type=Type.INT32_T,
                        doc="dummies all but last point.")                        ,
               Constant('VVU_DUMMYREPEAT_MIDDLE', value='2', type=Type.INT32_T,
                        doc="dummies all but middle point.")                        
           ]),

    Define('VVU_INTERP',
           doc="Interpolation method to use",
           constants=[
               Constant('VVU_INTERP_NEAREST', value='1', type=Type.INT32_T)                        ,
               Constant('VVU_INTERP_LINEAR', value='2', type=Type.INT32_T)                        ,
               Constant('VVU_INTERP_CUBIC', value='3', type=Type.INT32_T)                        ,
               Constant('VVU_INTERP_AKIMA', value='4', type=Type.INT32_T)                        ,
               Constant('VVU_INTERP_PREDICT', value='5', type=Type.INT32_T)                        
           ]),

    Define('VVU_INTERP_EDGE',
           doc="Interpolation method to use on edges",
           constants=[
               Constant('VVU_INTERP_EDGE_NONE', value='0', type=Type.INT32_T)                        ,
               Constant('VVU_INTERP_EDGE_SAME', value='1', type=Type.INT32_T)                        ,
               Constant('VVU_INTERP_EDGE_NEAREST', value='2', type=Type.INT32_T)                        ,
               Constant('VVU_INTERP_EDGE_LINEAR', value='3', type=Type.INT32_T)                        
           ]),

    Define('VVU_LINE',
           doc="Line Types",
           constants=[
               Constant('LINE_2_POINTS', value='0', type=Type.INT32_T)                        ,
               Constant('LINE_POINT_AZIMUTH', value='1', type=Type.INT32_T)                        
           ]),

    Define('VVU_MASK',
           doc="Type of clipping",
           constants=[
               Constant('VVU_MASK_INSIDE', value='0', type=Type.INT32_T,
                        doc="Mask :class:`VV` is set to dummy at locations inside the :class:`PLY`.")                        ,
               Constant('VVU_MASK_OUTSIDE', value='1', type=Type.INT32_T,
                        doc="Mask :class:`VV` is set to dummy at locations outside the :class:`PLY`.")                        
           ]),

    Define('VVU_MATCH',
           doc="Matching style",
           constants=[
               Constant('VVU_MATCH_FULL_STRINGS', value='0', type=Type.INT32_T,
                        doc="entire string")                        ,
               Constant('VVU_MATCH_INPUT_LENGTH', value='1', type=Type.INT32_T,
                        doc="match the first part of a string.")                        
           ]),

    Define('VVU_MODE',
           doc="Statistic to select",
           constants=[
               Constant('VVU_MODE_MEAN', value='0', type=Type.INT32_T)                        ,
               Constant('VVU_MODE_MEDIAN', value='1', type=Type.INT32_T)                        ,
               Constant('VVU_MODE_MAXIMUM', value='2', type=Type.INT32_T)                        ,
               Constant('VVU_MODE_MINIMUM', value='3', type=Type.INT32_T)                        
           ]),

    Define('VVU_OFFSET',
           doc="Heading",
           constants=[
               Constant('VVU_OFFSET_FORWARD', value='0', type=Type.INT32_T)                        ,
               Constant('VVU_OFFSET_BACKWARD', value='1', type=Type.INT32_T)                        ,
               Constant('VVU_OFFSET_RIGHT', value='2', type=Type.INT32_T)                        ,
               Constant('VVU_OFFSET_LEFT', value='3', type=Type.INT32_T)                        
           ]),

    Define('VVU_PRUNE',
           doc="Prune options",
           constants=[
               Constant('VVU_PRUNE_DUMMY', value='0', type=Type.INT32_T,
                        doc="0")                        ,
               Constant('VVU_PRUNE_VALID', value='1', type=Type.INT32_T,
                        doc="1")                        
           ]),

    Define('VVU_SPL',
           doc="Spline types",
           constants=[
               Constant('VVU_SPL_LINEAR', value='0', type=Type.INT32_T)                        ,
               Constant('VVU_SPL_CUBIC', value='1', type=Type.INT32_T)                        ,
               Constant('VVU_SPL_AKIMA', value='2', type=Type.INT32_T)                        ,
               Constant('VVU_SPL_NEAREST', value='3', type=Type.INT32_T)                        
           ]),

    Define('VVU_SRCHREPL_CASE',
           doc="Search and Replace handling of string case",
           constants=[
               Constant('VVU_SRCHREPL_CASE_TOLERANT', value='0', type=Type.INT32_T)                        ,
               Constant('VVU_SRCHREPL_CASE_SENSITIVE', value='1', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AverageRepeat_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Average repeat values.",
               notes="""
               Repeated values in the reference :class:`VV` will be averaged
               in the data :class:`VV`.  The first value in the data :class:`VV` will be set to the
               average and subsequent data :class:`VV` values will be dummied out.
               Data is processed only to the minimum length of the
               input :class:`VV` lengths.
               """,
               see_also=":func:`RemoveDummy_VVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="reference :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="data :class:`VV` to average")
               ]),

        Method('AverageRepeatEx_VVU', module='geogxx', version='8.0.1',
               availability=Availability.LICENSED, 
               doc="Average repeat values.",
               notes="""
               Repeated values in the reference :class:`VV` will be set to the mean, median, minimum or maximum value
               in the data :class:`VV`.  For minimum and maximum, the index in the data :class:`VV` containing the minimum or maximum value
               is retained, and the other repeated values are dummied out. For mean and median, the first value in the 
               data :class:`VV` will be reset and subsequent data :class:`VV` values will be dummied out.
               Data is processed only to the minimum length of the
               input :class:`VV` lengths.
               """,
               see_also=":func:`RemoveDummy_VVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="reference :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="data :class:`VV` to average"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`VVU_MODE`")
               ]),

        Method('AverageRepeat2_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Average repeat values based on 2 reference channels.",
               notes="""
               Repeated values in the reference :class:`VV` will be averaged
               in the data :class:`VV`.  The first value in the data :class:`VV` will be set to the
               average and subsequent data :class:`VV` values will be dummied out.
               Data is processed only to the minimum length of the
               input :class:`VV` lengths.
               Both the reference :class:`VV` values must repeat for the averageing
               to occur. This version is useful for averaging on repeated
               (X,Y) locations.
               """,
               see_also="RemoveDummy_VV",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="reference :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="reference :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="data :class:`VV` to average")
               ]),

        Method('AverageRepeat2Ex_VVU', module='geogxx', version='8.0.1',
               availability=Availability.LICENSED, 
               doc="Average repeat values based on 2 reference channels.",
               notes="""
               Repeated values in the reference :class:`VV` will be set to the mean, median, minimum or maximum value
               in the data :class:`VV`.  The first value in the data :class:`VV` will be reset and subsequent data :class:`VV` values will be dummied out.
               Data is processed only to the minimum length of the
               input :class:`VV` lengths.
               Both the reference :class:`VV` values must repeat for the averageing
               to occur. This version is useful for averaging on repeated
               (X,Y) locations.
               """,
               see_also="RemoveDummy_VV",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="reference :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="reference :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="data :class:`VV` to average"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`VVU_MODE`")
               ]),

        Method('BinarySearch_VVU', module='geogxx', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="Search  numeric value in a :class:`VV`.",
               notes="""
               The :class:`VV` should be sorted.Search comparison is made on double
               comparison of the data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="value to search for."),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Minmum Location"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Maximum Location")
               ]),

        Method('BoxCox_VVU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Run Box-Cox (lambda) Transformation on :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="[i/o] :class:`VV`"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="[i] Lambda Value")
               ]),

        Method('BPFilt_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Band-pass filter to the specified.",
               notes="""
               If the short and long wavelengths are <= 0, the input channel
               is simply copied to the output channel without filtering.
               
               The wavelengths are in fiducials.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="input :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="filtered :class:`VV`"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Short wavelength cutoff, 0 for highpass"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Long wavelength cutoff, 0 for lowpass"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Filter Length, 0 for default length")
               ]),

        Method('Clip_VVU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Clip a :class:`VV` to a range.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` to clip"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="minimum value, :def_val:`rDUMMY` for no minimum clip"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="maximum value, :def_val:`rDUMMY` for no maximum clip"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`VVU_CLIP`")
               ]),

        Method('ClipToDetectLimit_VVU', module='geogxx', version='5.1.6',
               availability=Availability.LICENSED, 
               doc="Apply detection limit clipping of data.",
               notes="""
               Flow:
               
               1. If auto-converting negatives, then all negative values
                   are replaced by -0.5*value, and detection limit is ignored.
               
               2. If not auto-converting negatives, and the detection limit is not
                  :def_val:`rDUMMY`, then values less than the detection limit are converted to
                  one-half the detection limit.
               
               This function is identical to :func:`ClipToDetectLimit_CHIMERA`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input data vv (altered)."),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Detection limit"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Auto-convert negatives?")
               ]),

        Method('CondDepthTEM_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Calculate TEM apparent conductivity and depth",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Response channel (microvolts)"),
                   Parameter('p2', type="VV",
                             doc="Time channel (milliseconds)"),
                   Parameter('p3', type="VV",
                             doc="Conductivity channel (siemen/m)"),
                   Parameter('p4', type="VV",
                             doc="Depth (m)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Transmitter current"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Flag  Transmitter defined by moment (0) or by 4 VVs (1) below"),
                   Parameter('p7', type="VV",
                             doc="Minimum X to define transmitter loop layout (moment)"),
                   Parameter('p8', type="VV",
                             doc="Minimum Y to define transmitter loop layout (moment)"),
                   Parameter('p9', type="VV",
                             doc="Maximum X to define transmitter loop layout (moment)"),
                   Parameter('p10', type="VV",
                             doc="Maximum Y to define transmitter loop layout (moment)"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Transmitter moment (square meters), dummy if the above flag is 1"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="Receiver moment (square meters)"),
                   Parameter('p13', type=Type.INT32_T,
                             doc=":def:`TEM_ARRAY`")
               ]),

        Method('Decimate_VVU', module='geogxx', version='6.1.0',
               availability=Availability.LICENSED, 
               doc="Decimate a :class:`VV`.",
               notes="""
               For a decimation factor N, will remove all values except
               those with indices equal to MN, where M is an integer.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="decimation factor (must be > 0)")
               ]),

        Method('Deviation_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate distance of point locations to a straight line",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X :class:`VV`,REAL :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Y :class:`VV`,REAL :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Output deviation :class:`VV`,REAL :class:`VV`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X of 1st point to define straight line"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y of 1st point to define straight line"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="X of 2nd point or line azimuth in degrees (North is 0 degree)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Y of 2nd point or :def_val:`GS_R8DM` if line azimuth is defined"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`VVU_LINE`")
               ]),

        Method('Distance_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a cumulative distance :class:`VV`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X :class:`VV`,REAL :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Y :class:`VV`,REAL :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Output distance :class:`VV`,REAL :class:`VV`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X :class:`VV` fid start"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X :class:`VV` fid incr"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Y :class:`VV` fid start"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Y :class:`VV` fid incr")
               ]),

        Method('DistanceNonCumulative_VVU', module='geogxx', version='7.2.0',
               availability=Availability.LICENSED, 
               doc="""
               Create a non cumulative distance :class:`VV` i.e each
               distance element is the distance of the corresponding
               (X,Y) element and the previous element.
               """,
               notes="The fist distace element is :def_val:`rDUMMY`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X :class:`VV`,REAL :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Y :class:`VV`,REAL :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Output distance :class:`VV`,REAL :class:`VV`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X :class:`VV` fid start"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X :class:`VV` fid incr"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Y :class:`VV` fid start"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Y :class:`VV` fid incr")
               ]),

        Method('Distance3D_VVU', module='geogxx', version='8.0.1',
               availability=Availability.LICENSED, 
               doc="Create a cumulative distance :class:`VV` from X, Y and Z VVs",
               notes="""
               The output :class:`VV` is the length of the shortest X,Y or Z input :class:`VV`.
               Any values with dummies are ignored - the distance at that
               point is equal to the distance at the previous valid point.
               The returned :class:`VV` is the cumulative straight-line distance
               between the points. No re-sampling is performed.
               VVs of any type are supported.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X :class:`VV`,REAL :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Y :class:`VV`,REAL :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Z :class:`VV`,REAL :class:`VV`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Distance at first location"),
                   Parameter('p5', type="VV",
                             doc="Output distance :class:`VV`,REAL :class:`VV`")
               ]),

        Method('FindGaps3D_VVU', module='geogxx', version='8.1.0',
               availability=Availability.LICENSED, 
               doc="Return indices of locations separated from previous locations by more than the input gap distance.",
               notes="""
               Locate the starting points of line segements determined by an input gap distance.
               The returned indices indicate where to break the line, given an input gap.
               The number of returned indices is one less than the number of line segments.
               (So if there are no gaps the returned :class:`VV` has zero length).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X :class:`VV`,REAL :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Y :class:`VV`,REAL :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Z :class:`VV`,REAL :class:`VV`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Gap size (must be greater than zero)"),
                   Parameter('p5', type="VV",
                             doc="Returned indices of start of sections after gaps (INT :class:`VV`)")
               ]),

        Method('DummyRange_VVU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Dummy values inside or outside a range in a :class:`VV`",
               notes="""
               If the Inside flag is TRUE, values within the specified
               range are set to dummy. If the inside flag is FALSE,
               values outside the range are set to dummy.  If the Inclusive
               flag is TRUE, then dMin and dMax are considered part of the
               range. If it is FALSE, then < or > are used, and dMin and
               dMax lie outside the range.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Minimum range value"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Maximum range value"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="If TRUE, dummy inside the range"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="If TRUE, include Min, Max in the range.")
               ]),

        Method('DummyRangeEx_VVU', module='geogxx', version='5.0.7',
               availability=Availability.PUBLIC, 
               doc="Like DummyRangeVVU, with inclusion options for both ends.",
               notes="""
               If the Inside flag is TRUE, values within the specified
               range are set to dummy. If the inside flag is FALSE,
               values outside the range are set to dummy.  If the Inclusive
               flag is TRUE, then dMin and dMax are considered part of the
               range. If it is FALSE, then < or > are used, and dMin and
               dMax lie outside the range.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Minimum range value"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Maximum range value"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="If TRUE, dummy inside the range"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="If TRUE, include Min in the range."),
                   Parameter('p6', type=Type.INT32_T,
                             doc="If TRUE, include Max in the range.")
               ]),

        Method('DummyRepeat_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="dummy repeat values in a :class:`VV`.",
               notes="""
               Either the first, middle or last point will be left.
                                 Use :func:`Interp_VVU` to interpolate after if desired.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`VVU_DUMMYREPEAT`")
               ]),

        Method('DupStats_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate means and differences for duplicate sample pairs",
               notes="""
               Created for duplicate sample handling in :class:`CHIMERA`. On input,
               a numeric :class:`VV` containing data values, and a sample type :class:`VV`.
               Sample pairs have types "1" and "2". This routine searches for
               types in order "1 2 1 2", and writes the mean values of pairs
               to the mean value :class:`VV`, and the differences with the mean (equal
               values, negative and positive) to the difference :class:`VV`. Results
               for samples out of order, for unmatched values, or when the
               sample type does not equal "1" or "2" are set to dummy.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Duplicate data :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Sample Type :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Mean values :class:`VV` (returned)"),
                   Parameter('p4', type="VV",
                             doc="Diff values :class:`VV` (returned)")
               ]),

        Method('ExpDist_VVU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Fill with exponentially distributed values.",
               notes="""
               :class:`VV` is set to input length (except for -1)
               See RAND for a short discription of the
               random number generator used.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Random number generator seed"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Mean value of distribution (> 0.0)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Number of values (-1 for all)")
               ]),

        Method('Filter_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Apply a convolution filter to a :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="input :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="filtered :class:`VV`"),
                   Parameter('p3', type="FILTER",
                             doc="Filter handle (see :class:`FLT`)")
               ]),

        Method('FindStringItems_VVU', module='geogxx', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Searches a :class:`VV` for items in a second :class:`VV`, returns indices of those found.",
               notes="""
               This is a much more efficient way of determining if items in
               one :class:`VV` are found in a second, than by searching
               repeatedly in a loop.
               The returned :def_val:`GS_LONG` :class:`VV` contains the same number of items as
               the "search items" :class:`VV`, and contains -1 for items where the
               value is not found, and the index of items that are found.
               Comparisons are case-tolerant.
               Non-string VVs are converted to string type VVs (element size 24) internally.
               
               The method requires that the :class:`VV` items be sorted, and
               will do so internally. Since the input VVs may already be sorted,
               the method will run faster if this stage can be skipped.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="String :class:`VV` in which to locate items"),
                   Parameter('p2', type="VV",
                             doc="String :class:`VV` Items to search for"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Is the first :class:`VV` already sorted?"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Is the second :class:`VV` already sorted"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Case tolerance for string comparisons"),
                   Parameter('p6', type="VV",
                             doc=":def_val:`GS_LONG` :class:`VV` of returned indices into the first :class:`LST`.")
               ]),

        Method('FractalFilter_VVU', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Fractal filter a :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="[i] :class:`VV`"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="[i] filter order"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="[i] filter number"),
                   Parameter('p4', type="VV",
                             doc="[o] filtered :class:`VV`")
               ]),

        Method('iCloseXY_VVU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Find the closest point to an input point (XY).",
               notes="""
               Input X and Y location VVs, and a location.
               Returns the index of the point in the :class:`VV` closest to the
               input point.
               """,
               return_type=Type.INT32_T,
               return_doc="Index of closest point, -1 if no valid locations, or data is masked.",
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X locations"),
                   Parameter('p2', type="VV",
                             doc="Y locations"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="input X"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="input Y")
               ]),

        Method('iCloseXYM_VVU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Find the closest point to an input point, with mask (XY).",
               notes="""
               Input X and Y location VVs, and a location.
               Returns the index of the point in the :class:`VV` closest to the
               input point.
               This skips points where the mask value is dummy.
               If no valid points are in the VVs, or all the mask :class:`VV` values
               are dummy, the returned index is -1.
               """,
               return_type=Type.INT32_T,
               return_doc="Index of closest point, -1 if no valid locations, or data is masked.",
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X locations"),
                   Parameter('p2', type="VV",
                             doc="Y locations"),
                   Parameter('p3', type="VV",
                             doc="Mask values"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="input X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="input Y")
               ]),

        Method('iCloseXYZ_VVU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Find the closest point to an input point (XYZ).",
               notes="""
               Input X, Y and Z location VVs, and a location.
               Returns the index of the point in the :class:`VV` closest to the
               input point.
               """,
               return_type=Type.INT32_T,
               return_doc="Index of closest point, -1 if no valid locations, or data is masked.",
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X locations"),
                   Parameter('p2', type="VV",
                             doc="Y locations"),
                   Parameter('p3', type="VV",
                             doc="Z locations"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="input X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="input Y"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="input Z")
               ]),

        Method('iCloseXYZM_VVU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Find the closest point to an input point, with mask (XYZ).",
               notes="""
               Input X, Y and Z location VVs, and a location.
               Returns the index of the point in the :class:`VV` closest to the
               input point.
               This skips points where the mask value is dummy.
               If no valid points are in the VVs, or all the mask :class:`VV` values
               are dummy, the returned index is -1.
               """,
               return_type=Type.INT32_T,
               return_doc="Index of closest point, -1 if no valid locations, or data is masked.",
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X locations"),
                   Parameter('p2', type="VV",
                             doc="Y locations"),
                   Parameter('p3', type="VV",
                             doc="Z locations"),
                   Parameter('p4', type="VV",
                             doc="Mask values"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="input X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="input Y"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="input Z")
               ]),

        Method('iDummyBackTracks_VVU', module='geogxx', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Dummy all points that keep a :class:`VV` from being monotonically increasing.",
               notes="""
               The :class:`VV` length remains the same. Any point that is less than or equal to
               the previous (valid) point in the :class:`VV` is dummied.
               """,
               return_type=Type.INT32_T,
               return_doc="The number of items dummied in order to render the :class:`VV` montonically increasing.",
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` handle")
               ]),

        Method('iFindDummy_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find the first dummy|non-dummy value in :class:`VV`",
               notes="""
               Start and end of range are always defined lowest
               to largest even if decreasing search order.  To search
               entire :class:`VV` range, specify 0,-1.
               """,
               return_type=Type.INT32_T,
               return_doc="""
               The index of the first dummy|non-dummy value in :class:`VV`
               -1 if not found or if length of :class:`VV` is 0
               """,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="0 increasing order 1 decreasing order"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="0 to find the first dummy 1 find first non-dummy"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="start search range at element"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="end search range at element (-1 for last)")
               ]),

        Method('Interp_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Replace all dummies by interpolating from valid data.",
               notes="""
               Edge behaviour: Dummies at the ends are treated as follows
               for various combinations of the inside and outside interpolation
                choices:
               
                 if ((iOutside==VV_INTERP_EDGE_NEAREST) ||
                     (iOutside==VV_INTERP_EDGE_SAME && iInside==VV_INTERP_NEAREST))
               
                    // -- Set dummies to the same value as the last defined element
               
                 else if ((iOutside==VV_INTERP_EDGE_LINEAR) ||
                          (iOutside==VV_INTERP_EDGE_SAME &&  iInside==VV_INTERP_LINEAR))
               
                    // --- Set dummies using the slope of the last two defined elements
               
                 endif
               
               In all other cases and combinations of the two interpolation
               choices, the dummies are left "as is".
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="input :class:`VV`"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`VVU_INTERP`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`VVU_INTERP_EDGE`")
               ]),

        Method('iQCFillGaps_VVU', module='geogxx', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Calculate fill in line segments",
               notes="The X & Y VVs are returned as the calculated fill in line segments.",
               return_type=Type.INT32_T,
               return_doc="1 if error, 0 if successful",
               parameters = [
                   Parameter('p1', type="VV",
                             doc="input/output X :class:`VV` on which to operate Required in :def_val:`GS_DOUBLE` or :def_val:`GS_FLOAT`"),
                   Parameter('p2', type="VV",
                             doc="input/output Y :class:`VV` on which to operate In :def_val:`GS_DOUBLE` or :def_val:`GS_FLOAT`"),
                   Parameter('p3', type="VV",
                             doc="input Flag :class:`VV` Required in :def_val:`GS_BYTE`"),
                   Parameter('p4', type="VV",
                             doc="input Gap :class:`VV` to use for locating the fill inline segments In :def_val:`GS_DOUBLE` or :def_val:`GS_FLOAT`"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Min segment length  (required)")
               ]),

        Method('iSearchText_VVU', module='geogxx', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Search for a text value in a :class:`VV`",
               notes="""
               Search comparison is made on string comparison
               of the data. Returns index of first item matching
               the input string.
               If start index is -1 or dummy, then full :class:`VV` is searched.
               Use :def_val:`VVU_MATCH_INPUT_LENGTH` to match the first part of a string.
               This is also recommended for matching numerical values, since
               the displayed value in the database may not be the same as the
               stored value.
               """,
               see_also="sSearchReplace_VV",
               return_type=Type.INT32_T,
               return_doc="Index of first matching text, -1 if not found.",
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` to search"),
                   Parameter('p2', type=Type.STRING,
                             doc="Text to match"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`VVU_CASE`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`VVU_MATCH`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="index to begin search (-1 for full :class:`VV`)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="1: forward search, -1: backward search")
               ]),

        Method('Mask_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Mask dummies in one :class:`VV` onto another.",
               notes="""
               :class:`VV` to mask will be resampled to reference :class:`VV` if required.
               The returned length of the :class:`VV` to mask will be the shorter
               of the reference :class:`VV` or the mask :class:`VV`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` to be masked"),
                   Parameter('p2', type="VV",
                             doc="mask reference :class:`VV`")
               ]),

        Method('MaskAND_VVU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Create mask from logical AND of two VVs.",
               notes="If both values are non-dummies, then result is 1, else dummy.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` A"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` B"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` C (returned)")
               ]),

        Method('MaskOR_VVU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Create mask from logical OR of two VVs.",
               notes="If either values is non-dummy, then result is 1, else dummy.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` A"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` B"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` C (returned)")
               ]),

        Method('NLFilt_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Applies a non-linear filter.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="input :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="filtered :class:`VV`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Filter Width"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Filter Tolerance, 0 for 1% of Std. Dev.")
               ]),

        Method('NoiseCheck_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Check on deviation of data from variable background in a :class:`VV`",
               notes="""
               This function checks vertical deviation of data in input :class:`VV`
               against a moving straight line. The straight line at any time is
               defined by two extreme points of a data segment.  Output :class:`VV` will
               be 0 if data point in input :class:`VV` falls within the deviation,
               otherwise, it will be 1.
               Output :class:`VV` will be 0 if the straight line is vertical.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="input :class:`VV` on which to apply quality control Required in :def_val:`GS_DOUBLE` or :def_val:`GS_FLOAT`"),
                   Parameter('p2', type="VV",
                             doc="output flag :class:`VV` with result 0 and 1. Required in :def_val:`GS_BYTE`"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="allowed deviation over a number of data points in input :class:`VV` (next parameter). Must be >= 0.0"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="number of data points. Must be > 0")
               ]),

        Method('NoiseCheck2_VVU', module='geogxx', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Like :func:`NoiseCheck_VVU`, but returns maximum deviation at all points.",
               notes="""
               This function checks vertical deviation of data in an input :class:`VV`
               against a moving straight line, where the X-axis value is
               taken to be the data index, and the Y-axis value is the
               input data :class:`VV` value. The straight line is drawn between data points
               at the ends of the line segment, whose length is an input.
               
               The output flag :class:`VV` is set to 0 if data point in input :class:`VV` falls within the
               deviation for all the moving line segments of which it is a part, otherwise, it
               will be set to 1.
               
               The output maximum deviation :class:`VV` contains the maximum deviation at each point
               for all the moving line segments that it is a part of.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="input :class:`VV` on which to apply quality control Required in :def_val:`GS_DOUBLE` or :def_val:`GS_FLOAT`"),
                   Parameter('p2', type="VV",
                             doc="output flag :class:`VV` with result 0 and 1. Required in :def_val:`GS_BYTE`"),
                   Parameter('p3', type="VV",
                             doc="Output maximum deviation :class:`VV`."),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="allowed deviation over a number of data points in input :class:`VV` (next parameter). Must be >= 0.0"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="number of data points in the line segment. Must be > 0")
               ]),

        Method('NormalDist_VVU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Fill with normally (Gaussian) distributed values.",
               notes="""
               :class:`VV` is set to input length (except for -1)
               See RAND for a short discription of the
               random number generator used.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Random number generator seed"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Mean value of distribution"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Variance of the distribution"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Number of values (-1 for all)")
               ]),

        Method('OffsetCircles_VVU', module='geogxx', version='5.0.7',
               availability=Availability.LICENSED, 
               doc="Get non-overlapping offset location for circular symbols.",
               notes="""
               Often on maps plotted symbols and text overlap each other.
               This routine accepts of :class:`VV` of locations and returns a new
               set of locations offset from the originals, and guaranteed
               not to overlap, given the size of the original symbols.
               The returned offset X, Y
               locations are offset from the original locations by
               the minimum of a) the input offset, b) the input symbol
               radius. This is to ensure that the original location is
               never covered by the offset symbol.
               
               Care should be taken when choosing the symbol size, because
               if the point density is too high, all the points will get
               pushed to the outside edge and your plot will look like a
               hedgehog (it also takes a lot longer!).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input X locations"),
                   Parameter('p2', type="VV",
                             doc="Input Y locations"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="minimum offset distance"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="symbol radius"),
                   Parameter('p5', type="VV",
                             doc="Output (offset) X locations"),
                   Parameter('p6', type="VV",
                             doc="Output (offset) Y locations")
               ]),

        Method('OffsetCorrect_VVU', module='geogxx', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Correct locations based on heading and fixed offset.",
               notes="""
               In many applications, measurements are taken with an instrument which
               is towed behind, or pushed ahead of where the locations are recorded.
               Use this function to estimate the actual location of the instrument.
               The method determines the heading along the line, using a "thinned"
               version of the line. The degree of thinning is based on the size of the
               offset; the larger the offset, the greater the distance between sample
               locations used to construct the thinned lined used for determining headings.
               The thinned line is splined at a frequency greater than the sample
               frequency, and the heading at any given point is determined from the
               vector formed by the closest two points on the splined line. The
               correction (behind, in front, left or right) is determined with respect
               to the heading, and added to the original location.
               
               IF this method fails, no dummies, no duplicated locations, no reversals
               are produced.
               
               The algorithm:
               
               1. Determine average distance between each point = D
               2. Smoothing interval = MAX(2*D, Offset distance) = I
               3. Thin input points to be at least the smoothing interval I apart from each other.
               4. Smoothly re-interpolate the thinned points at five times the
                  original average distance D.
               5. For each input point, calculate the bearing using the nearest points
                  on the smoothed curve
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input X"),
                   Parameter('p2', type="VV",
                             doc="Input Y"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Offset distance"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`VVU_OFFSET`"),
                   Parameter('p5', type="VV",
                             doc="Output X"),
                   Parameter('p6', type="VV",
                             doc="Output Y")
               ]),

        Method('OffsetCorrect2_VVU', module='geogxx', version='5.1.3',
               availability=Availability.LICENSED, 
               doc="Same as :func:`OffsetCorrect_VVU`, but for an arbitrary offset angle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input X"),
                   Parameter('p2', type="VV",
                             doc="Input Y"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Offset distance"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Offset azimuth (degrees counter-clockwise from straight ahead)"),
                   Parameter('p5', type="VV",
                             doc="Output X"),
                   Parameter('p6', type="VV",
                             doc="Output Y")
               ]),

        Method('OffsetCorrect3_VVU', module='geogxx', version='5.1.4',
               availability=Availability.LICENSED, 
               doc="Same as :func:`OffsetCorrect2_VVU`, but specify smoothing interval.",
               notes="See the algorithm note #2 above for the default smoothing interval.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input X"),
                   Parameter('p2', type="VV",
                             doc="Input Y"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Offset distance"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Offset azimuth (degrees counter-clockwise from straight ahead)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Averaging interval - :def_val:`rDUMMY` for default"),
                   Parameter('p6', type="VV",
                             doc="Output X"),
                   Parameter('p7', type="VV",
                             doc="Output Y")
               ]),

        Method('OffsetCorrectXYZ_VVU', module='geogxx', version='9.0',
               availability=Availability.LICENSED, 
               doc="Correct locations based on heading and fixed offset.",
               notes="""
               In many applications, measurements are taken with an instrument which
               is towed behind, or pushed ahead of where the locations are recorded.
               Use this function to estimate the actual location of the instrument.
               The method determines the heading along the line, using a "thinned"
               version of the line. The default degree of thinning is based on the size of the
               offset; the larger the offset, the greater the distance between sample
               locations used to construct the thinned lined used for determining headings.
               The thinned line is splined at a frequency greater than the sample
               frequency, and the heading at any given point is determined from the
               vector formed by the closest two points on the splined line. The
               correction (behind, in front, left or right) is determined with respect
               to the heading, and added to the original location.
               
               IF this method fails, no dummies, no duplicated locations, no reversals
               are produced.
               
               The algorithm:
               
               1. Determine average distance between each point = D
               2. Default smoothing interval = MAX(2*D, Offset distance) = I
               3. Thin input points to be at least the smoothing interval I apart from each other.
               4. Smoothly re-interpolate the thinned points at five times the
               original average distance D.
               5. For each input point, calculate the bearing using the nearest points
               on the smoothed curve
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input X"),
                   Parameter('p2', type="VV",
                             doc="Input Y"),
                   Parameter('p3', type="VV",
                             doc="Input Z"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Offset along-track (+ve forward)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Offset across-track (+ve to the right)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Vertical Offset (+ve up)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Sampling interval - :def_val:`rDUMMY` for default"),
                   Parameter('p8', type="VV",
                             doc="Output X"),
                   Parameter('p9', type="VV",
                             doc="Output Y"),
                   Parameter('p10', type="VV",
                             doc="Output Z")
               ]),

        Method('OffsetRectangles_VVU', module='geogxx', version='5.0.7',
               availability=Availability.LICENSED, 
               doc="Get non-overlapping offset location for rectangular symbols.",
               notes="""
               Often on maps plotted symbols and text overlap each other.
               This routine accepts of :class:`VV` of locations and returns a new
               set of locations offset from the originals, and guaranteed
               not to overlap, given the size of the original symbols.
               The returned offset X, Y
               locations are offset from the original locations by
               the minimum of a) the input offset, b) the input symbol
               X or Y size. This is to ensure that the original location is
               never covered by the offset symbol. In addition, the offset
               symbol is never place directly below the original location,
               to make it easier to draw a connecting line.
               
               Care should be taken when choosing the symbol size, because
               if the point density is too high, all the points will get
               pushed to the outside edge and your plot will look like a
               hedgehog (it also takes a lot longer!).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input X locations"),
                   Parameter('p2', type="VV",
                             doc="Input Y locations"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="minimum offset distance"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="symbol X size (width)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="symbol Y size (height)"),
                   Parameter('p6', type="VV",
                             doc="Output (offset) X locations"),
                   Parameter('p7', type="VV",
                             doc="Output (offset) Y locations")
               ]),

        Method('PickPeak_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find peaks in a :class:`VV` - method one.",
               notes="""
               Peaks are the maximum point within a sequence of
               positive values in the input :class:`VV`.  The width is the
               number of points in the positive sequence.
               
               A :class:`VV` may have to be pre-filtered before finding
               the peak values:
               
               Use :func:`BPFilt_VVU` to smooth the data as required.
               Use :func:`Filter_VVU` to apply a Laplace filter
               "-0.5,1.0,-0.5" to make curvature data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="input :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="returned peak :class:`VV`, all dummies except peak points."),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="minimum value to accept (0.0 to find all)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="minimum width to accept (1 to find all)")
               ]),

        Method('PickPeak2_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find peaks in a :class:`VV` - method two.",
               notes="""
               Peaks are the maximum point within a sequence of
               values in the input :class:`VV`. Maximum points must be above
               the base level and have a local amplitude greater
               than the minimum amplitude specified.
               
               A :class:`VV` may have to be pre-filtered before finding
               the peak values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="input :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="returned peak :class:`VV`, all dummies except peak points."),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="base level to accept (0.0 to find all)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="minimum amplitude to accept")
               ]),

        Method('PickPeak3_VVU', module='geogxx', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Find peaks in a :class:`VV` - method two, returning width and half-amplitude widths.",
               notes="""
               Uses Method 2 above, but also returns the anomaly width (defined
               as the distance between the surrounding troughs), and the
               width at the half-amplitude. The half-amplitude width is
               calculated in two parts, individually for each side based on
               the distance from the maximum to the location where the
               amplitude is mid-way between the maximum and trough.
               
               The returned VVs are packed; no dummies. Instead the
               indicies of the peak locations are returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="[i] data :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="[i] X :class:`VV` used to calculate distance"),
                   Parameter('p3', type="VV",
                             doc="[i] Y :class:`VV` used to calculate distance"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="[i] minimum value to accept (0.0 to find all)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="[i] amplitude"),
                   Parameter('p6', type="VV",
                             doc="[o] Indices with peak locations"),
                   Parameter('p7', type="VV",
                             doc="[o] Amplitudes at the peaks"),
                   Parameter('p8', type="VV",
                             doc="[o] Anomaly widths"),
                   Parameter('p9', type="VV",
                             doc="[o] Anomaly half-amplitude widths")
               ]),

        Method('PolyFill_VVU', module='geogxx', version='5.0.6',
               availability=Availability.LICENSED, 
               doc="Fill a :class:`VV` with values from an n'th order polynomial, integral x.",
               notes="""
               The output :class:`VV` length must be set as desired before calling.
               
               The X scale is unitless (1 per element), i.e. 0,1,2,3,...
               """,
               see_also=":func:`Trend_VVU`, :func:`Trend2_VVU`, :func:`PolyFill2_VVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` with output data. (Preset length)"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="order of the polynomial 0-9"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` with polynomial coefficients (input)")
               ]),

        Method('PolyFill2_VVU', module='geogxx', version='5.0.6',
               availability=Availability.LICENSED, 
               doc="Fill a :class:`VV` with values from an n'th order polynomial, specified X",
               notes="""
               The output :class:`VV` length must be set as desired before calling.
               The X scale is defined by a X :class:`VV` (see Trend_VV for unitless X).
               """,
               see_also=":func:`Trend_VVU`, :func:`Trend2_VVU`, :func:`PolyFill_VVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` with x spacing (input)"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` with output data. (Preset length)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="order of the polynomial 0-9"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` with polynomial coefficients (order+1 values)")
               ]),

        Method('PolygonMask_VVU', module='geogxx', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Mask a :class:`VV` using XY data and a polygon.",
               notes="The VVs have to be the same length",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` to be masked"),
                   Parameter('p4', type="PLY",
                             doc=":class:`PLY` object"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`VVU_MASK`")
               ]),

        Method('Prune_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Prune values from a :class:`VV` based on reference :class:`VV`",
               notes="""
               Pruning will shorten the :class:`VV` by removing values
               that are either dummy or non-dummy in the reference
               :class:`VV`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` to prune"),
                   Parameter('p2', type="VV",
                             doc="Reference :class:`VV`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`VVU_PRUNE`")
               ]),

        Method('QC_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Qualit control on deviation of data from norm in a :class:`VV`",
               notes="""
               This function tests data in input :class:`VV` against
               two separate criteria. Each element of the output :class:`VV`
               will have one of the following indicators:
               
               Indicator  Meaning
               ---------  --------
                 0        Input data passed both tests
                 1        The input data and is greater than the nominal value
                          plus maximum tolerance/deviation (Criterion #1)
                 2        The input data over a specified distance is greater than the
                                  nominal value plus allowed tolerance (Criterion #2)
                 3        The input data failed on above two tests
                -1        The input data and is less than the nominal value
                          minus maximum tolerance (Criterion #1)
                -2        The input data over a specified distance is less than the
                                  nominal value minus allowed tolerance (Criterion #2)
                -3        The input data failed on above two tests
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="input :class:`VV` on which to apply quality control Required in :def_val:`GS_DOUBLE` or :def_val:`GS_FLOAT`"),
                   Parameter('p2', type="VV",
                             doc="distance :class:`VV` (NULL if criterion #2 does not apply). In :def_val:`GS_DOUBLE` or :def_val:`GS_FLOAT`"),
                   Parameter('p3', type="VV",
                             doc="output flag :class:`VV` with result 0,1,2,3,-1,-2,-3. Required in :def_val:`GS_BYTE`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="nominal reading  (required, must not be :def_val:`GS_R8DM`)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="maximum tolerance/deviation applied to a single reading (criterion #1). :def_val:`GS_R8DM` if criterion #1 does not apply. Otherwise, must be positive value including 0.0"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="allowed tolerance/deviation over a given distance (next parameter) (criterion #2). :def_val:`GS_R8DM` if criterion #2 does not apply. Otherwise, must be positive value including 0.0"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="the specified distance. :def_val:`GS_R8DM` if criterion #2 does not apply. Otherwise, must be positive value excluding 0.0"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`QC_CRITERION`")
               ]),

        Method('RangeVectorMag_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find the range of hypotenuse values of two VVs.",
               notes="""
               For each value in the VVs, finds sqrt(dV1*dV1 + dV2*dV2)
               and returns the min and max values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="First :class:`VV` (X)"),
                   Parameter('p2', type="VV",
                             doc="First :class:`VV` (Y)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Min value (returned)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Max value (returned)")
               ]),

        Method('Regress_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate linear regression through data",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X data"),
                   Parameter('p2', type="VV",
                             doc="Y data"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="returns slope"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="returns intercept")
               ]),

        Method('RelVarDup_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Estimate relative variance of duplicate sample pairs from a database.",
               notes="""
               Created for duplicate sample handling in :class:`CHIMERA`. On input,
               a numeric or text :class:`VV` containing data values, and a sample type :class:`VV`.
               Sample pairs have types "1" and "2". This routine searches for
               types in order "1 2 1 2", and calulates the unnormalized relative variance,
               defined as the sum of the squared differences between duplicates
               divided by the sum of the squared mean values of the duplicates.
               (To get the true rel.var., divide by N-1, where N is the number of
               duplicate pairs used.)
               Samples out of order, unmatched pairs, or when the
               sample type does not equal "1" or "2" are ignored.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Sample Type :class:`VV`"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Returned relative variance"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Returned number of duplicates used.")
               ]),

        Method('RemoveDummy_VVU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Remove dummy values from a :class:`VV`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV")
               ]),

        Method('RemoveDummy2_VVU', module='geogxx', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Remove dummy values from 2 VVs.",
               notes="""
               Removes all indices where either :class:`VV` has a dummy, or is
               not defined (due to length differences).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` object")
               ]),

        Method('RemoveDummy3_VVU', module='geogxx', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Remove dummy values from 3 VVs.",
               notes="""
               Removes all indices where any :class:`VV` has a dummy, or is
               not defined (due to length differences).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` object")
               ]),

        Method('RemoveDummy4_VVU', module='geogxx', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Remove dummy values from 4 VVs.",
               notes="""
               Removes all indices where any :class:`VV` has a dummy, or is
               not defined (due to length differences).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` object")
               ]),

        Method('RemoveDup_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Remove/average duplicate sample pairs from a database.",
               notes="""
               Created for duplicate sample handling in :class:`CHIMERA`. On input,
               a numeric or text :class:`VV` containing data values, and a sample type :class:`VV`.
               Sample pairs have types "1" and "2". This routine searches for
               types in order "1 2 1 2", and replaces the pair of values in the
               data :class:`VV` according to the :def:`VV_DUP` value.
               Results for samples out of order, for unmatched pairs, or when the
               sample type does not equal "1" or "2" remain unchanged.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Data :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Sample Type :class:`VV`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`VV_DUP`")
               ]),

        Method('RemoveXYDup_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Remove/average duplicate samples with the same (X, Y).",
               notes="""
               Searches for duplicated (X, Y) locations and removes the
               duplicates (can be more than just a pair). The "Z" values,
               if defined, are treated according to the value of :def:`VV_XYDUP`.
               The returned VVs are shortened to the new length, without
               duplicates.
               The Z :class:`VV` can be set to NULL on input, in which case it is ignored.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="(optional) Z :class:`VV`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`VV_XYDUP`")
               ]),

        Method('RemoveXYDupIndex_VVU', module='geogxx', version='7.2.0',
               availability=Availability.LICENSED, 
               doc="Remove duplicate samples with the same (X, Y) and update index.",
               notes="""
               Searches for duplicated (X, Y) locations and removes the
               duplicates (can be more than just a pair). The Index :class:`VV` is
               updated accordingly .i.e if  (X,Y) location of Index[0] == Index[1]
               Index[1] is removed.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Index :class:`VV`")
               ]),

        Method('RollingStats_VVU', module='geogxx', version='5.1.0',
               availability=Availability.LICENSED, 
               doc="Calculate a statistic in a rolling window.",
               notes="""
               If the input VVs are not REAL, copies are made to
               temporary REALs for processing.
               
               If the window size is even, it is increased by 1 so that the
               output value is put at the exact center index of the window.
               
               Statistics are calculated on the values in a window
               surrounding the individual data points.
               
               By shrinking the window at the ends, one-sided effects can be
               eliminated. For instance, if the data is linear to begin with,
               a rolling mean will not alter the original data.
               However, if the window size is kept constant, then values
               near the ends tend to be pulled up or down.
               
               With shrinking, the window is shrunk so that it always has the
               same width on both sides of the data point under analysis;
               at the end points the window width is 1, at the next point in
               it is 3, and so on, until the full width is reached.
               
               The median value is calculated by sorting the valid data in
               the window, then selecting the middle value. If the number
               of valid data points is even, then the average of the two
               central values is returned.
               
               The mode value is defined as the value which occurs most
               frequently in the data. This value may not even exist, or
               may not be unique. In this implementation, the following
               algorithm is used: The valid data in the window is sorted
               in ascending order. The number of occurrences of each data
               value is tracked, and if it occurs more times than any
               value, it becomes the modal value. If all
               values are different, this procedure returns the smallest
               value. If two or more values each have the same (maximum)
               number of occurrences, then the smallest of these values is
               returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Output :class:`VV`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`ST_INFO`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Window size (>0, increased to nearest odd value)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Shrink window at ends (1:Yes, 0:No)")
               ]),

        Method('SearchReplace_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Search and replace numeric values in a :class:`VV`.",
               notes="""
               Search comparison is made on double comparison
               of the data.
               """,
               see_also="SearchReplaceText_VV",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="value to replace"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="replacement")
               ]),

        Method('SearchReplaceText_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Search and replace text values in a :class:`VV`",
               notes="""
               Search comparison is made on string comparison
               of the data.
               """,
               see_also="SearchReplace_VV",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="string format for numeric :class:`VV`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="decimals for formating numeric :class:`VV`"),
                   Parameter('p4', type=Type.STRING,
                             doc="formatted string to replace"),
                   Parameter('p5', type=Type.STRING,
                             doc="replacement"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`VVU_SRCHREPL_CASE`")
               ]),

        Method('SearchReplaceTextEx_VVU', module='geogxx', version='6.0.1',
               availability=Availability.LICENSED, 
               doc="Search and replace text values in a :class:`VV`, count items changed.",
               notes="""
               Search comparison is made on a string comparison
               of the data.
               """,
               see_also="SearchReplaceText_VV",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="string format for numeric :class:`VV`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="decimals for formating numeric :class:`VV`"),
                   Parameter('p4', type=Type.STRING,
                             doc="formatted string to replace"),
                   Parameter('p5', type=Type.STRING,
                             doc="replacement"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`VVU_SRCHREPL_CASE`"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="number of items replaced (returned)")
               ]),

        Method('Spline_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Spline a Y :class:`VV` onto an X :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X (no dummies)"),
                   Parameter('p2', type="VV",
                             doc="Y to be splined (no dummies)"),
                   Parameter('p3', type="VV",
                             doc="Y output"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="output Length"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Starting Location"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Separation Distance"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Maximum gap to interpolate across"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Number of elements to extend"),
                   Parameter('p9', type=Type.INT32_T,
                             doc=":def:`VVU_SPL`")
               ]),

        Method('Spline2_VVU', module='geogxx', version='5.1.3',
               availability=Availability.LICENSED, 
               doc="Spline a Y :class:`VV` onto an X :class:`VV`. Uses specified values of X in X2",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X (no dummies)"),
                   Parameter('p2', type="VV",
                             doc="Y to be splined (no dummies)"),
                   Parameter('p3', type="VV",
                             doc="X2 (no dummies)"),
                   Parameter('p4', type="VV",
                             doc="Y output"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`VVU_SPL`")
               ]),

        Method('iTokenizeToValues_VVU', module='geogxx', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Tokenize a string based on any characters.",
               notes="Parses a series of space, tab or comma-delimited values to a :class:`VV`.",
               return_type=Type.INT32_T,
               return_doc="number of tokens (length of :class:`VV`)",
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` to place values in"),
                   Parameter('p2', type=Type.STRING,
                             doc="str - String to parse")
               ]),

        Method('Translate_VVU', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Translate values in a :class:`VV`",
               notes="(new :class:`VV`) = ((old :class:`VV`) + base) * scale",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="base"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="scale")
               ]),

        Method('Trend_VVU', module='geogxx', version='5.0.6',
               availability=Availability.LICENSED, 
               doc="Calculate an n'th order best-fit polynomial, integral x.",
               notes="""
               Returns coefficients c[0] .. c[n]
               
                  Y(x) = c[0] + c[1]x + c[2](x**2) + ... + c[n](x**n)
               
               The X scale is unitless (1 per element), i.e. 0,1,2,3,...
               
               The polynomial :class:`VV` length is set to the number of coefficients
               (order + 1)
               """,
               see_also=":func:`PolyFill_VVU`, :func:`Trend2_VVU`, :func:`PolyFill2_VVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` with input data"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="order of the polynomial 0-9"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` to hold polynomial coefficients (returned).")
               ]),

        Method('Trend2_VVU', module='geogxx', version='5.0.6',
               availability=Availability.LICENSED, 
               doc="Calculate an n'th order best-fit polynomial, specified X",
               notes="""
               Returns coefficients c[0] .. c[n]
               
                  Y(x) = c[0] + c[1]x + c[2](x**2) + ... + c[n](x**n)
               
               The X scale is defined by a X :class:`VV` (see Trend_VV for unitless X).
               
               The polynomial :class:`VV` length is set to the number of coefficients
               (order + 1)
               """,
               see_also=":func:`PolyFill_VVU`, :func:`Trend2_VVU`, :func:`PolyFill2_VVU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` with x spacing (input)"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` with input data"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="order of the polynomial 0-9"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` to hold polynomial coefficients (returned)")
               ]),

        Method('UniformDist_VVU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Fill with uniformly distributed values.",
               notes="""
               :class:`VV` is set to input length (except for -1)
               See rand.gxh for a short discription of the
               random number generator used.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Random number generator seed"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Minimum of range"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Maximum of range"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Number of values (-1 for all)")
               ])
    ],
    'Obsolete': [

        Method('OffsetCorrect4_VVU', module='geogxx', version='7.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Same as :func:`OffsetCorrect3_VVU`, but specify roll, pitch, yaw and Z.",
               notes="Add roll, pitch, yaw correction.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input X"),
                   Parameter('p2', type="VV",
                             doc="Input Y"),
                   Parameter('p3', type="VV",
                             doc="Input Z"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="ZOffset distance"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="XYOffset distance"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="XYOffset azimuth (degrees clockwise from straight ahead)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Averaging interval - :def_val:`rDUMMY` for default"),
                   Parameter('p8', type="VV",
                             doc="Roll"),
                   Parameter('p9', type="VV",
                             doc="Pitch"),
                   Parameter('p10', type="VV",
                             doc="Yaw"),
                   Parameter('p11', type="VV",
                             doc="Output X"),
                   Parameter('p12', type="VV",
                             doc="Output Y"),
                   Parameter('p13', type="VV",
                             doc="Output Z")
               ])
    ]
}

