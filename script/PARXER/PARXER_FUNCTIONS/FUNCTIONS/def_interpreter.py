from script.STDIN.WinSTDIN                      import stdin
from script                                     import control_string
from statement                                  import externalRest
from script.PARXER.PARXER_FUNCTIONS._IF_        import if_inter
from script.PARXER.PARXER_FUNCTIONS._IF_        import IfError    as Ie
from script.LEXER.FUNCTION                      import main
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS   import functions
from script.PARXER                              import module_load_treatment    as mlt
from functions                                  import internalDef              as ID
from script.DATA_BASE                           import data_base                as db
    

class EXTERNAL_DEF_STATEMENT:
    def __init__(self, master: any, data_base: dict, line: int):
        self.master             = master
        self.line               = line
        self.data_base          = data_base

    def DEF( self, 
            tabulation  : int,  
            class_name  : str   = '' , 
            class_key   : bool  = False,
            _type_      : str   = 'def',
            loop_list   : list  = [], 
            loop        : bool  = False
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
        self.loop_list          = loop_list
        self.next_line          = 0
   
        ##########################################################
        self.subFunc            = {
            'func_names'        : [],
            'functions'         : []
        }

        for j, _string_ in enumerate( self.loop_list ):
            self.if_line        += 1
            self.line           += 1
        
            if _string_ :
                if j >= self.next_line :
                    k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)                   
                    self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                        self.line ).STDIN_FOR_INTERPRETER( k, _string_ )
                    
                    if self.error is None:    
                        if self.active_tab is True:
                            self.get_block, self.value, self.error = ID.INTERNAL_BLOCKS( string=self.string,
                                        normal_string=self.normal_string, data_base=self.data_base, 
                                        line=self.if_line ).BLOCKS( tabulation=k+ 1,
                                        function=_type_, interpreter = False, class_name= class_name, class_key=class_key,
                                        func_name=self.data_base[ 'current_func' ], loop = True, locked=True)
                            
                            if self.error is None:
                                if class_key is False: pass 
                                else: 
                                    if self.get_block not in [ 'empty', 'any', 'end:', 'def:' ]:
                                        self.error = functions.ERRORS( self.line ).ERROR20( self.get_block[ : -1 ] )
                                        break
                                    else: pass
                            
                                if self.error is None:
                                    
                                    if self.get_block   == 'if:'    :
                                        self.next_line              = j+1
                                        self.def_starage.append( ( self.normal_string, True ) )
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                    index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = if_inter.INTERNAL_IF_STATEMENT(self.master,
                                                                self.data_base, self.line).IF_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('if')
                                                self.space      = 0
                                                self.def_starage.append( self._values_ )
                                            
                                            else: break
                                        else: 
                                            self.error = Ie.ERRORS( self.line ).ERROR4()
                                            break                  
                                    elif self.get_block == 'empty'  :
                                        if self.space <= 2:
                                            self.space += 1
                                            self.def_starage.append( ( self.normal_string, True ) )
                                        else:
                                            self.error = functions.ERRORS(self.line).ERROR10()
                                            break
                                    elif self.get_block == 'any'    :
                                        
                                        self.store_value.append( self.normal_string )
                                        self.space = 0
                                        self.def_starage.append( ( self.value, True ) )
                                    elif self.get_block == 'def:'   :
                                        self.next_line              = j+1
                                        self.store_value.append( self.normal_string )
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        
                                        self.db = db.DATA_BASE().STORAGE().copy()#functions.DB.func_data_base
                                        self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'def' )
                                        if self.error is None:
                                            self.error = INTERNAL_DEF_STATEMENT( None, self.db, self.line ).DEF( self.tabulation+1, 
                                                                                                            class_key, class_key, loop = loop )
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
                                                    self.error = functions.ERRORS( self.line ).ERROR22( self.db['func_names'][ 0 ] )
                                                    break
                                            else: break
                                        else: break

                                    ######################################################
                                    ######################################################
                                    
                                    elif self.get_block   == 'end:'   :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.def_starage.append( ( self.normal_string, False ) )
                                            
                                        else:
                                            self.error = functions.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                            break
                                    
                                else:break
                            else: break
                        else:
                            self.get_block, self.value, self.error = externalRest.EXTERNAL_BLOCKS(normal_string=self.normal_string, 
                                                                data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)
                            
                            if self.error is None:
                                if self.get_block   == 'end:'   :
                                    if self.store_value:
                                        del self.store_value[ : ]
                                        del self.history[ : ]
                                        self.def_starage.append( ( self.normal_string, False ) )

                                        break
                                    else:
                                        self.error = functions.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                        break

                                elif self.get_block == 'empty'  :
                                    if self.space <= 2:
                                        self.space += 1
                                        self.def_starage.append( ( self.normal_string, False ) )
                                    else:
                                        self.error = functions.ERRORS( self.line ).ERROR10()
                                        break

                                else:
                                    self.error = functions.ERRORS( self.line ).ERROR10()
                                    break
                            else: break
                    else: break
                else: pass
            else:
                self.error = Ie.ERRORS( self.line ).ERROR4()
                break
                
        EXTERNAL_DEF_STATEMENT( self.master, self.data_base, self.line ).UPDATE_FUNCTION( self.def_starage, self.subFunc )#self.subFunc

        
        return self.error

    def UPDATE_FUNCTION(self, history_of_data: list, subFunction: dict):
        self.function_names     = self.data_base[ 'func_names' ]
        self.current_function   = self.data_base[ 'current_func' ]
        self.position_in_lists  = self.function_names.index( self.current_function )

        self.function_info      = self.data_base[ 'functions' ][ self.position_in_lists ][ self.current_function ]
        
        if subFunction:  self.function_info['sub_functions']         = subFunction
        else: pass
       
        self.function_info[ 'history_of_data' ]     = history_of_data
        self.data_base[ 'functions' ][ self.position_in_lists ][ self.current_function ] = self.function_info
        self.data_base[ 'current_func' ]            = None

