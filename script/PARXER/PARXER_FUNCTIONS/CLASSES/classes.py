from script.PARXER.PARXER_FUNCTIONS.CLASSES     import end_class
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS   import functions
from script.STDIN.WinSTDIN                      import stdin
from script.LEXER.FUNCTION                      import main
from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from script                                     import control_string
try:
    from CythonModules.Windows                  import fileError as fe
except ImportError:
    from CythonModules.Linux                    import fileError as fe

class EXTERNAL_DEF_STATEMENT:
    def __init__(self, master: any, data_base: dict, line: int, extra: dict):
        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.extra_class_data   = extra

    def CLASSES( self, tabulation: int, _color_ :str = '' ):
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
        self.color              = bm.fg.rbg(199,21, 133 )
        self.class_starage      = []
        self.store_value        = []
        ke                      = bm.fg.rbg( 255, 255, 0)
        self.lexer              = None
        self.classes_before     = self.data_base[ 'classes' ][ : ]
        self.names_before       = self.data_base[ 'class_names' ][ : ]
        
        ##########################################################
        self._subClass_     = {
            'classes'       : [],
            'class_names'   : []
        }
        ##########################################################

        while self.end != 'end:' :
            self.if_line        += 1
            self.line           += 1

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                        self.line ).STDIN({ '0': ke, '1': self.color }, self.tabulation )

                if self.error is None:
                    if self.active_tab is True:
                            self.get_block, self.value, self.error = end_class.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )
                            if self.error is None:
                                if self.get_block   == 'def:'   :
                                    self.db = DB.def_data_base
                                    self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'class' )
                                    if self.error is None:
                                        self.key_init, self.error = EXTERNAL_DEF_STATEMENT(self.master, self.data_base,
                                                 self.line, self.extra_class_data).UPDATE_FUNCTION_BEFORE( self.lexer )
                                        if self.error is None:
                                            self.error = functions.EXTERNAL_DEF_STATEMENT( self.master, self.db,
                                                                    self.line ).DEF( self.tabulation + 1,
                                                                    self.data_base[ 'current_class' ], self.key_init )
                                            if self.error is None:
                                                self.error = EXTERNAL_DEF_STATEMENT(self.master, self.data_base,
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
                                        else: break
                                    else: break
                                elif self.get_block == 'class:' :
                                    
                                    self.db = DB.class_data_base
                                    self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'class' )
                                    if self.error is None:
                                        
                                        self.error = INTERNAL_DEF_STATTEMENT( None, self.db, self.line, 
                                                                         self.lexer['class'] ).CLASSES( self.tabulation + 1 )
                                
                                        if self.error is None:
                                            self.error = EXTERNAL_DEF_STATEMENT(self.master, self.db,
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
                                    else: break
                                elif self.get_block == 'empty'  :
                                        if self.space <= 2:
                                            self.space += 1
                                            #self.class_starage.append( ( self.normal_string, True ) )
                                        else:
                                            self.error = ERRORS(self.line).ERROR10()
                                            break
                            else: break
                    else:
                        self.get_block, self.value, self.error = end_class.EXTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )
                        if self.error is None:
                            if self.get_block   == 'end:'   :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.class_starage.append( ( self.normal_string, False ) )
                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break
                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
                                    self.space += 1
                                    #self.class_starage.append( ( self.normal_string, False ) )
                                else:
                                    self.error = ERRORS( self.line ).ERROR10()
                                    break
                            else:
                                self.error = ERRORS( self.line ).ERROR10()
                                break
                        else: break
                else:
                    if self.tabulation == 1: break
                    else:
                        self.get_block, self.value, self.error = end_class.EXTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.line).BLOCKS(  self.tabulation)

                        if self.error is None:
                            if self.get_block   == 'end:'   :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.class_starage.append( ( self.normal_string, False ) )
                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break
                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
                                    self.space += 1
                                    #self.def_starage.append((self.normal_string, False))
                                else:
                                    self.error = ERRORS(self.line).ERROR10()
                                    break
                            else:
                                self.error = ERRORS(self.line).ERROR10()
                                break
                        else: break
            except KeyboardInterrupt:
                self.error = ERRORS(self.line).ERROR10()
                break

        if self.error is None:
            EXTERNAL_DEF_STATEMENT( self.master, self.data_base, self.line, {} ).UPDATE_CLASS( self.class_starage )
        else:
            self.data_base[ 'classes' ]     = self.classes_before
            self.data_base[ 'class_names' ] = self.names_before
            try:
                self.db['current_func']     = None
                self.db['func_names']       = []
                self.db['functions']        = []
            except AttributeError: pass

        #print( self.data_base['classes'])
        return self.error

    def UPDATE_FUNCTION_BEFORE(self,  lexer : dict):
        self.error              = None
        self.key_init           = False
        self.functions          = lexer[ 'def' ]
        self.type               = self.functions[ 'type' ]
        self.arguments          = self.functions[ 'arguments' ]
        self.values             = self.functions[ 'value' ]
        self.history            = self.functions[ 'history_of_data' ]
        self.db                 = DB.def_data_base
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
                    self.error = ERRORS( self.line ).ERROR1( self.class_name )
                else: self.error = ERRORS( self.line ).ERROR2( )
            else:
                if self.func_name in self.extra_class_data[ 'function_names' ]:
                    self.error = ERRORS( self.line ).ERROR0( self.func_name, self.class_name )
                else:   self.extra_class_data[ 'function_names' ].append( self.func_name )

        return  self.key_init, self.error

    def UPDATE_FUNCTION_AFTER( self , header : tuple, db : dict, subClass : bool = False, subDict = None):
        
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
                else: self.error = ERRORS( self.line ).ERROR18( self.subNames[ 0 ] )
                  
            self.db['class_names']  = []
            self.db['classes']      = []
        
        return self.error 
    
    def UPDATE_CLASS( self, history_of_data: list ):
        self.class_names        = self.data_base[ 'class_names' ]
        self.current_class      = self.data_base[ 'current_class' ]
        self.position_in_lists  = self.class_names.index( self.current_class )
        
        self.data_base[ 'classes' ][ self.position_in_lists ] = history_of_data
        self.data_base[ 'current_class' ]         = None

