from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('ARCSYS',
                 doc="""
This library is not a class. It contains various general
system utilities used by the Geosoft extensions for ArcGIS.
""")





gx_methods = {
    'Miscellaneous': [

        Method('IGetBrowseLoc_ARCSYS', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the current catalog browser location in ArcGIS",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='1',
                             doc="Path String"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of path string")
               ]),

        Method('IGetCurrentDoc_ARCSYS', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the current Mx Document file name",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='1',
                             doc="Path String"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of path string")
               ]),

        Method('SetBrowseLoc_ARCSYS', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the current catalog browser location in ArcGIS",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Path String")
               ])
    ]
}

