from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('TEST',
                 doc="Used to place special testing methods")





gx_methods = {
    'Miscellaneous': [

        Method('EnableDisableArcEngineLicense_TEST', module='geogxx', version='6.4.2',
               availability=Availability.PUBLIC, 
               doc="Forcefully disable ArEngine license availability for testing purposes",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Enable/disable? :def:`GEO_BOOL`")
               ]),

        Method('iArcEngineLicense_TEST', module='geogxx', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Test availability of an ArEngine license on this system",
               return_type=Type.INT32_T,
               return_doc="0 - Not available, 1 - Available"),

        Method('iTestMode_TEST', module='geogxx', version='6.4.2',
               availability=Availability.PUBLIC, 
               doc="Checks to see if we are running inside testing system",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`"),

        Method('WrapperTest_TEST', module='geogxx', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="Test to make sure all wrappers are valid linking",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="List of functions to test"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output log file")
               ]),

        Method('CoreClass_TEST', module='geogxx', version='9.2.0',
               availability=Availability.PUBLIC, 
               doc="Generic Class Test Wrapper",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of class to test"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output log file")
               ])
    ]
}

