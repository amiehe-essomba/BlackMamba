from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation
from src.classes.matrix                             import checking_2D as c2D
from src.transform                                  import matrix_statistics as mstat
from script.STDIN.LinuxSTDIN 	                    import bm_configure as bm

class MATRIX_2D:
    def __init__(self, DataBase: dict, line:int, master: str, function: str, FunctionInfo : list ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        self.lexer          = main_lexer
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        
    def MATRIX_2D(self, mainName: str, mainString:  str, name_2D: list = [])    :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        self.main_dict      = mainString
        self.master, self.nrow, self.ncol, self.master_one = c2D.Array( self.master )
        self._values_       = [self.master_one, self.nrow, self.ncol] 
        
        if self.function not in ['round', "quantile"]:
            if   len( self.arguments ) == 2:
                if   self.arguments[ 0 ] == name_2D[0]      :
                    if   self.arguments[ 1 ] == name_2D[1]  : 
                        if   self.value[ 0 ]    is None  and self.value[ 1 ] is not None :  
                            self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name_2D[0]]] ) 
                        elif self.value[ 1 ]    is None  and self.value[ 0 ] is not None :  
                            self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name_2D[1]]] )
                        elif self.value[ 0 ]    is None  and self.value[ 1 ] is None     :  
                            self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name_2D[0]], [name_2D[1]]] )
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
                                            else: self.error = er.ERRORS( self.line ).ERROR0( mainString )
                                        else: pass
                                    else: 
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass

                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( bool() ) :
                                        if type( self.newValues[ 1 ] ) in [type(int()), type(None)] :
                                            self._values_ += [self.newValues[ 0 ], self.function, self.newValues[ 1 ], "matrix"] 
                                            if self.newValues[ 1 ] is None: pass 
                                            else: 
                                                if self.newValues[ 1 ] < self.ncol: self.master = self.master[ self.newValues[ 1 ] ]
                                                else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                            
                                            if self.error is None: 
                                                self.master, self.error = c2D.reverse( self._values_)
                                                if self.error is None:
                                                    self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                                                else: pass 
                                                del self.newValues
                                            else: pass
                                        else: self.error = er.ERRORS( self.line ).ERROR3(name_2D[0], 'an integer() or none()' )
                                    else: self.error = er.ERRORS( self.line ).ERROR3(name_2D[1], 'a boolean()'  )
                                except IndexError : self.error = er.ERRORS( self.line ).ERROR28( )
                            else: pass      
                    elif self.arguments[ 1 ] == name_2D[0]  :  self.error = er.ERRORS( self.line ).ERROR16( self.function, name_2D[0])
                    else:
                        if self.value[ 1 ] is None :
                            if self.value[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name_2D[0]]] ) 
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
                                                else: self.error = er.ERRORS( self.line ).ERROR0( mainString )
                                            else: pass 
                                        else:
                                            self.operator = self.dict_value[ 'operator' ]
                                            self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                    else: pass 
                                
                                if self.error is None:
                                    try: 
                                        if type( self.newValues[ 0 ] ) == type( bool() ) :
                                            if type( self.newValues[ 1 ] ) in [type( int() ), type(None)] : 
                                                self._values_ += [self.newValues[ 0 ], self.function, self.newValues[ 1 ], "matrix"] 
                                                if self.newValues[ 1 ] is None: pass 
                                                else: 
                                                    if self.newValues[ 1 ] < self.ncol: self.master = self.master[ self.newValues[ 1 ] ]
                                                    else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                                
                                                if self.error is None: 
                                                    self.master, self.error = c2D.reverse( self._values_)
                                                    if self.error is None:
                                                        self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                                                    else: pass 
                                                    del self.newValues
                                                    del self.allValues
                                                else: pass
                                            else: self.error = er.ERRORS( self.line ).ERROR3(name_2D[0], 'an integer() or none()'  )
                                        else: self.error = er.ERRORS( self.line ).ERROR3(name_2D[0], 'a boolean()' )
                                    except IndexError : self.error = er.ERRORS( self.line ).ERROR28( )
                                else: pass   
                        else: self.error = er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )                
                elif self.arguments[ 0 ] == name_2D[1]: 
                    if   self.arguments[ 1 ] == name_2D[0]  : 
                        if   self.value[ 0 ]    is None  and self.value[ 1 ] is not None :  
                            self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name_2D[1]]] ) 
                        elif self.value[ 1 ]    is None  and self.value[ 0 ] is not None :  
                            self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name_2D[0]]] )
                        elif self.value[ 0 ]    is None  and self.value[ 1 ] is None     :  
                            self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name_2D[1]], [name_2D[0]]] )
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
                                        self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass
                           
                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) in [type( int() ), type(None)] :
                                        if type( self.newValues[ 1 ] ) == type( bool() ) :
                                            self._values_ += [self.newValues[ 1 ], self.function, self.newValues[ 0 ], "matrix"] 
                                            if self.newValues[ 0 ] is None: pass 
                                            else: 
                                                if self.newValues[ 0 ] < self.ncol: self.master = self.master[ self.newValues[ 0 ] ]
                                                else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                            
                                            if self.error is None: 
                                                self.master, self.error = c2D.reverse( self._values_)
                                                if self.error is None:
                                                    self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                                                else: pass 
                                                del self.newValues
                                            else: pass
                                        else: self.error = er.ERRORS( self.line ).ERROR3( name_2D[0], 'a boolean()' )
                                    else: self.error =er. ERRORS( self.line ).ERROR3( name_2D[1], 'an integer() or none()' )
                                except IndexError : self.error = er.ERRORS( self.line ).ERROR28( )
                            else: pass
                    elif self.arguments[ 1 ] == name_2D[1]  : self.error = er.ERRORS( self.line ).ERROR16( self.function, name_2D[1])
                    else:
                        if self.value[ 1 ] is None :
                            if self.value[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name_2D[1]]] ) 
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
                                                else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                                            else: pass 
                                        else:
                                            self.operator = self.dict_value[ 'operator' ]
                                            self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                    else: pass 
                                
                                if self.error is None:
                                    try: 
                                        if type( self.newValues[ 1 ] ) in [type( int() ), type(None)] :
                                            if type( self.newValues[ 0 ] ) == type( bool() ) :
                                                self._values_ += [self.newValues[ 0 ], self.function, self.newValues[ 1 ], "matrix"] 
                                                if self.newValues[ 1 ] is None: pass 
                                                else: 
                                                    if self.newValues[ 1 ] < self.ncol: self.master = self.master[ self.newValues[ 1 ] ]
                                                    else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                                
                                                if self.error is None: 
                                                    self.master, self.error = c2D.reverse( self._values_)
                                                    if self.error is None:
                                                        self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                                                    else: pass 
                                                    del self.newValues
                                                    del self.allValues
                                                else: pass
                                            else: self.error = er.ERRORS( self.line ).ERROR3(name_2D[0], 'a boolean()' )
                                        else: self.error = er.ERRORS( self.line ).ERROR3( name_2D[1], 'an integer() or none()' )
                                    except IndexError : self.error = er.ERRORS( self.line ).ERROR28( )
                                else: pass   
                        else: self.error = er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )        
                else:
                    if self.value[ 0 ] is None: 
                        if self.arguments[ 1 ] == name_2D[1]: 
                            if self.value[ 1 ] is None  : self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name_2D[1]]] ) 
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
                                                else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                                            else: pass
                                        else: 
                                            self.operator = self.dict_value[ 'operator' ]
                                            self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                    else: pass

                                if self.error is None:
                                    try: 
                                        if type( self.newValues[ 0 ] ) == type( bool() ) :
                                            if type( self.newValues[ 1 ] ) in [type( int() ), type(None)] :
                                                self._values_ += [self.newValues[ 0 ], self.function, self.newValues[ 1 ], "matrix"] 
                                                if self.newValues[ 1 ] is None: pass 
                                                else: 
                                                    if self.newValues[ 1 ] < self.ncol: self.master = self.master[ self.newValues[ 1 ] ]
                                                    else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                                
                                                if self.error is None: 
                                                    self.master, self.error = c2D.reverse( self._values_)
                                                    if self.error is None:
                                                        self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                                                    else: pass 
                                                    del self.newValues
                                                    del self.allValues 
                                                else: pass
                                            else: self.error = er.ERRORS( self.line ).ERROR3( name_2D[1], 'an interger() or none()' )
                                        else: self.error = er.ERRORS( self.line ).ERROR3( name_2D[0], 'a boolean()' )
                                    except IndexError : self.error = er.ERRORS( self.line ).ERROR28( )
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
                                                else: self.error = er.ERRORS( self.line ).ERROR0( mainString )
                                            else: pass 
                                        else:
                                            self.operator = self.dict_value[ 'operator' ]
                                            self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                    else: pass 
                                
                                if self.error is None:
                                    try: 
                                        if type( self.newValues[ 0 ] ) == type( bool() ) :
                                            if type( self.newValues[ 1 ] ) in [type( int() ), type(None)] :
                                                self._values_ += [self.newValues[ 0 ], self.function, self.newValues[ 1 ], "matrix"] 
                                                
                                                if self.newValues[ 1 ] is None: pass 
                                                else: 
                                                    if self.newValues[ 1 ] < self.ncol: self.master = self.master[ self.newValues[ 1 ] ]
                                                    else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                                
                                                if self.error is None: 
                                                    self.master, self.error = c2D.reverse( self._values_)
                                                    if self.error is None:
                                                        self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                                                    else: pass 
                                                    del self.newValues
                                                    del self.allValues 
                                                else: pass
                                            else: self.error = er.ERRORS( self.line ).ERROR3( name_2D[0], 'an integer() or none()' )
                                        else: self.error = er.ERRORS( self.line ).ERROR3( name_2D[0], 'a boolean()' ) 
                                    except IndexError : self.error = er.ERRORS( self.line ).ERROR28( )
                                else: pass   
                            else: self.error = er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )
                    else: self.error = er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
            elif len( self.arguments ) == 1:
                if     self.arguments[ 0 ] == name_2D[0]: 
                    if self.value[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name_2D[0]]] ) 
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
                                                self._values_ += [self.newValues, self.function, None, "matrix"]  
                                                self.master, self.error = c2D.reverse( self._values_)
                                                if self.error is None:
                                                    self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                                                else: pass 
                                            else: self.error = er.ERRORS( self.line ).ERROR3( name_2D[0], 'a boolean()')   
                                        else: pass 
                                    else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                                else: pass
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass 
                elif   self.arguments[ 0 ] == name_2D[1]: 
                    if self.value[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name_2D[1]]] ) 
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
                                            if type( self.newValues ) in [type( int() ), type(None)]:
                                                self._values_ += [False, self.function, self.newValues, "matrix"]  
                                                if self.newValues is None: pass 
                                                else: 
                                                    if self.newValues < self.ncol: self.master = self.master[ self.newValues ]
                                                    else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                                
                                                if self.error is None: 
                                                    self.master, self.error = c2D.reverse( self._values_)
                                                    if self.error is None:
                                                        self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                                                    else: pass 
                                                else: pass
                                            else: self.error = er.ERRORS( self.line ).ERROR3( name_2D[0], 'an integer() or none()')   
                                        else: pass 
                                    else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                                else: pass
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass 
                else:
                    if self.arguments[ 0 ] is None: 
                        self._values_ += [False, self.function, None, "matrix"]  
                        self.master, self.error = c2D.reverse( self._values_)
                        if self.error is None:
                            self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                        else: pass 
                    else:
                        if self.value[ 0 ] is None:
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
                                                    self._values_ += [self.newValues, self.function, None, "matrix"]  
                                                    self.master, self.error = c2D.reverse( self._values_)
                                                    if self.error is None:
                                                        self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                                                    else: pass 
                                                else: self.error = er.ERRORS( self.line ).ERROR3( name_2D[0], 'a boolean()')   
                                            else: pass 
                                        else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass
                        else: self.error = er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
            elif len( self.arguments ) == 0:
                self._values_ += [False, self.function, None, "matrix"]  
                self.master, self.error = c2D.reverse( self._values_)
                if self.error is None:
                    self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                else: pass 
            else: self.error = er.ERRORS( self.line ).ERROR12( self.function, 2)
        else: self.error = er.ERRORS( self.line ).ERROR56( self.function )
      
        return self._return_, self.error