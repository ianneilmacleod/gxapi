from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DSEL',
                 doc="The :class:`DSEL` object is used to select subsets of data from the DATA object")


gx_defines = [
    Define('DSEL_PICTURE_QUALITY',
           doc="Line Label Formats",
           constants=[
               Constant('DSEL_PICTURE_QUALITY_DEFAULT', value='0', type=Type.INT32_T)                        ,
               Constant('DSEL_PICTURE_QUALITY_LOSSLESS', value='1', type=Type.INT32_T)                        ,
               Constant('DSEL_PICTURE_QUALITY_SEMILOSSY', value='2', type=Type.INT32_T)                        ,
               Constant('DSEL_PICTURE_QUALITY_LOSSY', value='3', type=Type.INT32_T)                        ,
               Constant('DSEL_PICTURE_QUALITY_NATIVE', value='4', type=Type.INT32_T)                        ,
               Constant('DSEL_PICTURE_QUALITY_ECW', value='5', type=Type.INT32_T)                        ,
               Constant('DSEL_PICTURE_QUALITY_JPG', value='6', type=Type.INT32_T)                        ,
               Constant('DSEL_PICTURE_QUALITY_PNG', value='7', type=Type.INT32_T)                        ,
               Constant('DSEL_PICTURE_QUALITY_BMP', value='8', type=Type.INT32_T)                        ,
               Constant('DSEL_PICTURE_QUALITY_TIF', value='9', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_DSEL', module='geoengine.core', version='5.0.3',
               availability=Availability.PUBLIC, 
               doc="Create a Selection object",
               return_type="DSEL",
               return_doc=":class:`DSEL` handle, terminates if creation fails"),

        Method('DataSignificantFigures_DSEL', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Specify the data significant figures required",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Significant figures (positive, can be fractional)")
               ]),

        Method('Destroy_DSEL', module='geoengine.core', version='5.0.3',
               availability=Availability.PUBLIC, 
               doc="Destroy a :class:`DSEL`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` to destroy.")
               ]),

        Method('MetaQuery_DSEL', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Specify a metadata query string.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Meta query string")
               ]),

        Method('PictureQuality_DSEL', module='geoengine.core', version='5.1.4',
               availability=Availability.PUBLIC, 
               doc="Specify the quality of pictures being returned.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Quality")
               ]),

        Method('RequestAllInfo_DSEL', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Request that all meta-data info be sent",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="TRUE to for all data, FALSE - for normal data")
               ]),

        Method('SelectArea_DSEL', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Select a complex clipping area",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` to destroy."),
                   Parameter('p2', type="PLY",
                             doc=":class:`PLY` containing complex area (must contain a projection)")
               ]),

        Method('SelectRect_DSEL', module='geoengine.core', version='5.0.3',
               availability=Availability.PUBLIC, 
               doc="Select a rectangular area.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` to destroy."),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Min X"),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="Min Y"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Max X"),
                   Parameter('p5', type=Type.DOUBLE,
                             doc="Max Y")
               ]),

        Method('SelectResolution_DSEL', module='geoengine.core', version='5.0.3',
               availability=Availability.PUBLIC, 
               doc="Specify the resolution desired",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="Minimum Resolution"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="TRUE to force this resolution, if possible")
               ]),

        Method('SelectSize_DSEL', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Specify the image size desired",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Image width in pixels"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Image height in pixels")
               ]),

        Method('SetExtractAsDocument_DSEL', module='geoengine.core', version='8.0.0',
               availability=Availability.PUBLIC, 
               doc="Specify that we want to extract this file as a document",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="TRUE (1) if we want as a document")
               ]),

        Method('SetIPJ_DSEL', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Set the desired projection",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` to destroy."),
                   Parameter('p2', type="IPJ",
                             doc=":class:`IPJ` to set"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="TRUE to force reprojection, if possible")
               ]),

        Method('SpatialAccuracy_DSEL', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Specify the spatial accuracy required.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DSEL",
                             doc=":class:`DSEL` object"),
                   Parameter('p2', type=Type.DOUBLE,
                             doc="spatial accuracy desired")
               ])
    ]
}

