from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DOCU',
                 doc="Class to work with documents")


gx_defines = [
    Define('DOCU_OPEN',
           doc="How to open document",
           constants=[
               Constant('DOCU_OPEN_VIEW', value='0', type=Type.INT32_T)                        ,
               Constant('DOCU_OPEN_EDIT', value='1', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Copy_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Copy :class:`DOCU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU",
                             doc="destination :class:`DOCU`"),
                   Parameter('p2', type="DOCU",
                             doc="source :class:`DOCU`")
               ]),

        Method('Create_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Create a document onject",
               return_type="DOCU",
               return_doc=":class:`DOCU` Object"),

        Method('CreateS_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Create from a serialized source",
               return_type="DOCU",
               return_doc=":class:`DOCU` Object",
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` from which to read :class:`DOCU`")
               ]),

        Method('Destroy_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Destroy",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU",
                             doc=":class:`DOCU` Handle")
               ]),

        Method('GetFile_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Get the document and place in a file.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU"),
                   Parameter('p2', type=Type.STRING,
                             doc="file to which to write document")
               ]),

        Method('GetFileMeta_DOCU', module='geogxx', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Get the document and place in a file with metadata.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU"),
                   Parameter('p2', type=Type.STRING,
                             doc="file to which to write document")
               ]),

        Method('GetMETA_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Get the document's meta",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU"),
                   Parameter('p2', type="META",
                             doc=":class:`META` object to fill in with the document's meta")
               ]),

        Method('IDocName_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="The document name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="buffer to fill with document name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of buffer")
               ]),

        Method('IFileName_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="The original document file name.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="buffer to fill with document file name"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_FILE',
                             doc="size of buffer")
               ]),

        Method('iHaveMETA_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Do you have meta data?",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="DOCU")
               ]),

        Method('iIsReference_DOCU', module='geogxx', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Is the document only a reference (a URL) ?",
               return_type=Type.INT32_T,
               return_doc="1 - Yes, 0 - No",
               parameters = [
                   Parameter('p1', type="DOCU",
                             doc="Document")
               ]),

        Method('Open_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Open a document in the document viewer",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`DOCU_OPEN`")
               ]),

        Method('Serial_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Serialize :class:`DOCU`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU"),
                   Parameter('p2', type="BF",
                             doc=":class:`BF` in which to write object")
               ]),

        Method('SetFile_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Set the document from a file source.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU"),
                   Parameter('p2', type=Type.STRING,
                             doc="document type"),
                   Parameter('p3', type=Type.STRING,
                             doc='document name, if "" file name will be used'),
                   Parameter('p4', type=Type.STRING,
                             doc="document file, must exist")
               ]),

        Method('SetFileMeta_DOCU', module='geogxx', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Set the document from a file source with metadata.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU"),
                   Parameter('p2', type=Type.STRING,
                             doc="document type extension"),
                   Parameter('p3', type=Type.STRING,
                             doc="document name, if NULL use file name"),
                   Parameter('p4', type=Type.STRING,
                             doc="document file or URL")
               ]),

        Method('SetMETA_DOCU', module='geogxx', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Set the document's meta",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DOCU"),
                   Parameter('p2', type="META",
                             doc=":class:`META` to add to the document's meta")
               ])
    ]
}

