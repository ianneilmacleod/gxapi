from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VULCAN',
                 doc="The :class:`VULCAN` class is used for importing Maptek® Vulcan block and triangulation files.")


gx_defines = [
    Define('BLOCK_MODEL_VARIABLE_TYPE',
           doc="Which variables to return from sReadBlockModelVariableInfo",
           constants=[
               Constant('BLOCK_MODEL_NUMERIC_VARIABLE', value='1', type=Type.INT32_T,
                        doc="Return numeric variable names")                        ,
               Constant('BLOCK_MODEL_STRING_VARIABLE', value='2', type=Type.INT32_T,
                        doc="Return string variable names")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('IsValidTriangulationFile_VULCAN', module='geoengine.interoperability', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Check if the given file can be opened as a Vulcan triangulation file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Triangulation file")
               ]),

        Method('IsValidBlockModelFile_VULCAN', module='geoengine.interoperability', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Check if the given file can be opened as a Vulcan block model file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Block model file")
               ]),

        Method('TriangulationToView_VULCAN', module='geoengine.interoperability', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Draw triangle edges in a Vulcan triangulation file to a 3D view in a map.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Triangulation file"),
                   Parameter('p2', type="IPJ",
                             doc="Triangulation projection"),
                   Parameter('p3', type="MVIEW",
                             doc="Destination :class:`MVIEW`"),
                   Parameter('p4', type=Type.STRING,
                             doc="New group name")
               ]),

        Method('GetBlockModelVariableInfo_VULCAN', module='geoengine.interoperability', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Query a block model for the variable names and descriptions.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Block model file"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`BLOCK_MODEL_VARIABLE_TYPE` Which variables to return."),
                   Parameter('p3', type="LST",
                             doc="List used to return variable names/descriptions.")
               ]),

        Method('GetBlockModelStringVariableValues_VULCAN', module='geoengine.interoperability', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Query a block model for the values a string variable can assume.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Block model file"),
                   Parameter('p2', type=Type.STRING,
                             doc="Variable name"),
                   Parameter('p3', type="LST",
                             doc="List used to return variable names")
               ]),

        Method('BlockModelToVoxel_VULCAN', module='geoengine.interoperability', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Create a Geosoft voxel file from a Vulcan block model file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Block model file"),
                   Parameter('p2', type="IPJ",
                             doc="Block model projection"),
                   Parameter('p3', type=Type.STRING,
                             doc="Variable to import"),
                   Parameter('p4', type=Type.STRING,
                             doc="Ouput voxel filename"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Remove default values from input? :def:`GEO_BOOL`"),
                   Parameter('p6', type=Type.STRING,
                             doc="Rock code file for string variable imports. Optional, unused for numeric variable imports.")
               ])
    ]
}

