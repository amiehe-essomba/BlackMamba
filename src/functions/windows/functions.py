import os , sys
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_if, for_begin, for_statement, for_switch, for_unless,  for_try
from script.LEXER.FUNCTION                              import main
from script.DATA_BASE                                   import data_base as db
from script.PARXER                                      import module_load_treatment  as mlt
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from src.functions                                      import error as er
from script.PARXER.PARXER_FUNCTIONS._IF_                import IfError
from functions                                          import internalDef as ID
from statement.comment                                  import externalCmt

class EXTERNAL_DEF_WINDOWS:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        self.master             = master
        self.line               = line
        self.data_base          = data_base

    def TERMINAL( self, 
            tabulation  : int,  
            class_name  : str   = '' , 
            class_key   : bool  = False,
            c           : str   = '',
            function    : str   = 'def',
            _type_      : str   = 'def'
            ):
        
        self.if_line            = 0
        self.error              = None
        self.string             = ''
        self.normal_string      = ''
        self.end                = ''

        ##########################################################
        self.space              = 0
        self.active_tab         = None
        self.tabulation         = tabulation
        self.history            = [ 'def' ]
        self.def_starage        = []
        self.store_value        = []
      
        ##########################################################
        self.color              = bm.fg.rbg(255,255,0)
        self.input              = '{}... {}'.format(self.color, bm.init.reset)
        self.length             = len(self.input)
        self.index              = self.length
        self.sub_length         = len('{}{}'.format( self.color, bm.init.reset))
        self.tab                = 1
        self.Input              = ''
        self.Index              = 0
        self.col                = []
        self.max_emtyLine       = 5
        self.c                  = c
        self.previous_c         = c
        self.mainString         = ''
        self.mainIndex          = 0
        ##########################################################
        
        self.subFunc            = {
            'func_names'        : [],
            'functions'         : []
        }
        
        sys.stdout.write(bm.clear.line(2))
        sys.stdout.write(bm.move_cursor.LEFT(1000))
        sys.stdout.write(bm.string().syntax_highlight(name = self.input))
        sys.stdout.flush()

        while True :
         
            try:
                self.char = bm.read().readchar()
                if self.char not in {10, 13}:
                    self.input      = self.input[: self.index] + chr(self.char) + self.input[self.index:]
                    self.mainString = self.mainString[: self.mainIndex] + chr(self.char) + self.mainString[  self.mainIndex:]
                    self.index      += 1
                    self.mainIndex  += 1
                    
                
                elif self.char in {10, 13}:
                    self.if_line += 1
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    self.s = self.input
                    self.clear_input = bm.chars().ansi_remove_chars(name=self.input[self.length:])

                    if self.clear_input:
                        ####################################################################
                        _, self._, self.err = self.analyse.BUILD_CON(string=self.clear_input, tabulation=self.tabulation)
                        if self.err is None:
                            if (self._ - 1) >= 0:
                                self.input = self.input[: self.length] + bm.words(string=self.mainString, color=self.c).final()
                            else:
                                self.input = self.input[: self.length] + bm.words(string=self.mainString, color=self.previous_c).final()
                        else:
                            self.input = self.input[: self.length] + bm.words(string=self.mainString,  color=self.previous_c).final()

                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        sys.stdout.write(bm.move_cursor.UP(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(self.input)
                        sys.stdout.flush()
                        sys.stdout.write(bm.move_cursor.DOWN(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(bm.move_cursor.LEFT(1000))
                        ######################################################################
                        self.string, self.active_tab, self.error = self.analyse.BUILD_CON(string=self.clear_input,
                                                                                    tabulation=self.tabulation)
                        if self.error is None:
                            self.normal_string = self.analyse.BUILD_NON_CON(string=self.clear_input,tabulation=self.tabulation)
                            if self.active_tab is True :
                                if self.error is None:
                                    self.get_block, self.value, self.error = ID.INTERNAL_BLOCKS( string=self.string,
                                                    normal_string=self.normal_string, data_base=self.data_base, 
                                                    line=self.if_line ).BLOCKS( tabulation=self.tabulation + 1,
                                                    function=function, interpreter = False, class_name= class_name, class_key=class_key,
                                                    func_name=self.data_base[ 'current_func' ], loop = False )
                                                    
                                    if self.error is None:
                                        if class_key is False: pass 
                                        else: 
                                            if self.get_block not in [ 'empty', 'any' ]:
                                                self.error = er.ERRORS( self.line ).ERROR20( self.get_block[ : -1 ] )
                                                break
                                            else: pass
                                        if self.error is None:
                                            if self.get_block   == 'begin:' :
                                                self.store_value.append(self.normal_string)
                                                self.def_starage.append( ( self.normal_string, True ) )
                                                
                                                self._values_, self.error = for_begin.COMMENT_STATEMENT(master=self.master,
                                                        data_base=self.data_base,  line=self.if_line).COMMENT( tabulation=self.tabulation + 1, color=c)
                                                
                                                if self.error is None:
                                                    self.history.append( 'begin' )
                                                    self.space = 0
                                                    self.def_starage.append( self._values_ )
                                                else: break 
                                            elif self.get_block == 'for:'   :
                                                self.store_value.append(self.normal_string)
                                                self.def_starage.append( ( self.normal_string, True ) )
                                                
                                                loop, tab, self.error = for_statement.EXTERNAL_FOR_STATEMENT( self.master,
                                                                            self.data_base, self.line ).FOR_STATEMENT( self.tabulation+1 )
                                                if self.error is None:
                                                    self.history.append( 'for' )
                                                    self.space = 0
                                                    self.def_starage.append( (loop, tab, self.error) )

                                                else: break             
                                            elif self.get_block == 'if:'    :
                                                self.store_value.append(self.normal_string)
                                                self.def_starage.append( ( self.normal_string, True ) )
                                                
                                                self._values_, self.error =  for_if.INTERNAL_IF_STATEMENT(master=self.master,
                                                            data_base=self.data_base, line=self.if_line).TERMINAL(bool_value=self.value,
                                                             tabulation=self.tabulation + 1, _type_=_type_, c=c)

                                                if self.error is None:
                                                    self.history.append( 'if' )
                                                    self.space = 0
                                                    self.def_starage.append( self._values_ )
                                                else: break                                      
                                            elif self.get_block == 'unless:':
                                                self.store_value.append(self.normal_string)
                                                self.def_starage.append( ( self.normal_string, True ) )
                                                self._values_, self.error = for_unless.INTERNAL_UNLESS_STATEMENT( self.master,
                                                                self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1 )

                                                if self.error is None:
                                                    self.history.append( 'unless' )
                                                    self.space = 0
                                                    self.def_starage.append( self._values_ )

                                                else: break                                            
                                            elif self.get_block == 'try:'   :
                                                self.store_value.append(self.normal_string)
                                                self.def_starage.append( ( self.normal_string, True ) )
                                            
                                                self._values_, self.error = for_try.INTERNAL_TRY_STATEMENT( self.master,
                                                        self.data_base, self.line ).TRY_STATEMENT( tabulation = self.tabulation + 1)

                                                if self.error is None:
                                                    self.history.append( 'try' )
                                                    self.space = 0
                                                    self.def_starage.append( self._values_ )

                                                else: break                                          
                                            elif self.get_block == 'switch:':
                                                self.store_value.append(self.normal_string)
                                                self.def_starage.append( ( self.normal_string, True ) )
                                                self._values_, self.error = for_switch.SWITCH_STATEMENT( self.master,
                                                        self.data_base, self.line ).SWITCH( self.value, self.tabulation + 1 )

                                                if self.error is None:
                                                    self.history.append( 'switch' )
                                                    self.space = 0
                                                    self.def_starage.append( self._values_ )

                                                else: break                                           
                                            elif self.get_block == 'empty'  :
                                                if self.space <= 2:
                                                    self.space += 1
                                                    self.def_starage.append( ( self.normal_string, True ) )
                                                else:
                                                    self.error = er.ERRORS(self.line).ERROR10()
                                                    break                                         
                                            elif self.get_block == 'any'    :
                                                self.store_value.append( self.normal_string )
                                                self.space = 0
                                                self.def_starage.append( ( self.value, True ) )                                           
                                            elif self.get_block == 'def:'   :
                                                self.store_value.append( self.normal_string )
                                                self.db = db.DATA_BASE().STORAGE().copy()
                                                self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'def' )
                                                if self.error is None:
                                                    self.error = EXTERNAL_DEF_WINDOWS( None, self.db, self.line ).TERMINAL( tabulation=self.tabulation+1, 
                                                            class_name=class_name, class_key=class_key, function=function, _type_=_type_, c=c)
                                                                                                                             
                                                    if self.error is None: 
                                                        self.history.append( 'def' )
                                                        self.space = 0
                                                        
                                                        if self.db['func_names'][ 0 ] not in self.subFunc['func_names'] :
                                                            self.db['functions'][0][self.db['func_names'][ 0 ]]['history_of_data'] = [self.db['functions'][0][self.db['func_names'][ 0 ]]['history_of_data']]
                                                            self.db['functions'][0][self.db['func_names'][ 0 ]]['history_of_data'].insert(0, (self.normal_string, True))
                                                            self.subFunc['func_names'].append( self.db['func_names'][ 0 ])  
                                                            self.subFunc['functions'].append( self.db['functions'][0]) 
                                                            mlt.INIT(self.db).INIT()
                                                                        
                                                        else: 
                                                            self.error = er.ERRORS( self.line ).ERROR22( self.db['func_names'][ 0 ] )
                                                            break
                                                    else: break
                                                else: break
                                        else:break
                                    else: break
                                else: break
                            else:
                                self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(normal_string=self.normal_string,
                                            data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)

                                if self.error is None:
                                    if self.get_block   == 'end:'   :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.def_starage.append( ( self.normal_string, False ) )
                                            break
                                        else:
                                            self.error = er.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                            break
                                    elif self.get_block == 'empty'  :
                                        if self.space <= self.max_emtyLine:
                                            self.space += 1
                                            self.def_starage.append( ( self.normal_string, False ) )
                                        else:
                                            self.error = er.ERRORS( self.line ).ERROR10()
                                            break
                                    else:
                                        self.error = er.ERRORS( self.line ).ERROR10()
                                        break
                                else: break
                        else:
                            if self.tabulation == 1: break
                            else:
                                self.normal_string = self.analyse.BUILD_NON_CON(string=self.clear_input,tabulation=self.tabulation)
                                
                                self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(normal_string=self.normal_string,
                                            data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)

                                if self.error is None:
                                    if self.get_block   == 'end:'   :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.def_starage.append( ( self.normal_string, False ) )
                                            break
                                        else:
                                            self.error = er.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                            break
                                    elif self.get_block == 'empty'  :
                                        if self.space <= self.max_emtyLine:
                                            self.space += 1
                                            self.def_starage.append( ( self.normal_string, False ) )
                                        else:
                                            self.error = er.ERRORS( self.line ).ERROR10()
                                            break
                                    else:
                                        self.error = er.ERRORS( self.line ).ERROR10()
                                        break
                                else: break
                    else:
                        if self.space <= self.max_emtyLine:
                            self.space += 1
                            self.loop.append((self.normal_string, False))
                        else:
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break
                elif self.char == 9:  # tabular
                    self.tabular = '\t'
                    self.input = self.input[: self.index] + self.tabular + self.input[self.index:]
                    self.index += 4
             
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                sys.stdout.write(bm.clear.line(pos=0))
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                if self.index > 0:  sys.stdout.write(bm.move_cursor.RIGHT(pos=self.index - self.sub_length))
                else:  pass
                sys.stdout.flush()
            
            except KeyboardInterrupt:
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break

            except TypeError:
                self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                print(self._end_of_file_)
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break
            
        EXTERNAL_DEF_WINDOWS( self.master, self.data_base, self.line ).UPDATE_FUNCTION( self.def_starage, self.subFunc )

        return self.error