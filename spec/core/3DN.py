from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('3DN',
                 doc="""
                 This class manages the rendering of a 3D view. It allows
                 the positioning of the camera, specification of the zoom
                 as well as some rendering controls for the axis. It is
                 directly releated to the :class:`MVIEW` class.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Copy_3DN', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Copy one :class:`3DN` object to another.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc="Destination :class:`3DN` to copy to"),
                   Parameter('p2', type="3DN",
                             doc="Source :class:`3DN` to Copy from")
               ]),

        Method('Create_3DN', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Creates a :class:`3DN`.",
               return_type="3DN",
               return_doc=":class:`3DN` Object"),

        Method('Destroy_3DN', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Destroys a :class:`3DN` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle")
               ]),

        Method('GetPointOfView_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get location of the point we are looking from",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Distance from center relative to longest grid dimension (which is 1.0)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Declination, 0 to 360 CW from Y"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Inclination, -90 to +90")
               ]),

        Method('GetScale_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the axis relative scales.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="X Scale"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Y Scale"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Z Scale")
               ]),

        Method('iGetAxisColor_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the Axis draw color",
               return_type=Type.INT32_T,
               return_doc="Axis Color",
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle")
               ]),

        Method('IGetAxisFont_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the Axis font",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='p3',
                             doc="Font name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Font Buffer Size")
               ]),

        Method('iGetBackgroundColor_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the window background color",
               return_type=Type.INT32_T,
               return_doc="Background Color value",
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle")
               ]),

        Method('IGetRenderControls_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Get the rendering controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="Render Bounding Box (0 or 1)"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="Render Axis (0 or 1)"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="Label for X axis"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of X Buffer"),
                   Parameter('p6', type=Type.STRING, is_ref=True, size_of_param='p7',
                             doc="Label for Y axis"),
                   Parameter('p7', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of Y Buffer"),
                   Parameter('p8', type=Type.STRING, is_ref=True, size_of_param='p9',
                             doc="Label for Z axis"),
                   Parameter('p9', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of Z Buffer")
               ]),

        Method('iGetShading_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set the shading control on or off",
               return_type=Type.INT32_T,
               return_doc="Shading On/Off",
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle")
               ]),

        Method('_SetAxisColor_3DN', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Set the Axis draw color",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Axis Color")
               ]),

        Method('_SetAxisFont_3DN', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Set the Axis font",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Font name")
               ]),

        Method('_SetBackgroundColor_3DN', module='geoengine.map', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Set the window background color",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Background Color")
               ]),

        Method('SetPointOfView_3DN', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set location of the point we are looking from",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Distance from center relative to longest grid dimension (which is 1.0)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Declination, 0 to 360 CW from Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Inclination, -90 to +90")
               ]),

        Method('SetRenderControls_3DN', module='geoengine.map', version='5.1.2',
               availability=Availability.PUBLIC, 
               doc="Set the rendering controls",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Render Bounding Box (0 or 1)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Render Axis (0 or 1)"),
                   Parameter('p4', type=Type.STRING,
                             doc="Label for X axis"),
                   Parameter('p5', type=Type.STRING,
                             doc="Label for Y axis"),
                   Parameter('p6', type=Type.STRING,
                             doc="Label for Z axis")
               ]),

        Method('SetScale_3DN', module='geoengine.map', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="Set the axis relative scales.",
               notes="""
               By default all scales are equal (1.0). By setting
               these scales, relative adjustments to the overall
               view of the 3D objects can be made. Note that they
               are relative to each other. Thus, setting the scaling
               to 5,5,5 is the same as 1,1,1. This is typically used
               to exagerate one scale such as Z (1,1,5).
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X Scale (default 1.0)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y Scale (default 1.0)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Z Scale (default 1.0)")
               ]),

        Method('SetShading_3DN', module='geoengine.map', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set the shading control on or off",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="3DN",
                             doc=":class:`3DN` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="0: Off, 1:  On.")
               ])
    ]
}

