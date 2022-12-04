from script.LEXER.FUNCTION                              import main
from src.functions                                      import function

cdef class retuning:
    cdef public:
        str master
        dict data_base
        unsigned long long int line 
        dict regular_expression
    
    cdef:
        dict error, lexer, normal_expression, function_info
        str func_names
        dict expression, dictionary, _return_, library
        list vals_computed, vars_computed, default_vals, default_vars, typ, history_of_data

    def __cinit__(master, data_base, line, regular_expression):
        self.master             = master
        self.data_base          = data_base
        self.line               = line  
        self.regular_expression = regular_expression
        self.expression         = {'s':None}
        self.error              = {'s':None}
        self.normal_expression  = {"s":None}
        self.function_info      = {"s":None}
        self._return_           = {"s":None}
        self.library            = self.data_base[ 'LIB' ]
    
    cpdef internal(self, str name ):
        cdef:
            dict dict_ = {'functions' = []}

        self.dictionary             = {
            'function_name'         : None
            'arguments'             : None,
            'values'                : None,
            'type'                  : None
            'history'               : None
        }
        
        self.function_name                  = self.regular_expressions[ 'names' ][ 0 ]
        self.expression['s']                = 'def' + ' ' + self.regular_expressions[ 'expressions' ] + ' ' + ':'

        if self.function_name in self.library[ 'func_names' ]
            self.function_location              = self.library[ 'func_names' ].index( self.function_name )
            self.function_info['s']             = self.library[ 'func_names' ][ self.function_location ]
            self.lexer['s'], self.normal_expression['s'], self.error['s'] = main.MAIN( self.expression, self.dictionary,
                                                                            self.line ).MAIN( def_key = 'indirect' )
            if self.error['s'] is None:
                self._return_['s'],  self.error['s'] = function.FUNCTION( dict_[ 'functions' ]  ,
                                 self.data_base, self.line ).DOUBLE_INIT_FUNCTION( self.normal_expression['s'], self.function_name )
                if self.error['s'] is None:
                    self.vars_computed  = self.lexer['s']['def']['arguments']
                    self.vals_computed  = self.lexer['s']['def']['value']
                    self.default_vals   = self.function_info['s'][ self.function_name][ 'value' ]  
                    self.default_vars   = self.function_info['s'][ self.function_name][ 'arguments' ]  
                    self.typ            = self.function_info['s'][ self.function_name][ 'type' ] 
                    self.history_of_data= self.function_info['s'][ self.function_name][ 'history_of_data' ] 
                    self.liction        = self._return_['s']['location']

                    if self.values:
                        if len(self.vars_computed) == len(self.default_vars):
                            self.dictionary['functioni_name']   = self.function_name
                            self.dictionary['arguments']        = self.default_vars
                            self.dictionary['values']           = self.default_vals
                            self.dictionary['history']          = self.history_of_data
                            self.dictionary['type']             = self.typ
                        else: pass
                else: pass 
            else: pass 
