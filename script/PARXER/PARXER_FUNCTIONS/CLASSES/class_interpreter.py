from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS   import def_interpreter
from src.classes                                import errorClass as classes
from script.STDIN.WinSTDIN                      import stdin
from script.LEXER.FUNCTION                      import main
from statement                                  import externalRest
from script                                     import control_string
from script.PARXER.PARXER_FUNCTIONS._IF_        import IfError    as if_inter
from src.classes                                import db
from classes                                    import internalClass as IC


class EXTERNAL_CLASS_STATEMENT:
    def __init__(self,
                master      : any, 
                data_base   : dict, 
                line        : int, 
                extra       : dict
                ):
        
        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.extra_class_data   = extra

    def CLASSES( self, 
                tabulation  : int, 
                loop_list   : list  = [], 
                _type_      : str   = 'class'
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
        self.history            = [ 'class' ]
        self.class_starage      = []
        self.store_value        = []
        self.lexer              = None
        self.classes_before     = self.data_base[ 'classes' ][ : ]
        self.names_before       = self.data_base[ 'class_names' ][ : ]
        
        ##########################################################
        self._subClass_     = {
            'classes'       : [],
            'class_names'   : []
        }
        self.loop_list          = loop_list
        self.next_line          = 0
        self.comments           = []
        ##########################################################
        
        for j, _string_ in enumerate( self.loop_list):
            if _string_:
                self.if_line        += 1
                self.line           += 1
                
                if j >= self.next_line:
                    k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)  
                    #print(_string_)                 
                    self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                    self.line ).STDIN_FOR_INTERPRETER( k, _string_ )  
                                                            
                    if self.error is None:
                        if self.active_tab is True:
                            self.get_block, self.value, self.error = IC.INTERNAL_BLOCKS(normal_string=self.normal_string, data_base=self.data_base,
                                                            line=self.line).BLOCKS(tabulation=k+1, loop=True)
                            
                            if self.error is None:
                                if self.get_block   == 'def:'           :
                                    self.next_line  = j+1
                                    self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(k, self.loop_list[self.next_line : ],
                                                                                                    index = 'int', _class_ = True)
                                    
                                    self.db = db.DB.def_data_base
                                    self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'class' )
                                    
                                    if self.error is None:
                                        self.key_init, self.error = EXTERNAL_CLASS_STATEMENT(self.master, self.data_base,
                                                self.line, self.extra_class_data).UPDATE_FUNCTION_BEFORE( self.lexer )
                                        if self.error is None:
                                            
                                            if self.NewLIST:	
                                                self.next_line  += len(self.NewLIST)
                                                
                                                self.error = def_interpreter.EXTERNAL_DEF_STATEMENT( self.master, self.db, 
                                                                    self.line ).DEF( k, self.data_base[ 'current_class' ], self.key_init, _type_,
                                                                                self.NewLIST[:-1], loop = True )
                                                
                                                if self.error is None:
                                                    
                                                    self.error = EXTERNAL_CLASS_STATEMENT(self.master, self.data_base,
                                                        self.line, self.extra_class_data).UPDATE_FUNCTION_AFTER(
                                                        ( self.normal_string, True ), self.db )
                                                    
                                                    if self.error is None:
                                                        if not self.class_starage: self.class_starage.append( ( self.extra_class_data, True) )
                                                        else: self.class_starage[ 0 ] = ( self.extra_class_data, True)
                                                        self.store_value.append( self.normal_string )
                                                        self.history.append( 'class' )
                                                        self.space      = 0
                                                        self.key_init   = False
                                                    else: break
                                                else: break
                                            else: 
                                                self.error = if_inter.ERRORS( self.line ).ERROR4()
                                                break  
                                        else: break
                                    else: break
                                elif self.get_block == 'class:'         :
                                    self.next_line              = j+1
                                    self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                    index = 'int', _class_ = True)
                
                                    self.db =  db.DB.class_data_base
                                    self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'class' )
                                    if self.error is None:
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self.error = INTERNAL_CLASS_STATTEMENT( None, self.db, self.line, 
                                                                            self.lexer['class'] ).CLASSES( k, self.NewLIST, _type_ )
                                            if self.error is None:
                                                self.error = EXTERNAL_CLASS_STATEMENT(self.master, self.db,
                                                    self.line, self.extra_class_data).UPDATE_FUNCTION_AFTER(
                                                    ( self.normal_string, True ), self.db , True, self._subClass_ )
                                                
                                                if self.error is None:
                                                    self.store_value.append( self.normal_string )
                                                    self.history.append( 'class' )
                                                    self.space      = 0
                                                    self.extra_class_data[ 'sub_classes'] = self._subClass_
                                                
                                                    if not self.class_starage:
                                                        self.class_starage.append( ( self.extra_class_data , True) )
                                                    else: self.class_starage[ 0 ] = ( self.extra_class_data , True)
                                                else:
                                                    self.extra_class_data[ 'sub_classes']   = None
                                                    self.data_base['sub_classes']           = None 
                                                    break
                                            else: break
                                        else:
                                            self.error = if_inter.ERRORS( self.line ).ERROR4()
                                            break 
                                    else: break
                                elif self.get_block == 'empty'          :
                                        if self.space <= 2:
                                            self.space += 1
                                            self.class_starage.append( ( self.normal_string, True ) )
                                        else:
                                            self.error =  classes.ERRORS(self.line).ERROR10()
                                            break
                                elif self.get_block == 'comment_line'   :
                                    self.comments.append(self.normal_string)
                                    self.space = 0
                                #######################################################
                                #######################################################
                                
                                elif self.get_block   == 'end:'         :
                            
                                    if self.store_value:
                                        del self.store_value[ : ]
                                        del self.history[ : ]
                                        self.class_starage.append( ( self.normal_string, False ) )
                                        
                                    else:
                                        self.error =  classes.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                        break
                            
                            else: break
                        else:
                            self.get_block, self.value, self.error = externalRest.EXTERNAL_BLOCKS(normal_string=self.normal_string, 
                                                                data_base=self.data_base,  line=self.line).BLOCKS(tabulation=self.tabulation)    
                                                                           
                            if self.error is None:     
                                if self.get_block   == 'end:'           :
                                    if self.store_value:
                                        del self.store_value[ : ]
                                        del self.history[ : ]
                                        self.class_starage.append( ( self.normal_string, False ) )
                                        break
                                    else:
                                        self.error =  classes.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                        break
                                elif self.get_block == 'empty'          :
                                    if self.space <= 2:
                                        self.space += 1
                                        self.class_starage.append( ( self.normal_string, False ) )
                                    else:
                                        self.error =  classes.ERRORS( self.line ).ERROR10()
                                        break
                                else:
                                    self.error =  classes.ERRORS( self.line ).ERROR10()
                                    break
                            else: break
                    else: break
                else: pass
            else:
                self.error = if_inter.ERRORS( self.line ).ERROR4()
                break

        if self.error is None:
            EXTERNAL_CLASS_STATEMENT( self.master, self.data_base, self.line, {} ).UPDATE_CLASS( self.class_starage )
        else:
            self.data_base[ 'classes' ]     = self.classes_before
            self.data_base[ 'class_names' ] = self.names_before
            try:
                self.db['current_func']     = None
                self.db['func_names']       = []
                self.db['functions']        = []
            except AttributeError: pass

        return self.error

    def UPDATE_FUNCTION_BEFORE(self,  lexer : dict):
        self.error              = None
        self.key_init           = False
        self.functions          = lexer[ 'def' ]
        self.type               = self.functions[ 'type' ]
        self.arguments          = self.functions[ 'arguments' ]
        self.values             = self.functions[ 'value' ]
        self.history            = self.functions[ 'history_of_data' ]
        self.db                 =  db.DB.def_data_base
        self.func_name          = self.db[ 'func_names' ][ 0 ]
        self.class_name         = self.data_base[ 'current_class' ]

        if not self.extra_class_data[ 'function_names' ] :
            if self.func_name == 'initialize':
                self.key_init   = True
                self.extra_class_data[ 'function_names' ].append( 'initialize' )
                self.extra_class_data[ 'init_function' ] = {
                    'initialize'    : True,
                    'self'          : True,
                    'variables'     : {
                        'vars'      : [],
                        'values'    : []
                    },
                    'function'      : None,
                    'active'        : False
                }
            else: self.extra_class_data[ 'function_names' ].append( self.func_name )
        else:
            if self.func_name == 'initialize':
                if 'initialize' in self.extra_class_data[ 'function_names' ]:
                    self.error =  classes.ERRORS( self.line ).ERROR1( self.class_name )
                else: self.error =  classes.ERRORS( self.line ).ERROR2( )
            else:
                if self.func_name in self.extra_class_data[ 'function_names' ]:
                    self.error =  classes.ERRORS( self.line ).ERROR0( self.func_name, self.class_name )
                else:   self.extra_class_data[ 'function_names' ].append( self.func_name )

        return  self.key_init, self.error

    def UPDATE_FUNCTION_AFTER( self , 
                            header      : tuple, 
                            db          : dict, 
                            subClass    : bool  = False, 
                            subDict     : dict  = None
                            ):
        
        self.error = None 
        
        if subClass is False:
            self.db                 = db
            self.func_name          = self.db[ 'func_names' ][ 0 ]
            self.class_name         = self.data_base[ 'current_class' ]
        
            if self.func_name == 'initialize':
                self.extra_class_data[ 'init_function' ]['function'] = [ header, self.db[ 'functions'][ : ] ]
            else:
                if not self.extra_class_data[ 'functions' ]:
                    self.extra_class_data[ 'functions' ].append( [ header, self.db[ 'functions'][ : ]] )
                else:
                    if self.func_name in self.extra_class_data[ 'function_names' ]:
                        try:
                            self.index = self.extra_class_data[ 'function_names' ].index( self.func_name )
                            self.extra_class_data[ 'functions' ][ self.index] = [ header, self.db[ 'functions'][ : ] ]
                        except IndexError:
                            self.extra_class_data[ 'functions' ].append( [ header, self.db[ 'functions'][ : ]] )
                    else:
                        self.extra_class_data[ 'functions' ].append( [ header, self.db[ 'functions'][ : ]] )
            
            self.db[ 'current_func' ]       = None
            self.db[ 'func_names' ]         = []
            self.db[ 'functions' ]          = []
        
        else:
            self.db = db 
            self.subClasses         = self.db[ 'classes' ]
            self.subNames           = self.db[ 'class_names' ]

            if not subDict['class_names']:
                subDict['class_names'].append( self.subNames[ 0 ] )
                subDict['classes'].append( self.subClasses[ 0 ] )
            else:
                if self.subNames[ 0 ] not in subDict['class_names']:
                    subDict['class_names'].append( self.subNames[ 0 ] )
                    subDict['classes'].append( self.subClasses[ 0 ] )
                else: self.error =  classes.ERRORS( self.line ).ERROR18( self.subNames[ 0 ] )
                  
            self.db['class_names']  = []
            self.db['classes']      = []
        
        return self.error 
    
    def UPDATE_CLASS( self, history_of_data: list ):
        self.class_names        = self.data_base[ 'class_names' ]
        self.current_class      = self.data_base[ 'current_class' ]
        self.position_in_lists  = self.class_names.index( self.current_class )
        
        self.data_base[ 'classes' ][ self.position_in_lists ] = history_of_data
        self.data_base[ 'current_class' ]         = None

