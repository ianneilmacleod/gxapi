from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('DGW',
                 doc="""
                 Provides access to dialog boxes for user I/O. You can
                 use this class to store to, or retrieve information from
                 the current workspace parameter block via dialog boxes
                 """,
                 notes="""
                 Setting Fonts in GX dialogs.
                 
                 By default, "new look" GX dialogs uses the "Tahoma" font. This font can be
                 overridden by updating the application settings. This can be done programmatically
                 using the :func:`GlobalSet_SYS` function using the following parameters:
                 
                 MONTAJ.GX_FONT="Font_name"
                 
                 This sets the default font to "Font_name". It applies to text in all
                 components of the dialog.
                 
                 Additional customization of individual components can be accomplished
                 using the following parameters:
                 
                 MONTAJ.GX_CAPTION_FONT="Caption_Font": Font for the field captions (labels)
                 MONTAJ.GX_BUTTON_FONT="Button_Font"  : Font for buttons, including the "Browse"
                                                 button
                 MONTAJ.GX_TITLE_FONT="Title_Font"    : Font for special titles (see :func:`SetTitle_DGW`).
                 
                 The font used for the text in edit windows remains the default, or the
                 value specified using MONTAJ.GX_FONT.
                 
                 Note that the "OK" button, and the Title, use "Bold" versions of the
                 specified font. If the bolded version does not exist as a normal font,
                 then the operating system may provide its own alternative which may not
                 appear the same as you expect.
                 
                 Before version 6.2. there used to be a parameter, MONTAJ.GX_CHARSET, that
                 affected characters above ASCII 127. 6.2. introduced Unicode in the core
                 montaj engine that eliminated the need for such a setting. All strings
                 on the GX API level are encoded in :def:`UTF8` during runtime which makes it possible
                 to represent all possible characters without using character sets.
                 """)


