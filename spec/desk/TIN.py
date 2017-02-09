from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('TIN',
                 doc="""
                 The :class:`TIN` class calculates the Delaunay triangulation of the
                 positions in a database. This is the "best" set of triangles
                 that can be formed from irregularly distributed points. The
                 serialized :class:`TIN` files can be used for gridding using the
                 Tin-based Nearest Neighbour Algorithm, or for plotting the
                 Delaunay triangles or Voronoi cells to a map.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Copy_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Copy :class:`TIN`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc="destination :class:`TIN`"),
                   Parameter('p2', type="TIN",
                             doc="source :class:`TIN`")
               ]),

        Method('Create_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="This method creates a :class:`TIN` object.",
               notes="""
               CreateTIN does the :class:`TIN` calculation.
               The Z values are not required, and a 0-length :class:`VV` can be used to indicate
               the values are not to be used.
               """,
               return_type="TIN",
               return_doc=":class:`TIN` Object",
               parameters = [
                   Parameter('p1', type="VV",
                             doc="X positions"),
                   Parameter('p2', type="VV",
                             doc="Y positions"),
                   Parameter('p3', type="VV",
                             doc="Z values (optional)")
               ]),

        Method('CreateS_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create :class:`TIN` from a serialized source",
               return_type="TIN",
               return_doc=":class:`TIN` Object",
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` from which to read :class:`TIN`")
               ]),

        Method('Destroy_TIN', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys the :class:`TIN` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` Handle")
               ]),

        Method('ExportXML_TIN', module='geogxx', version='6.0.1',
               availability=Availability.LICENSED, 
               doc="Export a :class:`TIN` object as XML",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`TIN` file"),
                   Parameter('p2', type="var CRC", is_ref=True,
                             doc="CRC returned (Currently this is not implemented)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output XML file")
               ]),

        Method('GetConvexHull_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get the convex hull of the :class:`TIN`.",
               notes="""
               The convex hull is the outside boundary of the
               triangulated region.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type="PLY",
                             doc=":class:`PLY` object")
               ]),

        Method('GetIPJ_TIN', module='geogxx', version='5.0.3',
               availability=Availability.LICENSED, 
               doc="Get the projection.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` in which to place the :class:`TIN` projection")
               ]),

        Method('GetJoins_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get joins from a :class:`TIN` mesh.",
               notes="""
               The join information is returned in three VVs.
               - The joins :class:`VV` is a list off the adjacent nodes for
                 each node, arranged for 1st node, 2nd node etc.
               - The index :class:`VV` gives the starting index in the
                 joins :class:`VV` for the adjacent nodes to each node.
               - The number :class:`VV` gives the number of adjacent nodes
                 for each node.
               All VVs must be type :def_val:`GS_LONG`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type="VV",
                             doc="Joins :class:`VV` (adjacent nodes)"),
                   Parameter('p3', type="VV",
                             doc="Index :class:`VV`"),
                   Parameter('p4', type="VV",
                             doc="Number :class:`VV`")
               ]),

        Method('GetMesh_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get lines from a :class:`TIN` mesh.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` of type GS_D2LINE (returned)")
               ]),

        Method('GetNodes_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get the X,Y locations and Z values of the :class:`TIN` nodes.",
               notes="""
               If this is not a Z-valued :class:`TIN`, the Z values will
               be dummies.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Y :class:`VV`"),
                   Parameter('p4', type="VV",
                             doc="Z :class:`VV`")
               ]),

        Method('GetTriangles_TIN', module='geogxx', version='8.4.0',
               availability=Availability.LICENSED, 
               doc="Get the triangle nodes.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type="VV",
                             doc="Node 1 :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Node 2 :class:`VV`"),
                   Parameter('p4', type="VV",
                             doc="Node3 :class:`VV`")
               ]),

        Method('GetTriangle_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get the locations of the vertices of a specific triangle",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="triangle index [0...N-1]"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="X0"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Y0"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="X1"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Y1"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="X2"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Y2")
               ]),

        Method('GetVoronoiEdges_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get line segments defining Voronoi cells.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` of GS_D2LINE type (create with type -32)")
               ]),

        Method('iIsZValued_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Does the :class:`TIN` contain Z values with each X,Y?",
               return_type=Type.INT32_T,
               return_doc="Returns :def_val:`GS_TRUE` if Z values are defined in the :class:`TIN`",
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object")
               ]),

        Method('iLocateTriangle_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get the index of the triangle containing X, Y.",
               notes="""
               Index returned begins at 0, but could be negative.
               -1 If X,Y is not contained in a triangle (or triangle not found)
               -2 If the location is on an edge
                  This is for "fall-back" purposes only.
               	Frequently edge positions are located as being part of
                  a triangle, so do not rely on this result to determine
                  if a node position is on an edge.
               -3 If the location is a vertex.
                  This is for "fall-back" purposes only in the code.
                  Normal operation is to include a node position
                  inside a triangle, so do not rely on this result to determine
                  if a node position is input.
               """,
               return_type=Type.INT32_T,
               return_doc="The index of the triangle containing X, Y.",
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="seed triangle (can be iDummy or <0)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="target X location"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="target Y location")
               ]),

        Method('iNodes_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Returns the number of nodes in the :class:`TIN`",
               return_type=Type.INT32_T,
               return_doc="The number of nodes in the :class:`TIN`",
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object")
               ]),

        Method('InterpVV_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Interp TINned values using the natural neighbour method.",
               notes="""
               The :class:`TIN` have been created using max length = :def_val:`rDUMMY` to
               ensure that the :class:`TIN` has a convex hull (otherwise the
               routine that locates the triangle for a given location may fail).
               The :class:`TIN` must also have been created using the Z values.
               Values located outside the convex hull are set to :def_val:`rDUMMY`.
               The method is based on the following paper:
               
               Sambridge, M., Braun, J., and McQueen, H., 1995,
               Geophysical parameterization and interpolation of irregular
               data using natural neighbours:
               Geophysical Journal International, 122 p. 837-857.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` X locations to interpolate (:def_val:`GS_DOUBLE`)"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` Y locations to interpolate (:def_val:`GS_DOUBLE`)"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` Interpolated Z values (:def_val:`GS_DOUBLE`)")
               ]),

        Method('iTriangles_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Returns the number of triangles in the :class:`TIN`.",
               return_type=Type.INT32_T,
               return_doc="The number of triangles in the :class:`TIN`",
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object")
               ]),

        Method('LinearInterpVV_TIN', module='geogxx', version='5.1.4',
               availability=Availability.LICENSED, 
               doc="Interp TINned values using the linear interpolation",
               notes="""
               The :class:`TIN` have been created using max length = :def_val:`rDUMMY` to
               ensure that the :class:`TIN` has a convex hull (otherwise the
               routine that locates the triangle for a given location may fail).
               The :class:`TIN` must also have been created using the Z values.
               Values located outside the convex hull are set to :def_val:`rDUMMY`.
               
               The values are set assuming that each :class:`TIN` triangle defines a
               plane.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` X locations to interpolate (:def_val:`GS_DOUBLE`)"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` Y locations to interpolate (:def_val:`GS_DOUBLE`)"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` Interpolated Z values (:def_val:`GS_DOUBLE`)")
               ]),

        Method('NearestVV_TIN', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Interp TINned values using the nearest neighbour.",
               notes="""
               The :class:`TIN` have been created using max length = :def_val:`rDUMMY` to
               ensure that the :class:`TIN` has a convex hull (otherwise the
               routine that locates the triangle for a given location may fail).
               The :class:`TIN` must also have been created using the Z values.
               Values located outside the convex hull are set to :def_val:`rDUMMY`.
               
               Within each voronoi triangle, the Z value of node closest to the input
               X,Y location is returned.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` X locations to interpolate (:def_val:`GS_DOUBLE`)"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` Y locations to interpolate (:def_val:`GS_DOUBLE`)"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` Interpolated Z values (:def_val:`GS_DOUBLE`)")
               ]),

        Method('RangeXY_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Find the range in X and Y of the TINned region.",
               notes="""
               The TINned range is the range of X and Y covered by
               the :class:`TIN` triangles. It can thus be less than the full
               X and Y range of the nodes themselves, if a full
               convex hull is not calculated.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Min X  (returned)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Min Y"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Max X"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Max Y")
               ]),

        Method('Serial_TIN', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Serialize :class:`TIN`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN"),
                   Parameter('p2', type="BF",
                             doc=":class:`BF` in which to write :class:`TIN`")
               ]),

        Method('SetIPJ_TIN', module='geogxx', version='5.0.3',
               availability=Availability.LICENSED, 
               doc="Set the projection.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TIN",
                             doc=":class:`TIN` object"),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` to place in the :class:`TIN`")
               ])
    ]
}

