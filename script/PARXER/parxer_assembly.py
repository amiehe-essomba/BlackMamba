from script.PARXER              import numerical_value
from script.PARXER.VAR_NAME     import get_var_name
from script.PARXER.PRINT        import show_data
from script.LEXER.FUNCTION      import print_value

from script.STDIN.WinSTDIN                              import stdin
from script.PARXER.PARXER_FUNCTIONS._IF_                import if_statement, if_inter
from script.PARXER.PARXER_FUNCTIONS._IF_                import end_else_elif
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import unless_statement, unless_interpreter
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import end_else_elif as _end_else_elif_
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import end_case_default, switch_statement
from script.PARXER.PARXER_FUNCTIONS._FOR_               import end_for_else, for_interpreter
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment as cmt
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import cmt_interpreter as cmt_int
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.LEXER_CONFIGURE                      import numeric_lexer
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_statement, for_if, for_unless, for_switch, for_try
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_block_treatment, for_begin
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS           import functions, def_interpreter
from script.PARXER.PARXER_FUNCTIONS.CLASSES             import classes, class_interpreter
from script.PARXER                                      import module_load_treatment 
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:
    from CythonModules.Windows                          import fileError as fe 
except ImportError:
    from CythonModules.Linux                            import fileError as fe 


class ASSEMBLY( ):
    def __init__(self, master: dict, data_base: dict, line: int ):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.num_parxer     = numerical_value
        self.variables      = self.data_base[ 'variables' ][ 'vars' ]
        self._values_       = self.data_base[ 'variables' ][ 'values' ]
        self.global_vars    = self.data_base[ 'global_vars' ][ 'vars' ]
        self.global_values  = self.data_base[ 'global_vars' ][ 'values' ]
        
        try:
            self._if_egal_  = self.master[ 'if_egal' ]
            self.main_value = self.master[ 'all_data' ]
        except: self._if_egal_ = 'comment'

    def ASSEMBLY(self, main_string : str, key: bool = False, interpreter: bool = False, locked: bool = False):
        self.error          = None
        self._return_       = None
        self.key_return     = False

        if self._if_egal_ == 'comment' : pass

        if self._if_egal_ is None:
            self._return_, self.error = self.num_parxer.NUMERICAL( self.master, self.data_base,
                                                                   self.line ).ANALYSE( main_string )
            if self.error is None:
                if not self.data_base[ 'no_printed_values' ]:
                    if self._return_ is not None:
                        if interpreter is False:
                            if locked is False: 
                                for value in self._return_:
                                    show_data.SHOW( value, self.data_base, key ).SHOW()
                            else: pass
                        else: pass
                    else: pass
                else: self.data_base[ 'no_printed_values' ] = []
            else:
                if self.data_base[ 'no_printed_values' ]: self.data_base[ 'no_printed_values' ] = []
                else : pass

        elif self._if_egal_ == True:
            self._operator_     = self.main_value[ 'operator' ]
            self.var_names      = self.main_value[ 'variable' ]

            for i,  name in enumerate( self.var_names ):
                self.name, self.error = get_var_name.GET_VAR(name, self.data_base, self.line).GET_VAR()
                if self.error is None:
                    self.var_names[ i ] = self.name
                else: break

            if self.error is None:
                self._return_, self.error = self.num_parxer.NUMERICAL( self.master, self.data_base,
                                                                      self.line ).ANALYSE( main_string )
                if self.error is None:
                    if not self.data_base[ 'no_printed_values' ] :
                        for i in range( len( self.var_names ) ):
                            if   type( self.var_names[ i ] ) == type( str() )   :
                                if self.var_names[ i ] in self.variables:
                                    if type( self._return_[ i ] ) == type( str() ):
                                        #self._return_[ i ] = '"'+self._return_[ i ]+'"'
                                        try:
                                            if '"' in self._return_[ i ][ 0 ]: pass
                                            else: pass#self._return_[ i ] = self._return_[ i ]
                                        except IndexError: pass
                                    else: pass

                                    self.idd = self.variables.index( self.var_names[ i ] )
                                    self._values_[ self.idd ] = self._return_[ i ]

                                    if self.global_vars:
                                        if self.var_names[ i ] in self.global_vars:
                                            self.idd = self.global_vars.index( self.var_names[ i ] )
                                            self.global_values[ self.idd ] = self._return_[ i ]
                                        else: pass
                                    else:pass

                                else:
                                    if type( self._return_[ i ] ) == type( str() ):
                                        try:
                                            if '"' in self._return_[ i ][ 0 ]: pass
                                            else: pass #self._return_[ i ] = '"'+self._return_[ i ]+'"'
                                            #self._return_[ i ] = self._return_[ i ]
                                        except IndexError: pass
                                    else: pass

                                    self.variables.append( self.var_names[ i ] )
                                    self._values_.append( self._return_[ i ] )

                                    if self.global_vars:
                                        if self.var_names[ i ] in self.global_vars:
                                            self.idd = self.global_vars.index( self.var_names[ i ] )
                                            self.global_values[ self.idd ] = self._return_[ i ]
                                        else: pass
                                    else: pass

                            elif type( self.var_names[ i ] ) == type( list() )  :

                                self._name_ = self.var_names[ i ][ 0 ][ 'name' ]
                                self.info   = self.var_names[ i ][ 0 ][ 'info' ]

                                if type( self._return_[ i ] ) == type( str() ):
                                    try:
                                        if '"' in self._return_[ 0 ][ i ]: pass
                                        else: pass # self._return_[ i ] = '"' + self._return_[ i ] + '"'
                                    except IndexError: pass
                                else: pass

                                self.idd            = self.variables.index( self._name_ )
                                self.__value__      = self._values_[ self.idd ]

                                for j, _in_ in enumerate( self.info ):
                                    try:
                                        if j != len( self.info ) - 1:
                                            if type( _in_ ) != type( list() ):
                                                self.__value__ = self.__value__[ _in_ ]

                                            else:
                                                for w in _in_:
                                                    self.__value__ = self.__value__[ w ]
                                        else:
                                            if type( _in_ ) != type( list() ):
                                                self.__value__[ _in_ ]  = self._return_[ i ]

                                            else:
                                                for w in _in_:
                                                    if w != len( _in_ ) - 1 :
                                                        self.__value__ = self.__value__[ w ]
                                                    else:
                                                        self.__value__[ w ] = self._return_[ i ]

                                    except TypeError:
                                        self.error = ERRORS( self.line ).ERROR1( self.__value__, 'a list()')
                                        break

                                if self.global_vars:
                                    if self._name_ in self.global_vars:
                                        self._idd_ = self.global_vars.index( self._name_ )
                                        self.global_values[ self._idd_ ] = self._values_[ self.idd ]
                                    else: pass
                                else: pass

                            elif type( self.var_names[ i ] ) == type( dict() )  :
                                self._name_         = self.var_names[ i ][ 'name' ]
                                self._keys_         = self.var_names[ i ][ 'keys' ]

                                if type( self._return_[ i ] ) == type( str() ):
                                    try:
                                        if '"' in self._return_[ 0 ][ i ]: pass
                                        else: pass
                                        #self._return_[ i ] = '"' + self._return_[ i ] + '"'
                                    except IndexError: pass
                                else: pass

                                self.list_keys  = list( self.var_names[ i ] .keys()  )
                                self.idd        = self.variables.index( self._name_ )
                                self.__value__  = self._values_[ self.idd ]

                                if 'info' not in self.list_keys:
                                    for j, keys in enumerate( self._keys_ ):
                                        if j != len( self._keys_ ) - 1:
                                            self.__value__ = self.__value__[ keys ]
                                        else:
                                            self.__value__[ keys ] = self._return_[ i ]
                                else:
                                    self.info = self.var_names[ i ][ 'info' ]
                                    self.all_info = self.info + self._keys_

                                    for j, _in_ in enumerate( self.all_info ):
                                        if j != len( self.all_info ) - 1:
                                            self.__value__ = self.__value__[ _in_ ]
                                        else:
                                            self.__value__[_in_] = self._return_[ i ]

                                if self.global_vars:
                                    if self._name_ in self.global_vars:
                                        self._idd_ = self.global_vars.index( self._name_ )
                                        self.global_values[ self._idd_ ] = self._values_[ self.idd ]
                                    else: pass
                                else: pass

                        self.data_base[ 'variables' ]   = {
                            'vars'                      : self.variables,
                            'values'                    : self._values_
                        }

                        self.data_base[ 'global_vars' ] = {
                            'vars'                      : self.global_vars,
                            'values'                    : self.global_values
                        }
                    else:
                        self.error = ERRORS( self.line ).ERROR2( self.data_base[ 'assigment' ] )
                        self.data_base[ 'no_printed_values' ]   = []
                        self.data_base[ 'assigment' ]           = None
                else: pass
            else: pass

        return self.error  #self._return_, self.key_return, self.error

    def GLOBAL_ASSEMBLY(self, main_string: str, interpreter: bool = False):
        self._return_           = None
        self.key_return         = None
        self.error              = None
        self.active_function    = None
        self.all_data_vars      = list( self.master.keys() )
        self.structure          = [ 'begin', 'if', 'loop_for', 'loop_until', 'loop_while', 'try', 'unless', 'switch' ]

        for i , data in enumerate( self.all_data_vars ):
            if data != 'if_egal':
                if self.master[ data ] is None: pass
                else:
                    self.active_function = data
                    break
            else: pass

        if self.active_function == 'all_data':
            if   self.master[ 'function' ] is None      :
                self.error = ASSEMBLY( self.master, self.data_base, self.line).ASSEMBLY( main_string, interpreter )

            elif self.master[ 'function' ] == 'if'      :

                self._return_, self.error = end_else_elif.MAIN_IF( main_string, self.data_base, self.line ).BOCKS()
                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.listTransform, self.error = for_if.EXTERNAL_IF_STATEMENT( None,
                                            self.data_base, self.line ).IF_STATEMENT( self._return_, 1)

                    if self.error is None:
                        self.newLine                    = self.line 
                        self.error = if_statement.EXTERNAL_IF_LOOP_STATEMENT( None , self.data_base,
                                            self.newLine ).IF_STATEMENT( self._return_, 1, self.listTransform )
                        
                        if self.error is None:
                            if self.data_base[ 'print' ] is not None:
                                self.list_of_values = self.data_base[ 'print' ]
                                for i, value in enumerate( self.list_of_values ):
                                    if i < len( self.list_of_values ) - 1:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                                    else:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )             
                            else: pass
                            self.data_base['print'] = []
                        else: pass 
                    else: pass
                else: pass

            elif self.master[ 'function' ] == 'unless'  :
                self._return_, self.error = _end_else_elif_.MAIN_UNLESS(main_string, self.data_base,
                                                                  self.line).BOCKS()
                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.listTransform, self.error = for_unless.EXTERNAL_UNLESS_STATEMENT( None,
                                            self.data_base, self.line ).UNLESS_STATEMENT( self._return_, 1)
 
                    if self.error is None:
                        self.newLine                    = self.line 
                        self.error = unless_statement.EXTERNAL_UNLESS_LOOP_STATEMENT( None , self.data_base,
                                            self.newLine ).UNLESS_STATEMENT( self._return_, 1, self.listTransform )
                        
                        if self.error is None:
                            if self.data_base[ 'print' ] is not None:
                                self.list_of_values = self.data_base[ 'print' ]
                                for i, value in enumerate( self.list_of_values ):
                                    if i < len( self.list_of_values ) - 1:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                                    else:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )             
                            else: pass
                            self.data_base['print'] = []
                        else: pass 
                    else: pass
                else: pass

            elif self.master[ 'function' ] == 'switch'  :
                self._return_, self.error = end_case_default.MAIN_SWITCH( main_string, self.data_base,
                                                                  self.line).BOCKS()
                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.listTransform, self.error = for_switch.SWITCH_STATEMENT( None,
                                            self.data_base, self.line ).SWITCH( self._return_, 1)
 
                    if self.error is None:
                        self.newLine                    = self.line 
                        self.error = switch_statement.SWITCH_LOOP_STATEMENT( None , self.data_base,
                                            self.newLine ).SWITCH( self._return_, 1, self.listTransform )
                        
                        if self.error is None:
                            if self.data_base[ 'print' ] is not None:
                                self.list_of_values = self.data_base[ 'print' ]
                                for i, value in enumerate( self.list_of_values ):
                                    if i < len( self.list_of_values ) - 1:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                                    else:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )             
                            else: pass
                            self.data_base['print'] = []
                        else: pass 
                    else: pass
                    
                else: pass
                
            elif self.master[ 'function' ] == 'for'     :
                self.value, self.name, self.operator, self.error = end_for_else.MAIN_FOR( self.master, self.data_base,
                                                                self.line ).BOCKS( main_string )

                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.got_errors, self.error = for_block_treatment.TREATMENT( self.data_base,
                                                    self.line ).FOR( main_string, self.value, self.name )

                    if self.error is None:
                        if self.data_base[ 'print' ] is not None:
                            self.list_of_values = self.data_base[ 'print' ]
                            for i, value in enumerate( self.list_of_values ):
                                if len( self.value ) == 1 :
                                    for sub_value in value:
                                        if i < len( self.list_of_values) - 1:
                                            show_data.SHOW( sub_value, self.data_base, False ).SHOW( loop = True)
                                        else:
                                           show_data.SHOW( sub_value, self.data_base, False ).SHOW( loop = False) 
                                else:
                                    if i < len( self.list_of_values) - 1:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                                    else:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = False )

                                if self.got_errors:
                                    print( self.got_errors[ i ])
                                else: pass
                        else: pass
                    else: pass
                    self.data_base['print'] = []

                else: self.error = self.error

            else: print(self.master)

        else:
            if   self.master[ 'begin'  ] is True:
                self.newLine                   = self.line 
                self.listTransform, self.error = for_begin.COMMENT_STATEMENT( None, self.data_base, self.newLine  ).COMMENT( tabulation = 1, color = bm.fg.rbg(255,255,255) )
                if self.error is None:
                    self.error = cmt.COMMENT_LOOP_STATEMENT( None, self.data_base, self.newLine ).COMMENT( 1, self.listTransform ) 
                else: pass              
            elif self.master[ 'delete' ] is True: pass
            elif self.master[ 'global' ] is True: pass
            elif self.master[ 'print'  ] is not None: pass
            elif self.master[ 'transformation' ] is not None: pass
            elif self.master[ 'try' ] is True:
                self.data_base[ 'print' ] = []
                self.newLine                    = self.line 

                self.listTransform, self.error = for_try.EXTERNAL_TRY_STATEMENT( None,
                                            self.data_base, self.newLine ).TRY_STATEMENT( tabulation = 1)
            
                if self.error is None:
                    self._finally_key_, self.error = try_statement.EXTERNAL_TRY_FOR_STATEMENT(None,
                                                        self.data_base, self.newLine ).TRY_STATEMENT(1, self.listTransform)
                    #self._, self.error = try_statement.EXTERNAL_TRY_STATEMENT(None,
                    #                                    self.data_base, self.line ).TRY_STATEMENT(tabulation = 1)
                    if self.error is None:
                        if self.data_base[ 'print' ] is not None:
                            self.list_of_values = self.data_base[ 'print' ]
                            for i, value in enumerate( self.list_of_values ):
                                if i < len( self.list_of_values) - 1:
                                    print_value.PRINT_PRINT( value ).PRINT_PRINT( key = False, loop = True )
                                else:
                                    print_value.PRINT_PRINT( value ).PRINT_PRINT( key = False, loop = True )
                        else:  pass
                    else: pass
                else: pass
            else:
                if   self.data_base[ 'current_func' ]  is not None:
                    self.error = functions.EXTERNAL_DEF_STATEMENT( None, self.data_base, self.line ).DEF( 1 )
                    if self.error is None: pass
                    else: pass
                elif self.data_base[ 'current_class' ] is not None:
                    
                    self.error = classes.EXTERNAL_DEF_STATEMENT( None, self.data_base, self.line, self.master['class']).CLASSES( 1 )
                    if self.error is None: pass
                    else: pass
                elif self.data_base[ 'importation' ]   is not None:
                    self.modules = self.data_base[ 'importation' ] 
                    self.dataS, self.info, self.error = module_load_treatment.TREATMENT( self.modules, self.data_base, 
                                                                                        self.line ).MODULE_MAIN( main_string )
                    if self.error is None:
                        self.error = module_load_treatment.MODULES( self.data_base, self.line, self.dataS, self.info ).LOAD()
                        if self.error is None:
                            self.error = module_load_treatment.CLASSIFICATION( self.data_base, self.line ).CLASSIFICATION( self.data_base[ 'modulesImport' ], 
                                                                                    info = self.data_base[ 'importation' ])
                            
                        else: pass
                    else: pass
                    
                    self.data_base[ 'importation' ] = None
                   
        return  self._return_, self.key_return, self.error

    def GLOBAL_ASSEMBLY_FOR_INTERPRETER(self, 
                                    main_string     : str, 
                                    interpreter     : bool  = False, 
                                    MainList        : list  = [], 
                                    baseFileName    : str   = ''
                                    ):
        
        self._return_           = None
        self.key_return         = None
        self.error              = None
        self.active_function    = None
        self.all_data_vars      = list( self.master.keys() )
        self.structure          = [ 'begin', 'if', 'loop_for', 'loop_until', 'loop_while', 'try', 'unless', 'switch' ]

        for i , data in enumerate( self.all_data_vars ):
            if data != 'if_egal':
                if self.master[ data ] is None: pass
                else:
                    self.active_function = data
                    break
            else: pass

        if self.active_function == 'all_data':
            if   self.master[ 'function' ] is None      :
                self.error = ASSEMBLY( self.master, self.data_base, self.line).ASSEMBLY( main_string, interpreter )

            elif self.master[ 'function' ] == 'if'      :

                self._return_, self.error = end_else_elif.MAIN_IF( main_string, self.data_base,
                                                                   self.line ).BOCKS()
                if self.error is None:
                    self.data_base[ 'print' ]       = []
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                    self.newLine                    = self.line
                    
                    self.listTransform ,self.error  = if_inter.EXTERNAL_IF_STATEMENT( None, self.data_base,
                                                                         self.line ).IF_STATEMENT(1, self.NewLIST )
                    if self.error is None:
                        self.MainStringTransform        = 't'+main_string
                        self.listTransform              = [(self.MainStringTransform , True), self.listTransform]
                        
                        self.error = if_statement.EXTERNAL_IF_LOOP_STATEMENT( None , self.data_base,
                                            self.newLine ).IF_STATEMENT( self._return_, 1, self.listTransform )
                        if self.error is None:
                            if self.data_base[ 'print' ] is not None:
                                self.list_of_values = self.data_base[ 'print' ]
                                for i, value in enumerate( self.list_of_values ):
                                    if i < len( self.list_of_values ) - 1:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                                    else:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )   
                            else: pass
                            self.data_base['print'] = []
                        else: pass
                    else: pass
                else:
                    self.error = self.error

            elif self.master[ 'function' ] == 'unless'  : 
                self._return_, self.error = _end_else_elif_.MAIN_UNLESS(main_string, self.data_base,
                                                                  self.line).BOCKS()
                if self.error is None:
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                
                    self.error                      = unless_interpreter.EXTERNAL_UNLESS_STATEMENT(None, self.data_base,
                                                                            self.line).UNLESS_STATEMENT(self._return_, 1, self.NewLIST )
                    
                    if self.error is None:
                        if self.data_base[ 'print' ] is not None:
                            self.list_of_values = self.data_base[ 'print' ]
                            for i, value in enumerate( self.list_of_values ):
                                if i < len( self.list_of_values ) - 1:
                                    print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                                else:
                                    print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )
                                    
                        else: pass
                        self.data_base['print'] = []
                    else: pass
                else: pass

            elif self.master[ 'function' ] == 'switch'  :
                self._return_, self.error = end_case_default.MAIN_SWITCH( main_string, self.data_base,
                                                                  self.line).BOCKS()
                if self.error is None:
                    self.error = switch_statement.SWITCH_STATEMENT (None, self.data_base,
                                                        self.line).SWITCH(self._return_, 1)
                else:
                    self.error = self.error

            elif self.master[ 'function' ] == 'for'     :
                self.value, self.name, self.operator, self.error = end_for_else.MAIN_FOR( self.master, self.data_base,
                                                                self.line ).BOCKS( main_string )
                
                if self.error is None:
                    self.data_base['variables']['vars'].append(self.name)
                    self.data_base['variables']['values'].append(self.value[-1])
                    
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                    self.newLine                    = self.line
                    
                    self.listTransform = for_interpreter.EXTERNAL_FOR_STATEMENT( None, self.data_base,
                                                                         self.line ).FOR_STATEMENT(1, self.NewLIST )
                    
                    self.data_base[ 'print' ] = []
                    self.got_errors, self.error = for_block_treatment.TREATMENT( self.data_base,
                                                    self.line ).FOR( main_string, self.value, self.name, True, self.listTransform )

                    if self.error is None:
                        if self.data_base[ 'print' ] is not None:
                            self.list_of_values = self.data_base[ 'print' ]
                            for i, value in enumerate( self.list_of_values ):
                                if len( self.value ) == 1 :
                                    for sub_value in value:
                                        if i < len( self.list_of_values) - 1:
                                            show_data.SHOW( sub_value, self.data_base, False ).SHOW( loop = True)
                                        else:
                                           show_data.SHOW( sub_value, self.data_base, False ).SHOW( loop = False) 
                                else:
                                    if i < len( self.list_of_values) - 1:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                                    else:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = False )

                                if self.got_errors:
                                    print( self.got_errors[ i ])
                                else: pass
                        else: pass
                    else: pass
                    self.data_base['print'] = []

                else: self.error = self.error

            else: pass

        else:
            if   self.master[ 'begin'  ] is True:
                self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList )
                self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                
                self.error = cmt_int.COMMENT_STATEMENT( None, self.data_base, self.line ).COMMENT( 1, self.NewLIST )
            elif self.master[ 'delete' ] is True: pass
            elif self.master[ 'global' ] is True: pass
            elif self.master[ 'print'  ]            is not None: pass
            elif self.master[ 'transformation' ]    is not None: pass
            elif self.master[ 'try' ]    is True:
                self.data_base[ 'print' ] = []
                self._, self.error = try_statement.EXTERNAL_TRY_STATEMENT(None,
                                                    self.data_base, self.line ).TRY_STATEMENT(tabulation = 1)

                if self.data_base[ 'print' ] is not None:
                    self.list_of_values = self.data_base[ 'print' ]
                    for i, value in enumerate( self.list_of_values ):
                        if i < len( self.list_of_values) - 1:
                            print_value.PRINT_PRINT( value ).PRINT_PRINT( key = False, loop = True )
                        else:
                            print_value.PRINT_PRINT( value ).PRINT_PRINT( key = False, loop = True )
                else:  pass
            else:
                if   self.data_base[ 'current_func' ]  is not None:
                    
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                    self.newLine                    = self.line
                    self.MainStringTransform        = main_string
                    self.listTransform              = self.NewLIST 
                    
                    self.error = def_interpreter.EXTERNAL_DEF_STATEMENT( None, self.data_base, self.line ).DEF( tabulation = 1, 
                                                                        loop_list = self.listTransform )
                    if self.error is None: pass
                    else: pass
                    
                elif self.data_base[ 'current_class' ] is not None:
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                    self.newLine                    = self.line
                    self.MainStringTransform        = main_string
                    self.listTransform              = self.NewLIST 
                    
                    self.error = class_interpreter.EXTERNAL_DEF_STATEMENT( None, self.data_base, self.line, self.master['class']).CLASSES(  tabulation = 1, 
                                                                        loop_list = self.listTransform )
                    if self.error is None: pass
                    else: pass
                     
                elif self.data_base[ 'importation' ]   is not None:
                    self.modules = self.data_base[ 'importation' ] 
                    self.dataS, self.info, self.error = module_load_treatment.TREATMENT( self.modules, self.data_base, 
                                                                    self.line ).MODULE_MAIN( main_string, baseFileName = baseFileName )
                    if self.error is None:
                        self.error = module_load_treatment.MODULES( self.data_base, self.line, self.dataS, self.info ).LOAD()
                        if self.error is None:
                            self.error = module_load_treatment.CLASSIFICATION( self.data_base, self.line ).CLASSIFICATION( self.data_base[ 'modulesImport' ], 
                                                                                    baseFileName = baseFileName, info = self.data_base[ 'importation' ])
                            #print(self.data_base['modulesImport']['mainFuncNames'], self.data_base['modulesImport']['fileNames'])
                            #print(self.data_base['modulesImport']['variables'])
                           
                        else: pass
                    else: pass
                    self.data_base[ 'importation' ] = None
                   
        return  self._return_, self.key_return, self.error

    def GLOBAL_ASSEMBLY_FILE_INTERPRETER(self, 
                                    main_string     : str, 
                                    interpreter     : bool  = False, 
                                    MainList        : list  = [], 
                                    baseFileName    : str   = '',
                                    locked          : bool  = True
                                    ):
        
        self._return_           = None
        self.key_return         = None
        self.error              = None
        self.active_function    = None
        self.all_data_vars      = list( self.master.keys() )
        self.structure          = [ 'begin', 'if', 'loop_for', 'loop_until', 'loop_while', 'try', 'unless', 'switch' ]

        for i , data in enumerate( self.all_data_vars ):
            if data != 'if_egal':
                if self.master[ data ] is None: pass
                else:
                    self.active_function = data
                    break
            else: pass

        if self.active_function == 'all_data':
            if   self.master[ 'function' ] is None      :
                self.error = ASSEMBLY( self.master, self.data_base, self.line).ASSEMBLY( main_string, interpreter )
            
            elif self.master[ 'function' ] == 'if'      :
    
                self._return_, self.error = end_else_elif.MAIN_IF( main_string, self.data_base,
                                                                   self.line ).BOCKS()
                if self.error is None:
                    self.data_base[ 'print' ]       = []
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                    self.newLine                    = self.line
                    
                    self.listTransform ,self.error  = if_inter.EXTERNAL_IF_STATEMENT( None, self.data_base,
                                                                         self.line ).IF_STATEMENT(1, self.NewLIST )
                else: pass
                
            elif self.master[ 'function' ] == 'for'     :
                self.value, self.name, self.operator, self.error = end_for_else.MAIN_FOR( self.master, self.data_base,
                                                                self.line ).BOCKS( main_string )
                
                if self.error is None:
                    self.data_base['variables']['vars'].append(self.name)
                    self.data_base['variables']['values'].append(self.value[-1])
                    
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                    self.newLine                    = self.line
                    
                    self.listTransform = for_interpreter.EXTERNAL_FOR_STATEMENT( None, self.data_base,
                                                                         self.line ).FOR_STATEMENT(1, self.NewLIST )
                else : pass
            
            else: pass 
            
        else:
            if   self.data_base[ 'current_func' ]  is not None:
                
                self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                self.newLine                    = self.line
                self.MainStringTransform        = main_string
                self.listTransform              = self.NewLIST 
                
                self.error = def_interpreter.EXTERNAL_DEF_STATEMENT( None, self.data_base, self.line ).DEF( tabulation = 1, 
                                                                    loop_list = self.listTransform )
                if self.error is None: pass
                else: pass
                
            elif self.data_base[ 'current_class' ] is not None:
                self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                self.newLine                    = self.line
                self.MainStringTransform        = main_string
                self.listTransform              = self.NewLIST 
                
                self.error = class_interpreter.EXTERNAL_DEF_STATEMENT( None, self.data_base, self.line, self.master['class']).CLASSES(  tabulation = 1, 
                                                                    loop_list = self.listTransform )
                if self.error is None: pass
                else: pass
                    
            elif self.data_base[ 'importation' ]   is not None:
                self.data_base[ 'loading' ]    = True
                self.modules = self.data_base[ 'importation' ] 
                self.dataS, self.info, self.error = module_load_treatment.TREATMENT( self.modules, self.data_base, 
                                                                                    self.line ).MODULE_MAIN( main_string )
                if self.error is None:
                    self.error = module_load_treatment.MODULES( self.data_base, self.line, self.dataS, self.info ).LOAD()
                    if self.error is None:
                        self.error = module_load_treatment.CLASSIFICATION( self.data_base, self.line ).CLASSIFICATION( self.data_base[ 'modulesImport' ], 
                                                                                info = self.data_base[ 'importation' ])
                    else: pass
                else: pass
                self.data_base[ 'importation' ] = None
                
        return  self._return_, self.key_return, self.error
    
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

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str, _char_ = 'an integer()' ):
        error = '{}is not {}{} {}type. {}line: {}{}'.format(self.white, self.blue, _char_, self.yellow,
                                                            self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors() +'{}<< {} >> '.format(self.magenta, string) + error

        return self.error+self.reset
    
    def ERROR2(self, func: str ):
        error = '{}returns no values. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors() +'{}{} '.format(self.cyan, func) + error

        return self.error+self.reset