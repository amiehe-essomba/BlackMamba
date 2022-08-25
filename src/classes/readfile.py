from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation


class READFILE:
    def __init__(self, DataBase: dict, line:int, master: str, function: any, FunctionInfo : list ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        self.lexer          = main_lexer
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        
    def READFILE( self, mainName: str = '', mainString: str = '' ):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        self.fileS          = []

        try:
            if   self.function in [ 'readlines'  ]              :
                self._return_, self.error = READFILE(self.DataBase, self.line, self.master, self.function,
                                                        [self.FunctionInfo]).READLINE( mainName, mainString )
                if self.error is None:
                    try:
                        if self.master[ 2 ] in [ 'r' ]:
                            if self._return_ is not None:
                                if self.master[ 4 ] is None:
                                    with open( self.master[ 1 ], self.master[ 2 ]) as file:
                                        for line in file.readlines( self._return_ ):
                                            self.fileS.append( line.rstrip() )
                                else:
                                    with open( self.master[ 1 ], self.master[ 2 ], encoding=self.master[4], errors='surrogateescape') as file:
                                        for line in file.readlines( self._return_ ):
                                            self.fileS.append( line.rstrip() )
                            else:
                                if self.master[ 4 ] is None:
                                    with open( self.master[ 1 ], self.master[ 2 ]) as file:
                                        for line in file.readlines():
                                            self.fileS.append( line.rstrip() )
                                else:
                                    with open( self.master[ 1 ], self.master[ 2 ], encoding=self.master[4], errors='surrogateescape') as file:
                                        for line in file.readlines( self._return_ ):
                                            self.fileS.append( line.rstrip() )
                                            
                            self._return_ = self.fileS
                        else: self.error = er.ERRORS( self.line ).ERROR37( self.master[ 1 ], self.master[ 2 ] ) 
                    except FileNotFoundError: self.error = er.ERRORS( self.line ).ERROR36( self.master[ 1 ])  
                else: pass            
            elif self.function in [ 'write', 'writeline'  ]     :
                if self.master[ 2 ] in [ 'w' ] :
                    self.__return__, self.error = READFILE(self.DataBase, self.line, self.master, self.function,
                                                        [self.FunctionInfo]).WRITELINE( mainName, mainString )
                    if self.error is None:
                        if self.master[ 3 ] == 'old': self.master[ 2 ] = 'a'
                        else: pass
                        
                        file = open( self.master[ 1 ], self.master[ 2 ])
                        file.write( self.__return__ )
                        self.DataBase[ 'no_printed_values' ].append( None )
                    else: pass
                else: self.error = er.ERRORS( self.line ).ERROR37( self.master[ 1 ], self.master[ 2 ] ) 
            elif self.function in [ 'writelines'  ]             :
                if self.master[ 2 ] in [ 'w' ] :
                    self.__return__, self.error = READFILE(self.DataBase, self.line, self.master, self.function,
                                                        [self.FunctionInfo]).WRITELINE( mainName, mainString, 'list' )
                    if self.error is None:
                        if self.master[ 3 ] == 'old': self.master[ 2 ] = 'a'
                        else: pass
                        
                        file = open( self.master[ 1 ], self.master[ 2 ])
                        try:
                            if self.__return__ :
                                file.writelines( self.__return__ )
                            else: self.error = er.ERRORS( self.line ).ERROR24( 'list' )
                        except TypeError:
                            if self.self.__return__:
                                for l, _str_ in enumerate( self.__return__ ):
                                    if type( _str_ ) in [ type(str())] : pass 
                                    else: 
                                        self.error = er.ERRORS( self.line ).ERROR38( l )
                                        break
                            else: pass
                        self.DataBase[ 'no_printed_values' ].append( None )
                    else: pass
                else: self.error = er.ERRORS( self.line ).ERROR37( self.master[ 1 ], self.master[ 2 ] ) 
            elif self.function in [ 'readline', 'read' ]        :
                if self.master[ 2 ] in [ 'r' ]:
                    self._return_, self.error = READFILE(self.DataBase, self.line, self.master, self.function,
                                                        [self.FunctionInfo]).READLINE( mainName, mainString )
                    if self.error is None:
                        try:
                            file = open( self.master[ 1 ], self.master[ 2 ])
                            if self._return_ is not None:
                                self._return_ = file.readline( self._return_ )
                            else: self._return_ = file.readline() 
                        except FileNotFoundError: self.error = er.ERRORS( self.line ).ERROR36( self.master[ 1 ])
                    else: pass 
                else: self.error = er.ERRORS( self.line ).ERROR37( self.master[ 1 ], self.master[ 2 ] ) 
            elif self.function in [ 'close' ]:
                if None in self.arguments:
                    self.DataBase[ 'no_printed_values' ].append( None )
                    if mainName in self.DataBase[ 'open' ]['nonCloseKey']:
                        self.idd = self.DataBase[ 'open' ]['nonCloseKey'].index( mainName )
                        del self.DataBase[ 'open' ]['nonCloseKey'][ self.idd ]
                        del self.DataBase[ 'open' ]['name'][ self.idd ]
                        del self.DataBase[ 'open' ]['file'][ self.idd ]
                        del self.DataBase[ 'open' ]['action'][ self.idd ]
                        del self.DataBase[ 'open' ]['status'][ self.idd ]
                        del self.DataBase[ 'open' ]['encoding'][ self.idd ]
                    else: pass
                else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        
        except UnicodeDecodeError   : self.error = er.ERRORS( self.line ).ERROR40() 
        except UnicodeEncodeError   : self.error = er.ERRORS( self.line ).ERROR39()
        except UnicodeError         : self.error = er.ERRORS( self.line ).ERROR41() 
             
        return self._return_, self.error 
    
    def READLINE (self, mainName: str, mainString:  str)    :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'numeric': 
                if self.value[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [['numeric']] ) 
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
                                        if type( self.newValues ) == type( int() ):
                                            if self.newValues  >= 0:
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = er.ERRORS( self.line ).ERROR30()
                                        else: self.error = er.ERRORS( self.line ).ERROR3( "numeric" )   
                                    else: pass
                                else: self.error = er.ERRORS( self.line ).ERROR0( mainString )
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            elif self.arguments[ 0 ] is None: self._return_ = None
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
                                        if type( self.newValues ) == type( int() ):
                                            if self.newValues >= 0:
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = er.ERRORS( self.line ).ERROR30()
                                        else: self.error = er.ERRORS( self.line ).ERROR3( "numeric" )   
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
    
    def WRITELINE (self, mainName: str, mainString:  str, typ : str = 'str')   :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'master': 
                if self.value[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
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
                                        if typ == 'str':
                                            if type( self.newValues ) == type( str() ):
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = er.ERRORS( self.line ).ERROR3( "master", ' a string()' )   
                                        elif typ == 'list':
                                            if type( self.newValues ) == type( list() ):
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = er.ERRORS( self.line ).ERROR3( "master", ' a list()' )  
                                    else: pass
                                else: self.error = er.ERRORS( self.line ).ERROR0( mainString )
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            elif self.arguments[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
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
                                        if typ == 'str':
                                            if type( self.newValues ) == type( str() ):
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = er.ERRORS( self.line ).ERROR3( "master", ' a string()' )   
                                        elif typ == 'list':
                                            if type( self.newValues ) == type( list() ):
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = er.ERRORS( self.line ).ERROR3( "master", ' a list()' )  
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