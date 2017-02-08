from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DATAMINE',
                 doc="""
:class:`DATAMINE` functions provide an interface to Datamine Software Limited files.
See also :class:`GIS` for various other Datamine-specific functions.
""",
                 notes="None.")


gx_defines = [
    Define('GIS_DMTYPE',
           doc="Datamine file types",
           constants=[
               Constant('GIS_DMTYPE_STRING', value='2', type=Type.INT32_T)                        ,
               Constant('GIS_DMTYPE_WIREFRAME_TR', value='8', type=Type.INT32_T)                        ,
               Constant('GIS_DMTYPE_DTM', value='16', type=Type.INT32_T)                        ,
               Constant('GIS_DMTYPE_BLOCKMODEL', value='32', type=Type.INT32_T)                        ,
               Constant('GIS_DMTYPE_WIREFRAME_PT', value='64', type=Type.INT32_T)                        ,
               Constant('GIS_DMTYPE_POINTDATA', value='1024', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('CreateVoxel_DATAMINE', module='geoengine.interoperability', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Create a Geosoft Voxel file from a Datamine block model file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Datamine file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Field to use for data"),
                   Parameter('p3', type="IPJ",
                             doc="Projection to set"),
                   Parameter('p4', type="META",
                             doc=":class:`META` to set"),
                   Parameter('p5', type=Type.STRING,
                             doc="Output voxel file name")
               ]),

        Method('NumericFieldLST_DATAMINE', module='geoengine.interoperability', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Return a :class:`LST` containing the non-standard numeric fields in a Datamine file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Datamine file name"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to populate")
               ])
    ]
}

