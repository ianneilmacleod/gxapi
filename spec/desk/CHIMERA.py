from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('CHIMERA',
                 doc=":class:`CHIMERA` GX function library.")


gx_defines = [
    Define('CHIMERA_MAX_CHAN',
           is_constant=True,
           is_single_constant=True,
           doc="Maximum channels in Chimera database",
           constants=[
               Constant('CHIMERA_MAX_CHAN', value='128', type=Type.INT32_T)                        
           ]),

    Define('CHIMERA_PLOT',
           doc="Chimera plot type",
           constants=[
               Constant('CHIMERA_PLOT_ROSE', value='0', type=Type.INT32_T)                        ,
               Constant('CHIMERA_PLOT_PIE', value='1', type=Type.INT32_T)                        ,
               Constant('CHIMERA_PLOT_BAR', value='2', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('BarPlot_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, 
               doc="Plot a Bar plot of up to 8 channels.",
               notes="""
               The number of channels is taken from the Data handles :class:`VV`.
               Plots a bar plot with the center of the "X" axis at the symbol location.
               See the note on offset symbols in :func:`RosePlot_CHIMERA`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View object to plot to"),
                   Parameter('p2', type=Type.STRING,
                             doc="Data group name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Offset group name"),
                   Parameter('p4', type="VV",
                             doc="X locations"),
                   Parameter('p5', type="VV",
                             doc="Y locations"),
                   Parameter('p6', type="VV",
                             doc="Data handles, stored as INT values"),
                   Parameter('p7', type="VV",
                             doc="Colours"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Colour for edges"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Offset symbols (0: No, 1: Yes)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Offset symbol size"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Single bar width in data units.")
               ]),

        Method('CategorizeByValue_CHIMERA', module='geochimera', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Transform values to the index of input data ranges.",
               notes="""
               A list of minima (e.g.  M1, M2, M3, M4, M5) is input.
               A list of values V is input and transformed to outputs N in the following manner:
               
               if(V) >= M5) N = 5
               else if(V) >= M4) N = 4
               ...
               ...
               else if(V) >= M1) N = 1
               else N = 0
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input range minima"),
                   Parameter('p2', type="VV",
                             doc="Input data :class:`VV`.      (REAL)"),
                   Parameter('p3', type="VV",
                             doc="Output (altered) :class:`VV`.(REAL)")
               ]),

        Method('CategorizeByValueDetLimit_CHIMERA', module='geochimera', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Transform values to the index of input data ranges, with detection limit.",
               notes="""
               Same as :func:`CategorizeByValue_CHIMERA`, but if the
               input value is less than the detection limit,
               the output value is set to zero.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input range minima"),
                   Parameter('p2', type="VV",
                             doc="Input data :class:`VV`.      (REAL)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Detection limit (can be :def_val:`rDUMMY`)"),
                   Parameter('p4', type="VV",
                             doc="Output (altered) :class:`VV`.(REAL)")
               ]),

        Method('ClipToDetectLimit_CHIMERA', module='geochimera', version='5.0.8',
               availability=Availability.EXTENSION, 
               doc="Apply detection limit clipping of data.",
               notes="""
               Flow:
               
               1. If auto-converting negatives, then all negative values
                   are replaced by -0.5*value, and detection limit is ignored.
               
               2. If not auto-converting negatives, and the detection limit is not
                  :def_val:`rDUMMY`, then values less than the detection limit are converted to
                  one-half the detection limit.
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

        Method('DrawCircleOffsetMarkers_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, 
               doc="Plots location marker and joining line for circle offset symbols",
               notes="Draws black filled circle (symbols.gfn #7) and a joining line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="VV",
                             doc="Original (marker) X location"),
                   Parameter('p3', type="VV",
                             doc="Original (marker) Y location"),
                   Parameter('p4', type="VV",
                             doc="Offset (new) X location"),
                   Parameter('p5', type="VV",
                             doc="Offset (new) Y location"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Marker symbol radius")
               ]),

        Method('DrawRectangleOffsetMarkers_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, 
               doc="Plots location marker and joining line for rectangle offset symbols",
               notes="Draws black filled circle (symbols.gfn #7) and a joining line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="VV",
                             doc="Original (marker) X location"),
                   Parameter('p3', type="VV",
                             doc="Original (marker) Y location"),
                   Parameter('p4', type="VV",
                             doc="Offset (new) X location"),
                   Parameter('p5', type="VV",
                             doc="Offset (new) Y location"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Offset symbol width"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Offset symbol height"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Marker symbol radius")
               ]),

        Method('DuplicateChem_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, 
               doc="Plot an ASSAY Duplicate result in a graph window.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="VV",
                             doc="Duplicate data"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="log-transform: 0 - linear, 1 - log"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Detect Limit"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="number of old samples in the :class:`VV`"),
                   Parameter('p6', type="VV",
                             doc="tolerances (1-5 values)"),
                   Parameter('p7', type=Type.STRING,
                             doc="Title"),
                   Parameter('p8', type=Type.STRING,
                             doc="Unit"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="X location (bottom left corner of graph)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="graph width"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="graph height")
               ]),

        Method('DuplicateChemView_CHIMERA', module='geochimera', version='8.3.0',
               availability=Availability.EXTENSION, 
               doc="Plot an ASSAY Duplicate result in a new view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc="Map"),
                   Parameter('p2', type=Type.STRING,
                             doc="New view name"),
                   Parameter('p3', type=Type.STRING,
                             doc="New group name"),
                   Parameter('p4', type="IPJ"),
                   Parameter('p5', type="VV",
                             doc="Duplicate data"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="log-transform: 0 - linear, 1 - log"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Detect Limit"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="number of old samples in the :class:`VV`"),
                   Parameter('p9', type="VV",
                             doc="tolerances (1-5 values)"),
                   Parameter('p10', type=Type.STRING,
                             doc="Title"),
                   Parameter('p11', type=Type.STRING,
                             doc="Unit"),
                   Parameter('p12', type="VV",
                             doc=":class:`VV` X"),
                   Parameter('p13', type="VV",
                             doc=":class:`VV` Line"),
                   Parameter('p14', type="VV",
                             doc=":class:`VV` Fid"),
                   Parameter('p15', type="DB",
                             doc="Database"),
                   Parameter('p16', type=Type.DOUBLE, is_ref=True,
                             doc="Returned MinY"),
                   Parameter('p17', type=Type.DOUBLE, is_ref=True,
                             doc="Returned MaxY")
               ]),

        Method('GetExpressionDataVV_CHIMERA', module='geochimera', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Get data from a line using a channel expression.",
               notes="""
               Input a channel expression. Units for individual channels
               are stored in the input INI. Returns a :class:`VV` for the given line
               with the calculated expression values.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line to read"),
                   Parameter('p3', type=Type.STRING,
                             doc='geochem stage (just "raw data stage" for now).'),
                   Parameter('p4', type=Type.STRING,
                             doc="channel expression"),
                   Parameter('p5', type=Type.STRING,
                             doc='INI file name with required units (e.g. PARAMETER.CU="ppm") (optional)'),
                   Parameter('p6', type="VV",
                             doc="Returned data")
               ]),

        Method('GetLithogeochemData_CHIMERA', module='geochimera', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Get all rows of non-dummy data in a database.",
               notes="""
               This function is a quick way to get all rows
               of data, guaranteeing no dummy items.
               Book-keeping VVs returned let you easily
               write back results to new channels in the
               correct locations.
               Set the "Dummy Row" :class:`VV` to 1 if you wish to
               remove any row where a value for the corresponding
               channel is a dummy.
               
               Transforms to apply:
               
               -1 - Channel default (will be either raw or log)
               0 - Raw Transform
               1 - Log transform: base e with log min = CHIMERA_LOG_MIN
               2 - Lambda transform
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="[i] database handle"),
                   Parameter('p2', type="LST",
                             doc="[i] channels of data to get"),
                   Parameter('p3', type="DB_SYMB",
                             doc="[i] mask channel (can be :def_val:`NULLSYMB`)"),
                   Parameter('p4', type="VV",
                             doc="[i] transforms to apply"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="[i] remove dummy rows?"),
                   Parameter('p6', type="VV",
                             doc='[i] dummy row if this channel value is dummy (0:No, 1:Yes)? Effective only if "remove dummy rows" value is TRUE'),
                   Parameter('p7', type=Type.INT32_T,
                             doc="[i] warn if rows removed because of dummy data items?"),
                   Parameter('p8', type="VV",
                             doc="[o] (INT) returned data - one :class:`VV` handle per channel"),
                   Parameter('p9', type="VV",
                             doc="[o] line symbols selected"),
                   Parameter('p10', type="VV",
                             doc="[o] number of original data items in each line"),
                   Parameter('p11', type="VV",
                             doc="[o] number of non-dummy rows"),
                   Parameter('p12', type="VV",
                             doc="[o] indices into original data"),
                   Parameter('p13', type="VV",
                             doc="[o] Fid Starts (REAL)"),
                   Parameter('p14', type="VV",
                             doc="[o] Fid Increments (REAL)")
               ]),

        Method('GetTransform_CHIMERA', module='geochimera', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Get channel transform options and lambda values.",
               notes="""
               If the lambda transform is requested, the channel
               must have the lambda value defined.
               
               Input Transform options
               
               -1 - Channel default (will be either raw or log)
               0 - Raw Transform
               1 - Log transform: base e with log min = CHIMERA_LOG_MIN
               2 - Lambda transform
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc=":class:`DB` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Channel name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Transform option: -1, 0, 1 or 2"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="returned transform used"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="returned lambda value for option==2")
               ]),

        Method('iIsAcquireChan_CHIMERA', module='geochimera', version='7.2.0',
               availability=Availability.EXTENSION, 
               doc='Is this channel in acQuire format (e.g. "Ag_ppm_4AWR")',
               notes="""
               Expressions can take acQuire-type named channels
               if the exact element/oxide is not found. This function
               extracts the channel name, and units from an acQuire-formatted
               channel name.
               """,
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="string to test"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="returned channel name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="buffer size for channel name"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="returned units"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DEFAULT_SHORT',
                             doc="buffer size for units"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="units factor (e.g. ppm = 1.e-6)"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc=":def:`GEO_BOOL` is this an oxide?")
               ]),

        Method('iIsElement_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, 
               doc="Tests a string to see if it is an element symbol",
               notes="""
               Suggested use - testing to see if a channel name is an
               element so that the "ASSAY" class can be set.
               """,
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="string to test"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`STR_CASE`")
               ]),

        Method('LaunchHistogram_CHIMERA', module='geochimera', version='5.0.6',
               availability=Availability.EXTENSION, 
               doc="Launch histogram tool on a database.",
               notes="""
               The database should be a currently open database.
               This function supercedes :func:`LaunchHistogram_EDB`, (which now
               just gets the name of the :class:`EDB` and calls this function).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database name"),
                   Parameter('p2', type=Type.STRING,
                             doc="First chan name")
               ]),

        Method('LaunchProbability_CHIMERA', module='geochimera', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Launch probability tool on a database.",
               notes="The database should be a currently open database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database name"),
                   Parameter('p2', type=Type.STRING,
                             doc="First chan name")
               ]),

        Method('LaunchScatter_CHIMERA', module='geochimera', version='5.0.6',
               availability=Availability.EXTENSION, 
               doc="Launch scatter tool on a database.",
               notes="""
               The scatter tool uses the following INI parameters
               
               SCATTER.STM       name of the scatter template,"none" for none
               SCATTER.STM_NAME  name of last template section, "" for none.
               SCATTER.X         name of channel to display in X
               SCATTER.Y         name of channel to display in Y
               SCATTER.MASK      name of channel to use for mask
               
               The database should be a currently open database.
               This function supercedes :func:`LaunchScatter_EDB`, (which now
               just gets the name of the :class:`EDB` and calls this function).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database name")
               ]),

        Method('LaunchTriplot_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, 
               doc="Launch Triplot tool on a database.",
               notes="""
               The Triplot tool uses the following INI parameters
               
                        TRIPLOT.TTM       name of the triplot template,"none" for none
                        TRIPLOT.TTM_NAME  name of last template section, "" for none.
                        TRIPLOT.X         name of channel to display in X
                        TRIPLOT.Y         name of channel to display in Y
                        TRIPLOT.Z         name of channel to display in Z
                        TRIPLOT.MASK      name of channel to use for mask
               
               The database should be a currently open database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database name")
               ]),

        Method('MaskChanLST_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, 
               doc="Load a :class:`LST` with mask channels.",
               notes="""
               Loads a :class:`LST` with all channels with CLASS "MASK", as well
               as all channels containing the string "MASK", as long
               as the CLASS for these channels is not set to something
               other than "" or "MASK".
               
               This function has been duplicated by :func:`MaskChanLST_DB`, which
               is safe to use in applications which do not have :class:`CHIMERA` loaded.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Database Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object to populate")
               ]),

        Method('OrderedChannelLST_CHIMERA', module='geochimera', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Fill a list with the channels in the preferred order.",
               notes="""
               Loads a :class:`LST` with all channels in the preferred order:
               
               First:  Sample, E, N, assay channels,
               Middle: Data from survey (other channels),
               Last:   Duplicate, Standard, Chemmask (and other masks), weight, lab, batch
               
               If the input :class:`LST` object has values, it is used as the channel :class:`LST`,
               otherwise, get all the database channels. (This allows you to pass in
               the currently displayed channels and only reload those).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="hDB - Database Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object to populate [recommended 2*:def_val:`STR_DB_SYMBOL`]")
               ]),

        Method('PiePlot_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, 
               doc="Plot a Pie plot of up to 8 channels.",
               notes="""
               The number of channels is taken from the Data handles :class:`VV`.
               The values in each data :class:`VV` are summed and the pie arc is
               is given by the percent contribution of each consituent.
               See the note on offset symbols in :func:`RosePlot_CHIMERA`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View object to plot to"),
                   Parameter('p2', type=Type.STRING,
                             doc="Data group name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Offset group name"),
                   Parameter('p4', type="VV",
                             doc="X locations"),
                   Parameter('p5', type="VV",
                             doc="Y locations"),
                   Parameter('p6', type="VV",
                             doc="Data handles, stored as INT values"),
                   Parameter('p7', type="VV",
                             doc="Colours"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Colour for edges"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Offset symbols (0: No, 1: Yes)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Offset symbol size"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Pie plot radius in data units.")
               ]),

        Method('PiePlot2_CHIMERA', module='geochimera', version='5.1.5',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`PiePlot_CHIMERA`, with a starting angle.",
               notes="""
               The starting angle is the location of the edge of the first pie
               slice, counted in degrees counter-clockwise from horizontal
               (3 o'clock). Zero degrees gives the same plot as :func:`PiePlot_CHIMERA`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View object to plot to"),
                   Parameter('p2', type=Type.STRING,
                             doc="Data group name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Offset group name"),
                   Parameter('p4', type="VV",
                             doc="X locations"),
                   Parameter('p5', type="VV",
                             doc="Y locations"),
                   Parameter('p6', type="VV",
                             doc="Data handles, stored as INT values"),
                   Parameter('p7', type="VV",
                             doc="Colours"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Colour for edges"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Offset symbols (0: No, 1: Yes)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Offset symbol size"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Pie plot radius in data units."),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="Starting angle in degrees CCW from horizontal (:def_val:`rDUMMY` gives 0.0)")
               ]),

        Method('PlotStringClassifiedSymbolsLegendFromClassFile_CHIMERA', module='geochimera', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="Plot legend for the string classified symbols",
               notes="Plot in a legend the classes in the class file found in the input class indices.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="Map view object"),
                   Parameter('p2', type=Type.STRING,
                             doc="title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="left side X location"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="bottom Y bound"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="top Y bound"),
                   Parameter('p6', type=Type.STRING,
                             doc="Class file name (:class:`TPAT`)"),
                   Parameter('p7', type="VV",
                             doc="Class indices  (INT :class:`VV`)")
               ]),

        Method('rAtomicWeight_CHIMERA', module='geochimera', version='6.4.2',
               availability=Availability.EXTENSION, 
               doc="Return the atomic weight of a particular element.",
               notes="""
               If the input string is not an element symbol (elements in the range
               1-92, "H" to "U"), then returns a dummy (:def_val:`GS_R8DM`).
               """,
               return_type=Type.DOUBLE,
               return_doc="The atomic weight of the given element.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="element name (case insensitive)")
               ]),

        Method('RosePlot_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, 
               doc="Plot a Rose plot of up to 8 channels.",
               notes="""
               The number of channels is taken from the Data handles :class:`VV`.
               The values in each data :class:`VV` give the radius, in view units,
               of the sector arc to plots. Values <=0 or dummies are not
               plotted.
               
               Offset symbols: When selected, the symbols plot without
               overlap, away from the original locations. The original
               location is marked with a small symbol and a line joins the
               original position and the relocated symbol.
               Care should be taken when choosing the symbol size, because
               if the point density is too high, all the points will get
               pushed to the outside edge and your plot will look like a
               hedgehog (it also takes a lot longer!).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View object to plot to"),
                   Parameter('p2', type=Type.STRING,
                             doc="Data group name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Offset group name"),
                   Parameter('p4', type="VV",
                             doc="X locations"),
                   Parameter('p5', type="VV",
                             doc="Y locations"),
                   Parameter('p6', type="VV",
                             doc="Data handles, stored as INT values"),
                   Parameter('p7', type="VV",
                             doc="Colours"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Colour for edges"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Offset symbols (0: No, 1: Yes)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Offset symbol size")
               ]),

        Method('RosePlot2_CHIMERA', module='geochimera', version='5.1.5',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`RosePlot_CHIMERA`, with a starting angle.",
               notes="""
               The starting angle is the location of the edge of the first pie
               slice, counted in degrees counter-clockwise from horizontal
               (3 o'clock). Zero degrees gives the same plot as :func:`RosePlot_CHIMERA`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View object to plot to"),
                   Parameter('p2', type=Type.STRING,
                             doc="Data group name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Offset group name"),
                   Parameter('p4', type="VV",
                             doc="X locations"),
                   Parameter('p5', type="VV",
                             doc="Y locations"),
                   Parameter('p6', type="VV",
                             doc="Data handles, stored as INT values"),
                   Parameter('p7', type="VV",
                             doc="Colours"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Colour for edges"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Offset symbols (0: No, 1: Yes)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Offset symbol size"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Starting angle in degrees CCW from horizontal (:def_val:`rDUMMY` gives 0.0)")
               ]),

        Method('Scatter2_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, 
               doc="Plot the scatter plot on a map using symbol number, size and color VVs.",
               notes="""
               The view scaling is not altered with any projection. The base view
               is best as the input.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of box)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="box width"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="box height"),
                   Parameter('p7', type="VV",
                             doc="Horizontal channel"),
                   Parameter('p8', type="VV",
                             doc="Vertical channel"),
                   Parameter('p9', type=Type.STRING,
                             doc='decorated font name, "" for default symbol font (normally symbols.gfn)'),
                   Parameter('p10', type="VV",
                             doc="Symbol numbers"),
                   Parameter('p11', type="VV",
                             doc="Symbol sizes"),
                   Parameter('p12', type="VV",
                             doc="Colours  if symbol number or colour == 0, do not plot"),
                   Parameter('p13', type=Type.INT32_T,
                             doc="Annotation style 0 - outside, 1 - inside"),
                   Parameter('p14', type=Type.STRING,
                             doc="Horizontal channel name"),
                   Parameter('p15', type=Type.STRING,
                             doc="Vertical channel name"),
                   Parameter('p16', type=Type.STRING,
                             doc="Horizontal channel units"),
                   Parameter('p17', type=Type.STRING,
                             doc="Vertical channel units"),
                   Parameter('p18', type=Type.DOUBLE,
                             doc="Min. Horizontal value, :def_val:`rDUMMY` for default"),
                   Parameter('p19', type=Type.DOUBLE,
                             doc="Max. Horizontal value"),
                   Parameter('p20', type=Type.DOUBLE,
                             doc="Min. Vertical value"),
                   Parameter('p21', type=Type.DOUBLE,
                             doc="Max. Vertical value"),
                   Parameter('p22', type=Type.DOUBLE,
                             doc="Min. Horizontal range value"),
                   Parameter('p23', type=Type.DOUBLE,
                             doc="Max. Horizontal range value"),
                   Parameter('p24', type=Type.DOUBLE,
                             doc="Min. Vertical range value"),
                   Parameter('p25', type=Type.DOUBLE,
                             doc="Max. Vertical range value"),
                   Parameter('p26', type=Type.INT32_T,
                             doc="Use Min Horz. Range selection?"),
                   Parameter('p27', type=Type.INT32_T,
                             doc="Use Max Horz. Range selection?"),
                   Parameter('p28', type=Type.INT32_T,
                             doc="Use Min Vert. Range selection?"),
                   Parameter('p29', type=Type.INT32_T,
                             doc="Use Max Vert. Range selection?"),
                   Parameter('p30', type=Type.INT32_T,
                             doc="horizontal axis scaling: 0 - linear, 1 - log"),
                   Parameter('p31', type=Type.INT32_T,
                             doc="vertical axis scaling")
               ]),

        Method('FixedSymbolScatterPlot_CHIMERA', module='geochimera', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="""
               Plot a scatter plot using a single fixed symbol.
               Optional data masking with masking colour.
               Optioinal database linking.
               """,
               notes="Plot a scatter plot using a single fixed symbol.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of box)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="box width"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="box height"),
                   Parameter('p7', type="VV",
                             doc="Horizontal channel data"),
                   Parameter('p8', type="VV",
                             doc="Vertical channel data"),
                   Parameter('p9', type="VV",
                             doc="Mask channel data (can be NULL)"),
                   Parameter('p10', type=Type.INT32_T,
                             doc='Mask colour; overrides symbol colour where mask data is not dummy. Set to :func:`iColor_MVIEW`("") to not plot.'),
                   Parameter('p11', type=Type.STRING,
                             doc='decorated font name, "" for default symbol font (normally symbols.gfn)'),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Symbol number (>=0)"),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Symbol size ( >=0)"),
                   Parameter('p14', type=Type.DOUBLE,
                             doc="Symbol angle (-360 to 360)"),
                   Parameter('p15', type=Type.INT32_T,
                             doc="Symbol colour"),
                   Parameter('p16', type=Type.INT32_T,
                             doc="Symbol fill colour"),
                   Parameter('p17', type="DB",
                             doc="Database (source of data)"),
                   Parameter('p18', type="VV",
                             doc="Line handles for data"),
                   Parameter('p19', type="VV",
                             doc="Fid values for data"),
                   Parameter('p20', type=Type.INT32_T,
                             doc="Annotation style 0 - outside, 1 - inside"),
                   Parameter('p21', type=Type.STRING,
                             doc="Horizontal channel name"),
                   Parameter('p22', type=Type.STRING,
                             doc="Vertical channel name"),
                   Parameter('p23', type=Type.STRING,
                             doc="Horizontal channel units"),
                   Parameter('p24', type=Type.STRING,
                             doc="Vertical channel units"),
                   Parameter('p25', type=Type.DOUBLE,
                             doc="Min. Horizontal value, :def_val:`rDUMMY` for default"),
                   Parameter('p26', type=Type.DOUBLE,
                             doc="Max. Horizontal value"),
                   Parameter('p27', type=Type.DOUBLE,
                             doc="Min. Vertical value"),
                   Parameter('p28', type=Type.DOUBLE,
                             doc="Max. Vertical value"),
                   Parameter('p29', type=Type.INT32_T,
                             doc="horizontal axis scaling: 0 - linear, 1 - log"),
                   Parameter('p30', type=Type.INT32_T,
                             doc="vertical axis scaling"),
                   Parameter('p31', type=Type.STRING,
                             doc='plot overlay ("" for none)')
               ]),

        Method('ZoneColouredScatterPlot_CHIMERA', module='geochimera', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="""
               Plot a scatter plot using colours based on a zone file.
               Optional data masking with masking colour.
               Optioinal database linking.
               """,
               notes="Plot a scatter plot using colours based on a zone file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of box)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="box width"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="box height"),
                   Parameter('p7', type="VV",
                             doc="Horizontal channel data"),
                   Parameter('p8', type="VV",
                             doc="Vertical channel data"),
                   Parameter('p9', type="VV",
                             doc="Mask channel data (can be NULL)"),
                   Parameter('p10', type=Type.INT32_T,
                             doc='Mask colour; overrides symbol colour where mask data is not dummy. Set to :func:`iColor_MVIEW`("") to not plot.'),
                   Parameter('p11', type="VV",
                             doc="Zone channel data"),
                   Parameter('p12', type=Type.STRING,
                             doc="Zone file name"),
                   Parameter('p13', type=Type.STRING,
                             doc='decorated font name, "" for default symbol font (normally symbols.gfn)'),
                   Parameter('p14', type=Type.INT32_T,
                             doc="Symbol number (>=0)"),
                   Parameter('p15', type=Type.DOUBLE,
                             doc="Symbol size ( >=0)"),
                   Parameter('p16', type=Type.DOUBLE,
                             doc="Symbol angle (-360 to 360)"),
                   Parameter('p17', type=Type.INT32_T,
                             doc="Symbol colour"),
                   Parameter('p18', type=Type.INT32_T,
                             doc="Symbol fill colour"),
                   Parameter('p19', type=Type.INT32_T,
                             doc="Fix symbol edge colour?"),
                   Parameter('p20', type="DB",
                             doc="Database (source of data)"),
                   Parameter('p21', type="VV",
                             doc="Line handles for data"),
                   Parameter('p22', type="VV",
                             doc="Fid values for data"),
                   Parameter('p23', type=Type.INT32_T,
                             doc="Annotation style 0 - outside, 1 - inside"),
                   Parameter('p24', type=Type.STRING,
                             doc="Horizontal channel name"),
                   Parameter('p25', type=Type.STRING,
                             doc="Vertical channel name"),
                   Parameter('p26', type=Type.STRING,
                             doc="Horizontal channel units"),
                   Parameter('p27', type=Type.STRING,
                             doc="Vertical channel units"),
                   Parameter('p28', type=Type.DOUBLE,
                             doc="Min. Horizontal value, :def_val:`rDUMMY` for default"),
                   Parameter('p29', type=Type.DOUBLE,
                             doc="Max. Horizontal value"),
                   Parameter('p30', type=Type.DOUBLE,
                             doc="Min. Vertical value"),
                   Parameter('p31', type=Type.DOUBLE,
                             doc="Max. Vertical value"),
                   Parameter('p32', type=Type.INT32_T,
                             doc="horizontal axis scaling: 0 - linear, 1 - log"),
                   Parameter('p33', type=Type.INT32_T,
                             doc="vertical axis scaling"),
                   Parameter('p34', type=Type.STRING,
                             doc='plot overlay ("" for none)')
               ]),

        Method('StringClassifiedScatterPlot_CHIMERA', module='geochimera', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="""
               Plot a scatter plot using symbols based on a symbol class file.
               Optional data masking with masking colour.
               Optioinal database linking.
               """,
               notes="Plot a scatter plot using symbols based on a symbol class file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of box)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="box width"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="box height"),
                   Parameter('p7', type="VV",
                             doc="Horizontal channel data"),
                   Parameter('p8', type="VV",
                             doc="Vertical channel data"),
                   Parameter('p9', type="VV",
                             doc="Mask channel data"),
                   Parameter('p10', type=Type.INT32_T,
                             doc='Mask colour; overrides symbol colour. Set to :func:`iColor_MVIEW`("") to not plot.'),
                   Parameter('p11', type="VV",
                             doc="Class channel data"),
                   Parameter('p12', type=Type.STRING,
                             doc="Class file (:class:`TPAT`) name."),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Symbol size override. Set to 0.0 to use class file symbol sizes."),
                   Parameter('p14', type="DB",
                             doc="Database (source of data)"),
                   Parameter('p15', type="VV",
                             doc="Line handles for data"),
                   Parameter('p16', type="VV",
                             doc="Fid values for data"),
                   Parameter('p17', type=Type.INT32_T,
                             doc="Annotation style 0 - outside, 1 - inside"),
                   Parameter('p18', type=Type.STRING,
                             doc="Horizontal channel name"),
                   Parameter('p19', type=Type.STRING,
                             doc="Vertical channel name"),
                   Parameter('p20', type=Type.STRING,
                             doc="Horizontal channel units"),
                   Parameter('p21', type=Type.STRING,
                             doc="Vertical channel units"),
                   Parameter('p22', type=Type.DOUBLE,
                             doc="Min. Horizontal value, :def_val:`rDUMMY` for default"),
                   Parameter('p23', type=Type.DOUBLE,
                             doc="Max. Horizontal value"),
                   Parameter('p24', type=Type.DOUBLE,
                             doc="Min. Vertical value"),
                   Parameter('p25', type=Type.DOUBLE,
                             doc="Max. Vertical value"),
                   Parameter('p26', type=Type.INT32_T,
                             doc="horizontal axis scaling: 0 - linear, 1 - log"),
                   Parameter('p27', type=Type.INT32_T,
                             doc="vertical axis scaling"),
                   Parameter('p28', type=Type.STRING,
                             doc='plot overlay ("" for none)')
               ]),

        Method('SetLithogeochemData_CHIMERA', module='geochimera', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Set data back into a database.",
               notes="""
               This function would normally be called after
               AAGetLithogeochemData_CHIMERA to write processed values
               back into a database, in the correct lines,
               and in the correct fiducial locations wrt the
               other data. The book-keeping VVs would all be
               set up in AAGetLithogeochemData_CHIMERA.
               
               Values NOT in the data (missing indices) will
               be initialized to dummy if the channel is new,
               or if the value in the last :class:`VV` below is set to 1.
               
               New channel types will be set using the data :class:`VV` type.
               Any meta data (CLASS, display formats) should be set separately.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="[i] database handle"),
                   Parameter('p2', type="LST",
                             doc="[i] channels of data to set"),
                   Parameter('p3', type="VV",
                             doc="[i] (INT) input data - one :class:`VV` handle per channel"),
                   Parameter('p4', type="VV",
                             doc="[i] line symbols selected"),
                   Parameter('p5', type="VV",
                             doc="[i] number of original data items in each line"),
                   Parameter('p6', type="VV",
                             doc="[i] number of non-dummy rows"),
                   Parameter('p7', type="VV",
                             doc="[i] indices into original data"),
                   Parameter('p8', type="VV",
                             doc="[i] Fid Starts (REAL)"),
                   Parameter('p9', type="VV",
                             doc="[i] Fid Increments (REAL)"),
                   Parameter('p10', type="VV",
                             doc="[i] init channel values to dummies first (0:No, 1:Yes)?")
               ]),

        Method('StackedBarPlot_CHIMERA', module='geochimera', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Plot a Bar plot of up to 8 channels, bars stacked on each other",
               notes="""
               The number of channels is taken from the Data handles :class:`VV`.
               Plots a bar plot with the center of the "X" axis at the symbol location.
               See the note on offset symbols in :func:`RosePlot_CHIMERA`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View object to plot to"),
                   Parameter('p2', type=Type.STRING,
                             doc="Data group name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Offset group name"),
                   Parameter('p4', type="VV",
                             doc="X locations"),
                   Parameter('p5', type="VV",
                             doc="Y locations"),
                   Parameter('p6', type="VV",
                             doc="Data handles, stored as INT values"),
                   Parameter('p7', type="VV",
                             doc="Colours"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Colour for edges"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Offset symbols (0: No, 1: Yes)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Offset symbol size"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Single bar width in data units.")
               ]),

        Method('Standard_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, 
               doc="Plot ASSAY Standard result in a graph window.",
               notes="""
               If the tolerance is :def_val:`rDUMMY`, then the minimum and maximum
               values are used, and must be specified.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type="VV",
                             doc="standard data"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="number of old samples in the :class:`VV`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="tolerance as a function of std dev"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="minimum acceptable value"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="maximum acceptable value"),
                   Parameter('p7', type=Type.STRING,
                             doc="Title"),
                   Parameter('p8', type=Type.STRING,
                             doc="Unit"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="X location (bottom left corner of graph)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="graph width"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="graph height")
               ]),

        Method('StandardView_CHIMERA', module='geochimera', version='8.3.0',
               availability=Availability.EXTENSION, 
               doc="Plot ASSAY Standard result in a graph window.",
               notes="Same as :func:`Standard_CHIMERA` but plot in a new view.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc="Map"),
                   Parameter('p2', type=Type.STRING,
                             doc="New view name"),
                   Parameter('p3', type=Type.STRING,
                             doc="New group name"),
                   Parameter('p4', type="IPJ"),
                   Parameter('p5', type="VV",
                             doc="standard data (:class:`VV` Y)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="number of old samples in the :class:`VV`"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="tolerance as a function of std dev"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="minimum acceptable value"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="maximum acceptable value"),
                   Parameter('p10', type=Type.STRING,
                             doc="Title"),
                   Parameter('p11', type=Type.STRING,
                             doc="Unit"),
                   Parameter('p12', type=Type.DOUBLE,
                             doc="Size X"),
                   Parameter('p13', type="VV",
                             doc=":class:`VV` X"),
                   Parameter('p14', type="VV",
                             doc=":class:`VV` Line"),
                   Parameter('p15', type="VV",
                             doc=":class:`VV` Fid"),
                   Parameter('p16', type="DB",
                             doc="Database"),
                   Parameter('p17', type=Type.DOUBLE, is_ref=True,
                             doc="Returned MinY"),
                   Parameter('p18', type=Type.DOUBLE, is_ref=True,
                             doc="Returned MaxY")
               ]),

        Method('TriPlot2_CHIMERA', module='geochimera', version='5.1.6',
               availability=Availability.EXTENSION, 
               doc="Plot the TriPlot on a map using symbol number, size and color VVs.",
               notes="""
               The mask channel :class:`VV` is used for plotting precedence; those points with
               mask = dummy are plotted first, then overwritten with the non-masked
               values, so you don't get "good" points being covered up by masked values.
               The view scaling is not altered with any projection. The base view
               is best as the input.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of box)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="box width"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="box height"),
                   Parameter('p7', type="VV",
                             doc="X channel"),
                   Parameter('p8', type="VV",
                             doc="Y channel"),
                   Parameter('p9', type="VV",
                             doc="Z channel"),
                   Parameter('p10', type="VV",
                             doc="Mask channel"),
                   Parameter('p11', type=Type.STRING,
                             doc='decorated font name, "" for default symbol font (normally symbols.gfn)'),
                   Parameter('p12', type="VV",
                             doc="Symbol numbers"),
                   Parameter('p13', type="VV",
                             doc="Symbol sizes"),
                   Parameter('p14', type="VV",
                             doc="Colours  if symbol number or colour == 0, do not plot"),
                   Parameter('p15', type=Type.STRING,
                             doc="X channel name"),
                   Parameter('p16', type=Type.STRING,
                             doc="Y channel name"),
                   Parameter('p17', type=Type.STRING,
                             doc="Z channel name"),
                   Parameter('p18', type=Type.DOUBLE,
                             doc="Min. X range value"),
                   Parameter('p19', type=Type.DOUBLE,
                             doc="Max. X range value"),
                   Parameter('p20', type=Type.DOUBLE,
                             doc="Min. Y range value"),
                   Parameter('p21', type=Type.DOUBLE,
                             doc="Max. Y range value"),
                   Parameter('p22', type=Type.DOUBLE,
                             doc="Min. Z range value"),
                   Parameter('p23', type=Type.DOUBLE,
                             doc="Max. Z range value"),
                   Parameter('p24', type=Type.INT32_T,
                             doc="Use Min X Range selection?"),
                   Parameter('p25', type=Type.INT32_T,
                             doc="Use Max X Range selection?"),
                   Parameter('p26', type=Type.INT32_T,
                             doc="Use Min Y Range selection?"),
                   Parameter('p27', type=Type.INT32_T,
                             doc="Use Max Y Range selection?"),
                   Parameter('p28', type=Type.INT32_T,
                             doc="Use Min Z Range selection?"),
                   Parameter('p29', type=Type.INT32_T,
                             doc="Use Max Z Range selection?"),
                   Parameter('p30', type=Type.INT32_T,
                             doc="Plot Grid lines? (0: Just outside edge tics, 1: Grid lines)."),
                   Parameter('p31', type=Type.DOUBLE,
                             doc="Tic Increment (in percent)"),
                   Parameter('p32', type=Type.DOUBLE,
                             doc="Grid increment (in percent)")
               ]),

        Method('FixedSymbolTriPlot_CHIMERA', module='geochimera', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="""
               Plot a tri-plot using a single fixed symbol.
               Optional data masking with masking colour.
               Optioinal database linking.
               """,
               notes="Plot a tri plot using a single fixed symbol.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of box)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Triangle side length"),
                   Parameter('p6', type="VV",
                             doc="X channel data"),
                   Parameter('p7', type="VV",
                             doc="Y channel data"),
                   Parameter('p8', type="VV",
                             doc="Z channel data"),
                   Parameter('p9', type="VV",
                             doc="Mask channel data"),
                   Parameter('p10', type=Type.INT32_T,
                             doc='Mask colour; overrides symbol colour where mask data is not dummy. Set to :func:`iColor_MVIEW`("") to not plot.'),
                   Parameter('p11', type=Type.STRING,
                             doc='decorated font name, "" for default symbol font (normally symbols.gfn)'),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Symbol number (>=0)"),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Symbol size ( >=0)"),
                   Parameter('p14', type=Type.DOUBLE,
                             doc="Symbol angle (-360 to 360)"),
                   Parameter('p15', type=Type.INT32_T,
                             doc="Symbol colour"),
                   Parameter('p16', type=Type.INT32_T,
                             doc="Symbol fill colour"),
                   Parameter('p17', type="DB",
                             doc="Database (source of data)"),
                   Parameter('p18', type="VV",
                             doc="Line handles for data"),
                   Parameter('p19', type="VV",
                             doc="Fid values for data"),
                   Parameter('p20', type=Type.STRING,
                             doc="X channel name"),
                   Parameter('p21', type=Type.STRING,
                             doc="Y channel name"),
                   Parameter('p22', type=Type.STRING,
                             doc="Z channel name"),
                   Parameter('p23', type=Type.INT32_T,
                             doc="Plot Grid lines? (0: Just outside edge tics, 1: Grid lines)."),
                   Parameter('p24', type=Type.DOUBLE,
                             doc="Tic Increment (in percent)"),
                   Parameter('p25', type=Type.DOUBLE,
                             doc="Grid increment (in percent)"),
                   Parameter('p26', type=Type.STRING,
                             doc='plot overlay ("" for none)')
               ]),

        Method('ZoneColouredTriPlot_CHIMERA', module='geochimera', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="""
               Plot a tri-plot using colours based on a zone file.
               Optional data masking with masking colour.
               Optioinal database linking.
               """,
               notes="Plot a tri plot using colours based on a zone file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of box)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Triangle side length"),
                   Parameter('p6', type="VV",
                             doc="X channel data"),
                   Parameter('p7', type="VV",
                             doc="Y channel data"),
                   Parameter('p8', type="VV",
                             doc="Z channel data"),
                   Parameter('p9', type="VV",
                             doc="Mask channel data"),
                   Parameter('p10', type=Type.INT32_T,
                             doc='Mask colour; overrides symbol colour where mask data is not dummy. Set to :func:`iColor_MVIEW`("") to not plot.'),
                   Parameter('p11', type="VV",
                             doc="Zone channel data"),
                   Parameter('p12', type=Type.STRING,
                             doc="Zone file name"),
                   Parameter('p13', type=Type.STRING,
                             doc='decorated font name, "" for default symbol font (normally symbols.gfn)'),
                   Parameter('p14', type=Type.INT32_T,
                             doc="Symbol number (>=0)"),
                   Parameter('p15', type=Type.DOUBLE,
                             doc="Symbol size ( >=0)"),
                   Parameter('p16', type=Type.DOUBLE,
                             doc="Symbol angle (-360 to 360)"),
                   Parameter('p17', type=Type.INT32_T,
                             doc="Symbol colour"),
                   Parameter('p18', type=Type.INT32_T,
                             doc="Symbol fill colour"),
                   Parameter('p19', type=Type.INT32_T,
                             doc="Fix symbol edge colour?"),
                   Parameter('p20', type="DB",
                             doc="Database (source of data)"),
                   Parameter('p21', type="VV",
                             doc="Line handles for data"),
                   Parameter('p22', type="VV",
                             doc="Fid values for data"),
                   Parameter('p23', type=Type.STRING,
                             doc="X channel name"),
                   Parameter('p24', type=Type.STRING,
                             doc="Y channel name"),
                   Parameter('p25', type=Type.STRING,
                             doc="Z channel name"),
                   Parameter('p26', type=Type.INT32_T,
                             doc="Plot Grid lines? (0: Just outside edge tics, 1: Grid lines)."),
                   Parameter('p27', type=Type.DOUBLE,
                             doc="Tic Increment (in percent)"),
                   Parameter('p28', type=Type.DOUBLE,
                             doc="Grid increment (in percent)"),
                   Parameter('p29', type=Type.STRING,
                             doc='plot overlay ("" for none)')
               ]),

        Method('StringClassifiedTriPlot_CHIMERA', module='geochimera', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="""
               Plot a tri-plot using symbols based on a symbol class file.
               Optional data masking with masking colour.
               Optioinal database linking.
               """,
               notes="Plot a tri-plot using symbols based on a symbol class file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of box)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Triangle side length"),
                   Parameter('p6', type="VV",
                             doc="X channel data"),
                   Parameter('p7', type="VV",
                             doc="Y channel data"),
                   Parameter('p8', type="VV",
                             doc="Z channel data"),
                   Parameter('p9', type="VV",
                             doc="Mask channel data"),
                   Parameter('p10', type=Type.INT32_T,
                             doc='Mask colour; overrides symbol colour. Set to :func:`iColor_MVIEW`("") to not plot.'),
                   Parameter('p11', type="VV",
                             doc="Class channel data"),
                   Parameter('p12', type=Type.STRING,
                             doc="Class file (:class:`TPAT`) name."),
                   Parameter('p13', type=Type.DOUBLE,
                             doc="Symbol size override. Set to 0.0 to use class file symbol sizes."),
                   Parameter('p14', type="DB",
                             doc="Database (source of data)"),
                   Parameter('p15', type="VV",
                             doc="Line handles for data"),
                   Parameter('p16', type="VV",
                             doc="Fid values for data"),
                   Parameter('p17', type=Type.STRING,
                             doc="X channel name"),
                   Parameter('p18', type=Type.STRING,
                             doc="Y channel name"),
                   Parameter('p19', type=Type.STRING,
                             doc="Z channel name"),
                   Parameter('p20', type=Type.INT32_T,
                             doc="Plot Grid lines? (0: Just outside edge tics, 1: Grid lines)."),
                   Parameter('p21', type=Type.DOUBLE,
                             doc="Tic Increment (in percent)"),
                   Parameter('p22', type=Type.DOUBLE,
                             doc="Grid increment (in percent)"),
                   Parameter('p23', type=Type.STRING,
                             doc='plot overlay ("" for none)')
               ])
    ],
    'Obsolete': [

        Method('GetStringClassifiedSymbolsIndex_CHIMERA', module='geochimera', version='6.3.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Get symbol indices based on a classification :class:`VV`.",
               notes="Obsolete - Use GetStringClassifiedSymbolsIndexFromClassFile_CHIMERA. Scatter and Triplots now use class files.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Classification channel (string type)"),
                   Parameter('p2', type="VV",
                             doc="Symbol indices (returned) (INT :class:`VV`)")
               ]),

        Method('GetStringClassifiedSymbols_CHIMERA', module='geochimera', version='6.3.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Get symbol numbers and colours based on a classification :class:`VV`.",
               notes="""
               Obsolete - Use GetStringClassifiedSymbolsFromClassFile_CHIMERA. Scatter and Triplots now use class files.
               Up to 42 different symbols are defined.
               Index 0 is returned for unclassified strings ""
               Index 1 is returned for unassigned strings (only the
               first 40 different classes get their own unique symbol/colour.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Symbol indices  (INT :class:`VV`)"),
                   Parameter('p2', type="VV",
                             doc="Symbol numbers (returned) (INT :class:`VV`)"),
                   Parameter('p3', type="VV",
                             doc="Symbol colours (returned) (INT :class:`VV`)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="(TRUE/FALSE) Set Unclassified symbol colour to C_ANY_NONE?"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="(TRUE/FALSE) Set Unassigned symbol colour to C_ANY_NONE?")
               ]),

        Method('PlotStringClassifiedSymbolsLegend_CHIMERA', module='geochimera', version='6.3.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Plot legend for the string classified symbols",
               notes="""
               Obsolete - Use :func:`PlotStringClassifiedSymbolsLegendFromClassFile_CHIMERA`. Scatter and Triplots now use class files.
               Up to 42 different symbols are defined.
               Duplicate symbol indices are removed.
               Index 0 is returned for unclassified strings ""
               Index 1 is returned for unassigned strings (only the
               first 40 different classes get their own unique symbol/colour.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="Map view object"),
                   Parameter('p2', type=Type.STRING,
                             doc="title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="left side X location"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="bottom Y bound"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="top Y bound"),
                   Parameter('p6', type="VV",
                             doc="Strings (string :class:`VV`)"),
                   Parameter('p7', type="VV",
                             doc="Symbol indices  (INT :class:`VV`) 0-41"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Plot Unclassified symbol?"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Plot Unassigned symbol?")
               ]),

        Method('Scatter_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Plot the scatter plot on a map.",
               notes="""
               OBSOLETE.
               The view scaling is not altered with any projection. The base view
               is best as the input.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of colour boxes)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="box width"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="box height"),
                   Parameter('p7', type="VV",
                             doc="Horizontal channel"),
                   Parameter('p8', type="VV",
                             doc="Vertical channel"),
                   Parameter('p9', type="VV",
                             doc="Mask channel"),
                   Parameter('p10', type=Type.STRING,
                             doc="Horizontal channel name"),
                   Parameter('p11', type=Type.STRING,
                             doc="Vertical channel name"),
                   Parameter('p12', type=Type.STRING,
                             doc="Mask channel name"),
                   Parameter('p13', type=Type.STRING,
                             doc="Horizontal channel units"),
                   Parameter('p14', type=Type.STRING,
                             doc="Vertical channel units"),
                   Parameter('p15', type=Type.DOUBLE,
                             doc="Min. Horizontal value"),
                   Parameter('p16', type=Type.DOUBLE,
                             doc="Max. Horizontal value"),
                   Parameter('p17', type=Type.DOUBLE,
                             doc="Min. Vertical value"),
                   Parameter('p18', type=Type.DOUBLE,
                             doc="Max. Vertical value"),
                   Parameter('p19', type=Type.DOUBLE,
                             doc="Min. Horizontal range value"),
                   Parameter('p20', type=Type.DOUBLE,
                             doc="Max. Horizontal range value"),
                   Parameter('p21', type=Type.DOUBLE,
                             doc="Min. Vertical range value"),
                   Parameter('p22', type=Type.DOUBLE,
                             doc="Max. Vertical range value"),
                   Parameter('p23', type=Type.INT32_T,
                             doc="Use Min Horz. Range selection?"),
                   Parameter('p24', type=Type.INT32_T,
                             doc="Use Max Horz. Range selection?"),
                   Parameter('p25', type=Type.INT32_T,
                             doc="Use Min Vert. Range selection?"),
                   Parameter('p26', type=Type.INT32_T,
                             doc="Use Max Vert. Range selection?"),
                   Parameter('p27', type=Type.INT32_T,
                             doc="Use linear horizontal axis scaling?"),
                   Parameter('p28', type=Type.INT32_T,
                             doc="Use linear vertical axis scaling?"),
                   Parameter('p29', type=Type.INT32_T,
                             doc="Symbol size (0: small, 1: medium, 2: large)")
               ]),

        Method('Scatter3_CHIMERA', module='geochimera', version='6.3.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Like :func:`Scatter2_CHIMERA`, but passes Line-Fid info, more options.",
               notes="""
               OBSOLETE - Replaced by Scatter4_CHIMERA.
               - As of v6.3, the plotted data is put in its own view. The Line-Fid
               values are passed in to enable Line-Fid linking.
               - Optional Mask symbol colours
               - Optional overlay. (See :class:`SEMPLOT` class).
               - If the classified symbols are used, unique symbols (up to 266) are
               given to the different classes. An "Unassigned" symbol is plotted
               for blank or classes above 266.
               - The view is given a user-projection and so should not be re-used
               for other purposes (like the base view for the :func:`Scatter_CHIMERA` and
               :func:`Scatter2_CHIMERA` functions can be).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of box)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="box width"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="box height"),
                   Parameter('p7', type="VV",
                             doc="Horizontal channel"),
                   Parameter('p8', type="VV",
                             doc="Vertical channel"),
                   Parameter('p9', type="VV",
                             doc="Mask channel"),
                   Parameter('p10', type=Type.STRING,
                             doc='decorated font name, "" for default symbol font (normally symbols.gfn)'),
                   Parameter('p11', type="VV",
                             doc="Symbol numbers"),
                   Parameter('p12', type="VV",
                             doc="Symbol sizes"),
                   Parameter('p13', type="VV",
                             doc="Colours  if symbol number or colour == 0, do not plot"),
                   Parameter('p14', type=Type.INT32_T,
                             doc='Mask colour; overrides symbol colour. Set to :func:`iColor_MVIEW`("") to not plot.'),
                   Parameter('p15', type="DB",
                             doc="Database (source of data)"),
                   Parameter('p16', type="VV",
                             doc="Line handles for data"),
                   Parameter('p17', type="VV",
                             doc="Fid values for data"),
                   Parameter('p18', type=Type.INT32_T,
                             doc="Annotation style 0 - outside, 1 - inside"),
                   Parameter('p19', type=Type.STRING,
                             doc="Horizontal channel name"),
                   Parameter('p20', type=Type.STRING,
                             doc="Vertical channel name"),
                   Parameter('p21', type=Type.STRING,
                             doc="Horizontal channel units"),
                   Parameter('p22', type=Type.STRING,
                             doc="Vertical channel units"),
                   Parameter('p23', type=Type.DOUBLE,
                             doc="Min. Horizontal value, :def_val:`rDUMMY` for default"),
                   Parameter('p24', type=Type.DOUBLE,
                             doc="Max. Horizontal value"),
                   Parameter('p25', type=Type.DOUBLE,
                             doc="Min. Vertical value"),
                   Parameter('p26', type=Type.DOUBLE,
                             doc="Max. Vertical value"),
                   Parameter('p27', type=Type.INT32_T,
                             doc="horizontal axis scaling: 0 - linear, 1 - log"),
                   Parameter('p28', type=Type.INT32_T,
                             doc="vertical axis scaling"),
                   Parameter('p29', type=Type.STRING,
                             doc='plot overlay ("" for none)')
               ]),

        Method('TriPlot_CHIMERA', module='geochimera', version='5.0.7',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Plot the TriPlot on a map.",
               notes="OBSOLETE",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of colour boxes)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="box width"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="box height"),
                   Parameter('p7', type="VV",
                             doc="X channel"),
                   Parameter('p8', type="VV",
                             doc="Y channel"),
                   Parameter('p9', type="VV",
                             doc="Z channel"),
                   Parameter('p10', type="VV",
                             doc="Mask channel"),
                   Parameter('p11', type=Type.STRING,
                             doc="X channel name"),
                   Parameter('p12', type=Type.STRING,
                             doc="Y channel name"),
                   Parameter('p13', type=Type.STRING,
                             doc="Z channel name"),
                   Parameter('p14', type=Type.STRING,
                             doc="Mask channel name"),
                   Parameter('p15', type=Type.DOUBLE,
                             doc="Min. X range value"),
                   Parameter('p16', type=Type.DOUBLE,
                             doc="Max. X range value"),
                   Parameter('p17', type=Type.DOUBLE,
                             doc="Min. Y range value"),
                   Parameter('p18', type=Type.DOUBLE,
                             doc="Max. Y range value"),
                   Parameter('p19', type=Type.DOUBLE,
                             doc="Min. Z range value"),
                   Parameter('p20', type=Type.DOUBLE,
                             doc="Max. Z range value"),
                   Parameter('p21', type=Type.INT32_T,
                             doc="Use Min X Range selection?"),
                   Parameter('p22', type=Type.INT32_T,
                             doc="Use Max X Range selection?"),
                   Parameter('p23', type=Type.INT32_T,
                             doc="Use Min Y Range selection?"),
                   Parameter('p24', type=Type.INT32_T,
                             doc="Use Max Y Range selection?"),
                   Parameter('p25', type=Type.INT32_T,
                             doc="Use Min Z Range selection?"),
                   Parameter('p26', type=Type.INT32_T,
                             doc="Use Max Z Range selection?"),
                   Parameter('p27', type=Type.INT32_T,
                             doc="Plot Grid lines? (0: Just outside edge tics, 1: Grid lines)."),
                   Parameter('p28', type=Type.DOUBLE,
                             doc="Tic Increment (in percent)"),
                   Parameter('p29', type=Type.DOUBLE,
                             doc="Grid increment (in percent)"),
                   Parameter('p30', type=Type.INT32_T,
                             doc="Symbol size (0: small, 1: medium, 2: large)")
               ]),

        Method('TriPlot3_CHIMERA', module='geochimera', version='6.3.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="TriPlot to its own view, with Line-Fid info.",
               notes="OBSOLETE",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVIEW",
                             doc="View"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location (bottom left corner of box)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Triangle side length"),
                   Parameter('p6', type="VV",
                             doc="X channel"),
                   Parameter('p7', type="VV",
                             doc="Y channel"),
                   Parameter('p8', type="VV",
                             doc="Z channel"),
                   Parameter('p9', type="VV",
                             doc="Mask channel"),
                   Parameter('p10', type=Type.STRING,
                             doc='decorated font name, "" for default symbol font (normally symbols.gfn)'),
                   Parameter('p11', type="VV",
                             doc="Symbol numbers"),
                   Parameter('p12', type="VV",
                             doc="Symbol sizes"),
                   Parameter('p13', type="VV",
                             doc="Symbol colours  if symbol number or colour == 0, do not plot"),
                   Parameter('p14', type=Type.INT32_T,
                             doc='Mask colour; overrides symbol colour. Set to :func:`iColor_MVIEW`("") to not plot.'),
                   Parameter('p15', type="DB",
                             doc="Database (source of data)"),
                   Parameter('p16', type="VV",
                             doc="Line handles for data"),
                   Parameter('p17', type="VV",
                             doc="Fid values for data"),
                   Parameter('p18', type=Type.STRING,
                             doc="X channel name"),
                   Parameter('p19', type=Type.STRING,
                             doc="Y channel name"),
                   Parameter('p20', type=Type.STRING,
                             doc="Z channel name"),
                   Parameter('p21', type=Type.INT32_T,
                             doc="Plot Grid lines? (0: Just outside edge tics, 1: Grid lines)."),
                   Parameter('p22', type=Type.DOUBLE,
                             doc="Tic Increment (in percent)"),
                   Parameter('p23', type=Type.DOUBLE,
                             doc="Grid increment (in percent)"),
                   Parameter('p24', type=Type.STRING,
                             doc='plot overlay ("" for none)')
               ])
    ]
}

