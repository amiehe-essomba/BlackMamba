from script.PARXER                              import numerical_value
from script.STDIN.WinSTDIN                      import stdin
from script                                     import control_string
from script.PARXER.LEXER_CONFIGURE              import numeric_lexer
from script.PARXER.PARXER_FUNCTIONS._FOR_       import end_for_else
from script.LEXER.FUNCTION                      import function
from script.PARXER.PARXER_FUNCTIONS._FOR_       import for_if, for_begin, for_statement, for_switch, for_unless,  for_try
from script.PARXER.INTERNAL_FUNCTION            import get_list
from script.LEXER.FUNCTION                      import main
from script.PARXER.LEXER_CONFIGURE              import lexer_and_parxer
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS   import def_end
from script.PARXER.PARXER_FUNCTIONS._IF_        import if_statement
from script.LEXER.FUNCTION                      import print_value
from script.DATA_BASE                           import data_base as db
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS   import def_if
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment as cmt
from script.PARXER                                      import module_load_treatment  as mlt
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import unless_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement

try:  from CythonModules.Windows                        import fileError as fe 
except ImportError:  from CythonModules.Linux           import fileError as fe 
try:  from CythonModules.Linux                          import loop_for
except ImportError: from CythonModules.Windows          import loop_for


class FUNCTION_TREATMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int 
                ):
        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.library            = self.data_base[ 'LIB' ]

    def TREATMENT(self, 
                main_string         : str, 
                regular_expressions : dict, 
                initialize_data     : any = None, 
                _main_              : str = '' 
                ):
        
        self.error                  = None
        self.final_values           = None
        self.regular_expressions    = regular_expressions
        self.function_name          = self.regular_expressions[ 'names' ][ 0 ]
        self.expression             = 'def' + ' ' + self.regular_expressions[ 'expressions' ] + ' ' + ':'
        self.dictionary             = {
            'functions'             : [],
            'func_names'            : []
        }
        self.print_values           = False
        self.initialize_values      = None
        
        
        if   self.function_name in self.data_base[ 'func_names' ]   :
            
            self.data_base[ 'assigment' ] = self.function_name+'( )'
            self.function_location      = self.data_base[ 'func_names' ].index( self.function_name )
            self.function_info          = self.data_base[ 'functions' ][ self.function_location ]
            self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                        self.line ).MAIN( def_key = 'indirect' )

            if self.error is None:

                self._return_,  self.error = FUNCTION( self.dictionary[ 'functions' ]  ,
                             self.data_base, self.line ).DOUBLE_INIT_FUNCTION( self.normal_expression, self.function_name )

                if self.error is None:
                    self._new_data_base_, self.error  = FUNCTION( [ self.function_info ], self.data_base,
                                                    self.line).INIT_FUNCTION( self.normal_expression, self._return_ )

                    if self.error is None:
                        self.new_data_base              = self._new_data_base_[ 'data_base' ]
                        
                        self.new_data_base              = FUNCTION_TREATMENT( self.master, self.data_base, self.line ).INIT_FUNCTION( initialize_data,
                                                                                            self.new_data_base, self.function_name )
                        
                        self.new_data_base[ 'print' ]   = []
                        self.all_data_analyses  = self.data_base[ 'functions' ][ self.function_location ][ self.function_name ]
                        self.all_data_analyses  = self.all_data_analyses[ 'history_of_data' ]
                        
                        if self.new_data_base[ 'empty_values' ] is None:
                            self.error = EXTERNAL_DEF_LOOP_STATEMENT( None, self.new_data_base,
                                                            self.line ).DEF_STATEMENT( 1, self.all_data_analyses )
                            if self.error is None:
                                self.initialize_values      = self.new_data_base[ 'variables' ]
                                self.data_base[ 'irene' ]   = self.new_data_base[ 'irene' ]
                                self.data_base[ 'matrix' ]  = self.new_data_base[ 'matrix' ]
                                self.keyActivation          = False
                                
                                if self.new_data_base[ 'return' ] is not None:
                                    if len( self.new_data_base[ 'return' ] ) == 1:
                                        self.final_values = self.new_data_base[ 'return' ][ 0 ]
                                    else: self.final_values = tuple( self.new_data_base[ 'return' ] )

                                    if self.new_data_base[ 'print' ] is not None:
                                       
                                        self.print_values   = True
                                        self.list_of_values = self.new_data_base[ 'print' ]
                                        
                                        for i, value in enumerate( self.list_of_values ):
                                            print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )

                                        self.new_data_base[ 'print' ]   = []
                                    else: pass
                                    UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base, self._new_data_base_ )

                                else:
                                    if self.new_data_base[ 'sub_print' ] is None:
                                        if self.new_data_base[ 'transformation' ] is None:
                                            self.final_values   = self.new_data_base[ 'return' ]
                                        else:
                                            self.keyActivation  = True
                                            self.final_values   = self.new_data_base[ 'transformation' ]
                                            self.new_data_base[ 'transformation' ]  = None

                                        
                                        if self.new_data_base[ 'print' ] :
                                            self.print_values = True
                                            self.list_of_values = self.new_data_base[ 'print' ]

                                            for i, value in enumerate( self.list_of_values ):
                                                print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )

                                            self.new_data_base[ 'print' ]       = []
                                        else:  
                                            if self.keyActivation is True: pass
                                            else: 
                                                if self.function_name == 'initialize': pass 
                                                else: self.data_base[ 'no_printed_values' ].append( None )
                                            
                                        UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base, self._new_data_base_ )
                                    else:
                                        self.data_base[ 'no_printed_values' ].append( self.new_data_base[ 'sub_print' ] )
                                        UPDATE_DATA_BASE(None, None, None).INITIALIZATION(self.new_data_base, self._new_data_base_)
                            else: pass
                        else:
                            self.empty_values = self.new_data_base[ 'empty_values' ]
                            self.error = ERRORS( self.line ).ERROR15( self.function_name, self.empty_values )
                            
                    else: pass
                else: pass
            else: pass

        elif self.function_name in self.library[ 'func_names' ]     :
            
            self.data_base[ 'assigment' ] = self.function_name+'( )'
            self.function_location  = self.library[ 'func_names' ].index( self.function_name )
            self.function_info      = self.library[ 'functions' ][ self.function_location ]
            self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                       self.line ).MAIN( def_key = 'indirect' )

            if self.error is None:
                self._return_,  self.error = FUNCTION( self.dictionary[ 'functions' ]  ,
                             self.data_base, self.line ).DOUBLE_INIT_FUNCTION( self.normal_expression, self.function_name )

                if self.error is None:
                    self._new_data_base_, self.error  = FUNCTION( [ self.function_info ], self.data_base,
                                                    self.line).INIT_FUNCTION( self.normal_expression, self._return_ )

                    if self.error is None:
                        self.new_data_base              = self._new_data_base_[ 'data_base' ]
                        self.new_data_base              = FUNCTION_TREATMENT( self.master, self.data_base, self.line ).INIT_FUNCTION(initialize_data,
                                                                                                    self.new_data_base, self.function_name, lib = True)
                        
                        self.new_data_base[ 'print' ]   = []
                        try:
                            self.all_data_analyses  = self.library[ 'functions' ][ self.function_location ][ self.function_name ]
                            self.all_data_analyses  = self.all_data_analyses[ 'history_of_data' ]
                            self.keyActivation      = False
                            
                            if self.new_data_base[ 'empty_values' ] is None:
                               
                                self.error = EXTERNAL_DEF_LOOP_STATEMENT( None, self.new_data_base,
                                                                self.line).DEF_STATEMENT( 1, self.all_data_analyses )
                                if self.error is None:
                                    
                                    self.data_base['irene']     = self.new_data_base['irene']
                                    self.data_base['matrix']    = self.new_data_base['matrix']
                                    self.initialize_values      = self.new_data_base[ 'variables' ]
                                    
                                    if self.new_data_base[ 'return' ] is not None:
                                        if len( self.new_data_base[ 'return' ] ) == 1:
                                            self.final_values   = self.new_data_base[ 'return' ][ 0 ]
                                        else:
                                            self.final_values   = tuple( self.new_data_base[ 'return' ] )

                                        if self.new_data_base[ 'print' ] :
                                            #self.data_base[ 'no_printed_values' ].append( self.new_data_base[ 'print' ] )
                                            
                                            self.print_values = True
                                            self.list_of_values = self.new_data_base[ 'print' ]
                                            for i, value in enumerate( self.list_of_values ):
                                                print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )

                                            self.new_data_base['print'] = []
                                        else: pass
                                        
                                        UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,  self._new_data_base_ )

                                    else:
                                        if self.new_data_base[ 'sub_print' ] is None:
                                            if self.new_data_base[ 'transformation' ] is None:
                                                self.final_values   = self.new_data_base[ 'return' ]
                                            else:
                                                self.keyActivation  = True
                                                self.final_values   = self.new_data_base[ 'transformation' ]
                                                self.new_data_base[ 'transformation' ] = None
                                        
                                            if self.new_data_base[ 'print' ] :
                                                
                                                #self.data_base['no_printed_values'].append( self.new_data_base[ 'print' ] )
                                                self.print_values = True
                                                self.list_of_values = self.new_data_base[ 'print' ]

                                                for i, value in enumerate( self.list_of_values ):
                                                    print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )

                                                self.new_data_base[ 'print' ] = []
                                            else:     
                                                if self.keyActivation is True: 
                                                    if self.function_name == 'fopen': 
                                                        self.data_base[ 'no_printed_values' ].append( None )
                                                        self.error = SET_OPEN_FILE( self.new_data_base[ 'open' ], self.data_base, self.line).SET_OPEN()
                                                        #self.data_base[ 'open' ] = self.new_data_base[ 'open' ]
                                                    else: pass
                                                else: 
                                                    if self.function_name == 'initialize': pass 
                                                    else: self.data_base[ 'no_printed_values' ].append( None )
                                                
                                            UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,  self._new_data_base_ )
                                        else:
                                            self.data_base[ 'no_printed_values' ].append( self.new_data_base[ 'sub_print' ] )
                
                                            UPDATE_DATA_BASE(None, None, None).INITIALIZATION(self.new_data_base, self._new_data_base_)
                                else: pass
                            else:
                                self.empty_values = self.new_data_base[ 'empty_values' ]
                                self.error = ERRORS( self.line ).ERROR15( self.function_name, self.empty_values ) 
                        except KeyError: self.error = ERRORS( self.line ).ERROR13( self.function_name )
                    else: pass
                else: pass
            else: pass
       
        else: 
            self.mod = LOAD(self.data_base['modulesImport']['func_names'], self.function_name).LOAD()
    
            if self.mod['key'] is True: 
                
                self.data_base[ 'assigment' ]   = self.function_name+'( )'
                self.function_info              = self.data_base['modulesImport']['functions'][self.mod['id1']][self.mod['id2']]
                self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                       self.line ).MAIN( def_key = 'indirect' )
                
                if self.error is None: 
                    self._return_,  self.error = FUNCTION( self.dictionary[ 'functions' ]  ,
                             self.data_base, self.line ).DOUBLE_INIT_FUNCTION( self.normal_expression, self.function_name ) 
                    if self.error is None:
                        self._new_data_base_, self.error  = FUNCTION( [ self.function_info ], self.data_base,
                                                    self.line).INIT_FUNCTION( self.normal_expression, self._return_ )

                        if self.error is None:
                            self.new_data_base              = self._new_data_base_[ 'data_base' ]
                            self.new_data_base              = FUNCTION_TREATMENT( self.master, self.data_base, self.line ).INIT_FUNCTION(initialize_data,
                                                                                                    self.new_data_base, self.function_name, lib = True)
                            LOAD(self.data_base['modulesImport']['func_names'][self.mod['id1']], self.function_name).INITIALIZE(self.new_data_base, 
                                              self.data_base['modulesImport']['functions'][self.mod['id1']])
                            self.n = self.data_base['modulesImport']['fileNames'].index(_main_)
                            LOAD(None, None).GLOBAL_VARS(self.new_data_base, self.data_base['modulesImport']['variables'], self.n)
                            self.new_data_base[ 'print' ]   = []
                            
                            try:
                                self.all_data_analyses  = self.data_base['modulesImport']['functions'][self.mod['id1']][self.mod['id2']][ self.function_name ]
                                self.all_data_analyses  = self.all_data_analyses[ 'history_of_data' ]
                                self.keyActivation      = False
                                
                                if self.new_data_base[ 'empty_values' ] is None:
                                    self.error = EXTERNAL_DEF_LOOP_STATEMENT( None, self.new_data_base,
                                                                    self.line).DEF_STATEMENT( 1, self.all_data_analyses )
                                    if self.error is None:
                                        
                                        self.data_base['irene']     = self.new_data_base['irene']
                                        self.initialize_values      = self.new_data_base[ 'variables' ]
                                        if self.new_data_base[ 'return' ] is not None:
                                            if len( self.new_data_base[ 'return' ] ) == 1:
                                                self.final_values   = self.new_data_base[ 'return' ][ 0 ]
                                            else:
                                                self.final_values   = tuple( self.new_data_base[ 'return' ] )

                                            if self.new_data_base[ 'print' ] :
                                                
                                                self.print_values = True
                                                self.list_of_values = self.new_data_base[ 'print' ]
                                                for i, value in enumerate( self.list_of_values ):
                                                    print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )

                                                self.new_data_base['print'] = []
                                            else: pass
                                            
                                            UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,  self._new_data_base_ )

                                        else:
                                            if self.new_data_base[ 'sub_print' ] is None:
                                                if self.new_data_base[ 'transformation' ] is None:
                                                    self.final_values   = self.new_data_base[ 'return' ]
                                                else:
                                                    self.keyActivation  = True
                                                    self.final_values   = self.new_data_base[ 'transformation' ]
                                                    self.new_data_base[ 'transformation' ] = None
                                            
                                                if self.new_data_base[ 'print' ] :
                                                    
                                                    self.print_values = True
                                                    self.list_of_values = self.new_data_base[ 'print' ]

                                                    for i, value in enumerate( self.list_of_values ):
                                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )

                                                    self.new_data_base[ 'print' ] = []
                                                else:     
                                                    if self.keyActivation is True: 
                                                        if self.function_name == 'fopen': 
                                                            self.data_base[ 'no_printed_values' ].append( None )
                                                            self.error = SET_OPEN_FILE( self.new_data_base[ 'open' ], 
                                                                                       self.data_base, self.line).SET_OPEN()
                                                       
                                                        else: pass
                                                    else: 
                                                        if self.function_name == 'initialize': pass 
                                                        else: self.data_base[ 'no_printed_values' ].append( None )
                                                    
                                                UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,  self._new_data_base_ )
                                            else:
                                                self.data_base[ 'no_printed_values' ].append( self.new_data_base[ 'sub_print' ] )
                    
                                                UPDATE_DATA_BASE(None, None, None).INITIALIZATION(self.new_data_base, self._new_data_base_)
                                    else: pass
                                else:
                                    self.empty_values = self.new_data_base[ 'empty_values' ]
                                    self.error = ERRORS( self.line ).ERROR15( self.function_name, self.empty_values ) 
                            except KeyError: self.error = ERRORS( self.line ).ERROR13( self.function_name )
                        else: pass 
                    else: pass
                else: pass
                
            else: self.error = ERRORS( self.line ).ERROR13( self.function_name )

        return self.final_values, self.data_base[ 'no_printed_values' ], self.initialize_values, self.error

    def TOTAL_TREATMENT(self, 
                    value   : any, 
                    typ     : str = 'def' 
                    ):
        self.error      = None 
        self._result    = None 
        
        if typ == 'def':
            self.string     = self.master[ 'add_params' ]
            self._result, _, self.error = get_list.LIS_OPTIONS( [ self.master ], self.master, self.data_base, self.line ).ARGUMENT_LIST( value, 
                                                                                            self.string, function = True )
        elif typ == 'class':
            self.string     = self.master[ 'add_params' ][ -1 ]
            self._result, _, self.error = get_list.LIS_OPTIONS( [ self.master ], self.master, self.data_base, self.line ).ARGUMENT_LIST( value, 
                                                                                            self.string, function = True )
            
        return self._result, self.error

    def INIT_FUNCTION( self, 
                    initialize_data : any, 
                    new_data_base   : dict, 
                    funcName        : str   = '', 
                    lib             : bool  = False
                    ):
        
        new_data_base[ 'classes' ]          = self.data_base[ 'classes' ].copy()
        new_data_base[ 'class_names' ]      = self.data_base[ 'class_names' ].copy()
        new_data_base[ 'functions' ]        = self.data_base[ 'functions' ].copy()
        new_data_base[ 'func_names' ]       = self.data_base[ 'func_names' ].copy()
        new_data_base['modulesImport']      = self.data_base['modulesImport'].copy()
        
        if lib == False:    
            self.idd = self.data_base[ 'func_names' ].index( funcName )
            self.mainFunction = self.data_base[ 'functions' ][ self.idd ][ funcName ][ 'sub_functions' ]
            
            if not self.mainFunction: pass 
            else:
                for i, name in enumerate(self.mainFunction['func_names']) :
                    if name not in new_data_base[ 'func_names' ]:
                        new_data_base[ 'func_names' ].append( name )
                        new_data_base[ 'functions' ].append( self.mainFunction['functions'][ i ])
                    else:
                        self._idd_ = new_data_base[ 'func_names' ].index( name )
                        new_data_base[ 'functions' ][self._idd_ ] = self.mainFunction['functions'][ i ]
                
            if initialize_data is None: return new_data_base 
            else:
                self.variables          = self.new_data_base[ 'variables' ]
                self.init_vars          = initialize_data[ 'vars' ]
                self.init_values        = initialize_data[ 'values' ] 
                
                self.old_vars           = self.variables[ 'vars' ]
                self.old_values         = self.variables[ 'values' ] 
                
                if self.init_vars:
                    for i, name in enumerate( self.init_vars ):
                        if name not in self.old_vars:
                            self.old_vars.append( name )
                            self.old_values.append( self.init_values[ i ] ) 
                        else:
                            self.idd = self.old_vars.index( name )
                            self.init_values[ self.idd ] = self.init_values[ i ]
                
                else: pass 
                
                self.variables[ 'vars' ]            = self.old_vars
                self.variables[ 'values']           = self.old_values 
                
                new_data_base[ 'variales' ]         = self.variables 
            
                return new_data_base
        else: return new_data_base 
            
    def LIBRARY(self):
        pass
    
    def UPDATING(self, db: dict):
        
        self.new_data_base = db
        
        self.initialize_values      = self.new_data_base[ 'variables' ]
        self.data_base[ 'irene' ]   = self.new_data_base[ 'irene' ]
        self.keyActivation          = False
        
        if self.new_data_base[ 'return' ] is not None:
            if len( self.new_data_base[ 'return' ] ) == 1:
                self.final_values = self.new_data_base[ 'return' ][ 0 ]
            else: self.final_values = tuple( self.new_data_base[ 'return' ] )

            if self.new_data_base[ 'print' ] is not None:
                
                self.print_values   = True
                self.list_of_values = self.new_data_base[ 'print' ]
                
                for i, value in enumerate( self.list_of_values ):
                    print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )

                self.new_data_base[ 'print' ]   = []
            else: pass
            UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base, self._new_data_base_ )

        else:
            if self.new_data_base[ 'sub_print' ] is None:
                if self.new_data_base[ 'transformation' ] is None:
                    self.final_values   = self.new_data_base[ 'return' ]
                else:
                    self.keyActivation  = True
                    self.final_values   = self.new_data_base[ 'transformation' ]
                    self.new_data_base[ 'transformation' ]  = None

                
                if self.new_data_base[ 'print' ] :
                    self.print_values = True
                    self.list_of_values = self.new_data_base[ 'print' ]

                    for i, value in enumerate( self.list_of_values ):
                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )

                    self.new_data_base[ 'print' ]       = []
                else:  
                    if self.keyActivation is True: pass
                    else: self.data_base[ 'no_printed_values' ].append( None )
                    
                UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base, self._new_data_base_ )
            else:
                self.data_base[ 'no_printed_values' ].append( self.new_data_base[ 'sub_print' ] )
                UPDATE_DATA_BASE(None, None, None).INITIALIZATION(self.new_data_base, self._new_data_base_)
      
