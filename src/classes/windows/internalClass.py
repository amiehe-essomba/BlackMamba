from script.PARXER.PARXER_FUNCTIONS.CLASSES     import end_class
from src.functions.windows                      import windowsDef as WD
from script.STDIN.WinSTDIN                      import stdin
from script.LEXER.FUNCTION                      import main
from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from src.classes                                import errorClass as EC
from src.classes                                import db
from src.classes                                import updatingClasses as UC
from script                                     import control_string
from statement.comment                          import externalCmt

class INTERNAL_CLASS:
    def __init__(self, 
                master      : str, 
                data_base   : dict, 
                line        : int, 
                extra       : dict,
                history     : list,
                store_value : list,
                space       : int,
                ):
        
        # main string
        self.master             = master
        # current line in the IDE
        self.line               = line
        # data base 
        self.data_base          = data_base
        # external data containig certain informatios regarding classes  
        self.extra_class_data   = extra
        # class canceling key
        self.class_cancel       = False
        # history of command 
        self.history            = history
        # canceling def when any command was not typed
        self.store_value        = store_value
        # counting empty line 
        self.space              = space
        #contriling string
        self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)
        
    def CLASS( self, 
                tabulation      : int,
                class_starage   : list,
                _type_          : str = 'class',
                c               : str = '' 
                ):
        
        self.error              = None
        self.string             = ''
        self.normal_string      = ''

        ##########################################################
        self.active_tab         = None
        self.tabulation         = tabulation
        self.class_starage      = class_starage
        self.lexer              = None
        self.max_emtyLine       = 5
        
        ##########################################################

        for i in range(1):
            # concatening string and extraction of string concatenated , tabulation for and indensation and error        
            self.string, self.active_tab, self.error = self.analyse.BUILD_CON(string=self.master,
                                                                        tabulation=self.tabulation)
            if self.error is None:
                # build normal string 
                self.normal_string = self.analyse.BUILD_NON_CON(string=self.master, tabulation=self.tabulation)
                
                # when idendation is True
                if self.active_tab is True:
                        self.get_block, self.value, self.error = end_class.INTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )
                        if self.error is None:
                            # function block
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
                                                        class_key  = self.key_init, function='class')
                                        
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
                            # sub-classs block
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
                            #empty line 
                            elif self.get_block == 'empty'  :
                                    if self.space <= self.max_emtyLine:
                                        self.space += 1
                                        self.class_starage.append( ( self.normal_string, True ) )
                                    else:
                                        self.error = EC.ERRORS(self.line).ERROR10()
                                        break
                        else: break
                else:
                    self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(normal_string=self.normal_string,
                            data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)
        
                    if self.error is None:
                        # closing class
                        if self.get_block   == 'end:'   :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.class_starage.append( ( self.normal_string, False ) )
                                self.class_cancel = True
                                break
                            else:
                                self.error = EC.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                break
                        # empty line
                        elif self.get_block == 'empty'  :
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.class_starage.append( ( self.normal_string, False ) )
                            else:
                                self.error = EC.ERRORS( self.line ).ERROR10()
                                break
                        # canceling function due to an error
                        else:
                            self.error = EC.ERRORS( self.line ).ERROR10()
                            break
                    else: break
            else:
                if self.tabulation == 1: break
                else:
                    # if tabulation is false ( not indentation)
                    self.error = None
                    self.normal_string = self.analyse.BUILD_NON_CON(string=self.master,tabulation=self.tabulation)
                    
                    self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(normal_string=self.normal_string,
                            data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)
    
                    if self.error is None:
                        # ending class
                        if self.get_block   == 'end:'   :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.class_starage.append( ( self.normal_string, False ) )
                                self.class_cancel = True
                                break
                            else:
                                self.error = EC.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                break
                        # empty line
                        elif self.get_block == 'empty'  :
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.class_starage.append( ( self.normal_string, False ) )
                            else:
                                self.error = EC.ERRORS(self.line).ERROR10()
                                break
                        # canceling function due to an error
                        else:
                            self.error = EC.ERRORS(self.line).ERROR10()
                            break
                    else: break
         
        if self.error is None: 
            try:
                self.db['current_func']     = None
                self.db['func_names']       = []
                self.db['functions']        = []
            except AttributeError: pass
        else: pass

        return self.class_cancel, self.error