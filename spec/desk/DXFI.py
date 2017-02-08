from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DXFI',
                 doc="The :class:`DXFI` class is used for importing AutoCAD® dxf files into Geosoft maps.")





gx_methods = {
    'Miscellaneous': [

        Method('Create_DXFI', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create :class:`DXFI`.",
               return_type="DXFI",
               return_doc=":class:`DXFI` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="DXF file name")
               ]),

        Method('Destroy_DXFI', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`DXFI` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DXFI",
                             doc=":class:`DXFI` Handle")
               ]),

        Method('DXF2PLY_DXFI', module='geogxx', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Convert a DXF file to a :class:`PLY` object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PLY",
                             doc=":class:`PLY` handle"),
                   Parameter('p2', type="DXFI",
                             doc=":class:`DXFI` handle")
               ]),

        Method('DXF2ViewEx_DXFI', module='geogxx', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Draw entities in a DXF file to a view in a map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DXFI"),
                   Parameter('p2', type="MVIEW"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="User defined number of pens to use (can be :def_val:`iDUMMY`)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="TRUE to place entire DXF in one group"),
                   Parameter('p5', type=Type.STRING,
                             doc='group name for one group (can be "" if above is FALSE)'),
                   Parameter('p6', type=Type.INT32_T,
                             doc="TRUE to force one colour"),
                   Parameter('p7', type=Type.INT32_T,
                             doc=":def:`MVIEW_COLOR` (ignored if above is FALSE)")
               ]),

        Method('GetRange_DXFI', module='geogxx', version='6.2.0',
               availability=Availability.PUBLIC, 
               doc="Get DXF data range",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DXFI",
                             doc=":class:`DXFI` handle"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X min"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X max"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y min"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y max"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Z min"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Z max")
               ])
    ],
    'Obsolete': [

        Method('DXF2Map_DXFI', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Draw entities in a DXF file in a map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc="Map handle"),
                   Parameter('p2', type="DXFI",
                             doc=":class:`DXFI` handle"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="User defined map scale"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="unit conversion factor"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X origin of the map"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Y origin of the map"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="User defined number of pens to use"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Force black color if 1")
               ]),

        Method('DXF2MapEx_DXFI', module='geogxx', version='5.0.6',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Draw entities in a DXF file in a map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DXFI",
                             doc=":class:`DXFI` handle"),
                   Parameter('p2', type="MAP",
                             doc="Map handle"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="User defined map scale"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="unit conversion factor"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X origin of the map"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Y origin of the map"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="User defined number of pens to use"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="TRUE to place entire DXF in one group"),
                   Parameter('p9', type=Type.STRING,
                             doc="group name for one group"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="TRUE to force one colour"),
                   Parameter('p11', type=Type.INT32_T,
                             doc=":def:`MVIEW_COLOR`")
               ]),

        Method('DXF2View_DXFI', module='geogxx', version='5.0.6',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Draw entities in a DXF file to a view in a map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DXFI"),
                   Parameter('p2', type="MVIEW"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="User defined map scale"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="unit conversion factor"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X origin of the map"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Y origin of the map"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="User defined number of pens to use"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="TRUE to place entire DXF in one group"),
                   Parameter('p9', type=Type.STRING,
                             doc="group name for one group"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="TRUE to force one colour"),
                   Parameter('p11', type=Type.INT32_T,
                             doc=":def:`MVIEW_COLOR`")
               ]),

        Method('MapExtents_DXFI', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Get map extent",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DXFI",
                             doc=":class:`DXFI` handle"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Min X - returned"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Min Y - returned"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Max X - returned"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Max Y - returned")
               ]),

        Method('SetIPJ_DXFI', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Set the projection of the DXF.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DXFI",
                             doc="View"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` to place in the view")
               ])
    ]
}