class INTERNAL_DEF_STATEMENT:
    def __init__(self, master: any, data_base: dict, line: int):
        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.analyze            = control_string.STRING_ANALYSE( self.data_base, self.line )

    def DEF( self, 
            tabulation  : int,  
            class_name  : str   = '' ,
            class_key   : bool  = False,
            _type_      : str   = 'def',
            loop_list   : list  = [],
            loop        : bool  = False
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
        self.loop_list          = loop_list
        
        ##########################################################

        for j, _string_ in enumerate( self.loop_list ):
            self.if_line        += 1
            self.line           += 1
            
            if _string_ :
                if j >= self.next_line :
                    k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)                   
                    self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                        self.line ).STDIN_FOR_INTERPRETER( k, _string_ )
                    if self.error is None:    
                        if self.active_tab is True:

                            self.get_block, self.value, self.error = ID.INTERNAL_BLOCKS( string=self.string,
                                        normal_string=self.normal_string, data_base=self.data_base, 
                                        line=self.if_line ).BLOCKS( tabulation=k+ 1,
                                        function=_type_, interpreter = False, class_name= class_name, class_key=class_key,
                                        func_name=self.data_base[ 'current_func' ], loop = True)
                                        
                            if self.error is None:
                                if class_key is False: pass 
                                else: 
                                    if self.get_block not in [ 'empty', 'any' ]:
                                        self.error = functions.ERRORS( self.line ).ERROR20( self.get_block[ : -1 ] )
                                        break
                                    else: pass
                                
                                if self.error is None:
                                    if self.get_block   == 'if:'    :
                                        self.next_line              = j+1
                                        self.def_starage.append( ( self.normal_string, True ) )
                                        self.isbreak    = True
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                    index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = if_inter.EXTERNAL_IF_STATEMENT(self.master,
                                                                self.data_base, self.line).IF_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('if')
                                                self.space      = 0
                                                self.def_starage.append( self._values_ )
                                            
                                            else: break
                                        else: 
                                            self.error = Ie.ERRORS( self.line ).ERROR4()
                                            break
                                    elif self.get_block == 'empty'  :
                                        if self.space <= 2:
                                            self.space += 1
                                            self.def_starage.append( ( self.normal_string, True ) )
                                        else:
                                            self.error = functions.ERRORS(self.line).ERROR10()
                                            break
                                    elif self.get_block == 'any'    :
                                        self.store_value.append( self.normal_string )
                                        self.space = 0
                                        self.def_starage.append( ( self.value, True ) )
                                    elif self.get_block == 'def:'   :
                                        self.val, self.error =  self.analyze.DELETE_SPACE( self.value[3:-1] )
                                        if self.error is None: 
                                            self.error = functions.ERRORS( self.line ).ERROR23( self.val )
                                            break
                                        else: 
                                            self.error = functions.ERRORS( self.line ).ERROR0( self.value )
                                            break
                                        
                                    ######################################################
                                    ######################################################
                                    
                                    elif self.get_block   == 'end:'   :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.def_starage.append( ( self.normal_string, False ) )
                                        else:
                                            self.error = functions.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = functions.ERRORS( self.line ).ERROR10()
                                        break
     
                                else:break
                            else: break
                        else:
                            self.get_block, self.value, self.error = externalRest.EXTERNAL_BLOCKS(normal_string=self.normal_string, 
                                                                data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)

                            if self.error is None:
                                if self.get_block   == 'end:'   :
                                    if self.store_value:
                                        del self.store_value[ : ]
                                        del self.history[ : ]
                                        self.def_starage.append( ( self.normal_string, False ) )

                                        break
                                    else:
                                        self.error = functions.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                        break

                                elif self.get_block == 'empty'  :
                                    if self.space <= 2:
                                        self.space += 1
                                        self.def_starage.append( ( self.normal_string, False ) )
                                    else:
                                        self.error = functions.ERRORS( self.line ).ERROR10()
                                        break

                                else:
                                    self.error = functions.ERRORS( self.line ).ERROR10()
                                    break
                            else: break 
                    else: break
                else: pass
            else:
                self.error = Ie.ERRORS( self.line ).ERROR4()
                break

        EXTERNAL_DEF_STATEMENT( self.master, self.data_base, self.line ).UPDATE_FUNCTION( self.def_starage, {} )

        return self.error
