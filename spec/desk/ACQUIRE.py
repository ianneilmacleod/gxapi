from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('ACQUIRE',
                 doc="""
This class is used to import Acquire data. It uses the
public Acquire API.
""")


gx_defines = [
    Define('ACQUIRE_SEL',
           doc="Type of Selection",
           constants=[
               Constant('ACQUIRE_SEL_HOLES', value='0', type=Type.INT32_T)                        ,
               Constant('ACQUIRE_SEL_POINT', value='1', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_ACQUIRE', module='geoacquire', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Create a :class:`ACQUIRE` object",
               return_type="ACQUIRE",
               return_doc=":class:`ACQUIRE` Object"),

        Method('DeleteEmptyChan_ACQUIRE', module='geoacquire', version='6.0.0',
               availability=Availability.LICENSED, 
               doc="Delete empty channels",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ACQUIRE",
                             doc=":class:`ACQUIRE` Handle"),
                   Parameter('p2', type="DB",
                             doc="Database")
               ]),

        Method('Destroy_ACQUIRE', module='geoacquire', version='6.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroy :class:`ACQUIRE`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="ACQUIRE",
                             doc="Aquire Object")
               ]),

        Method('iImportHole_ACQUIRE', module='geoacquire', version='6.0.1',
               availability=Availability.LICENSED, 
               doc="Import Drillhole data acQuire database into a GDB",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Error (Will not stop GX)
               """,
               parameters = [
                   Parameter('p1', type="ACQUIRE",
                             doc="Aquire Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="project name"),
                   Parameter('p3', type=Type.STRING,
                             doc="project directory"),
                   Parameter('p4', type=Type.STRING,
                             doc="Parameter File"),
                   Parameter('p5', type="VV",
                             doc="list of geology name database"),
                   Parameter('p6', type=Type.INT32_T,
                             doc="0: Write to existing databases (overwrite holes), 1: Delete existing databases."),
                   Parameter('p7', type=Type.INT32_T,
                             doc="Convert Negatives (0,1)")
               ]),

        Method('iImportPoint_ACQUIRE', module='geoacquire', version='6.0.1',
               availability=Availability.LICENSED, 
               doc="Import Point Sample data acQuire database into a GDB",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - Error (Will not stop GX)
               """,
               parameters = [
                   Parameter('p1', type="ACQUIRE",
                             doc=":class:`ACQUIRE` Handle"),
                   Parameter('p2', type="DB",
                             doc="Geosoft GDB"),
                   Parameter('p3', type=Type.STRING,
                             doc="Parameter File"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Convert Negatives (0,1)")
               ]),

        Method('iSelectionTool_ACQUIRE', module='geoacquire', version='6.0.1',
               availability=Availability.LICENSED, 
               doc="Run the Acquire Selection Tool.",
               return_type=Type.INT32_T,
               return_doc="""
               0 - Ok
               1 - if user cancels
               """,
               parameters = [
                   Parameter('p1', type="ACQUIRE",
                             doc="Aquire Object"),
                   Parameter('p2', type=Type.STRING,
                             doc="Selection File Name"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`ACQUIRE_SEL`")
               ])
    ]
}

