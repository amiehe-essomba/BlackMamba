from script                                         import control_string
from script.LEXER                                   import particular_str_selection
from script.LEXER                                   import main_lexer
from script.LEXER                                   import check_if_affectation
from script.PARXER                                  import numerical_value
from script.LEXER.FUNCTION                          import main
from script.STDIN.LinuxSTDIN                        import bm_configure as bm
from script.PARXER.INTERNAL_FUNCTION                import get_list
from src.classes.Tuples                             import Tuples
from src.classes                                    import error as er        

class TUPLE:
    def __init__(self, master: dict, data_base: dict, line: int):
        self.line                       = line
        self.master                     = master
        self.data_base                  = data_base

        self.control                    = control_string.STRING_ANALYSE(self.data_base, self.line)
        self.selection                  = particular_str_selection
        self.lexer                      = main_lexer
        self.numeric                    = numerical_value
        self.affectation                = check_if_affectation
        self.variables                  = self.data_base[ 'variables' ][ 'vars' ]

    def TUPLE(self):
        self.error                      = None
        self.type                       = self.master[ 'type' ]
        self.main_dict                  = self.master[ 'numeric' ][ 0 ]
        self._return_                   = []
        self.all_data                   = None

        self.string     = self.main_dict[ 1: -1]
        self.string, self.error = self.control.DELETE_SPACE( self.string )
        if self.data_base['Transpiler_for']['residus_head']['complete'] is False:
            self.data_base['Transpiler_for']['residus_head']['val'] = self.main_dict
        else: pass
        if self.error is None:
            self.value, self.error = self.selection.SELECTION( self.string, self.string, self.data_base,
                                                        self.line).CHAR_SELECTION( ',' )
            if self.error is None:
                for _value_ in self.value:
                    self.true_value, self.error = self.control.DELETE_SPACE( _value_ )
                    
                    if self.error is None:
                        self.check_dot, self.error = self.selection.SELECTION(self.true_value, self.true_value,
                                                                self.data_base,self.line).CHAR_SELECTION( ':' )
                        if self.error is None:
                            if len( self.check_dot ) == 1:
                                self.dict_value, self.error = self.affectation.AFFECTATION(self.true_value,
                                                            self.true_value,self.data_base, self.line ).DEEP_CHECKING()

                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ):
                                        self.lex, self.error = self.lexer.FINAL_LEXER( self.string, self.data_base,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None:
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None: self._return_ .append(self.all_data )
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.main_dict )
                                                break
                                        else:  break
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = ERRORS( self.line ).ERROR0(self.main_dict, self.operator )
                                        break
                                else: break
                            else:
                                self.error = ERRORS( self.line ).ERROR1( self.main_dict, ':' )
                                break
                        else:  break
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.main_dict )
                        break
            else: pass
        else: pass

        return self._return_, self.error

    def MAIN_TUPLE(self, main_string: str):
        self.error              = None
        self.numeric            = self.master[ 'numeric' ]
        self._return_           = []
        self.historyOfFunctions = []
        self.tupleFunctions     = [ 'empty', 'init', 'enumerate', 'size', 'choice', 'index', 'count'] 

        if self.numeric is not None:
            self.tuple_values, self.error = TUPLE( self.master, self.data_base, self.line ).TUPLE()
            return self.tuple_values, self.error 
        else: return None, None 
            