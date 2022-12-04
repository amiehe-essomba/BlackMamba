from src.functions                  import error            as er
from src.transform                  import error            as err
from script.LEXER.FUNCTION          import transformation   as t  
from script.PARXER.LEXER_CONFIGURE  import numeric_lexer    as NL
from script.STDIN.LinuxSTDIN        import bm_configure     as bm
from src.functions                  import updating_data, type_of_data


cdef class internal:
    cdef public:
        str master:
        dict data_base
        unsigned long long int line 
    cdef:
        dict error, values, var_type
        list type
        str str_type, string, func
        dict final_value

    def __cinit__(self, master, data_base, line):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.error          = {"s":None}
        self.values         = {"s":None}
        self.typ            = []
        self.var_type       = {"s":""}
        self.str_type       = ""
        self.string         = ""
        self.func           = ""
        self.final_value    = {"s":None}

    cdef integer( self ):
        cdef :
            signed long long int x
            
        self.typ = ['float', 'int', 'string', 'bool']
        self.values['s'], self.error['s'] = NL.NUMERCAL_LEXER( self.master, self.data_base, self.line).LEXER( self.master )
        if self.error['s'] is None: pass 
            self.var_type['s'] = type_of_data.CHECK_TYPE_OF_DATA( self.values['s'] ).DATA()
            if self.var_type['s'] not in self.typ:
                for x in range(len(self.typ)):
                    self.str_type   = type_of_data.CHECK_TYPE_OF_DATA( self.typ[ x ] ).TYPE()
                    if x < len( self.type ) - 1: self.string += self.str_type + ', or '
                    else                                    : self.string += self.str_type
                self.error['s'] = er.ERRORS( self.line ).ERROR3( input, self.string, self.func)
                break
            else: 
                try: self.final_value['s'] = int( float( self.values['s'] ))
                except (ValueError, TypeError):
                    self.func = bm.fg.rbg(0, 255, 0   )+' in integer( ).' + bm.init.reset 
                    self.error['s'] = err.ERRORS( self.line ).ERROR2( self.value, func=func )
        else: pass

        return self.final_value['s'], self.error['s']

