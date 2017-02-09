from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('GER',
                 doc="""
                 Allows access to a Geosoft format error message file. This class
                 does not in itself produce an error message, but retrieves a
                 selected message from the file, and allows the
                 setting of replacement parameters within the message. It
                 is up to the user to display or use the message.
                 """,
                 notes="""
                 :class:`GER` message files contain numbered messages that can be used within GXs.
                 Following is an example from the file :class:`GEOSOFT`.:class:`GER`:
                 
                 
                       #20008
                       ! Invalid password. The product installation has failed.
                 
                       #20009
                       ! Unable to find INI file: %1
                       ! See the documentation for details
                 
                 
                 A '#' character in column 1 indicates a message number.  The message
                 follows on lines that begin with a '!' character.  Strings in the message
                 may be replaced at run time with values using the :func:`SetString_GER`,
                 :func:`SetInt_GER` and :func:`SetReal_GER` methods. The iGet_GER will return the message
                 with strings replaced by their settings.  By convention, we recommend
                 that you use "%1", "%2", etc. as replacement strings.
                 """)





gx_methods = {
    'Miscellaneous': [

        Method('Create_GER', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Opens an ASCII error file to read from.",
               notes="""
               The :class:`GER` file may be in the local directory or the :class:`GEOSOFT`
               directory.
               """,
               return_type="GER",
               return_doc=":class:`GER` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`GER` file name.")
               ]),

        Method('Destroy_GER', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys a :class:`GER` Object",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GER",
                             doc=":class:`GER` object to destroy")
               ]),

        Method('IiGet_GER', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get a message string.",
               return_type=Type.INT32_T,
               return_doc="""
               0 if message found
               1 if no message, passed message remains unchanged
               """,
               parameters = [
                   Parameter('p1', type="GER",
                             doc=":class:`GER` Object"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="message number"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="message string returned, replacements filtered"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="maximum string length")
               ]),

        Method('SetInt_GER', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a replacement string value to an int.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GER",
                             doc=":class:`GER` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc='replacement string (ie. "%1")'),
                   Parameter('p3', type=Type.INT32_T,
                             doc="setting")
               ]),

        Method('SetReal_GER', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a replacement string value to a real.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GER",
                             doc=":class:`GER` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc='replacement string (ie. "%1")'),
                   Parameter('p3', type=Type.DOUBLE,
                             doc="setting")
               ]),

        Method('SetString_GER', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Set a replacement string value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="GER",
                             doc=":class:`GER` Object"),
                   Parameter('p2', type=Type.STRING,
                             doc='replacement string (ie. "%1")'),
                   Parameter('p3', type=Type.STRING,
                             doc="setting")
               ])
    ]
}

