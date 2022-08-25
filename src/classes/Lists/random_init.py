import                                              random
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
    
    def RANDOM (self, 
                mainName    : str, 
                mainString  : str, 
                typ         : str = 'normal'
                )    :
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
                                            if abs( self.newValues ) > 0:
                                                self.matrix = []
                                                for i in range( abs( self.newValues ) ):
                                                    if typ == 'normal':
                                                        if  self.newValues > 0:
                                                            self.matrix.append( random.randint( 0, self.newValues ) )
                                                        else:
                                                            self.matrix.append( random.randint( self.newValues, 0 ) )
                                                    else:
                                                        if  self.newValues > 0:
                                                            self.matrix.append( random.random( ) )
                                                        else:
                                                            self.matrix.append( - random.random( ) )
                                                        
                                                self._return_   = self.matrix
                                                if mainName == 'list.': pass 
                                                else:
                                                    self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                    self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_ 
                                            else: self.error = er.ERRORS( self.line ).ERROR30()
                                        elif type( self.newValues ) == type( tuple() ):
                                            try:
                                                if len( self.newValues ) == 2:
                                                    self.n, self.m = self.newValues[0], self.newValues[1]
                                                    if type( self.n ) == type( int() ):                 
                                                        if type(self.m) == type( int() ):
                                                            if self.n > 0:
                                                                if  abs( self.m ) > 0:
                                                                    self.matrix = []
                                                                    for i in range( abs( self.n ) ):
                                                                        if typ == 'normal':
                                                                            if  self.m > 0:  self.matrix.append( random.randint( 0, self.m ) )
                                                                            else:  self.matrix.append( random.randint( self.m, 0 ) )
                                                                        else: self.error =  er.ERRORS( self.line ).ERROR3( )
                                                                    
                                                                    if self.error is None:
                                                                        self._return_   = self.matrix
                                                                        if mainName == 'list.': pass 
                                                                        else:
                                                                            self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                                            self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_
                                                                    else: pass
                                                                else: self.error =  er.ERRORS( self.line ).ERROR30( s= 'max_num')
                                                            else: self.error =  er.ERRORS( self.line ).ERROR47( ) 
                                                        elif type(self.m) == type( tuple() ):
                                                            if self.n > 0:
                                                                if len(self.m) == 2: 
                                                                    if type(self.m[0]) == type( int() ):
                                                                        if type(self.m[1]) == type(int()):
                                                                            if self.m[0] != self.m[1]: 
                                                                                self.matrix = []
                                                                                for i in range( abs( self.n ) ):
                                                                                    if typ == 'normal':
                                                                                        self.matrix.append( random.randint( min(self.m), max(self.m) ) )
                                                                                    else: self.error =  er.ERRORS( self.line ).ERROR3( )
                                                                                
                                                                                if self.error is None:
                                                                                    self._return_   = self.matrix
                                                                                    if mainName == 'list.': pass 
                                                                                    else:
                                                                                        self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                                                        self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_
                                                                                else: pass
                                                                            else: self.error =  er.ERRORS( self.line ).ERROR48( )
                                                                        else: self.error =  er.ERRORS( self.line ).ERROR3( "max_num2" )
                                                                    else: self.error =  er.ERRORS( self.line ).ERROR3( "max_num1" )
                                                                else: self.error =  er.ERRORS( self.line ).ERROR29( "max_num" )
                                                            else: self.error =  er.ERRORS( self.line ).ERROR47( ) 
                                                        else: self.error =  er.ERRORS( self.line ).ERROR3( "max_num" ) 
                                                    else: self.error =  er.ERRORS( self.line ).ERROR3( "max_step" ) 
                                                else : self.error =  er.ERRORS( self.line ).ERROR29( "numeric" )
                                            except IndexError : pass
                                        else: self.error =  er.ERRORS( self.line ).ERROR49( "numeric" )  
                                    else: pass
                                else: self.error =  er.ERRORS( self.line ).ERROR0( mainString )
                            else: pass
                        else: 
                            self.operator   = self.dict_value[ 'operator' ]
                            self.error      =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            elif self.arguments[ 0 ] is None: self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['numeric']] ) 
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
                                        if   type( self.newValues ) == type( int() ):
                                            if abs( self.newValues ) > 0:
                                                self.matrix = []
                                                for i in range( abs( self.newValues ) ):
                                                    if typ == 'normal':
                                                        if  self.newValues > 0:
                                                            self.matrix.append( random.randint( 0, self.newValues ) )
                                                        else:
                                                            self.matrix.append( random.randint( self.newValues, 0 ) )
                                                    else:
                                                        if  self.newValues > 0:
                                                            self.matrix.append( random.random( ) )
                                                        else:
                                                            self.matrix.append( - random.random( ) )
                                                self._return_   = self.matrix
                                                if mainName == 'list.': pass 
                                                else:
                                                    self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                    self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_ 
                                            else: self.error = er.ERRORS( self.line ).ERROR30()
                                        elif type( self.newValues ) == type( tuple() ):
                                            try:
                                                if len( self.newValues ) == 2:
                                                    self.n, self.m = self.newValues[0], self.newValues[1]
                                                    if type( self.n ) == type( int() ):                 
                                                        if type(self.m) == type( int() ):
                                                            if self.n > 0:
                                                                if  abs( self.m ) > 0:
                                                                    self.matrix = []
                                                                    for i in range( abs( self.n ) ):
                                                                        if typ == 'normal':
                                                                            if  self.m > 0:  self.matrix.append( random.randint( 0, self.m ) )
                                                                            else:  self.matrix.append( random.randint( self.m, 0 ) )
                                                                        else: self.error =  er.ERRORS( self.line ).ERROR3( )
                                                                    
                                                                    if self.error is None:
                                                                        self._return_   = self.matrix
                                                                        if mainName == 'list.': pass 
                                                                        else:
                                                                            self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                                            self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_
                                                                    else: pass
                                                                else: self.error = er.ERRORS( self.line ).ERROR30( s= 'max_num')
                                                            else: self.error = er.ERRORS( self.line ).ERROR47( ) 
                                                        elif type(self.m) == type( tuple() ):
                                                            if self.n > 0:
                                                                if len(self.m) == 2: 
                                                                    if type(self.m[0]) == type( int() ):
                                                                        if type(self.m[1]) == type(int()):
                                                                            if self.m[0] != self.m[1]: 
                                                                                self.matrix = []
                                                                                for i in range( abs( self.n ) ):
                                                                                    if typ == 'normal':
                                                                                        self.matrix.append( random.randint( min(self.m), max(self.m) ) )
                                                                                    else: self.error =  er.ERRORS( self.line ).ERROR3( )
                                                                                
                                                                                if self.error is None:
                                                                                    self._return_   = self.matrix
                                                                                    if mainName == 'list.': pass 
                                                                                    else:
                                                                                        self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                                                        self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_
                                                                                else: pass
                                                                            else: self.error =  er.ERRORS( self.line ).ERROR48( )
                                                                        else: self.error =  er.ERRORS( self.line ).ERROR3( "max_num2" )
                                                                    else: self.error =  er.ERRORS( self.line ).ERROR3( "max_num1" )
                                                                else: self.error =  er.ERRORS( self.line ).ERROR29( "max_num" )
                                                            else: self.error =  er.ERRORS( self.line ).ERROR47( ) 
                                                        else: self.error =  er.ERRORS( self.line ).ERROR3( "max_num" ) 
                                                    else: self.error =  er.ERRORS( self.line ).ERROR3( "max_step" ) 
                                                else : self.error =  er.ERRORS( self.line ).ERROR29( "numeric" )
                                            except IndexError : pass
                                        else: self.error =  er.ERRORS( self.line ).ERROR49( "numeric" )   
                                    else: pass
                                else: self.error =  er.ERRORS( self.line ).ERROR0( mainString )
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
                else: self.error =  er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error =  er.ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error