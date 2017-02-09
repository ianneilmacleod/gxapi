from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('AGG',
                 doc="""
                 The :class:`AGG` class is used to handle image display on maps.
                 An aggragate contains one or more image layers (LAY) with
                 each layer representing a grid or image file. The :class:`AGG`
                 will combine all the layers to form one image
                 """)


gx_defines = [
    Define('AGG_LAYER_ZONE',
           doc="Aggregate Layer Zone defines",
           constants=[
               Constant('AGG_LAYER_ZONE_DEFAULT', value='0', type=Type.INT32_T,
                        doc="""
                        If a colour table with no colour transform is passed
                        it will be used with the default zoning
                        method of the data, which is usually
                        :def_val:`AGG_LAYER_ZONE_EQUALAREA`.
                        """)                        ,
               Constant('AGG_LAYER_ZONE_LINEAR', value='1', type=Type.INT32_T,
                        doc="Linear Distribution")                        ,
               Constant('AGG_LAYER_ZONE_NORMAL', value='2', type=Type.INT32_T,
                        doc="Normal Distribution")                        ,
               Constant('AGG_LAYER_ZONE_EQUALAREA', value='3', type=Type.INT32_T,
                        doc="Equal Area Distribution")                        ,
               Constant('AGG_LAYER_ZONE_SHADE', value='4', type=Type.INT32_T,
                        doc="""
                        If :def_val:`AGG_LAYER_ZONE_SHADE` is specified, a shaded relief
                        layer is created from the specified grid.  A new grid
                        file will also be created to hold the shaded relief
                        image data.  This file will have the same name as the
                        original grid but with "_s" added to the root name.
                        It will always be located in the workspace directory
                        regardless of the location of the original source image.
                        If the file already exists, it will used as it is.
                        Shading is always at inclination = declination = 45 deg.
                        with default scaling.  If different shading is desired,
                        use the :func:`LayerShadeIMG_AGG` method.
                        """)                        ,
               Constant('AGG_LAYER_ZONE_LOGLINEAR', value='5', type=Type.INT32_T,
                        doc="Log Linear Distribution")                        ,
               Constant('AGG_LAYER_ZONE_LAST', value='6', type=Type.INT32_T,
                        doc="""
                        The last :class:`ITR` used to display this
                        data will be used if it exists.  If it
                        does not exist, the behaviour is the same
                        as :def_val:`AGG_LAYER_ZONE_DEFAULT`.
                        """)                        
           ]),

    Define('AGG_MODEL',
           doc="Aggregation color model defines",
           constants=[
               Constant('AGG_MODEL_HSV', value='1', type=Type.INT32_T,
                        doc="Hue Saturation Value")                        ,
               Constant('AGG_MODEL_RGB', value='2', type=Type.INT32_T,
                        doc="Red Green Blue")                        ,
               Constant('AGG_MODEL_CMY', value='3', type=Type.INT32_T,
                        doc="Cyan Magenta Yellow")                        
           ]),

    Define('AGG_RENDER',
           doc="Aggregation rendering modes",
           constants=[
               Constant('AGG_RENDER_ADD', value='0', type=Type.INT32_T,
                        doc="Add all the colors together")                        ,
               Constant('AGG_RENDER_BLEND', value='1', type=Type.INT32_T,
                        doc="Adds and divides by the number of non-dummy colors")                        ,
               Constant('AGG_RENDER_BLEND_ALL', value='2', type=Type.INT32_T,
                        doc="Adds and divides by the number of colors")                        ,
               Constant('AGG_RENDER_FADE', value='3', type=Type.INT32_T,
                        doc="Multiplies current colors by the input's colors over 255 (input works as the percentage of color to preserve)")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('_SetModel_AGG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Sets the Color Model",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="AGG"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`AGG_MODEL`")
               ]),

        Method('ChangeBrightness_AGG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Change the brightness.",
               notes="""
               0.0 brightness does nothing.
               -1.0 to 0.0 makes colours darker, -1.0 is black
               0.0 to 1.0 makes colours lighter, 1.0 is white
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="AGG",
                             doc=":class:`AGG` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="-1.0 - black; 0.0 no change; 1.0 white")
               ]),

        Method('Create_AGG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create an aggregate",
               return_type="AGG",
               return_doc=":class:`AGG` Object"),

        Method('CreateMap_AGG', module='geoengine.map', version='5.0.5',
               availability=Availability.PUBLIC, 
               doc="Create :class:`AGG` from Map with Group name.",
               notes="""
               The Agg Group name must include the View name with a
               backslash separating the view name and group name; e.g.
               "Data\\AGG_test" (when used as a string, the double slash
               represents as single \\).
               """,
               return_type="AGG",
               return_doc=":class:`AGG` Object",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` on which to place the view"),
                   Parameter('p2', type=Type.STRING,
                             doc="Agg Group name")
               ]),

        Method('Destroy_AGG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`AGG` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="AGG",
                             doc=":class:`AGG` Handle")
               ]),

        Method('GetLayerITR_AGG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`ITR` of a layer",
               notes="""
               Layers are numbered from 0, consecutively in the order they are
               placed in the aggregate.
               
               An error will occur if the layer does not exist.
               
               Caller must create/destroy :class:`ITR`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="AGG"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="layer number"),
                   Parameter('p3', type="ITR")
               ]),

        Method('ILayerPIC_AGG', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Add a PIC as a layer in an aggregate.",
               notes="""
               This function creates a temporary PNG file in the temp directory.
               The name is returned so that you can pack the map and remove the file
               or copy the file elsewhere for later use.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="AGG"),
                   Parameter('p2', type="PIC"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Temp File name"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_FILE',
                             doc="Max Temp File name length")
               ]),

        Method('iListImg_AGG', module='geoengine.core', version='5.0.6',
               availability=Availability.PUBLIC, 
               doc="Lists file names of all the IMGs inside of the :class:`AGG`.",
               notes="The returned :class:`VV` contains the file names.",
               return_type=Type.INT32_T,
               return_doc="The number of Imgs.",
               parameters = [
                   Parameter('p1', type="AGG",
                             doc=":class:`AGG` Handle"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` of type -:def_val:`STR_FILE`")
               ]),

        Method('iNumLayers_AGG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of layers in an aggregate.",
               return_type=Type.INT32_T,
               return_doc="The number of layers in an aggregate.",
               parameters = [
                   Parameter('p1', type="AGG")
               ]),

        Method('LayerIMG_AGG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add an image as a layer in an aggregate.",
               see_also=":func:`LayerShadeIMG_AGG`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="AGG"),
                   Parameter('p2', type=Type.STRING,
                             doc="grid name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`AGG_LAYER_ZONE` transform to use if colour table has none defined."),
                   Parameter('p4', type=Type.STRING,
                             doc='colour table name, "" for default This can be a .TBL .ZON .:class:`ITR` or .:class:`AGG` file .TBL is the default'),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="colour contour interval or :def_val:`rDUMMY` for default")
               ]),

        Method('LayerIMGEx_AGG', module='geoengine.core', version='8.2',
               availability=Availability.PUBLIC, 
               doc="Add an image as a layer in an aggregate.",
               see_also=":func:`LayerShadeIMG_AGG`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="AGG"),
                   Parameter('p2', type=Type.STRING,
                             doc="grid name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`AGG_LAYER_ZONE` transform to use if colour table has none defined."),
                   Parameter('p4', type=Type.STRING,
                             doc='colour table name, "" for default This can be a .TBL .ZON .:class:`ITR` or .:class:`AGG` file .TBL is the default'),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="minimum value or :def_val:`rDUMMY` for default"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="maximum value or :def_val:`rDUMMY` for default"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="colour contour interval or :def_val:`rDUMMY` for default")
               ]),

        Method('LayerShadeIMG_AGG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a shaded image as a layer in an aggregate.",
               notes="""
               A new grid file will be created to hold the shaded
               image data.  This file will have the same name as the
               original grid but with "_s" added to the root name.
               It will always be located in the workspace directory
               regardless of the location of the original source image.
               If the file already exists, it will replaced.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="AGG"),
                   Parameter('p2', type=Type.STRING,
                             doc="grid name"),
                   Parameter('p3', type=Type.STRING,
                             doc='colour table name, "" for default'),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="inclination"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="declination"),
                   Parameter('p6', type=Type.DOUBLE, is_ref=True,
                             doc="scale (:def_val:`rDUMMY` for default, returns value used)")
               ]),

        Method('rGetBrightness_AGG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the brightness setting of the :class:`AGG`",
               notes="""
               Brightness can range from -1.0 (black) to 1.0 (white).
               This brightness control is relative to the normal colour
               when the :class:`AGG` is created.
               
               :class:`AGG` brightness depends on the brightness of the :class:`ITR` of each layer.
               Calling dGetBright_AGG will poll all layers, and if all have the same
               brightness, this is returned.  If any of the layers have a different
               brightness, the current brightness of each layer is changed to be
               the reference brightness (0.0)and the brightness value of 0.0 is
               returned.
               """,
               see_also=":func:`ChangeBrightness_AGG`, :func:`rGetBrightness_AGG`, :func:`ChangeBrightness_AGG`",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type="AGG",
                             doc=":class:`AGG` object")
               ]),

        Method('SetLayerITR_AGG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the :class:`ITR` of a layer",
               notes="""
               Layers are numbered from 0, consecutively in the order they are
               placed in the aggregate.
               
               An error will occur if the layer does not exist.
               
               Caller must create/destroy :class:`ITR`.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="AGG"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="layer number"),
                   Parameter('p3', type="ITR")
               ]),

        Method('SetRenderMethod_AGG', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Sets the Rendering Method",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="AGG"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`AGG_RENDER`")
               ]),

        Method('UpdateThumb_AGG', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Update the thumbnail of an :class:`IMG` from an :class:`AGG`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="AGG",
                             doc=":class:`AGG` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="name of the grid to update"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="size of the thumbnail in pixels (64 is typical) the minimum size if 16 (16x16)")
               ])
    ]
}

