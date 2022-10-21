from src.functions.windows                      import windowsDef as WD
from script.LEXER.FUNCTION                      import main
from src.classes                                import errorClass as EC
from src.classes                                import db
from src.classes                                import updatingClasses as UC
from statement.comment                          import externalCmt
from script                                     import control_string
from src.classes.windows                        import subWindowsClass as SWC
from classes                                    import internalClass as IC

class EXTERNAL_CLASS:
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
                _subClass_      : dict, 
                _type_          : str = 'class',
                c               : str = '',
                term            : str = ''
                ):
        
        self.error              = None
        self.string             = ''
        self.normal_string      = ''

        ##########################################################
        self.active_tab         = None
        self.tabulation         = tabulation
        self.class_starage      = class_starage
        self._subClass_         = _subClass_
        self.lexer              = None
        self.max_emtyLine       = 5
        self.comments           = []
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
                        self.get_block, self.value, self.error = IC.INTERNAL_BLOCKS(normal_string=self.normal_string, data_base=self.data_base,
                                                            line=self.line).BLOCKS(tabulation=self.tabulation+1, loop=False)
                            #end_class.INTERNAL_BLOCKS( self.string, self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )
                        if self.error is None:
                            # function block
                            if self.get_block   == 'def:'   :
                                self.db = db.DB.def_data_base
                                self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'class' )
                                if self.error is None:
                                    self.key_init, self.error = UC.UPDATING(self.data_base,
                                                self.line, self.extra_class_data).UPDATE_FUNCTION_BEFORE( self.lexer )
                                    if self.error is None:
                                        self.error = WD.EXTERNAL_DEF_WINDOWS(data_base=self.db,  line=self.line, term=term).TERMINAL(tabulation=self.tabulation + 1, c=c,
                                                        _type_ = _type_, class_name = self.data_base[ 'current_class' ], class_key  = self.key_init, function='class')
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
                            #class block
                            elif self.get_block == 'class:' :
                                
                                self.db = db.DB.class_data_base
                                self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'class' )
                                if self.error is None:
                                    # calling sub-class IDE 
                                    self.error = SWC.INTERNAL_CLASS_WINDOWS( data_base=self.db, line=self.line, 
                                                    extra=self.lexer['class'], term = term).TERMINAL(tabulation=self.tabulation + 1,  c=c, _type_=_type_)
                                    
                                    # checking error 
                                    if self.error is None:
                                        # updating the data 
                                        self.error = UC.UPDATING(self.db,
                                            self.line, self.extra_class_data).UPDATE_FUNCTION_AFTER(
                                            ( self.normal_string, True ), self.db , True, self._subClass_ )
                                        
                                        if self.error is None:
                                            # storing value 
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
                            # empty line 
                            elif self.get_block == 'empty'  :
                                    if self.space <= self.max_emtyLine:
                                        self.space += 1
                                        self.class_starage.append( ( self.normal_string, True ) )
                                    else:
                                        self.error = EC.ERRORS(self.line).ERROR10()
                                        break
                            # comment line
                            elif self.get_block == 'comment_line':
                                self.comments.append(self.normal_string)
                                self.space = 0
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
            # data base initialization 
            try:
                self.db['current_func']     = None
                self.db['func_names']       = []
                self.db['functions']        = []
            except AttributeError: pass
        else: pass
            
        return self.class_cancel, self.error