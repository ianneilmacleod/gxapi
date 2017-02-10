from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('VOXD',
                 doc=":class:`VOX` Display object.")





gx_methods = {
    'Miscellaneous': [

        Method('Create_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Create a new :class:`VOXD`",
               notes="""
               Fails if the :class:`VOX` object is NOT thematic.
               (See the :func:`CreateThematic_VOXD` function.)
               """,
               return_type="VOXD",
               return_doc=":class:`VOXD` handle, terminates if creation fails",
               parameters = [
                   Parameter('p1', type="VOX",
                             doc=":class:`VOX` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc='colour table name, "" for default'),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`ITR_ZONE`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="colour contour interval or :def_val:`rDUMMY`")
               ]),

        Method('CreateITR_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Create a new :class:`VOXD` with our own :class:`ITR`",
               notes="""
               Fails if the :class:`VOX` object is thematic.
               (See the :func:`CreateThematic_VOXD` function.)
               """,
               return_type="VOXD",
               return_doc=":class:`VOXD` handle, terminates if creation fails",
               parameters = [
                   Parameter('p1', type="VOX",
                             doc=":class:`VOX` Object"),
                   Parameter('p2', type="ITR",
                             doc=":class:`ITR` Object")
               ]),

        Method('CreateThematic_VOXD', module='geoengine.map', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a new :class:`VOXD` for a thematic :class:`VOX` object.",
               notes="""
               A thematic voxel is one where the stored integer values
               represent indices into an internally stored :class:`TPAT` object.
               Thematic voxels contain their own color definitions, and
               normal numerical operations, such as applying ITRs for display,
               are not valid.
               
               To determine if a :class:`VOX` object is thematic, use the
               :func:`iIsThematic_VOX` function.
               
               Fails if the :class:`VOX` object is NOT thematic.
               """,
               return_type="VOXD",
               return_doc=":class:`VOXD` handle, terminates if creation fails",
               parameters = [
                   Parameter('p1', type="VOX",
                             doc=":class:`VOX` Object")
               ]),

        Method('Destroy_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`VOXD`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOXD",
                             doc=":class:`VOXD` to destroy.")
               ]),

        Method('GetDrawControls_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the draw controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Draw Bounding Box"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Transparency"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Min X"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Min Y"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Min Z"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Max X"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Max Y"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Max Z")
               ]),

        Method('IGetName_VOXD', module='geoengine.map', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Gets the file name of the voxel.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOXD",
                             doc=":class:`VOXD` handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="file name returned"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="file name string size")
               ]),

        Method('GetITR_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`ITR` of the :class:`VOXD`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('p2', type="ITR",
                             doc=":class:`ITR` object")
               ]),

        Method('GetShellControls_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get the shell controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Min Value (:def_val:`rDUMMY` for no limit)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Max Value (:def_val:`rDUMMY` for no limit)")
               ]),

        Method('SetDrawControls_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Set the draw controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Draw Bounding Box"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Transparency"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Min Z"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Max Y"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Max Z")
               ]),

        Method('SetITR_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Set the :class:`ITR` of the :class:`VOXD`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('p2', type="ITR",
                             doc=":class:`ITR` object")
               ]),

        Method('SetShellControls_VOXD', module='geoengine.map', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Set the shell controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="VOXD",
                             doc=":class:`VOXD` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Min Value (:def_val:`rDUMMY` for no limit)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Max Value (:def_val:`rDUMMY` for no limit)")
               ])
    ]
}

