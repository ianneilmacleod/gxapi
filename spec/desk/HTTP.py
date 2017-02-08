from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('HTTP',
                 doc="Connect to an Internet Server using :class:`HTTP`.",
                 notes="""
References:

1. http://www.w3.org/Protocols/:class:`HTTP`/HTTP2.html

2. http://www.w3.org/Addressing/URL/5_BNF.html

Note that path and search must conform be xalpha string (ref 2.).
Special characters can be specified with a %xx, where xx is the
hex ASCII number.  For example, a search string "This one" should
be  specified as "This%20one"
""")





gx_methods = {
    'Miscellaneous': [

        Method('Create_HTTP', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method creates a connection to an :class:`HTTP` server",
               return_type="HTTP",
               return_doc=":class:`HTTP` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="URL of the server"),
                   Parameter('p2', type=Type.STRING,
                             doc='user name, "" for none'),
                   Parameter('p3', type=Type.STRING,
                             doc='password,  "" for none'),
                   Parameter('p4', type=Type.STRING,
                             doc="Purpose of communication (for user verification)")
               ]),

        Method('Destroy_HTTP', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`HTTP`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HTTP",
                             doc=":class:`HTTP` to Destroy")
               ]),

        Method('Download_HTTP', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Download file from the internet to a :class:`BF`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HTTP",
                             doc="http object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name on the :class:`HTTP` site"),
                   Parameter('p3', type="BF",
                             doc=":class:`BF` in which to place the file"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Dynamic content (0 - no, 1 - yes)")
               ]),

        Method('SilentDownload_HTTP', module='geogxx', version='8.2.0',
               availability=Availability.PUBLIC, 
               doc="Download file from the internet to a :class:`BF` with no prompt for proxy authentication.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HTTP",
                             doc="http object"),
                   Parameter('p2', type=Type.STRING,
                             doc="File Name on the :class:`HTTP` site"),
                   Parameter('p3', type="BF",
                             doc=":class:`BF` in which to place the file"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Dynamic content (0 - no, 1 - yes)")
               ]),

        Method('Get_HTTP', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Get data from a server.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HTTP",
                             doc="http object"),
                   Parameter('p2', type=Type.STRING,
                             doc="http path (file or an ISAPI DLL), no spaces"),
                   Parameter('p3', type=Type.STRING,
                             doc="http search string, no spaces"),
                   Parameter('p4', type="BF",
                             doc="data to send"),
                   Parameter('p5', type="BF",
                             doc="data returned")
               ]),

        Method('Post_HTTP', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Post data to the server.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HTTP",
                             doc="http object"),
                   Parameter('p2', type=Type.STRING,
                             doc="http path (file or an ISAPI DLL)"),
                   Parameter('p3', type=Type.STRING,
                             doc="http search string, no spaces"),
                   Parameter('p4', type="BF",
                             doc="data to post")
               ]),

        Method('SetProxyCredentials_HTTP', module='geogxx', version='7.2.0',
               availability=Availability.PUBLIC, 
               doc="""
               Assigns the proxy username and password so that
               user is not prompted when the first download fails
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="HTTP",
                             doc="http object"),
                   Parameter('p2', type=Type.STRING,
                             doc="username"),
                   Parameter('p3', type=Type.STRING,
                             doc="password")
               ])
    ]
}

