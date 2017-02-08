from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('IP',
                 doc="""
This class is used in the :class:`IP` System for the import, export
and processing of Induced Polarization data.
""",
                 notes="""
The following defines are used in GX code but are not
part of any functions:

:def:`IP_ARRAY`
:def:`IP_CHANNELS`
:def:`IP_LINES`
""")


gx_defines = [
    Define('IP_ARRAY',
           doc=":class:`IP` Array options",
           constants=[
               Constant('IP_ARRAY_DPDP', value='0', type=Type.INT32_T)                        ,
               Constant('IP_ARRAY_PLDP', value='1', type=Type.INT32_T)                        ,
               Constant('IP_ARRAY_PLPL', value='2', type=Type.INT32_T)                        ,
               Constant('IP_ARRAY_GRAD', value='3', type=Type.INT32_T)                        ,
               Constant('IP_ARRAY_WENNER', value='5', type=Type.INT32_T)                        ,
               Constant('IP_ARRAY_SCHLUMBERGER', value='6', type=Type.INT32_T)                        ,
               Constant('IP_ARRAY_UNKNOWN', value='7', type=Type.INT32_T)                        ,
               Constant('IP_ARRAY_3D', value='9', type=Type.INT32_T)                        ,
               Constant('IP_ARRAY_3D_PLDP', value='10', type=Type.INT32_T)                        ,
               Constant('IP_ARRAY_3D_PLPL', value='11', type=Type.INT32_T)                        
           ]),

    Define('IP_CHANNELS',
           doc="Channels to display",
           constants=[
               Constant('IP_CHANNELS_DISPLAYED', value='0', type=Type.INT32_T)                        ,
               Constant('IP_CHANNELS_SELECTED', value='1', type=Type.INT32_T)                        ,
               Constant('IP_CHANNELS_ALL', value='2', type=Type.INT32_T)                        
           ]),

    Define('IP_DOMAIN',
           doc="Types of Domains",
           constants=[
               Constant('IP_DOMAIN_NONE', value='-1', type=Type.INT32_T)                        ,
               Constant('IP_DOMAIN_TIME', value='0', type=Type.INT32_T)                        ,
               Constant('IP_DOMAIN_FREQUENCY', value='1', type=Type.INT32_T)                        ,
               Constant('IP_DOMAIN_BOTH', value='2', type=Type.INT32_T)                        
           ]),

    Define('IP_DUPLICATE',
           doc="How to handle duplicates",
           constants=[
               Constant('IP_DUPLICATE_APPEND', value='0', type=Type.INT32_T)                        ,
               Constant('IP_DUPLICATE_OVERWRITE', value='1', type=Type.INT32_T)                        
           ]),

    Define('IP_FILTER',
           doc="Fraser Filters",
           constants=[
               Constant('IP_FILTER_PANTLEG', value='1', type=Type.INT32_T,
                        doc="""
                        Regular pant-leg filter:    _!_  maxn:
                        /*_*\\   n1
                        /*/ \\*\\  n2
                        /*/   \\*\\ n3
                        :  :
                        """)                        ,
               Constant('IP_FILTER_PANTLEGP', value='2', type=Type.INT32_T,
                        doc="""
                        Regular pant-leg filter with top at first point:
                        !  nscp:
                        /*\\   n1
                        /*_*\\  n2
                        /*/ \\*\\ n3
                        :  :
                        """)                        ,
               Constant('IP_FILTER_PYRIAMID', value='3', type=Type.INT32_T,
                        doc="""
                        Regular pyramid filter:     _!_  maxn:
                        /* *\\   n1
                        /* * *\\  n2
                        /* * * *\\ n3
                        :  :
                        """)                        ,
               Constant('IP_FILTER_PYRIAMIDP', value='4', type=Type.INT32_T,
                        doc="""
                        Regular pyramid filter      !  maxn:
                        with peak on a point:      /*\\   n1
                        /* *\\  n2
                        /* * *\\ n3
                        :  :
                        """)                        
           ]),

    Define('IP_I2XIMPMODE',
           doc="Interpext Import Mode",
           constants=[
               Constant('IP_I2XIMPMODE_REPLACE', value='0', type=Type.INT32_T,
                        doc="Recreates the line from scratch.")                        ,
               Constant('IP_I2XIMPMODE_MERGE', value='1', type=Type.INT32_T,
                        doc="""
                        Looks for matching Tx1 and N values and
                        replaces data in matching lines only.
                        """)                        
           ]),

    Define('IP_I2XINV',
           doc="Type of Inversion",
           constants=[
               Constant('IP_I2XINV_IMAGE', value='0', type=Type.INT32_T)                        ,
               Constant('IP_I2XINV_ZONGE', value='1', type=Type.INT32_T)                        
           ]),

    Define('IP_LINES',
           doc="Lines to display",
           constants=[
               Constant('IP_LINES_DISPLAYED', value='0', type=Type.INT32_T)                        ,
               Constant('IP_LINES_SELECTED', value='1', type=Type.INT32_T)                        ,
               Constant('IP_LINES_ALL', value='2', type=Type.INT32_T)                        
           ]),

    Define('IP_PLOT',
           doc="Type of Plot",
           constants=[
               Constant('IP_PLOT_PSEUDOSECTION', value='0', type=Type.INT32_T)                        ,
               Constant('IP_PLOT_STACKEDSECTION', value='1', type=Type.INT32_T)                        
           ]),

    Define('IP_STACK_TYPE',
           doc="Spacing Types",
           constants=[
               Constant('IP_STACK_TYPE_MAP', value='0', type=Type.INT32_T,
                        doc="""
                        Use map-based spacing, and preserve the directions of the
                        original lines by rotating the sections as desired to their true
                        locations. (At present only N-S and E-W sections are supported).
                        """)                        ,
               Constant('IP_STACK_TYPE_EQUAL', value='1', type=Type.INT32_T,
                        doc="""
                        Spaces the sections equally, with enough room to
                        guarantee no overlap with high N-values or closely spaced lines.
                        """)                        ,
               Constant('IP_STACK_TYPE_GEOGRAPHIC', value='2', type=Type.INT32_T,
                        doc="Now the same as IP_STACK_MAP")                        
           ]),

    Define('IP_STNSCALE',
           doc="Station Scaling",
           constants=[
               Constant('IP_STNSCALE_NONE', value='0', type=Type.INT32_T,
                        doc="Station numbers become X or Y locations")                        ,
               Constant('IP_STNSCALE_ASPACE', value='1', type=Type.INT32_T,
                        doc="Multiply station numbers by the A spacing")                        ,
               Constant('IP_STNSCALE_VALUE', value='2', type=Type.INT32_T,
                        doc="Multiply by an input value.")                        ,
               Constant('IP_STNSCALE_FILE', value='3', type=Type.INT32_T,
                        doc="Look up locations from a CSV Line/Station/X/Y file")                        
           ]),

    Define('IP_SYS',
           doc="Instrument",
           constants=[
               Constant('IP_SYS_IPDATA', value='0', type=Type.INT32_T)                        ,
               Constant('IP_SYS_IP2', value='1', type=Type.INT32_T)                        ,
               Constant('IP_SYS_IP6', value='2', type=Type.INT32_T)                        ,
               Constant('IP_SYS_IP10', value='3', type=Type.INT32_T)                        ,
               Constant('IP_SYS_SYSCALR2', value='4', type=Type.INT32_T)                        ,
               Constant('IP_SYS_IPR11', value='5', type=Type.INT32_T)                        ,
               Constant('IP_SYS_IPR12', value='6', type=Type.INT32_T)                        ,
               Constant('IP_SYS_PHOENIX', value='7', type=Type.INT32_T)                        ,
               Constant('IP_SYS_PHOENIX_V2', value='8', type=Type.INT32_T)                        ,
               Constant('IP_SYS_ELREC_PRO', value='9', type=Type.INT32_T)                        
           ]),

    Define('IP_UBC_CONTROL',
           doc="Types of Domains",
           constants=[
               Constant('IP_UBC_CONTROL_NONE', value='-1', type=Type.INT32_T)                        ,
               Constant('IP_UBC_CONTROL_DEFAULT', value='0', type=Type.INT32_T)                        ,
               Constant('IP_UBC_CONTROL_FILE', value='1', type=Type.INT32_T)                        ,
               Constant('IP_UBC_CONTROL_VALUE', value='2', type=Type.INT32_T)                        ,
               Constant('IP_UBC_CONTROL_LENGTH', value='3', type=Type.INT32_T)                        
           ]),

    Define('IP_PLDP_CONV',
           doc="Types of Domains",
           constants=[
               Constant('IP_PLDP_CONV_CLOSE_RX', value='0', type=Type.INT32_T)                        ,
               Constant('IP_PLDP_CONV_MID_RX', value='1', type=Type.INT32_T)                        ,
               Constant('IP_PLDP_CONV_DISTANT_RX', value='2', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Plot Jobs': [

        Method('ConvertUBCIP2DToGrid_IP', module='geogxx', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Convert a UBC 2D model to a regular grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Output grid file name"),
                   Parameter('p2', type="PG",
                             doc="Model data"),
                   Parameter('p3', type="VV",
                             doc="Model cells sizes (input)"),
                   Parameter('p4', type="VV",
                             doc="Model cells sizes (input)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Top-left corner X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Top-left corner Z"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Output grid cell size in X"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Output grid cell size in Z"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Output reciprocal of values (0:No, 1:Yes) for resistivity?")
               ]),

        Method('CreateDefaultJob_IP', module='geogxx', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Create a default job from scratch.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type=Type.STRING,
                             doc="File name of the INI file to create (forces correct suffix)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`IP_PLOT`")
               ]),

        Method('ExportUBCIP3_IP', module='geogxx', version='8.1',
               availability=Availability.EXTENSION, 
               doc="Export of :class:`IP` data to UBC format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Output :class:`IP` channel name"),
                   Parameter('p5', type=Type.STRING,
                             doc='Output error channel name ("" for none)'),
                   Parameter('p6', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('p7', type=Type.STRING,
                             doc="Output TOPO file name"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="version number (3 or 5)")
               ]),

        Method('ExportUBCIPControl_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Export a control file for using in the UBC IPINV2D programme.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Output control file name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="niter"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="irest"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="chifact"),
                   Parameter('p5', type=Type.STRING,
                             doc=":class:`IP` obs file"),
                   Parameter('p6', type=Type.STRING,
                             doc="conductivity file"),
                   Parameter('p7', type=Type.STRING,
                             doc="mesh file"),
                   Parameter('p8', type=Type.STRING,
                             doc="topography file"),
                   Parameter('p9', type=Type.STRING,
                             doc="initial model file"),
                   Parameter('p10', type=Type.STRING,
                             doc="reference model"),
                   Parameter('p11', type=Type.STRING,
                             doc="alphas"),
                   Parameter('p12', type=Type.STRING,
                             doc="weights file")
               ]),

        Method('ExportUBCIPControlV5_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Export a control file for using in the UBC IPINV2D programme.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Output control file name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="niter"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="chifact"),
                   Parameter('p4', type=Type.STRING,
                             doc="RES obs file"),
                   Parameter('p5', type=Type.STRING,
                             doc="topography file (required)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Conductivity type :def:`IP_UBC_CONTROL` FILE or VALUE"),
                   Parameter('p7', type=Type.STRING,
                             doc='Conductivity file (can be "") or value'),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Mesh type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('p9', type=Type.STRING,
                             doc='mesh file (can be "") or value'),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Initial model type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('p11', type=Type.STRING,
                             doc='initial model file (can be "") or value'),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Reference model type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('p13', type=Type.STRING,
                             doc='reference model file (can be "") or value('),
                   Parameter('p14', type=Type.INT32_T,
                             doc="Alphas type :def:`IP_UBC_CONTROL` FILE, VALUE, LENGTH or DEFAULT"),
                   Parameter('p15', type=Type.STRING,
                             doc='alphas  file (can be ""), value or length'),
                   Parameter('p16', type=Type.STRING,
                             doc="weights file")
               ]),

        Method('ExportUBCRes3_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Export of :class:`IP` Resistivity data to UBC format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Output voltage channel name"),
                   Parameter('p5', type=Type.STRING,
                             doc="Output current channel name"),
                   Parameter('p6', type=Type.STRING,
                             doc='Output error channel name ("" for none)'),
                   Parameter('p7', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('p8', type=Type.STRING,
                             doc="Output TOPO file name"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="version number (3 or 5)")
               ]),

        Method('ExportUBCResControl_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Export a control file for using in the UBC DCINV2D programme.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Output control file name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="niter"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="irest"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="chifact"),
                   Parameter('p5', type=Type.STRING,
                             doc="RES obs file"),
                   Parameter('p6', type=Type.STRING,
                             doc="mesh file"),
                   Parameter('p7', type=Type.STRING,
                             doc="topography file (required)"),
                   Parameter('p8', type=Type.STRING,
                             doc='initial model file (can be "" or "NULL")'),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="reference model conductivity"),
                   Parameter('p10', type=Type.STRING,
                             doc="alphas"),
                   Parameter('p11', type=Type.STRING,
                             doc="weights file")
               ]),

        Method('ExportUBCResControlV5_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Export a control file for using in the UBC DCINV2D programme.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Output control file name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="niter"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="chifact"),
                   Parameter('p4', type=Type.STRING,
                             doc="RES obs file"),
                   Parameter('p5', type=Type.STRING,
                             doc="topography file (required)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Mesh type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('p7', type=Type.STRING,
                             doc='mesh file (can be "") or value'),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Initial model type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('p9', type=Type.STRING,
                             doc='initial model file (can be "") or value'),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Reference model type :def:`IP_UBC_CONTROL` FILE, VALUE or DEFAULT"),
                   Parameter('p11', type=Type.STRING,
                             doc='reference model file (can be "") or value('),
                   Parameter('p12', type=Type.INT32_T,
                             doc="Alphas type :def:`IP_UBC_CONTROL` FILE, VALUE, LENGTH or DEFAULT"),
                   Parameter('p13', type=Type.STRING,
                             doc='alphas  file (can be ""), value or length'),
                   Parameter('p14', type=Type.STRING,
                             doc="weights file")
               ]),

        Method('ExportDataToUBC3D_IP', module='geogxx', version='9.2',
               availability=Availability.EXTENSION, 
               doc="Export of :class:`IP` data to UBC 3D :class:`IP` format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type="LST",
                             doc="Lines to export (Name, Symbol)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Locations only (0: No, 1: Yes)?"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Include Z values (0: No, 1: Yes)?"),
                   Parameter('p6', type=Type.STRING,
                             doc=':class:`IP` channel name (can be "" if exporting locations only)'),
                   Parameter('p7', type=Type.STRING,
                             doc='Error channel name (can be "" if exporting locations only)'),
                   Parameter('p8', type=Type.STRING,
                             doc='Mask channel name (can be "")'),
                   Parameter('p9', type=Type.INT32_T,
                             doc="IPTYPE (1: Vp, 2: Chargeability)"),
                   Parameter('p10', type=Type.STRING,
                             doc='Comments (can be "")'),
                   Parameter('p11', type=Type.STRING,
                             doc="Output OBS file name")
               ]),

        Method('ImportUBC2DMOD_IP', module='geogxx', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Import a MOD file from the UBC IPINV2D programme.",
               return_type="PG",
               return_doc=":class:`PG` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="UBC MOD file name to import"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="0 - CON, 1 - CHG")
               ]),

        Method('ImportUBC2DMSH_IP', module='geogxx', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Import a MSH file from the UBC IPINV2D programme.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="UBC MSH file to import"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Returned origin X (top left corner)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Returned origin Z (top left corner)"),
                   Parameter('p4', type="VV",
                             doc="Cell widths  (left to right) (real)"),
                   Parameter('p5', type="VV",
                             doc="Cell heights (top down) (real)")
               ]),

        Method('ImportUBC2DTopo_IP', module='geogxx', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Import a Topography file from the UBC IPINV2D programme.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="UBC Topo file to import"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Returned top of mesh elevation"),
                   Parameter('p3', type="VV",
                             doc="Topography X values"),
                   Parameter('p4', type="VV",
                             doc="Topography Z values (elevations)")
               ]),

        Method('OpenJob_IP', module='geogxx', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Open a :class:`IP` plotting job",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="job file name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Job type :def:`IP_PLOT`")
               ]),

        Method('SaveJob_IP', module='geogxx', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Save a :class:`IP` plotting job",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="job file name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Job type  :def:`IP_PLOT`")
               ]),

        Method('TrimUBC2DModel_IP', module='geogxx', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc="Trim the padding cells from the UBC IPINV2D Model.",
               return_type="PG",
               return_doc=":class:`PG` Object",
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Input model (unchanged)"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Cells to remove on left"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Cells to remove on right"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Cells to remove on the bottom"),
                   Parameter('p5', type="VV",
                             doc="Column widths (modified)"),
                   Parameter('p6', type="VV",
                             doc="Row heights (modified)"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Top left corner X (modified)")
               ]),

        Method('WriteDistantElectrodes_IP', module='geogxx', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="Write distant electrode locations to channels",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object")
               ]),

        Method('WriteDistantElectrodesLST_IP', module='geogxx', version='6.4.2',
               availability=Availability.EXTENSION, 
               doc="Write distant electrode locations to channels for a :class:`LST` of lines",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type="LST",
                             doc="Lines to write out")
               ])
    ],
    'Miscellaneous': [

        Method('AverageDuplicatesQC_IP', module='geogxx', version='7.3.0',
               availability=Availability.EXTENSION, 
               doc="Average duplicate samples in a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to export from"),
                   Parameter('p3', type=Type.STRING,
                             doc="Mask or reference channel (required)"),
                   Parameter('p4', type=Type.STRING,
                             doc="QC channel (can be left blank)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`IP_DUPLICATE`")
               ]),

        Method('Create_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create :class:`IP`.",
               return_type="IP",
               return_doc=":class:`IP` Object"),

        Method('Destroy_IP', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`IP` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Handle")
               ]),

        Method('ExportI2X_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Export line(s) to an Interpex RESIX I2X format file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to export from"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of the file"),
                   Parameter('p4', type=Type.STRING,
                             doc="Name of the line"),
                   Parameter('p5', type=Type.STRING,
                             doc="Resistivity (data) channel"),
                   Parameter('p6', type=Type.STRING,
                             doc=':class:`IP` (data) channel (can be "")'),
                   Parameter('p7', type=Type.STRING,
                             doc='Image model resistivity channel (can be "")'),
                   Parameter('p8', type=Type.STRING,
                             doc='Image model :class:`IP` channel (can be "")'),
                   Parameter('p9', type=Type.STRING,
                             doc='Image model synthetic resistivity channel (can be "")'),
                   Parameter('p10', type=Type.STRING,
                             doc='Image model synthetic :class:`IP` channel (can be "")'),
                   Parameter('p11', type=Type.STRING,
                             doc='Resistivity (polygon) channel (can be "")'),
                   Parameter('p12', type=Type.STRING,
                             doc=':class:`IP` (polygon) channel (can be "")')
               ]),

        Method('ExportIPDATA_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Exports data in the Geosoft IPDATA format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to export from"),
                   Parameter('p3', type=Type.STRING,
                             doc="Channel to export"),
                   Parameter('p4', type=Type.STRING,
                             doc="Title for IPDATA files")
               ]),

        Method('ExportIPDATADir_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Exports data in the Geosoft IPDATA format in the specified directory",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to export from"),
                   Parameter('p3', type=Type.STRING,
                             doc="Channel to export"),
                   Parameter('p4', type=Type.STRING,
                             doc="Title for IPDATA files"),
                   Parameter('p5', type=Type.STRING,
                             doc="Directory for IPDATA files")
               ]),

        Method('ExportIPRED_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Exports pseudo-section in the Geosoft IPRED format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to export from"),
                   Parameter('p3', type=Type.STRING,
                             doc="Title for first line of file"),
                   Parameter('p4', type=Type.STRING,
                             doc="Channel to process"),
                   Parameter('p5', type=Type.STRING,
                             doc="File suffix (type)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`IP_FILTER`"),
                   Parameter('p7', type=Type.STRING,
                             doc="The Fraser Filter weights"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="First Station position (:def_val:`rDUMMY` for default)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Last Station position  (:def_val:`rDUMMY` for default)"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Maximum n spacing")
               ]),

        Method('ExportIPREDDir_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Exports pseudo-section in the Geosoft IPRED format in the specified directory",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to export from"),
                   Parameter('p3', type=Type.STRING,
                             doc="Title for first line of file"),
                   Parameter('p4', type=Type.STRING,
                             doc="Channel to process"),
                   Parameter('p5', type=Type.STRING,
                             doc="File suffix (type)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`IP_FILTER`"),
                   Parameter('p7', type=Type.STRING,
                             doc="The Fraser Filter weights"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="First Station position (:def_val:`rDUMMY` for default)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Last Station position  (:def_val:`rDUMMY` for default)"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Maximum n spacing"),
                   Parameter('p11', type=Type.STRING,
                             doc="Directory to export to")
               ]),

        Method('ExportLineIPDATA_IP', module='geogxx', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Exports one line of data in the Geosoft IPDATA format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to export from"),
                   Parameter('p3', type=Type.STRING,
                             doc="Line to export"),
                   Parameter('p4', type=Type.STRING,
                             doc="Channel to export"),
                   Parameter('p5', type=Type.STRING,
                             doc="Title for IPDATA files")
               ]),

        Method('ExportSGDF_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Exports data to a Scintrex Geophysical Data Format file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to export from"),
                   Parameter('p3', type=Type.STRING,
                             doc="SGDF file to create"),
                   Parameter('p4', type=Type.STRING,
                             doc="Time Domain channel or Frequency Amplitude Channel"),
                   Parameter('p5', type=Type.STRING,
                             doc="Frequency Domain Phase channel (optional)")
               ]),

        Method('GetNValueLST_IP', module='geogxx', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Fill a list with unique N values in selected lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('GetTopoLine_IP', module='geogxx', version='6.4.2',
               availability=Availability.EXTENSION, 
               doc="Get topography values for a line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import data to"),
                   Parameter('p3', type=Type.STRING,
                             doc="Line name"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc='Starting "X" (station) value (:def_val:`rDUMMY` for default)'),
                   Parameter('p5', type=Type.DOUBLE,
                             doc='Ending "X" (station) value (:def_val:`rDUMMY` for default)'),
                   Parameter('p6', type=Type.DOUBLE,
                             doc='"X" increment along the line (:def_val:`rDUMMY` for default = half "A" separation)'),
                   Parameter('p7', type="VV",
                             doc="Returned topography values")
               ]),

        Method('iGetChanDomain_IP', module='geogxx', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Is this channel registered as a Time or Frequency domain channel?",
               return_type=Type.INT32_T,
               return_doc=":def:`IP_DOMAIN`",
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type=Type.STRING,
                             doc="channel to check")
               ]),

        Method('IGetChanLabel_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Get the default label and units for a given channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Input channel"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="Returned label"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Label length"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="Returned units"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DEFAULT',
                             doc="Units label length")
               ]),

        Method('GetChannelInfo_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Time Windows or Frequency info from a channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type=Type.STRING,
                             doc="channel to check"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc=":def:`IP_DOMAIN`"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Delay or Base Frequency"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="Number of time windows or frequencies"),
                   Parameter('p7', type="VV",
                             doc="Time windows or frequencies")
               ]),

        Method('SetChannelInfo_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Set Time Windows or Frequency info for a channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type=Type.STRING,
                             doc="channel to check"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`IP_DOMAIN`"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Delay or Base Frequency"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Number of time windows or frequencies"),
                   Parameter('p7', type="VV",
                             doc="Time windows or frequencies")
               ]),

        Method('ImportDump_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports data from an :class:`IP` instrument dump file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`IP_SYS`"),
                   Parameter('p3', type="DB",
                             doc=":class:`DB` Handle"),
                   Parameter('p4', type=Type.STRING,
                             doc="Dump file name")
               ]),

        Method('ImportGrid_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports data from a grid",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import data to"),
                   Parameter('p3', type=Type.STRING,
                             doc="The name of the grid file, with decorations"),
                   Parameter('p4', type=Type.STRING,
                             doc="The name of the channel to import to")
               ]),

        Method('ImportI2X_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports an Interpex RESIX I2X format file to a line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import to"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of file to import"),
                   Parameter('p4', type=Type.STRING,
                             doc="Line to import to"),
                   Parameter('p5', type=Type.STRING,
                             doc="Resistivity (data) channel"),
                   Parameter('p6', type=Type.STRING,
                             doc=':class:`IP` (data) channel (can be "")'),
                   Parameter('p7', type=Type.STRING,
                             doc='Image model resistivity channel (can be "")'),
                   Parameter('p8', type=Type.STRING,
                             doc='Image model :class:`IP` channel (can be "")'),
                   Parameter('p9', type=Type.STRING,
                             doc='Image model synthetic resistivity channel (can be "")'),
                   Parameter('p10', type=Type.STRING,
                             doc='Image model synthetic :class:`IP` channel (can be "")'),
                   Parameter('p11', type=Type.STRING,
                             doc='Resistivity (polygon) channel (can be "")'),
                   Parameter('p12', type=Type.STRING,
                             doc=':class:`IP` (polygon) channel (can be "")'),
                   Parameter('p13', type=Type.INT32_T,
                             doc=":def:`IP_I2XIMPMODE`")
               ]),

        Method('ImportI2XEx_IP', module='geogxx', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`ImportI2X_IP`, with Zonge data imported as well.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import to"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of file to import"),
                   Parameter('p4', type=Type.STRING,
                             doc="Line to import to"),
                   Parameter('p5', type=Type.STRING,
                             doc="Resistivity (data) channel"),
                   Parameter('p6', type=Type.STRING,
                             doc=':class:`IP` (data) channel (can be "")'),
                   Parameter('p7', type=Type.STRING,
                             doc='Image model resistivity channel (can be "")'),
                   Parameter('p8', type=Type.STRING,
                             doc='Image model :class:`IP` channel (can be "")'),
                   Parameter('p9', type=Type.STRING,
                             doc='Image model synthetic resistivity channel (can be "")'),
                   Parameter('p10', type=Type.STRING,
                             doc='Image model synthetic :class:`IP` channel (can be "")'),
                   Parameter('p11', type=Type.STRING,
                             doc='Resistivity (polygon) channel (can be "")'),
                   Parameter('p12', type=Type.STRING,
                             doc=':class:`IP` (polygon) channel (can be "")'),
                   Parameter('p13', type=Type.STRING,
                             doc='Zonge Resistivity channel (can be "")'),
                   Parameter('p14', type=Type.STRING,
                             doc='Zonge :class:`IP` channel (can be "")'),
                   Parameter('p15', type=Type.INT32_T,
                             doc=":def:`IP_I2XIMPMODE`")
               ]),

        Method('ImportInstrumentationGDD_IP', module='geogxx', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports an Instrumentation GDD format file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import to"),
                   Parameter('p3', type=Type.STRING,
                             doc="GDD file name")
               ]),

        Method('ImportIPDATA_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports data in the Geosoft IPDATA format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import to"),
                   Parameter('p3', type=Type.STRING,
                             doc="IPDATA file name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Channel to import to")
               ]),

        Method('ImportIPDATA2_IP', module='geogxx', version='5.1.0',
               availability=Availability.EXTENSION, 
               doc="Imports data in the Geosoft IPDATA format - up to two arrays.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import to"),
                   Parameter('p3', type=Type.STRING,
                             doc="IPDATA file name"),
                   Parameter('p4', type=Type.STRING,
                             doc='Channel to import to (default is ":class:`IP`")'),
                   Parameter('p5', type=Type.STRING,
                             doc="(optional) Second channel to import to")
               ]),

        Method('ImportIPRED_IP', module='geogxx', version='5.1.0',
               availability=Availability.EXTENSION, 
               doc="Imports data from the Geosoft IPRED format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import to"),
                   Parameter('p3', type=Type.STRING,
                             doc="File to import from"),
                   Parameter('p4', type=Type.STRING,
                             doc="Channel to import")
               ]),

        Method('ImportMergeIPRED_IP', module='geogxx', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Imports IPRED data to an existing line.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import to"),
                   Parameter('p3', type=Type.STRING,
                             doc="File to import from"),
                   Parameter('p4', type=Type.STRING,
                             doc="Channel to import")
               ]),

        Method('ImportSGDF_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports data from a Scintrex Geophysical Data Format file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import to"),
                   Parameter('p3', type=Type.STRING,
                             doc="SGDF file name")
               ]),

        Method('ImportTopoCSV_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports topography data from a CSV line-station file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to calculate topography for"),
                   Parameter('p3', type=Type.STRING,
                             doc="The name of CSV file")
               ]),

        Method('ImportTopoGrid_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports topography data from a grid",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to calculate topography for"),
                   Parameter('p3', type=Type.STRING,
                             doc="The name of the grid file, with decorations")
               ]),

        Method('ImportZongeAVG_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports a Zonge AVG format file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import to"),
                   Parameter('p3', type=Type.STRING,
                             doc="FLD file name"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Line number (will be scaled if applicable)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`IP_STNSCALE`"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Line, station multiplier (for :def_val:`IP_STNSCALE_VALUE`)")
               ]),

        Method('ImportZongeFLD_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Imports a Zonge FLD format file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to import to"),
                   Parameter('p3', type=Type.STRING,
                             doc="FLD file name"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`IP_STNSCALE`"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Line, station multiplier (for :def_val:`IP_STNSCALE_VALUE`)")
               ]),

        Method('NewXYDatabase_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc='Create a subset database using a mask channel, "N" value',
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type="DB",
                             doc="New :class:`DB` object"),
                   Parameter('p4', type="VV",
                             doc="Channel list"),
                   Parameter('p5', type=Type.STRING,
                             doc="Mask channel"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc='"N" Value')
               ]),

        Method('PseudoPlot_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create pseudo-sections of a single line using a control file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('p4', type=Type.STRING,
                             doc="current line name"),
                   Parameter('p5', type=Type.STRING,
                             doc="map name to create")
               ]),

        Method('PseudoPlot2_IP', module='geogxx', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`PseudoPlot_IP`, but specify a tag for grids created.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('p4', type=Type.STRING,
                             doc="current line name"),
                   Parameter('p5', type=Type.STRING,
                             doc="tag for created grids"),
                   Parameter('p6', type=Type.STRING,
                             doc="map name to create")
               ]),

        Method('PseudoPlot2Dir_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`PseudoPlot2_IP`, but with directory specified.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('p4', type=Type.STRING,
                             doc="current line name"),
                   Parameter('p5', type=Type.STRING,
                             doc="tag for created grids"),
                   Parameter('p6', type=Type.STRING,
                             doc="map name to create"),
                   Parameter('p7', type=Type.STRING,
                             doc="directory to create files")
               ]),

        Method('PSStack_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create a stacked pseudo-section plot using a control file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc="channel to plot"),
                   Parameter('p4', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('p5', type=Type.STRING,
                             doc="map name to create")
               ]),

        Method('PSStack2_IP', module='geogxx', version='5.1.0',
               availability=Availability.EXTENSION, 
               doc="As :func:`PSStack_IP`, but select section spacing option.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc="channel to plot"),
                   Parameter('p4', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`IP_STACK_TYPE`"),
                   Parameter('p6', type=Type.STRING,
                             doc="map name to create")
               ]),

        Method('PSStack2Dir_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`PseudoPlot2_IP`, but with directory specified.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc="channel to plot"),
                   Parameter('p4', type=Type.STRING,
                             doc='"IPPLOT" INI file name'),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`IP_STACK_TYPE`"),
                   Parameter('p6', type=Type.STRING,
                             doc="map name to create"),
                   Parameter('p7', type=Type.STRING,
                             doc="directory to create files")
               ]),

        Method('QCChanLST_IP', module='geogxx', version='7.3.0',
               availability=Availability.EXTENSION, 
               doc="Fill a list with QC channels.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('Recalculate_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Recalculate derived channel values.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database")
               ]),

        Method('RecalculateEx_IP', module='geogxx', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Recalculate derived channel values, with option for including/excluding location calculations.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Recalculate XYZ locations (TRUE or FALSE)?")
               ]),

        Method('RecalculateZ_IP', module='geogxx', version='5.1.1',
               availability=Availability.EXTENSION, 
               doc="Recalculate Z channel values.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database")
               ]),

        Method('RESIX_Zonge_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Runs the Interpex RESIX Zonge inversion on selected lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database object"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of the line"),
                   Parameter('p4', type=Type.STRING,
                             doc="Apparent resistivity channel"),
                   Parameter('p5', type=Type.STRING,
                             doc="Synthetic Apparent resistivity channel"),
                   Parameter('p6', type=Type.STRING,
                             doc="Inverted Apparent resistivity channel"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="invert :class:`IP` data too? :def:`IP_I2XINV`"),
                   Parameter('p8', type=Type.STRING,
                             doc=":class:`IP` channel"),
                   Parameter('p9', type=Type.STRING,
                             doc="Synthetic :class:`IP` channel"),
                   Parameter('p10', type=Type.STRING,
                             doc="Inverted :class:`IP` channel")
               ]),

        Method('SetImportMode_IP', module='geogxx', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="When importing data to a line, set append/overwrite mode.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="0: Overwrite, 1: Append")
               ]),

        Method('Window_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Window an :class:`IP` array channel to produce a normal channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc=":class:`VA` channel to use"),
                   Parameter('p4', type=Type.STRING,
                             doc="New channel"),
                   Parameter('p5', type=Type.STRING,
                             doc="Window list")
               ]),

        Method('WinnowChanList_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Removes obviously non-pseudo-section type channels from list.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="List of channels")
               ]),

        Method('WinnowChanList2_IP', module='geogxx', version='5.1.3',
               availability=Availability.EXTENSION, 
               doc="Same as :func:`WinnowChanList_IP`, but removes current X,Y,Z.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="List of channels"),
                   Parameter('p2', type="DB",
                             doc="Database")
               ]),

        Method('isValidLine_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="See if a given database line is registered for the :class:`IP` system",
               return_type=Type.INT32_T,
               return_doc="1 if the line is a valid :class:`IP` line, 0 if not",
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type=Type.STRING,
                             doc="Line name")
               ]),

        Method('iLineArrayType_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Return the type of :class:`IP` array for the input line. If necessary, first imports the specified line into the :class:`IP` object",
               return_type=Type.INT32_T,
               return_doc=":def:`IP_ARRAY`",
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type=Type.STRING,
                             doc="Line name")
               ]),

        Method('rASpacing_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Return the A-Spacing for the input line. If necessary, first imports the specified line into the :class:`IP` object.",
               return_type=Type.DOUBLE,
               return_doc="""
               The A-Spacing value. If there are multiple A-Spacings, the base or smallest value.
               				 This value could be :def_val:`rDUMMY` for some arrays (such as 3D) where no A-Spacing is explicitly defined.
               """,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Object"),
                   Parameter('p2', type="DB",
                             doc="Database"),
                   Parameter('p3', type=Type.STRING,
                             doc="Line name")
               ]),

        Method('iPLDPConvention_IP', module='geogxx', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Return the user's plot point convention for pole-dipole arrays.",
               return_type=Type.INT32_T,
               return_doc="The user's PLDP plot point convention :def:`IP_PLDP_CONV`",
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` Object")
               ]),

        Method('GetElectrodeLocationsAndMaskValues_IP', module='geogxx', version='9.0.0',
               availability=Availability.EXTENSION, 
               doc="Get unique electrodes, along with current mask info.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc='Line name ("" for all selected lines)'),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Electrode type. 0:Tx, 1:Rx"),
                   Parameter('p5', type="VV",
                             doc="X locations"),
                   Parameter('p6', type="VV",
                             doc="Y locations"),
                   Parameter('p7', type="VV",
                             doc='Off-time QC channel values ("QC")'),
                   Parameter('p8', type="VV",
                             doc='On-time QC channel values ("QC_RES")')
               ]),

        Method('SetElectrodeMaskValues_IP', module='geogxx', version='9.0.0',
               availability=Availability.EXTENSION, 
               doc="Set unique electrodes, along with current mask info.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc='Line name ("" for all selected lines)'),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Electrode type. 0:Tx, 1:Rx"),
                   Parameter('p5', type="VV",
                             doc="X locations"),
                   Parameter('p6', type="VV",
                             doc="Y locations"),
                   Parameter('p7', type="VV",
                             doc='Off-time QC channel values ("QC")'),
                   Parameter('p8', type="VV",
                             doc='On-time QC channel values ("QC_RES")')
               ])
    ],
    'Obsolete': [

        Method('AverageDuplicates_IP', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Average duplicate samples in a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object"),
                   Parameter('p2', type="DB",
                             doc="Database to export from"),
                   Parameter('p3', type=Type.STRING,
                             doc="Mask or reference channel"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`IP_DUPLICATE`")
               ]),

        Method('ExportUBCIP_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Export an :class:`IP` OBS file to use in the UBC IPINV2D programme.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Output :class:`IP` channel name"),
                   Parameter('p5', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('p6', type=Type.STRING,
                             doc="Output TOPO file name")
               ]),

        Method('ExportUBCIP2_IP', module='geogxx', version='6.4.2',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Same as :func:`ExportUBCIP_IP`, with error channel output.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Output :class:`IP` channel name"),
                   Parameter('p5', type=Type.STRING,
                             doc='Output error channel name ("" for none)'),
                   Parameter('p6', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('p7', type=Type.STRING,
                             doc="Output TOPO file name")
               ]),

        Method('ExportUBCRes_IP', module='geogxx', version='6.4.0',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Export a RES OBS file to use in the UBC DCINV2D programme.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Output voltage channel name"),
                   Parameter('p5', type=Type.STRING,
                             doc="Output current channel name"),
                   Parameter('p6', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('p7', type=Type.STRING,
                             doc="Output TOPO file name")
               ]),

        Method('ExportUBCRes2_IP', module='geogxx', version='6.4.2',
               availability=Availability.EXTENSION, is_obsolete=True, 
               doc="Same as :func:`ExportUBCRes_IP`, with error channel output.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`IP` object."),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` object"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output line name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Output voltage channel name"),
                   Parameter('p5', type=Type.STRING,
                             doc="Output current channel name"),
                   Parameter('p6', type=Type.STRING,
                             doc='Output error channel name ("" for none)'),
                   Parameter('p7', type=Type.STRING,
                             doc="Output OBS file name"),
                   Parameter('p8', type=Type.STRING,
                             doc="Output TOPO file name")
               ])
    ]
}

