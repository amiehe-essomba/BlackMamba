###########################################################
# external module used for creating a main function       #
# we can create function using 2 methods :                #
#                                                         #
# iris = func( color : string, size : float):             #
#       def name():                                       #
#           return 'green'                                #
#       end:                                              #
#                                                         #
#       return name(), size                               #
# end:                                                    #
###########################################################
# def sum(a : int, b : float):                            #  
#       return (a+b)                                      #
# end:                                                    #
###########################################################    
# created by : amiehe-essomba                             #
# updated by : Elena-Royer                                #
###########################################################


from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_statement, for_try
from script.PARXER.PARXER_FUNCTIONS._FOR_.IF.WINDOWS    import WindowsIF as wIF
from script.LEXER.FUNCTION                              import main
from script.DATA_BASE                                   import data_base as db
from script.PARXER                                      import module_load_treatment  as mlt
from src.functions                                      import error as er
from functions                                          import internalDef as ID
from statement.comment                                  import externalCmt
from src.functions.windows                              import subWindowsDef as SWD
from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._FOR_.UNLESS        import WindowsUnless as wU
from script.PARXER.PARXER_FUNCTIONS._FOR_.SWITCH.WINDOWS    import WindowsSwitch as WSw
from script.PARXER.PARXER_FUNCTIONS._FOR_.WHILE.WINDOWS     import WindowsWhile as WWh
from script.PARXER.PARXER_FUNCTIONS._FOR_.BEGIN.WINDOWS     import begin