class FUNCTION:
    def __init__(self, 
                master      :list, 
                data_base   :dict, 
                line        :int
                ):
        self.master             = master[ 0 ]
        self.line               = line
        self.data_base          = data_base
        self.global_vars        = self.data_base[ 'global_vars' ]

    def INIT_FUNCTION(self, main_string: str, info_data: dict):
        self.error              = None
        ###########################################################################
        self.keys               = list( self.master.keys() )
        self.function_name      = self.keys[ 0 ]

        self.get_informations   = self.master[ self.function_name ]
        self.type_of_data       = self.get_informations[ 'type' ][ : ]
        self.arguments          = self.get_informations[ 'arguments' ][ : ]
        self.values             = self.get_informations[ 'value' ][ : ]
        self.int_values         = self.values[ : ]
        self.emty_values        = []

        ###########################################################################
        self.computed_values    = info_data[ 'values_computed' ]
        self.external_vars      = info_data[ 'vars' ]
        self.external_values    = info_data[ 'values' ]
        self.location           = info_data[ 'location' ]

        self.lenght_exernal     = len( self.computed_values )
        self.lenght_internal    = len( self.arguments )
        self.sub_length         = 0

        for value in self.values:
            if value is not None: self.sub_length += 1
            else: pass

        self.difference         = self.lenght_internal - self.sub_length

        ###########################################################################
        self.function_names, self.function_expr  = db.DATA_BASE().FUNCTIONS()
        self.def_data_base      =  db.DATA_BASE().STORAGE().copy()

        if self.arguments:
            if self.external_vars:
                self.check_arguments = []
                for args in self.external_vars:
                    if not  self.check_arguments:
                        self.check_arguments.append( args )
                    else:
                        if args not in self.check_arguments:
                            self.check_arguments.append( args )
                        else:
                            self.error = ERRORS( self.line ).ERROR16( self.function_name, args )
                            break

                if self.error is None:
                    if self.lenght_exernal <= self.lenght_internal:
                        for w, vars in enumerate( self.external_vars ):
                            if vars in self.arguments :
                                self.idd    = self.arguments.index( vars )
                                self.values[ self.idd ] = self.computed_values[ self.location[ w ] ]

                            else:
                                self.error  = ERRORS(self.line).ERROR11(self.function_name, vars)

                        if self.error is None:
                            if self.lenght_exernal == len( self.external_vars ): pass
                            else:
                                loc             = self.location[ : ]
                                self.location   = sorted( loc, reverse = True )
                                for i in self.location:
                                    del self.computed_values[ i ]

                                for value in self.computed_values:
                                    if None in self.values:
                                        self.index = self.values.index( None )
                                        self.values[ self.index ] = value
                                    else: pass

                            for i, value in enumerate( self.values ):
                                if value is None:
                                    self.emty_values.append( ( self.arguments[ i ], i ) )
                                else: pass

                            if self.emty_values:
                                self.error = ERRORS(self.line).ERROR15(self.function_name, self.emty_values )
                            else: pass
                        else: self.error = self.error

                    else:
                        self.error = ERRORS(self.line).ERROR12(self.function_name, self.lenght_internal)
                else: self.error = self.error

            else:
                if self.computed_values:
                    if self.lenght_internal == 1 :
                        if self.arguments[ 0 ] is None:
                            self.error = ERRORS(self.line).ERROR14( self.function_name )
                        else:
                            if self.lenght_exernal == 1:
                                for s, value in enumerate( self.computed_values ):
                                    self.values[ s ] = value
                            else:
                                self.error = ERRORS(self.line).ERROR12(self.function_name, self.lenght_internal)
                    else:
                        if self.lenght_internal >= self.lenght_exernal:
                            try:
                                for s, value in enumerate( self.computed_values ):
                                    self.values[ s ] = value

                                for i, value in enumerate( self.values ):
                                    if value is None:
                                        self.emty_values.append( ( self.arguments[ i ], i ) )
                                    else: pass
                                if self.emty_values:
                                    self.error = ERRORS(self.line).ERROR15(self.function_name, self.emty_values )
                                else : pass
                            except IndexError: pass

                        else:
                            self.error = ERRORS(self.line).ERROR12( self.function_name, self.lenght_internal )
                else:
                    if self.lenght_internal == 1:
                        if self.arguments[ 0 ] is None:
                            del self.values[ 0 ]
                            del self.arguments[ 0 ]

                        else:
                            if self.values[ 0 ] is None:
                                self.error = ERRORS(self.line).ERROR15(self.function_name, [(self.arguments[0],0) ])
                            else: pass
                    else:
                        for i, value in enumerate( self.values ):
                            if value is None:
                                self.emty_values.append( (self.arguments[ i ], i ) )
                            else:
                                pass

                        if self.emty_values:
                            self.error = ERRORS(self.line).ERROR15(self.function_name, self.emty_values )
                        else: pass

        else:
            if self.external_vars:
                self.error = ERRORS(self.line).ERROR11( self.function_name, self.external_vars[0] )
            elif self.computed_values:
                self.error = ERRORS(self.line).ERROR12(self.function_name, 0 )
            else: pass

        if self.error is None:
            self.list_types = ''
            self.func = bm.fg.rbg(0,255,0)+' in {}( ).'.format(self.function_name)+bm.init.reset
            if self.values:
                for i, value in enumerate( self.values ):
                    self.error = CHECK_TYPE_OF_DATA( self.type_of_data[ i ] ).CHECK_TYPE( self.line, self.arguments[ i ], self.function_name )
                    if self.error is None:
                        if type( value ) == type( str() ):
                            if value not in [ None, '@670532821@656188185@670532821@']:
                                self._values_, self.error = numeric_lexer.NUMERCAL_LEXER( value, self.data_base,
                                                                                        self.line).LEXER( value )
                                if self.error is None:

                                    self._type_         = CHECK_TYPE_OF_DATA( self._values_ ).DATA()
                                    
                                    if 'any' in self.type_of_data[ i ] :
                                        if len( self.type_of_data[ i ] ) == 1: self.values[ i ]    = self._values_ 
                                        else: 
                                            for x, _typ_ in enumerate( self.type_of_data[ i ] ):
                                                if _typ_ == 'any': pass 
                                                else:
                                                    self.str_type   = CHECK_TYPE_OF_DATA( _typ_ ).TYPE()
                                                    if x < len( self.type_of_data[ i ] ) - 1:
                                                        self.list_types += self.str_type + ', '
                                                    else:
                                                        self.list_types += 'or ' + self.str_type
                                            self.error = ERRORS( self.line ).ERROR18( self.list_types, self.func )
                                            break
                                    else:
                                        if self._type_ not in self.type_of_data[ i ]:
                                            for x, _typ_ in enumerate( self.type_of_data[ i ] ):
                                                self.str_type   = CHECK_TYPE_OF_DATA( _typ_ ).TYPE()
                                                if x < len( self.type_of_data[ i ] ) - 1:
                                                    self.list_types += self.str_type + ', or '
                                                else:
                                                    self.list_types += self.str_type
                                                    
                                            self.error = ERRORS( self.line ).ERROR3( value, self.list_types, self.func)
                                            break
                                        else: self.values[ i ] = self._values_ 
                                else: break
                            else: self.values[ i ] = '@670532821@656188185@670532821@'
                        else: pass
                    else: break
            else: pass

            if self.error is None:
                UPDATE_DATA_BASE( self.values, self.arguments, self.global_vars ).UPDATE( self.def_data_base )

            else: pass
        else: pass

        self._return_     = {
            'data_base'         : self.def_data_base,
            'vars'              : self.arguments,
            'values'            : self.int_values
        }

        return  self._return_, self.error

    def DOUBLE_INIT_FUNCTION(self, main_string: str, function_name: str):
        self.error              = None
        self.function_name      = function_name

        self.get_informations   = self.master[ self.function_name ]
        self.type_of_data       = self.get_informations[ 'type' ]
        self.arguments          = self.get_informations[ 'arguments' ]
        self.values             = self.get_informations[ 'value' ]
        self.new_list_of_data   = []
        self.location           = []

        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] is None:
                del self.arguments[ 0 ]
                del self.values[ 0 ]
            else: pass
        else: pass

        if self.values:
            self.decrement = 0
            for i, value in enumerate( self.values ):
                if value is not None:
                    if self.error is None:
                        self.new_list_of_data.append( value )
                        self.location.append( i )
                    else: break

                else:
                    self.new_list_of_data.append( self.arguments[ i - self.decrement ] )
                    self.values[ i ]    = self.arguments[ i - self.decrement ]
                    del self.arguments[ i - self.decrement ]
                    self.decrement += 1

        else: pass

        self._return_ = {
            'values_computed'   : self.new_list_of_data,
            'values'            : self.values,
            'vars'              : self.arguments,
            'location'          : self.location
        }

        return self._return_,  self.error

