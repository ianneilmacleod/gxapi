from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('BF',
                 doc="""
                 The :class:`BF` class is used to access (or create) Binary files and remove
                 (or destroy) files from use. You can also perform a variety of
                 additional tasks, such as positioning within files, reading from
                 files and writing to files.
                 """)


gx_defines = [
    Define('BF_BYTEORDER',
           doc="Byte order for read/write",
           constants=[
               Constant('BF_BYTEORDER_LSB', value='256', type=Type.INT32_T,
                        doc="Least significant byte first (Intel, Windows)")                        ,
               Constant('BF_BYTEORDER_MSB', value='512', type=Type.INT32_T,
                        doc="Most significant byte first (Mororola, Sun)")                        
           ]),

    Define('BF_CLOSE',
           doc="Close Flags",
           constants=[
               Constant('BF_KEEP', value='0', type=Type.INT32_T)                        ,
               Constant('BF_DELETE', value='1', type=Type.INT32_T)                        
           ]),

    Define('BF_ENCODE',
           doc="The way a string is encoded",
           constants=[
               Constant('BF_ENCODE_ANSI', value='0', type=Type.INT32_T,
                        doc="String is stored as ANSI code page")                        ,
               Constant('BF_ENCODE_UTF8', value='1', type=Type.INT32_T,
                        doc="String is stored as :def:`UTF8`")                        
           ]),

    Define('BF_OPEN_MODE',
           doc="Open Status",
           constants=[
               Constant('BF_READ', value='0', type=Type.INT32_T,
                        doc="Read only")                        ,
               Constant('BF_READWRITE_NEW', value='1', type=Type.INT32_T,
                        doc="erases existing file")                        ,
               Constant('BF_READWRITE_OLD', value='2', type=Type.INT32_T,
                        doc="file must pre-exist")                        ,
               Constant('BF_READWRITE_APP', value='4', type=Type.INT32_T,
                        doc="open and append onto pre-existing file (cannot be read from)")                        
           ]),

    Define('BF_SEEK',
           doc="Seek Location",
           constants=[
               Constant('BF_SEEK_START', value='0', type=Type.INT32_T)                        ,
               Constant('BF_SEEK_CURRENT', value='1', type=Type.INT32_T)                        ,
               Constant('BF_SEEK_EOF', value='2', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('ReadBuff_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_cpp=True, 
               doc="Read data from a :class:`BF` stream into memory",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` object"),
                   Parameter('p2', type="void*",
                             doc="Data buffer to read data into"),
                   Parameter('p3', type=Type.INT32_T, is_val=True,
                             doc="Number of bytes to read")
               ]),

        Method('WriteBuff_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_cpp=True, 
               doc="Write data from memory into a :class:`BF` stream",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` object"),
                   Parameter('p2', type="const void*",
                             doc="Data buffer to write data from"),
                   Parameter('p3', type=Type.INT32_T, is_val=True,
                             doc="Number of bytes to write")
               ]),

        Method('_ChSize_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Changes the size of a file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="new length in bytes")
               ]),

        Method('_Seek_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Moves file position",
               notes="""
               Terminates if attempt to move past the end of
               a read-only file.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="number of bytes from reference point"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`BF_SEEK`")
               ]),

        Method('Copy_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Copy entire contents of a source :class:`BF` to a destination :class:`BF`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc="Source :class:`BF`"),
                   Parameter('p2', type="BF",
                             doc="Destination :class:`BF`")
               ]),

        Method('CRC_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Compute CRC of a file.",
               return_type="CRC",
               return_doc="CRC Value",
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="number of bytes to CRC"),
                   Parameter('p3', type="CRC",
                             doc="CRC start (use :def_val:`CRC_INIT_VALUE` for new)")
               ]),

        Method('Create_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create :class:`BF` object.",
               notes="""
               Run-time specific directory paths may be added the the front of file names
               as follows:
               
               <geosoft>      the main Geosoft installation directory
               <geosoft2>     the secondary Geosoft installation directory
               <geotemp>      the Geosoft temporary file directory
               <windows>      the operating system Windows directory
               <system>       the operating system system directory
               <other>        other environment variables
               
               For example "<geosoft>/user/csv/datum.csv"
               """,
               return_type="BF",
               return_doc=":class:`BF` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='file name to open ("" is a temporary file)'),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`BF_OPEN_MODE`")
               ]),

        Method('CreateSBF_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Create :class:`BF` object inside an :class:`SBF`.",
               notes="see sbf.gxh",
               return_type="BF",
               return_doc=":class:`BF` Object",
               parameters = [
                   Parameter('p1', type="SBF",
                             doc="Storage"),
                   Parameter('p2', type=Type.STRING,
                             doc='file name to open ("" is a temporary file)'),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`BF_OPEN_MODE`")
               ]),

        Method('Destroy_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`BF` handle.",
               notes="The DestroyEx call implies :def_val:`BF_KEEP`",
               return_type=Type.VOID,
               return_doc="nothing",
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="BF_?")
               ]),

        Method('DestroyEx_BF', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`BF` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle")
               ]),

        Method('iEOF_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns 1 if at the end of the file",
               return_type=Type.INT32_T,
               return_doc="""
               1 if at the end of the file,
               0 if not at the end of the file
               """,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle")
               ]),

        Method('iQueryWrite_BF', module='geoengine.core', version='5.1.1',
               availability=Availability.PUBLIC, 
               doc="Check if you can write to the :class:`BF`.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - No
               1 - Yes
               """,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle")
               ]),

        Method('IReadBinaryString_BF', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Reads string data from current position in :class:`BF`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Number of bytes to read"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`BF_ENCODE`"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='4',
                             doc="data"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Length of the string buffer")
               ]),

        Method('iSize_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the file length",
               return_type=Type.INT32_T,
               return_doc="File size in bytes.",
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle")
               ]),

        Method('iTell_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns current position of file pointer in bytes",
               return_type=Type.INT32_T,
               return_doc="Current file pointer location",
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle")
               ]),

        Method('ReadInt_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Reads int data from current position in :class:`BF`",
               notes="""
               If the data source may be in byte order different from that
               required by the reader, you can add the source byte-order
               to the :class:`BF` elelment type.  The byte order will be swapped
               if required.  For example, to write out a real number 3.5
               with Most-Significant_Byte first (Mortorola) convention:
               
               :func:`WriteReal_BF`(hBF,:def_val:`BF_BYTEORDER_MSB`+:def_val:`GS_REAL`,3.5).
               
               If a byte order is not specified, the source is assumed to be
               in the native byte order of the reading/writing computer.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GS_TYPES` and :def:`BF_BYTEORDER`"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="data")
               ]),

        Method('ReadReal_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Reads real data from current position in :class:`BF`",
               notes="""
               If the data source may be in byte order different from that
               required by the reader, you can add the source byte-order
               to the :class:`BF` elelment type.  The byte order will be swapped
               if required.  For example, to write out a real number 3.5
               with Most-Significant_Byte first (Mortorola) convention:
               
               :func:`WriteReal_BF`(hBF,:def_val:`BF_BYTEORDER_MSB`+:def_val:`GS_REAL`,3.5).
               
               If a byte order is not specified, the source is assumed to be
               in the native byte order of the reading/writing computer.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GS_TYPES` and :def:`BF_BYTEORDER`"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="data")
               ]),

        Method('ReadVM_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_cpp=True, 
               doc="Read data to a :class:`VM` from current position in :class:`BF`",
               notes="""
               If the data source may be in byte order different from that
               required by the reader, you can add the source byte-order
               to the :class:`BF` elelment type.  The byte order will be swapped
               if required.  For example, to write out a real number 3.5
               with Most-Significant_Byte first (Mortorola) convention:
               
               :func:`WriteReal_BF`(hBF,:def_val:`BF_BYTEORDER_MSB`+:def_val:`GS_REAL`,3.5).
               
               If a byte order is not specified, the source is assumed to be
               in the native byte order of the reading/writing computer.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GS_TYPES` and :def:`BF_BYTEORDER`"),
                   Parameter('p3', type="VM",
                             doc=":class:`VM` data to read, :class:`VM` length is read")
               ]),

        Method('ReadVV_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Read data to a :class:`VV` from current position in :class:`BF`",
               notes="""
               If the data source may be in byte order different from that
               required by the reader, you can add the source byte-order
               to the :class:`BF` elelment type.  The byte order will be swapped
               if required.  For example, to write out a real number 3.5
               with Most-Significant_Byte first (Mortorola) convention:
               
               :func:`WriteReal_BF`(hBF,:def_val:`BF_BYTEORDER_MSB`+:def_val:`GS_REAL`,3.5).
               
               If a byte order is not specified, the source is assumed to be
               in the native byte order of the reading/writing computer.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GS_TYPES` and :def:`BF_BYTEORDER`"),
                   Parameter('p3', type="VV",
                             doc=":class:`VV` data to read, :class:`VV` length is read")
               ]),

        Method('SetDestroyStatus_BF', module='geoengine.core', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Set the flag to delete the file on close",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`BF_CLOSE`")
               ]),

        Method('WriteBinaryString_BF', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Write a binary string to a :class:`BF`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`BF_ENCODE`"),
                   Parameter('p3', type=Type.STRING,
                             doc="string to write out")
               ]),

        Method('WriteDataNull_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Writes a null byte (0) to :class:`BF`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle")
               ]),

        Method('WriteInt_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Writes int to the :class:`BF`",
               notes="""
               See comments on byte order for the Read.. functions if you
               want to enforce a certain byte order.
               
               If a byte order is not specified, the data is written
               in the native byte order of the writing computer.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GS_TYPES` and :def:`BF_BYTEORDER`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="data")
               ]),

        Method('WriteReal_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Writes real to the :class:`BF`",
               notes="""
               See comments on byte order for the Read.. functions if you
               want to enforce a certain byte order.
               
               If a byte order is not specified, the data is written
               in the native byte order of the writing computer.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GS_TYPES` and :def:`BF_BYTEORDER`"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="data")
               ]),

        Method('WriteVM_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_cpp=True, 
               doc="Writes :class:`VM` to the :class:`BF`",
               notes="""
               See comments on byte order for the Read.. functions if you
               want to enforce a certain byte order.
               
               If a byte order is not specified, the data is written
               in the native byte order of the writing computer.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GS_TYPES` and :def:`BF_BYTEORDER`"),
                   Parameter('p3', type="VM",
                             doc="data")
               ]),

        Method('WriteVV_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Writes :class:`VV` to the :class:`BF`",
               notes="""
               See comments on byte order for the Read.. functions if you
               want to enforce a certain byte order.
               
               If a byte order is not specified, the data is written
               in the native byte order of the writing computer.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GS_TYPES` and :def:`BF_BYTEORDER`"),
                   Parameter('p3', type="VV",
                             doc="data")
               ])
    ],
    'Obsolete': [

        Method('iCheckFileUNC_BF', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Check if this is UNICODE file.",
               notes="Was not implemented.",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='file name to open ("" is a temporary file)')
               ]),

        Method('IReadString_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Reads string data from current position in :class:`BF`",
               notes="""
               If the data source may be in byte order different from that
               required by the reader, you can add the source byte-order
               to the :class:`BF` elelment type.  The byte order will be swapped
               if required.  For example, to write out a real number 3.5
               with Most-Significant_Byte first (Mortorola) convention:
               
               :func:`WriteReal_BF`(hBF,:def_val:`BF_BYTEORDER_MSB`+:def_val:`GS_REAL`,3.5).
               
               If a byte order is not specified, the source is assumed to be
               in the native byte order of the reading/writing computer.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GS_TYPES` and :def:`BF_BYTEORDER`"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="data"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Length of string to read, NULL will be added so the string length must be at least int+1.")
               ]),

        Method('WriteDataString_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Writes a string of bytes to :class:`BF`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="data string to write (no nulls)")
               ]),

        Method('WriteString_BF', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, is_obsolete=True, 
               doc="Writes string to the :class:`BF`",
               notes="""
               See comments on byte order for the Read.. functions if you
               want to enforce a certain byte order.
               
               If a byte order is not specified, the data is written
               in the native byte order of the writing computer.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`GS_TYPES` and :def:`BF_BYTEORDER`"),
                   Parameter('p3', type=Type.STRING,
                             doc="data")
               ])
    ]
}

