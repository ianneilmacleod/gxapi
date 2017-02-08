from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('IPGUI',
                 doc="""
This class is used in the :class:`IP` System for :class:`GUI` functions
such as defining parameters for pseudo-section plots.
""")





gx_methods = {
    'Miscellaneous': [

        Method('iModifyJob_IPGUI', module='geoguilib', version='6.1.0',
               availability=Availability.EXTENSION, 
               doc="Modify parameters for an :class:`IP` plot.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               -1 - User Cancelled
               """,
               parameters = [
                   Parameter('p1', type="IP",
                             doc=":class:`DH` Handle"),
                   Parameter('p2', type="DB",
                             doc=":class:`DB` Handle"),
                   Parameter('p3', type=Type.STRING,
                             doc="Job Name (*.inp)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Job type :def:`IP_PLOT`"),
                   Parameter('p5', type=Type.INT32_T, is_ref=True,
                             doc="Page to open :class:`GUI` on")
               ]),

        Method('LaunchIPQCTool_IPGUI', module='geoguilib', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="Launch the In-Line :class:`IP` QC tool on a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Current Line (can be blank)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Channel to open with (can be blank)")
               ]),

        Method('LaunchOffsetIPQCTool_IPGUI', module='geoguilib', version='9.1.0',
               availability=Availability.EXTENSION, 
               doc="Launch the Offset :class:`IP` QC tool on a database.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Database name"),
                   Parameter('p2', type=Type.STRING,
                             doc="Current Line (can be blank)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Channel to open with (can be blank)")
               ]),

        Method('iIPQCToolExists_IPGUI', module='geoguilib', version='8.1.0',
               availability=Availability.EXTENSION, 
               doc="See if there is an IPQC Tool (Offset or Inline) already open.",
               return_type=Type.INT32_T,
               return_doc="0 if not open, 1 if open")
    ]
}

