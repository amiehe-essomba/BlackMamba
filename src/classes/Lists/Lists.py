import                                              random
from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation
from src.classes.Lists                              import inserting, random_init, sorting
from src.classes.Lists                              import to_array as ta
import numpy as np


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
        
    def LIST(   self, mainName: str, mainString:  str )   :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
            
        if   self.function in [ 'empty' ]            :
            if None in self.arguments: 
                if    self.master: self._return_ = False
                else: self._return_ = True
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function ) 
        elif self.function in [ 'copy'  ]            :
            if None in self.arguments: self._return_ = self.master.copy()
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function ) 
        elif self.function in [ 'clear' ]            :
            if None in self.arguments: 
                self.master.clear()
                self._return_ =  self.master
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function )      
        elif self.function in [ 'insert']            :
            self._return_, self.error = inserting.LIST( self.DataBase, self.line, self.master,
                                                self.function, [self.FunctionInfo] ).INSERT( mainName, mainString  )   
        elif self.function in ['sorted' ]            :
            self._return_, self.error = sorting.LIST( self.DataBase, self.line, self.master,
                                                self.function, [self.FunctionInfo] ).SOERTED( mainName, mainString )  
        elif self.function in [ 'size'  ]            :
            if None in self.arguments: 
                self._return_ = len( self.master )
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'init'  ]            :
            self._return_ = []
            self.idd =  self.DataBase[ 'variables' ][ 'vars' ].index( mainName )
            self.DataBase[ 'variables' ][ 'values' ][ self.idd ] = []
        elif self.function in [ 'choice']            :
            if None in self.arguments:
                if self.master:
                    self._return_ = random.choice( self.master )
                else: self.error =  er.ERRORS( self.line ).ERROR24( 'list / tuple / range' )    
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'to_array']          :
            self._return_, self.error = ta.TO( self.DataBase, self.line, self.master,
                                                 self.function, [self.FunctionInfo] ).ARRAY( mainName, mainString )
            if self.error is None:
                self.index = self.DataBase['variables']['vars'].index( mainName )
                if type(self._return_) in [type(list()), type(dict()), type(np.array([1]))]:
                    self.DataBase['variables'][ 'values'][self.index] = self._return_.copy()
                else: self.DataBase['variables'][ 'values'][self.index] = self._return_
            else: pass
        elif self.function in [ 'enumerate' ]        :
            if None in self.arguments:
                if self.master:
                    self._return_ = []
                    for i, value in enumerate( self.master ):
                        self._return_.append( (i, value) )
                else: self.error =  er.ERRORS( self.line ).ERROR24( 'list' )    
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function )      
        elif self.function in ['random', 'rand' ]    :
            if self.function == 'random':
                self._return_, self.error = random_init.LIST( self.DataBase, self.line, self.master,
                                                 self.function, [self.FunctionInfo] ).RANDOM( mainName, mainString ) 
            else:
                self._return_, self.error = random_init.LIST( self.DataBase, self.line, self.master,
                                                 self.function, [self.FunctionInfo] ).RANDOM( mainName, mainString, 'float' ) 
        elif self.function in [ 'count', 'index', 'remove', 'add', 'round' ]   :
            if len( self.arguments ) == 1: 
                if self.arguments[ 0 ] in [ 'master' ]:
                    if  self.value[ 0 ] is None: self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                    else:
                        self.dict_value, self.error = self.affectation.AFFECTATION(self.value[ 0 ],
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
                                            if   self.function in [ 'count', 'index' ]:
                                                try:
                                                    if self.function in [ 'count' ]:
                                                        self._return_ = self.master.count( self.final_val[ 0 ] )
                                                    else: 
                                                        try: self._return_ = self.master.index( self.final_val[ 0 ] )
                                                        except ValueError : self.error =  er.ERRORS( self.line ).ERROR27( self.value[ 0 ] )
                                                except ValueError: self.error =  er.ERRORS( self.line ).ERROR27( self.value[ 0 ] )
                                            elif self.function in [ 'remove' ]:
                                                if type( self.final_val[ 0 ] ) == type( int() ):
                                                    try: 
                                                        del self.master[ self.final_val[ 0 ] ]
                                                        self._return_ = self.master[ : ]
                                                    except IndexError : self.error =  er.ERRORS( self.line ).ERROR28( )
                                                else: self.error =  er.ERRORS( self.line ).ERROR3( "master" )
                                            elif self.function in [ 'insert' ]:
                                                if type( self.final_val[ 0 ] ) == type( tuple() ):
                                                    try: 
                                                        if len( self.final_val[ 0 ] ) == 2:
                                                            if type( self.final_val[ 0 ][ 0 ] ) == type( int() ) :
                                                                self.master.insert( self.final_val[ 0 ][ 0 ], self.final_val[ 0 ][ 1 ] )
                                                                self._return_ = self.master[ : ]
                                                            else: self.error =  er.ERRORS( self.line ).ERROR3( "master[ 0 ]" )
                                                        else: self.error =  er.ERRORS( self.line ).ERROR29()
                                                    except IndexError : self.error =  er.ERRORS( self.line ).ERROR28( )
                                                else: self.error =  er.ERRORS( self.line ).ERROR3( "master", 'a tuple()' )
                                            elif self.function in [ 'add'    ]:
                                                self.master.append( self.final_val[ 0 ] )
                                                self._return_ = self.master[ : ]
                                            elif self.function in [ 'round'  ]:
                                                self.new = self.master[ : ]
                                                if type( self.final_val[ 0 ] ) == type( int() ) :
                                                    if self.final_val[ 0 ] >= 0:
                                                        if self.master:
                                                            for i in range( len( self.master)):
                                                                if type( self.master[ i ]) in [ type(int()), type(float()), type(bool())]:
                                                                    self.new.append( round( self.master[ i ], self.final_val[0]) )
                                                                else: 
                                                                    self.master = self.new
                                                                    self.error =  er.ERRORS( self.line ).ERROR35( i )
                                                                    break
                                                            self._return_ = self.new
                                                            
                                                        else: self.error =  er.ERRORS( self.line ).ERROR24( 'list')
                                                    else: self.error =  er.ERRORS( self.line ).ERROR34( 'master')
                                                else: self.error =  er.ERRORS( self.line ).ERROR3( 'master' )
                                        else: pass
                                    else: self.error =  er.ERRORS( self.line ).ERROR0( mainString )
                                else: pass 
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                elif self.arguments[ 0 ] is None:  self.error =  er.ERRORS( self.line ).ERROR15( self.function, [['master']] )
                else:
                    if self.value[ 0 ] is None :
                        self.dict_value, self.error = self.affectation.AFFECTATION(self.arguments[ 0 ],
                                                                self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
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
                                            if   self.function in [ 'count', 'index' ]  :
                                                #if type( self.final_val[ 0 ] ) == type( str() ):
                                                try:
                                                    if self.function in [ 'count' ]:
                                                        self._return_ = self.master.count( self.final_val[ 0 ] )
                                                    else: 
                                                        try: self._return_ = self.master.index( self.final_val[ 0 ] )
                                                        except ValueError : self.error =  er.ERRORS( self.line ).ERROR27( self.arguments[ 0 ] )
                                                except ValueError : self.error =  er.ERRORS( self.line ).ERROR27( self.value[ 0 ] )
                                            elif self.function in [ 'remove' ]          :
                                                if type( self.final_val[ 0 ] ) == type( int() ):
                                                    try: 
                                                        del self.master[ self.final_val[ 0 ] ]
                                                        self._return_ = self.master[ : ]
                                                    except IndexError : self.error =  er.ERRORS( self.line ).ERROR28( )
                                                else: self.error =  er.ERRORS( self.line ).ERROR3( "master" )
                                            elif self.function in [ 'add' ]             :
                                                self.master.append( self.final_val[ 0 ] )
                                                self._return_ = self.master[ : ]
                                            elif self.function in [ 'round'  ]          :
                                                self.new = []
                                                if type( self.final_val[ 0 ] ) == type( int() ) :
                                                    if self.final_val[ 0 ] >= 0:
                                                        if self.master:
                                                            for i in range( len( self.master)):
                                                                if type( self.master[ i ]) in [ type(int()), type(float()), type(bool())]:
                                                                    self.new.append( round( self.master[ i ], self.final_val[0]) )
                                                                else: 
                                                                    self.master = self.new
                                                                    self.error =  er.ERRORS( self.line ).ERROR35( i )
                                                                    break
                                                            self._return_ = self.new
                                                            
                                                        else: self.error =  er.ERRORS( self.line ).ERROR24( 'list')
                                                    else: self.error =  er.ERRORS( self.line ).ERROR34( 'master')
                                                else: self.error =  er.ERRORS( self.line ).ERROR3( 'master' )
                                        else: pass
                                else: pass 
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error =  er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                    else:  er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
            else: self.error =  er.ERRORS( self.line ).ERROR12( self.function, 1)                   
        
        return self._return_, self.error  
            
    
      
        
    