class INTERNAL_DEF_STATTEMENT:
    def __init__(self, master: any, data_base: dict, line: int, extra: dict):
        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.extra_class_data   = extra
        self.analyze            = control_string.STRING_ANALYSE( self.data_base, self.line )
        
    def CLASSES( self, tabulation: int, _color_ :str = '' ):
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
        self.color              = bm.fg.rbg(0,100, 250 )
        self.class_starage      = []
        self.store_value        = []
        ke                      = bm.fg.rbg( 255, 255, 0)
        self.lexer              = None
        self.classes_before     = self.data_base[ 'classes' ][ : ]
        self.names_before       = self.data_base[ 'class_names' ][ : ]
        ##########################################################
        self._subClass_     = {
            'classes'       : [],
            'class_names'   : []
        }
        ##########################################################

        while self.end != 'end:' :
            self.if_line        += 1
            self.line           += 1

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                        self.line ).STDIN({ '0': ke, '1': self.color }, self.tabulation )

                if self.error is None:
                    if self.active_tab is True:
                            self.get_block, self.value, self.error = end_class.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )
                            if self.error is None:
                                if self.get_block   == 'def:'   :
                                    self.db = DB.def_data_base
                                    self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'class' )
                                    if self.error is None:
                                        self.key_init, self.error = EXTERNAL_DEF_STATEMENT(self.master, self.data_base,
                                                 self.line, self.extra_class_data).UPDATE_FUNCTION_BEFORE( self.lexer )
                                        if self.error is None:
                                            self.error = functions.EXTERNAL_DEF_STATEMENT( self.master, self.db,
                                                                    self.line ).DEF( self.tabulation + 1,
                                                                    self.data_base[ 'current_class' ], self.key_init )
                                            if self.error is None:
                                                EXTERNAL_DEF_STATEMENT(self.master, self.data_base,
                                                    self.line, self.extra_class_data).UPDATE_FUNCTION_AFTER(
                                                    ( self.normal_string, True ), self.db )
                                                if not self.class_starage:
                                                    self.class_starage.append( ( self.extra_class_data, True) )
                                                else:
                                                    self.class_starage[ 0 ] = ( self.extra_class_data, True)
                                                self.store_value.append( self.normal_string )
                                                self.history.append( 'class' )
                                                self.space      = 0
                                                self.key_init   = False
                                            else: break
                                        else: break
                                    else: break
                                elif self.get_block == 'class:' :
                                    try:
                                        self.val, self.error =  self.analyze.DELETE_SPACE( self.value[5:-1] )
                                        if self.error is None: 
                                            self.error = ERRORS( self.line ).ERROR3( self.val )
                                            break
                                        else: 
                                            self.error = ERRORS( self.line ).ERROR4( self.value )
                                            break
                                    except IndexError: 
                                        self.error = ERRORS( self.line ).ERROR4( self.value )
                                        break
                                elif self.get_block == 'empty'  :
                                        if self.space <= 2:
                                            self.space += 1
                                        else:
                                            self.error = ERRORS(self.line).ERROR10()
                                            break
                            else: break
                    else:
                        self.get_block, self.value, self.error = end_class.EXTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )
                        if self.error is None:
                            if self.get_block   == 'end:'   :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.class_starage.append( ( self.normal_string, False ) )
                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break
                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
                                    self.space += 1
                                    #self.class_starage.append( ( self.normal_string, False ) )
                                else:
                                    self.error = ERRORS( self.line ).ERROR10()
                                    break
                            else:
                                self.error = ERRORS( self.line ).ERROR10()
                                break
                        else: break
                else:
                    if self.tabulation == 1: break
                    else:
                        self.get_block, self.value, self.error = end_class.EXTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.line).BLOCKS(  self.tabulation)

                        if self.error is None:
                            if self.get_block   == 'end:'   :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.class_starage.append( ( self.normal_string, False ) )
                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break
                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
                                    self.space += 1
                                    #self.def_starage.append((self.normal_string, False))
                                else:
                                    self.error = ERRORS(self.line).ERROR10()
                                    break
                            else:
                                self.error = ERRORS(self.line).ERROR10()
                                break
                        else: break
            except KeyboardInterrupt:
                self.error = ERRORS(self.line).ERROR10()
                break

        if self.error is None:
            EXTERNAL_DEF_STATEMENT( self.master, self.data_base, self.line, {} ).UPDATE_CLASS( self.class_starage )
        else:
            self.data_base[ 'classes' ]     = self.classes_before
            self.data_base[ 'class_names' ] = self.names_before
            try:
                self.db['current_func']     = None
                self.db['func_names']       = []
                self.db['functions']        = []
            except AttributeError: pass

        return self.error

