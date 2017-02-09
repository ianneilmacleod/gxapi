from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('HGD',
                 doc="""
                 High Performance Grid. Designed to place grid data
                 on a DAP server. It produces a multi-resolution
                 compressed object that supports multi-threading and
                 allows for high-speed extraction of data at any
                 resolution.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Create_HGD', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Create a handle to an :class:`HGD` object",
               return_type="HGD",
               return_doc=":class:`HGD` handle, terminates if creation fails",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('Destroy_HGD', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`HGD`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HGD",
                             doc=":class:`HGD` to destroy.")
               ]),

        Method('ExportIMG_HGD', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="Export all layers of this :class:`HGD` into grid files.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HGD",
                             doc=":class:`HGD` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of grids (each layers adds _Number to the name)")
               ]),

        Method('GetMETA_HGD', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Get the metadata of a grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HGD",
                             doc=":class:`HGD` object"),
                   Parameter('p2', type="META",
                             doc=":class:`META` object to save :class:`HGD`'s meta to")
               ]),

        Method('hCreateIMG_HGD', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Make an :class:`HGD` from an :class:`IMG`",
               return_type="HGD",
               return_doc=":class:`HGD` Object",
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Image Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Name of :class:`HGD` object")
               ]),

        Method('SetMETA_HGD', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Set the metadata of a grid.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HGD",
                             doc="source :class:`HGD`"),
                   Parameter('p2', type="META",
                             doc=":class:`META` object to add to :class:`HGD`'s meta")
               ])
    ]
}

