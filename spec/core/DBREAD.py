from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DBREAD',
                 doc="""
The :class:`DBREAD` class is used to open and read from databases. Very large lines
  are split into blocks and served up sequentially to prevent the over-use of virtual memory when channels are read into VVs or VAs.
  Individual data blocks are limited by default to 1 MB (which is user-alterable). Single lines smaller than the block size
  are served up whole, one block per line.
""")





gx_methods = {
    'Create Methods': [

        Method('Create_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="""
               Create a :class:`DBREAD` object
               Add channels using the :func:`iAddChannel_DBREAD`() method.channel.
               """,
               return_type="DBREAD",
               return_doc=":class:`DBREAD` object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database input"),
                   Parameter('p2', type="LST",
                             doc="list of lines to process NAME = line name, VALUE = line symbol")
               ]),

        Method('CreateXY_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="""
               Create a :class:`DBREAD` object for a XY-located data. Add channels using the
               		               :func:`iAddChannel_DBREAD`() method.
               """,
               return_type="DBREAD",
               return_doc=":class:`DBREAD` object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database input"),
                   Parameter('p2', type="LST",
                             doc="list of lines to process NAME = line name, VALUE = line symbol")
               ]),

        Method('CreateXYZ_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="""
               Create a :class:`DBREAD` object for a XYZ-located data.
               Add channels using the :func:`iAddChannel_DBREAD`() method.channel
               """,
               return_type="DBREAD",
               return_doc=":class:`DBREAD` object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database input"),
                   Parameter('p2', type="LST",
                             doc="list of lines to process NAME = line name, VALUE = line symbol")
               ]),

        Method('Destroy_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`DBREAD` handle.",
               return_type=Type.VOID,
               return_doc="nothing",
               parameters = [
                   Parameter('p1', type="DBREAD",
                             doc=":class:`DBREAD` handle")
               ]),

        Method('iAddChannel_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Add a data channel to the :class:`DBREAD` object.",
               return_type=Type.INT32_T,
               return_doc="Channel index. Use for getting the correct :class:`VV` or :class:`VA` object.",
               parameters = [
                   Parameter('p1', type="DBREAD",
                             doc=":class:`DBREAD` handle"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle (does not need to be locked, but can be.)")
               ])
    ],
    'Data Access Methods': [

        Method('GetVV_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`VV` handle for a channel.",
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('p1', type="DBREAD",
                             doc=":class:`DBREAD` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index of channel to access.")
               ]),

        Method('GetVA_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`VA` handle for an array channel.",
               return_type="VA",
               return_doc=":class:`VA` handle",
               parameters = [
                   Parameter('p1', type="DBREAD",
                             doc=":class:`DBREAD` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index of channel to access.")
               ]),

        Method('GetVVx_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the X channel :class:`VV` handle.",
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('p1', type="DBREAD",
                             doc=":class:`DBREAD` handle")
               ]),

        Method('GetVVy_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the Y channel :class:`VV` handle.",
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('p1', type="DBREAD",
                             doc=":class:`DBREAD` handle")
               ]),

        Method('GetVVz_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the Z channel :class:`VV` handle.",
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('p1', type="DBREAD",
                             doc=":class:`DBREAD` handle")
               ]),

        Method('iGetChanArraySize_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of columns of data in a channel.",
               return_type=Type.INT32_T,
               return_doc="The number of columns (array size) for a channel",
               parameters = [
                   Parameter('p1', type="DBREAD",
                             doc=":class:`DBREAD` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index of channel to access.")
               ]),

        Method('iGetNumberOfBlocksToProcess_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of blocks to be served up.",
               return_type=Type.INT32_T,
               return_doc="The number of blocks to process in the selected lines.",
               parameters = [
                   Parameter('p1', type="DBREAD",
                             doc=":class:`DBREAD` handle")
               ])
    ],
    'Processing': [

        Method('iGetNextBlock_DBREAD', module='geoengine.core', version='8.5.0',
               availability=Availability.PUBLIC, 
               doc="Get the next block of data.",
               return_type=Type.INT32_T,
               return_doc="Returns the current block index, or -1 if at end of file (no new data returned).",
               parameters = [
                   Parameter('p1', type="DBREAD",
                             doc=":class:`DBREAD` handle"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="(returned) The index into the input selected line list of the line whose data is contained in the current block"),
                   Parameter('p3', type=Type.INT32_T, is_ref=True,
                             doc="(returned) The block index (0 to NBlocks-1) for the current line of data."),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="(returned) The number of blocks that the current line is split into.")
               ])
    ]
}

