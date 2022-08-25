from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation

class LIST:
    def __init__(self, 
                DataBase    : dict, 
                line        : int, 
                master      : str, 
                function    : any, 
                FunctionInfo: list 
                ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        self.lexer          = main_lexer
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        
    def SOERTED(self, mainName: str, mainString:  str)    :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'reverse': 
                if self.value[ 0 ] is None: self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['reverse']] ) 
                else: 
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
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if type( self.newValues ) == type( bool() ):
                                            if self.master:
                                                try:
                                                    self._return_   = sorted( self.master , reverse=self.newValues)
                                                    self.master     = self._return_
                                                except TypeError:
                                                    for i in range( len( self.master )):
                                                        if type( self.master[i]) not in [ type(float()), type(int()), type(bool())]:
                                                            self.error =  er.ERRORS( self.line ).ERROR35( i )
                                                            break
                                                        else: pass
                                            else: self.error =  er.ERRORS( self.line ).ERROR24( 'list' )
                                        else: self.error =  er.ERRORS( self.line ).ERROR3( "reverse", 'a boolean()')   
                                    else: pass 
                                else: self.error =  er.ERRORS( self.line ).ERROR0( mainString ) 
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            else:
                if self.arguments[ 0 ] is None:
                    if self.master:
                        try:
                            self._return_   = sorted( self.master , reverse=False)
                            self.master     = self._return_
                        except TypeError:
                            for i in range( len( self.master )):
                                if type( self.master[i]) not in [ type(float()), type(int()), type(bool())]:
                                    self.error =  er.ERRORS( self.line ).ERROR35( i )
                                    break
                            else: pass
                    else: self.error =  er.ERRORS( self.line ).ERROR24( 'list' )
                else:
                    if self.value[ 0 ] is None:
                        if self.master:
                            self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                    self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase,self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues = self.final_val[ 0 ]
                                                if type( self.newValues ) == type( bool() ):
                                                    if self.master:
                                                        try:
                                                            self._return_   = sorted( self.master , reverse=self.newValues)
                                                            self.master     = self._return_
                                                        except TypeError:
                                                            for i in range( len( self.master )):
                                                                if type( self.master[i]) not in [ type(float()), type(int()), type(bool())]:
                                                                    self.error =  er.ERRORS( self.line ).ERROR35( i )
                                                                    break
                                                                else: pass
                                                    else: self.error =  er.ERRORS( self.line ).ERROR24( 'list' )
                                                else: self.error =  er.ERRORS( self.line ).ERROR3( "reverse", 'a boolean()')   
                                            else: pass 
                                        else: self.error =  er.ERRORS( self.line ).ERROR0( mainString ) 
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass
                        else: self.error =  er.ERRORS( self.line ).ERROR24( 'list' )
                    else: self.error =  er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error =  er.ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error