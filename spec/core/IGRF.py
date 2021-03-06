from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('IGRF',
                 doc="""
                 International Geomagnetic Reference Field
                 Methods to work with :class:`IGRF` objects. The :class:`IGRF` object
                 contains data for the :class:`IGRF` model of the geomagnetic
                 reference field.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Calc_IGRF', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate :class:`IGRF` data for a given :class:`IGRF` model.",
               notes="""
               Calculate :class:`IGRF` data (total field, inclination, and declination)
               for a given :class:`IGRF` model. The model used will be the same as that
               obtained with :func:`Create_IGRF`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IGRF",
                             doc=":class:`IGRF` model"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Elevation (metres)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Longitude (-180 to 180)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Latitude  (-90 to 90) Returns"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Field strength"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="Field inclination"),
                   Parameter('p7', type=Type.DOUBLE, is_ref=True,
                             doc="Field declination")
               ]),

        Method('CalcVV_IGRF', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Calculate :class:`IGRF` data :class:`VV`'s for a given :class:`IGRF` model.",
               notes="""
               Calculate :class:`IGRF` data (total field, inclination, and declination)
               for a given :class:`IGRF` model. The model used will be the same as that
               obtained with :func:`Create_IGRF`.
               All of the :class:`VV`'s should be the same length. The function
               will abort if they are not.
               
               No assumption is made on what data types are contained by
               any of the :class:`VV`'s. However, all total field, inclination, and
               declination values are internally calculated as real data.
               These values will be converted to the types contained in the
               output :class:`VV`'s.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IGRF",
                             doc=":class:`IGRF` model"),
                   Parameter('p2', type="VV",
                             doc="Input elevation data (metres)"),
                   Parameter('p3', type="VV",
                             doc="Input longitude data (-180 to 180)"),
                   Parameter('p4', type="VV",
                             doc="Input latitude data  (-90 to 90)"),
                   Parameter('p5', type="VV",
                             doc="Output total field"),
                   Parameter('p6', type="VV",
                             doc="Output inclination"),
                   Parameter('p7', type="VV",
                             doc="Output declination")
               ]),

        Method('Create_IGRF', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create an :class:`IGRF`.",
               notes="""
               If the year of the :class:`IGRF` model is dummy, then
               the :class:`IGRF` year nearest to the line's date will
               be used. Otherwise, the specified year is used.
               """,
               return_type="IGRF",
               return_doc=":class:`IGRF` Object",
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="Date required"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Year of the :class:`IGRF` model to use"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of the :class:`IGRF` reference data file")
               ]),

        Method('DateRange_IGRF', module='geoengine.core', version='6.1.0',
               availability=Availability.LICENSED, 
               doc="Determine the range of years covered by an :class:`IGRF` or DGRF file",
               notes="""
               This is useful when using a DGRF file, because the system is set
               up only to calculate for years within the date range, and will
               return an error otherwise.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Model data file name"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum year  (:def_val:`rMAX` if none found)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum year  (:def_val:`rMIN` if none found)")
               ]),

        Method('Destroy_IGRF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy an :class:`IGRF`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IGRF",
                             doc=":class:`IGRF` to destroy.")
               ])
    ]
}

