from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('CSYMB',
                 doc="""
                 This class is used for generating and modifying colored symbol objects.
                 Symbol fills are assigned colors based on their Z values and a zone, Aggregate
                 or :class:`ITR` file which defines what colors are associated with different ranges
                 of Z values. The position of a symbol is defined by its X,Y coordinates.
                 """)


gx_defines = [
    Define('CSYMB_COLOR',
           doc="Color Symbol filling defines",
           constants=[
               Constant('CSYMB_COLOR_EDGE', value='0', type=Type.INT32_T,
                        doc="Draw Edges only")                        ,
               Constant('CSYMB_COLOR_FILL', value='1', type=Type.INT32_T,
                        doc="Fill Symbols")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('_SetAngle_CSYMB', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the symbol angle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="CSYMB",
                             doc=":class:`CSYMB` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Symbol angle")
               ]),

        Method('_SetBase_CSYMB', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set base value to subtract from Z values.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="CSYMB",
                             doc=":class:`CSYMB` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Symbol Base")
               ]),

        Method('_SetDynamicCol_CSYMB', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Associate symbol edge or fill colors with Z data
               and color transform.
               """,
               notes="""
               Use this method after a call to :func:`SetStaticCol_CSYMB`. This method
               reestablishes the symbol color association with their Z data
               values and color transform.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="CSYMB",
                             doc=":class:`CSYMB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`CSYMB_COLOR`")
               ]),

        Method('_SetFixed_CSYMB', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set symbol sizing to fixed (or proportionate)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="CSYMB",
                             doc=":class:`CSYMB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="TRUE  = Fixed symbol sizing FALSE = Proportionate sizing")
               ]),

        Method('_SetNumber_CSYMB', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the symbol number.",
               notes="""
               The lower 16 bits of the number is interpreted as UTF-16 with a valid Unicode character
               code point. GFN fonts wil produce valid symbols depending on the font for 0x01-0x7f and the degree,
               plus-minus and diameter symbol(latin small letter o with stroke) for 0xB0, 0xB1 and 0xF8 respectively.
               
               It is possible to check if a character is valid using :func:`iIsValidUTF16Char_UNC`. The high 16-bits are reserved
               for future use. Also see: :func:`iValidSymbol_UNC` and :func:`ValidateSymbols_UNC`
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="CSYMB",
                             doc=":class:`CSYMB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Symbol number (0x1-0x1ffff)")
               ]),

        Method('_SetScale_CSYMB', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the symbol scale.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="CSYMB",
                             doc=":class:`CSYMB` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Symbol scale (> 0.0)")
               ]),

        Method('AddData_CSYMB', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add x,y,z data to a color symbol object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="CSYMB",
                             doc=":class:`CSYMB` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` for X data"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` for Y data"),
                   Parameter('p4', type="VV",
                             doc=":class:`VV` for Z data")
               ]),

        Method('Create_CSYMB', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`CSYMB`.",
               return_type="CSYMB",
               return_doc=":class:`CSYMB` handle",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="ZON, :class:`AGG`, or :class:`ITR` file name")
               ]),

        Method('Destroy_CSYMB', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`CSYMB`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="CSYMB",
                             doc=":class:`CSYMB` to destroy")
               ]),

        Method('SetFont_CSYMB', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the symbol font name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="CSYMB",
                             doc=":class:`CSYMB` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Font name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Geosoft font? (TRUE or FALSE)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`MVIEW_FONT_WEIGHT`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Italics? (TRUE or FALSE)")
               ]),

        Method('SetStaticCol_CSYMB', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a static color for the symbol edge or fill.",
               notes="""
               Use this method to set a STATIC color for symbol edge or fill.
               By default, both edge and fill colors vary according to their
               Z data values and a color transform.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="CSYMB",
                             doc=":class:`CSYMB` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Color value"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`CSYMB_COLOR`")
               ])
    ]
}

