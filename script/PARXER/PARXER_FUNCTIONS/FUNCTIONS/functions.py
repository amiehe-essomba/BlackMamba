from script.STDIN.WinSTDIN                              import stdin
from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._FOR_               import end_for_else
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_if, for_begin, for_statement, for_switch, for_unless,  for_try
from script.PARXER.INTERNAL_FUNCTION                    import get_list
from script.LEXER.FUNCTION                              import main
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS           import def_end
from script.PARXER.PARXER_FUNCTIONS._IF_                import if_statement
from script.LEXER.FUNCTION                              import print_value
from script.DATA_BASE                                   import data_base as db
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment as cmt
from script.PARXER                                      import module_load_treatment  as mlt
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import unless_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from src.functions                                      import error as er
from src.functions                                      import function, loading, set_openfile, updating_data
import  numpy as np
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

                self._return_,  self.error = function.FUNCTION( self.dictionary[ 'functions' ]  ,
                             self.data_base, self.line ).DOUBLE_INIT_FUNCTION( self.normal_expression, self.function_name )

                if self.error is None:
                    self._new_data_base_, self.error  = function.FUNCTION( [ self.function_info ], self.data_base,
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
                                    updating_data.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base, self._new_data_base_ )

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
                                            
                                        updating_data.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base, self._new_data_base_ )
                                    else:
                                        self.data_base[ 'no_printed_values' ].append( self.new_data_base[ 'sub_print' ] )
                                        updating_data.UPDATE_DATA_BASE(None, None, None).INITIALIZATION(self.new_data_base, self._new_data_base_)
                            else: pass
                        else:
                            self.empty_values = self.new_data_base[ 'empty_values' ]
                            self.error = er.ERRORS( self.line ).ERROR15( self.function_name, self.empty_values )
                            
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
                self._return_,  self.error =function.FUNCTION( self.dictionary[ 'functions' ]  ,
                             self.data_base, self.line ).DOUBLE_INIT_FUNCTION( self.normal_expression, self.function_name )

                if self.error is None:
                    self._new_data_base_, self.error  = function.FUNCTION( [ self.function_info ], self.data_base,
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
                                        
                                        updating_data.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,  self._new_data_base_ )

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
                                                        self.error = set_openfile.SET_OPEN_FILE( self.new_data_base[ 'open' ], self.data_base, self.line).SET_OPEN()
                                                        #self.data_base[ 'open' ] = self.new_data_base[ 'open' ]
                                                    else: pass
                                                else: 
                                                    if self.function_name == 'initialize': pass 
                                                    else: self.data_base[ 'no_printed_values' ].append( None )
                                                
                                            updating_data.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,  self._new_data_base_ )
                                        else:
                                            self.data_base[ 'no_printed_values' ].append( self.new_data_base[ 'sub_print' ] )
                
                                            updating_data.UPDATE_DATA_BASE(None, None, None).INITIALIZATION(self.new_data_base, self._new_data_base_)
                                else: pass
                            else:
                                self.empty_values = self.new_data_base[ 'empty_values' ]
                                self.error = er.ERRORS( self.line ).ERROR15( self.function_name, self.empty_values ) 
                        except KeyError: self.error = er.ERRORS( self.line ).ERROR13( self.function_name )
                    else: pass
                else: pass
            else: pass
       
        else: 
            self.mod = loading.LOAD(self.data_base['modulesImport']['func_names'], self.function_name).LOAD()
    
            if self.mod['key'] is True: 
                
                self.data_base[ 'assigment' ]   = self.function_name+'( )'
                self.function_info              = self.data_base['modulesImport']['functions'][self.mod['id1']][self.mod['id2']]
                self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                       self.line ).MAIN( def_key = 'indirect' )
                
                if self.error is None: 
                    self._return_,  self.error = function.FUNCTION( self.dictionary[ 'functions' ]  ,
                             self.data_base, self.line ).DOUBLE_INIT_FUNCTION( self.normal_expression, self.function_name ) 
                    if self.error is None:
                        self._new_data_base_, self.error  = function.FUNCTION( [ self.function_info ], self.data_base,
                                                    self.line).INIT_FUNCTION( self.normal_expression, self._return_ )

                        if self.error is None:
                            self.new_data_base              = self._new_data_base_[ 'data_base' ]
                            self.new_data_base              = FUNCTION_TREATMENT( self.master, self.data_base, self.line ).INIT_FUNCTION(initialize_data,
                                                                                                    self.new_data_base, self.function_name, lib = True)
                            loading.LOAD(self.data_base['modulesImport']['func_names'][self.mod['id1']], self.function_name).INITIALIZE(self.new_data_base, 
                                              self.data_base['modulesImport']['functions'][self.mod['id1']])
                            self.n = self.data_base['modulesImport']['fileNames'].index(_main_)
                            loading.LOAD(None, None).GLOBAL_VARS(self.new_data_base, self.data_base['modulesImport']['variables'], self.n)
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
                                            
                                            updating_data.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,  self._new_data_base_ )

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
                                                            self.error = set_openfile.SET_OPEN_FILE( self.new_data_base[ 'open' ], 
                                                                                       self.data_base, self.line).SET_OPEN()
                                                       
                                                        else: pass
                                                    else: 
                                                        if self.function_name == 'initialize': pass 
                                                        else: self.data_base[ 'no_printed_values' ].append( None )
                                                    
                                                updating_data.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,  self._new_data_base_ )
                                            else:
                                                self.data_base[ 'no_printed_values' ].append( self.new_data_base[ 'sub_print' ] )
                    
                                                updating_data.UPDATE_DATA_BASE(None, None, None).INITIALIZATION(self.new_data_base, self._new_data_base_)
                                    else: pass
                                else:
                                    self.empty_values = self.new_data_base[ 'empty_values' ]
                                    self.error = er.ERRORS( self.line ).ERROR15( self.function_name, self.empty_values ) 
                            except KeyError: self.error = er.ERRORS( self.line ).ERROR13( self.function_name )
                        else: pass 
                    else: pass
                else: pass
                
            else: self.error = er.ERRORS( self.line ).ERROR13( self.function_name )

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
            updating_data.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base, self._new_data_base_ )

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
                    
                updating_data.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base, self._new_data_base_ )
            else:
                self.data_base[ 'no_printed_values' ].append( self.new_data_base[ 'sub_print' ] )
                updating_data.UPDATE_DATA_BASE(None, None, None).INITIALIZATION(self.new_data_base, self._new_data_base_)
      
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
                                    self.error = er.ERRORS( self.line ).ERROR20( self.get_block[ : -1 ] )
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
                                                self.error = er.ERRORS( self.line ).ERROR22( self.db['func_names'][ 0 ] )
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
                                    self.error = er.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break

                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
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
                                    self.error =er. ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break

                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
                                    self.space += 1
                                    self.def_starage.append((self.normal_string, False))
                                else:
                                    self.error = er.ERRORS(self.line).ERROR10()
                                    break

                            else:
                                self.error = er.ERRORS(self.line).ERROR10()
                                break

                        else: break

            except KeyboardInterrupt:
                self.error = er.ERRORS(self.line).ERROR10()
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
                                    self.error = er.ERRORS( self.line ).ERROR20( self.get_block[ : -1 ] )
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
                                        self.error = er.ERRORS(self.line).ERROR10()
                                        break
                                
                                elif self.get_block == 'any'    :
                                    self.store_value.append( self.normal_string )
                                    self.space = 0
                                    self.def_starage.append( ( self.value, True ) )
                                
                                elif self.get_block == 'def:'   :
                                    self.val, self.error =  self.analyze.DELETE_SPACE( self.value[3:-1] )
                                    if self.error is None: 
                                        self.error = er.ERRORS( self.line ).ERROR23( self.val )
                                        break
                                    else: 
                                        self.error = er.ERRORS( self.line ).ERROR0( self.value )
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
                                    self.error = er.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break

                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
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
                                    self.error = er.ERRORS( self.line ).ERROR17( self.history[ -1 ] )
                                    break

                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
                                    self.space += 1
                                    self.def_starage.append((self.normal_string, False))
                                else:
                                    self.error = er.ERRORS(self.line).ERROR10()
                                    break

                            else:
                                self.error = er.ERRORS(self.line).ERROR10()
                                break

                        else: break

            except KeyboardInterrupt:
                self.error = er.ERRORS(self.line).ERROR10()
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
                                self.error = er.ERRORS( self.line ).ERROR10()
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
                                self.error = er.ERRORS(self.line).ERROR17( self.history[ -1 ] )
                                break

                        elif self.get_block == 'empty'  :
                            if self.space <= 2:
                                self.space += 1
                            else:
                                self.error = er.ERRORS( self.line ).ERROR10()
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
                                self.error = er.ERRORS( self.line ).ERROR10()
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
                                self.error = er.ERRORS(self.line).ERROR17( self.history[ -1 ] )
                                break

                        elif self.get_block == 'empty'  :
                            if self.space <= 2:
                                self.space += 1
                            else:
                                self.error = er.ERRORS( self.line ).ERROR10()
                                break

                    else: break
            else:
                self.if_line        += 1
                self.line           += 1
                self.next_line      = None

        return self.error







         

