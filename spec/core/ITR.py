from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('ITR',
                 doc="""
The :class:`ITR` class provides access to :class:`ITR` files. An :class:`ITR` file maps
ranges of values to specific colours. The :class:`ITR` object is typically
used in conjunction with :class:`MVIEW` objects (see :class:`MVIEW` and :class:`MVU`).
""",
                 notes="""
Histogram ranges and colour zone ranges

Histogram bins are defined with inclusive minima and exclusive maxima;
for instance if Min = 0 and Inc = 1, then the second bin would include
all values z such that  0 <= z < 1 (the first bin has all values < 0).

Colour zones used in displaying grids (:class:`ITR`, ZON etc...) are the
opposite, with exclusive minima and inclusive maxima.
For instance, if a zone is defined from 0 to 1, then it would
contain all values of z such that 0 < z <= 1.

These definitions mean that it is impossible to perfectly assign
:class:`ITR` colours to individual bars of a histogram. The best work-around
when the data values are integers is to define the colour zones using
0.5 values between the integers. A general work-around is to make the
number of histogram bins much larger than the number of colour zones.

The :def_val:`ITR_NULL` is used to hold a NULL handle to an :class:`ITR` class.
""")


gx_defines = [
    Define('ITR_COLOR_MODEL',
           doc=":class:`ITR` Color Model defines",
           constants=[
               Constant('ITR_COLOR_MODEL_HSV', value='1', type=Type.INT32_T)                        ,
               Constant('ITR_COLOR_MODEL_RGB', value='2', type=Type.INT32_T)                        ,
               Constant('ITR_COLOR_MODEL_CMY', value='3', type=Type.INT32_T)                        
           ]),

    Define('ITR_NULL',
           is_null_handle=True,
           doc="Null :class:`ITR` Object"),

    Define('ITR_POWER',
           doc="Power Zoning defines",
           constants=[
               Constant('ITR_POWER_10', value='0', type=Type.INT32_T,
                        doc="Power of 10")                        ,
               Constant('ITR_POWER_EXP', value='1', type=Type.INT32_T,
                        doc="Exponential")                        
           ]),

    Define('ITR_ZONE',
           doc="Zoning Methods",
           constants=[
               Constant('ITR_ZONE_DEFAULT', value='0', type=Type.INT32_T)                        ,
               Constant('ITR_ZONE_LINEAR', value='1', type=Type.INT32_T)                        ,
               Constant('ITR_ZONE_NORMAL', value='2', type=Type.INT32_T)                        ,
               Constant('ITR_ZONE_EQUALAREA', value='3', type=Type.INT32_T)                        ,
               Constant('ITR_ZONE_SHADE', value='4', type=Type.INT32_T)                        ,
               Constant('ITR_ZONE_LOGLINEAR', value='5', type=Type.INT32_T)                        
           ]),

    Define('ITR_ZONE_MODEL',
           doc=":class:`ITR` Zone Model defines",
           constants=[
               Constant('ITR_ZONE_MODEL_NOZONE', value='-1', type=Type.INT32_T,
                        doc="The :class:`ITR` has no numeric zones defined (e.g. from a TBL file)")                        ,
               Constant('ITR_ZONE_MODEL_NONE', value='0', type=Type.INT32_T,
                        doc="There is no specific zone model defined.")                        ,
               Constant('ITR_ZONE_MODEL_LINEAR', value='1', type=Type.INT32_T,
                        doc="The :class:`ITR` is set up with a linear transform.")                        ,
               Constant('ITR_ZONE_MODEL_NORMAL', value='2', type=Type.INT32_T,
                        doc="The :class:`ITR` is set up with a normal distribution transform.")                        ,
               Constant('ITR_ZONE_MODEL_EQUAL', value='3', type=Type.INT32_T,
                        doc="The :class:`ITR` is set up with an equal area transform.")                        ,
               Constant('ITR_MODEL_LOGLIN', value='4', type=Type.INT32_T,
                        doc="The :class:`ITR` is set up with a log-linear transform.")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('ChangeBrightness_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Change the brightness.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="-1.0 - black; 0.0 no change; 1.0 white")
               ]),

        Method('ColorVV_ITR', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Get color transform of a :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR"),
                   Parameter('p2', type="VV",
                             doc="Input :class:`VV` of values (none-string)"),
                   Parameter('p3', type="VV",
                             doc="Output :class:`VV` of colours (type INT)")
               ]),

        Method('Copy_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copies ITRs",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` Destination"),
                   Parameter('p2', type="ITR",
                             doc=":class:`ITR` Source")
               ]),

        Method('Create_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`ITR` Object",
               return_type="ITR",
               return_doc=":class:`ITR` Object"),

        Method('CreateFile_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`ITR` Object from an itr, tbl, zon, lut file.",
               return_type="ITR",
               return_doc=":class:`ITR` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="file name, type determined from extension")
               ]),

        Method('CreateIMG_ITR', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`ITR` for an image.",
               return_type="ITR",
               return_doc=":class:`ITR` Object",
               parameters = [
                   Parameter('p1', type="IMG"),
                   Parameter('p2', type=Type.STRING,
                             doc="colour table name, NULL for default"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`ITR_ZONE`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="colour contour interval or :def_val:`rDUMMY`")
               ]),

        Method('CreateMap_ITR', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create :class:`ITR` from Map with Agg Group name.",
               return_type="ITR",
               return_doc=":class:`ITR` Object",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` on which to place the view"),
                   Parameter('p2', type=Type.STRING,
                             doc="Agg Group name")
               ]),

        Method('CreateS_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create an :class:`ITR` Object from a :class:`BF`",
               return_type="ITR",
               return_doc=":class:`ITR` Object",
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` to serialize from")
               ]),

        Method('Destroy_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`ITR` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` Handle")
               ]),

        Method('EqualArea_ITR', module='geoengine.core', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Calculate an equal area transform.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('p2', type="ST",
                             doc="Stat object with a histogram"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="colour contour interval or dummy for none")
               ]),

        Method('GetDataLimits_ITR', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Get :class:`ITR` max/min data limits.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Data minimum value (or :def_val:`rDUMMY` if not set)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Data maximum value (or :def_val:`rDUMMY` if not set)")
               ]),

        Method('GetREG_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`ITR`'s :class:`REG`",
               return_type="REG",
               return_doc=":class:`REG` object",
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object")
               ]),

        Method('GetZoneColor_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the colour in a zone of the :class:`ITR`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Number of the zone to set."),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc=":def:`MVIEW_COLOR`")
               ]),

        Method('iColorValue_ITR', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Transform single data value to color",
               return_type=Type.INT32_T,
               return_doc=":def:`MVIEW_COLOR`",
               parameters = [
                   Parameter('p1', type="ITR"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Data value")
               ]),

        Method('iGetSize_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of zones in an :class:`ITR`",
               return_type=Type.INT32_T,
               return_doc="The number of zones.",
               parameters = [
                   Parameter('p1', type="ITR",
                             doc="The :class:`ITR` Object")
               ]),

        Method('iGetZoneModelType_ITR', module='geoengine.core', version='6.4.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`ITR` zone model (e.g. Linear, LogLin, Equal Area).",
               return_type=Type.INT32_T,
               return_doc=":def:`ITR_ZONE_MODEL`",
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object")
               ]),

        Method('Linear_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Calculate a linear transform.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="minimum"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="maximum"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="colour contour interval or dummy for none")
               ]),

        Method('LoadA_ITR', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Load to an ASCII file, ZON, TBL or ER-Mapper LUT",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR"),
                   Parameter('p2', type=Type.STRING,
                             doc="file name")
               ]),

        Method('LogLinear_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Calculate a log transform.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="minimum ( > 0)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="maximum ( > minimum)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="colour contour interval or dummy for none")
               ]),

        Method('Normal_ITR', module='geoengine.core', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Calculate a normal distribution transform.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Standard deviation"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="mean"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="expansion, normally 1.0"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="colour contour interval or dummy for none")
               ]),

        Method('PowerZone_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Modified :class:`ITR` zone values to 10 (or e) raized to the power of the values",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`ITR_POWER`")
               ]),

        Method('rGetBrightness_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the brightness setting of the :class:`ITR`",
               return_type=Type.DOUBLE,
               return_doc="The brightness setting of the :class:`ITR`",
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object")
               ]),

        Method('rGetZoneValue_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the value in a zone of the :class:`ITR`",
               return_type=Type.DOUBLE,
               return_doc="The value of the specified zone.",
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Number of the zone to set.")
               ]),

        Method('SaveA_ITR', module='geoengine.core', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Save to an ASCII file, ZON, TBL or ER-Mapper LUT",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR"),
                   Parameter('p2', type=Type.STRING,
                             doc="file name")
               ]),

        Method('SaveFile_ITR', module='geoengine.core', version='8.2',
               availability=Availability.PUBLIC, 
               doc="Save to any type (based on the extension of the input file name).",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR"),
                   Parameter('p2', type=Type.STRING,
                             doc="file name")
               ]),

        Method('Serial_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Serialize an :class:`ITR` to a :class:`BF`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object to serialize"),
                   Parameter('p2', type="BF",
                             doc=":class:`BF` to serialize to")
               ]),

        Method('SetAggMap_ITR', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set :class:`ITR` to an Agg in map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` on which to place the view"),
                   Parameter('p2', type=Type.STRING,
                             doc="Agg group name"),
                   Parameter('p3', type="ITR",
                             doc=":class:`ITR` object to set")
               ]),

        Method('SetBrightContrast_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the brightness of the :class:`ITR` colours",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="0.0 - black; 0.5 normal; 1.0 white"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="0.0 - flat; 1.0 normal")
               ]),

        Method('SetColorModel_ITR', module='geoengine.core', version='5.0.2',
               availability=Availability.PUBLIC, 
               doc="Set the color model of an :class:`ITR`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`ITR_COLOR_MODEL`")
               ]),

        Method('SetDataLimits_ITR', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set :class:`ITR` max/min data limits.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Data minimum value"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Data maximum value")
               ]),

        Method('SetSize_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the number of zones in an :class:`ITR`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Number of zones to set :class:`ITR` to.")
               ]),

        Method('SetZoneColor_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the colour in a zone of the :class:`ITR`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Number of the zone to set."),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MVIEW_COLOR`")
               ]),

        Method('SetZoneValue_ITR', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the value in a zone of the :class:`ITR`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ITR",
                             doc=":class:`ITR` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Number of the zone to set."),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="The value to set")
               ])
    ]
}

