from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('PGU',
                 doc="""
                 A collection of methods applied to :class:`PG` objects, including
                 fills, trending and 2-D :class:`FFT` operations.
                 """)


gx_defines = [
    Define('BLAKEY_TEST',
           doc="Types of BLAKEY tests",
           constants=[
               Constant('BLAKEY_TEST_ONESIDE', value='1', type=Type.INT32_T)                        ,
               Constant('BLAKEY_TEST_TWOSIDE', value='2', type=Type.INT32_T)                        ,
               Constant('BLAKEY_TEST_THREESIDE', value='3', type=Type.INT32_T)                        ,
               Constant('BLAKEY_TEST_FOURSIDE', value='4', type=Type.INT32_T)                        
           ]),

    Define('PGU_CORR',
           doc="Correlation (must be synchronized with :def:`ST2_CORRELATION`)",
           constants=[
               Constant('PGU_CORR_SIMPLE', value='0', type=Type.INT32_T,
                        doc="Simple correlation")                        ,
               Constant('PGU_CORR_PEARSON', value='1', type=Type.INT32_T,
                        doc="Pearson's correlation (normalized to standard deviations)")                        
           ]),

    Define('PGU_DIRECTGRID',
           doc="Type of statistic to use on the data points in each cell.",
           constants=[
               Constant('PGU_DIRECTGRID_MINIMUM', value='0', type=Type.INT32_T,
                        doc="Select the minimum value found in each cell")                        ,
               Constant('PGU_DIRECTGRID_MAXIMUM', value='1', type=Type.INT32_T,
                        doc="Select the maximum value found in each cell")                        ,
               Constant('PGU_DIRECTGRID_MEAN', value='2', type=Type.INT32_T,
                        doc="Select the mean of all values found in each cell")                        ,
               Constant('PGU_DIRECTGRID_ITEMS', value='3', type=Type.INT32_T,
                        doc="The number of valid (non-dummy) items found in each cell")                        
           ]),

    Define('PGU_DIRECTION',
           doc="Direction",
           constants=[
               Constant('PGU_FORWARD', value='0', type=Type.INT32_T,
                        doc="""
                        Forward direction: Removes mean and standard deviation,
                        storing the values in the VVs.
                        """)                        ,
               Constant('PGU_BACKWARD', value='1', type=Type.INT32_T,
                        doc="""
                        Backward direction: Applies mean and standard deviation
                        values in the VVs to the data.
                        """)                        
           ]),

    Define('PGU_TRANS',
           doc="transform methods for the columns",
           constants=[
               Constant('PGU_TRANS_NONE', value='0', type=Type.INT32_T)                        ,
               Constant('PGU_TRANS_LOG', value='1', type=Type.INT32_T)                        
           ]),

    Define('PGU_INTERP_ORDER',
           doc="interpolation direction order",
           constants=[
               Constant('PGU_INTERP_ORDER_XYZ', value='0', type=Type.INT32_T)                        ,
               Constant('PGU_INTERP_ORDER_XZY', value='1', type=Type.INT32_T)                        ,
               Constant('PGU_INTERP_ORDER_YXZ', value='2', type=Type.INT32_T)                        ,
               Constant('PGU_INTERP_ORDER_YZX', value='3', type=Type.INT32_T)                        ,
               Constant('PGU_INTERP_ORDER_ZXY', value='4', type=Type.INT32_T)                        ,
               Constant('PGU_INTERP_ORDER_ZYX', value='5', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'General': [

        Method('Bool_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Apply reference file boolean mask to pager",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="pager obj"),
                   Parameter('p2', type=Type.STRING,
                             doc="sRefFil - reference file for boolean mask flag.")
               ]),

        Method('DirectGriddingDAT_PGU', module='geogxx', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Direct-gridding method, :class:`DAT` version.",
               notes="""
               Grid cells take on the specified statistic of the values inside the
               cell area. Grid cells containing no data values are set to dummy.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input grid"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X origin of grid"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y origin of grid"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X cell size"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y cell size"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="rotation angle (degrees CCW)."),
                   Parameter('p7', type="DAT",
                             doc=":class:`DAT` source"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`PGU_DIRECTGRID`")
               ]),

        Method('DirectGriddingDAT3D_PGU', module='geogxx', version='8.0.0',
               availability=Availability.LICENSED, 
               doc="Direct-gridding method, :class:`DAT` version, 3D.",
               notes="""
               3D grid cells take on the specified statistic of the values inside the
               cell area. Grid cells containing no data values are set to dummy.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input 3D :class:`PG`"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X origin of 3D grid"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y origin of 3D grid"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z origin of 3D grid"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X cell size"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Y cell size"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Z cell size"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="rotation angle (degrees CCW, vertical axis only)."),
                   Parameter('p9', type="DAT",
                             doc="3D :class:`DAT` source"),
                   Parameter('p10', type=Type.INT32_T,
                             doc=":def:`PGU_DIRECTGRID`")
               ]),

        Method('DirectGriddingDB_PGU', module='geogxx', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Direct-gridding method, :class:`DB` version.",
               notes="""
               Grid cells take on the specified statistic of the values inside the
               cell area. Grid cells containing no data values are set to dummy.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input grid"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X origin of grid"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y origin of grid"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X cell size"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y cell size"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="rotation angle (degrees CCW)."),
                   Parameter('p7', type="DB",
                             doc="Database"),
                   Parameter('p8', type="DB_SYMB",
                             doc="X Channel [READONLY]"),
                   Parameter('p9', type="DB_SYMB",
                             doc="Y Channel [READONLY]"),
                   Parameter('p10', type="DB_SYMB",
                             doc="Data Channel [READONLY]"),
                   Parameter('p11', type=Type.INT32_T,
                             doc=":def:`PGU_DIRECTGRID`")
               ]),

        Method('DirectGriddingDB3D_PGU', module='geogxx', version='8.0.0',
               availability=Availability.LICENSED, 
               doc="Direct-gridding method, :class:`DB` version, 3D.",
               notes="""
               3D grid cells take on the specified statistic of the values inside the
               cell area. Grid cells containing no data values are set to dummy.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input 3D :class:`PG`"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X origin of 3D grid"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y origin of 3D grid"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z origin of 3D grid"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X cell size"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Y cell size"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Z cell size"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="rotation angle (degrees CCW, vertical axis only)."),
                   Parameter('p9', type="DB",
                             doc="Database"),
                   Parameter('p10', type="DB_SYMB",
                             doc="X Channel [READONLY]"),
                   Parameter('p11', type="DB_SYMB",
                             doc="Y Channel [READONLY]"),
                   Parameter('p12', type="DB_SYMB",
                             doc="Z Channel [READONLY]"),
                   Parameter('p13', type="DB_SYMB",
                             doc="Data Channel [READONLY]"),
                   Parameter('p14', type=Type.INT32_T,
                             doc=":def:`PGU_DIRECTGRID`")
               ]),

        Method('DirectGriddingVV_PGU', module='geogxx', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="Direct-gridding method, :class:`VV` version.",
               notes="""
               Grid cells take on the specified statistic of the values inside the
               cell area. Grid cells containing no data values are set to dummy.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input grid"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X origin of grid"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y origin of grid"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X cell size"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y cell size"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="rotation angle (degrees CCW)."),
                   Parameter('p7', type="VV",
                             doc="X locations of values"),
                   Parameter('p8', type="VV",
                             doc="Y locations of values"),
                   Parameter('p9', type="VV",
                             doc="Z values to grid"),
                   Parameter('p10', type=Type.INT32_T,
                             doc=":def:`PGU_DIRECTGRID`")
               ]),

        Method('Expand_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Expand a pager by filling the dummies for expanded edges",
               notes="3D pagers are expanded in X,Y direction the number of slices(Z) is unchanged .",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="original pager obj"),
                   Parameter('p2', type="PG",
                             doc="expanded pager obj"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="% expansion"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="option  0 - rectangular, 1 - square"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="X dimension to expand to (0 for expansion to FFT2D legal dimension)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Y dimension to expand to (0 for expansion to FFT2D legal dimension)")
               ]),

        Method('Fill_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Replace all dummies in a pager by predict values.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="pager obj"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Roll off weighting option: 1 - linear, 2 - square"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="dRollBase - the value to roll off to, :def_val:`GS_R8DM` for roll off to mean value line by line."),
                   Parameter('p4', type=Type.INT32_T,
                             doc="lRollDist - (at unit of cell dist.) for roll-off. 0 for no roll of, -1 for the default: 2 times of min. dummy edge dim."),
                   Parameter('p5', type=Type.INT32_T,
                             doc="lMxf - max. filter length.  -1 for no max. entropy. 0 for the default of MIN(minimum dummy edge dim, 32)."),
                   Parameter('p6', type=Type.INT32_T,
                             doc="lMxp - max. pred. sample 0 for the default of 2*lMxf."),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="dAmpLmt - limit (abs. value) amplitudes to this level. Amplitudes are limited starting at half this value. <=0.0 for no amp limit."),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="dEdgeLmt - limit edge (abs. value) amplitudes to this level. <0.0 for no edge limit."),
                   Parameter('p9', type=Type.INT32_T,
                             doc="lEdgeWidth - within this dist. (at unit of cell size) for amp. limited. -1 for no edge limit. 0 for the default of minimum dummy edge dim."),
                   Parameter('p10', type=Type.INT32_T,
                             doc="iNPass - number of time to pass smooth filter"),
                   Parameter('p11', type=Type.STRING,
                             doc="sRefFil - reference file for smooth filter flag.")
               ]),

        Method('FillValue_PGU', module='geogxx', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Set all values in a pager to a single value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="pager obj"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Value to set in pager")
               ]),

        Method('FiltSym_PGU', module='geogxx', version='5.1.5',
               availability=Availability.LICENSED, 
               doc="Apply 5x5, 7x7 or 9X9 symmetric convolution filter to a :class:`PG`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="pager obj"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="number of time to pass smooth filter"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="flag to use filter file"),
                   Parameter('p4', type=Type.STRING,
                             doc="file for filter values"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="size of filter window, 5/7/9"),
                   Parameter('p6', type="VV",
                             doc="array of 6/10/15 filter coefficients")
               ]),

        Method('FiltSym5_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Apply 5x5 symmetric convolution filter to a :class:`PG`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="pager obj"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="number of time to pass smooth filter"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="flag to use filter file"),
                   Parameter('p4', type=Type.STRING,
                             doc="file for filter values"),
                   Parameter('p5', type="VV",
                             doc="array of 6 filter coefficients at position 00, 10, 11, 20, 21, 22. Symmetric filters look like : 22 21 20 21 22 21 11 10 11 21 20 10 00 10 20 21 11 10 11 21 22 21 20 21 22")
               ]),

        Method('GridPeak_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Pick grid peaks.",
               notes="""
               Blakey test limit defines how grid peaks are to be found.
               For example, with the :def_val:`BLAKEY_TEST_ONESIDE`, a grid
               point will be picked if its grid value is greater than
               the value of one or more of its four neighouring points.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Grid file name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`BLAKEY_TEST`"),
                   Parameter('p3', type="VV",
                             doc="X of found peaks"),
                   Parameter('p4', type="VV",
                             doc="Y of found peaks"),
                   Parameter('p5', type="VV",
                             doc="Z values of found peaks")
               ]),

        Method('IDWGriddingDAT_PGU', module='geogxx', version='7.3.0',
               availability=Availability.LICENSED, 
               doc=":func:`IDWGriddingDAT_PGU`     Inverse-distance weighting gridding method, :class:`DAT` version.",
               notes="See the notes for :func:`IDWGriddingDB_PGU`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input grid"),
                   Parameter('p2', type="DAT",
                             doc=":class:`DAT` source"),
                   Parameter('p3', type="REG",
                             doc="Parameters (see above)")
               ]),

        Method('IDWGriddingDAT3D_PGU', module='geogxx', version='8.0.0',
               availability=Availability.LICENSED, 
               doc=":func:`IDWGriddingDAT3D_PGU`     Inverse-distance weighting gridding method, :class:`DAT` version, 3D.",
               notes="See the notes for :func:`IDWGriddingDB3D_PGU`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input 3D :class:`PG`"),
                   Parameter('p2', type="DAT",
                             doc=":class:`DAT` source"),
                   Parameter('p3', type="REG",
                             doc="Parameters (see above)")
               ]),

        Method('IDWGriddingDB_PGU', module='geogxx', version='7.3.0',
               availability=Availability.LICENSED, 
               doc=":func:`IDWGriddingDB_PGU`     Inverse-distance weighting gridding method, :class:`DB` version.",
               notes="""
               Grid cells take on the averaged values within a search radius, weighted inversely by distance.
               
               Weighting can be controlled using the power and slope properties;
               
               weighting = 1 / (distance^wtpower + 1/slope) where distance is in
               units of grid cells (X dimenstion). Default is 0.0,
               
               If the blanking distance is set, all cells whose center point is not within the blanking distance of
               at least one data point are set to dummy.
               
               :class:`REG` Parameters:
               
               X0, Y0, DX, DY: Grid origin, and cell sizes (required)
               WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters
               SEARCH_RADIUS: Distance weighting limit (default = 4 * SQRT(DX*DY))
               BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 * SQRT(DX*DY))
               LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?
               LOG_BASE: One of :def_val:`VV_LOG_BASE_10` (default) or :def_val:`VV_LOG_BASE_E`
               LOG_NEGATIVE: One of :def_val:`VV_LOG_NEGATIVE_NO` (default) or :def_val:`VV_LOG_NEGATIVE_YES`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input grid"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Channel [READONLY]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Channel [READONLY]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Data Channel [READONLY]"),
                   Parameter('p6', type="REG",
                             doc="Parameters (see above)")
               ]),

        Method('IDWGriddingDB3D_PGU', module='geogxx', version='8.0.0',
               availability=Availability.LICENSED, 
               doc=":func:`IDWGriddingDB3D_PGU`     Inverse-distance weighting gridding method, :class:`DB` version, 3D.",
               notes="""
               3D cells take on the averaged values within a search radius, weighted inversely by distance.
               
               Weighting can be controlled using the power and slope properties;
               
               weighting = 1 / (distance^wtpower + 1/slope) where distance is in
               units of grid cells (X dimenstion). Default is 0.0,
               
               If the blanking distance is set, all cells whose center point is not within the blanking distance of
               at least one data point are set to dummy.
               
               :class:`REG` Parameters:
               
               X0, Y0, Z0, DX, DY, DZ: Grid origin, and cell sizes (required)
               WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters
               SEARCH_RADIUS: Distance weighting limit (default = 4 * CUBE_ROOT(DX*DY*DZ))
               BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 * CUBE_ROOT(DX*DY*DZ))
               LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?
               LOG_BASE: One of :def_val:`VV_LOG_BASE_10` (default) or :def_val:`VV_LOG_BASE_E`
               LOG_NEGATIVE: One of :def_val:`VV_LOG_NEGATIVE_NO` (default) or :def_val:`VV_LOG_NEGATIVE_YES`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input 3D :class:`PG`"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type="DB_SYMB",
                             doc="X Channel [READONLY]"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Y Channel [READONLY]"),
                   Parameter('p5', type="DB_SYMB",
                             doc="Z Channel [READONLY]"),
                   Parameter('p6', type="DB_SYMB",
                             doc="Data Channel [READONLY]"),
                   Parameter('p7', type="REG",
                             doc="Parameters (see above)")
               ]),

        Method('IDWGriddingVV_PGU', module='geogxx', version='7.3.0',
               availability=Availability.LICENSED, 
               doc=":func:`IDWGriddingVV_PGU`     Inverse-distance weighting gridding method, :class:`VV` version.",
               notes="See the notes for :func:`IDWGriddingDB_PGU`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input grid"),
                   Parameter('p2', type="VV",
                             doc="X locations"),
                   Parameter('p3', type="VV",
                             doc="Y locations"),
                   Parameter('p4', type="VV",
                             doc="Data values to grid"),
                   Parameter('p5', type="REG",
                             doc="Parameters (see above)")
               ]),

        Method('NumericToThematic_PGU', module='geogxx', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="""
               :func:`NumericToThematic_PGU`    Set index values in a pager based on a numeric pager with translation :class:`VV`.
               
               Returns			  Nothing
               """,
               notes="""
               The values in the input data :class:`VV` represent the center-of-range
               values of unique properties with indices 0 to N-1, where N
               is the number of items in the input :class:`VV`.
               
               This :class:`VV` is sorted from smallest to largest, and each value in
               in the input numeric :class:`PG` is tested to see into which range it goes.
               The closest range value for each item is used, so the half-way point
               is the dividing point. The top and bottom-most range widths are determined
               by the "inside half-width" to the nearest range.
               
               The INDEX of the closest range is then inserted into the output :class:`PG`, so
               it can be used in a thematic voxel (for instance).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Input numeric :class:`PG`"),
                   Parameter('p2', type="VV",
                             doc="Translation :class:`VV` (see notes above)"),
                   Parameter('p3', type="PG",
                             doc="Output thematic :class:`PG`")
               ]),

        Method('Peakedness_PGU', module='geogxx', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Find all peaks in peakedneess grid pager",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Grid file name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Cutoff limit for finding peaks"),
                   Parameter('p3', type="VV",
                             doc="X of found peaks"),
                   Parameter('p4', type="VV",
                             doc="Y of found peaks"),
                   Parameter('p5', type="VV",
                             doc="Z values of found peaks")
               ]),

        Method('PeakednessGrid_PGU', module='geogxx', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Create peakedneess grid from input grid.",
               notes="""
               This function creates a peakedneess grid from input grid.
               Radius, is the maximum radius at which the value of the parent pixel is compared to
               the value of surrounding pixels.
               PercentLesser, is used to indicate the percentage of pixels at each radii smaller than
               or equal to Radius that must have value lower than the parent pixel in order to call
               that radius true or equal to 1.
               Description:  For each pixel in the grid a series of radii are evaluated from 1 to Radius.
               If the percentage of pixels for a given radius is less than PercentLesser the parent pixel
               receives an additional 1.
               For examples if the Radius is set to 5 and the PercentLesser is set to 70%.
               And radius 1 = 90%, radius 2 = 85%, radius 3 = 75%, radius 4 = 70% and radius 5 = 65%
               then the parent pixel would receive 1+1+1+1+0 = 4.
               Use:  This function is useful in isolating the anomaly peaks in data that has a large
               value range for anomalies. For example the 1 mV anomaly could quite possibly have
               the same representation as the 100 mV anomaly using this function.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input grid file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output grid (peakedness) file name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Radius"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="PercentLess")
               ]),

        Method('RefFile_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a reference file (boolean mask flag) from pager.",
               notes="""
               A reference file is a binary file with the following format:
               
               The first 8 bytes are the pager dimensions NX and NY as longs.
               The remaining bits, one bit per pager cell - (NX * NY)/8 bytes
               are zero where the pager is dummy, and 1 where the pager is defined.
               
               The reference file is used in various operations where it is
               necessary to mask some output to the original defined cells.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc=":class:`PG` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Reference file name")
               ]),

        Method('SaveFile_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Writes a :class:`PG` to an image file.",
               notes="The trend object and projection are optional.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input :class:`PG` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X origin"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y origin"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="DX"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="DY"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="rotation angle"),
                   Parameter('p7', type="TR",
                             doc="Trend information or NULL"),
                   Parameter('p8', type="IPJ",
                             doc="Projection or NULL"),
                   Parameter('p9', type=Type.STRING,
                             doc="Output file name")
               ]),

        Method('ThematicToNumeric_PGU', module='geogxx', version='7.3.0',
               availability=Availability.LICENSED, 
               doc="""
               Set numeric values in a pager based on an index pager with translation :class:`VV`.
               
               Returns			  Nothing
               """,
               notes="""
               The items in the input data :class:`VV` are inserted into
               the output :class:`PG` using the indices in the index :class:`PG`.
               
               This function is useful when converting a thematic voxel, which is
               type :def_val:`GS_LONG` and contains indices into its own internal :class:`TPAT`
               object, and you provide a numeric mapping :class:`VV`, calculated using
               SetupTranslateToNumericVV_TPAT.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Input Index :class:`PG`"),
                   Parameter('p2', type="VV",
                             doc="Translation :class:`VV`"),
                   Parameter('p3', type="PG",
                             doc="Output Data :class:`PG`")
               ]),

        Method('Trend_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Trend remove or replace back in pager",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="original pager obj"),
                   Parameter('p2', type="PG",
                             doc="trended pager obj"),
                   Parameter('p3', type="TR",
                             doc="trend obj"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="option  0 - calculate, 1 - given in :class:`TR`, 2 - replace back from :class:`TR`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="trend base on: 0 - all points, 1 - edge points"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="trend orogin  rXo,"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="trend orogin  rYo,"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="inclrement in X directon  rDx,"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="inclrement in Y directon  rDy")
               ])
    ],
    'Math Operations': [

        Method('AddScalar_PGU', module='geogxx', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="Add a scalar value to a pager",
               notes="Only available for FLOAT or DOUBLE pagers",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Pager"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Scalar Value")
               ]),

        Method('MultiplyScalar_PGU', module='geogxx', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="Multiply a scalar value and a pager",
               notes="Only available for FLOAT or DOUBLE pagers",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Pager"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Scalar Value")
               ])
    ],
    'Matrix Operation': [

        Method('CorrelationMatrix_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find the correlations between columns in a matrix",
               notes="""
               The input matrix is M rows by N columns. The returned matrix
               is a symmetric N by N matrix whose elements are the normalized
               dot products of the columns of the input matrix with themselves.
               The elements take on values from 0 (orthogonal) to 1 (parallel).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input matrix"),
                   Parameter('p2', type="PG",
                             doc="returned correlation matrix")
               ]),

        Method('CorrelationMatrix2_PGU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Same as :func:`CorrelationMatrix_PGU`, but select correlation type.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input matrix"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`PGU_CORR`"),
                   Parameter('p3', type="PG",
                             doc="returned correlation matrix")
               ]),

        Method('InvertMatrix_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Inverts a square matrix using LU decomp. and back-substitution",
               notes="""
               This is an "in-place" operation, and set up so that the input and
               output pagers may be the same handle. (If they are different, the
               input pager remains unchanged).
               Pagers and VVs must be type REAL.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Input matrix"),
                   Parameter('p2', type="PG",
                             doc="Output inverted matrix (can be same as input).")
               ]),

        Method('Jacobi_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find eigenvalues, eigenvectors of a real symmetric matrix.",
               notes="""
               The number of rows must equal the number of columns.
               Eienvalues, vectors are sorted in descending order.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Input Pager"),
                   Parameter('p2', type="VV",
                             doc="Eigenvalues (returned)"),
                   Parameter('p3', type="PG",
                             doc="Eigenvectors (returned)")
               ]),

        Method('LUBackSub_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Solve a linear system using LU decomposition and back-substitution.",
               notes="""
               Solves the system Ax = b for a given b, using the LU decomposition
               of the matrix a
               The LU decomposition and the permutation vector are obtained
               from :func:`LUBackSub_PGU`.
               Pagers and VVs must be type REAL except for the permutation vector,
               which should be INT
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="LU decomposition of A"),
                   Parameter('p2', type="VV",
                             doc="permutation vector (type INT)"),
                   Parameter('p3', type="VV",
                             doc="right hand side vector B (input)"),
                   Parameter('p4', type="VV",
                             doc="solution vector (output)")
               ]),

        Method('LUDecomp_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Perform an LU decomposition on a square pager.",
               notes="""
               The L and U matrix are both contained in the returned pager; The
               "L" matrix is composed of the sub-diagonal elements of the output
               pager, as well as "1" values on the diagonal. The "U" matrix is
               composed of the diagonal elements (sub-diagonal elements set to 0).
               This is an "in-place" operation, and set up so that the input and
               output pagers may be the same handle. (If they are different, the
               input pager remains unchanged).
               The LU decomposition, and the permutation vector are used for
               :func:`LUBackSub_PGU`.
               Pagers must be type REAL and the permutation vector type INT
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input"),
                   Parameter('p2', type="PG",
                             doc="LU decomposition (may be same pager as input)"),
                   Parameter('p3', type="VV",
                             doc="permutation vector (type INT)")
               ]),

        Method('MatrixMult_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Multiply two pagers as if they were matrices.",
               notes="""
               The matrices must be correctly dimensioned, taking into
               account whether transposition should occur before
               multiplication. The input matrices are not altered on output (even
               if transposition is requested).
               Assertions if: Matrices are not expected sizes
               Dummies are treated as 0 values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="matrix U"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="TRUE (1) if U should be transposed before multiplication"),
                   Parameter('p3', type="PG",
                             doc="matrix V"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="TRUE (1) if V should be transposed before multiplication"),
                   Parameter('p5', type="PG",
                             doc="returned matrix U*V")
               ]),

        Method('MatrixVectorMult_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Multiply a :class:`VV` by a pager like a matrix*vector multiply.",
               notes="""
               The matrix is input as an M rows (data) by N columns (variables) :class:`PG`.
               The vector must be of length N. The output :class:`VV` is set to length M.
               The :class:`PG` and VVs must be type :def_val:`GS_DOUBLE`.
               Terminates if: Matrices, :class:`VV` are not expected sizes (taken from U)
                              PGs are not REAL.
               Dummies are treated as 0 values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="matrix U"),
                   Parameter('p2', type="VV",
                             doc="vector x"),
                   Parameter('p3', type="VV",
                             doc="returned vector U*x")
               ]),

        Method('SVDecompose_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Do a singular value decomposition on a matrix stored as a :class:`PG`",
               notes="""
               The matrix is input as an N rows (data) by M columns (variables) :class:`PG`.
               On return, the matrix is decomposed to A = U * W * Vt.
               If M<N, then an error will be registered. In this case, augment the
               "A" :class:`PG` with rows of zero values.
               The input matrices must be A[M,N], U[M.N] and V[N,N]. The length of the W :class:`VV`
               is set by sSVD_PGU to N.
               The Pagers must be type REAL.
               Terminates if: U is not M by N. (Taken from size of A)
                              V is not N by N. (Taken from #columns in A).
                              PGs, :class:`VV` are not REAL
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Input A matrix, M data (rows), N variables (columns)"),
                   Parameter('p2', type="PG",
                             doc="The returned U Matrix"),
                   Parameter('p3', type="VV",
                             doc="Returned weights (W)"),
                   Parameter('p4', type="PG",
                             doc="Returned V matrix")
               ]),

        Method('SVRecompose_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Reconstitute the original matrix from an SVD.",
               notes="""
               The matrix is input as an N rows (data) by M columns (variables) :class:`PG`.
               On return, the matrix is decomposed to A = U * W * Vt.
               If M<N, then an error will be registered. In this case, augment the
               "A" :class:`PG` with rows of zero values.
               The input matrices must be A[M,N], U[M.N] and V[N,N]. The length of the W :class:`VV`
               is set by sSVDecompose_PGU to N.
               The Pagers must be type :def_val:`GS_DOUBLE`.
               Terminates if: U is not M by N. (Taken from size of A)
                              V is not N by N. (Taken from #columns in A).
                              PGs, :class:`VV` are not REAL.
               Dummies are treated as 0 values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="U matrix"),
                   Parameter('p2', type="VV",
                             doc="Weights (W)"),
                   Parameter('p3', type="PG",
                             doc="V matrix"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Minimum weight to use (Dummy for all)"),
                   Parameter('p5', type="PG",
                             doc="A matrix (returned)")
               ])
    ],
    'Principal Component Analysis': [

        Method('PCCommunality_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Determines principal component communalities.",
               notes="""
               Calculate communalities (sums of the squares of the column
               values in each row)
               Pagers and VVs must be type :def_val:`GS_DOUBLE`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Input pager of the principal components"),
                   Parameter('p2', type="VV",
                             doc="returned communality values")
               ]),

        Method('PCLoadings_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Compute the principal component loadings from the standardized data.",
               notes="""
               Works on columns of the :class:`PG`.
               Calculates the correlation matrix from the columns of the
               standardized data, then computes the eigen values and eigenvectors
               of the correlation matrix. The loadings are the eigenvectors, ordered
               by descending eigenvalues, scaled by the square root of the
               eigenvalues. The returned pager must be sized the same as the
               input pager.
               Correlations are performed using ":def_val:`PGU_CORR_SIMPLE`", so if you want
               Pearson correlations, or wish to use a modified correlation matrix,
               use :func:`PCLoadings2_PGU` and input the correlation matrix directly.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="standardized data matrix (M by N)"),
                   Parameter('p2', type="PG",
                             doc="principal component loadings (N by N)")
               ]),

        Method('PCLoadings2_PGU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Same as PCLoading_PGU, but input correlation matrix.",
               notes="See :func:`PCLoadings_PGU`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="correllation matrix (N by N)"),
                   Parameter('p2', type="PG",
                             doc="principal component loadings (N by N)")
               ]),

        Method('PCScores_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Compute the principal component scores from the standardized data.",
               notes="""
               t  -1
               Forms the product X Ap (Ap Ap),  where X is the
               standardized data matrix, and Ap is the matrix of
               principal component loadings (see :func:`PCLoadings_PGU`).
               The loadings must be input, and can be calculated by calling
               :func:`PCLoadings_PGU`.
               Pagers and VVs must be type :def_val:`GS_DOUBLE`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="standardized data matrix  (M by N)"),
                   Parameter('p2', type="PG",
                             doc="principal component loadings (input) (N by L, L<=N)"),
                   Parameter('p3', type="PG",
                             doc="principal component scores (returned) (M by L, L<=N)")
               ]),

        Method('PCStandardize_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Remove/Replace mean and standard deviation",
               notes="Works on columns of the :class:`PG`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="matrix to standardize"),
                   Parameter('p2', type="VV",
                             doc="means"),
                   Parameter('p3', type="VV",
                             doc="standard deviations"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`PGU_DIRECTION`")
               ]),

        Method('PCStandardize2_PGU', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Remove/Replace mean and standard deviation, subset values.",
               notes="""
               Like :func:`PCStandardize_PGU`, except that not all the values are
               included in the calculation of the means and standard
               deviations. The inclusion is controlled by a mask :class:`VV`,
               The rows where the mask is dummy are not included
               in the calculation, but ALL the values are standardized.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="matrix to standardize"),
                   Parameter('p2', type="VV",
                             doc="mask :class:`VV` for data selection (forward only)"),
                   Parameter('p3', type="VV",
                             doc="means"),
                   Parameter('p4', type="VV",
                             doc="standard deviations"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="forward or reverse")
               ]),

        Method('PCTransform_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Transform/De-transform data.",
               notes="""
               Works on columns of the :class:`PG`.
               Forward direction: Applies the selected transform to the data.
               Backward direction: Applies the inverse transform to the data.
               The detection limits are input with a :class:`VV`. In the forward
               transform, data values less than the detection limit are set
               to the limit.
               The factor limits are input with a :class:`VV`. In the forward
               transform, data values greater than the maximum values are set
               to the maximum.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="matrix to transform"),
                   Parameter('p2', type="VV",
                             doc="detection limits for the columns"),
                   Parameter('p3', type="VV",
                             doc="maximum values for the columns"),
                   Parameter('p4', type="VV",
                             doc=":def:`PGU_TRANS`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`PGU_DIRECTION`")
               ]),

        Method('PCVarimax_PGU', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Perform the Kaiser Varimax transformation on pr. comp. loadings",
               notes="""
               Rotates the principal components using the Kaiser's varimax
               scheme to move move each factor axis to positions so that
               projections from each variable on the factor axes are either
               near the extremities or near the origin.
               Pagers must be type :def_val:`GS_DOUBLE`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="principal component loadings (input) (N by M, M<=N)"),
                   Parameter('p2', type="PG",
                             doc="rotated principal component loadings (returned) (N by L, L<=M)")
               ])
    ],
    'Specialized Operations': [

        Method('rMaximumTerrainSteepness_PGU', module='geogxx', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="Compute the Maximum Steepness of a topography Pager",
               notes="""
               Calculates forward-looking slopes SX and SY in the X and Y directions
               using pager locations (ix, iy), (ix+size, iy), (ix, iy+isize)
               and returns SX*SX + SY*SY.
               The values in the last "size" rows and columns are not
               processed.
               The wrapper was created for testing and development purposes.
               """,
               return_type=Type.DOUBLE,
               return_doc="Maximum Terrain Steepness Computation.",
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Topography Pager"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Annular Size")
               ])
    ],
    'Miscellaneous': [

    ],
    'Obsolete': [

        Method('DirectGrid_PGU', module='geogxx', version='7.2.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Direct-gridding method.",
               notes="""
               Grid cells take on the averaged values inside their bounds.
               
               Weighting can be controlled using the power and slope properties;
               
               weighting = 1 / (distance^wtpower + 1/slope) where distance is in
               units of grid cells (X dimenstion). Default is 0.0,
               
               MADE OBSOLETE BECAUSE: Inverse-distance-weighting makes no sense with
               this method, especially as no search radius is specified.
               
               REPLACED BY: DirectGridding_PGU.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="input grid"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X origin of grid"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y origin of grid"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X cell size"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y cell size"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="rotation angle (degrees CCW)."),
                   Parameter('p7', type="VV",
                             doc="X locations of values"),
                   Parameter('p8', type="VV",
                             doc="Y locations of values"),
                   Parameter('p9', type="VV",
                             doc="Z values to grid"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="power weighting for averaging (set to 0 for straight average)"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="slope weighting for averaging (set to 0 for pure power-law weighting)")
               ]),

        Method('FFT2Filter_PGU', module='geogxx', version='5.0.0',
               availability=Availability.UNKNOWN, is_obsolete=True, 
               doc="Carry out a fourier transform filter on a pager object",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="pager obj"),
                   Parameter('p2', type=Type.STRING,
                             doc="sConFil - :class:`FFT` filter control file"),
                   Parameter('p3', type="TR",
                             doc=":class:`TR` obj"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="rDx - X increment"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="rDy - Y increment"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="rRot- Rotation degree")
               ]),

        Method('FFT2Trans_PGU', module='geogxx', version='5.0.0',
               availability=Availability.UNKNOWN, is_obsolete=True, 
               doc="Carry out a fourier transform on a pager object",
               notes="Obsolete",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="pager obj"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="option: 0 - forward transform, 1 - invers transform")
               ])
    ]
}

