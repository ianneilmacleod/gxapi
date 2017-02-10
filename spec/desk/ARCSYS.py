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
               notes="""
               Gets the "local" directory (current catalog browser location in ArcGIS if map has not been saved,
               otherwise MxD path). We cannot mess with the CWD in ArcGIS because there MxD settings for
               relative/absolute paths depends on it.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="Path String"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of path string")
               ]),

        Method('IGetCurrentDoc_ARCSYS', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the current Mx Document file name",
               notes="If the current document is not yet saved, this will return an empty string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING, is_ref=True, size_of_param='p2',
                             doc="Path String"),
                   Parameter('p2', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Size of path string")
               ]),

        Method('SetBrowseLoc_ARCSYS', module='geoarcgis', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the current catalog browser location in ArcGIS",
               notes="""
               Will also set the current working directory (CWD) if the MxD has not been saved.
               We cannot mess with the CWD in ArcGIS because their MxD settings for relative/absolute paths depends on it.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Path String")
               ])
    ]
}

