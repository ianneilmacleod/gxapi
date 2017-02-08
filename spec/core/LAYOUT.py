from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('LAYOUT',
                 doc="""
Layout class for generic relative layout calculation

The relative layout algorithm allows a logical organization of layout rectangles.
You can set constraints with English-like semantics. For example:

"Set the left side of rectangle 1 equal to the right side of rectangle 2 plus 10 pixels."
"Set the bottom of rectangle 1 to 25 percent of the height of rectangle 2."
"Move node 1 such that its bottom is equal to the top of rectangle 2 minus 10 pixels."

The last constraint set would enjoy priority over any others as it would be
the last one that would influence the rectangle calculations. See the notes for iSetConstraint
for more details.
""")


gx_defines = [
    Define('LAYOUT_CONSTR',
           doc="Layout constraint specifiers",
           constants=[
               Constant('LAYOUT_CONSTR_LEFT', value='0', type=Type.INT32_T,
                        doc="adjust rectangle's left side")                        ,
               Constant('LAYOUT_CONSTR_RIGHT', value='1', type=Type.INT32_T,
                        doc="adjust rectangle's right side")                        ,
               Constant('LAYOUT_CONSTR_TOP', value='2', type=Type.INT32_T,
                        doc="adjust rectangle's top side")                        ,
               Constant('LAYOUT_CONSTR_BOTTOM', value='3', type=Type.INT32_T,
                        doc="adjust rectangle's bottom side")                        ,
               Constant('LAYOUT_CONSTR_WIDTH', value='4', type=Type.INT32_T,
                        doc="adjust rectangle's width")                        ,
               Constant('LAYOUT_CONSTR_HEIGHT', value='5', type=Type.INT32_T,
                        doc="adjust rectangle's height")                        ,
               Constant('LAYOUT_CONSTR_HCENTER', value='6', type=Type.INT32_T,
                        doc="center rectangle with respect to width")                        ,
               Constant('LAYOUT_CONSTR_VCENTER', value='7', type=Type.INT32_T,
                        doc="center rectangle with respect to height")                        ,
               Constant('LAYOUT_CONSTR_MOVEL', value='8', type=Type.INT32_T,
                        doc="move rectangle, with respect to left")                        ,
               Constant('LAYOUT_CONSTR_MOVER', value='9', type=Type.INT32_T,
                        doc="move rectangle, with respect to right")                        ,
               Constant('LAYOUT_CONSTR_MOVET', value='10', type=Type.INT32_T,
                        doc="move rectangle, with respect to top")                        ,
               Constant('LAYOUT_CONSTR_MOVEB', value='11', type=Type.INT32_T,
                        doc="move rectangle, with respect to bottom")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('CalculateRects_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Calculate new positions based on initial conditions and constraints",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LAYOUT",
                             doc=":class:`LAYOUT` Object"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Parent Rectangle Min X after calculation"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Parent Rectangle Min Y after calculation"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Parent Rectangle Max X after calculation"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Parent Rectangle Max Y after calculation")
               ]),

        Method('ClearAll_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Remove all children and constraints from layout",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LAYOUT",
                             doc=":class:`LAYOUT` Object")
               ]),

        Method('ClearConstraints_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Remove all constraints from layout",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LAYOUT",
                             doc=":class:`LAYOUT` Object")
               ]),

        Method('Create_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Creates a layout calculation object",
               return_type="LAYOUT",
               return_doc=":class:`LAYOUT` object.",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="Initial number of objects (may be 0)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Optional name of parent layout (may be empty)")
               ]),

        Method('Destroy_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Destroys the layout calculation object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LAYOUT",
                             doc=":class:`LAYOUT` object")
               ]),

        Method('GetRectangle_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Gets the current bounds for a rectangle or the parent layout",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LAYOUT",
                             doc=":class:`LAYOUT` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Rectangle to get info for (-1 for parent)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Rectangle Min X"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Rectangle Min Y"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Rectangle Max X"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Rectangle Max Y")
               ]),

        Method('GetRectName_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Gets an optional name the current info for a rectangle or the parent layout",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LAYOUT",
                             doc=":class:`LAYOUT` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Rectangle to get info for (-1 for parent)"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Buffer for name of the rectangle"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the Buffer")
               ]),

        Method('iAddConstraint_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Add a constraint between any two rectangles or to one with absolute positioning",
               return_type=Type.INT32_T,
               return_doc="""
               0 - OK
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type="LAYOUT",
                             doc=":class:`LAYOUT` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="From rectangle (Or -1 for parent)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`LAYOUT_CONSTR` From constraint flag"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="To rectangle (Or -1 for parent Or -2 for absolute positioning)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`LAYOUT_CONSTR` To constraint flag"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Offset modifier"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Multiplicative modifier")
               ]),

        Method('iAddRectangle_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Adds a rectangle as one of the layout's children (Higer.",
               return_type=Type.INT32_T,
               return_doc="Rectangle number, -1 on error",
               parameters = [
                   Parameter('p1', type="LAYOUT",
                             doc=":class:`LAYOUT` Object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Rectangle Min X   (All 0's for undefined allowed)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Rectangle Min Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Rectangle Max X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Rectangle Max Y")
               ]),

        Method('iNumRectangles_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Returns the number of children in the list.",
               return_type=Type.INT32_T,
               return_doc="Number of rectangles not counting the parent",
               parameters = [
                   Parameter('p1', type="LAYOUT",
                             doc=":class:`LAYOUT` Object")
               ]),

        Method('SetRectangle_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Sets the current bounds for a rectangle previously added to the layout",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LAYOUT",
                             doc=":class:`LAYOUT` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Rectangle to set info for (-1 for parent)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Rectangle Min X"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Rectangle Min Y"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Rectangle Max X"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Rectangle Max Y")
               ]),

        Method('SetRectangleName_LAYOUT', module='geoengine.map', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Sets an optional name the current info for a rectangle or the parent layout",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="LAYOUT",
                             doc=":class:`LAYOUT` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Rectangle to set info for (-1 for parent)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name")
               ])
    ]
}

