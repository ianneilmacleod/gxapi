from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('ARCDH',
                 doc="""
                 This library is not a class. It contains various utilities
                 used in the Target extension for ArcGIS.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('CloseProject_ARCDH', module='geoarcgis', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Closes the current :class:`DH` project in the Target extension",
               return_type=Type.VOID),

        Method('SetProject_ARCDH', module='geoarcgis', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Sets the current :class:`DH` project in the Target extension",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Path String"),
                   Parameter('p2', type=Type.STRING,
                             doc="Project Name")
               ]),

        Method('SetStringFileGDB_ARCDH', module='geoarcgis', version='8.0.0',
               availability=Availability.EXTENSION, 
               doc="Sets the current Geostring File Geodatabase in the Target extension",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Geodatabase")
               ]),

        Method('StopEditingStringFileGDB_ARCDH', module='geoarcgis', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="Stops editing session for current string fGDB",
               return_type=Type.VOID),

        Method('iHasStringFileGDBEdits_ARCDH', module='geoarcgis', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="Is a Geostring File Geodatabase loaded and contain edits?",
               return_type=Type.INT32_T),

        Method('iGeostringsExtensionAvailable_ARCDH', module='geoarcgis', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="Verifies if the geostrings extension in TfA is available. Return 1 if true, 0 otherwise",
               return_type=Type.INT32_T),

        Method('GetCurrentStringFileGDB_ARCDH', module='geoarcgis', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="Gets the current Geostring File Geodatabase.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="name returned"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_FILE',
                             doc="string size")
               ]),

        Method('iIsValidFGDBFileName_ARCDH', module='geoarcgis', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="Is this a valid FGDB filename?",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="FGDB filename")
               ]),

        Method('iIsValidFeatureClassName_ARCDH', module='geoarcgis', version='8.0.1',
               availability=Availability.EXTENSION, 
               doc="Is this a valid featureclass name?",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="featureclass name")
               ]),

        Method('sPromptForESRISymbol_ARCDH', module='geoarcgis', version='8.2.0',
               availability=Availability.EXTENSION, no_gxh=True, 
               doc="Prompt the user to select an ESRI symbol and return it as an XML string. The output string will be empty if the user cancels the dialog.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HWND", is_val=True,
                             doc="Window handle"),
                   Parameter('p2', type=Type.STRING,
                             doc='Initial symbol that you want displayed when the dialog is launched (use "" if none)'),
                   Parameter('p3', type=Type.INT32_T,
                             doc="(This parameter is ignored if an initial symbol was specified) Initial symbol type that you want displayed when the dialog is launched (0 for Fill, 1 for Line)"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="Returned XML string representing the symbol that was chosen by the user"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Length of output XML string"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="RGBA representation of fill color to be set"),
                   Parameter('p7', type=Type.INT32_T, is_ref=True,
                             doc="RGBA representation of edge color to be set")
               ])
    ]
}

