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
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`VVU_DUMMYREPEAT`")
               ]),

        Method('DupStats_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate means and differences for duplicate sample pairs",
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
               return_type=Type.INT32_T,
               return_doc="The number of items dummied in order to render the :class:`VV` montonically increasing.",
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` handle")
               ]),

        Method('iFindDummy_VVU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find the first dummy|non-dummy value in :class:`VV`",
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