class DB:
    def_data_base   = {
        'variables'         : {
            'vars'          : [],
            'values'        : []
        },
        'global_vars'       : {
            'vars'          : [],
            'values'        : []
        },
        'return'            : [],
        'empty_values'      : None,
        'total_vars'        : None,
        'return'            : None,
        'print'             : [],
        'irene'             : None,
        'sub_print'         : None,
        'transformation'    : None,
        'functions'         : [],
        'classes'           : [],
        'class_names'       : [],
        'func_names'        : [],
        'current_func'      : None,
        'current_class'     : None,
        'no_printed_values' : [],
    }

    class_data_base = {
        'variables'         : {
            'vars'          : [],
            'values'        : []
        },
        'global_vars'       : {
            'vars'          : [],
            'values'        : []
        },
        'return'            : [],
        'empty_values'      : None,
        'total_vars'        : None,
        'return'            : None,
        'print'             : [],
        'irene'             : None,
        'sub_print'         : None,
        'transformation'    : None,
        'functions'         : [],
        'classes'           : [],
        'class_names'       : [],
        'func_names'        : [],
        'current_func'      : None,
        'current_class'     : None,
        'no_printed_values' : [],
    }
    
class ERRORS:
    def __init__(self, line: int):
        self.line           = line
        self.cyan           = bm.fg.cyan_L
        self.red            = bm.fg.red_L
        self.green          = bm.fg.green_L
        self.yellow         = bm.fg.yellow_L
        self.magenta        = bm.fg.magenta_M
        self.white          = bm.fg.white_L
        self.blue           = bm.fg.blue_L
        self.reset          = bm.init.reset

    def ERROR0(self, name_func: str, name_class: str):
        error = '{}is already defined in the {}{}( ) {}class. {}line: {}{}'.format(self.white, self.blue, name_class, self.red,
                                                                          self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors()+ '{}the function {}{}( ) '.format(self.white, self.green,
                                                                name_func ) + error
        return self.error+self.reset

    def ERROR1(self, class_name: str ):
        error = '{}initialize( ) {}function is already defined in {}{}( ) {}{}. {}line : {}{}'.format(self.red,
                                                                self.white, self.blue, class_name, self.red, 'class',
                                                                 self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ error
        return self.error+self.reset

    def ERROR2(self ):
        error = '{}set {}initialize( ) {}function before any orthers functions. {}line : {}{}'.format( self.white, self.red,
                                                self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ error
        return self.error+self.reset
    
    def ERROR3( self, string ):
        error = '{}cannot be {}a class. {}line: {}{}'.format(self.white, self.yellow, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}The subclass {}{} '.format(self.white,  self.red, string) + error
        return self.error + self.reset
    
    def ERROR4( self, string ):
        error = '{}<< {} >>. {}line: {}{}'.format(self.cyan, string, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}invalid syntax in '.format( self.white) + error
        return self.error + self.reset

    def ERROR10( self ):
        self.error = fe.FileErrors('IndentationError').Errors() + '{}unexpected an indented block, {}line: {}{}'.format(
                                                self.yellow,  self.white, self.yellow, self.line)
        return self.error + self.reset

    def ERROR17( self, string ):
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format(self.green,
                                                self.white, self.cyan, string, self.white, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}invalid syntax. '.format(self.white) + error
        return self.error + self.reset
    
    def ERROR18( self, string ):
        error = '{}already exits. {}line: {}{}'.format(self.yellow, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('NameError').Errors() + '{}the class name {}{} '.format(self.white, self.red, string,) + error
        return self.error + self.reset
