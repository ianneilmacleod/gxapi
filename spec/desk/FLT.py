from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('FLT',
                 handle_name='FILTER',
                 doc="The :class:`FLT` class allows the application of user-defined convolution filters to data in an OASIS database")





gx_methods = {
    'Miscellaneous': [

        Method('Create_FLT', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="create a filter from a comma/space delimited string.",
               notes="""
               Terminates process if filter not found.
               Sample Fraser Filter string:
               
                     "-1,-1,1,1"
               """,
               return_type="FILTER",
               return_doc=":class:`FLT` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Filter string")
               ]),

        Method('Destroy_FLT', module='geogxx', version='5.0.0',
               availability=Availability.PUBLIC, 
               doc="This method destroys a filter handle",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="FILTER",
                             doc=":class:`FILTER` object to destroy")
               ]),

        Method('Load_FLT', module='geogxx', version='5.0.0',
               availability=Availability.LICENSED, 
               doc="Load and return handle to a convolution filter.",
               notes="""
               Terminates process if filter not found.
               A filter file is an ASCII file that contains filter
               coefficients, which are simply mumbers.  There can be
               one coefficient to a line.  Blank lines and comment lines
               are skipped.  Comment lines beginn with a forward slash
               character in column 1.  Following is an example Fraser
               Filter file:
               
                  /----------------------
                  / Fraser Filter
                  /----------------------
                  -1
                  -1
                  1
                  1
               """,
               return_type="FILTER",
               return_doc=":class:`FLT` Object",
               parameters = [
                   Parameter('p1', type=Type.STRING,
                             doc="Name of the filter File")
               ])
    ]
}

