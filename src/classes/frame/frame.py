from src.classes                                    import error as er 
from src.transform                                  import error as er_
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation
from CythonModules.Windows                          import frame
from script.STDIN.LinuxSTDIN                        import bm_configure as bm

class DATA:
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
        
    def FRAME( self, mainName: str, mainString: str, name : str = 'show_id' ):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        self.main_dict      = mainString 
        
        if self.function in [ 'keys' ]            :
            if None in self.arguments: 
                self._return_ = list( self.master.keys() )
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        else:
            self._return_, self.error = DATA(self.DataBase, self.line, self.master, self.function, 
                            self.FunctionInfo).SUB_FRAME(mainName, mainString, name)
        
        return self._return_, self.error
    
    def SUB_FRAME(self, mainName: str, mainString: str, name: str = 'show_id' ):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.values         = self.FunctionInfo[ self.function ][ 'value' ]
        self.main_dict      = mainString 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == name: 
                if self.values[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name]] ) 
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
                                        func = bm.fg.rbg(0, 255, 0   )+f' in {self._value_[ 1 ]}( ).' +bm.fg.rbg(255,255,255)+\
                                                            ' / '+bm.fg.rbg(255, 255, 0)+"class " +bm.fg.rbg(0, 0, 255) +"data"+ bm.init.reset 
                                        if name == 'show_id' :
                                            if type( self.newValues ) == type(bool()): 
                                                self.show, s, ss, self.error  = frame.FRAME(self.master, self.line).FRAME(True)
                                                if self.error is None:
                                                    self.show_id = self.newValues
                                                    self.show, s, ss, self.error  = frame.FRAME({"s":show, 'id':list(self.show.index)}, self.line).FRAME(False, 'DataFrame', self.show_id)
                                                    if self.error is None: 
                                                        b = bm.fg.blue_L
                                                        o = bm.fg.rbg(252, 127, 0 )
                                                        w = bm.fg.white_L
                                                        r = bm.init.reset
                                                        self.s1    = bm.init.bold+'{}[{} result{} ]{} : {}'.format(b, o, b,  w, r )
                                                        sys.stdout.write( self.s1+"\n\n"+s+'\n')
                                                    else: pass 
                                                else: pass
                                            else: self.error = er.ERRORS( self.line ).ERROR3( name , 'a boolean()')
                                        elif name == "column": 
                                            if type( self.newValues ) == type(int()): 
                                                if self.function == "set_id": 
                                                    self.final_value, s, ss, self.error  = frame.FRAME(self.master, self.line).FRAME(True)
                                                    if self.error is None:
                                                        self.id_ = self.newValues
                                                        self.keys_ = list(self.final_value.keys())
                                                        if self.id_< len(self.keys_):
                                                            self.final_value.set_index(self.keys_[self.id_], inplace=True)    
                                                        else: self.error = er_.ERRORS( self.line ).ERROR45( func=func )
                                                    else: pass
                                                elif self.function == "select": 
                                                    self.final_value, s, ss, self.error  = frame.FRAME(self.master, self.line).FRAME(True)
                                                    if self.error is None:
                                                        self.id_    = self.newValues
                                                        self.keys_  = list(self.final_value.keys())
                                                        try: 
                                                            self.name = self.keys_[ self.id_]
                                                            self.final_value = self.master[ self.name ]
                                                        except IndexError : self.error = er_.ERRORS( self.line ).ERROR45( func=func )
                                                    else:pass
                                            else: self.error = er.ERRORS( self.line ).ERROR3( name , 'a integer()') 
                                        else: self.error = er.ERRORS(self.line).ERROR13(name)
                                    else: pass 
                                else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            else:
                if self.arguments[ 0 ] is None:
                    self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name]] )
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
                                                            self.DataBase, self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues = self.final_val[ 0 ]
                                                func = bm.fg.rbg(0, 255, 0   )+f' in {self._value_[ 1 ]}( ).' +bm.fg.rbg(255,255,255)+\
                                                            ' / '+bm.fg.rbg(255, 255, 0)+"class " +bm.fg.rbg(0, 0, 255) +"data"+ bm.init.reset 
                                                if name == 'show_id' :
                                                    if type( self.newValues ) == type(bool()): 
                                                        self.show, s, ss, self.error  = frame.FRAME(self.master, self.line).FRAME(True)
                                                        if self.error is None:
                                                            self.show_id = self.newValues
                                                            self.show, s, ss, self.error  = frame.FRAME({"s":show, 'id':list(self.show.index)}, self.line).FRAME(False, 'DataFrame', self.show_id)
                                                            if self.error is None: 
                                                                b = bm.fg.blue_L
                                                                o = bm.fg.rbg(252, 127, 0 )
                                                                w = bm.fg.white_L
                                                                r = bm.init.reset
                                                                self.s1    = bm.init.bold+'{}[{} result{} ]{} : {}'.format(b, o, b,  w, r )
                                                                sys.stdout.write( self.s1+"\n\n"+s+'\n')
                                                            else: pass 
                                                        else: pass
                                                    else: self.error = er.ERRORS( self.line ).ERROR3( name , 'a boolean()')
                                                elif name == "column": 
                                                    if type( self.newValues ) == type(int()): 
                                                        if self.function == "set_id": 
                                                            self.final_value, s, ss, self.error  = frame.FRAME(self.master, self.line).FRAME(True)
                                                            if self.error is None:
                                                                self.id_ = self.newValues
                                                                self.keys_ = list(self.final_value.keys())
                                                                if self.id_< len(self.keys_):
                                                                    self.final_value.set_index(self.keys_[self.id_], inplace=True)    
                                                                else: self.error = er_.ERRORS( self.line ).ERROR45( func=func )
                                                            else: pass
                                                        elif self.function == "select": 
                                                            self.final_value, s, ss, self.error  = frame.FRAME(self.master, self.line).FRAME(True)
                                                            if self.error is None:
                                                                self.id_    = self.newValues
                                                                self.keys_  = list(self.final_value.keys())
                                                                try: 
                                                                    self.name = self.keys_[ self.id_]
                                                                    self.final_value = self.master[ self.name ]
                                                                except IndexError : self.error = er_.ERRORS( self.line ).ERROR45( func=func )
                                                            else:pass
                                                    else: self.error = er.ERRORS( self.line ).ERROR3( name , 'a integer()') 
                                                else: self.error = er.ERRORS(self.line).ERROR13(name)
                                            else: pass 
                                        else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass
                        else: self.error = er.ERRORS( self.line ).ERROR24( 'table()' )
                    else: self.error = er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = er.ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error