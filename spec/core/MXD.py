from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MXD',
                 doc="""
A :class:`MXD` wraps and provides manipulation and usage for
the content of an ArcGIS :class:`MXD` file.
""")





gx_methods = {
    'Miscellaneous': [

        Method('Commit_MXD', module='geoengine.map', version='7.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Commit any changes to a :class:`MXD`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MXD",
                             doc=":class:`MXD` Handle")
               ]),

        Method('Create_MXD', module='geoengine.map', version='7.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Create a :class:`MXD`.",
               return_type="MXD",
               return_doc=":class:`MXD` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`MXD` file name")
               ]),

        Method('CreateMetadata_MXD', module='geoengine.map', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Create metadata for this brand new :class:`MXD` (we are the creator)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`MXD` file name")
               ]),

        Method('Destroy_MXD', module='geoengine.map', version='7.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Destroy the :class:`MXD` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MXD",
                             doc=":class:`MXD` Handle")
               ]),

        Method('Discard_MXD', module='geoengine.map', version='7.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Discard all changes made to the :class:`MXD`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MXD",
                             doc=":class:`MXD` Handle")
               ]),

        Method('SaveAsMap_MXD', module='geoengine.map', version='7.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Save :class:`MXD` as Geosoft map",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MXD",
                             doc=":class:`MXD` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Geosoft map file name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Export focus map only? :def:`GEO_BOOL`")
               ]),

        Method('ConvertToMap_MXD', module='geoengine.map', version='9.0.0',
               availability=Availability.LICENSED, 
               doc="Create Geosoft map from ArcGIS :class:`MXD`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="ArcGIS :class:`MXD` file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Geosoft map file name")
               ]),

        Method('SaveAsMXD_MXD', module='geoengine.map', version='7.0.0',
               availability=Availability.LICENSED, is_obsolete=True, 
               doc="Save :class:`MXD` as a :class:`MXD` in different location",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MXD",
                             doc=":class:`MXD` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc=":class:`MXD` file name")
               ]),

        Method('Sync_MXD', module='geoengine.map', version='7.0.0',
               availability=Availability.LICENSED, 
               doc="Syncronize any Metadata for this :class:`MXD`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`MXD` file name")
               ])
    ]
}

