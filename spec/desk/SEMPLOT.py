from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('SEMPLOT',
                 doc="Oasis montaj implementation of RTE :class:`SEMPLOT`",
                 verbatim_gxh_defines="#define ImportAscWizard_SEMPLOT(A,B,C) IImportAsciiWizard_SEMPLOT(A, B, C, sizeof(C))")


gx_defines = [
    Define('SEMPLOT_GROUP_CLASS',
           is_constant=True,
           is_single_constant=True,
           doc=":class:`SEMPLOT` group class.",
           constants=[
               Constant('SEMPLOT_GROUP_CLASS', value='Semplot', type=Type.STRING)                        
           ]),

    Define('SEMPLOT_EXPORT',
           doc=":class:`SEMPLOT` export type selection.",
           constants=[
               Constant('SEMPLOT_EXPORT_NORMAL', value='0', type=Type.INT32_T,
                        doc="Exports Sample info channels, oxides/ratios, totals, extra channels.")                        ,
               Constant('SEMPLOT_EXPORT_NOEXTRA', value='1', type=Type.INT32_T,
                        doc="Exports Sample info, oxides/ratios, totals.")                        
           ]),

    Define('SEMPLOT_EXT',
           doc=":class:`SEMPLOT` file extension selection",
           constants=[
               Constant('SEMPLOT_EXT_ALL', value='0', type=Type.INT32_T,
                        doc="""
                        Use for selection only. Selects both "Semplot" and ":class:`CHIMERA`" type
                        files when creating LSTs etc.
                        """)                        ,
               Constant('SEMPLOT_EXT_SEMPLOT', value='1', type=Type.INT32_T,
                        doc="""
                        Read/write templates with extensions ".xyt", ".tri" and ".semtemplate"
                        Read/write overlays with extensions ".oly" and ".semoverlay"
                        """)                        ,
               Constant('SEMPLOT_EXT_CHIMERA', value='2', type=Type.INT32_T,
                        doc="""
                        Read/write templates with extensions ".geosoft_template"
                        Read/write overlays with extensions ".geosoft_overlay"
                        """)                        
           ]),

    Define('SEMPLOT_PLOT',
           doc=":class:`SEMPLOT` plot type selection.",
           constants=[
               Constant('SEMPLOT_PLOT_ALL', value='0', type=Type.INT32_T,
                        doc="""
                        Use for selection only. Selects both "XYPlot" and "TriPlot"
                        plots when creating LSTs etc.
                        """)                        ,
               Constant('SEMPLOT_PLOT_XYPLOT', value='1', type=Type.INT32_T,
                        doc="Select XY (Scatter) plot.")                        ,
               Constant('SEMPLOT_PLOT_TRIPLOT', value='2', type=Type.INT32_T,
                        doc="Select Tri (Triangular) plot.")                        ,
               Constant('SEMPLOT_PLOT_UNKNOWN', value='3', type=Type.INT32_T,
                        doc="Returned as an error status from some functions.")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('ApplyFilterToMask_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Apply the filter to the mask channel",
               notes="""
               The mask channel is updated for the current data to reflect
               the actions of the filter. Those values passing get 1, those
               failing get 0.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Filter name"),
                   Parameter('p3', type=Type.STRING,
                             doc="Mask channel name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Mineral channel name"),
                   Parameter('p5', type=Type.STRING,
                             doc='Mineral to use ("All" or "" for all)'),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Mask mode (0: Append, 1: New)")
               ]),

        Method('ConvertDummies_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Convert dummies to zero values for assay channels.",
               notes="""
               The is operation is controlled by the Preferences
               "Use dummies to indicate no data?" By default, this option is "yes"
               so this function will return with no changes. However, if
               "no", then all ASSAY class channels will have dummy values
               converted to 0.0.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database handle"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Input line to convert")
               ]),

        Method('CreateGroups_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Group data by anomaly or string channel - Interactive.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Mask channel")
               ]),

        Method('DefaultGroups_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Group data by selected anomalies.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle")
               ]),

        Method('EditMapPlotParameters_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Alter parameters in an XYplot Triplot map.",
               notes="""
               The Parameters :class:`GUI` is loaded based on settings stored in
               the map. The map is then re-plotted, overwriting the old one,
               based on the new settings. Note that the selection of data
               in the current :class:`DB` is used to replot the map.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc='Mask channel (can be "")'),
                   Parameter('p3', type=Type.STRING,
                             doc='Mineral channel (can be "" for raw data)'),
                   Parameter('p4', type="MAP",
                             doc="Map handle"),
                   Parameter('p5', type=Type.STRING,
                             doc="Map View")
               ]),

        Method('EditPlotComponents_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Set group names and channels to plot in a template.",
               notes="""
               The "Components" group in the INI file is edited.
               
               Looks first in user\\etc, then in \\etc.
               Looks first for file prefix "semtemplate" then "xyt" or "tri"
               The altered template will be output to the user\\etc directory with
               the file extension "semtemplate".
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Template name")
               ]),

        Method('EditPlotParameters_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Set TriPlot parameters in a template.",
               notes="""
               The "Parameters" group in the INI file is edited.
               
               Looks first in user\\etc, then in \\etc.
               Looks first for file prefix "semtemplate" then "xyt" or "tri"
               The altered template will be output to the user\\etc directory with
               the file extension "semtemplate".
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Template name")
               ]),

        Method('ExportOverlay_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Create overlay map and file from a group.",
               notes="""
               The group is written to a new map, and an overlay file
               is created which points to this map.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="overlay file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="associated map"),
                   Parameter('p3', type="MVIEW",
                             doc="View with group"),
                   Parameter('p4', type=Type.STRING,
                             doc="group name"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`SEMPLOT_PLOT`"),
                   Parameter('p6', type=Type.STRING,
                             doc="XStage"),
                   Parameter('p7', type=Type.STRING,
                             doc="XOxide"),
                   Parameter('p8', type=Type.STRING,
                             doc="YStage"),
                   Parameter('p9', type=Type.STRING,
                             doc="YOxide"),
                   Parameter('p10', type=Type.STRING,
                             doc="ZStage"),
                   Parameter('p11', type=Type.STRING,
                             doc="ZOxide"),
                   Parameter('p12', type=Type.INT32_T,
                             doc=":def:`SEMPLOT_EXT`")
               ]),

        Method('ExportView_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc='Create a "View" database',
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Original raw data database"),
                   Parameter('p2', type="LST",
                             doc="List of lines (anomlies) to export"),
                   Parameter('p3', type="DB",
                             doc="Destination database"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="View to export - One of SEMPLOT_XXX_STAGE"),
                   Parameter('p5', type=Type.STRING,
                             doc='Mask channel ("" for None)'),
                   Parameter('p6', type=Type.STRING,
                             doc="Mineral channel"),
                   Parameter('p7', type=Type.STRING,
                             doc='Mineral to export ("" for all)')
               ]),

        Method('ExportView2_SEMPLOT', module='geoguilib', version='7.1.0',
               availability=Availability.EXTENSION, 
               doc='Create a "View" database, with channel selection',
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Original raw data database"),
                   Parameter('p2', type="LST",
                             doc="List of lines (anomlies) to export"),
                   Parameter('p3', type="DB",
                             doc="Destination database"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="View to export - One of SEMPLOT_XXX_STAGE"),
                   Parameter('p5', type=Type.STRING,
                             doc='Mask channel ("" for None)'),
                   Parameter('p6', type=Type.STRING,
                             doc="Mineral channel"),
                   Parameter('p7', type=Type.STRING,
                             doc='Mineral to export ("" for all)'),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`SEMPLOT_EXPORT` Channel selection")
               ]),

        Method('FilterLST_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Fill a :class:`LST` with existing :class:`SEMPLOT` filters",
               notes="""
               "Supplied" filters are stored in \\etc, while user-edited and new filters
               are stored in user\\etc. This function finds all files with the extension
               ".semfilter", first in user\\etc, then in \\etc, and adds the file names
               (without the extension) to the :class:`LST`. The name with the extension is stored
               as the value.
               The :class:`LST` is cleared first.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` to fill.")
               ]),

        Method('FilterMineralPosData_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Filter raw data by position and mineral values",
               notes="""
               The Mask channel will be updated so that those data values
               which "pass" get "1" and those that "fail" get dummy "*"
               NO DATA IS REMOVED.
               Works on all selected lines of data.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Mask channel"),
                   Parameter('p3', type=Type.STRING,
                             doc="Mineral channel"),
                   Parameter('p4', type=Type.STRING,
                             doc='mineral (string) - "C", "I" etc.'),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Grain position")
               ]),

        Method('GetAssociatedLST_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Get the associated channels for this group in a :class:`LST`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Data Group handle"),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` to copy channels into")
               ]),

        Method('GetCurrentMineralLST_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Retrieve :class:`LST` of minerals in selected lines.",
               notes="""
               If the mineral channel name is not specified, it returns
               just the "X" (Unknown) item.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Mineral channel name"),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('GetCurrentPositionLST_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Retrieve :class:`LST` of positions in selected lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('GetFullMineralLST_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Retrieve :class:`LST` of all minerals in Semplot_Minerals.csv",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('GetFullPositionLST_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Retrieve :class:`LST` of all possible mineral positions.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc=":class:`LST` object")
               ]),

        Method('GetGroupingLST_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Get list of items to group symbols by.",
               notes="""
               The first item is "Anomaly", which gives the line names, The second
               item (if the channel exists in the database) is the Sample Number.
               After this are included all string channels which are NOT oxides or
               elements. (The list can include the mineral).
               Channel symbol is the :class:`LST` value (except for the first item - "Anomaly")
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database handle"),
                   Parameter('p2', type="LST",
                             doc="list to hold items")
               ]),

        Method('iCreateASCIITemplate_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc=": Generate ASCII import template automatically",
               return_type=Type.INT32_T,
               return_doc="""
               1 if it succeeds in creating a Template.
               0 if it fails.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make")
               ]),

        Method('iCreateDatabaseTemplate_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Generate database import template automatically",
               return_type=Type.INT32_T,
               return_doc="""
               1 if it succeeds in creating a Template.
               0 if it fails.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make")
               ]),

        Method('iEditFilter_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Edit and create filter on channel values",
               return_type=Type.INT32_T,
               return_doc="""
               -1 - Cancel - Edits to filter discarded.
               
                0 - Normal Return. Edits saved to filter file.
               
                1 - Apply filter to current data only
               
                2 - Remove filter - If removing filtered data, just
                    restore the data to the Min/Pos data
                    otherwise set the mask channel to 1.
               
               Re-entry code. If not :def_val:`iDUMMY`, what to do inside the filter after
               going back in. Returned on exit, used on next input.
               
                0 - Nothing. Don't need to go back into this function again.
                1 - Edit the filter.
               
               Notes            New and edited filters are stored in user\\etc in files with
                the file extension ".semfilter"
                If a file for the specified filter does not exist, then a
                new filter by that name will be created.
               """,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of filter"),
                   Parameter('p3', type=Type.STRING,
                             doc="Mask channel name"),
                   Parameter('p4', type=Type.STRING,
                             doc="Mineral channel name"),
                   Parameter('p5', type=Type.STRING,
                             doc="Mineral to restrict filter to.")
               ]),

        Method('IGetMineralChannelName_SEMPLOT', module='geoguilib', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="Retrieve the mineral channel name.",
               notes="""
               First looks at the :class:`SEMPLOT`.MINERAL_CHANNEL value.
               If not found, returns the first MINERAL class
               channel found. If still not found, returns a
               blank string.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Mineral channel name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="Size of the Buffer")
               ]),

        Method('IImportAsciiWizard_SEMPLOT', module='geoguilib', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="Generate a :class:`SEMPLOT` ASCII import template.",
               notes="""
               If the anomaly name is not included, then
               the input data must have an "Anom_Name" field.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc='anomaly name (can be "")'),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DB_SYMBOL',
                             doc="buffer size")
               ]),

        Method('IImportDatabaseODBC_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Generate a template file for importing ODBC databases.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="connection string (input and returned)"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="connection string buffer size"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="template file (returned)"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="templage file buffer size")
               ]),

        Method('ImportBIN_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Import blocked binary or archive ASCII data",
               notes="""
               This wrapper is for :class:`SEMPLOT`, and does not require the import licence.
               
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
               see_also=":func:`LabTemplate_DU` in du.gxh",
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

        Method('ImportDatabaseADO_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Generate a template file for importing semplot databases.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make")
               ]),

        Method('InitGroupSymbolsUsed_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Initializes memory of symbols used in plotting.",
               notes="""
               Maintains a list of the symbols used in plotting. Call before
               Plotting one or more legends - symbols are accumulated.
               :func:`PlotSymbolLegend_SEMPLOT` uses this information to create a legend.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database handle")
               ]),

        Method('iTemplateType_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Create a new XYPlot or TriPlot template.",
               return_type=Type.INT32_T,
               return_doc="""
               :def_val:`SEMPLOT_PLOT_XYPLOT` or
               :def_val:`SEMPLOT_PLOT_TRIPLOT`
               Terminates if error.
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Template name")
               ]),

        Method('iViewType_SEMPLOT', module='geoguilib', version='6.4.2',
               availability=Availability.EXTENSION, 
               doc="Test to see if a view is an XYPlot or Triplot view.",
               notes="""
               First checks the view name to see if it starts with
               "XYplt_" or "Triplt_". Failing that it looks in the
               view :class:`REG` for a value for "Components.Type", which will
               be either "XYPlot" or "TriPlot".
               If the view does not appear to be an XYPlot or a TriPlot view,
               the function returns :def_val:`SEMPLOT_PLOT_UNKNOWN`.
               """,
               return_type=Type.INT32_T,
               return_doc=":def:`SEMPLOT_PLOT`",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc="Input map object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Input view name")
               ]),

        Method('MineralID_SEMPLOT', module='geoguilib', version='6.3.0',
               availability=Availability.EXTENSION, 
               doc="Identify minerals from the oxide channels.",
               notes="""
               Finds the best mineral matching the composition for each
               row of oxide values. Works using linear programming and
               the simplex method to maximize the oxides used to create
               each of the possible output minerals. The mineral leaving the
               least leftover is selected, as long as the residual (measured
               as a percent of the total) is less than or equal to the
               input value.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Maximum residual value (in % of the total oxide)"),
                   Parameter('p3', type="DB_SYMB",
                             doc="Mineral channel (Locked RW)"),
                   Parameter('p4', type="DB_SYMB",
                             doc="Residual channel (Locked RW)")
               ]),

        Method('NewFilter_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Create a new selection filter.",
               notes="Creates a new, empty filter file in the user\\etc directory",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="New filter name"),
                   Parameter('p2', type=Type.STRING,
                             doc='Filter to use as a model (can be "")')
               ]),

        Method('NewTemplate_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Create a new XYPlot or TriPlot template.",
               notes="""
               The new template is written to the user\\etc directory, with
               the file extension "semfilter". The template contains a parameter
               identifying it as an XY or Triplot.
               
               Model Template: Looks first in user\\etc, then in \\etc.
               Looks first for file prefix "semtemplate" then "xyt" or "tri"
               
               Because there are so many shared parameters, it is possible to use
               an XYPlot template as a model for a TriPlot, and vica-verca, with
               few complications.  (e.g. needing to define a "Z" component)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="New template name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Unknown"),
                   Parameter('p3', type=Type.STRING,
                             doc='Template to use as a model (can be "")')
               ]),

        Method('OverlayLST_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Fill a list with the available plot overlay names",
               notes="""
               Looks first in user\\etc, then in \\etc.
               See :def:`SEMPLOT_EXT` definitions above for which files to look for.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="Input :class:`LST`."),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`SEMPLOT_EXT`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`SEMPLOT_PLOT`")
               ]),

        Method('Plot_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Plot an XYPlot or TriPlot based on the template.",
               notes="""
               The "Components" and "Parameters" groups in the INI file
               are used.
               Only values with mask values of 1 are plotted, if the mask
               channel is specified.
               
               Call ":func:`ResetUsedChannel_SEMPLOT`" prior to this function
               in order to track the values actually plotted.
               
               Call :func:`InitGroupSymbolsUsed_SEMPLOT` prior to this function
               to reset recording of the symbols used in plotting (for legends etc).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Template file name"),
                   Parameter('p3', type=Type.STRING,
                             doc='Mask channel (can be "")'),
                   Parameter('p4', type=Type.STRING,
                             doc='Mineral channel (can be "" for raw data)'),
                   Parameter('p5', type=Type.STRING,
                             doc="Map name"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Map open mode; one of MAP_WRITEXXX (see map.gxh)"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Plot symbols (O: No, 1:Yes) ?")
               ]),

        Method('PlotSymbolLegend_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Plot a symbol legend in a view.",
               notes="""
               This function depends on :func:`InitGroupSymbolsUsed_SEMPLOT`
               before the plot for which this legend is created is made.
               The symbols and groups to use in the legend are stored to
               a database blob after the plot is made. These values are
               recovered by this function to make the legend at the
               specified location.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type="MVIEW",
                             doc="View to plot into"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X Minimum"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y Minimum"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y Maximum"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Symbol size")
               ]),

        Method('PropSymb_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Plot a proportional symbol plot.",
               notes="Replots map using proportional symbols",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type="MAP",
                             doc="Map to plot to"),
                   Parameter('p3', type=Type.STRING,
                             doc="View to replot"),
                   Parameter('p4', type=Type.STRING,
                             doc="channel name"),
                   Parameter('p5', type=Type.STRING,
                             doc='mask channel (can be "")'),
                   Parameter('p6', type=Type.STRING,
                             doc="mineral channel ("),
                   Parameter('p7', type=Type.INT32_T,
                             doc="linear (0) or logarithmic (1) scaling"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="scale by diameter (0) or area (1)"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="scale base (log) data units"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="scale factor (log) data units/mm"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="symbol number"),
                   Parameter('p12', type=Type.INT32_T,
                             doc="symbol weight"),
                   Parameter('p13', type=Type.INT32_T,
                             doc="symbol line color"),
                   Parameter('p14', type=Type.INT32_T,
                             doc="symbol fill color"),
                   Parameter('p15', type=Type.INT32_T,
                             doc="plot legend?")
               ]),

        Method('Replot_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Replot an existing :class:`SEMPLOT` plot based on current data.",
               notes="""
               Note that the selection of data
               in the current :class:`DB` is used to replot the map.
               
               Call ":func:`ResetUsedChannel_SEMPLOT`" prior to this function
               in order to track the values actually plotted.
               
               Call :func:`InitGroupSymbolsUsed_SEMPLOT` prior to this function
               to reset recording of the symbols used in plotting (for legends etc).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc='Mask channel (can be "")'),
                   Parameter('p3', type=Type.STRING,
                             doc='Mineral channel (can be "" for raw data)'),
                   Parameter('p4', type="MAP",
                             doc="Map handle"),
                   Parameter('p5', type=Type.STRING,
                             doc="Map View containing the plot")
               ]),

        Method('RePlotSymbolLegend_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Replot a symbol legend in a view.",
               notes="""
               Searches the VIEW :class:`REG` for information on a previously
               created legend, and if it finds that info, replots the Legend,
               using the current data, group key etc.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type="MVIEW",
                             doc="View to plot into")
               ]),

        Method('ResetGroups_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Re-group data using current settings.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Mask channel")
               ]),

        Method('ResetUsedChannel_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc='Set the "Plotted" channel to dummies',
               notes="""
               This function is called before one or a series of plots to initialize
               the "Plotted" channel in all the selected lines to dummy values.
               As the plots are created, those points used in the plot are set to 1,
               so that at the end the database records which values have been plotted.
               This information can then be used to make a symbol legend.
               If the "Plotted" channel does not exist, it is created, associated,
               loaded, and filled with dummies.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database handle")
               ]),

        Method('SelectPoly_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Select data from a polygonal area on a map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type="MVIEW",
                             doc="View Handle"),
                   Parameter('p3', type=Type.STRING,
                             doc="Mask channel to update"),
                   Parameter('p4', type=Type.STRING,
                             doc="Mineral channel"),
                   Parameter('p5', type="PLY",
                             doc="Polygon to select from, in the view coordinates."),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Mask mode (0: Append, 1: New)")
               ]),

        Method('SetChannelOrder_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Sets preset channel order.",
               notes="""
               Sets channel order as follows:
               
               Sample_No
               X and Y Locations
               Mineral
               Grain_No
               Position (e.g. center, edge etc.)
               Grain Morph
               Oxides (in the order they appear in Semplot_Oxides.csv)
               Trace Elements (Ordered as in the periodic table)
               Total
               Mask
               IsPlotted (flag set when a value is plotted)
               Other channels
               
               Channel order is set for all "RawData" groups.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database handle"),
                   Parameter('p2', type="LST",
                             doc="channel names, handles")
               ]),

        Method('SetChannelUnits_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Set units for oxides (%) and elements (ppm)",
               notes="""
               If the channel units are already set, then they are not changed.
               Oxide channels are identified from the Semplot_Oxides.csv file.
               Trace elements are identified from the periodic table of the
               elements, except for "Y", if it is the current Y channel.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database handle")
               ]),

        Method('SetITR_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Put :class:`ITR` into a channel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Data channel handle"),
                   Parameter('p3', type="ITR")
               ]),

        Method('SetMask_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Set the mask channel ON or OFF.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Mask channel"),
                   Parameter('p3', type=Type.STRING,
                             doc="Mineral channel"),
                   Parameter('p4', type=Type.STRING,
                             doc='Mineral to use ("All" or "" for all)'),
                   Parameter('p5', type=Type.INT32_T,
                             doc="0 for all lines, 1 for selected lines"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="0 for off, 1 for on.")
               ]),

        Method('SortData_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Sort data by Sample No, Grain and Position",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database handle"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Data Group handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Use Anomaly channel as primary sort?")
               ]),

        Method('TemplateLST_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Fill a list with the available plot template names",
               notes="""
               Looks first in user\\etc, then in \\etc.
               Looks first for file prefix "semtemplate" then "xyt" or "tri"
               (New-style templates with the "semtemplate" extentsion have the
               plot type "triplot" or "xyplot" inside them.)
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LST",
                             doc="Input :class:`LST`."),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`SEMPLOT_PLOT`")
               ]),

        Method('TileWindows_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Tile currently maximimized windows.",
               return_type=Type.VOID),

        Method('TotalOxides_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, 
               doc="Calculate the total oxides channel.",
               notes="""
               The mineral channel is needed in order to adjust the total
               with the Fe Corrected Ferric and Ferrous values, and these
               require a mineral for their identification. If none is provided,
               mineral "X" (unknown) is assumed.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DB",
                             doc="database handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Mineral channel")
               ])
    ],
    'Obsolete': [

        Method('ImportAsciiWizard_SEMPLOT', module='geoguilib', version='6.2.0',
               availability=Availability.EXTENSION, is_obsolete=True, no_gxh=True, 
               doc="Generate a :class:`SEMPLOT` ASCII import template.",
               notes="""
               The new :func:`IImportAsciiWizard_SEMPLOT` returns
               the specified anomaly name if no anomaly
               name channel is in the database.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="data file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="template to make")
               ])
    ]
}

