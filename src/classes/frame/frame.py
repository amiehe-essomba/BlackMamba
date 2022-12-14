from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation


class DATA:
    def __init__(self, DataBase: dict, line:int, master: str, function, FunctionInfo : list ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        self.lexer          = main_lexer
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        
    def FRAME( self, mainName: str, mainString: str ):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if self.function in [ 'keys' ]            :
            if None in self.arguments: 
                self._return_ = list(self.master.keys())
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        else:
            if None in self.arguments: 
                self.dict_value, self.error = self.affectation.AFFECTATION( self.value[ 0 ],
                                                                self.value[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                if self.error is None:
                    if 'operator' not in list( self.dict_value.keys() ): 
                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                        if self.error is None: 
                            self.all_data = self.lex[ 'all_data' ]
                            if self.all_data is not None:
                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                self.DataBase,self.line).ANALYSE( mainString )
                            else: self.error = er.ERRORS( self.line ).ERROR0( mainString )       
                        else: pass 
                    else:
                        self.operator = self.dict_value[ 'operator' ]
                        self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                else: pass
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )   
            
        return self._return_, self.error