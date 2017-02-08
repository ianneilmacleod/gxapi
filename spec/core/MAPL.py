from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('MAPL',
                 doc="""
The :class:`MAPL` class is the interface with the MAPPLOT program,
which reads a MAPPLOT control file and plots graphical
entities to a map. The :class:`MAPL` object is created for a given
control file, then passed to the MAPPLOT program, along
with the target :class:`MAP` object on which to do the drawing
""")





gx_methods = {
    'Miscellaneous': [

        Method('Create_MAPL', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a :class:`MAPL`.",
               return_type="MAPL",
               return_doc=":class:`MAPL`, aborts if creation fails",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`MAPL` file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="map base reference name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="start line number in file (0 is first)")
               ]),

        Method('CreateREG_MAPL', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a :class:`MAPL` with :class:`REG`.",
               return_type="MAPL",
               return_doc=":class:`MAPL`, aborts if creation fails",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`MAPL` file name"),
                   Parameter('p2', type=Type.STRING,
                             doc="map base reference name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="start line number in file (0 is first)"),
                   Parameter('p4', type="REG")
               ]),

        Method('Destroy_MAPL', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy the :class:`MAPL` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPL",
                             doc=":class:`MAPL` Handle")
               ]),

        Method('Process_MAPL', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Process a :class:`MAPL`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPL",
                             doc=":class:`MAPL` Handle"),
                   Parameter('p2', type="MAP")
               ]),

        Method('ReplaceString_MAPL', module='geoengine.map', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Adds a replacement string to a mapplot control file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="MAPL",
                             doc=":class:`MAPL` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Variable"),
                   Parameter('p3', type=Type.STRING,
                             doc="Replacement")
               ])
    ]
}