class EXTERNAL_DEF:
    def __init__(self, 
            master      : str,              
            data_base   : dict,             
            line        : int ,
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
        # history of command 
        self.history            = history
        # canceling def when any command was not typed
        self.store_value        = store_value
        # counting empty line 
        self.space              = space
        #canceling def 
        self.def_cancel         = False
        #contriling string
        self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)

    def DEF( self, 
            tabulation  : int,                  # tabulation for indentation
            def_starage : list,                 # function data storage 
            subFunc     : dict,                 # dictionary of sub function
            class_name  : str   = '' ,          # class name when using in class 
            class_key   : bool  = False,        # class key , set on True when using in class
            c           : str   = '',           # color inside def
            function    : str   = 'def',        # function type
            _type_      : str   = 'def',        # type 
            term        : str   = ''
            ):
        
        #########################################################
        self.if_line            = self.line     # counting
        self.error              = None          # error 
        self.string             = ''            # concatented string
        self.normal_string      = ''            # normal string
        self.end                = ''            # canceling deff

        ##########################################################
        self.active_tab         = None          # activating indentation 
        self.tabulation         = tabulation    # counting indentation 
        self.def_starage        = def_starage   # history of values 
        self.max_emtyLine       = 5             # max line for empty line
        self.subFunc            = subFunc       # sub-function 
        
        ##########################################################
        
        for i in range(1): 
            # concatening string and extraction of string concatenated , tabulation for and indensation and error        
            self.string, self.active_tab, self.error = self.analyse.BUILD_CON(string=self.master,
                                                                        tabulation=self.tabulation)
            if self.error is None:
                # build normal string 
                self.normal_string = self.analyse.BUILD_NON_CON(string=self.master, tabulation=self.tabulation)
                
                # when idendation is True
                if self.active_tab is True :
                    if self.error is None:
                        
                        # get key and value for different functions which can be defined inside a function 
                        self.get_block, self.value, self.error = ID.INTERNAL_BLOCKS( string=self.string,
                                        normal_string=self.normal_string, data_base=self.data_base, 
                                        line=self.if_line ).BLOCKS( tabulation=self.tabulation + 1,
                                        function=function, interpreter = False, class_name= class_name, class_key=class_key,
                                        func_name=self.data_base[ 'current_func' ], loop = False )
                                        
                        if self.error is None:
                            # only in class, when initialize function if defined
                            if class_key is False: pass 
                            else: 
                                if self.get_block not in [ 'empty', 'any' ]:
                                    self.error = er.ERRORS( self.line ).ERROR20( self.get_block[ : -1 ] )
                                    break
                                else: pass
                            if self.error is None:
                                # begin statement
                                if self.get_block   == 'begin:' :
                                    self.store_value.append(self.normal_string)
                                    self.def_starage.append( ( self.normal_string, True ) )
                                    # calling begin module
                                    self._values_, self.error = begin.COMMENT_WINDOWS(data_base=self.data_base,
                                                   line=self.line, term=term).COMMENT( tabulation=self.tabulation + 1, c=c)
                                    
                                    if self.error is None:
                                        # storing data 
                                        self.history.append( 'begin' )
                                        self.space = 0
                                        self.def_starage.append( self._values_ )
                                    else: break 
                                # for loop
                                elif self.get_block == 'for:'   :
                                    self.store_value.append(self.normal_string)
                                    self.def_starage.append( ( self.normal_string, True ) )
                                    
                                    # calling for module
                                    loop, tab, self.error = for_statement.EXTERNAL_FOR_STATEMENT( self.master,
                                                                self.data_base, self.line ).FOR_STATEMENT( self.tabulation+1 )
                                    if self.error is None:
                                        #storing data
                                        self.history.append( 'for' )
                                        self.space = 0
                                        self.def_starage.append( (loop, tab, self.error) )

                                    else: break             
                                # if statement
                                elif self.get_block == 'if:'    :
                                    self.store_value.append(self.normal_string)
                                    self.def_starage.append( ( self.normal_string, True ) )
                                    
                                    # calling if module
                                    self._values_, self.error = wIF.EXTERNAL_IF_WINDOWS(data_base=self.data_base, line=self.if_line, term=term ).TERMINAL(
                                            bool_value= self.value, tabulation=self.tabulation + 1, _type_ = _type_, c=c)
                                    
                                    if self.error is None:
                                        self.history.append( 'if' )
                                        self.space = 0
                                        self.def_starage.append( self._values_ )
                                    else: break                                      
                                # unless statement
                                elif self.get_block == 'unless:':
                                    self.store_value.append(self.normal_string)
                                    self.def_starage.append( ( self.normal_string, True ) )
                                    
                                    # calling unless modules
                                    self._values_, self.error = wU.EXTERNAL_UNLESS_WINDOWS(data_base=self.data_base, line=self.if_line, term=term ).TERMINAL(
                                            bool_value= self.value, tabulation=self.tabulation + 1, _type_ = _type_, c=c )

                                    if self.error is None:
                                        #storing data 
                                        self.history.append( 'unless' )
                                        self.space = 0
                                        self.def_starage.append( self._values_ )

                                    else: break                                            
                                # try statement
                                elif self.get_block == 'try:'   :
                                    self.store_value.append(self.normal_string)
                                    self.def_starage.append( ( self.normal_string, True ) )

                                    # calling try module
                                    self._values_, self.error = for_try.INTERNAL_TRY_STATEMENT( self.master,
                                            self.data_base, self.line ).TRY_STATEMENT( tabulation = self.tabulation + 1)

                                    if self.error is None:
                                        # storage data
                                        self.history.append( 'try' )
                                        self.space = 0
                                        self.def_starage.append( self._values_ )

                                    else: break                                          
                                # switch statement
                                elif self.get_block == 'while:' :
                                    self.store_value.append(self.normal_string)
                                    self.def_starage.append((self.normal_string, True))
                                    # calling while module
                                    self._values_, self.error = WWh.EXTERNAL_WHILE_WINDOWS(data_base=self.data_base,
                                            line=self.if_line, term=term).TERMINAL(  bool_value=self.value, tabulation=self.tabulation + 1, _type_=_type_, c=c)

                                    if self.error is None:
                                        self.history.append('while')
                                        self.space = 0
                                        self.def_starage.append(self._values_)
                                    else:  break
                                elif self.get_block == 'switch:':
                                    self.store_value.append(self.normal_string)
                                    self.def_starage.append( ( self.normal_string, True ) )
                                    
                                    # calling switch module
                                    self._values_, self.error = WSw.EXTERNAL_SWITCH_WINDOWS(data_base=self.data_base,
                                                        line=self.if_line, term=term).TERMINAL(  bool_value=self.value,
                                                            tabulation=self.tabulation + 1, _type_=_type_, c=c)

                                    if self.error is None:
                                        # data storage
                                        self.history.append( 'switch' )
                                        self.space = 0
                                        self.def_starage.append( self._values_ )

                                    else: break                                           
                                #empty line
                                elif self.get_block == 'empty'  :
                                    # when space is lower than max_emptyLine
                                    if self.space <= self.max_emtyLine:
                                        self.space += 1
                                        self.def_starage.append( ( self.normal_string, True ) )
                                    else:
                                        self.error = er.ERRORS(self.line).ERROR10()
                                        break                                         
                                # function value
                                elif self.get_block == 'any'    :
                                    self.store_value.append( self.normal_string )
                                    self.space = 0
                                    self.def_starage.append( ( self.value, True ) )                                           
                                # functions
                                elif self.get_block == 'def:'   :
                                    self.store_value.append( self.normal_string )
                                    
                                    # data base initialization
                                    self.db = db.DATA_BASE().STORAGE().copy()
                                    # get lexer for function arguments extraction 
                                    self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'def' )
                                    if self.error is None:
                                        # calling the sub-function 
                                        self.error = SWD.INTERNAL_DEF_WINDOWS(data_base=self.db, line=self.line,term=term).TERMINAL( tabulation=self.tabulation+1, 
                                                class_name=class_name, class_key=class_key, function=function, _type_=_type_, c=c)
                                                                                                                    
                                        if self.error is None: 
                                            self.history.append( 'def' )
                                            self.space = 0
                                            if self.db['func_names'][ 0 ] not in self.subFunc['func_names'] :
                                                
                                                # updating sub-function values, history of data, name etc..
                                                self.db['functions'][0][self.db['func_names'][ 0 ]]['history_of_data'] = [self.db['functions'][0][self.db['func_names'][ 0 ]]['history_of_data']]
                                                self.db['functions'][0][self.db['func_names'][ 0 ]]['history_of_data'].insert(0, (self.normal_string, True))
                                                self.subFunc['func_names'].append( self.db['func_names'][ 0 ])  
                                                self.subFunc['functions'].append( self.db['functions'][0]) 
                                                
                                                # data base initializing
                                                mlt.INIT(self.db).INIT()     
                                            else: 
                                                self.error = er.ERRORS( self.line ).ERROR22( self.db['func_names'][ 0 ] )
                                                break
                                        else: break
                                    else: break
                                elif self.get_block == 'comment_line':
                                    self.store_value.append(self.normal_string)
                                    self.space = 0
                                    self.def_starage.append((self.normal_string, True))
                            else:break
                        else: break
                    else: break
                else:
                    # if tabulation is false ( not indentation)
                    self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(normal_string=self.normal_string,
                                data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)

                    if self.error is None:
                        # closing function
                        if self.get_block   == 'end:'   :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.def_starage.append( ( self.normal_string, False ) )
                                self.def_cancel = True
                                break
                            else:
                                self.error = er.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                break
                        # empty line 
                        elif self.get_block == 'empty'  :
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.def_starage.append( ( self.normal_string, False ) )
                            else:
                                self.error = er.ERRORS( self.line ).ERROR10()
                                break
                        # canceling function due to an error
                        else:
                            self.error = er.ERRORS( self.line ).ERROR10()
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
                        # closing function
                        if self.get_block   == 'end:'   :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.def_starage.append( ( self.normal_string, False ) )
                                self.def_cancel = True
                                break
                            else:
                                self.error = er.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                break
                        # empty line 
                        elif self.get_block == 'empty'  :
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.def_starage.append( ( self.normal_string, False ) )
                            else:
                                self.error = er.ERRORS( self.line ).ERROR10()
                                break
                        # canceling function due to an error
                        else:
                            self.error = er.ERRORS( self.line ).ERROR10()
                            break
                    else: break
        
        return self.def_cancel, self.error