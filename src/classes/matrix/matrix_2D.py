import numpy as np
from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation
from src.classes.matrix                             import checking_2D as c2D
from src.transform                                  import matrix_statistics as mstat
from script.STDIN.LinuxSTDIN 	                    import bm_configure as bm
from src.transform                                  import datatype as dt

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
        self.master_copy    = self.master.copy()
        self.master, self.nrow, self.ncol, self.master_one = c2D.Array( self.master )
        self._values_       = [self.master_one, self.nrow, self.ncol] 
        
        if self.function in ['dtype', 'size', 'ndim', 'copy', 'owner', 'choice', 'sorted']:
            if type(self.master_copy) == type(np.array([1])):
                if   self.function == 'dtype'   : self._return_ = dt.data( str( self.master_copy.dtype ) ).type()
                elif self.function == 'ndim'    : self._return_ = list(self.master_copy.shape)
                elif self.function == 'copy'    : self._return_ = self.master_copy.copy()
                elif self.function == 'sorted'  : self.master_copy.sort(); self._return_ = self.master_copy.copy()
                elif self.function == 'choice'  : 
                    if len( list( self.master_copy.shape ) ) == 1:
                        self._return_ = np.random.choice(self.master_copy)
                    elif len( list( self.master_copy.shape ) ) == 2:
                        self.shape = list( self.master_copy.shape )
                        self._return_ = []
                        for i in range(self.shape[0]):
                            self._return_.append(np.random.choice(self.master_copy[i]))
                        self._return_ = np.array(self._return_).reshape((self.shape[0], -1))
                    else: self.error = er.ERRORS( self.line ).ERROR61( mainName )
                elif self.function == 'owner'   : 
                    self._return_ = self.master_copy.base
                    if self._return_ is None: self._return_ = False 
                    else : self._return_ = True
                else: self._return_ = np.array(self.master).size
            else: self.error = er.ERRORS( self.line ).ERROR3( mainName, "ndarray()" )
        else:
            if self.function not in ['round', "quantile"]:
                if   len( self.arguments ) == 2:
                    if   self.arguments[ 0 ] == name_2D[0]:
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
                                                print()
                                                self.master, self.error = c2D.reverse( self._values_)
                                                if self.newValues[ 1 ] is None: 
                                                    if self.newValues[ 0 ] is True:
                                                        self._values_[0], self._values_[1], self._values_[2], self._values_[5] = self.master, self.ncol, self.nrow, None
                                                    else: pass
                                                else: 
                                                    if  self.newValues[ 0 ] is True:
                                                        if self.newValues[ 1 ] < self.ncol: self.master = [ self.master[ self.newValues[ 1 ] ] ]
                                                        else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                                    else:
                                                        if self.newValues[ 1 ] < self.nrow: self.master = [ self.master[ self.newValues[ 1 ] ] ]
                                                        else: self.error = er.ERRORS( self.line ).ERROR55( self.nrow )
                                                            
                                                    self._values_[0], self._values_[1], self._values_[2], self._values_[5] = self.master, 1, len(self.master[0]), None
                                                
                                                if self.error is None:
                                                    self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
                                                else: pass 
                                                del self.newValues
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
                                                    
                                                    self.master, self.error = c2D.reverse( self._values_)
                                                    if self.newValues[ 1 ] is None: 
                                                        if self.newValues[ 0 ] is True:
                                                            self._values_[0], self._values_[1], self._values_[2], self._values_[5] = self.master, self.ncol, self.nrow, None
                                                        else: pass
                                                    else: 
                                                        if  self.newValues[ 0 ] is True:
                                                            if self.newValues[ 1 ] < self.ncol: self.master = [ self.master[ self.newValues[ 1 ] ] ]
                                                            else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                                        else:
                                                            if self.newValues[ 1 ] < self.nrow: self.master = [ self.master[ self.newValues[ 1 ] ] ]
                                                            else: self.error = er.ERRORS( self.line ).ERROR55( self.nrow )
                                                            
                                                        self._values_[0], self._values_[1], self._values_[2], self._values_[5] = self.master, 1, len(self.master[0]), None
                                                    
                                                    if self.error is None:
                                                        self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
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
                                                
                                                self.master, self.error = c2D.reverse( self._values_)
                                                if self.newValues[ 0 ] is None: 
                                                    if self.newValues[ 1 ] is True:
                                                        self._values_[0], self._values_[1], self._values_[2] = self.master, self.ncol, self.nrow
                                                        self._values_[5] = None
                                                    else: pass
                                                else: 
                                                    if  self.newValues[ 1 ] is True:
                                                        if self.newValues[ 0 ] < self.ncol: self.master = [ self.master[ self.newValues[ 0 ] ] ]
                                                        else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                                    else:
                                                        if self.newValues[ 0 ] < self.nrow: self.master = [ self.master[ self.newValues[ 0 ] ] ]
                                                        else: self.error = er.ERRORS( self.line ).ERROR55( self.nrow )
                                                        
                                                    self._values_[0], self._values_[1], self._values_[2] = self.master, 1, len(self.master[0])
                                                    self._values_[5] = None
                                                    
                                                if self.error is None:  
                                                    self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
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
                                                    
                                                    self.master, self.error = c2D.reverse( self._values_)
                                                    if self.newValues[ 1 ] is None: 
                                                        if self.newValues[ 0 ] is True:
                                                            self._values_[0], self._values_[1], self._values_[2] = self.master, self.ncol, self.nrow
                                                            self._values_[5] = None
                                                        else: pass
                                                    else: 
                                                        if  self.newValues[ 0 ] is True:
                                                            if self.newValues[ 1 ] < self.ncol: self.master = [ self.master[ self.newValues[ 1 ] ] ]
                                                            else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                                        else:
                                                            if self.newValues[ 1 ] < self.nrow: self.master = [ self.master[ self.newValues[ 1 ] ] ]
                                                            else: self.error = er.ERRORS( self.line ).ERROR55( self.nrow )
                                                    
                                                        self._values_[0], self._values_[1], self._values_[2] = self.master, 1, len(self.master[0])
                                                        self._values_[5] = None
                                                    
                                                    if self.error is None:     
                                                        self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
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
                                                    
                                                    self.master, self.error = c2D.reverse( self._values_)
                                                    if self.newValues[ 1 ] is None: 
                                                        if self.newValues[ 0 ] is True:
                                                            self._values_[0], self._values_[1], self._values_[2] = self.master, self.ncol, self.nrow
                                                            self._values_[5] = None
                                                        else: pass
                                                    else: 
                                                        if  self.newValues[ 0 ] is True:
                                                            if self.newValues[ 1 ] < self.ncol: self.master = [ self.master[ self.newValues[ 1 ] ] ]
                                                            else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                                        else:
                                                            if self.newValues[ 1 ] < self.nrow: self.master = [ self.master[ self.newValues[ 1 ] ] ]
                                                            else: self.error = er.ERRORS( self.line ).ERROR55( self.nrow )
                        
                                                        self._values_[0], self._values_[1], self._values_[2] = self.master, 1, len(self.master[0])
                                                        self._values_[5] = None
                                                        
                                                    if self.error is None: 
                                                        self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
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
                                                    
                                                    self.master, self.error = c2D.reverse( self._values_)
                                                    if self.newValues[ 1 ] is None: 
                                                        if self.newValues[ 0 ] is True:
                                                            self._values_[0], self._values_[1], self._values_[2] = self.master, self.ncol, self.nrow
                                                            self._values_[5] = None
                                                        else: pass
                                                    else:
                                                        if  self.newValues[ 0 ] is True:
                                                            if self.newValues[ 1 ] < self.ncol: self.master = [ self.master[ self.newValues[ 1 ] ] ]
                                                            else: self.error = er.ERRORS( self.line ).ERROR55( self.ncol )
                                                        else:
                                                            if self.newValues[ 1 ] < self.nrow: self.master = [ self.master[ self.newValues[ 1 ] ] ]
                                                            else: self.error = er.ERRORS( self.line ).ERROR55( self.nrow )
                                                            
                                                        self._values_[0], self._values_[1], self._values_[2] = self.master, 1, len(self.master[0])
                                                        self._values_[5] = None
                                                    
                                                    if self.error is None: 
                                                        self._return_, self.error = mstat.R(self.master, self._values_.copy(), self.line).R()
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
                                                    self.master, self.error = c2D.reverse( self._values_.copy())
                                                    if self.newValues is True:
                                                        self._values_[0], self._values_[1], self._values_[2] = self.master, self.ncol, self.nrow
                                                    else: pass
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
                                                    self._values_ += [False, self.function, None, "matrix"]  
                                                    if self.newValues is None: pass 
                                                    else: 
                                                        if self.newValues < self.nrow: 
                                                            self.master = [self.master[ self.newValues ]]
                                                            self._values_[0], self._values_[1], self._values_[2] = self.master.copy(), 1, self.ncol 
                                                        else: self.error = er.ERRORS( self.line ).ERROR55( self.nrow )
                                                    
                                                    if self.error is None: 
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
                                                        self.master, self.error = c2D.reverse( self._values_.copy())
                                                        if self._values_[3] is True:
                                                            self._values_[0], self._values_[1], self._values_[2] = self.master, self.ncol, self.nrow
                                                        else: pass
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
    
    