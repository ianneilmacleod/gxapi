from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('FFT',
                 doc="""
This class allows for the application of predefined
filters to data in an OASIS database. The system uses
the Winograd algorithm to transform data in the spatial
domain to the wavenumber or Fourier domain.
""")


gx_defines = [
    Define('FFT_DETREND',
           doc="Detrending option",
           constants=[
               Constant('FFT_DETREND_NONE', value='0', type=Type.INT32_T,
                        doc="no trend remove")                        ,
               Constant('FFT_DETREND_ENDS', value='1', type=Type.INT32_T,
                        doc="detrend order 1 using only two end points")                        ,
               Constant('FFT_DETREND_ALL', value='2', type=Type.INT32_T,
                        doc="detrend order 1 using all data points")                        ,
               Constant('FFT_DETREND_MEAN', value='3', type=Type.INT32_T,
                        doc="remove mean value")                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AppDens_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Appparent density filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Thickness (meters) of the earth model"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Background density (g/cm3) (default = 0)")
               ]),

        Method('AppSusc_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Apparent susceptiblity filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Total magnetic field strength")
               ]),

        Method('BandPass_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Bandpass filter (using low and high wavelength cutoffs)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Low Cutoff wavelength (meters)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="High Cutoff wavelength (meter)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="1= Pass the defined band (default); 0= Reject the band")
               ]),

        Method('BWorth_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Butterworth filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Central cutoff wavelength (meter)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Degree of the filter function (default = 8.0)"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Filter type: 1= Low-pass (regional) filter (default) 0= High-pass (residual) filter")
               ]),

        Method('RCFilter_FFT', module='geogxx', version='8.5.0',
               availability=Availability.EXTENSION, 
               doc="RC filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Central cutoff wavelength (meter)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Filter type: 1= Low-pass (regional) filter (default) 0= High-pass (residual) filter")
               ]),

        Method('Contin_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Upward/Downward continuation filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Distance to continue; positive = downwards negative = upwards")
               ]),

        Method('CosRoll_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Cosine roll-off filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Low wavelength start point (meters)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="High wavelength end point (meters)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Degree of the filter function (default = 2.0)"),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Filter type: 1= Low-pass (regional) filter (default) 0= High-pass (residual) filter")
               ]),

        Method('Create_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Create a New :class:`FFT` with detrend options.",
               return_type="FFT",
               return_doc=":class:`FFT` Object",
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` to transform."),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Element space interval"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`FFT_DETREND`")
               ]),

        Method('CreateEx_FFT', module='geogxx', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="Create a New :class:`FFT` with detrend and expansion options.",
               return_type="FFT",
               return_doc=":class:`FFT` Object",
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` to transform."),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Element space interval"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`FFT_DETREND`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="minimum expansion %")
               ]),

        Method('CreateRef_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="""
               Create :class:`FFT` object with detrend options from reference (original) channel,
               but no :class:`FFT` process.
               """,
               return_type="FFT",
               return_doc=":class:`FFT` Object",
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` contains channel data to perform :class:`FFT` operations upon."),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Element space interval, should be the same as in Create(Ex)_FFT() call"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`FFT_DETREND`")
               ]),

        Method('CreateRefEx_FFT', module='geogxx', version='5.1.8',
               availability=Availability.EXTENSION, 
               doc="""
               Create :class:`FFT` object with detrend and expansion options from reference (original) channel,
               but no :class:`FFT` process.
               """,
               return_type="FFT",
               return_doc=":class:`FFT` Object",
               parameters = [
                   Parameter('p1', type="VV",
                             doc=":class:`VV` contains channel data to perform :class:`FFT` operations upon."),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Element space interval, should be the same as in Create(Ex)_FFT() call"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`FFT_DETREND`"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="minimum expansion %, should be the same as in :func:`CreateEx_FFT`() call"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="DC level multiple")
               ]),

        Method('Destroy_FFT', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy an :class:`FFT`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to destroy.")
               ]),

        Method('Gaus_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Gaussian filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Standard deviation cutoff of function (meters)"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Filter type: 1= Low-pass (residual) filter (default) 0= High-pass (regional) filter")
               ]),

        Method('GetVV_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Copies real and imaginary :class:`VV`'s to user :class:`VV`'s.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT"),
                   Parameter('p2', type="VV",
                             doc="real component"),
                   Parameter('p3', type="VV",
                             doc="imaginary component")
               ]),

        Method('HDrv_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Horizontal derivative",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Order of differentiation (default = 1)")
               ]),

        Method('HighPass_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="High bandpass filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Cutoff wavelength (meter)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Fiducial increment of the :class:`FFT`'s channel data")
               ]),

        Method('HInt_FFT', module='geogxx', version='5.1.4',
               availability=Availability.EXTENSION, 
               doc="Horizontal integration",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to integrate")
               ]),

        Method('Inverse_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Inverse the :class:`FFT` from wave number domain to space domain",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to invert"),
                   Parameter('p2', type="VV",
                             doc="Output :class:`VV`"),
                   Parameter('p3', type="VV",
                             doc="Original :class:`VV` which was used to create :class:`FFT` (will be used as mask for output :class:`VV`; no masking if this parameter is NULL)")
               ]),

        Method('LowPass_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Low bandpass filter",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Cutoff wavelength (meters)")
               ]),

        Method('RedPol_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Reduction to magnetic pole",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Geomagnetic inclination (degrees)"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Geomagnetic declination (degrees)"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Inclination (degrees) for amplitude correction (default = 20.0)"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Direction (degrees) of Line from North")
               ]),

        Method('rNyquist_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Gets the Nyquist frequency (wavenumbers/sample unit).",
               return_type=Type.DOUBLE,
               return_doc="Nyquist frequency (wavenumbers/sample unit).",
               parameters = [
                   Parameter('p1', type="FFT")
               ]),

        Method('rSampIncr_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Gets the original sample increment.",
               return_type=Type.DOUBLE,
               return_doc="Original sample increment.",
               parameters = [
                   Parameter('p1', type="FFT")
               ]),

        Method('rWaveIncr_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Get the wave number increment.",
               return_type=Type.DOUBLE,
               return_doc="Wave number increment",
               parameters = [
                   Parameter('p1', type="FFT")
               ]),

        Method('SetVV_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Sets real and imaginary VVs in :class:`FFT`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT"),
                   Parameter('p2', type="VV",
                             doc="real component"),
                   Parameter('p3', type="VV",
                             doc="imaginary component")
               ]),

        Method('Spectrum_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Calculates a power spectrum",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to calculate power spectrum for"),
                   Parameter('p2', type="VV",
                             doc="Output power spectrum :class:`VV`")
               ]),

        Method('VDrv_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Vertical derivative",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to filter"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Order of differentiation (default = 1)")
               ]),

        Method('VInt_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Vertical integration",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` to integrate")
               ]),

        Method('WriteSpectrum_FFT', module='geogxx', version='5.0.0',
               availability=Availability.EXTENSION, 
               doc="Writes a power spectrum to a file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FFT",
                             doc=":class:`FFT` used to calculate power spectrum :class:`VV`"),
                   Parameter('p2', type="VV",
                             doc="Output power spectrum :class:`VV`"),
                   Parameter('p3', type=Type.STRING,
                             doc="File name for output spectrum")
               ])
    ]
}

