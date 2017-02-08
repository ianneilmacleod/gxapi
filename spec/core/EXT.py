from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('EXT',
                 doc="External (plug-in) image methods.")





gx_methods = {
    'Miscellaneous': [

        Method('GetInfo_EXT', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Retrieves information about an external image format.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Image Name"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X Min"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y Min"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="X Max"),
                   Parameter('p5', type=Type.DOUBLE, is_ref=True,
                             doc="Y Max"),
                   Parameter('p6', type="IPJ",
                             doc="Projection Information")
               ])
    ]
}

