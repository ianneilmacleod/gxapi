from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DMPPLY',
                 doc="Datamine Multiple polygon object")





gx_methods = {
    'Miscellaneous': [

        Method('_Clear_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Clear/remove all polygons from the :class:`DMPPLY`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY")
               ]),

        Method('Copy_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Copy",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc="destination"),
                   Parameter('p2', type="DMPPLY",
                             doc="source")
               ]),

        Method('Create_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Creates a :class:`DMPPLY` object.",
               return_type="DMPPLY",
               return_doc="DMPLY Object"),

        Method('Destroy_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys the :class:`DMPPLY` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` Object")
               ]),

        Method('GetAzimuth_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the azimuth of a given polygon.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to NP)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Azimuth (degrees) (o)")
               ]),

        Method('GetExtents_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the center, width and height of a given polygon.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to NP)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Center point X (o)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Center point Y (o)"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Center point Z (o)"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Width of polygon (in its plane) (o)"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Height of polygon (Z extent) (o)")
               ]),

        Method('GetJoins_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get join lines for each vertex in a specific polygon.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc="Datamine polygon Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to N)"),
                   Parameter('p3', type="VV",
                             doc="INT :class:`VV` of join indices (1 to NJoins).")
               ]),

        Method('GetNormalVectors_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the normal vectors of a given polygon.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to NP)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X component (o) (Horizontal azimuth vector)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y component (o)"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Z component (o)"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="X component (o) (Down-dip, in the vertical plane)"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Y component (o)"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Z component (o)"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="X component (o) (Normal vector)"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Y component (o)"),
                   Parameter('p11', type=Type.DOUBLE, is_ref=True,
                             doc="Z component (o)")
               ]),

        Method('GetPoly_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get a specific polygon from a :class:`DMPPLY` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to NP) (i)"),
                   Parameter('p3', type="VV",
                             doc="X Locations (o)"),
                   Parameter('p4', type="VV",
                             doc="Y Locations (o)"),
                   Parameter('p5', type="VV",
                             doc="Z Locations (o)")
               ]),

        Method('GetSwing_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the swing of a given polygon.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to NP)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Swing (degrees) (o)")
               ]),

        Method('GetVertex_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get a vertex location from a :class:`DMPPLY` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to NP)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="vertex number (1 to NV)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="X Location (o)"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y Location (o)"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Z Location (o)")
               ]),

        Method('iNumJoins_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the number of joining lines in a :class:`DMPPLY` object.",
               return_type=Type.INT32_T,
               return_doc="Number of joining lines",
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object")
               ]),

        Method('iNumPolys_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the number of polygons in a :class:`DMPPLY` object.",
               return_type=Type.INT32_T,
               return_doc="Number of polygons",
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object")
               ]),

        Method('iNumVertices_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Get the number of vertices in a polygon.",
               return_type=Type.INT32_T,
               return_doc="Number of vertices in a polygon",
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to NP)")
               ]),

        Method('Load_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Loads a Datamine polygon file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the file to load")
               ]),

        Method('MoveVertex_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Moves a vertex and any associated lines.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to NP)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="vertex number (1 to NV)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="new location X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="new location Y"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="new location Z")
               ]),

        Method('ProjectPoly_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Project a polygon onto a vertical plane.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to NP)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location of plane origin in 3D"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location of plane origin in 3D"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Z location of plane origin in 3D"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="azimuth of the plane in degrees"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="swing of the plane in degrees"),
                   Parameter('p8', type="VV",
                             doc="X (horizontal along-section locations on vertical plane  (o)"),
                   Parameter('p9', type="VV",
                             doc="Y (vertical locations on vertical plane  (o)"),
                   Parameter('p10', type="VV",
                             doc="Z (horizontal distances perpendicular to the plane  (o)")
               ]),

        Method('ReProjectPoly_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Recover polygon locations from 2D locations on vertical plane.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to lNP) (i)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X location of plane origin in 3D (i)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y location of plane origin in 3D (i)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Z location of plane origin in 3D (i)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="azimuth of the plane in degrees (i)"),
                   Parameter('p7', type="VV",
                             doc="X locations on vertical plane  (i)"),
                   Parameter('p8', type="VV",
                             doc="Y (actually Z) locations on vertical plane  (i)"),
                   Parameter('p9', type="VV",
                             doc="X Locations of polygon (o)"),
                   Parameter('p10', type="VV",
                             doc="Y Locations of polygon (o)"),
                   Parameter('p11', type="VV",
                             doc="Z Locations of polygon (o)")
               ]),

        Method('Save_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Save to a Datamine polygon file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of the file to save to")
               ]),

        Method('SetPoly_DMPPLY', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Set a specific polygon into a :class:`DMPPLY` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DMPPLY",
                             doc=":class:`DMPPLY` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="polygon number (1 to NP) (i)"),
                   Parameter('p3', type="VV",
                             doc="X Locations (i)"),
                   Parameter('p4', type="VV",
                             doc="Y Locations (i)"),
                   Parameter('p5', type="VV",
                             doc="Z Locations (i)")
               ])
    ]
}

