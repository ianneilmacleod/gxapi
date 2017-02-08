from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('INTERNET',
                 doc="""
This library provides functions for accessing the internet
and MAPI-compliant e-mail services.
Supported by Oasis montaj ONLY.
""")





gx_methods = {
    'Miscellaneous': [

        Method('iDownloadHTTP_INTERNET', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Download :class:`HTTP` file from the internet to file.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Error
               """,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc=":class:`HTTP` URL"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name to save to"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="No longer used, just pass 0")
               ]),

        Method('SendMail_INTERNET', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Prepaire an email for the user.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='Recipient Name        ("" for none)'),
                   Parameter('p2', type=Type.STRING,
                             doc='Recipient Address     ("" for none)'),
                   Parameter('p3', type=Type.STRING,
                             doc='szSubject             ("" for none)'),
                   Parameter('p4', type=Type.STRING,
                             doc='Message Text          ("" for none)'),
                   Parameter('p5', type=Type.STRING,
                             doc='Attachment1 File Name ("" for none)'),
                   Parameter('p6', type=Type.STRING,
                             doc='Attachment1 User Name ("" for none)'),
                   Parameter('p7', type=Type.STRING,
                             doc='Attachment2 File Name ("" for none)'),
                   Parameter('p8', type=Type.STRING,
                             doc='Attachment2 User Name ("" for none)')
               ])
    ]
}

