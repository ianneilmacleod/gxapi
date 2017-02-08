from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('LMSG',
                 doc="Message class methods.")





gx_methods = {
    'Miscellaneous': [

        Method('GotoPoint_LMSG', module='geogxx', version='5.0.7',
               availability=Availability.LICENSED, 
               doc="Sends a move cursor message",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="X location"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y location"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Z location"),
                   Parameter('p4', type="IPJ",
                             doc=":class:`IPJ` (if (:class:`IPJ`)0, default coordinate system)")
               ]),

        Method('ViewArea_LMSG', module='geogxx', version='5.0.7',
               availability=Availability.LICENSED, 
               doc="Sends a view area message",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE,
                             doc="X0 location"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y0 location"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="X1 location"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Y1 location"),
                   Parameter('p5', type="IPJ",
                             doc=":class:`IPJ` (if (:class:`IPJ`)0, default coordinate system)")
               ])
    ]
}

