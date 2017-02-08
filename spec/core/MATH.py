from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MATH',
                 doc="""
This is not a class. This is a collection of standard
mathematical functions, including most of the common
logarithmic and geometric functions.
""")





gx_methods = {
    'Miscellaneous': [

        Method('CrossProduct_MATH', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Cross product of two vectors.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="X1 component"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y1 component"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Z1 component"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X2 component"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y2 component"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Z2 component"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="X3 component (output)"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="Y3 component (output)"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Z3 component (output)")
               ]),

        Method('iAbs_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate absolute value",
               return_type=Type.INT32_T,
               return_doc="integer",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="integer")
               ]),

        Method('iAnd_MATH', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="""
               Return the unary operation result of A & B
               
               Returns			an integer number
               
               If A or B is a dummy, returns dummy.
               """,
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="A"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="B")
               ]),

        Method('iMod_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculates the modulus of two integers",
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="A"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="B (must not be zero)")
               ]),

        Method('iOr_MATH', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="""
               Return the unary operation result of A | B
               
               Returns			an integer number
               
               If A or B is a dummy, returns dummy.
               """,
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="A"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="B")
               ]),

        Method('iRound_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Round to the nearest whole number",
               return_type=Type.INT32_T,
               return_doc="integer",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="round")
               ]),

        Method('iXor_MATH', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="""
               Return the unary operation result of A ^ B
               
               Returns			an integer number
               
               If A or B is a dummy, returns dummy.
               """,
               return_type=Type.INT32_T,
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="A"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="B")
               ]),

        Method('NicerLogScale_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Finds nicer min, max values for logarithmic plot scales.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE, is_ref=True,
                             doc="Min value (changed)"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Max value (changed)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Fine flag")
               ]),

        Method('NicerScale_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Compute a nicer scale for a given min and max.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE, is_ref=True,
                             doc="Min value (changed)"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Max value (changed)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Inc value (returned)"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Power value (returned)")
               ]),

        Method('Normalise3D_MATH', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Scale a vector to unit length.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE, is_ref=True,
                             doc="X component (altered)"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Y component (altered)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Z component (altered)")
               ]),

        Method('rAbs_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate absolute value",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE)
               ]),

        Method('rArcCos_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate the arccosine",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE)
               ]),

        Method('rArcSin_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate the arcsin",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE)
               ]),

        Method('rArcTan_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate the arctan",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE)
               ]),

        Method('rArcTan2_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate ArcTan(Y/X)",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Y"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X")
               ]),

        Method('rCeil_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculates the ceiling of the value",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE)
               ]),

        Method('rCos_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate the cosine",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Angle in radians")
               ]),

        Method('rDotProduct3D_MATH', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Compute Dot product of two vectors.",
               return_type=Type.DOUBLE,
               return_doc="Dot product",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="X1 component"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y1 component"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Z1 component"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X2 component"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y2 component"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Z2 component")
               ]),

        Method('rExp_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate e raised to the power of X",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="X")
               ]),

        Method('rFloor_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculates the floor of the value",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE)
               ]),

        Method('rHypot_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="sqrt(X*X + Y*Y)",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="X"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y")
               ]),

        Method('rLambdaTrans_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Performs lambda transform on a value.",
               return_type=Type.DOUBLE,
               return_doc="The lambda transformed value",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Z Value"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Lambda value")
               ]),

        Method('rLambdaTransRev_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Performs a reverse lambda transform on a value.",
               return_type=Type.DOUBLE,
               return_doc="The original non-lambda transformed value",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Lambda transformed Z Value"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Lambda value")
               ]),

        Method('rLog_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate the natural log",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE)
               ]),

        Method('rLog10_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate the base 10 log",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE)
               ]),

        Method('rLogZ_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="""
               Given a Z value and the Log style and Log Minimum this
               function will return the log value.
               """,
               return_type=Type.DOUBLE,
               return_doc="The Log Value.",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Z Value"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Log Mode (0 - Log, 1 - LogLinearLog)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Log Minimum (must be greater than 0)")
               ]),

        Method('rMod_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculates the modulus of two reals (A mod B)",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="A"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="B (must not be zero)")
               ]),

        Method('RotateVector_MATH', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Rotate a vector about an axis.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="X1 component (vector to rotate)"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y1 component"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Z1 component"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Angle to rotate, CW in radians"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="X2 component (axis of rotation)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Y2 component"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Z2 component"),
                   Parameter('p8', type=Type.DOUBLE, is_ref=True,
                             doc="X3 component  (rotated vector, can"),
                   Parameter('p9', type=Type.DOUBLE, is_ref=True,
                             doc="Y3 component   be the same as input)"),
                   Parameter('p10', type=Type.DOUBLE, is_ref=True,
                             doc="Z3 component")
               ]),

        Method('rPow_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate X raised to the power of Y",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="X"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y")
               ]),

        Method('rRand_MATH', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get a  random number between 0 and 1",
               return_type=Type.DOUBLE,
               return_doc="a real number"),

        Method('rRound_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Round to n significant digits",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE),
                   Parameter('p2', type=Type.INT32_T,
                             doc="number of significant digits to round to")
               ]),

        Method('rSign_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Determine return value based on value of Z1",
               return_type=Type.DOUBLE,
               return_doc="|Z2| if Z1>0, -|Z2| if Z1<0, 0 if Z1 = 0, and Z2 if Z1 = Dummy",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Z1"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Z2")
               ]),

        Method('rSin_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate the sin",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Angle in radians")
               ]),

        Method('rSqrt_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate the square root",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE)
               ]),

        Method('rTan_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Calculate the tangent",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Angle in radians")
               ]),

        Method('rUnLogZ_MATH', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Inverse of rLogZ",
               return_type=Type.DOUBLE,
               return_doc="The original value",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="log value"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Log Mode (0 - Log, 1 - LogLinearLog)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Log Minimum (must be greater than 0)")
               ]),

        Method('SRand_MATH', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Seed the random-number generator with current time",
               return_type=Type.VOID)
    ]
}

