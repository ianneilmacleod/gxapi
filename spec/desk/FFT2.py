from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('FFT2',
                 doc="""
2-D Fast Fourier Transforms
These methods now work with an :class:`IMG` object, instead of creating
their own :class:`FFT2` object.
""")


gx_defines = [
    Define('FFT2_PG',
           doc="Pager Direction",
           constants=[
               Constant('FFT2_PG_FORWARD', value='0', type=Type.INT32_T)                        ,
               Constant('FFT2_PG_INVERSE', value='1', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Fft2In_FFT2', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc=":class:`FFT2` transform",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input image"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output Transform file name string"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output Power Spectrum file name string")
               ]),

        Method('FilterPG_FFT2', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Apply 2D :class:`FFT` filters to data in pager",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="pager obj"),
                   Parameter('p2', type=Type.STRING,
                             doc="sConFil - :class:`FFT` filter control file"),
                   Parameter('p3', type="TR",
                             doc=":class:`TR` obj"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="rDx - X increment"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="rDy - Y increment"),
                   Parameter('p6', type=Type.DOUBLE,
                             doc="rRot- Rotation degree")
               ]),

        Method('Flt_FFT2', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc=":class:`FFT2` filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input image (Transform grid)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output file (Transform grid)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Control file")
               ]),

        Method('FltInv_FFT2', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc=":class:`FFT2` filter and inverse",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input image (Transform grid)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output file"),
                   Parameter('p3', type=Type.STRING,
                             doc="Control file")
               ]),

        Method('PowSpc_FFT2', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc=":class:`FFT2` transform power spectrum",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input image (Transform grid)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output Power Spectrum file name string")
               ]),

        Method('RadSpc_FFT2', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc=":class:`FFT2` transform Radially averaged power spectrum",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input image (Transform grid)"),
                   Parameter('p2', type=Type.STRING,
                             doc="Output Radial Spectrum file name string")
               ]),

        Method('RadSpc1_FFT2', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc=":class:`FFT2` transform Radially averaged power spectrum for one :class:`IMG`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input image (Transform grid)"),
                   Parameter('p2', type="VV",
                             doc="Output Radial Spectrum :class:`VV`")
               ]),

        Method('RadSpc2_FFT2', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc=":class:`FFT2` transform Radially averaged power spectrum for two IMGs",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input image1 (Transform grid1 - G)"),
                   Parameter('p2', type="IMG",
                             doc="Input image2 (Transform grid2 - H)"),
                   Parameter('p3', type="VV",
                             doc="Output Radial Spectrum :class:`VV`"),
                   Parameter('p4', type="VV",
                             doc="Output Radial Spectrum Standard deviation VVst	(Null: no calc)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="lOpt - 1: <Re(GH*/HH*)> :class:`VV`;  0: <Re(GH*)> :class:`VV`")
               ]),

        Method('TdXdY_FFT2', module='geogxx', version='5.0.1',
               availability=Availability.EXTENSION, 
               doc=":class:`FFT2` filter (calculate T from the derivatives Tx and Ty)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="IMG",
                             doc="Input dX image (Transform grid)"),
                   Parameter('p2', type="IMG",
                             doc="Input dY image (Transform grid)"),
                   Parameter('p3', type=Type.STRING,
                             doc="Output T file name"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="0 - no invers, 1 - invers :class:`FFT` applied")
               ]),

        Method('TransPG_FFT2', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Apply 2D :class:`FFT` transform to data in pager",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="PG",
                             doc="pager obj"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`FFT2_PG`")
               ])
    ]
}

