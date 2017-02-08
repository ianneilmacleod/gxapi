from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('COM',
                 doc="This class is used to communicate with external serial devices. It allows the setting of timeouts.")


gx_defines = [
    Define('COM_BAUD',
           doc="Connection Speed",
           constants=[
               Constant('COM_BAUD_110', value='0', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_300', value='1', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_600', value='2', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_1200', value='3', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_2400', value='4', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_4800', value='5', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_9600', value='6', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_14400', value='7', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_19200', value='8', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_56000', value='9', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_57600', value='10', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_115200', value='11', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_128000', value='12', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_256000', value='13', type=Type.INT32_T)                        ,
               Constant('COM_BAUD_38400', value='14', type=Type.INT32_T)                        
           ]),

    Define('COM_DATASIZE',
           doc="Data Bits",
           constants=[
               Constant('COM_DATASIZE_FIVE', value='5', type=Type.INT32_T)                        ,
               Constant('COM_DATASIZE_SIX', value='6', type=Type.INT32_T)                        ,
               Constant('COM_DATASIZE_SEVEN', value='7', type=Type.INT32_T)                        ,
               Constant('COM_DATASIZE_EIGHT', value='8', type=Type.INT32_T)                        
           ]),

    Define('COM_FLOWCONTROL',
           doc="Flow Control Options",
           constants=[
               Constant('COM_FLOWCONTROL_NONE', value='0', type=Type.INT32_T)                        ,
               Constant('COM_FLOWCONTROL_RTS_CTS', value='1', type=Type.INT32_T)                        ,
               Constant('COM_FLOWCONTROL_DTR_DSR', value='2', type=Type.INT32_T)                        ,
               Constant('COM_FLOWCONTROL_XON_XOFF', value='3', type=Type.INT32_T)                        
           ]),

    Define('COM_PARITY',
           doc="Parity",
           constants=[
               Constant('COM_PARITY_EVEN', value='0', type=Type.INT32_T)                        ,
               Constant('COM_PARITY_NARK', value='1', type=Type.INT32_T)                        ,
               Constant('COM_PARITY_NONE', value='2', type=Type.INT32_T)                        ,
               Constant('COM_PARITY_ODD', value='3', type=Type.INT32_T)                        ,
               Constant('COM_PARITY_SPACE', value='4', type=Type.INT32_T)                        
           ]),

    Define('COM_STOPBITS',
           doc="Stop Bits",
           constants=[
               Constant('COM_STOPBITS_ONE', value='0', type=Type.INT32_T)                        ,
               Constant('COM_STOPBITS_ONE5', value='1', type=Type.INT32_T)                        ,
               Constant('COM_STOPBITS_TWO', value='2', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_COM', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Create :class:`COM` object.",
               return_type="COM",
               return_doc=":class:`COM` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='port name to open ("COM1" is example)'),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`COM_BAUD`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`COM_DATASIZE`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`COM_PARITY`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`COM_STOPBITS`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`COM_FLOWCONTROL`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Timeout in Ms (500)")
               ]),

        Method('CreateNoTerminate_COM', module='geogxx', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Create :class:`COM` object.",
               return_type="COM",
               return_doc=":class:`COM` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc='port name to open ("COM1" is example)'),
                   Parameter('p2', type=Type.INT32_T,
                             doc=":def:`COM_BAUD`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`COM_DATASIZE`"),
                   Parameter('p4', type=Type.INT32_T,
                             doc=":def:`COM_PARITY`"),
                   Parameter('p5', type=Type.INT32_T,
                             doc=":def:`COM_STOPBITS`"),
                   Parameter('p6', type=Type.INT32_T,
                             doc=":def:`COM_FLOWCONTROL`"),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Timeout in Ms (500)")
               ]),

        Method('Destroy_COM', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`COM` handle.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle")
               ]),

        Method('IiReadLineNoTerminate_COM', module='geogxx', version='6.0.1',
               availability=Availability.LICENSED, 
               doc="Reads a Line from the :class:`COM`",
               return_type=Type.INT32_T,
               return_doc="""
               0 - if successful in reading a line
               1 - if an error was encountered
               """,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="string for line"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Length of Line to read, CT-LF is not stipped, NULL will be added so the Line length must be at least int+1.")
               ]),

        Method('iReadCharsNoTerminate_COM', module='geogxx', version='6.0.1',
               availability=Availability.LICENSED, 
               doc="Reads characters from the :class:`COM`, times out and does not terminate",
               return_type=Type.INT32_T,
               return_doc="""
               1 - if time out or error
               0 - if successful
               """,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="string for characters"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="number of characters to read (string size must be +1) to silence all message reporting enter the nevative value of the number of chars to read")
               ]),

        Method('IReadLine_COM', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Reads a Line from the :class:`COM`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="string for line"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Length of Line to read, NULL will be added so the Line length must be at least int+1.")
               ]),

        Method('iWriteCharsNoTerminate_COM', module='geogxx', version='6.0.1',
               availability=Availability.LICENSED, 
               doc="Writes characters to the :class:`COM`.  Does not terminate upon error",
               return_type=Type.INT32_T,
               return_doc="""
               0 - if successful in writing a string
               1 - if time out or error was encountered
               """,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="line to write")
               ]),

        Method('PurgeComm_COM', module='geogxx', version='5.1.8',
               availability=Availability.LICENSED, 
               doc="Purges the input and output buffers.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="COM",
                             doc="Port")
               ]),

        Method('ReadChars_COM', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Reads characters from the :class:`COM`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle"),
                   Parameter('p2', type=Type.STRING, is_ref=True, size_of_param='2',
                             doc="string for characters"),
                   Parameter('p3', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="number of characters to read (string size must be +1)")
               ]),

        Method('ReadEM61LinesWA_COM', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Reads Lines from the :class:`COM` to a :class:`WA`: Geonics EM61 only",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="number of lines"),
                   Parameter('p3', type="WA",
                             doc="Where to put lines")
               ]),

        Method('ReadFile2WA_COM', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Reads entire dataset from the :class:`COM` to a :class:`WA`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle"),
                   Parameter('p2', type="WA",
                             doc="Where to put lines")
               ]),

        Method('ReadLinesWA_COM', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Reads Lines from the :class:`COM` to a :class:`WA`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="number of lines"),
                   Parameter('p3', type="WA",
                             doc="Where to put lines")
               ]),

        Method('SetTimeOut_COM', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Set the timeout value.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="Timeout in Ms (500)")
               ]),

        Method('WriteChars_COM', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Writes characters to the :class:`COM`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="line to write")
               ]),

        Method('WriteLine_COM', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Writes a Line to the :class:`COM`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="COM",
                             doc=":class:`COM` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="line to write")
               ])
    ]
}

