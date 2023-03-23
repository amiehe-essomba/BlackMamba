from script.STDIN.LinuxSTDIN    import control_string
from script.LEXER               import checking_tabulation
from script.LEXER               import check_if_affectation
from script.LEXER               import main_lexer
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from CythonModules.Windows      import fileError    as fe 



class MAIN:
    def __init__(self, master: str, data_base: dict, line: int):
        self.master         = master
        self.line           = line
        self.data_base      = data_base
        self.lex            = main_lexer
        self.tab            = checking_tabulation
        self.affectation    = check_if_affectation

        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def MAIN(self, _id_: int = 1, _type_ : any = None, _key_:bool = False, def_key:str = 'direct', 
             class_key:str = 'direct', interpreter: bool = False, MainList: list = [] 
             ):
        self.error          = None
        self.lexer          = None
        self.normal_string  = None
        self.value          = None
        self.new_string     = ''

        if interpreter is False:
            self.new_string, self.error = self.tab.CHECK_TAB( self.master, self.master,
                                                            self.data_base, self.line).CHECK_LINE(_id_ = _id_)
        else:
            self.new_string, self.error = self.tab.CHECK_TAB_FOR_INTERPRETER( self.master, self.master,
                                                             self.data_base, self.line).CHECK_LINE(_id_, MainList)

        if self.error is None:
            self.new_string = self.new_string

            if self.new_string is not None:
                self.value, self.error = self.affectation.AFFECTATION(self.new_string, self.new_string,
                                                                      self.data_base, self.line).DEEP_CHECKING()

                if self.error is None:
                    self.data_base[ 'final_value' ] = self.value

                    self.final_value, self.error = self.lex.FINAL_LEXER( self.new_string, self.data_base,
                                        self.line ).FINAL_LEXER( self.value, _type_=_type_, _key_ = _key_,
                                                            def_key = def_key, class_key = class_key )

                    if self.error is None:
                        self.lexer = self.final_value

                        if self.final_value[ 'class' ] is not None:
                            self.error = MAIN( self.new_string, self.data_base, self.line ).CLASS( self.final_value )

                        elif self.final_value[ 'def' ] is not None:
                            self.error = MAIN( self.new_string, self.data_base, self.line ).DEF( self.final_value )

                        elif self.final_value[ 'function' ] == 'for':
                            self.data_base[ 'loop_for' ].append( self.final_value[ 'all_data' ] )

                        elif self.final_value[ 'function' ] == 'while':
                            self.data_base[ 'loop_while' ].append( self.final_value[ 'all_data' ] )

                        elif self.final_value[ 'function' ] == 'until':
                            self.data_base[ 'loop_until' ].append( self.final_value[ 'all_data' ] )

                        elif self.final_value[ 'global' ] is not None:
                            self.error = MAIN( self.new_string, self.data_base, self.line ).GLOBAL( self.final_value )

                        elif self.final_value[ 'return' ] is not None:
                            
                            self.data_base[ 'return' ]  = self.final_value[ 'return' ]

                        elif self.final_value[ 'function' ] in [ 'if', 'switch', 'unless' ]:
                            self.data_base[ self.final_value[ 'function' ] ].append( self.final_value[ 'all_data' ] )

                        elif self.final_value[ 'try' ] == True:
                            self.data_base[ 'try' ] =  self.final_value[ 'try' ]

                        elif self.final_value[ 'delete' ] == True:
                            self.data_base[ 'delete' ] =  self.final_value[ 'delete' ]

                        elif self.final_value[ 'print' ] is not None:
                            self.data_base['print'].append( self.final_value['print'] )

                        elif self.final_value[ 'sub_print' ] is not None:
                            self.data_base[ 'sub_print' ] = self.final_value[ 'sub_print' ]

                        elif self.final_value[ 'begin' ] == True:
                            self.data_base[ 'begin' ] =  self.final_value[ 'begin' ]
                            
                        elif self.final_value[ 'module_import' ] is not None:
                            self.data_base[ 'importation' ] =  self.final_value[ 'module_import' ]
                        elif self.final_value[ 'break' ] is not None:
                            self.data_base[ 'break' ] =  self.final_value[ 'break' ]
                        elif self.final_value[ 'pass' ] is not None:
                            self.data_base[ 'pass' ] =  self.final_value[ 'pass' ]
                        elif self.final_value[ 'continue' ] is not None:
                            self.data_base[ 'continue' ] =  self.final_value[ 'continue' ]
                        elif self.final_value[ 'next' ] is not None:
                            self.data_base[ 'next' ] =  self.final_value[ 'next' ]
                        elif self.final_value[ 'break' ] is not None:
                            self.data_base[ 'exit' ] =  self.final_value[ 'exit' ]
                        else:
                            try:
                                if self.final_value['transformation'] not in [ None, ' ', '']:
                                    self.data_base['transformation'] = self.final_value['transformation']
                                else:  pass
                            except ValueError:
                                self.data_base['transformation'] = self.final_value['transformation']
                    else: pass
                else: pass
            else: self.lexer = None
        else: pass
        
        return  self.lexer, self.new_string, self.error

    def CLASS(self, final_value: dict):

        self.error          = None
        self.final_value    = final_value
        self.name           = self.final_value[ 'class' ][ 'class_name' ]
        
        if self.data_base[ 'class_names' ]:
            self.data_base[ 'current_class' ] = self.final_value[ 'class' ][ 'class_name' ]
            if self.name in self.data_base[ 'class_names' ]:
                del self.final_value[ 'class' ][ 'class_name' ]
                del self.final_value[ 'class' ][ 'arguments' ]
                self._value_ = final_value[ 'class' ]
                self.index = self.data_base[ 'class_names' ].index( self.name )
                self.data_base[ 'classes' ][ self.index ] = self._value_
                #self.data_base[ 'classes' ][ self.index ][ self.name ] = self._value_

            else:
                self.data_base[ 'current_class' ] = self.final_value[ 'class' ][ 'class_name' ]
                del self.final_value[ 'class' ][ 'class_name' ]
                del self.final_value[ 'class' ][ 'arguments' ]
                self._value_ = self.final_value[ 'class' ]
                #self._data_ = {
                #    '{}'.format( self.name ): self._value_
                #}
                self.data_base[ 'classes' ].append( self._value_ )
                self.data_base[ 'class_names' ].append( self.name )

        else:
            self.data_base[ 'current_class' ] = self.final_value[ 'class' ][ 'class_name' ]
            del self.final_value[ 'class' ][ 'class_name' ]
            del self.final_value[ 'class' ][ 'arguments' ]
            self._value_ = final_value[ 'class' ]
            #self._data_ = {
            #    '{}'.format( self.name ): self._value_
            #}
            self.data_base[ 'classes' ].append( self._value_ )
            self.data_base[ 'class_names' ].append( self.name )

        return  self.error

    def DEF(self, final_value: dict):
        self.error          = None
        self.final_value    = final_value

        self.name = self.final_value[ 'def' ][ 'function_name' ]

        if self.data_base[ 'func_names' ]:
            if self.name in self.data_base[ 'func_names' ]:
                del self.final_value[ 'def' ][ 'function_name' ]
                self._value_ = self.final_value[ 'def' ]
                self.index = self.data_base[ 'func_names' ].index( self.name )
                self.data_base[ 'functions' ][ self.index ][ self.name ] = self._value_
            else:
                del self.final_value[ 'def' ][ 'function_name' ]
                self._value_ = self.final_value[ 'def' ]
                self._data_ = {
                    '{}'.format(self.name): self._value_
                }
                self.data_base[ 'functions' ].append( self._data_ )
                self.data_base[ 'func_names' ].append( self.name )

        else:
            del self.final_value[ 'def' ][ 'function_name' ]
            self._value_ = self.final_value[ 'def' ]
            self._data_ = {
                '{}'.format( self.name ): self._value_
            }
            self.data_base[ 'functions' ].append( self._data_ )
            self.data_base[ 'func_names' ].append( self.name )

        return self.error

    def GLOBAL(self, final_value: dict):
        self.error          = None
        self.final_value    = final_value
        self.variables      = self.data_base[ 'global_vars' ][ 'vars' ][ : ]
        self.global_values  = self.data_base[ 'global_vars' ][ 'values' ][ : ]
        self._variables_    = self.data_base[ 'variables' ][ 'vars' ][ : ]
        self._values_       = self.data_base[ 'variables' ][ 'values' ][ : ]

        if not self.variables :
            for _global_ in self.final_value[ 'global' ][ 'global' ]:
                if _global_ not in self.variables:
                    self.variables.append( _global_ )
                    if _global_ in self._variables_:
                        self.index = self._variables_.index( _global_ )
                        self.global_values.append( self._values_[ self.index ] )
                    else: self.global_values.append( '@670532821@656188@656188185@' )
                else:
                    self.error = ERRORS( self.line ).ERROR1( self.master, _global_ )
                    break

        else:
            for _global_ in self.final_value[ 'global' ][ 'global' ]:
                if _global_ not in self.variables:
                    self.variables.append( _global_ )
                    if _global_ in self._variables_:
                        self.index = self._variables_.index( _global_ )
                        self.global_values.append( self._values_[ self.index ] )
                    else: self.global_values.append( '@670532821@656188@656188185@' )
                else:
                    self.error  = ERRORS( self.line ).ERROR2( self.master, _global_ )
                    break

        if self.error is None:
            self.data_base['global_vars'] = {
                'vars'              : self.variables,
                'values'            : self.global_values
            }

        else: pass

        return self.error

