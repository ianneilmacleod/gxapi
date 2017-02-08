from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('EUL3',
                 doc="""
This is a specialized class which performs 3D Euler deconvolution
for potential field interpretation.
""")


gx_defines = [
    Define('EUL3_RESULT',
           doc="Euler result types",
           constants=[
               Constant('EUL3_RESULT_X', value='1', type=Type.INT32_T)                        ,
               Constant('EUL3_RESULT_Y', value='2', type=Type.INT32_T)                        ,
               Constant('EUL3_RESULT_DEPTH', value='3', type=Type.INT32_T)                        ,
               Constant('EUL3_RESULT_BACKGROUND', value='4', type=Type.INT32_T)                        ,
               Constant('EUL3_RESULT_DEPTHERROR', value='5', type=Type.INT32_T)                        ,
               Constant('EUL3_RESULT_LOCATIONERROR', value='6', type=Type.INT32_T)                        ,
               Constant('EUL3_RESULT_WINDOWX', value='7', type=Type.INT32_T)                        ,
               Constant('EUL3_RESULT_WINDOWY', value='8', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('_Destr_EUL3', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Destroys a :class:`EUL3` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EUL3",
                             doc=":class:`EUL3` object")
               ]),

        Method('Creat_EUL3', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Creates an :class:`EUL3` object.",
               return_type="EUL3",
               return_doc=":class:`EUL3` Object",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Image of grid T"),
                   Parameter('p2', type="IMG",
                             doc="Image of grid Tx"),
                   Parameter('p3', type="IMG",
                             doc="Image of grid Ty"),
                   Parameter('p4', type="IMG",
                             doc="Image of grid Tz"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Window size (maximum 20)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Geometric index, from 0.0 to 3.0"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Max tolerance to allow (percentage)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Max dist. acceptable (0 for infinite)"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="ObsFlg  Height (0) or Elevation (1)"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Height of observation plane"),
                   Parameter('p11', type=Type.DOUBLE,
                             doc="Elevation of observation plane")
               ]),

        Method('GetResult_EUL3', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Get a result field :class:`VV` from :class:`EUL3` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EUL3",
                             doc=":class:`EUL3` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` to store the result"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`EUL3_RESULT`")
               ]),

        Method('Write_EUL3', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Write the results of :class:`EUL3` object to output file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EUL3",
                             doc=":class:`EUL3` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output File Name")
               ]),

        Method('ExEulerDerive_EUL3', module='geogxx', version='9.0.0',
               availability=Availability.EXTENSION, 
               doc="Calculates gradients",
               return_type=Type.INT32_T,
               return_doc="0 for OK, -1 for Error",
               parameters = [
                   Parameter('p1', type="VV",
                             doc="Input distance"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Sample Interval"),
                   Parameter('p3', type="VV",
                             doc="Input mag"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="SampleCount"),
                   Parameter('p5', type="VV",
                             doc="Horizontal Gradient out"),
                   Parameter('p6', type="VV",
                             doc="Vertical Gradient out"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Output array size limit")
               ]),

        Method('ExEulerCalc_EUL3', module='geogxx', version='9.0.0',
               availability=Availability.EXTENSION, 
               doc="Does the exeuler depth calculations",
               return_type=Type.INT32_T,
               return_doc=">0 for OK, -1 for Error",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Solution type flag (0 for contacts, 1 for dykes)"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Structural index value (used only when generating dykes)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Window length"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Field strength in nT"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Inclination"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Declination"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Profile azimuth wrt north"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Minimum depth for returned solutions"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Maximum depth for returned solutions"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Percentage error allowed before rejection"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="Number of points in profile"),
                   Parameter('p12', type="VV",
                             doc="Array of point distances along profile"),
                   Parameter('p13', type="VV",
                             doc="Array of observed values"),
                   Parameter('p14', type="VV",
                             doc="Array of horizontal derivative values. Can be NULL for calculated"),
                   Parameter('p15', type="VV",
                             doc="Array of vertical derivative values. Can be NULL for calculated"),
                   Parameter('p16', type=Type.INT32_T,
                             doc="Length of solutions arrays passed in"),
                   Parameter('p17', type="VV",
                             doc="The profile distance for each solution"),
                   Parameter('p18', type="VV",
                             doc="The depth for each solution"),
                   Parameter('p19', type="VV",
                             doc="The dip for each solution"),
                   Parameter('p20', type="VV",
                             doc="The susceptibility for each solution")
               ])
    ]
}

