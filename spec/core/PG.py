from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('PG',
                 doc="""
                 Pager methods for large 2-D arrays
                 This class handles very-large 2-D arrays in which efficient
                 access is required along both rows and columns.
                 """,
                 notes="""
                 Typically a grid is accessed using the :class:`IMG` class, and a :class:`PG`
                 is obtained from the :class:`IMG` using the :func:`GetPG_IMG` function.
                 Following operations on the :class:`PG`, it can be written back to
                 the :class:`IMG` using :func:`SetPG_IMG`.
                 """)


gx_defines = [
    Define('PG_3D_DIR',
           doc="3D Pager direction",
           constants=[
               Constant('PG_3D_DIR_XYZ', value='0', type=Type.INT32_T)                        ,
               Constant('PG_3D_DIR_YXZ', value='1', type=Type.INT32_T)                        ,
               Constant('PG_3D_DIR_XZY', value='2', type=Type.INT32_T)                        ,
               Constant('PG_3D_DIR_YZX', value='3', type=Type.INT32_T)                        ,
               Constant('PG_3D_DIR_ZXY', value='4', type=Type.INT32_T)                        ,
               Constant('PG_3D_DIR_ZYX', value='5', type=Type.INT32_T)                        
           ]),

    Define('PG_BF_CONV',
           doc="Pager binary conversions",
           constants=[
               Constant('PG_BF_CONV_NONE', value='0', type=Type.INT32_T,
                        doc="The Data is in Raw form")                        ,
               Constant('PG_BF_CONV_SWAP', value='1', type=Type.INT32_T,
                        doc="The data needs to be byte swapped")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Math_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Do math to a pager",
               return_type=Type.INT32_T,
               return_doc="Always 0",
               parameters = [
                   Parameter('p1', type="PG",
                             doc="First Pager"),
                   Parameter('p2', type="PG",
                             doc="Second Pager"),
                   Parameter('p3', type="PG",
                             doc="Result Pager"),
                   Parameter('p4', type="void*",
                             doc="Pointer to pass to your function"),
                   Parameter('p5', type="void (_cdecl *param4)(void*,short,long,void*,void*,void*)",
                             doc="Math Functions (void (cdecl*)(void *pInfo, short sType, long lItems, void *pPG1, void *pPG2, void *pPGR)"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="GS_BOOL SMP Support")
               ]),

        Method('ReadColMem_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Read a set of elements in X (column) from pager directly into memory",
               return_type=Type.INT32_T,
               return_doc="Always 0",
               parameters = [
                   Parameter('p1', type="PG",
                             doc="First Pager"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Column"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="First Element"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Number of Elements"),
                   Parameter('p5', type="void*",
                             doc="Data buffer to read into")
               ]),

        Method('WriteColMem_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Write a set of elements in X (column) to pager directly from memory",
               return_type=Type.INT32_T,
               return_doc="Always 0",
               parameters = [
                   Parameter('p1', type="PG",
                             doc="First Pager"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Column"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="First Element"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Number of Elements"),
                   Parameter('p5', type="const void*",
                             doc="Data buffer to read from")
               ]),

        Method('ReadRowMem_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Read a set of elements in Y (row) from pager directly into memory",
               return_type=Type.INT32_T,
               return_doc="Always 0",
               parameters = [
                   Parameter('p1', type="PG",
                             doc="First Pager"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Row"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="First Element"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Number of Elements"),
                   Parameter('p5', type="void*",
                             doc="Data buffer to read into")
               ]),

        Method('WriteRowMem_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, no_gxh=True, no_csharp=True, no_cpp=True, 
               doc="Write a set of elements in Y (row) to pager directly from memory",
               return_type=Type.INT32_T,
               return_doc="Always 0",
               parameters = [
                   Parameter('p1', type="PG",
                             doc="First Pager"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Row"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="First Element"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Number of Elements"),
                   Parameter('p5', type="const void*",
                             doc="Data buffer to read from")
               ])
    ],
    '2D Methods': [

        Method('Copy_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Copy the data from one pager to another.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Destination :class:`PG` object"),
                   Parameter('p2', type="PG",
                             doc="Source :class:`PG` object")
               ]),

        Method('CopySubset_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Copy a subset of data from one pager to another.",
               notes="2D Only",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Destination :class:`PG` object"),
                   Parameter('p2', type="PG",
                             doc="Source :class:`PG` object"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Y (row) Origin on destination"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="X (col) Origin on destination"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Y (row) Origin on source"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="X (col) Origin on source"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Number of Y (rows) to copy"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="Number of X (columns) to copy")
               ]),

        Method('Create_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Creates a Pager object",
               return_type="PG",
               return_doc=":class:`PG` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="# elements in y (# of row)"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="# elements in x (# of column)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`")
               ]),

        Method('CreateS_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create a 2D :class:`PG` from serialized source.",
               notes="For 3D pagers, use CreateBF_PG.",
               return_type="PG",
               return_doc=":class:`PG` Object",
               parameters = [
                   Parameter('p1', type="BF")
               ]),

        Method('Destroy_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a table resource.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Pager Object to Destroy")
               ]),

        Method('Dummy_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Sets the Entire pager to dummy.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc=":class:`PG` object")
               ]),

        Method('iEType_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Gets the type of pager.",
               return_type=Type.INT32_T,
               return_doc=":def:`GS_TYPES`",
               parameters = [
                   Parameter('p1', type="PG",
                             doc="source :class:`PG`")
               ]),

        Method('iNCols_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Gets the # of columns in pager.",
               return_type=Type.INT32_T,
               return_doc="# of columns.",
               parameters = [
                   Parameter('p1', type="PG",
                             doc="source :class:`PG`")
               ]),

        Method('iNRows_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Gets the # of rows in pager.",
               return_type=Type.INT32_T,
               return_doc="# of rows.",
               parameters = [
                   Parameter('p1', type="PG",
                             doc="source :class:`PG`")
               ]),

        Method('iNSlices_PG', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Gets the # of slices (z) in pager.",
               return_type=Type.INT32_T,
               return_doc="# of rows.",
               parameters = [
                   Parameter('p1', type="PG",
                             doc="source :class:`PG`")
               ]),

        Method('Range_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Computes the range of the entire pager.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Pager to Range"),
                   Parameter('p2', type=Type.DOUBLE, is_ref=True,
                             doc="Minimum Data (Dummy if no range)"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Maximum Data (Dummy if no range)")
               ]),

        Method('rGet_PG', module='geoengine.core', version='8.3.0',
               availability=Availability.LICENSED, 
               doc="Read a single value from a 2D :class:`PG`",
               notes="This is a low-performance method.",
               return_type=Type.DOUBLE,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="iBx - element # in x (column #)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="iBy - element # in y (row #)")
               ]),

        Method('ReadCol_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Read a set of elements in X (column) from pager into vv",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="iBx - element # in x (column #)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="iBy - begining element # in y to read (0 is the first)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="iNy - # elements to read (0 for whole vector)"),
                   Parameter('p5', type="VV",
                             doc="hVV - :class:`VV` handle")
               ]),

        Method('ReadRow_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Read a set of elements in Y (row) from pager into vv",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="iBy - element # in y (row #)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="iBx - begining element # in x to read (0 is the first)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="iNx - # elements to read (0 for whole vector)"),
                   Parameter('p5', type="VV",
                             doc="hVV - :class:`VV` handle")
               ]),

        Method('ReAllocate_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Changes the size of Pager",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc=":class:`PG` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Number of Y (rows) to reallocate"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Number of X (columns) to reallocate")
               ]),

        Method('Serial_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Serialize a 2D :class:`PG` to a :class:`BF`.",
               notes="For 3D pagers, use :func:`WriteBF_PG`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG"),
                   Parameter('p2', type="BF")
               ]),

        Method('Statistics_PG', module='geoengine.core', version='6.3.1',
               availability=Availability.LICENSED, 
               doc="Compute the statistics of a pager object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type="ST",
                             doc="hST - statistics object")
               ]),

        Method('WriteCol_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Write a set of elements in X (column) from vv into pager",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="iBx - element # in x (column #)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="iBy - begining element # in y to write (0 is the first)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="iNy - # elements to write (0 for whole vector)"),
                   Parameter('p5', type="VV",
                             doc="hVV - :class:`VV` handle")
               ]),

        Method('WriteRow_PG', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Write a set of elements in Y (row) from vv into pager",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="iBy - element # in y (row #)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="iBx - begining element # in x to write (0 is the first)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="iNx - # elements to write (0 for whole vector)"),
                   Parameter('p5', type="VV",
                             doc="hVV - :class:`VV` handle")
               ])
    ],
    '3D Methods': [

        Method('CopySubset3D_PG', module='geoengine.core', version='8.0.0',
               availability=Availability.LICENSED, 
               doc="Copy a subset of data from one pager to another.",
               notes="2D Only",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="Destination :class:`PG` object"),
                   Parameter('p2', type="PG",
                             doc="Source :class:`PG` object"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Z (slice) Origin on destination"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Y (row) Origin on destination"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="X (col) Origin on destination"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Z (slice) Origin on source"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Y (row) Origin on source"),
                   Parameter('p8', type=Type.INT32_T,
                             doc="X (col) Origin on source"),
                   Parameter('p9', type=Type.INT32_T,
                             doc="Number of Z (slice) to copy"),
                   Parameter('p10', type=Type.INT32_T,
                             doc="Number of Y (rows) to copy"),
                   Parameter('p11', type=Type.INT32_T,
                             doc="Number of X (columns) to copy")
               ]),

        Method('Create3D_PG', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Creates a Pager object",
               return_type="PG",
               return_doc=":class:`PG` Object",
               parameters = [
                   Parameter('p1', type=Type.INT32_T,
                             doc="# elements in z (# of slices)"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="# elements in y (# of row)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="# elements in x (# of column)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`GS_TYPES`")
               ]),

        Method('ReadCol3D_PG', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Read a set of elements in X (column) from pager into vv",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="iBz - element # in z (slice #)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="iBx - element # in x (column #)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="iBy - begining element # in y to read (0 is the first)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="iNy - # elements to read (0 for whole vector)"),
                   Parameter('p6', type="VV",
                             doc="hVV - :class:`VV` handle")
               ]),

        Method('ReadRow3D_PG', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Read a set of elements in Y (row) from pager into vv",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="iBz - element # in z (slice #)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="iBy - element # in y (row #)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="iBx - begining element # in x to read (0 is the first)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="iNx - # elements to read (0 for whole vector)"),
                   Parameter('p6', type="VV",
                             doc="hVV - :class:`VV` handle")
               ]),

        Method('ReadTrace3D_PG', module='geoengine.core', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Read a set of elements in Z (trace) from pager into vv",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="iBx - element # in x (column #)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="iBy - element # in y (row #)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="iBy - begining element # in z to read (0 is the first)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="iNy - # elements to read (0 for whole vector)"),
                   Parameter('p6', type="VV",
                             doc="hVV - :class:`VV` handle")
               ]),

        Method('ReAllocate3D_PG', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Changes the size of 3D Pager",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc=":class:`PG` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Number of Z (slices) to reallocate"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Number of Y (rows) to reallocate"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Number of X (columns) to reallocate")
               ]),

        Method('WriteCol3D_PG', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Write a set of elements in X (column) from vv into pager",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="iBz - element # in z (slice #)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="iBx - element # in x (column #)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="iBy - begining element # in y to write (0 is the first)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="iNy - # elements to write (0 for whole vector)"),
                   Parameter('p6', type="VV",
                             doc="hVV - :class:`VV` handle")
               ]),

        Method('WriteRow3D_PG', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Write a set of elements in Y (row) from vv into pager",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="iBz - element # in z (slice #)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="iBy - element # in y (row #)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="iBx - begining element # in x to write (0 is the first)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="iNx - # elements to write (0 for whole vector)"),
                   Parameter('p6', type="VV",
                             doc="hVV - :class:`VV` handle")
               ]),

        Method('WriteTrace3D_PG', module='geoengine.core', version='6.3.0',
               availability=Availability.LICENSED, 
               doc="Write a set of elements in Z (trace) from pager into vv",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="hPG - :class:`PG` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="iBx - element # in x (column #)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="iBy - element # in y (row #)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="iBy - begining element # in z to read (0 is the first)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="iNy - # elements to read (0 for whole vector)"),
                   Parameter('p6', type="VV",
                             doc="hVV - :class:`VV` handle")
               ])
    ],
    'Utility Methods': [

        Method('ReadBF_PG', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Read the contents of a 2D or 3D pager to from a :class:`BF`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc=":class:`PG` handle"),
                   Parameter('p2', type="BF",
                             doc=":class:`BF` to read from"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`PG_3D_DIR`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`PG_BF_CONV`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Reverse X"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Reverse Y"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Reverse Z")
               ]),

        Method('ReadRA_PG', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Read the contents of a 2D or 3D pager to from an :class:`RA`.",
               notes="Each line must hold only 1 value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc=":class:`PG` handle"),
                   Parameter('p2', type="RA",
                             doc=":class:`RA` to read from"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`PG_3D_DIR`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Reverse X"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Reverse Y"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Reverse Z"),
                   Parameter('p7', type=Type.STRING,
                             doc="Dummy")
               ]),

        Method('WriteBF_PG', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Write the contents of a 2D or 3D pager to a :class:`BF`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc=":class:`PG` handle"),
                   Parameter('p2', type="BF",
                             doc=":class:`BF` to write to"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`PG_3D_DIR`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`PG_BF_CONV`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Reverse X"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Reverse Y"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Reverse Z")
               ]),

        Method('WriteWA_PG', module='geoengine.core', version='6.2.0',
               availability=Availability.LICENSED, 
               doc="Write the contents of a 2D or 3D pager to a :class:`WA`",
               notes="Each line will hold only 1 value",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc=":class:`PG` handle"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` to write to"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`PG_3D_DIR`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Reverse X"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Reverse Y"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="Reverse Z"),
                   Parameter('p7', type=Type.STRING,
                             doc="Dummy")
               ])
    ],
    'Miscellaneous': [

    ]
}