gx_defines = [
    Define('DGW_OBJECT',
           doc="""
           Dialog object defines
           INFO TYPE   EDIT   FEDIT  LEDIT  CEDIT  EBUT
           =========   =====  =====  =====  =====  =====
           LABEL       RW     RW     RW     RW     RW          R - can use GetInfo_DGW
           TEXT        RW     RW     RW     RW     .           W - can use :func:`SetInfo_DGW`
           PATH        .      RW     .      .      .
           FILEPATH    .      RW     .      .      .
           LISTVAL     .      .      R      .      .
           LISTALIAS   .      .      RW     .      .
           """,
           constants=[
               Constant('DGW_LABEL', value='0', type=Type.INT32_T,
                        doc="The text label tied to each Dialogue component.")                        ,
               Constant('DGW_TEXT', value='1', type=Type.INT32_T,
                        doc="The edit field text.")                        ,
               Constant('DGW_PATH', value='2', type=Type.INT32_T,
                        doc="The file edit path.")                        ,
               Constant('DGW_FILEPATH', value='3', type=Type.INT32_T,
                        doc="The complete file name, path included.")                        ,
               Constant('DGW_LISTVAL', value='4', type=Type.INT32_T,
                        doc="The alias value associated with the list entry.")                        ,
               Constant('DGW_LISTALIAS', value='5', type=Type.INT32_T,
                        doc="The text value associated with the list entry.")                        ,
               Constant('DGW_EXT', value='7', type=Type.INT32_T,
                        doc="The extension associated with a filename entry.")                        ,
               Constant('DGW_HIDE', value='8', type=Type.INT32_T,
                        doc='Hide the button or entry and its label, if string is not "0"')                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('Create_DGW', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               This method creates a Dialogue window from a specified
               resource. The Resource is loaded into memory but not displayed.
               """,
               return_type="DGW",
               return_doc="Handle to the :class:`DGW` object.",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the Window Resource to use")
               ]),

        Method('Destroy_DGW', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Destroys a Dialogue Window.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DGW",
                             doc="Dialogue to Destroy")
               ]),

        Method('GetInfoMETA_DGW', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Copies the Dialogue information to a :class:`META` attribute.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DGW",
                             doc="Dialogue"),
                   Parameter('p2', type="DGW_OBJ",
                             doc="Dialogue Object"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DGW_OBJECT`"),
                   Parameter('p4', type="META"),
                   Parameter('p5', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p6', type="META_TOKEN",
                             doc="Attribute")
               ]),

        Method('GetInfoSYS_DGW', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               This method uses the information in a Dialogue box to
               set a :class:`SYS` variable.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DGW",
                             doc="Dialogue"),
                   Parameter('p2', type="DGW_OBJ",
                             doc="Dialogue Object"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DGW_OBJECT`"),
                   Parameter('p4', type=Type.STRING,
                             doc="Group name of the Variable"),
                   Parameter('p5', type=Type.STRING,
                             doc="Variable name")
               ]),

        Method('GetList_DGW', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               This method retrieves the list (:class:`LST`) object associated
               with a Dialogue object.
               """,
               return_type="LST",
               return_doc="The List Object",
               parameters = [
                   Parameter('p1', type="DGW",
                             doc="Dialogue"),
                   Parameter('p2', type="DGW_OBJ",
                             doc="Dialogue Object")
               ]),

        Method('GtInfo_DGW', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               This method fills the specified string with the text from
               the text object specified.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DGW",
                             doc="Dialogue"),
                   Parameter('p2', type="DGW_OBJ",
                             doc="Handle to the TEXT Object"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DGW_OBJECT`"),
                   Parameter('p4', type=Type.STRING, is_ref=True, size_of_param='p5',
                             doc="Where to place the String"),
                   Parameter('p5', type=Type.INT32_T, default_length='STR_VERY_LONG',
                             doc="Size of the String")
               ]),

        Method('iRunDialogue_DGW', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This method runs the Dialogue window.",
               return_type=Type.INT32_T,
               return_doc="The Exit Code of the Dialogue window.",
               parameters = [
                   Parameter('p1', type="DGW",
                             doc="Dialogue Window")
               ]),

        Method('SetInfo_DGW', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               This method sets the string of a text object. If the string
               is too long it will be truncated.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DGW",
                             doc="Dialogue"),
                   Parameter('p2', type="DGW_OBJ",
                             doc="Handle to the TEXT Object"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DGW_OBJECT`"),
                   Parameter('p4', type=Type.STRING,
                             doc="String to set the Text To")
               ]),

        Method('SetInfoMETA_DGW', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="This sets a text object to the text found in a :class:`META` attribute.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DGW",
                             doc="Dialogue"),
                   Parameter('p2', type="DGW_OBJ",
                             doc="Dialogue Object"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DGW_OBJECT`"),
                   Parameter('p4', type="META"),
                   Parameter('p5', type="META_TOKEN",
                             doc="Object"),
                   Parameter('p6', type="META_TOKEN",
                             doc="Attribute")
               ]),

        Method('SetInfoSYS_DGW', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="""
               This sets a text object to the text found in a system
               parameter variable. If the variable has not been set,
               the text is not set.
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DGW",
                             doc="Dialogue"),
                   Parameter('p2', type="DGW_OBJ",
                             doc="Dialogue Object"),
                   Parameter('p3', type=Type.INT32_T,
                             doc=":def:`DGW_OBJECT`"),
                   Parameter('p4', type=Type.STRING,
                             doc="Group name of the Variable"),
                   Parameter('p5', type=Type.STRING,
                             doc="Variable name")
               ]),

        Method('SetTitle_DGW', module='None', version='5.0.0',
               availability=Availability.PUBLIC, is_app=True, 
               doc="Changes the title of the dialog.",
               notes="""
               A "Special", additional title can be added to a dialog by using
               the following syntax:
               
               :func:`SetTitle_DGW`(Diag, "Window Title\\nAdditional Title");
               
               In the title argument, a line break character '\\n' is used to
               separate the parts.
               
               The window title free_appears as the title in the upper bar of the dialog.
               The additional title free_appears below this, in the main body of the
               dialog, and is separated from the rest of the fields by a horizontal
               line. It is printed in the bold version of the default font (or of the
               special font specified using the MONTAJ.GX_TITLE_FONT parameter noted
               above in "Setting Fonts in GX dialogs."
               """,
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="DGW",
                             doc="Dialogue"),
                   Parameter('p2', type=Type.STRING,
                             doc="Title to set")
               ])
    ]
}

