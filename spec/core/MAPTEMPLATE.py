from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MAPTEMPLATE',
                 doc="""
                 A :class:`MAPTEMPLATE` wraps and provides manipulation and usage for the XML content in map template files.
                 See the annotated schema file maptemplate.xsd in the <:class:`GEOSOFT`>\\maptemplate folder and the accompanying
                 documentation in that folder for documentation on the file format.
                 """)


gx_defines = [
    Define('MAPTEMPLATE_OPEN',
           doc="Open Modes",
           constants=[
               Constant('MAPTEMPLATE_WRITENEW', value='0', type=Type.INT32_T,
                        doc="Create new empty map template (will overwrite existing files)")                        ,
               Constant('MAPTEMPLATE_EXIST', value='1', type=Type.INT32_T,
                        doc="Create from existing template on disk")                        
           ])]


gx_methods = {
    'Content Manipulation Methods': [

        Method('GetTmpCopy_MAPTEMPLATE', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Get a temporary XML file for manipulation of the map template.",
               notes="""
               After manipulating contents the object may be updated by a call to
               the UpdateFromTmpCopy method.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPTEMPLATE"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="returned temporary map template file name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of file name string")
               ]),

        Method('UpdateFromTmpCopy_MAPTEMPLATE', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Update the object contents from a temporary XML file that may have bee manipulated externally.",
               notes="""
               This method will not modify the original contents of the file until a call to the
               the Commit method is made or the object is destroyed. A call to the Discard method
               will restore the contents to that of the original file. The temporary file is not deleted
               and should be to not leak file resources.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPTEMPLATE"),
                   Parameter('p2', type=Type.STRING,
                             doc="Temporary map template file name")
               ])
    ],
    'File Methods': [

        Method('Commit_MAPTEMPLATE', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Commit any changes to the map template to disk",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPTEMPLATE")
               ]),

        Method('Create_MAPTEMPLATE', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`MAPTEMPLATE` from an existing file.",
               notes="""
               The base template name should be the file name part of a geosoft_maptemplate
               file in the <geosoft>\\maptemplate or <geosoftuser>\\maptemplate folders. A base file
               in the user folder will override any in the Geosoft install dir.
               """,
               return_type="MAPTEMPLATE",
               return_doc=":class:`MAPTEMPLATE` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Map Template file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Map Template base template to create from"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MAPTEMPLATE_OPEN`")
               ]),

        Method('Destroy_MAPTEMPLATE', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`MAPTEMPLATE` handle.",
               notes="All changes to the :class:`MAPTEMPLATE` will be committed if it is not read-only.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPTEMPLATE",
                             doc=":class:`MAPTEMPLATE` Handle")
               ]),

        Method('Discard_MAPTEMPLATE', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Discard all changes made to the map template and reload from disk.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPTEMPLATE")
               ]),

        Method('GetFileName_MAPTEMPLATE', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Get the file name of the map template.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPTEMPLATE"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="returned map template file name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of file name string")
               ])
    ],
    'Map Making': [

        Method('CreateMap_MAPTEMPLATE', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Create a map from the map template",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPTEMPLATE",
                             doc=":class:`MAPTEMPLATE` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="New map file name (if it exists it will be overwritten)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Group name to use for settings")
               ])
    ],
    'Render/Preview': [

        Method('Refresh_MAPTEMPLATE', module='geoengine.map', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Refresh the map template with any newly saved items",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPTEMPLATE",
                             doc=":class:`MAPTEMPLATE` Handle")
               ]),

        Method('RenderPreview_MAPTEMPLATE', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, no_gxh=True, 
               doc="""
               Create a preview of the map template onto a
               Windows DC handle
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPTEMPLATE",
                             doc=":class:`MAPTEMPLATE` Handle"),
                   Parameter('p2', type="HDC", is_val=True,
                             doc="DC Handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="left value of the render rect in Windows coordinates (bottom>top)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="bottom value"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="right value"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="top value")
               ]),

        Method('RenderPreviewMapProduction_MAPTEMPLATE', module='geoengine.map', version='6.4.0',
               availability=Availability.LICENSED, no_gxh=True, 
               doc="Render a preview for map sheet production purposes",
               notes="""
               This method can also be used to get the data view pixel location
               by passing a null DC handle. This help to plot the view contents
               preview from another location.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPTEMPLATE",
                             doc=":class:`MAPTEMPLATE` Handle"),
                   Parameter('p2', type="HDC", is_val=True,
                             doc="DC Handle (pass 0 to just query the Data view pixel location)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="left value of the render rect in Windows coordinates (bottom>top)"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="bottom value"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="right value"),
                   Parameter('p6', type=Type.INT32_T, is_ref=True,
                             doc="top value")
               ])
    ],
    'Miscellaneous': [

    ]
}