class SCANNER:
    def __init__(self, master: str, data_base: dict, line: int):
        self.master         = master
        self.line           = line
        self.data_base      = data_base
        self.lex            = main_lexer
        self.tab            = checking_tabulation
        self.affectation    = check_if_affectation

        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def SCANNER(self, _id_: int = 1, _type_ : any = None, _key_:bool = False):

        self.error = None
        self.lexer = None
        self.normal_string = None

        self.new_string, self.error = self.tab.CHECK_TAB(self.master, self.master,
                                                         self.data_base, self.line).CHECK_LINE(_id_ = _id_)
        if self.error is None:
            self.new_string = self.new_string

            if self.new_string is not None:
                self.value, self.error = self.affectation.AFFECTATION(self.new_string, self.new_string,
                                                                      self.data_base, self.line).DEEP_CHECKING()
                if self.error is None:
                    #self.final_value, self.error = self.lex.FINAL_LEXER(self.new_string, self.data_base,
                    #                                self.line).FINAL_LEXER(self.value,_type_=_type_, _key_ = _key_)
                    pass
                else: pass
            else: self.lexer = None
        else: pass

        return  self.error

class ERRORS:
    def __init__(self, line):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    def ERROR1(self, string: str, name: str):
        error = '{}is duplicated as a {}global {}variable. {}line: {}{}'.format(self.white, self.green, self.red, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'SyntaxError' ).Errors() +'{}<< {} >> '.format(self.cyan, name) + error
        
        return self.error+self.reset

    def ERROR2(self, string: str, name: str):
        error = '{}is already defined as a {}global {}variable. {}line: {}{}'.format(self.white, self.green, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}<< {} >> '.format(self.cyan, name) + error
       
        return self.error+self.reset

