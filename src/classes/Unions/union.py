from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation
from CythonModules.Windows                          import frame

class DICTIONARY:
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
        
    def DICT( self, mainName: str, mainString: str ):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
            
        if   self.function in [ 'get'   ]            :
            if len( self.arguments ) == 1:
                if   self.arguments[ 0 ] in [ 'type' ]:
                    if self.value[ 0 ] is not None:
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
                                            if type( self.newValues ) == type( str() ):
                                                if self.master:
                                                    if self.newValues == 'keys':
                                                        self._return_ = list( self.master.keys())
                                                    elif self.newValues == 'items': 
                                                        self._return_ = list( self.master.items() )
                                                    elif self.newValues == 'values': 
                                                        self.ss = []
                                                        if self.master:
                                                            for s in self.master.items():
                                                                self.ss.append( s[ 1 ] )
                                                            self._return_ = self.ss.copy()
                                                        else: self.error = er.ERRORS( self.line ).ERROR24( )
                                                    elif self.value[ 0 ] is None: 
                                                        self.error = er.ERRORS( self.line ).ERROR15( self.function, [['type']] )  
                                                    else :  self.error =  er.ERRORS( self.line ).ERROR23( self.value[ 0 ] ) 
                                                else: self.error = er.ERRORS( self.line ).ERROR24( )
                                            else: self.error = er.ERRORS( self.line ).ERROR3( "name", 'a string()' )
                                        else: pass 
                                    else: self.error = er.ERRORS( self.line ).ERROR0( mainString )
                                else: pass
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                    else: self.error = er.ERRORS( self.line ).ERROR15( self.function, [['type']] )
                else:
                    if self.value[ 0 ] is None: 
                        if  self.arguments[ 0 ] is not None:
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
                                                        if self.newValues == 'keys':
                                                            self._return_ = list( self.master.keys())
                                                        elif self.newValues == 'items': 
                                                            self._return_ = list( self.master.items() )
                                                        elif self.newValues == 'values': 
                                                            self.ss = []
                                                            if self.master:
                                                                for s in self.master.items():
                                                                    self.ss.append( s[ 1 ] )
                                                                self._return_ = self.ss.copy()
                                                            else: self.error = er.ERRORS( self.line ).ERROR24( )
                                                        elif self.arguments[ 0 ] is None: 
                                                            self.error = er.ERRORS( self.line ).ERROR15( self.function, [['type']] )  
                                                        else :  
                                                            self.error =  er.ERRORS( self.line ).ERROR23( self.value[ 0 ] ) 
                                                    else: self.error = er.ERRORS( self.line ).ERROR24( )
                                                else: self.error = er.ERRORS( self.line ).ERROR3( "name", 'a string()' )
                                            else: pass 
                                        else: self.error = er.ERRORS( self.line ).ERROR0( mainString )
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass 
                        else: self.error = er.ERRORS( self.line ).ERROR15( self.function, [['type']] )
                    else: self.error =  er.ERRORS( self.line ).ERROR23( self.arguments[ 0 ] )             
            else: self.error = er.ERRORS( self.line ).ERROR12( self.function, 1)
        elif self.function in [ 'empty' ]            :
            if None in self.arguments: 
                if    self.master: self._return_ = False
                else: self._return_ = True
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )    
        elif self.function in [ 'copy'  ]            :
            if None in self.arguments: 
                if  mainName in self.DataBase[ 'variables' ][ 'vars' ]:
                    self.idd =  self.DataBase[ 'variables' ][ 'vars' ].index( mainName )
                    self.DataBase[ 'variables' ][ 'values' ][ self.idd ] = self.master.copy()
                else: pass
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )       
        elif self.function in [ 'clear' ]            :
            if None in self.arguments: 
                if  mainName in self.DataBase[ 'variables' ][ 'vars' ]:
                    self.idd =  self.DataBase[ 'variables' ][ 'vars' ].index( mainName )
                    self.DataBase[ 'variables' ][ 'values' ][ self.idd ] = self.master.clear()
                else: pass
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function ) 
        elif self.function in [ 'remove', "merges"]  :
            if len( self.arguments ) == 1: 
                if self.arguments[ 0 ] in [ 'key' ]:
                    if  self.value[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [['name']] ) 
                    else:
                        if self.master:
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
                                                if   self.function =='remove':
                                                    if type( self.newValues ) == type( str() ):
                                                        if self.newValues in list( self.master.keys() ):
                                                            self._return_ = self.master.pop( self.newValues )
                                                        else: self.error = er.ERRORS( self.line ).ERROR25( self.value[ 0 ] )
                                                    else: self.error =er. ERRORS( self.line ).ERROR3( "key", 'a string()' )
                                                elif self.function == "merge":
                                                    if type( self.newValues ) == type( dict() ):
                                                        if self.newValues:
                                                            if self.newValues in list( self.master.keys() ):
                                                                if  mainName in self.DataBase[ 'variables' ][ 'vars' ]:
                                                                    self.idd =  self.DataBase[ 'variables' ][ 'vars' ].index( mainName )
                                                                    self.DataBase[ 'variables' ][ 'values' ][ self.idd ] = self.master.update( self.newValues )
                                                                else: self._return_ = self.master.update( self.newValues )
                                                            else: self.error = er.ERRORS( self.line ).ERROR25( self.value[ 0 ] )
                                                        else: pass
                                                    else: self.error =er. ERRORS( self.line ).ERROR3( "name", 'a dictionary()' )
                                            else: pass 
                                        else: self.error = er.ERRORS( self.line ).ERROR0( mainString )
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass
                        else: self.error = er.ERRORS( self.line ).ERROR24( )
                elif self.arguments[ 0 ] is None:  self.error = er.ERRORS( self.line ).ERROR15( self.function, [['key']] )
                else:
                    if self.value[ 0 ] is None :
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
                                                if   self.function =="remove":
                                                    if type( self.newValues ) == type( str() ):
                                                        if self.newValues in list( self.master.keys() ):
                                                            self._return_ = self.master.pop( self.newValues )
                                                        else: self.error = er.ERRORS( self.line ).ERROR25( self.arguments[ 0 ] )
                                                    else: self.error = er.ERRORS( self.line ).ERROR3( "key", 'a string()' )
                                                elif self.function == "merge":
                                                    if type( self.newValues ) == type( dict() ):
                                                        if self.newValues:
                                                            if self.newValues in list( self.master.keys() ):
                                                                if  mainName in self.DataBase[ 'variables' ][ 'vars' ]:
                                                                    self.idd =  self.DataBase[ 'variables' ][ 'vars' ].index( mainName )
                                                                    self.DataBase[ 'variables' ][ 'values' ][ self.idd ] = self.master.update( self.newValues )
                                                                else: self._return_ = self.master.update( self.newValues )
                                                            else: self.error = er.ERRORS( self.line ).ERROR25( self.value[ 0 ] )
                                                        else: pass
                                                    else: self.error =er. ERRORS( self.line ).ERROR3( "name", 'a dictionary()' )
                                            else: pass 
                                        else: self.error = er.ERRORS( self.line ).ERROR0( mainString )
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass                             
                        else: self.error = er.ERRORS( self.line ).ERROR24( )
                    else: er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )                   
            else: self.error = er.ERRORS( self.line ).ERROR12( self.function, 1)              
        elif self.function in [ 'init'  ]            :
            if None in self.arguments: 
                self.idd =  self.DataBase[ 'variables' ][ 'vars' ].index( mainName )
                self.DataBase[ 'variables' ][ 'values' ][ self.idd ] = {}
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'sorted' ]           :
            if len( self.arguments ) == 1:
                if   self.arguments[ 0 ] in [ 'reverse' ]:
                    if self.value[ 0 ] is not None:
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
                                            if type( self.newValues ) == type( tuple() ):
                                                if self.master:
                                                    items = list(self.master.items())
                                                    if len(self.newValues) == 2:
                                                        if type(self.newValues[0]) == type(bool()):
                                                            try:
                                                                if   self.newValues[1] == 'keys':
                                                                    self._return_ = sorted(items, key = lambda x : x[0], reverse = self.newValues[0])
                                                                    self._return_ = dict(self._return_)
                                                                elif self.newValues[1] == 'values':
                                                                    self._return_ = sorted(items, key = lambda x : x[1], reverse = self.newValues[0])
                                                                    self._return_ = dict(self._return_)
                                                                else: self.error = er.ERRORS( self.line ).ERROR53( )
                                                            except TypeError: self.error = er.ERRORS( self.line ).ERROR54( )
                                                        else: self.error = er.ERRORS( self.line ).ERROR51( )
                                                    else: self.error = er.ERRORS( self.line ).ERROR52()
                                                else: self.error = er.ERRORS( self.line ).ERROR24( )
                                            else: self.error = er.ERRORS( self.line ).ERROR3( "reverse", 'a tuple()' )
                                        else: pass 
                                    else: self.error = er.ERRORS( self.line ).ERROR0( mainString )
                                else: pass
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                    else: self.error = er.ERRORS( self.line ).ERROR15( self.function, [['reverse']] )
                else:
                    if self.value[ 0 ] is None: 
                        if  self.arguments[ 0 ] is not None:
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
                                                if type( self.newValues ) == type( tuple() ):
                                                    if self.master:
                                                        items = list(self.master.items())
                                                        if len(self.newValues) == 2:
                                                            if type(self.newValues[0]) == type(bool()):
                                                                try:
                                                                    if   self.newValues[1] == 'keys':
                                                                        self._return_ = sorted(items, key = lambda x : x[0], reverse = self.newValues[0])
                                                                        self._return_ = dict(self._return_)
                                                                    elif self.newValues[1] == 'values':
                                                                        self._return_ = sorted(items, key = lambda x : x[1], reverse = self.newValues[0])
                                                                        self._return_ = dict(self._return_)
                                                                    else: self.error = er.ERRORS( self.line ).ERROR53( )
                                                                except TypeError: self.error = er.ERRORS( self.line ).ERROR54( )
                                                            else: self.error = er.ERRORS( self.line ).ERROR51( )
                                                        else: self.error = er.ERRORS( self.line ).ERROR52()
                                                    else: self.error = er.ERRORS( self.line ).ERROR24( )
                                                else: self.error = er.ERRORS( self.line ).ERROR3( "reverse", 'a tuple()' )
                                            else: pass 
                                        else: self.error = er.ERRORS( self.line ).ERROR0( mainString )
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass 
                        else: self.error = er.ERRORS( self.line ).ERROR15( self.function, [['reverse']] )
                    else: self.error =  er.ERRORS( self.line ).ERROR23( self.arguments[ 0 ] )             
            else: self.error = er.ERRORS( self.line ).ERROR12( self.function, 1)
        elif self.function in [ 'asFrame']          :
            if None in self.arguments: 
                self._return_, s, ss, self.error  = frame.FRAME(self.master, self.line).FRAME(Frame = True)
                
                if self.error is None :
                    if  mainName in self.DataBase[ 'variables' ][ 'vars' ]:
                        self.idd =  self.DataBase[ 'variables' ][ 'vars' ].index( mainName )
                        self.DataBase[ 'variables' ][ 'values' ][ self.idd ] = self._return_
                    else: pass
                else: pass
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
            
        return self._return_, self.error  