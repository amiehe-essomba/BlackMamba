from script.PARXER.PARXER_FUNCTIONS.CLASSES     import end_class
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS   import functions
from src.functions.windows                      import windowsDef as WD
from script.STDIN.WinSTDIN                      import stdin
from script.LEXER.FUNCTION                      import main
from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from script                                     import control_string
from src.classes                                import errorClass as EC
from src.classes                                import db
from src.classes                                import updatingClasses as UC

class EXTERNAL_DEF_STATEMENT:
    def __init__(self, master: any, data_base: dict, line: int, extra: dict):
        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.extra_class_data   = extra

    def CLASSES( self, 
                tabulation  : int,
                _type_      : str = 'class',
                c           : str = '' 
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
        self.color              = bm.fg.rbg(199,21, 133 )
        self.class_starage      = []
        self.store_value        = []
        ke                      = bm.fg.rbg( 255, 255, 0)
        self.lexer              = None
        self.classes_before     = self.data_base[ 'classes' ][ : ]
        self.names_before       = self.data_base[ 'class_names' ][ : ]
        self.max_emtyLine       = 5
        
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
                                    self.db = db.DB.def_data_base
                                    self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'class' )
                                    if self.error is None:
                                        self.key_init, self.error = UC.UPDATING(self.data_base,
                                                 self.line, self.extra_class_data).UPDATE_FUNCTION_BEFORE( self.lexer )
                                        if self.error is None:
                                            self.error = WD.EXTERNAL_DEF_WINDOWS(data_base=self.db,  line=self.line).TERMINAL(tabulation=self.tabulation + 1, c=c,
                                                            _type_ = _type_, class_name = self.data_base[ 'current_class' ], class_key  = self.key_init, function='def')
                                            if self.error is None:
                                                self.error = UC.UPDATING(self.data_base,
                                                    self.line, self.extra_class_data).UPDATE_FUNCTION_AFTER(
                                                    ( self.normal_string, True ), self.db )
                                                
                                                if self.error is None:
                                                    if not self.class_starage:  self.class_starage.append( ( self.extra_class_data, True) )
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
                                    
                                    self.db = db.DB.class_data_base
                                    self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'class' )
                                    if self.error is None:
                                        
                                        self.error = INTERNAL_DEF_STATTEMENT( master=None, data_base=self.db, line=self.line, 
                                                                        extra=self.lexer['class'] ).CLASSES( tabulation=self.tabulation + 1,
                                                                        c=c, _type_=_type_)
                                
                                        if self.error is None:
                                            self.error = UC.UPDATING(self.db,
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
                                        if self.space <= self.max_emtyLine:
                                            self.space += 1
                                            self.class_starage.append( ( self.normal_string, True ) )
                                        else:
                                            self.error = EC.ERRORS(self.line).ERROR10()
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
                                    self.error = EC.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break
                            elif self.get_block == 'empty'  :
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.class_starage.append( ( self.normal_string, False ) )
                                else:
                                    self.error = EC.ERRORS( self.line ).ERROR10()
                                    break
                            else:
                                self.error = EC.ERRORS( self.line ).ERROR10()
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
                                    self.error = EC.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break
                            elif self.get_block == 'empty'  :
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.class_starage.append( ( self.normal_string, False ) )
                                else:
                                    self.error = EC.ERRORS(self.line).ERROR10()
                                    break
                            else:
                                self.error = EC.ERRORS(self.line).ERROR10()
                                break
                        else: break
            except KeyboardInterrupt:
                self.error = EC.ERRORS(self.line).ERROR10()
                break

        if self.error is None:
            UC.UPDATING( self.data_base, self.line, {} ).UPDATE_CLASS( self.class_starage )
        else:
            self.data_base[ 'classes' ]     = self.classes_before
            self.data_base[ 'class_names' ] = self.names_before
            try:
                self.db['current_func']     = None
                self.db['func_names']       = []
                self.db['functions']        = []
            except AttributeError: pass

        return self.error

class INTERNAL_DEF_STATTEMENT:
    def __init__(self, master: any, data_base: dict, line: int, extra: dict):
        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.extra_class_data   = extra
        self.analyze            = control_string.STRING_ANALYSE( self.data_base, self.line )
        
    def CLASSES( self, 
                tabulation  : int, 
                _type_      : str = 'class',
                c           : str = '' 
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
        self.color              = bm.fg.rbg(0,100, 250 )
        self.class_starage      = []
        self.store_value        = []
        ke                      = bm.fg.rbg( 255, 255, 0)
        self.lexer              = None
        self.classes_before     = self.data_base[ 'classes' ][ : ]
        self.names_before       = self.data_base[ 'class_names' ][ : ]
        self.max_emtyLine       = 5
        
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
                                    self.db = db.DB.def_data_base
                                    self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'class' )
                                    if self.error is None:
                                        self.key_init, self.error = UC.UPDATING(self.data_base,
                                                 self.line, self.extra_class_data).UPDATE_FUNCTION_BEFORE( self.lexer )
                                        if self.error is None:
                                            #self.error = functions.EXTERNAL_DEF_STATEMENT( self.master, self.db,
                                            #                        self.line ).DEF( self.tabulation + 1,
                                            #                        self.data_base[ 'current_class' ], self.key_init )
                                            self.error = WD.EXTERNAL_DEF_WINDOWS(data_base=self.db, 
                                                            line=self.line).TERMINAL(tabulation=self.tabulation + 1, c=c,
                                                            _type_ = _type_, class_name = self.data_base[ 'current_class' ],
                                                            class_key  = self.key_init, function='def')
                                            
                                            if self.error is None:
                                                UC.UPDATING(self.data_base,  self.line, self.extra_class_data).UPDATE_FUNCTION_AFTER(
                                                                                ( self.normal_string, True ), self.db )
                                                if not self.class_starage: self.class_starage.append( ( self.extra_class_data, True) )
                                                else: self.class_starage[ 0 ] = ( self.extra_class_data, True)
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
                                            self.error = EC.ERRORS( self.line ).ERROR3( self.val )
                                            break
                                        else: 
                                            self.error = EC.ERRORS( self.line ).ERROR4( self.value )
                                            break
                                    except IndexError: 
                                        self.error = EC.ERRORS( self.line ).ERROR4( self.value )
                                        break
                                elif self.get_block == 'empty'  :
                                        if self.space <= self.max_emtyLine:
                                            self.space += 1
                                            self.class_starage.append( ( self.normal_string, True ) )
                                        else:
                                            self.error = EC.ERRORS(self.line).ERROR10()
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
                                    self.error = EC.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break
                            elif self.get_block == 'empty'  :
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.class_starage.append( ( self.normal_string, False ) )
                                else:
                                    self.error = EC.ERRORS( self.line ).ERROR10()
                                    break
                            else:
                                self.error = EC.ERRORS( self.line ).ERROR10()
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
                                    self.error = EC.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break
                            elif self.get_block == 'empty'  :
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.def_starage.append((self.normal_string, False))
                                else:
                                    self.error = EC.ERRORS(self.line).ERROR10()
                                    break
                            else:
                                self.error = EC.ERRORS(self.line).ERROR10()
                                break
                        else: break
            except KeyboardInterrupt:
                self.error = EC.ERRORS(self.line).ERROR10()
                break

        if self.error is None:  UC.UPDATING(self.data_base, self.line, {} ).UPDATE_CLASS( self.class_starage )
        else:
            self.data_base[ 'classes' ]     = self.classes_before
            self.data_base[ 'class_names' ] = self.names_before
            try:
                self.db['current_func']     = None
                self.db['func_names']       = []
                self.db['functions']        = []
            except AttributeError: pass

        return self.error
