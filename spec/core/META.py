from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('META',
                 doc="""
                 A :class:`META` object contains hierarchical organized metadata
                 of any type, including other objects.  :class:`META` information
                 is organized in an XML-like structure based on a data
                 schema that describes the data hierarchy.   :class:`META` objects
                 are used by many entities that need to store metadata
                 specific to the entities or to the application.
                 
                 Metadata can be saved in databases and maps, as well as in
                 channels, lines, views and groups.  Oasis montaj objects
                 can be queried for their associated metadata, and if it
                 exists, the metadata can be retrieved and utilized by
                 other Oasis montaj processes.
                 """)


gx_defines = [
    Define('H_META_INVALID_TOKEN',
           is_constant=True,
           is_single_constant=True,
           doc=":class:`META` Invalid Token",
           constants=[
               Constant('H_META_INVALID_TOKEN', value='-1', type=Type.INT32_T)                        
           ]),

    Define('META_CORE_ATTRIB',
           doc=":class:`META` Core Attributes",
           constants=[
               Constant('META_CORE_ATTRIB_Class_Description', value='-300', type=Type.INT32_T,
                        doc="Description of this class")                        ,
               Constant('META_CORE_ATTRIB_Class_Application', value='-301', type=Type.INT32_T,
                        doc="Application that created this class")                        ,
               Constant('META_CORE_ATTRIB_Class_ReferenceURL', value='-302', type=Type.INT32_T,
                        doc="URL that defines this class")                        ,
               Constant('META_CORE_ATTRIB_Class_Type', value='-303', type=Type.INT32_T,
                        doc="Type of Class")                        ,
               Constant('META_CORE_ATTRIB_Type_Description', value='-304', type=Type.INT32_T,
                        doc="Description of this type")                        ,
               Constant('META_CORE_ATTRIB_Type_ReferenceURL', value='-305', type=Type.INT32_T,
                        doc="URL that defines this type")                        ,
               Constant('META_CORE_ATTRIB_Type_FixedSize', value='-306', type=Type.INT32_T,
                        doc="Fixed size of this type (in bytes)")                        ,
               Constant('META_CORE_ATTRIB_Type_ByteOrder', value='-307', type=Type.INT32_T,
                        doc="Byte order for this type")                        ,
               Constant('META_CORE_ATTRIB_Type_MinValue', value='-308', type=Type.INT32_T,
                        doc="Minimum Value for this type")                        ,
               Constant('META_CORE_ATTRIB_Type_MaxValue', value='-309', type=Type.INT32_T,
                        doc="Maximum Value for this type")                        ,
               Constant('META_CORE_ATTRIB_Type_MaxSize', value='-310', type=Type.INT32_T,
                        doc="Maximum Size in bytes for this type")                        ,
               Constant('META_CORE_ATTRIB_Type_ObjectClass', value='-311', type=Type.INT32_T,
                        doc="Object class that manages this type")                        ,
               Constant('META_CORE_ATTRIB_Type_hCreatS_Func', value='-312', type=Type.INT32_T,
                        doc="Object creating function")                        ,
               Constant('META_CORE_ATTRIB_Type_sSerial_Func', value='-313', type=Type.INT32_T,
                        doc="Object serializationg function")                        ,
               Constant('META_CORE_ATTRIB_Type_Enum_Value', value='-314', type=Type.INT32_T,
                        doc="Enumeration Value")                        ,
               Constant('META_CORE_ATTRIB_Attrib_Visible', value='-315', type=Type.INT32_T,
                        doc="Is this attribute visible to the user")                        ,
               Constant('META_CORE_ATTRIB_Attrib_Editable', value='-316', type=Type.INT32_T,
                        doc="Is this atttribute editable by the user")                        ,
               Constant('META_CORE_ATTRIB_Attrib_FlatName', value='-317', type=Type.INT32_T,
                        doc="The flat name of this attribute")                        
           ]),

    Define('META_CORE_CLASS',
           doc="Meta Core Class Objects",
           constants=[
               Constant('META_CORE_CLASS_Base', value='-100', type=Type.INT32_T,
                        doc="All Classes are subordinate to this class")                        ,
               Constant('META_CORE_CLASS_Predefined', value='-101', type=Type.INT32_T,
                        doc="All Predefined symbols are in this class")                        ,
               Constant('META_CORE_CLASS_Attributes', value='-102', type=Type.INT32_T)                        ,
               Constant('META_CORE_CLASS_ClassAttributes', value='-103', type=Type.INT32_T)                        ,
               Constant('META_CORE_CLASS_TypeAttributes', value='-104', type=Type.INT32_T)                        ,
               Constant('META_CORE_CLASS_ObjectAttributes', value='-105', type=Type.INT32_T)                        ,
               Constant('META_CORE_CLASS_EnumAttributes', value='-106', type=Type.INT32_T)                        ,
               Constant('META_CORE_CLASS_AttributeAttributes', value='-107', type=Type.INT32_T)                        ,
               Constant('META_CORE_CLASS_ItemAttributes', value='-108', type=Type.INT32_T)                        ,
               Constant('META_CORE_CLASS_Types', value='-109', type=Type.INT32_T)                        ,
               Constant('META_CORE_CLASS_Enums', value='-110', type=Type.INT32_T)                        ,
               Constant('META_CORE_CLASS_Enum_Bool', value='-111', type=Type.INT32_T)                        ,
               Constant('META_CORE_CLASS_Enum_ClassType', value='-112', type=Type.INT32_T)                        
           ]),

    Define('META_CORE_TYPE',
           doc=":class:`META` Core Data Types",
           constants=[
               Constant('META_CORE_TYPE_Bytes', value='-200', type=Type.INT32_T,
                        doc="Data Bytes (Base type)")                        ,
               Constant('META_CORE_TYPE_Bool', value='-201', type=Type.INT32_T,
                        doc="Boolean")                        ,
               Constant('META_CORE_TYPE_I1', value='-202', type=Type.INT32_T,
                        doc="Signed character")                        ,
               Constant('META_CORE_TYPE_U1', value='-203', type=Type.INT32_T,
                        doc="Unsigned character")                        ,
               Constant('META_CORE_TYPE_I2', value='-204', type=Type.INT32_T,
                        doc="Signed short")                        ,
               Constant('META_CORE_TYPE_U2', value='-205', type=Type.INT32_T,
                        doc="Unsigned short")                        ,
               Constant('META_CORE_TYPE_I4', value='-206', type=Type.INT32_T,
                        doc="Signed long")                        ,
               Constant('META_CORE_TYPE_U4', value='-207', type=Type.INT32_T,
                        doc="Unsigned long")                        ,
               Constant('META_CORE_TYPE_I8', value='-208', type=Type.INT32_T,
                        doc="Singed long long (64 bit int)")                        ,
               Constant('META_CORE_TYPE_U8', value='-209', type=Type.INT32_T,
                        doc="Unsigned long long")                        ,
               Constant('META_CORE_TYPE_R4', value='-210', type=Type.INT32_T,
                        doc="Float (32bit)")                        ,
               Constant('META_CORE_TYPE_R8', value='-211', type=Type.INT32_T,
                        doc="Double (64bit)")                        ,
               Constant('META_CORE_TYPE_String', value='-212', type=Type.INT32_T,
                        doc="String")                        ,
               Constant('META_CORE_TYPE_Object', value='-213', type=Type.INT32_T,
                        doc="Predefined Object (:class:`ITR`,:class:`IPJ`)")                        ,
               Constant('META_CORE_TYPE_Enum', value='-214', type=Type.INT32_T,
                        doc="Enumeration")                        ,
               Constant('META_CORE_TYPE_ClassType', value='-215', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Attribute': [

        Method('CreateAttrib_META', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="Create an attribute",
               return_type="META_TOKEN",
               return_doc="x - Attribute Token",
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` object."),
                   Parameter('p2', type=Type.STRING,
                             doc="Attribute Name"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Parent class or :def:`META_CORE_CLASS`"),
                   Parameter('p4', type="META_TOKEN",
                             doc="Type of Attribute or :def:`META_CORE_TYPE`")
               ]),

        Method('DeleteAttrib_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Delete Attrib from :class:`META`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` object."),
                   Parameter('p2', type="META_TOKEN",
                             doc="Attrib to delete")
               ])
    ],
    'Browser': [

        Method('SetAttributeEditable_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Allow/disallow an attribute to be editable in the browser",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` Object"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Attribute or :def:`META_CORE_ATTRIB`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Editable Flag")
               ]),

        Method('SetAttributeVisible_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Allow/disallow an attribute to be visible in the browser",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` Object"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Attribute or :def:`META_CORE_ATTRIB`"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Editable Flag")
               ])
    ],
    'Class': [

        Method('CreateClass_META', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="Create a class",
               return_type="META_TOKEN",
               return_doc="x - Class Token",
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` object."),
                   Parameter('p2', type=Type.STRING,
                             doc="Class Name"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Parent class or :def_val:`META_CORE_CLASS_Base`")
               ]),

        Method('DeleteClass_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Delete Class from :class:`META`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` object."),
                   Parameter('p2', type="META_TOKEN",
                             doc="Class to delete")
               ])
    ],
    'Core': [

        Method('Copy_META', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Copy a :class:`META` to another",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc="Destination :class:`META` object."),
                   Parameter('p2', type="META",
                             doc="Source :class:`META` object.")
               ]),

        Method('Create_META', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Create",
               return_type="META",
               return_doc=":class:`META` Object"),

        Method('CreateS_META', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Create a :class:`META` Object from a :class:`BF`",
               return_type="META",
               return_doc=":class:`META` Object",
               parameters = [
                   Parameter('p1', type="BF",
                             doc=":class:`BF` to serialize from")
               ]),

        Method('Destroy_META', module='geoengine.core', version='5.0.8',
               availability=Availability.PUBLIC, 
               doc="Destroy",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` to destroy.")
               ]),

        Method('Serial_META', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Serialize an :class:`META` to a :class:`BF`",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` object to serialize"),
                   Parameter('p2', type="BF",
                             doc=":class:`BF` to serialize to")
               ])
    ],
    'Get Data': [

        Method('FindData_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Does this meta/attribute have a value ?",
               return_type="META_TOKEN",
               return_doc="""
               x  - Data Value
               :def_val:`H_META_INVALID_TOKEN` - No
               """,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute")
               ]),

        Method('GetAttribBool_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Get a boolean value to an attribute",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Value to set")
               ]),

        Method('GetAttribEnum_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Get an enum value to an attribute (as an integer)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Value to set")
               ]),

        Method('GetAttribInt_META', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Get an integer value to an attribute",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type=Type.INT32_T, is_ref=True,
                             doc="Value to set")
               ]),

        Method('GetAttribReal_META', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Get an integer value to an attribute",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type=Type.DOUBLE, is_ref=True,
                             doc="Value to set")
               ]),

        Method('IGetAttribString_META', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Get a string value to an attribute",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="String value to get"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Length of string")
               ]),

        Method('iHasValue_META', module='geoengine.core', version='6.0.1',
               availability=Availability.PUBLIC, 
               doc="Does this meta/attribute have a value set?",
               return_type=Type.INT32_T,
               return_doc=":def:`GEO_BOOL`",
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute")
               ])
    ],
    'Import/Export': [

        Method('ExportTableCSV_META', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Export all items in a class as a CSV",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Class of items to export"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of CSV file to produce")
               ]),

        Method('ImportTableCSV_META', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Import a CSV into a class as items.",
               notes="""
               Field names in the CSV file that match attribute names in the class will be
               imported into table entries in the class.  Usually this will be used with
               a class created using the hCreateTable_SCHEMA method so that the contents of
               class can be viewed as a table.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Class to import into"),
                   Parameter('p3', type=Type.STRING,
                             doc="Name of CSV file to load")
               ]),

        Method('WriteText_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Write the entire meta as a text file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="WA",
                             doc=":class:`WA` to write to")
               ])
    ],
    'Item': [

        Method('DeleteAllItems_META', module='geoengine.core', version='5.1.5',
               availability=Availability.PUBLIC, 
               doc="Delete all items in this class.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` Object"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Class of items to delete")
               ]),

        Method('DeleteItem_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Delete item from :class:`META`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` object."),
                   Parameter('p2', type="META_TOKEN",
                             doc="Item to delete")
               ]),

        Method('hCreatItem_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Creates item in Class.",
               return_type="META_TOKEN",
               return_doc="""
               x                    - Next Item
               :def_val:`H_META_INVALID_TOKEN` - Error
               """,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` Object."),
                   Parameter('p2', type=Type.STRING,
                             doc="Unique item Name"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Class (can be root)")
               ]),

        Method('hGetNextItem_META', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Count the number of items in a class",
               return_type="META_TOKEN",
               return_doc="""
               x                    - Next Item
               :def_val:`H_META_INVALID_TOKEN` - No more items
               """,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` Object"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Class"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Starting Item (must :def_val:`H_META_INVALID_TOKEN` for first item)")
               ])
    ],
    'Object': [

        Method('GetAttribOBJ_META', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Get an object from an attribute",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type="HANDLE",
                             doc="Object to get info into")
               ]),

        Method('SetAttribOBJ_META', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Set an object to an attribute",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type="HANDLE",
                             doc="Object to set")
               ])
    ],
    'Set Data': [

        Method('SetAttribBool_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Set a boolean value to an attribute",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Value to set")
               ]),

        Method('SetAttribEnum_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Set an enum value to an attribute (as an integer)",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Value to set")
               ]),

        Method('SetAttribInt_META', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Set an integer value to an attribute",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type=Type.INT32_T,
                             doc="Value to set")
               ]),

        Method('SetAttribReal_META', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Set an integer value to an attribute",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type=Type.DOUBLE,
                             doc="Value to set")
               ]),

        Method('SetAttribString_META', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Set a string value to an attribute",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute"),
                   Parameter('p4', type=Type.STRING,
                             doc="String value to set")
               ]),

        Method('SetEmptyAttrib_META', module='geoengine.core', version='6.3.0',
               availability=Availability.PUBLIC, 
               doc="Set an empty attribute data holder",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` Object"),
                   Parameter('p2', type="META_TOKEN",
                             doc="MetaObject to set"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute MetaObject to set")
               ])
    ],
    'Transfer': [

        Method('hCopyAcrossAttribute_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Copy an Attribute from one :class:`META` to another",
               return_type="META_TOKEN",
               return_doc="""
               x                  - Handle of Attribute
               META_INVALID_TOKEN - No visible data
               """,
               parameters = [
                   Parameter('p1', type="META",
                             doc="Destination :class:`META` object."),
                   Parameter('p2', type="META",
                             doc="Source :class:`META` object."),
                   Parameter('p3', type="META_TOKEN",
                             doc="Attribute to copy")
               ]),

        Method('hCopyAcrossClass_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Copy a Class from one :class:`META` to another",
               notes="This will copy all parent classes as well.",
               return_type="META_TOKEN",
               return_doc="""
               x                  - Handle of Class
               META_INVALID_TOKEN - No visible data anywhere
               """,
               parameters = [
                   Parameter('p1', type="META",
                             doc="Destination :class:`META` object."),
                   Parameter('p2', type="META",
                             doc="Source :class:`META` object."),
                   Parameter('p3', type="META_TOKEN",
                             doc="Class to copy")
               ]),

        Method('hCopyAcrossData_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Copy a Data value from one :class:`META` to another",
               return_type="META_TOKEN",
               return_doc="""
               x                  - Handle of Data value
               META_INVALID_TOKEN - No visible data
               """,
               parameters = [
                   Parameter('p1', type="META",
                             doc="Destination :class:`META` object."),
                   Parameter('p2', type="META",
                             doc="Source :class:`META` object."),
                   Parameter('p3', type="META_TOKEN",
                             doc="Data value to copy")
               ]),

        Method('hCopyAcrossItem_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Copy an Item from one :class:`META` to another",
               return_type="META_TOKEN",
               return_doc="""
               x                  - Handle of Item
               META_INVALID_TOKEN - No visible data
               """,
               parameters = [
                   Parameter('p1', type="META",
                             doc="Destination :class:`META` object."),
                   Parameter('p2', type="META",
                             doc="Source :class:`META` object."),
                   Parameter('p3', type="META_TOKEN",
                             doc="Item to copy")
               ]),

        Method('hCopyAcrossType_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Copy a Type from one :class:`META` to another",
               notes="Classes and parent types will also be copied.",
               return_type="META_TOKEN",
               return_doc="""
               x                  - Handle of type
               META_INVALID_TOKEN - No visible data anywhere
               """,
               parameters = [
                   Parameter('p1', type="META",
                             doc="Destination :class:`META` object."),
                   Parameter('p2', type="META",
                             doc="Source :class:`META` object."),
                   Parameter('p3', type="META_TOKEN",
                             doc="Type to copy")
               ]),

        Method('MoveDatasAcross_META', module='geoengine.core', version='5.1.8',
               availability=Availability.PUBLIC, 
               doc="Moves data items from one :class:`META` to another",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc="Destination :class:`META` Object"),
                   Parameter('p2', type="META",
                             doc="Source :class:`META` Object"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Object to copy data from"),
                   Parameter('p4', type="META_TOKEN",
                             doc="Object to copy data to")
               ])
    ],
    'Type': [

        Method('CreateType_META', module='geoengine.core', version='6.1.0',
               availability=Availability.PUBLIC, 
               doc="Create an attribute",
               return_type="META_TOKEN",
               return_doc="x - Type Token",
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` object."),
                   Parameter('p2', type=Type.STRING,
                             doc="Attribute Name"),
                   Parameter('p3', type="META_TOKEN",
                             doc="Parent Class or :def:`META_CORE_CLASS`"),
                   Parameter('p4', type="META_TOKEN",
                             doc="Parent Type or :def:`META_CORE_TYPE`")
               ]),

        Method('DeleteData_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Delete Data from :class:`META`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` object."),
                   Parameter('p2', type="META_TOKEN",
                             doc="Data to delete")
               ]),

        Method('DeleteType_META', module='geoengine.core', version='5.1.6',
               availability=Availability.PUBLIC, 
               doc="Delete Type from :class:`META`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META",
                             doc=":class:`META` object."),
                   Parameter('p2', type="META_TOKEN",
                             doc="Type to delete")
               ])
    ],
    'UMN': [

        Method('IGetObjName_META', module='geoengine.core', version='5.1.3',
               availability=Availability.PUBLIC, 
               doc="Get the name of this item.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='p4',
                             doc="Name of object"),
                   Parameter('p4', type=Type.INT32_T, default_length='STR_DEFAULT_LONG',
                             doc="Size of name buffer")
               ]),

        Method('ResolveUMN_META', module='geoengine.core', version='5.1.0',
               availability=Availability.PUBLIC, 
               doc="Resolve a Unique Meta Name (UMN) and find the token",
               return_type="META_TOKEN",
               return_doc="""
               x                    - Token
               :def_val:`H_META_INVALID_TOKEN` - Not found
               """,
               parameters = [
                   Parameter('p1', type="META"),
                   Parameter('p2', type=Type.STRING,
                             doc="Unique Meta Name (UMN)")
               ])
    ],
    'Miscellaneous': [

    ]
}