class EXTERNAL_DEF_STATEMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        self.master             = master
        self.line               = line
        self.data_base          = data_base

    def DEF( self, 
            tabulation  : int,  
            class_name  : str   = '' , 
            class_key   : bool  = False
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
        ke                      = bm.fg.rbg(255,255, 0)
        self.color              = bm.fg.cyan_L
        if class_key is False: pass 
        else: self.color        = bm.fg.rbg(0,255, 255)
        

        ##########################################################
        self.subFunc            = {
            'func_names'        : [],
            'functions'         : []
        }

        while self.end != 'end:' :
            self.if_line        += 1
            self.line           += 1 

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                        self.line ).STDIN({ '0': ke, '1': self.color }, self.tabulation )

                if self.error is None:
                    if self.active_tab is True:

                        self.get_block, self.value, self.error = def_end.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1, class_name, class_key,
                                                                                               self.data_base[ 'current_func' ] )
                        if self.error is None:
                            if class_key is False: pass 
                            else: 
                                if self.get_block not in [ 'empty', 'any' ]:
                                    self.error = ERRORS( self.line ).ERROR20( self.get_block[ : -1 ] )
                                    break
                                else: pass
                            if self.error is None:
                                if self.get_block   == 'begin:' :
                                    self.store_value.append(self.normal_string)
                                    self.def_starage.append( ( self.normal_string, True ) )
                                    self._values_, self.error = for_begin.COMMENT_STATEMENT( self.master, self.data_base,
                                                                                self.line  ).COMMENT( self.tabulation + 1, self.color )
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
                                    self._values_, self.error = for_if.INTERNAL_IF_STATEMENT( self.master,
                                            self.data_base, self.line ).IF_STATEMENT( self.value, self.tabulation + 1 )

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
                                        self.error = ERRORS(self.line).ERROR10()
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
                                        self.error = INTERNAL_DEF_STATEMENT( None, self.db, self.line ).DEF( self.tabulation+1, 
                                                                                                        class_key, class_key )
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
                                                self.error = ERRORS( self.line ).ERROR22( self.db['func_names'][ 0 ] )
                                                break
                                        else: break
                                    else: break
                            else:break
                        else: break

                    else:
                        self.get_block, self.value, self.error = end_for_else.EXTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )

                        if self.error is None:
                            if self.get_block   == 'end:'   :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.def_starage.append( ( self.normal_string, False ) )

                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break

                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
                                    self.space += 1
                                    self.def_starage.append( ( self.normal_string, False ) )
                                else:
                                    self.error = ERRORS( self.line ).ERROR10()
                                    break

                            else:
                                self.error = ERRORS( self.line ).ERROR10()
                                break

                        else: break

                else:
                    if self.tabulation == 1:
                        self.error = self.error
                        break
                    else:
                        self.get_block, self.value, self.error = end_for_else.EXTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.line).BLOCKS(  self.tabulation)

                        if self.error is None:
                            if self.get_block   == 'end:'   :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.def_starage.append( ( self.normal_string, False ) )
                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break

                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
                                    self.space += 1
                                    self.def_starage.append((self.normal_string, False))
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

        EXTERNAL_DEF_STATEMENT( self.master, self.data_base, self.line ).UPDATE_FUNCTION( self.def_starage, self.subFunc )

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
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.analyze            = control_string.STRING_ANALYSE( self.data_base, self.line )

    def DEF( self, 
            tabulation  : int,  
            class_name  : str   = '' , 
            class_key   : bool  = False
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
        ke                      = bm.fg.rbg(255,255, 0)
        self.color              = bm.fg.rbg(255,255, 100)
        if class_key is False: pass 
        else: self.color        = bm.fg.rbg(0,255, 255)
        

        ##########################################################

        while self.end != 'end:' :
            self.if_line        += 1
            self.line           += 1

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                        self.line ).STDIN({ '0': ke, '1': self.color }, self.tabulation )

                if self.error is None:
                    if self.active_tab is True:

                        self.get_block, self.value, self.error = def_end.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1, class_name, class_key,
                                                                                               self.data_base[ 'current_func' ] )
                        if self.error is None:
                            if class_key is False: pass 
                            else: 
                                if self.get_block not in [ 'empty', 'any' ]:
                                    self.error = ERRORS( self.line ).ERROR20( self.get_block[ : -1 ] )
                                    break
                                else: pass
                            if self.error is None:
                                if self.get_block   == 'begin:' :
                                    self.store_value.append(self.normal_string)
                                    self.def_starage.append( ( self.normal_string, True ) )
                                    self._values_, self.error = for_begin.COMMENT_STATEMENT( self.master, self.data_base, 
                                                                                            self.line  ).COMMENT( self.tabulation + 1, self.color )
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
                                    self._values_, self.error = for_if.EXTERNAL_IF_STATEMENT( self.master,
                                            self.data_base, self.line ).IF_STATEMENT( self.value, self.tabulation + 1 )

                                    if self.error is None:
                                        self.history.append( 'if' )
                                        self.space = 0
                                        self.def_starage.append( self._values_ )

                                    else: break
                                
                                elif self.get_block == 'unless:':
                                    self.store_value.append(self.normal_string)
                                    self.def_starage.append( ( self.normal_string, True ) )
                                    self._values_, self.error = for_unless.EXTERNAL_UNLESS_STATEMENT( self.master,
                                                    self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1 )

                                    if self.error is None:
                                        self.history.append( 'unless' )
                                        self.space = 0
                                        self.def_starage.append( self._values_ )

                                    else: break     
                                
                                elif self.get_block == 'try:'   :
                                    self.store_value.append(self.normal_string)
                                    self.def_starage.append( ( self.normal_string, True ) )
                                 
                                    self._values_, self.error = for_try.EXTERNAL_TRY_STATEMENT( self.master,
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
                                        self.error = ERRORS(self.line).ERROR10()
                                        break
                                
                                elif self.get_block == 'any'    :
                                    self.store_value.append( self.normal_string )
                                    self.space = 0
                                    self.def_starage.append( ( self.value, True ) )
                                
                                elif self.get_block == 'def:'   :
                                    self.val, self.error =  self.analyze.DELETE_SPACE( self.value[3:-1] )
                                    if self.error is None: 
                                        self.error = ERRORS( self.line ).ERROR23( self.val )
                                        break
                                    else: 
                                        self.error = ERRORS( self.line ).ERROR0( self.value )
                                        break
                            else:break
                        else: break

                    else:
                        self.get_block, self.value, self.error = end_for_else.EXTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )

                        if self.error is None:
                            if self.get_block   == 'end:'   :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.def_starage.append( ( self.normal_string, False ) )

                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break

                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
                                    self.space += 1
                                    self.def_starage.append( ( self.normal_string, False ) )
                                else:
                                    self.error = ERRORS( self.line ).ERROR10()
                                    break

                            else:
                                self.error = ERRORS( self.line ).ERROR10()
                                break

                        else: break

                else:
                    if self.tabulation == 1:
                        self.error = self.error
                        break
                    else:
                        self.get_block, self.value, self.error = end_for_else.EXTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.line).BLOCKS(  self.tabulation)

                        if self.error is None:
                            if self.get_block   == 'end:'   :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.def_starage.append( ( self.normal_string, False ) )
                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break

                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
                                    self.space += 1
                                    self.def_starage.append((self.normal_string, False))
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

        EXTERNAL_DEF_STATEMENT( self.master, self.data_base, self.line ).UPDATE_FUNCTION( self.def_starage, {} )

        return self.error

