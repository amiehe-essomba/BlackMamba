from script                                         import control_string as CS
from script.LEXER                                   import particular_str_selection as PS
from script.LEXER                                   import check_if_affectation as CA
from script.LEXER                                   import main_lexer as ML
from script.PARXER.INTERNAL_FUNCTION                import get_tuple as err

cdef class TUPLE:
    cdef public :
        dict master, data_base
        unsigned long long int line  
    cdef : 
        dict error,numeric, string, value, dict_value
        dict  typ, main_dict, _return_,
        list historyOfFunctions, tupleFunctions
        list variables

    def __cinit__(self, master, data_base, line):
        self.line                       = line
        self.master                     = master
        self.data_base                  = data_base
        self.error                      = {'s':None}
        self.variables                  = self.data_base[ 'variables' ][ 'vars' ]
        self.dict_value                 = {'s':None}

    cdef TUPLE(self):
        cdef:
            dict true_value = {'s':None}
            dict check_dot  = {'s':None} 
            dict lex, all_data = {'s':None}

        self.typ                        = {'s':self.master[ 'type' ]}
        self.main_dict                  = {'s':self.master[ 'numeric' ][ 0 ]}
        self._return_                   = {'s':[]}
        self.value                      = {'s':None}

        self.string     = {'s':self.main_dict[ 1: -1]}
        self.string['s'], self.error['s'] = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( self.string )
        
        if self.error['s'] is None:
            self.value['s'], self.error['s'] = self.selection.SELECTION( self.string['s'], self.string['s'], self.data_base,
                                                        self.line).CHAR_SELECTION( ',' )
            if self.error['s'] is None:
                for _value_ in self.value:
                    true_value['s'], self.error['s'] = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( _value_ )
                    
                    if self.error['s'] is None:
                        check_dot['s'], self.error['s'] = PS.SELECTION(true_value['s'], true_value['s'],
                                                                self.data_base,self.line).CHAR_SELECTION( ':' )
                        if self.error['s'] is None:
                            if len( check_dot['s'] ) == 1:
                                self.dict_value['s'], self.error['s'] = CA.AFFECTATION(true_value['s'],
                                                            true_value['s'],self.data_base, self.line ).DEEP_CHECKING()
                                if self.error['s'] is None:
                                    if 'operator' not in list( self.dict_value['s'].keys() ):
                                        lex, self.error['s'] = ML.FINAL_LEXER( self.string['s'], self.data_base,
                                                                        self.line).FINAL_LEXER( self.dict_value['s'], _type_ = None )
                                        if self.error['s'] is None:
                                            all_data['s'] = lex[ 'all_data' ]
                                            if all_data['s'] is not None: pass
                                            else : 
                                                self.error['s'] = err.ERRORS( self.line ).ERROR0( self.main_dict['s'] )
                                                break
                                        else: break
                                    else: 
                                        self.error['s'] = err.ERRORS( self.line ).ERROR0(self.main_dict['s'], 
                                                           self.dict_value['s'][ 'operator' ])
                                        break
                                else: break
                            else: 
                                self.error['s'] = err.ERRORS( self.line ).ERROR1( self.main_dict['s'], ':' )
                                break
                        else: break
                    else: 
                        self.error['s'] = err.ERRORS( self.line ).ERROR0( self.main_dict['s'] )
                        break
            else: pass
        else: pass

    cpdef MAIN_TUPLE(self, str main_string):
        cdef:
            dict tuple_values

        self.numeric            = {'s':self.master[ 'numeric' ]}
        self.historyOfFunctions = []
        self.tupleFunctions     = [ 'empty', 'init', 'enumerate', 'size', 'choice', 'index', 'count'] 

        if self.numeric['s'] is not None:
            tuple_values, self.error['s'] = TUPLE( self.master, self.data_base, self.line ).TUPLE()
        else : pass

        return tuple_values, self.error['s']