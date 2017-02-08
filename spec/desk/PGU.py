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
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="pager obj"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="option: 0 - forward transform, 1 - invers transform")
               ])
    ]
}