class EXTERNAL_DEF_LOOP_STATEMENT:
    def __init__(self, 
                master      :any, 
                data_base   :dict, 
                line        :int
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.lex_par                = lexer_and_parxer 

    def DEF_STATEMENT(self, 
                    tabulation  : int   = 1, 
                    def_list    : list  = None, 
                    class_name  : str   = '', 
                    class_key   : bool  = False,
                    _type_      : str   = 'def'
                    ):
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.if_line                = 0

        ############################################################################

        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'def' ]
        self.color                  = bm.fg.blue_L
        self.def_list               = def_list
        self.next_line              = None
        self.subFunctionNames       = []

        ############################################################################
        self.keyPass                = False
        ############################################################################

        for j, _string_ in enumerate( self.def_list ):

            if j != self.next_line:
                self.if_line                         = 1
                self.line                           += 1 
                self.normal_string, self.active_tab  = _string_
                self.string                          = self.normal_string
                
                if self.active_tab is True:
                    self.get_block, self.value, self.error = def_end.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation + 1 )
                    
                    if self.error is None:
                        if   self.get_block == 'any'     :
                            self.space = 0
                            self.store_value.append( self.normal_string )
                            self._value_  = self.value[ self.tabulation : ]

                            if self.data_base['pass'] is None:
                                self.error = self.lex_par.LEXER_AND_PARXER( self.value[self.tabulation :], self.data_base,
                                                                self.line ).ANALYZE( _id_ = self.tabulation+1, _type_ = _type_ )
                                if self.error is None: pass
                                else: break
                            else: self.keyPass = True

                        elif self.get_block == 'if:'     :
                            self.next_line  = j + 1
                            self.error = if_statement.INTERNAL_IF_LOOP_STATEMENT ( self.master,
                                        self.data_base, self.line ).IF_STATEMENT( self.value, self.tabulation + 1,
                                                                                self.def_list[ j + 1], _type_ = _type_ )
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'if' )
                                self.space = 0

                            else: break
                        
                        elif self.get_block == 'switch:' :
                            self.next_line  = j + 1
                            self.error = switch_statement.SWITCH_LOOP_STATEMENT( self.master , self.data_base,
                                            self.line ).SWITCH( self.value, self.tabulation + 1,
                                                                                self.def_list[ j + 1], _type_ = _type_ )
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'switch' )
                                self.space = 0

                            else: break
                            
                        elif self.get_block == 'unless:' :
                            self.next_line  = j + 1
                            self.error = unless_statement.INTERNAL_UNLESS_LOOP_STATEMENT( self.master , self.data_base,
                                            self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                                self.def_list[ j + 1], _type_ = _type_ )
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'unless' )
                                self.space = 0

                            else: break
                        
                        elif self.get_block == 'for:'    :
                            self.next_line  = j + 1
                            self.before     = end_for_else.CHECK_VALUES(self.data_base).BEFORE()
                            
                            self.var_name       = self.value[ 'variable' ]
                            self.for_values_init= self.value[ 'value' ]
                            self.variables      = self.data_base['variables']['vars'].copy()
                            self._values_       = self.data_base['variables']['values'].copy()
                            
                            if self.var_name in self.variables:
                                self.idd = self.variables.index( self.var_name )
                                self._values_[ self.idd ] = self.for_values_init[ 0 ]
                                self.data_base[ 'variables' ][ 'values' ] = self._values_

                            else:
                                self.variables.append( self.var_name )
                                self._values_.append( self.for_values_init[ 0 ] )
                                self.data_base[ 'variables' ][ 'values' ]   = self._values_
                                self.data_base[ 'variables' ][ 'vars' ]     = self.variables
            
                            self.error  = loop_for.LOOP( self.data_base, self.line ).LOOP( list(self.for_values_init),
                                                                        self.var_name, True, self.def_list[ j + 1] )
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'for' )
                                self.space = 0

                            else: break

                        elif self.get_block == 'try:'    :
                            self.next_line = j + 1
                            
                            self._finally_key_, self.error = try_statement.INTERNAL_TRY_FOR_STATEMENT( self.master,
                                                        self.data_base, self.line ).TRY_STATEMENT(self.tabulation + 1,
                                                            self.def_list[ self.next_line],  keyPass = self.keyPass, _type_ =  _type_)
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'try' )
                                self.space = 0
                            else: break
                            
                        elif self.get_block == 'begin:'  :
                            self.next_line  = j + 1
                            self.error = cmt.COMMENT_LOOP_STATEMENT( self.master, self.data_base, self.line ).COMMENT( self.tabulation + 1, 
                                                                                                            self.def_list[ j + 1]) 
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'begin' )
                                self.space = 0
                            else:
                                self.after = end_for_else.CHECK_VALUES( self.data_base ).AFTER()
                                self.error = end_for_else.CHECK_VALUES( self.data_base ).UPDATE( self.before, self.after, self.error )
                                break

                        elif self.get_block == 'def:'    :
                            self.db = db.DATA_BASE().STORAGE().copy()
                            self.next_line  = j + 1
                            self.lexer, _, self.error = main.MAIN(self.value, self.db, self.line).MAIN( _type_ = 'def' )

                            if self.error is None:
                                self._vars_     = self.db['variables']['vars'].copy()
                                self._values_   = self.db['variables']['values'].copy()
                                self.func_names = self.data_base['func_names'].copy()
                                self.functions  = self.data_base['functions'].copy()
                                self.class_names= self.data_base['class_names'].copy()
                                self.classes    = self.data_base['classes'].copy()
                                
                                if not self._vars_: pass 
                                else:
                                    for i, _var_ in self._vars_:
                                        if not self.data_base['variables']['vars']:
                                            self.data_base['variables']['vars'].append( _var_ )
                                            self.data_base['variables']['vars'].append( self._values_[ i ] )
                                        else:
                                            if _var_ in self.data_base['variables']['vars']: 
                                                self.id = self.data_base['variables']['vars'].index( _var_ )
                                                self.data_base['variables']['vars'][self.id] = self._values_[ i ]
                                            else:
                                                self.data_base['variables']['vars'].append( _var_ )
                                                self.data_base['variables']['vars'].append( self._values_[ i ] )
                                            
                                self.all_data_analyses = self.def_list[ j + 1]
                                
                                self.error = INTERNAL_DEF_LOOP_STATEMENT( None, self.data_base,
                                                                self.line ).DEF_STATEMENT( self.tabulation+1, self.all_data_analyses,
                                                                                          class_name, class_key, _type_ = _type_)
                                if self.error is None: 
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'def' )
                                    self.space  = 0
                                    self.name   = self.db['current_func'] 
                                    self.idd    = self.data_base['func_names'].index( self.name )
                                    self.subFunctionNames.append( self.name )
                                    
                                    #self.globalDB['subFunctionNames'] = self.subFunctionNames
                                    
                                    del self.data_base['func_names'][ self.idd ]
                                    del self.data_base['functions'][ self.idd ]
                                   
                                    self.data_base['class_names']   = self.class_names.copy()
                                    self.data_base['classes']       = self.classes.copy()
                                    self.data_base['functions']     = self.functions.copy()
                                    self.data_base['func_names']    = self.func_names.copy()
                                    mlt.INIT(self.db).INIT()
                                    
                                else: break
                            else: break
                            
                        elif self.get_block == 'empty'   :
                            if self.space <= 2: self.space += 1
                            else:
                                self.error = ERRORS( self.line ).ERROR10()
                                break

                    else: break

                else:
                    self.get_block, self.value, self.error = def_end.EXTERNAL_BLOCKS( self.string,
                             self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )

                    if self.error is None:
                        if self.get_block   == 'end:'   :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                break
                            else:
                                self.error = ERRORS(self.line).ERROR17( self.history[ -1 ] )
                                break

                        elif self.get_block == 'empty'  :
                            if self.space <= 2:
                                self.space += 1
                            else:
                                self.error = ERRORS( self.line ).ERROR10()
                                break
                    else: break
            else:
                self.if_line        += 1
                self.line           += 1
                self.next_line      = None

        return self.error

