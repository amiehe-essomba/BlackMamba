from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation
import numpy as np
import pandas as pd

class TO:
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
        
    def ARRAY( self,  mainName: str = '', mainString: str = '') :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.values         = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
           
            if self.arguments[ 0 ] == 'ncol': 
                if self.values[ 0 ] is None: self._return_   = np.array( [self.master] )
                else: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.values[ 0 ],
                                                                    self.values[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
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
                                        ncol = self.newValues
                                        if type( self.newValues ) == type( int() ):
                                            if self.master:
                                                self._return_, self.error = create(self.master, ncol, self.line)      
                                            else: self.error = er.ERRORS( self.line ).ERROR24( 'list' )
                                        else: self.error = er.ERRORS( self.line ).ERROR3( 'ncol', 'an integer()')   
                                    else: pass 
                                else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            else:
                if self.arguments[ 0 ] is None:
                    if self.master: 
                        ncol = len(self.master)
                        self._return_, self.error = create(self.master, ncol, self.line)
                    else: self.error = er.ERRORS( self.line ).ERROR24( 'list' )
                else:
                    if self.values[ 0 ] is None:
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
                                                ncol = self.newValues
                                                if type( self.newValues ) == type( int() ):
                                                    if self.master:
                                                        self._return_,self.error = create(self.master, ncol, self.line)  
                                                    else: self.error = er.ERRORS( self.line ).ERROR24( 'list' )
                                                else: self.error = er.ERRORS( self.line ).ERROR3( 'ncol', 'an integer()')   
                                            else: pass 
                                        else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass
                        else: self.error = er.ERRORS( self.line ).ERROR24( 'list' )
                    else: self.error = er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = er.ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error
    
def create( master, ncol, line ):
    error, _return_ = None , None

    #if len( master ) % ncol == 0:
    if master:
        typ = type(master[0])
        if typ not in [type(dict()), type(np.array([1])), 
                        type(pd.DataFrame(dict(a=[1], b=[2]))), type(pd.Series([1,2], index=[1,2]))]:
            
            if typ == type(list())      :
                LEN = len(master[0])
                if master[0] : size = LEN * len(master) 
                else: size = 1

                for i, s in enumerate(master):
                    if (type(s) == typ) :
                        if (len(s) == LEN): pass 
                        else:
                            error = er.ERRORS( line ).ERROR75( i )  
                            break
                    else:
                        error = er.ERRORS( line ).ERROR74( typ )  
                        break
            elif typ == type(tuple())   :
                LEN = len(master[0])
                if master[0] : size = LEN * len(master) 
                else: size = 1

                for i, s in enumerate(master):
                    if (type(s) == typ) :
                        if (len(s) == LEN): pass 
                        else: 
                            error = er.ERRORS( line ).ERROR75( i )  
                            break
                    else:
                        error = er.ERRORS( line ).ERROR74( typ )  
                        break
            else:
                size = len(master)
                
                for s in master:
                    if (type(s) == typ): pass 
                    else:
                        error = er.ERRORS( line ).ERROR74( typ )  
                        break
            
            if 0 < ncol <= size :
                if size % ncol == 0:
                    if error is None:
                        try:
                            if ncol == len(master):
                                _return_ = np.array(master).reshape((-1, ncol))
                            else:
                                nrow = size // ncol 
                                _return_ = np.array(master).reshape((nrow, ncol))
                        except ValueError : 
                            shape = np.array(master).shape
                            error = er.ERRORS( line ).ERROR66( (nrow, ncol), shape )
                    else: pass
                else: error = er.ERRORS( line ).ERROR58( 'ncol', size )
            else: error = er.ERRORS( line ).ERROR57( 'ncol', size )
        else: error = er.ERRORS( line ).ERROR77( idd=0)
    else:  error = er.ERRORS( line ).ERROR76( string="list")
  
    return _return_, error