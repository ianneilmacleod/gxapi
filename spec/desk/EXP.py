from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('EXP',
                 doc="""
                 :class:`EXP` objects are created from text strings that contain
                 C-like math to be applied to channels in a database.
                 It is used with the :func:`Math_DU` function (see :class:`DU`). See also
                 :class:`IEXP` for applying math expressions to images (grids).
                 See also :func:`Math_DU` applies expressions to the database
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Create_EXP', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="This method creates an :class:`EXP` object.",
               notes="""
               Expressions are strings that contain C-like math to be
               applied to channels in a database.  For example, following
               an expression:
               
                  "@a = mag-64000; @b = gravity*100;
                   $sRatio = @a/@b;
                   MULT = @a *@b;"
               
               Rules:
               
                  ;  - terminates a sub-expression
                  @  - prefix to a temporary name, which is a double precision
                       floating point number to be used later in the same
                       expression.
                  $  - prefix to a local GX variable name.  Such names will be
                       evaluated to the variable value at the time :func:`Create_EXP`
                       is called.
               
                  All other tokens are assumed to be channel names.
               """,
               return_type="EXP",
               return_doc=":class:`EXP` Object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Expression using channel names"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Maximum size of expression after expanding all local variables (those with $ prefix).")
               ]),

        Method('CreateFile_EXP', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="This method creates an :class:`EXP` object from a file",
               return_type="EXP",
               return_doc=":class:`EXP` Object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File name")
               ]),

        Method('Destroy_EXP', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a :class:`EXP` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="EXP",
                             doc="Destroy a :class:`EXP` object")
               ])
    ]
}

