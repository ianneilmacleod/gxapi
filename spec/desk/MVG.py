from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MVG',
                 doc="The :class:`MVG` class provides the ability to create view graphs.")


gx_defines = [
    Define('MVG_DRAW',
           doc=":class:`MVG` draw define",
           constants=[
               Constant('MVG_DRAW_POLYLINE', value='0', type=Type.INT32_T)                        ,
               Constant('MVG_DRAW_POLYGON', value='1', type=Type.INT32_T)                        
           ]),

    Define('MVG_GRID',
           doc=":class:`MVG` grid define",
           constants=[
               Constant('MVG_GRID_DOT', value='0', type=Type.INT32_T)                        ,
               Constant('MVG_GRID_LINE', value='1', type=Type.INT32_T)                        ,
               Constant('MVG_GRID_CROSS', value='2', type=Type.INT32_T)                        
           ]),

    Define('MVG_LABEL_BOUND',
           doc=":class:`MVG` label bound define",
           constants=[
               Constant('MVG_LABEL_BOUND_NO', value='0', type=Type.INT32_T)                        ,
               Constant('MVG_LABEL_BOUND_YES', value='1', type=Type.INT32_T)                        
           ]),

    Define('MVG_LABEL_JUST',
           doc=":class:`MVG` label justification define",
           constants=[
               Constant('MVG_LABEL_JUST_TOP', value='0', type=Type.INT32_T)                        ,
               Constant('MVG_LABEL_JUST_BOTTOM', value='1', type=Type.INT32_T)                        ,
               Constant('MVG_LABEL_JUST_LEFT', value='2', type=Type.INT32_T)                        ,
               Constant('MVG_LABEL_JUST_RIGHT', value='3', type=Type.INT32_T)                        
           ]),

    Define('MVG_LABEL_ORIENT',
           doc=":class:`MVG` label orientation",
           constants=[
               Constant('MVG_LABEL_ORIENT_HORIZONTAL', value='0', type=Type.INT32_T)                        ,
               Constant('MVG_LABEL_ORIENT_TOP_RIGHT', value='1', type=Type.INT32_T)                        ,
               Constant('MVG_LABEL_ORIENT_TOP_LEFT', value='2', type=Type.INT32_T)                        
           ]),

    Define('MVG_SCALE',
           doc=":class:`MVG` scale define",
           constants=[
               Constant('MVG_SCALE_LINEAR', value='0', type=Type.INT32_T)                        ,
               Constant('MVG_SCALE_LOG', value='1', type=Type.INT32_T)                        ,
               Constant('MVG_SCALE_LOGLINEAR', value='2', type=Type.INT32_T)                        
           ]),

    Define('MVG_WRAP',
           doc=":class:`MVG` wrap define",
           constants=[
               Constant('MVG_WRAP_NO', value='0', type=Type.INT32_T)                        ,
               Constant('MVG_WRAP_YES', value='1', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AxisX_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw an X axis",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVG"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y location in plot units (mm)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="left  X (rescaling unit)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="right X (rescaling unit)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="major tick interval (rescaling unit). Ticks drawn in decades in LOG or LOGLINEAR scale"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="minor tick interval  (rescaling unit). Not used in LOG/LOGLINEAR"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="tick size in view units (mm) (negative for down ticks)")
               ]),

        Method('AxisY_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw a  Y axis",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVG"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location in plot units (mm)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="bottom Y (rescaling unit)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="top Y (rescaling unit)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="major tick interval (rescaling unit). Ticks drawn in decades in LOG or LOGLINEAR scale"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="minor tick interval  (rescaling unit). Not used in LOG/LOGLINEAR"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="tick size in plot units (mm)(negative for left ticks)")
               ]),

        Method('Create_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a :class:`MVG` object",
               return_type="MVG",
               return_doc=":class:`MVG` handle (NULL if error)",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc="H_MAP handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="View Name"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Minimum X in map unit (mm)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Minimum Y in map unit (mm)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Maximum X in map unit (mm)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="Maximum Y in map unit (mm)"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Minimum X in view unit (m for example)"),
                   Parameter('p8', type=Type.DOUBLE,
                             doc="Minimum Y in view unit"),
                   Parameter('p9', type=Type.DOUBLE,
                             doc="Maximum X in view unit"),
                   Parameter('p10', type=Type.DOUBLE,
                             doc="Maximum Y in view unit")
               ]),

        Method('Destroy_MVG', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`MVG` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVG",
                             doc=":class:`MVG` Handle")
               ]),

        Method('GetMVIEW_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Get the :class:`MVIEW` Handle of the Object.",
               return_type="MVIEW",
               return_doc=":class:`MVIEW` Handle",
               parameters = [
                   Parameter('p1', type="MVG",
                             doc=":class:`MVG` object")
               ]),

        Method('Grid_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Draw a grid in the current :class:`MVG`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVG"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X position of 1st vertical grid line to draw (in rescaling unit)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Y position of 1st horizontal grid line to draw (in rescaling unit)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="X grid increment of rescaled map unit (see above Rescaling functions)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Y grid increment of rescaled map unit (see above Rescaling functions)"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="X dot increment/cross X size of rescaled map unit"),
                   Parameter('p7', type=Type.DOUBLE,
                             doc="Y dot increment/cross Y size of rescaled map unit"),
                   Parameter('p8', type=Type.INT32_T,
                             doc=":def:`MVG_GRID`")
               ]),

        Method('LabelX_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Label annotations on the X axis",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVG"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Y location in plot units (mm)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="left  X (rescaling unit)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="right X (rescaling unit)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="major tick interval (ignored if in LOG or LOGLINEAR rescaling)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="label justification :def:`MVG_LABEL_JUST`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="edge label bounding :def:`MVG_LABEL_BOUND`"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="label orientation   :def:`MVG_LABEL_ORIENT`")
               ]),

        Method('LabelY_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Label annotations on the Y axis",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVG"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="X location in plot units (mm)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="bottom  Y (rescaling unit)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="top Y (rescaling unit)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="label interval (ignored if in LOG or LOGLINEAR rescaling)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="label justification :def:`MVG_LABEL_JUST`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="edge label bounding :def:`MVG_LABEL_BOUND`"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="label orientation   :def:`MVG_LABEL_ORIENT`")
               ]),

        Method('PolyLineVA_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Creates PolyLines/polygons from :class:`VV` and :class:`VA`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVG"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVG_DRAW`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MVG_WRAP`"),
                   Parameter('p4', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('p5', type="VA",
                             doc="Y VAs"),
                   Parameter('p6', type="VV",
                             doc=":class:`VV` containing list of :class:`VA` ranges, such as 1,2 40 ... Entire :class:`VA` is drawn if this :class:`VV` is empty.")
               ]),

        Method('PolyLineVV_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Creates PolyLines/polygons from :class:`VV` and :class:`VV`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVG"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVG_DRAW`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`MVG_WRAP`"),
                   Parameter('p4', type="VV",
                             doc="X :class:`VV`"),
                   Parameter('p5', type="VV",
                             doc="Y :class:`VV`")
               ]),

        Method('RescaleXRange_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Re-scale horizontal axis",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVG",
                             doc=":class:`MVG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVG_SCALE`"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Scale information: new minimum X"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Scale information: new maximum X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Scale information: minimum X to apply log10, it is defined only for LOGLINEAR scale")
               ]),

        Method('RescaleYRange_MVG', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Re-scale vertical axis",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MVG",
                             doc=":class:`MVG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`MVG_SCALE`"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Scale information: new minimum Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Scale information: new maximum Y"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Scale information: minimum Y to apply log10, it is defined only for LOGLINEAR scale")
               ])
    ]
}

