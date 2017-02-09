from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('ST',
                 doc="""
                 Mono-variate statistics. The :class:`ST` class is used to accumulate statistical
                 information about a set of data. This class is usually used in conjunction
                 with others. For instance, :func:`Stat_DU` (see :class:`DU`) will add a channel's
                 data to the :class:`ST` object, and sComputeST_IMG (see :class:`IMG`) will compute
                 statistics for a grid.
                 """,
                 notes="""
                 *** Histogram ranges and colour zone ranges ***
                 
                 Histogram bins are defined with inclusive minima and exclusive maxima;
                 for instance if Min = 0 and Inc = 1, then the second bin would include
                 all values z such that  0 >= z > 1 (the first bin has all values < 0).
                 
                 Colour zones used in displaying grids (:class:`ITR`, ZON etc...) are the
                 opposite, with exclusive minima and inclusive maxima.
                 For instance, if a zone is defined from 0 to 1, then it would
                 contain all values of z such that 0 > z >= 1.
                 
                 These definitions mean that it is impossible to perfectly assign
                 :class:`ITR` colours to individual bars of a histogram. The best work-around
                 when the data values are integers is to define the colour zones using
                 0.5 values between the integers. A general work-around is to make the
                 number of histogram bins much larger than the number of colour zones.
                 
                 See also  :class:`ST2` (bi-variate statistics)
                 """)