class INTERNAL_CLASS_STATTEMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int, 
                extra       : dict
                ):
        
        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.extra_class_data   = extra
        self.analyze            = control_string.STRING_ANALYSE( self.data_base, self.line )
        
    def CLASSES( self, 
                tabulation  : int, 
                loop_list   : list  = [],
                _type_      : str   = 'class' 
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
        self.history            = [ 'class' ]
        self.class_starage      = []
        self.store_value        = []
        self.lexer              = None
        self.classes_before     = self.data_base[ 'classes' ][ : ]
        self.names_before       = self.data_base[ 'class_names' ][ : ]
        ##########################################################
        self._subClass_     = {
            'classes'       : [],
            'class_names'   : []
        }
        self.loop_list          = loop_list
        self.next_line          = 0
        self.comments           = []
        ##########################################################
       
        for j, _string_ in enumerate(self.loop_list):
            self.if_line        += 1
            self.line           += 1
            
            if _string_:
                if j >= self.next_line:
                    k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)                   
                    self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                        self.line ).STDIN_FOR_INTERPRETER( k, _string_ ) 
                    
                    if self.error is None:
                        if self.active_tab is True:
                                self.get_block, self.value, self.error = IC.INTERNAL_BLOCKS(normal_string=self.normal_string, data_base=self.data_base,
                                                            line=self.line).BLOCKS(tabulation=k+1, loop=True)
                               
                                if self.error is None:
                                    if self.get_block   == 'def:'           :
                                        self.next_line              = j+1
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(k, self.loop_list[self.next_line : ],
                                                                                                        index = 'int', _class_ = True)
                                        
                                        self.db = db.DB.def_data_base
                                        self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'class' )
                                        
                                        if self.error is None:
                                            self.key_init, self.error = EXTERNAL_CLASS_STATEMENT(self.master, self.data_base,
                                                    self.line, self.extra_class_data).UPDATE_FUNCTION_BEFORE( self.lexer )
                                            if self.error is None:
                                                if self.NewLIST:
                                                    self.next_line  += len(self.NewLIST)
                                               
                                                    self.error = def_interpreter.EXTERNAL_DEF_STATEMENT( self.master, self.db, 
                                                                        self.line ).DEF( k, self.data_base[ 'current_class' ], self.key_init, _type_,
                                                                                    self.NewLIST, loop = True )
                                                    if self.error is None:
                                                        
                                                        self.error = EXTERNAL_CLASS_STATEMENT(self.master, self.data_base,
                                                            self.line, self.extra_class_data).UPDATE_FUNCTION_AFTER(
                                                            ( self.normal_string, True ), self.db )
                                                   
                                                        if self.error is None:
                                                            if not self.class_starage:
                                                                self.class_starage.append( ( self.extra_class_data, True) )
                                                            else: self.class_starage[ 0 ] = ( self.extra_class_data, True)
                                                            self.store_value.append( self.normal_string )
                                                            self.history.append( 'class' )
                                                            self.space      = 0
                                                            self.key_init   = False
                                                        else: break
                                                    else: break
                                                else: 
                                                    self.error = if_inter.ERRORS( self.line ).ERROR4()
                                                    break  
                                            else: break
                                        else: break
                                    elif self.get_block == 'class:'         :
                                        try:
                                            self.val, self.error =  self.analyze.DELETE_SPACE( self.value[5:-1] )
                                            if self.error is None: 
                                                self.error =  classes.ERRORS( self.line ).ERROR3( self.val )
                                                break
                                            else: 
                                                self.error =  classes.ERRORS( self.line ).ERROR4( self.value )
                                                break
                                        except IndexError: 
                                            self.error =  classes.ERRORS( self.line ).ERROR4( self.value )
                                            break
                                    elif self.get_block == 'empty'          :
                                            if self.space <= 2:
                                                self.space += 1
                                                self.class_starage.append( ( self.normal_string, True ) )
                                            else:
                                                self.error =  classes.ERRORS(self.line).ERROR10()
                                                break
                                    elif self.get_block == 'comment_line'   :
                                        self.comments.append(self.normal_string)
                                        self.space = 0
                                    #################################################
                                    #################################################
                                    
                                    elif self.get_block   == 'end:'         :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.class_starage.append( ( self.normal_string, False ) )
                                    
                                        else:
                                            self.error =  classes.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                            break
                                else: break
                        else:
                            self.get_block, self.value, self.error = externalRest.EXTERNAL_BLOCKS(normal_string=self.normal_string, 
                                                                data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)
                            if self.error is None:
                                if self.get_block   == 'end:'               :
                                    if self.store_value:
                                        del self.store_value[ : ]
                                        del self.history[ : ]
                                        self.class_starage.append( ( self.normal_string, False ) )
                                        break
                                    else:
                                        self.error =  classes.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                        break
                                elif self.get_block == 'empty'              :
                                    if self.space <= 2:
                                        self.space += 1
                                        self.class_starage.append( ( self.normal_string, False ) )
                                    else:
                                        self.error =  classes.ERRORS( self.line ).ERROR10()
                                        break
                                else:
                                    self.error =  classes.ERRORS( self.line ).ERROR10()
                                    break
                            else: break
                    else: pass
                else: pass
            else:
                self.error = if_inter.ERRORS( self.line ).ERROR4()
                break

        if self.error is None:
            EXTERNAL_CLASS_STATEMENT( self.master, self.data_base, self.line, {} ).UPDATE_CLASS( self.class_starage )
        else:
            self.data_base[ 'classes' ]     = self.classes_before
            self.data_base[ 'class_names' ] = self.names_before
            try:
                self.db['current_func']     = None
                self.db['func_names']       = []
                self.db['functions']        = []
            except AttributeError: pass

        return self.error
