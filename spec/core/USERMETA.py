from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('USERMETA',
                 doc="""
                 The :class:`USERMETA` class handles user style metadata tied to real
                 data.
                 """)


gx_defines = [
    Define('USERMETA_FORMAT',
           doc=":class:`USERMETA` Format Types",
           constants=[
               Constant('USERMETA_FORMAT_DEFAULT', value='-1', type=Type.INT32_T,
                        doc="Use the standard type for the system")                        ,
               Constant('USERMETA_FORMAT_ISO', value='0', type=Type.INT32_T,
                        doc="ISO 19139 standard")                        ,
               Constant('USERMETA_FORMAT_FGDC', value='1', type=Type.INT32_T,
                        doc="FGDC Metadata Standard")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates an empty :class:`USERMETA` object",
               return_type="USERMETA",
               return_doc=":class:`USERMETA` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc=":def:`USERMETA_FORMAT` Type of Meta to create")
               ]),

        Method('CreateS_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`USERMETA` from a file",
               return_type="USERMETA",
               return_doc=":class:`USERMETA` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('Destroy_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroyes the :class:`USERMETA` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA",
                             doc="Projection to Destroy")
               ]),

        Method('GetDataCreationDate_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Data Creation Date",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Date")
               ]),

        Method('GetExtents2d_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the 2d Extents",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="MinX"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="MinY"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="MaxX"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="MaxY")
               ]),

        Method('GetExtents3d_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the 3d Extents",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="MinX"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="MinY"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="MinZ"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="MaxX"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="MaxY"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="MaxZ")
               ]),

        Method('GetIPJ_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`IPJ`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type="IPJ",
                             doc="Date")
               ]),

        Method('GetMetaCreationDate_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Meta Creation Date",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Date")
               ]),

        Method('GetXMLFormat_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the XML Format",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc=":def:`USERMETA_FORMAT`")
               ]),

        Method('iCompare_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Compare 2 :class:`USERMETA`'s",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="USERMETA",
                             doc="First :class:`USERMETA`"),
                   Parameter('p2', type="USERMETA",
                             doc="Second UERMETA")
               ]),

        Method('IGetDataCreator_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Data Creator",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="DataCreator returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="maximum name size")
               ]),

        Method('IGetFormat_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the File Format",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="title returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="maximum name size")
               ]),

        Method('IGetMetaCreator_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Meta Creator",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="MetaCreator returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="maximum name size")
               ]),

        Method('IGetProject_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the File Project",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="title returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="maximum name size")
               ]),

        Method('IGetTitle_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Title",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="title returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="maximum name size")
               ]),

        Method('Serial_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Serialize :class:`USERMETA` to a :class:`BF`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL` Output Geosoft Metadata?"),
                   Parameter('p3', type=Type.STRING,
                             doc="File name to save to")
               ]),

        Method('SetDataCreationDate_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Data Creation Date",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Date")
               ]),

        Method('SetDataCreator_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Data Creator",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.STRING,
                             doc="DataCreator")
               ]),

        Method('SetExtents2d_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the 2d Extents",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="MinX"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="MinY"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="MaxX"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="MaxY")
               ]),

        Method('SetExtents3d_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the 3d Extents",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="MinX"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="MinY"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="MinZ"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="MaxX"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="MaxY"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="MaxZ")
               ]),

        Method('SetFormat_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the File Format",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.STRING,
                             doc="Format")
               ]),

        Method('SetIPJ_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the :class:`IPJ`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type="IPJ",
                             doc="Date")
               ]),

        Method('SetMetaCreationDate_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Meta Creation Date",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Date")
               ]),

        Method('SetMetaCreator_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Meta Creator",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.STRING,
                             doc="MetaCreator")
               ]),

        Method('SetProject_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the File Project",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.STRING,
                             doc="Project")
               ]),

        Method('SetTitle_USERMETA', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the Title",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="USERMETA"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title")
               ]),

        Method('UpdateExtents2D_USERMETA', module='geoengine.core', version='7.0.1',
               availability=Availability.PUBLIC, 
               doc="""
               Edit an existing XML metadata file by
               changing the extents and projection data
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Filename of existing metadata to update"),
                   Parameter('p2', type="IPJ",
                             doc="New projection"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="New MinX value"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="New MinY value"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="New MaxX value"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="New MaxY value")
               ]),

        Method('UpdateFileType_USERMETA', module='geoengine.core', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="""
               Edit an existing XML metadata file by
               changing the file type
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Filename of existing metadata to update"),
                   Parameter('p2', type=Type.STRING,
                             doc="New file type")
               ]),

        Method('SaveFileLineage_USERMETA', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Add lineage to XML",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Filename of existing metadata to update"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GEO_BOOL` Output Geosoft Metadata?")
               ])
    ]
}

