from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('SBF',
                 doc="""
The :class:`SBF` class provides a means of storing data in a
file-type directory structure within a workspace, database
or map. Each of these three objects contains its own :class:`SBF` object,
which may be accessed using the :func:`hGetSYS_SBF`, :func:`hGetDB_SBF` and
:func:`hGetMAP_SBF` functions. To access data in a file, or create a
new file in the :class:`SBF` object, call the CreatSBF_BF function (see :class:`BF`),
which will return a :class:`BF` object to use.
""")


gx_defines = [
    Define('SBF_OPEN',
           doc=":class:`SBF` Open defines",
           constants=[
               Constant('SBF_READ', value='0', type=Type.INT32_T,
                        doc="Read only")                        ,
               Constant('SBF_READWRITE_NEW', value='1', type=Type.INT32_T,
                        doc="Read/write - erases structured file")                        ,
               Constant('SBF_READWRITE_OLD', value='2', type=Type.INT32_T,
                        doc="Read/write - open and append onto pre-existing structured file")                        
           ]),

    Define('SBF_TYPE',
           doc=":class:`SBF` Object type defines",
           constants=[
               Constant('SBF_TYPE_DIRS', value='1', type=Type.INT32_T,
                        doc="Embedded directory names")                        ,
               Constant('SBF_TYPE_FILES', value='2', type=Type.INT32_T,
                        doc="Embedded file names")                        ,
               Constant('SBF_TYPE_BOTH', value='3', type=Type.INT32_T,
                        doc="Embedded file and directory names")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_SBF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create a child :class:`SBF` object inside an :class:`SBF`.",
               return_type="SBF",
               return_doc=":class:`SBF` object, terminates if fails.",
               parameters = [
                   Parameter('p1', type="SBF",
                             doc="Parent :class:`SBF`"),
                   Parameter('p2', type=Type.STRING,
                             doc="directory name to open / create"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`SBF_OPEN`")
               ]),

        Method('CreateObjList_SBF', module='geoengine.core', version='5.0.7',
               availability=Availability.PUBLIC, 
               doc="Fills an :class:`LST` with embedded storage names of an :class:`SBF`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SBF",
                             doc=":class:`SBF` handle"),
                   Parameter('p2', type="LST",
                             doc=":class:`LST` handle"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`SBF_TYPE`")
               ]),

        Method('DelDir_SBF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete a directory (storage) from this storage.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SBF",
                             doc=":class:`SBF` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Dir/Storage Name")
               ]),

        Method('DelFile_SBF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Delete a file from this storage.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SBF",
                             doc=":class:`SBF` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('Destroy_SBF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`SBF` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SBF",
                             doc=":class:`SBF` handle")
               ]),

        Method('hGetDB_SBF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the embedded file storage from a database.",
               return_type="SBF",
               return_doc=":class:`SBF` Object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database")
               ]),

        Method('hGetMAP_SBF', module='geoengine.map', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the embedded file storage from a map.",
               return_type="SBF",
               return_doc=":class:`SBF` Object",
               parameters = [
                   Parameter('p1', type="MAP",
                             doc=":class:`MAP` object")
               ]),

        Method('hGetSYS_SBF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the main embedded file storage (in workspace).",
               return_type="SBF",
               return_doc=":class:`SBF` Object"),

        Method('iExistDir_SBF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Check to see if a directory (storage) exists inside this storage.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Does not exist
               1 - Exists
               """,
               parameters = [
                   Parameter('p1', type="SBF",
                             doc=":class:`SBF` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Dir/Storage Name")
               ]),

        Method('iExistFile_SBF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Check to see if a file exists inside this storage.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Does not exist
               1 - Exists
               """,
               parameters = [
                   Parameter('p1', type="SBF",
                             doc=":class:`SBF` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name")
               ]),

        Method('SaveLog_SBF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Save an embedded file to an ASCII file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="SBF",
                             doc=":class:`SBF` Parent"),
                   Parameter('p2', type=Type.STRING,
                             doc="Directory name in the Parent :class:`SBF`"),
                   Parameter('p3', type=Type.STRING,
                             doc="File name in the directory"),
                   Parameter('p4', type=Type.STRING,
                             doc="File to save as (as an ASCII file)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Append Mode: 0 - New file, 1 - Append file")
               ])
    ]
}

