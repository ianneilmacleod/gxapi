from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('PAT',
                 doc="""
A :class:`PAT` object is created from a Geosoft-format pattern file.
It contains all the individual patterns listed in the file.

Notes		You may create your own fill patterns should be added to the "user.pat"
le in the <geosoft>\\user\\etc directory.

you wish to add your own fill patterns, create a file named user.pat in
e <geosoft>/User/ directory and add your own fill patterns in the number
nge 20000 to 29999.
""")





gx_methods = {
    'Miscellaneous': [

        Method('Create_PAT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates a pattern object with current default patterns.",
               return_type="PAT",
               return_doc=":class:`PAT` object"),

        Method('Destroy_PAT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys a pattern object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PAT",
                             doc=":class:`PAT` Handle")
               ]),

        Method('GetLST_PAT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copies all pattern names into a :class:`LST` object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PAT",
                             doc=":class:`PAT` Handle"),
                   Parameter('p2', type=Type.STRING,
                             doc='Class name ("" for all classes)'),
                   Parameter('p3', type="LST",
                             doc=":class:`LST` Handle")
               ])
    ],
    'Obsolete': [

        Method('Copy_PAT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Copy one :class:`PAT` object to another.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PAT",
                             doc="Destination :class:`PAT` to copy to"),
                   Parameter('p2', type="PAT",
                             doc="Source :class:`PAT` to Copy from")
               ]),

        Method('Load_PAT', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Load patterns from a file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PAT",
                             doc=":class:`PAT` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Pattern file name")
               ])
    ]
}