class INTERNAL_DEF_LOOP_STATEMENT:
    def __init__(self, 
                master      :any, 
                data_base   :dict, 
                line        :int
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.lex_par                = lexer_and_parxer

    def DEF_STATEMENT(self, 
                    tabulation  : int   = 1, 
                    def_list    : list  = None, 
                    class_name  : str   = '', 
                    class_key   : bool  = False,
                    _type_      : str   = 'def'
                    ):
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.if_line                = 0

        ############################################################################

        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'def' ]
        self.color                  = bm.fg.blue_L
        self.def_list               = def_list
        self.next_line              = None

        ############################################################################
        self.keyPass                = False
        ############################################################################

        for j, _string_ in enumerate( self.def_list ):

            if j != self.next_line:
                self.if_line                         = 1
                self.line                           += 1
                self.normal_string, self.active_tab  = _string_
                self.string                          = self.normal_string

                if self.active_tab is True:
                    self.get_block, self.value, self.error = end_for_else.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation + 1 )
                    
                    if self.error is None:
                        if self.get_block   == 'any'     :
                            self.store_value.append( self.normal_string )
                            self.space = 0
                            if self.data_base['pass'] is None:
                                self.error = self.lex_par.LEXER_AND_PARXER( self.value, self.data_base,
                                                                self.line ).ANALYZE( _id_ = 1, _type_ = _type_ )
                                if self.error is None: pass
                                else: break
                            else: self.keyPass = True

                        elif self.get_block == 'if:'     :
                            self.next_line  = j + 1
                            self.error = if_statement.INTERNAL_IF_LOOP_STATEMENT ( self.master,
                                        self.data_base, self.line ).IF_STATEMENT( self.value, self.tabulation + 1,
                                                                                self.def_list[ j + 1], _type_ = _type_ )
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'if' )
                                self.space = 0

                            else: break

                        elif self.get_block == 'switch:' :
                            self.next_line  = j + 1
                            self.error = switch_statement.SWITCH_LOOP_STATEMENT( self.master , self.data_base,
                                            self.line ).SWITCH( self.value, self.tabulation + 1,
                                                                                self.def_list[ j + 1], _type_ = _type_ )
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'switch' )
                                self.space = 0

                            else: break
                            
                        elif self.get_block == 'unless:' :
                            self.next_line  = j + 1
                            self.error = unless_statement.EXTERNAL_UNLESS_LOOP_STATEMENT( self.master , self.data_base,
                                            self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                                self.def_list[ j + 1], _type_ = _type_ )
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'unless' )
                                self.space = 0

                            else: break

                        elif self.get_block == 'for:'    :
                            self.next_line  = j + 1
                            self.before     = end_for_else.CHECK_VALUES(self.data_base).BEFORE()
                            
                            self.var_name       = self.value[ 'variable' ]
                            self.for_values_init= self.value[ 'value' ]
                            self.variables      = self.data_base['variables']['vars'].copy()
                            self._values_       = self.data_base['variables']['values'].copy()
                            
                            if self.var_name in self.variables:
                                self.idd = self.variables.index( self.var_name )
                                self._values_[ self.idd ] = self.for_values_init[ 0 ]
                                self.data_base[ 'variables' ][ 'values' ] = self._values_

                            else:
                                self.variables.append( self.var_name )
                                self._values_.append( self.for_values_init[ 0 ] )
                                self.data_base[ 'variables' ][ 'values' ]   = self._values_
                                self.data_base[ 'variables' ][ 'vars' ]     = self.variables
            
                            self.error  = loop_for.LOOP( self.data_base, self.line ).LOOP( list(self.for_values_init),
                                                                        self.var_name, True, self.def_list[ j + 1] )
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'for' )
                                self.space = 0

                            else: break

                        elif self.get_block == 'try:'    :
                            self.next_line = j + 1
                            
                            self._finally_key_, self.error = try_statement.EXTERNAL_TRY_FOR_STATEMENT( self.master,
                                                        self.data_base, self.line ).TRY_STATEMENT(self.tabulation + 1,
                                                            self.def_list[ self.next_line],  keyPass = self.keyPass, _type_ =  _type_)
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'try' )
                                self.space = 0
                            else: break
                        
                        elif self.get_block == 'begin:'  :
                            self.next_line  = j + 1
                            self.error = cmt.COMMENT_LOOP_STATEMENT( self.master, self.data_base, self.line ).COMMENT( self.tabulation + 1, 
                                                                                                            self.def_list[ j + 1]) 
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'begin' )
                                self.space = 0

                            else: break

                        elif self.get_block == 'empty'   :
                            if self.space <= 2: self.space += 1
                            else:
                                self.error = ERRORS( self.line ).ERROR10()
                                break
                    else: break
                else:
                    self.get_block, self.value, self.error = def_end.EXTERNAL_BLOCKS( self.string,
                             self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )

                    if self.error is None:
                        if self.get_block   == 'end:'   :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                break
                            else:
                                self.error = ERRORS(self.line).ERROR17( self.history[ -1 ] )
                                break

                        elif self.get_block == 'empty'  :
                            if self.space <= 2:
                                self.space += 1
                            else:
                                self.error = ERRORS( self.line ).ERROR10()
                                break

                    else: break
            else:
                self.if_line        += 1
                self.line           += 1
                self.next_line      = None

        return self.error

