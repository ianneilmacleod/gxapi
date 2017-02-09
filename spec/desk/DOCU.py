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
               notes="""
               If this document is only a URL link, the URL link will
               be resolved and the document downloaded from the appropriate
               server using the protocol specified.
               
               The document has metadata, and the native document does not
               support metadata, the metadata will be placed in an associated
               file "filename.extension.GeosoftMeta"
               """,
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
               notes="""
               On Windows, the default application for the file extension is
               used to open the file.
               """,
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
               notes="""
               Document types are normally identified by their extension.  If you
               leave the document type blank, the extension of the document file
               will be used as the document type.
               
               To resolve conflicting types, you can define your own unique type
               by entering your own type "extension" string.
               
               The following types are pre-defined (as are any normal Geosoft
               file types):
               
                  "htm"       HTML
                  "html"      HTML
                  "txt"       ASCII text file
                  "doc"       Word for Windows document
                  "pdf"       Adobe PDF
                  "map"       Geosoft map file
                  "mmap"      Mapinfo map file (real extension "map")
                  "grd"       Geosoft grid file
                  "gdb"       Geosoft database
               
               URL Document Links
               
               The document name can be a URL link to the document using one of
               the supported protocols. The following protocols are supported:
               
                  http://www.mywebserver.com/MyFile.doc                 - :class:`HTTP`
                  dap://my.dap.server.com/dcs?DatasetName?MyFile.doc    - DAP (DAP Document Access)
                  ftp://my.ftp.server.com/Dir1/MyFile.doc               - FTP protocol
               
               The full file name will be stored but no data will be stored with
               the :class:`DOCU` class and the document can be retrieved using the sGetFile_DOCU
               method.
               """,
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
               notes="""
               See :func:`SetFile_DOCU`.
               This function is the same as sSetFile_DOCU, plus insures that a
               :class:`META` exists that includes the "Data" class.  If the file has
               associated metadata, either supported natively in the file, or
               through an associated file "filename.extension.GeosoftMeta",
               that metadata will be loaded into the :class:`DOCU` meta, and a Data
               class will be constructed if one does not exist.
               
               Also, the Document type Extension is very important in that it
               specifies the document types that natively have metadata. The
               ones currently supported are:
               
                  "map"       Geosoft map file
                  "gdb"       Geosoft database
                  "grd"       Geosoft grid file
               """,
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

