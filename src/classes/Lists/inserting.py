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
        
    def INSERT (self, mainName: str, mainString:  str)    :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 

        if len( self.arguments ) == 2:
            if   self.arguments[ 0 ] == 'pos'   :
                if   self.arguments[ 1 ] == 'master'    : 
                    if   self.value[ 0 ]    is None  and self.value[ 1 ] is not None :  
                        self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['pos']] ) 
                    elif self.value[ 1 ]    is None  and self.value[ 0 ] is not None :  
                        self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['master']] )
                    elif self.value[ 0 ]    is None  and self.value[ 1 ] is None     :  
                        self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['pos'], ['master']] )
                    else: 
                        self.newValues = []
                        for value in self.value:
                            self.dict_value, self.error = self.affectation.AFFECTATION(value,
                                                                    value, self.DataBase, self.line ).DEEP_CHECKING()
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
                                                self.newValues.append( self.final_val[ 0 ] )
                                            else: pass 
                                        else: self.error =  er.ERRORS( self.line ).ERROR0( mainString )
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass

                        if self.error is None:
                            try: 
                                if type( self.newValues[ 0 ] ) == type( int() ) :
                                    self.master.insert( self.newValues[ 0 ], self.newValues[ 1 ])
                                    self._return_ = self.master[ : ]
                                    del self.newValues
                                else: self.error =  er.ERRORS( self.line ).ERROR3( "pos" )
                            except IndexError : self.error =  er.ERRORS( self.line ).ERROR28( )
                        else: pass      
                elif self.arguments[ 1 ] == 'pos'       : 
                    self.error =  er.ERRORS( self.line ).ERROR16( self.function, 'pos')
                else:
                    if self.value[ 1 ] is None :
                        if self.value[ 0 ] is None: self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['pos']] ) 
                        else:
                            self.newValues = []
                            self.allValues = [ self.value[ 0 ], self.arguments[ 1 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION( value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ): 
                                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None: 
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                    self.DataBase, self.line).ANALYSE( mainString )
                                                if self.error is None:
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error =  er.ERRORS( self.line ).ERROR0( mainString )
                                        else: pass 
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass 
                            
                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( int() ) :
                                        self.master.insert( self.newValues[ 0 ], self.newValues[ 1 ])
                                        self._return_ = self.master[ : ]
                                        del self.newValues
                                        del self.allValues
                                    else: self.error =  er.ERRORS( self.line ).ERROR3( "pos" )
                                except IndexError : self.error =  er.ERRORS( self.line ).ERROR28( )
                            else: pass   
                    else: self.error =  er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )      
            elif self.arguments[ 0 ] == 'master': 
                if   self.arguments[ 1 ] == 'pos'       : 
                    if   self.value[ 0 ]    is None  and self.value[ 1 ] is not None :  
                        self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                    elif self.value[ 1 ]    is None  and self.value[ 0 ] is not None :  
                        self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['pos']] )
                    elif self.value[ 0 ]    is None  and self.value[ 1 ] is None     :  
                        self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['pos'], ['master']] )
                    else: 
                        self.newValues = []
                        for value in self.value:
                            self.dict_value, self.error = self.affectation.AFFECTATION(value,
                                                                    value, self.DataBase, self.line ).DEEP_CHECKING()
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
                                                self.newValues.append( self.final_val[ 0 ] )
                                            else: pass 
                                        else: pass 
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass

                        if self.error is None:
                            try: 
                                if type( self.newValues[ 1 ] ) == type( int() ) :
                                    self.master.insert( self.newValues[ 1 ], self.newValues[ 0 ])
                                    self._return_ = self.master[ : ]
                                    del self.newValues
                                else: self.error =  er.ERRORS( self.line ).ERROR3( "pos" )
                            except IndexError : self.error =  er.ERRORS( self.line ).ERROR28( )
                        else: pass
                elif self.arguments[ 1 ] == 'master'    :
                    self.error =  er.ERRORS( self.line ).ERROR16( self.function, 'master')
                else:
                    if self.value[ 1 ] is None :
                        if self.value[ 0 ] is None: self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                        else:
                            self.newValues = []
                            self.allValues = [ self.arguments[ 1 ], self.value[ 0 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION( value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ): 
                                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None: 
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                    self.DataBase, self.line).ANALYSE( mainString )
                                                if self.error is None:
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error =  er.ERRORS( self.line ).ERROR0( mainString ) 
                                        else: pass 
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass 
                            
                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( int() ) :
                                        self.master.insert( self.newValues[ 0 ], self.newValues[ 1 ])
                                        self._return_ = self.master[ : ]
                                        del self.newValues
                                        del self.allValues
                                    else: self.error =  er.ERRORS( self.line ).ERROR3( "pos" )
                                except IndexError : self.error =  er.ERRORS( self.line ).ERROR28( )
                            else: pass   
                    else: self.error =  er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )      
            else:
                if self.value[ 0 ] is None: 
                    if self.arguments[ 1 ] == 'master': 
                        if self.value[ 1 ] is None  : self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                        else: 
                            self.newValues = []
                            self.allValues = [ self.arguments[ 0 ], self.value[ 1 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION(value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
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
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error =  er.ERRORS( self.line ).ERROR0( mainString ) 
                                        else: pass
                                    else: 
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass

                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( int() ) :
                                        self.master.insert( self.newValues[ 0 ], self.newValues[ 1 ])
                                        self._return_ = self.master[ : ]
                                        del self.newValues
                                        del self.allValues
                                    else: self.error =  er.ERRORS( self.line ).ERROR3( "pos" )
                                except IndexError : self.error =  er.ERRORS( self.line ).ERROR28( )
                            else: pass
                    else:
                        if self.value[ 1 ] is None :
                            self.newValues = []
                            self.allValues = [ self.arguments[ 0 ], self.arguments[ 1 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION( value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ): 
                                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None: 
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                    self.DataBase, self.line).ANALYSE( mainString )
                                                if self.error is None:
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error =  er.ERRORS( self.line ).ERROR0( mainString )
                                        else: pass 
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass 
                            
                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( int() ) :
                                        self.master.insert( self.newValues[ 0 ], self.newValues[ 1 ])
                                        self._return_ = self.master[ : ]
                                        del self.newValues
                                        del self.allValues
                                    else: self.error =  er.ERRORS( self.line ).ERROR3( "pos" )
                                except IndexError : self.error =  er.ERRORS( self.line ).ERROR28( )
                            else: pass   
                        else: self.error =  er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )
                else: self.error =  er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else:  self.error =  er.ERRORS( self.line ).ERROR12( self.function, 2)

        return self._return_, self.error 