class UPDATE_DATA_BASE:
    def __init__(self, 
                values      : any, 
                variables   : any, 
                global_vars : dict
                ):
        self.values             = values
        self.variables          = variables
        self.global_vars        = global_vars
        self.num_parxer         = numerical_value

    def UPDATE(self, data_base:dict):
        self.name_without_values = []

        if self.variables:
            for i, vars in enumerate( self.variables ):
                if self.values[ i ] != '@670532821@656188185@670532821@':
                    data_base[ 'variables' ][ 'vars' ].append( vars )
                    data_base[ 'variables' ][ 'values'].append( self.values[ i ] )
                else: self.name_without_values.append( (vars, i) )
        else: pass

        self.global_variables   = self.global_vars[ 'vars' ].copy()
        self.global_values      = self.global_vars[ 'values' ].copy()

        if self.global_values:
            for i , value in enumerate( self.global_values ):
                if value not in [ '@670532821@656188@656188185@' ]:
                    data_base[ 'variables'] [ 'vars' ].append( self.global_variables[ i ] )
                    data_base[ 'variables' ][ 'values' ].append( value )
                else: pass
        else: pass

        if self.name_without_values: data_base[ 'empty_values' ] = self.name_without_values
        else: pass

        data_base[ 'total_vars' ] = self.variables

    def INITIALIZATION( self, data_base:dict, info:dict ):
        self.values                             = info[ 'values' ]
        self.arguments                          = info[ 'vars' ]

        data_base[ 'variables' ][ 'vars' ]      = self.arguments
        data_base[ 'variables' ][ 'values' ]    = self.values
        data_base[ 'empty_values' ]             = None
        data_base[ 'sub_print' ]                = []

