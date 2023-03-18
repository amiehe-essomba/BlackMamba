from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation
import numpy as np

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
                                                if 0 < ncol <= len(self.master):
                                                    if len(self.master )%self.newValues == 0:
                                                        if self.newValues == len(self.master):
                                                            self._return_ = np.array( [[x] for x in range(ncol)])
                                                        else:
                                                            self._return_  = []
                                                            n = 0
                                                            nrow = len(self.master) // ncol 
                                                            for i in range(nrow):
                                                                ss = []
                                                                for j in range(ncol):
                                                                    ss.append(self.master[n])
                                                                    n += 1
                                                                self._return_.append(ss)
                                                            self._return_ = np.array(self._return_)
                                                    else:  self.error = er.ERRORS( self.line ).ERROR58( 'ncol', len(self.master))
                                                else:  self.error = er.ERRORS( self.line ).ERROR57( 'ncol', len(self.master))        
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
                    if self.master: self._return_   = np.array( [self.master] )
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
                                                        if 0 < ncol <= len(self.master):
                                                            if len(self.master )%self.newValues == 0:
                                                                if self.newValues == len(self.master):
                                                                    self._return_ = np.array( [[x] for x in range(ncol)])
                                                                else:
                                                                    self._return_  = []
                                                                    n = 0
                                                                    nrow = len(self.master) // ncol 
                                                                    for i in range(nrow):
                                                                        ss = []
                                                                        for j in range(ncol):
                                                                            ss.append(self.master[n])
                                                                            n += 1
                                                                        self._return_.append(ss)
                                                                    self._return_ = np.array(self._return_)
                                                            else:  self.error = er.ERRORS( self.line ).ERROR58( 'ncol', len(self.master))
                                                        else:  self.error = er.ERRORS( self.line ).ERROR57( 'ncol', len(self.master))  
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