gx_defines = [
    Define('ST_INFO',
           doc="Information to retrieve",
           constants=[
               Constant('ST_ITEMS', value='0', type=Type.INT32_T,
                        doc="Number of non-dummy items")                        ,
               Constant('ST_NPOS', value='1', type=Type.INT32_T,
                        doc="Number of items greater than zero")                        ,
               Constant('ST_NZERO', value='22', type=Type.INT32_T,
                        doc="Number of items equal to zero")                        ,
               Constant('ST_DUMMIES', value='2', type=Type.INT32_T)                        ,
               Constant('ST_MIN', value='3', type=Type.INT32_T)                        ,
               Constant('ST_MAX', value='4', type=Type.INT32_T)                        ,
               Constant('ST_RANGE', value='5', type=Type.INT32_T)                        ,
               Constant('ST_MEAN', value='6', type=Type.INT32_T)                        ,
               Constant('ST_MEDIAN', value='7', type=Type.INT32_T)                        ,
               Constant('ST_MODE', value='8', type=Type.INT32_T)                        ,
               Constant('ST_GEOMEAN', value='9', type=Type.INT32_T)                        ,
               Constant('ST_VARIANCE', value='10', type=Type.INT32_T)                        ,
               Constant('ST_STDDEV', value='11', type=Type.INT32_T)                        ,
               Constant('ST_STDERR', value='12', type=Type.INT32_T)                        ,
               Constant('ST_SKEW', value='13', type=Type.INT32_T)                        ,
               Constant('ST_KURTOSIS', value='14', type=Type.INT32_T)                        ,
               Constant('ST_BASE', value='15', type=Type.INT32_T)                        ,
               Constant('ST_SUM', value='16', type=Type.INT32_T,
                        doc="Sums and sums of powers")                        ,
               Constant('ST_SUM2', value='17', type=Type.INT32_T)                        ,
               Constant('ST_SUM3', value='18', type=Type.INT32_T)                        ,
               Constant('ST_SUM4', value='19', type=Type.INT32_T)                        ,
               Constant('ST_MINPOS', value='21', type=Type.INT32_T,
                        doc="Smallest value greater than zero.")                        ,
               Constant('ST_HIST_MAXCOUNT', value='100', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_ST', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               This method creates a statistics object which is used to
               accumulate statistics.
               """,
               return_type="ST",
               return_doc=":class:`ST` Object"),

        Method('CreateExact_ST', module='geoengine.core', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="""
               This method creates a statistics object which stores
               all values.
               """,
               return_type="ST",
               return_doc=":class:`ST` Object"),

        Method('Data_ST', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Add this value to the statistics object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST",
                             doc=":class:`ST` Handle"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Value to Add")
               ]),

        Method('DataVV_ST', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Add all the values in this :class:`VV` to the statistics object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST",
                             doc=":class:`ST` object"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` object")
               ]),

        Method('Destroy_ST', module='geoengine.core', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys the statistics object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST",
                             doc=":class:`ST` Handle")
               ]),

        Method('GetHistogramBins_ST', module='geoengine.core', version='6.1.0',
               availability=Availability.LICENSED, 
               doc="Retrieve number of items in each hostogram bin",
               notes="""
               The length of the returned :class:`VV` is set to the total
               number of bins. If a histogram is not defined in
               the :class:`ST`, then the returned length is zero.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST",
                             doc=":class:`ST` Handle"),
                   Parameter('p2', type="VV",
                             doc=":class:`VV` for numbers of items")
               ]),

        Method('GetHistogramInfo_ST', module='geoengine.core', version='6.1.0',
               availability=Availability.LICENSED, 
               doc="Retrieve number of bins, min and max value in histogram",
               notes="""
               The items correspond to those in :func:`Histogram2_ST`.
               If a histogram is not defined in
               the :class:`ST`, then the returned number of bins is zero, and
               the min and max values will be dummies.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST",
                             doc=":class:`ST` Handle"),
                   Parameter('p2', type=Type.INT32_T, is_ref=True,
                             doc="# of bins"),
                   Parameter('p3', type=Type.DOUBLE, is_ref=True,
                             doc="Min (value at start of 2nd bin)"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Max (value at end of 2nd last bin)")
               ]),

        Method('Histogram_ST', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="This method prepares :class:`ST` for recording histogram.",
               notes="""
               The Number of bins includes the one before the minimum
               and the one after the maximum, so it must be a value >2.
               
               IMPORTANT: This function gets the histogram minimum and
               maximum from the current min and max values stored in the :class:`ST`,
               so this is equivalent to calling
               
               :func:`Histogram2_ST`( #bins, Min, (Max-Min)/(# bins -2));
               
               You should already have the data loaded in order to call this
               function.
               
               See the note above "Histogram ranges and colour zone ranges"
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST",
                             doc=":class:`ST` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="# of bins")
               ]),

        Method('Histogram2_ST', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="This method prepares :class:`ST` for recording histogram.",
               notes="""
               The Number of bins includes the one before the minimum
               and the one after the maximum, so it must be a value >2.
               The width of the individual bins will be (Min-Max)/(# - 2)
               
               See the note above "Histogram ranges and colour zone ranges"
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST",
                             doc=":class:`ST` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="# of bins"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Max")
               ]),

        Method('rEquivalentPercentile_ST', module='geoengine.core', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Return corresponding Percentile for a Value.",
               notes="""
               Statistics and histogram must have been calculated prior to
               calling this method
               """,
               return_type=Type.DOUBLE,
               return_doc="The percentile at the given value (0 - 100)",
               parameters = [
                   Parameter('p1', type="ST"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="input value")
               ]),

        Method('rEquivalentValue_ST', module='geoengine.core', version='5.0.8',
               availability=Availability.LICENSED, 
               doc="Return corresponding Value for a Percentile",
               notes="""
               Statistics and histogram must have been calculated prior to
               calling this method
               """,
               return_type=Type.DOUBLE,
               return_doc="The value at the given percentile.",
               parameters = [
                   Parameter('p1', type="ST"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="input percentile (0 - 100)")
               ]),

        Method('Reset_ST', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Resets the Statistics.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ST",
                             doc=":class:`ST` Handle")
               ]),

        Method('rGetInfo_ST', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="""
               This method allows you to retrieve (and compute) the
               information from the :class:`ST` object.
               """,
               notes="""
               The following can only be determined if the :class:`ST` has recorded
               a histogram: :def_val:`ST_MEDIAN`, :def_val:`ST_MODE`
               
               :def_val:`ST_MINPOS` can be used to retrieve the smallest value greater
               than zero, but not from :class:`ST` objects recovered from serialized object.
               """,
               return_type=Type.DOUBLE,
               return_doc="""
               Data you asked for
               :def_val:`GS_R8DM` for none
               """,
               parameters = [
                   Parameter('p1', type="ST",
                             doc=":class:`ST` Handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`ST_INFO`")
               ]),

        Method('rGetNormProb_ST', module='geoengine.core', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="return percent value",
               return_type=Type.DOUBLE,
               return_doc="""
               real
               
               
               Notes			this function is based on Normal Cumulative distribution function
               mit to about 5 standard deviations
               """,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE)
               ]),

        Method('rGetNormProbX_ST', module='geoengine.core', version='7.1.0',
               availability=Availability.LICENSED, 
               doc="Return number of sigmas from 50% a given percent is",
               return_type=Type.DOUBLE,
               return_doc="""
               real
               
               
               Notes			this function is based on Normal Cumulative distribution function
               mit to about 5 standard deviations
               """,
               parameters = [
                   Parameter('p1', type=Type.DOUBLE)
               ]),

        Method('rNormalTest_ST', module='geoengine.core', version='5.0.0',
               availability=Availability.LICENSED, 
               doc='Test the "normality" of the histogram distribution',
               notes="""
               This function compares the histogram to a normal curve with the
               same mean and standard deviation. The individual counts are normalized
               by the total counts, the bin width and the standard deviation.
               For each bin, the rms difference between the expected probability and
               the normalized count is summed, and the final result is normalized by
               the total number of bins. In this way histograms with different means,
               standard deviations, number of bins and counts can be compared.
               If the histogram were perfectly normal, then a value of 0 would be returned.
               The more "non-normal", the higher the statistic.
               """,
               return_type=Type.DOUBLE,
               return_doc="""
               The normality statistic.
               Terminates if no histogram in the :class:`ST` object.
               """,
               parameters = [
                   Parameter('p1', type="ST",
                             doc=":class:`ST` Handle")
               ])
    ]
}