class CHECK_TYPE_OF_DATA:
    def __init__(self, value : any ):
        self.value          = value

    def DATA(self):
        self._return_                           = ''
        self.type                               = type( self.value )

        if  self.type  == type( int() )         :       self._return_ = 'int'
        elif self.type == type( float() )       :       self._return_ = 'float'
        elif self.type == type( bool() )        :       self._return_ = 'bool'
        elif self.type == type( complex() )     :       self._return_ = 'cplx'
        elif self.type == type( dict() )        :       self._return_ = 'dict'
        elif self.type == type( list() )        :       self._return_ = 'list'
        elif self.type == type( tuple() )       :       self._return_ = 'tuple'
        elif self.type == type( str() )         :       self._return_ = 'string'
        elif self.type == type( range( 1 ) )    :       self._return_ = 'range'
        elif self.type == type( None )          :       self._return_ = 'none'
        return self._return_

    def TYPE(self):
        self._return_               = ''
        
        if   self.value == 'int'    :           self._return_ = '{}an integer(){}'.format(bm.fg.red_L, bm.init.reset)
        elif self.value == 'float'  :           self._return_ = '{}a float(){}'.format(bm.fg.rbg(0,255,0), bm.init.reset)
        elif self.value == 'bool'   :           self._return_ = '{}a boolean(){}'.format(bm.fg.cyan_L, bm.init.reset)
        elif self.value == 'cplx'   :           self._return_ = '{}a complex(){}'.format(bm.fg.blue, bm.init.reset)
        elif self.value == 'list'   :           self._return_ = '{}a list(){}'.format(bm.fg.rbg(255,255,0), bm.init.reset)
        elif self.value == 'tuple'  :           self._return_ = '{}a tuple(){}'.format(bm.fg.blue_L, bm.init.reset)
        elif self.value == 'dict'   :           self._return_ = '{}a dictionary(){}'.format(bm.fg.magenta_M, bm.init.reset)
        elif self.value == 'string' :           self._return_ = '{}a string(){}'.format(bm.fg.cyan, bm.init.reset)
        elif self.value == 'range'  :           self._return_ = '{}a range(){}'.format(bm.fg.green_L, bm.init.reset)
        elif self.value == 'none'   :           self._return_ = '{}a none(){}'.format(bm.fg.rbg(252, 127, 0 ), bm.init.reset)


        return self._return_ 
    
    def CHECK_TYPE( self , line: int, name: str, func_name: str):
        self.lists      = []
        self.error      = None
        
        if self.value:
            for value in self.value:
                if not self.lists: self.lists.append( value )
                else:
                    if value not in self.lists: self.lists.append( value )
                    else:
                        func        = bm.fg.rbg(0,255,0)+' in {}( )'.format( func_name )+bm.init.reset 
                        self.error  = ERRORS( line ).ERROR19( name,  value, func )
                        break
        else: pass
                
        return self.error 

class SET_OPEN_FILE:
    def __init__(self,
                master      : dict, 
                DataBase    : dict, 
                line        : int
                ):
        self.DataBase       = DataBase 
        self.master         = master 
        self.line           = line 
        
    def SET_OPEN(self):
        self.name           = self.master['name'][0]
        self.file           = self.master['file'][0]
        self.action         = self.master['action'][0]
        self.status         = self.master['status'][0]
        self.encoding       = self.master['encoding'][0]
        self.nonCloseKey    = self.master['nonCloseKey'][0]
        self.error          = None
        
        if not self.DataBase['open']['name']:
            self.DataBase['open']['name'].append( self.name )
            self.DataBase['open']['file'].append( self.file )
            self.DataBase['open']['action'].append( self.action )
            self.DataBase['open']['status'].append( self.status )
            self.DataBase['open']['encoding'].append( self.encoding )
            self.DataBase['open']['nonCloseKey'].append( self.nonCloseKey )
        else:
            if self.name in self.DataBase['open']['nonCloseKey']: self.error = ERRORS( self.line ).ERROR21( self.name )
            else:
                self.DataBase['open']['name'].append( self.name )
                self.DataBase['open']['file'].append( self.file )
                self.DataBase['open']['action'].append( self.action )
                self.DataBase['open']['status'].append( self.status )
                self.DataBase['open']['encoding'].append( self.encoding )
                self.DataBase['open']['nonCloseKey'].append( self.name )
        
        return self.error

