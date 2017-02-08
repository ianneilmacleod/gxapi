from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DBWRITE',
                 doc="""
The :class:`DBWRITE` class is used to open and write to databases. Large blocks of data
  are split into blocks and served up sequentially to prevent the over-use of virtual memory when VVs or VAs are being written to channels.
  Individual data blocks are limited by default to 1 MB (which is user-alterable). Data less than the block size
  are served up whole, one block per line.
""")





gx_methods = {
    'Create Methods': [

        Method('Create_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Create a :class:`DBWRITE` object
               Add channels using the :func:`iAddChannel_DBWRITE`() method.channel.
               """,
               return_type="DBWRITE",
               return_doc=":class:`DBWRITE` object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database input")
               ]),

        Method('CreateXY_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Create a :class:`DBWRITE` object for a XY-located data. Add channels using the
               		               :func:`iAddChannel_DBWRITE`() method.
               """,
               return_type="DBWRITE",
               return_doc=":class:`DBWRITE` object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database input")
               ]),

        Method('CreateXYZ_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="""
               Create a :class:`DBWRITE` object for a XYZ-located data.
               Add channels using the :func:`iAddChannel_DBWRITE`() method.channel
               """,
               return_type="DBWRITE",
               return_doc=":class:`DBWRITE` object",
               parameters = [
                   Parameter('p1', type="DB",
                             doc="Database input")
               ]),

        Method('Destroy_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`DBWRITE` handle.",
               return_type=Type.VOID,
               return_doc="nothing",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle")
               ]),

        Method('iAddChannel_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a data channel to the :class:`DBWRITE` object.",
               return_type=Type.INT32_T,
               return_doc="Channel index. Use for getting the correct :class:`VV` or :class:`VA` object.",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Channel handle (does not need to be locked, but can be.)")
               ])
    ],
    'Data Access Methods': [

        Method('GetDB_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the output :class:`DB` handle from the :class:`DBWRITE` object.",
               return_type="DB",
               return_doc=":class:`DB` handle",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle")
               ]),

        Method('GetVV_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`VV` handle for a channel.",
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index of channel to access.")
               ]),

        Method('GetVA_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the :class:`VA` handle for an array channel.",
               return_type="VA",
               return_doc=":class:`VA` handle",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index of channel to access.")
               ]),

        Method('GetVVx_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the X channel :class:`VV` handle.",
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle")
               ]),

        Method('GetVVy_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Y channel :class:`VV` handle.",
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle")
               ]),

        Method('GetVVz_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the Z channel :class:`VV` handle.",
               return_type="VV",
               return_doc=":class:`VV` handle",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle")
               ]),

        Method('iGetChanArraySize_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Get the number of columns of data in a channel.",
               return_type=Type.INT32_T,
               return_doc="The number of columns (array size) for a channel",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Index of channel to access.")
               ])
    ],
    'Processing': [

        Method('AddBlock_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Add the current block of data.",
               return_type=Type.VOID,
               return_doc="nothing",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle"),
                   Parameter('p2', type="DB_SYMB",
                             doc="Line")
               ]),

        Method('Commit_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Commit remaining data to the database.",
               return_type=Type.VOID,
               return_doc="nothing",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle")
               ]),

        Method('TestFunc_DBWRITE', module='geoengine.core', version='9.0.0',
               availability=Availability.PUBLIC, 
               doc="Temporary test function.",
               return_type=Type.VOID,
               return_doc="nothing",
               parameters = [
                   Parameter('p1', type="DBWRITE",
                             doc=":class:`DBWRITE` handle"),
                   Parameter('p2', type="RA",
                             doc=":class:`RA` handle to text file to import.")
               ])
    ]
}

