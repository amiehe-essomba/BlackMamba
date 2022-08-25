from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation

class STRING:
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
        
    def GLOBAL( self,  typ: str = 'index', mainString: str = '')  :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.values         = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'master': 
                if self.values[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
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
                                        if type( self.newValues ) == type( str() ):
                                            if self.master:
                                                if   typ == 'index'         :
                                                    try:
                                                        self._return_   = self.master.index( self.newValues ) 
                                                    except ValueError: self.error = er.ERRORS( self.line ).ERROR33( self.newValues )
                                                elif typ == 'count:'        :
                                                        self._return_   =  self.master.count( self.newValues )
                                                elif typ == 'starwith:'     :
                                                        self._return_   =  self.master.startswith( self.newValues )
                                                elif typ == 'endwith:'      :
                                                        self._return_   =  self.master.endswith( self.newValues )
                                                else: pass
                                            else: self.error = er.ERRORS( self.line ).ERROR24( 'string' )
                                        else: self.error = er.ERRORS( self.line ).ERROR3( 'master', 'a string()')   
                                    else: pass 
                                else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            else:
                if self.arguments[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [['master']] )
                else:
                    if self.values[ 0 ] is None:
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
                                            if type( self.newValues ) == type( str() ):
                                                if self.master:
                                                    if   typ == 'index'         :
                                                        try:
                                                            self._return_   =  self.master.index( self.newValues )
                                                        except ValueError : self.error = er.ERRORS( self.line ).ERROR33( self.newValues )
                                                    elif typ == 'count:'        :
                                                        self._return_   =  self.master.count( self.newValues )
                                                    elif typ == 'starwith:'     :
                                                            self._return_   =  self.master.startswith( self.newValues )
                                                    elif typ == 'endwith:'      :
                                                        self._return_   =  self.master.endswith( self.newValues )
                                                    else: pass
                                                else: self.error = er.ERRORS( self.line ).ERROR24( 'string' )
                                            else: self.error = er.ERRORS( self.line ).ERROR3( 'master', 'a string()')   
                                        else: pass 
                                    else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                                else: pass
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                    else: self.error = er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = er.ERRORS( self.line ).ERROR12( self.function, 1)
    
        return self._return_, self.error