class LOAD:
    def __init__(self, 
                moduleLoadNames : list, 
                funcName        : str
                ):
        self.moduleLoadNames        = moduleLoadNames 
        self.funcName               = funcName
        
    def LOAD(self):
        self.key        = False 
        self.id1        = 0
        self.id2        = 0
        
        for i, mod in enumerate(self.moduleLoadNames):
            if self.key is False: pass 
            else: break 
            
            if mod: 
                for j, sub_mod in enumerate(mod):
                    if sub_mod == self.funcName:
                        self.key = True
                        self.id1 = i
                        self.id2 = j
                        break 
                    else: pass
            else: pass
        
        return {'key' : self.key, 'id1' : self.id1, 'id2' : self.id2}

    def INITIALIZE(self, 
                new_data_base   : dict, 
                functions       : list
                ):
        
        for i, name in enumerate(self.moduleLoadNames):
            if name != self.funcName:
                if name in new_data_base['func_names']:
                    self.index = new_data_base['func_names'].index(name)
                    new_data_base['functions'][self.index] = functions[i]
                else:
                    new_data_base['functions'].append(functions[i]) 
                    new_data_base['func_names'].append(name) 
            else: pass
       
    def GLOBAL_VARS(self, 
                    db  : dict, 
                    var : dict, 
                    n   : int, 
                    typ : str = 'def'
                    ):
        
        self.vars, self.val = var['vars'][ n ], var['values'][n]

        if typ == 'def':
            if self.vars:
                for i, name in enumerate(self.vars) :
                    if name in db['variables']['vars']: pass 
                    else:
                        db['variables']['vars'].append( name )
                        db['variables']['values'].append(self.val[i])
            else: pass
        else:
            if self.vars:
                for i, name in enumerate(self.vars) :
                    if name in db['global_vars']['vars']: pass 
                    else:
                        db['global_vars']['vars'].append( name )
                        db['global_vars']['values'].append(self.val[i])
            else: pass
         
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}due to {}<< . >> .{}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white,self.cyan, string) + error

        return self.error+self.reset

    def ERROR2(self, string: str):
        error = '{}was not found. line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors()+'{}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR3(self, string: str, _char_ = 'an integer()', func = '' ):
        error = '{}is not {}{} {}type. {}line: {}{}'.format(self.white, self.blue, _char_, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error+self.reset

    def ERROR4(self, string: str, _char_ = 'an integer'):
        error = '{}to  {}{}() {}type. {}line: {}{}'.format(self.white, self.blue, _char_, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}impossible to convert {}<< {} >> '.format(self.white,self.cyan, string) + error

        return self.error+self.reset

    def ERROR5(self, string: str, key: str):
        error = '{}was not found in {}<< {} >>. {}line: {}{}'.format(self.white, self.red, string, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'KeyError' ).Errors()+'{}<< {} >> '.format(self.cyan, key) + error

        return self.error+self.reset

    def ERROR6(self, value):
        error = '{}a tuple(), {}or a string(), {}type. {}line: {}{}'.format(self.blue, self.cyan, self.yellow, self.white, self.yeloow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> {}is not {}a list(), '.format(self.cyan, value, self.white, self.yellow) + error
        return self.error+self.reset

    def ERROR7(self, op, ob1, ob2):
        error = '{}<< {}{} >>, {} and {}<< {}{} >>. {}type. {}line: {}{}'.format(self.white, ob1, self.white, 
                                                self.white, self.white, ob2, self.whie, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {}{}{} >> {}not supported between '.format(self.cyan, self.yellow,
                                                                                                             op, self.cyan, self.white) + error
        return self.error+self.reset

    def ERROR8(self, value):
        error = '{}<< EMPTY >>. {}line: {}{}'.format( self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'SyntaxError' ).Errors()+'{}<< {} >> {}is '.format(self.cyan, value, self.white) + error
        return self.error+self.reset

    def ERROR9(self, string: str = 'float' ):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'OverFlowError' ).Errors()+'infinity {}{} {}number. '.format(self.magenta, string, self.white) + error
        return self.error+self.reset

    def ERROR10(self):
        self.error =  fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                                        self.white, self.yellow, self.line )
        return self.error+self.reset

    def ERROR11(self, string: str, key: str):
        error = '{}has not {}<< {} >> {}as argument. {}line: {}{}'.format(self.white, self.red, key, self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'KeyError' ).Errors()+'{}<< {}( ) >> '.format(self.cyan, string ) + error
        return self.error+self.reset

    def ERROR12(self, string: str, pos1: int):
        char = ''
        if pos1 > 1:
            char = 'arguments'
        else:
            char = 'argument'

        error = '{}takes {}<< {} >> {}{}. {}line: {}{}'.format(self.white, self.red, pos1, self.yellow, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}<< {}( ) >> '.format(self.cyan, string ) + error
        return self.error+self.reset

    def ERROR13(self, string:str):
        error = '{}was not found. {}line: {}{}'.format(self.green,  self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'NameError' ).Errors()+'{}function name {}ERROR. {}<< {} >> '.format(self.white, self.yellow, self.cyan, string) + error

        return self.error+self.reset

    def ERROR14(self, string: str):
        error = '{}takes {}no arguments. {}line: {}{}'.format(self.white, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}<< {}( ) >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR15(self, string: str, value: list):
        self.list = []
        self.len = len( value )
        if self.len <= 1:
            self._string_ = 'argument'
        else:
            self._string_ = 'arguments'

        for _value_ in value:
            self.list.append( _value_[ 0 ] )

        error = '{}missing {}<< {} >> {}required {}: {}{}. {}line: {}{}'.format(self.green, self.red, self.len, self.white, self._string_, self.blue,
                                                                            self.list,  self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}in {}<< {}( ) >>, '.format(self.white, self.cyan, string) + error
        return self.error+self.reset 

    def ERROR16(self, string: str,key: str):
        error = '{}duplicated keyword argument {}<< {} >>. {}line: {}{}'.format(self.white, self.red, key, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}<< {}( ) >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR17(self, string):
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format(self.green, self.white, self.cyan, string, self.white,
                                                                                            self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. '.format( self.white ) + error
        return self.error+self.reset
    
    def ERROR18(self, string: str, func: str = ''):
        error = '{}with {}{}. {}line: {}{}'.format(self.white, self.cyan, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors()+'{}could not associate {}any() {}type '.format( self.white, self.yellow, 
                                                                                                              self.white ) + error + func
        return self.error+self.reset


    def ERROR19(self, name: str, key: str, func : str = ''):
        error = '{}duplicated {}<< {} >> {}type {}for the argument {}{}. {}line: {}{}'.format(self.white, self.red, key, self.green, self.white, self.cyan, name,
                                                                                          self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ error + func

        return self.error+self.reset
    
    def ERROR20(self, func: str = '' ):
        error = '{}{} {}cannot be defined in {}intialize( ) {}function. {}line: {}{}'.format(self.red, func, self.white, self.red, self.green,
                                                                                             self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ error 

        return self.error+self.reset
    
    def ERROR21(self, name: str):
        error = '{}before {}new opening. {}line: {}{}'.format(self.white, self.cyan, self.white, self.yellow, self.line)        
        self.error = fe.FileErrors( 'FileError' ).Errors() + '{}close {}{} '.format(self.white, self.red, name) + error

        return self.error+self.reset
    
    def ERROR22( self, string ):
        error = '{}already exits. {}line: {}{}'.format(self.yellow, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('NameError').Errors() + '{}the function name {}{} '.format(self.white, self.red, string,) + error
        return self.error + self.reset
    
    def ERROR23( self, string ):
        error = '{}cannot be {}a function. {}line: {}{}'.format(self.white, self.yellow, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}The subfunction {}{} '.format(self.white,  self.red, string) + error
        return self.error + self.reset
