from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('SURFACE',
                 doc="""
The :class:`SURFACE` class allows you to create, read and alter Geosurface files (*.geosoft_surface).
A Geosurface file can contain one or more surface items (see :class:`SURFACEITEM` class). In turn each item can
contains one or more triangular polyhedral meshes.
""")


gx_defines = [
    Define('SURFACE_OPEN',
           doc="Open Modes",
           constants=[
               Constant('SURFACE_OPEN_READ', value='0', type=Type.INT32_T)                        ,
               Constant('SURFACE_OPEN_READWRITE', value='1', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Create a new Geosurface file",
               return_type="SURFACE",
               return_doc=":class:`SURFACE` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Geosurface file name"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` containing coordinate system of the Geosurface")
               ]),

        Method('Open_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Open a Geosurface file",
               return_type="SURFACE",
               return_doc=":class:`SURFACE` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Geosurface file name"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`SURFACE_OPEN`")
               ]),

        Method('Destroy_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`SURFACE` Object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACE",
                             doc=":class:`SURFACE` Object")
               ]),

        Method('GetIPJ_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the coordinate system of the :class:`SURFACE`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACE",
                             doc=":class:`SURFACE` Object"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` in which to place the Geosurface coordinate system")
               ]),

        Method('SetIPJ_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Change the coordinate system of the :class:`SURFACE`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACE",
                             doc=":class:`SURFACE` Object"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` containing the new coordinate system of the Geosurface")
               ]),

        Method('GetSurfaceItems_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the surfaces items in a Geosurface file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACE",
                             doc=":class:`SURFACE` Object"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetSurfaceItem_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the an existing surface item from the :class:`SURFACE`",
               return_type="SURFACEITEM",
               return_doc=":class:`SURFACEITEM` Object",
               parameters = [
                   Parameter('p1', type="SURFACE",
                             doc=":class:`SURFACE` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Item GUID")
               ]),

        Method('AddSurfaceItem_SURFACE', module='geoengine.core', version='8.4.0',
               availability=Availability.PUBLIC, 
               doc="Add a new surface item to the :class:`SURFACE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACE",
                             doc=":class:`SURFACE` Object"),
                   Parameter('p2', type="SURFACEITEM",
                             doc=":class:`SURFACEITEM` to add")
               ]),

        Method('GetSurfaceNames_SURFACE', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the surface item names in a Geosurface file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Geosurface file"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to fill")
               ]),

        Method('GetClosedSurfaceNames_SURFACE', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the names of closed surface items in a Geosurface file (may return an empty list)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Geosurface file"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` to fill (may return an empty :class:`LST` if none of the surfaces are closed)")
               ]),

        Method('GetExtents_SURFACE', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the spatial range of all surface items.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SURFACE",
                             doc=":class:`SURFACE` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in X."),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in Y."),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum valid data in Z."),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in X."),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in Y."),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum valid data in Z.")
               ]),

        Method('CRC_SURFACE', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Compute an XML CRC of a Geosurface file.",
               return_type="CRC",
               return_doc="CRC Value (always 0)",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Geosurface file"),
                   Parameter('p2', type=Type.STRING,
                             doc="output file"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="CRC (unused, always set to 0)")
               ]),

        Method('Sync_SURFACE', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Syncronize the Metadata for this Geosurface",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Geosurface file")
               ]),

        Method('CreateFromDXF_SURFACE', module='geoengine.core', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Create Geosurface file from DXF file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IPJ"),
                   Parameter('p2', type=Type.STRING,
                             doc="Geosurface file"),
                   Parameter('p3', type=Type.STRING,
                             doc="dxf file")
               ]),

        Method('CreateFromVulcanTriangulation_SURFACE', module='geoengine.interoperability', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Create Geosurface file from a Maptek Vulcan triangulation file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="00t file"),
                   Parameter('p2', type="IPJ"),
                   Parameter('p3', type=Type.STRING,
                             doc="Geosurface file")
               ]),

        Method('AppendVulcanTriangulation_SURFACE', module='geoengine.interoperability', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Create new surface from a Maptek Vulcan triangulation file and add to an existing geosurface.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="00t file"),
                   Parameter('p2', type="IPJ"),
                   Parameter('p3', type=Type.STRING,
                             doc="Geosurface file")
               ])
    ]
}

