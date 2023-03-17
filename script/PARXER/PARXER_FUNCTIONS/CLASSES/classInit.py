import pandas as pd
import numpy as np
from script.LEXER.FUNCTION                          import main
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS       import functions as func
from src.classes                                    import error as er
from src.classes                                    import loading, readfile, check_char, run_func, inheritance
from src.classes.Chars                              import Char
from src.classes.Lists                              import Lists
from src.classes.Range                              import Range
from src.classes.Cplx                               import cplx 
from src.classes.Cplx                               import Float 
from src.classes.frame                              import frame
from src.classes.Tuples                             import Tuples
from src.classes.Unions                             import union   
from src.classes.matrix                             import matrix_2D as m2D  
from src.classes.matrix                             import arguments as argm
from src.functions                                  import loading as load         
from src.functions                                  import function            
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS       import externalLoading as extL      
from script.PARXER.PARXER_FUNCTIONS.CLASSES.NESTED  import nested_vars as n_v
from script.PARXER.PARXER_FUNCTIONS.CLASSES.NESTED  import nested_func_load as n_f_l
    
class CLASS_TREATMENT:
    def __init__(self,
                master      : dict,
                DataBase    : dict, 
                line        : int 
                ) :
        self.master         = master
        self.DataBase       = DataBase 
        self.line           = line 
        self.classes        = self.DataBase[ 'classes' ] 
        self.class_names    = self.DataBase[ 'class_names' ]
         
    def TREATMENT( self, 
                main_names  : str   = '', 
                loading     : bool  = False, 
                idd1        : any   = None, 
                idd2        : any   = None, 
                length      : int   = 3, 
                tabulation  : int   = 2 
                ):
        self.error                  = None 
        self.final_values           = None
        self.initialize_values      = None
        self.value_from_db          = None
        self.normal_expr            = ''

        self.main_name      = self.master[ 'names' ][ 0 ]
        self.name           = self.master[ 'names' ][ 1 ] 
        self.main_expr      = self.master[ 'expressions' ][ 0 ] 
        self.expr           = self.master[ 'expressions' ][ 1 ] 
        self.historyOfFunctions = []
        self.DataBase[ 'assigment' ]           = self.name+'( )'
        self.key                               = False
    
        for i, _str_ in enumerate( self.master['expressions'] ):
            if i < len(self.master[ 'expressions'])-1:
                self.normal_expr += _str_+'.'
            else: self.normal_expr += _str_
        self.normal_expr = main_names + self.normal_expr 
                
        if loading is True: self.key = True
        else: 
            if self.main_name in self.class_names: self.key = True 
            else: pass
        
        if len( self.master[ 'names' ]) <= 3:
            if self.key is True: #self.main_name in self.class_names or loading is True
                try:
                    self.main_body = None
                    
                    if loading is False:
                        self.index              = self.class_names.index( self.main_name )
                        self.my_class           = self.classes[ self.index ]
                        self.main_body          = self.my_class[ 0 ][ 0 ]
                    else:
                        if   length == 3:
                            self.my_class           = self.DataBase[ 'modulesImport' ][ 'modulesLoadC' ][idd1]['classes'][idd2]
                            self.main_body          = self.my_class[ 0 ][ 0 ]
                            
                            for x, name in enumerate(self.DataBase['modulesImport'][ 'modulesLoadC' ][idd1]['class_names']):
                                if name not in self.DataBase['class_names']:
                                    self.DataBase['class_names'].append(name)
                                    self.DataBase['classes'].append(self.DataBase['modulesImport'][ 'modulesLoadC' ][idd1]['classes'][x])
                                else:
                                    self.id = self.DataBase['class_names'].index(name)
                                    self.DataBase['classes'][self.id] =  self.DataBase['modulesImport'][ 'modulesLoadC' ][idd1]['classes']
                                    
                        elif length == 2:
                            self.my_class           = self.DataBase['modulesImport']['classes'][idd1][idd2]
                            self.main_body          = self.my_class[ 0 ][ 0 ]
                            
                            for x, name in enumerate(self.DataBase['modulesImport']['class_names'][idd1]):
                                if name not in self.DataBase['class_names']:
                                    self.DataBase['class_names'].append(name)
                                    self.DataBase['classes'].append(self.DataBase['modulesImport']['classes'][idd1][x])
                                else:
                                    self.id = self.DataBase['class_names'].index(name)
                                    self.DataBase['classes'][self.id] =  self.DataBase['modulesImport']['classes'][idd1][x]
                    
                    if type(self.main_body) == type(tuple()):
                        self.main_body = self.main_body[0]
                     
                    self.function_names     = self.main_body[ 'function_names' ]
                    self.inheritanceClass   = self.main_body[ 'class_inheritance' ]
                    
                    #print(self.function_names, self.inheritanceClass,self.DataBase['class_names'])
                    if self.main_body[ 'init_function' ] is None: 
                        
                        self._variables_        = None
                        self.key                = False
                        self._function_names_   = None 
                        self._functions_        = None
                        
                        if self.main_expr != self.main_name:
                            self._ = check_char.CHECK(self.main_expr, self.main_name, self.DataBase, self.line ).CHECK()
                            if self._ is True: pass 
                            else: self.error = er.ERRORS( self.line ).ERROR14( self.main_name, 'class' )
                        else: pass 
                        
                        if self.error is None:
                            if self.inheritanceClass is None: pass 
                            else: 
                                self.key = True
                                self._function_names_, self._functions_, self._variables_, self.error = inheritance.INHERITANCE( self.DataBase, self.line ,
                                                                                    self.inheritanceClass[ 0 ] ).CLASSES( self.normal_expr )
                            
                            if self.error is None:
                                if self.expr != self.name:
                                    if self._functions_:
                                        if len( self._functions_) == len( self._function_names_ ) : pass 
                                        else: self._function_names_ = self._function_names_[ 1 : ]
                                        
                                        for i in range( len( self._functions_) ):
                                            if self._function_names_[ i ] in self.function_names: pass 
                                            else:
                                                self.function_names.append( self._function_names_[ i ])
                                                self.main_body[ 'functions' ].append( self._functions_[ i ] )
                                    else: pass
                                    if self.name in self.function_names:
                                        if self.name != 'initialize':
                                            self.idd_func           = self.function_names.index( self.name )
                                            self.my_function        = self.main_body[ 'functions' ][ self.idd_func]# - 1 ]
                                            
                                            self.dictionary         = {
                                            'functions'             : [],
                                            'func_names'            : []
                                            }
                                          
                                            self.expression              = 'def '+self.expr+ ':'
                                            self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                                                    self.line ).MAIN( def_key = 'indirect' )
                                        
                                            if self.error is None: 
                                                self._return_, self.error = function.FUNCTION(  self.dictionary[ 'functions' ] , self.DataBase, 
                                                                                        self.line ).DOUBLE_INIT_FUNCTION( self.normal_expr, self.name )
                                                if self.error is None:
                                                    self._new_data_base_, self.error = function.FUNCTION( self.my_function[ 1 ], self.DataBase,
                                                                    self.line).INIT_FUNCTION( self.normal_expr, self._return_ )
                                                     
                                                    if self.error is None: 
                                                        self.new_data_base           = self._new_data_base_[ 'data_base' ]
                                                        self._types_                 = self._new_data_base_[ 'type' ]
                                                        
                                                        if self.key is True:
                                                            if self._variables_:
                                                                if self._variables_[ 'vars' ]:
                                                                    for i in range( len(self._variables_[ 'vars' ])):
                                                                        if self._variables_[ 'vars' ][ i ] in self.new_data_base[ 'variables' ][ 'vars' ]: pass 
                                                                        else:
                                                                            self.new_data_base[ 'variables' ][ 'vars' ].append( self._variables_[ 'vars' ][ i ] )
                                                                            self.new_data_base[ 'variables' ][ 'values' ].append( self._variables_[ 'values' ][ i ] )
                                                                else: pass
                                                            else: pass
                                                        else: pass
                                                         
                                                        self.all_data_analyses       = self.my_function[ 1 ][ 0 ]
                                                        self.all_data_analyses       = self.all_data_analyses[ self.name  ][ 'history_of_data' ]
                                                        self.old_DataBase = self.DataBase.copy()
                                                         
                                                        if self.DataBase['modulesImport']['modules']:
                                                            self.original_module = self.DataBase['modulesImport']['modules'][ 0 ]
                                                            extL.UPDATING(self.DataBase, self.DataBase).UPDATING(self.original_module)
                                                        else: pass
                                                        
                                                        #self.original_module = self.DataBase['modulesImport']['modules'][ 0 ]
                                                        #extL.UPDATING(self.DataBase, self.DataBase).UPDATING(self.original_module)
                                                        
                                                        #print(self.DataBase['modulesImport']['moduleLoading'])
                                                        #print(self.DataBase['modulesImport'][ 'moduleLoading' ]['names'])
                                                        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                                                        #print(self.new_data_base['modulesImport']['moduleLoading'])
                                                        #print(self.new_data_base['func_names'], self.DataBase['func_names']  )
                                                        
                                                        self.final_values, self.value_from_db, self.initialize_values, self.error = run_func.RUN_FUNCTION( self.DataBase, self.line,
                                                                self.new_data_base, self._new_data_base_).RUN( self.all_data_analyses, self.name ,
                                                                                                        tabulation = tabulation, _type_ = self._types_ )
                                                        self.DataBase = self.old_DataBase.copy()
                                                    else: pass 
                                                else: pass 
                                            else: pass
                                        else:self.error = er.ERRORS( self.line ).ERROR13( self.main_name, self.name )
                                    else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, self.name )
                                else: 
                                    if self.key is False: self.error = er.ERRORS( self.line ).ERROR21( self.main_name, self.name )
                                    else: 
                                        self._vars_     = []
                                        self._values_   = []
                                                
                                        _, _, self._variables_, self.error = inheritance.INHERITANCE( self.DataBase, self.line ,
                                                                                            self.inheritanceClass[ 0 ] ).CLASSES( self.normal_expr )
                                        if self.error is None:
                                            if self._variables_:
                                                if self._variables_[ 'vars' ]: 
                                                    for i in range( len( self._variables_[ 'vars' ]) ):
                                                        if self._variables_[ 'vars' ][ i ] in self._vars_: pass 
                                                        else:
                                                            self._vars_.append( self._variables_[ 'vars' ][ i ] )
                                                            self._values_.append( self._variables_[ 'values' ][ i ] )
                                                else: pass  
                                            else: pass
                                            
                                            if self._vars_ :
                                                
                                                if self.name in self._vars_ :
                                                    self.idd = self._vars_.index( self.name )   
                                                    self.final_values = self._values_[ self.idd ]
                                                    self.DataBase['no_printed_values'] = []
                                                    self._values_   = []
                                                    self._vars      = []
                                                else: self.error = er.ERRORS( self.line ).ERROR21( self.main_name, self.name )
                                            else: self.error = er.ERRORS( self.line ).ERROR21( self.main_name, self.name )
                                        else: pass
                            else: pass
                        else: pass          
                    else:
                    
                        self.dictionary         = {
                        'functions'             : [],
                        'func_names'            : []
                        }
                        self.main_initialize        = self.main_body[ 'init_function' ]
                        self.function_init          = self.main_initialize[ 'function' ][ 1 ][ 0 ]
                        self.init_arguments         = self.function_init[ 'initialize' ][ 'arguments' ]
                        self.all_data_analyses_init = self.function_init[ 'initialize' ][ 'history_of_data' ]
                        
                        if self.main_expr != self.main_name:
                            self.int_expression     = 'def initialize' + self.main_expr[ len( self.main_name) : ] + ':'
                            self.lexer, self.normal_expression, self.error = main.MAIN( self.int_expression, self.dictionary,
                                                                            self.line ).MAIN( def_key = 'indirect' )
                        else:
                            self.int_expression     = 'def initialize( ):'
                            self.lexer, self.normal_expression, self.error = main.MAIN( self.int_expression, self.dictionary,
                                                                            self.line ).MAIN( def_key = 'indirect' )
                        
                        if self.error is None:
                            self._return_, self.error = function.FUNCTION(  self.dictionary[ 'functions' ] , self.DataBase, 
                                                                self.line ).DOUBLE_INIT_FUNCTION( self.normal_expr, 'initialize' )
                        
                            if self.error is None:
                                self._new_data_base_, self.error = function.FUNCTION( [ self.function_init ], self.DataBase,
                                                        self.line).INIT_FUNCTION( self.normal_expr, self._return_ )
                                if self.error is None:
                                    self.new_data_base1          = self._new_data_base_[ 'data_base' ]
                                    
                                    if self.new_data_base1[ 'empty_values' ] is None: pass 
                                    else: 
                                        self.empty_values   = self.new_data_base1[ 'empty_values' ]
                                        self.error          = er.ERRORS( self.line ).ERROR15( 'initialize' , self.empty_values )
                                        
                                    self._, self.value, self.variables, self.error = run_func.RUN_FUNCTION( self.DataBase, self.line,
                                                                    self.new_data_base1, self._new_data_base_).RUN(self.all_data_analyses_init, 
                                                                                    'initialize', tabulation = tabulation, _type_ = None )
                                    
                                    if self.error is None:
                                        if self.expr != self.name: 
                                            self._variables_    = None
                                            self.key            = False
                                            if self.inheritanceClass is None: pass 
                                            else: 
                                                self.key = True
                                                self._function_names_, self._functions_, self._variables_, self.error = inheritance.INHERITANCE( self.DataBase, self.line ,
                                                                                                    self.inheritanceClass[ 0 ] ).CLASSES( self.normal_expr )
                                                if self.error is None:
                                                    if self._functions_:
                                                        if len( self._function_names_ ) == len( self._functions_ ): pass 
                                                        else: self._function_names_ = self._function_names_[1 : ]
                                                        
                                                        for i in range( len( self._functions_ ) ):
                                                            if self._function_names_[ i ] in self.function_names: pass 
                                                            else:
                                                                self.function_names.append( self._function_names_[ i ])
                                                                self.main_body[ 'functions' ].append( self._functions_[ i ] )
                                                    else: pass
                                                else: pass
                                            
                                            if self.error is None:
                                                if self.name in self.function_names:
                                                    if self.name != 'initialize':
                                                        self.idd_func           = self.function_names.index( self.name )
                                                        self.my_function        = self.main_body[ 'functions' ][ self.idd_func - 1 ]
                                                        self.dictionary         = {
                                                        'functions'             : [],
                                                        'func_names'            : []
                                                        }
                                                        
                        
                                                        self.expression              = 'def '+self.expr+ ':'
                                                        self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                                                self.line ).MAIN( def_key = 'indirect' )
                                                        if self.error is None:
                                                            self._return_, self.error = function.FUNCTION(  self.dictionary[ 'functions' ] , self.DataBase, 
                                                                                    self.line ).DOUBLE_INIT_FUNCTION( self.normal_expr, self.name )
                                                            if self.error is None:
                                                                self._new_data_base_, self.error = function.FUNCTION( self.my_function[ 1 ] , self.DataBase,
                                                                                self.line).INIT_FUNCTION( self.normal_expr, self._return_ )
                                                                
                                                                if self.error is None:
                                                                    self.new_data_base           = self._new_data_base_[ 'data_base' ]
                                                                    self._types_                 = self._new_data_base_[ 'type' ]
                                                                    self.vars                    = self.variables[ 'vars' ]
                                                                    self.values                  = self.variables[ 'values' ]
                                                                    
                                                                    if self.vars:
                                                                        for i, var in enumerate( self.vars ):
                                                                            if var in self.new_data_base[ 'variables' ][ 'vars' ]:
                                                                                self.new_data_base[ 'variables' ][ 'values' ][ i ] = self.values[ i ] 
                                                                            else:
                                                                                self.new_data_base[ 'variables' ][ 'vars' ].append( var )
                                                                                self.new_data_base[ 'variables' ][ 'values' ].append( self.values[ i ] )
                                                                                
                                                                        self.main_body[ 'init_function' ]['variables']  = self.variables
                                                                        self.main_body[ 'init_function' ]['active']     = True
                                                                        
                                                                    else: pass     
                                                                    
                                                                    if self.key is True:
                                                                        if self._variables_:
                                                                            if self._variables_[ 'vars' ]:
                                                                                for i in range( len(self._variables_[ 'vars' ])):
                                                                                    if self._variables_[ 'vars' ][ i ] in self.new_data_base[ 'variables' ][ 'vars' ]: pass 
                                                                                    else:
                                                                                        self.new_data_base[ 'variables' ][ 'vars' ].append( self._variables_[ 'vars' ][ i ] )
                                                                                        self.new_data_base[ 'variables' ][ 'values' ].append( self._variables_[ 'values' ][ i ] )
                                                                            else: pass 
                                                                        else: pass
                                                                    else: pass
                                                                    
                                                                    self.all_data_analyses       = self.my_function[ 1 ][ 0 ]
                                                                    self.all_data_analyses       = self.all_data_analyses[ self.name ][ 'history_of_data' ]

                                                                    #self.original_module = self.DataBase['modulesImport']['modules'][ 0 ]
                                                                    #extL.UPDATING(self.DataBase, self.DataBase).UPDATING(self.original_module)
                                                                    if self.DataBase['modulesImport']['modules']:
                                                                        self.original_module = self.DataBase['modulesImport']['modules'][ 0 ]
                                                                        extL.UPDATING(self.DataBase, self.DataBase).UPDATING(self.original_module)
                                                                    else: pass
                                                                    
                                                                    self.final_values, self.value_from_db, self.initialize_values, self.error = run_func.RUN_FUNCTION( self.DataBase, self.line,
                                                                                self.new_data_base, self._new_data_base_).RUN( self.all_data_analyses, self.name,
                                                                                                                              tabulation = tabulation, _type_ = self._types_ )
                                                                    
                                                                else: pass 
                                                            else: pass
                                                        else: pass
                                                    else:self.error = er.ERRORS( self.line ).ERROR13( self.main_name, self.name )
                                                else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, self.name )
                                            else: pass
                                        else:
                                            self.vars       = self.variables[ 'vars' ]
                                            self.values     = self.variables[ 'values' ]
                                            self._vars_     = []
                                            self._values_   = []
                                            
                                            if self.vars : 
                                                for i in range( len( self.vars) ):
                                                    self._vars_.append( self.vars[ i ] )
                                                    self._values_.append( self.values[ i ] )
                                            else: pass
                                            
                                            if self.inheritanceClass is None: pass 
                                            else: 
                                                _, _, self._variables_, self.error = inheritance.INHERITANCE( self.DataBase, self.line ,
                                                                                                self.inheritanceClass[ 0 ] ).CLASSES( self.normal_expr )
                                                if self.error is None:
                                                    if self._variables_:
                                                        if self._variables_[ 'vars' ]: 
                                                            for i in range( len( self._variables_[ 'vars' ]) ):
                                                                if self._variables_[ 'vars' ][ i ] in self._vars_: pass 
                                                                else:
                                                                    self._vars_.append( self._variables_[ 'vars' ][ i ] )
                                                                    self._values_.append( self._variables_[ 'values' ][ i ] )
                                                        else: pass  
                                                    else: pass
                                                else: pass 
                                            
                                            if self.error is None:
                                                if self._vars_ :
                                                    if self.expr in self._vars_ :
                                                        self.idd = self._vars_.index( self.name )   
                                                        self.final_values = self._values_[ self.idd ]
                                                        self.DataBase['no_printed_values'] = []
                                                        self._values_   = []
                                                        self._vars      = []
                                                    else: self.error = er.ERRORS( self.line ).ERROR21( self.main_name, self.name )
                                                else: self.error = er.ERRORS( self.line ).ERROR21( self.main_name, self.name )
                                            else: pass
                                    else: pass
                                else: pass
                            else: pass
                        else: pass   
                except KeyError: self.error = er.ERRORS( self.line).ERROR13( self.main_name )
                    
            else: 
                self.strFunctions       = [ 'upper', 'lower', 'capitalize', 'empty', 'enumerate', 'split', 'join', 'format', 'index', 'rstrip', 'lstrip',
                                            'count', 'endwith', 'startwith', 'replace', 'size']
                self.dictFunctions      = [ 'empty', 'get', 'clear', 'copy', 'remove', 'init', 'sorted', 'frame'] 
                self.cplxFunctions      = [ 'img', 'real', 'norm', 'conj' ] 
                self.floatFunctions      = [ 'round' ] 
                self.rangeFunctions      = [ 'size', 'enumerate', 'choice', 'to_array', 'sum', 'std', 'mean', 'var' ] 
                self.tupleFunctions     = [ 'empty', 'init', 'enumerate', 'size', 'choice', 'index', 'count'] 
                self.listFunctions      = [ 'empty', 'clear', 'copy', 'remove', 'init', 'index', 'count', 'sorted', 'add', 'insert', 'random', 'enumerate',
                                            'size', 'round', 'rand', 'choice', 'to_array' ]
                self.fileios            = ['readline', 'readlines', 'read', 'writeline', 'writelines', 'close', 'write' ]
                self.ndarrays           = [ 'sum', 'mean', 'std', 'pstd', 'var', 'pvar', 'sqrt', 'square', 'sorted', 'cov', 'linearR', 'min', 'max', 'ndim', 
                                           'quantile', 'median', 'sum_square', 'grouped', 'cms', 'round', 'iquantile', 'Q1', 'Q3', 'kurtosis', 'dtype', 
                                           'size', 'copy', 'owner', 'choice']
                self.table              = ['set_id', 'select', 'keys']  #['show', 'set_id', 'select', 'keys']
                
                if self.main_name in self.DataBase[ 'variables' ][ 'vars' ]: 
                    
                    self.idd    = self.DataBase[ 'variables' ][ 'vars' ].index( self.main_name )
                    self.value  = self.DataBase[ 'variables' ][ 'values' ][ self.idd ]
                
                    if   type( self.value ) == type( str() )        :
                        if self.main_name == self.main_expr: 
                            if self.name != self.expr:
                                if self.name in self.strFunctions:
                                    self.historyOfFunctions.append( self.name )
                                    self.expression         = 'def '+self.expr+ ':'
                                    self.dictionary         = {
                                    'functions'             : [],
                                    'func_names'            : []
                                    }
                                    self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                                self.line ).MAIN( def_key = 'indirect' )
                                    if self.error is None: 
                                        self.final_values, self.error = Char.STRING( self.DataBase, self.line, self.value,
                                                                            self.name, self.dictionary[ 'functions' ]).STR( self.main_name, self.normal_expr)
                                    else: pass    
                                else: self.error = er.ERRORS( self.line ).ERROR22( self.name )
                            else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )                       
                    elif type( self.value ) == type( dict() )       :
                        if self.main_name == self.main_expr: 
                            if self.name != self.expr:
                                if self.name in self.dictFunctions:
                                    self.historyOfFunctions.append( self.name )
                                    self.expression         = 'def '+self.expr+ ':'
                                    self.dictionary         = {
                                    'functions'             : [],
                                    'func_names'            : []
                                    }
                                    self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                                self.line ).MAIN( def_key = 'indirect' )
                                    if self.error is None: 
                                        self.final_values, self.error = union.DICTIONARY( self.DataBase, self.line, self.value,
                                                                            self.name, self.dictionary[ 'functions' ]).DICT( self.main_name, self.normal_expr )
                                    else: pass    
                                else: self.error = er.ERRORS( self.line ).ERROR22( self.name, 'dictionary( )' )
                            else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )                   
                    elif type( self.value ) == type( list() )       :
                        if self.main_name == self.main_expr: 
                            if self.name != self.expr:
                                if self.name in self.listFunctions:
                                    self.historyOfFunctions.append( self.name )
                                    self.expression         = 'def '+self.expr+ ':'
                                    self.dictionary         = {
                                    'functions'             : [],
                                    'func_names'            : []
                                    }
                                    self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                                self.line ).MAIN( def_key = 'indirect' )
                                    if self.error is None: 
                                        self.final_values, self.error = Lists.LIST( self.DataBase, self.line, self.value,
                                                                self.name, self.dictionary[ 'functions' ]).LIST( self.main_name, self.normal_expr )
                                    else: pass    
                                else: self.error =er. ERRORS( self.line ).ERROR22( self.name, 'list( )' )
                            else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )                    
                    elif type( self.value ) == type( range(2) )     :
                        if self.main_name == self.main_expr: 
                            if self.name != self.expr:
                                if self.name in self.rangeFunctions:
                                    self.historyOfFunctions.append( self.name )
                                    self.expression         = 'def '+self.expr+ ':'
                                    self.dictionary         = {
                                    'functions'             : [],
                                    'func_names'            : []
                                    }
                                    self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                                self.line ).MAIN( def_key = 'indirect' )
                                    if self.error is None: 
                                        self.final_values, self.error = Range.RANGE( self.DataBase, self.line, self.value,
                                                                self.name, self.dictionary[ 'functions' ]).RANGE( self.main_name, self.normal_expr )
                                    else: pass    
                                else: self.error =er. ERRORS( self.line ).ERROR22( self.name, 'range( )' )
                            else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' ) 
                    elif type( self.value ) == type( tuple() )      :
                        if self.main_name == self.main_expr: 
                            if self.name != self.expr:
                                if self.name in self.tupleFunctions:
                                    self.historyOfFunctions.append( self.name )
                                    self.expression         = 'def '+self.expr+ ':'
                                    self.dictionary         = {
                                    'functions'             : [],
                                    'func_names'            : []
                                    }
                                    self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                                self.line ).MAIN( def_key = 'indirect' )
                                    if self.error is None: 
                                        self.final_values, self.error = Tuples.TUPLE( self.DataBase, self.line, self.value,
                                                                self.name, self.dictionary[ 'functions' ]).TUPLE(self.main_name, self.normal_expr )
                                    else: pass    
                                else: self.error = er.ERRORS( self.line ).ERROR22( self.name, 'tuple( )' )
                            else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )                    
                    elif type( self.value ) == type( complex() )    :
                        if self.main_name == self.main_expr: 
                            if self.name != self.expr:
                                if self.name in self.cplxFunctions:
                                    self.historyOfFunctions.append( self.name )
                                    self.expression         = 'def '+self.expr+ ':'
                                    self.dictionary         = {
                                    'functions'             : [],
                                    'func_names'            : []
                                    }
                                    self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                                self.line ).MAIN( def_key = 'indirect' )
                                    if self.error is None: 
                                        self.final_values, self.error = cplx.CPLX( self.DataBase, self.line, self.value,
                                                                self.name, self.dictionary[ 'functions' ]).CPLX( )
                                    else: pass    
                                else: self.error = er.ERRORS( self.line ).ERROR22( self.name, 'complex( )' )
                            else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )    
                    elif type( self.value ) in [type( float() ) ]   :
                        if self.main_name == self.main_expr: 
                            if self.name != self.expr:
                                if self.name in self.floatFunctions:
                                    self.historyOfFunctions.append( self.name )
                                    self.expression         = 'def '+self.expr+ ':'
                                    self.dictionary         = {
                                    'functions'             : [],
                                    'func_names'            : []
                                    }
                                    self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                                self.line ).MAIN( def_key = 'indirect' )
                                    if self.error is None: 
                                        self.final_values, self.error = Float.Float( self.DataBase, self.line, self.value,
                                                                self.name, self.dictionary[ 'functions' ]).Float( self.normal_expr )
                                    else: pass    
                                else: self.error = er.ERRORS( self.line ).ERROR22( self.name, 'float( )' )
                            else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )                
                    elif type( self.value ) == type(pd.DataFrame({"s":[1]})):
                        if self.main_name == self.main_expr: 
                            if self.name != self.expr:
                                if self.name in self.table:
                                    self.historyOfFunctions.append( self.name )
                                    self.expression         = 'def '+self.expr+ ':'
                                    self.dictionary         = {
                                    'functions'             : [],
                                    'func_names'            : []
                                    }
                                    self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                                self.line ).MAIN( def_key = 'indirect' )
                                    if self.error is None: 
                                        self.final_values, self.error = frame.DATA( self.DataBase, self.line, self.value,
                                                                            self.name, self.dictionary[ 'functions' ]).FRAME( self.main_name, self.normal_expr )
                                    else: pass    
                                else: self.error = er.ERRORS( self.line ).ERROR22( self.name, 'table( )' )
                            else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )       
                    elif type( self.value ) == type(np.array([1])):
                        if self.main_name == self.main_expr: 
                            if self.name != self.expr:
                                if self.name in self.ndarrays:
                                    self.historyOfFunctions.append( self.name )
                                    self.expression         = 'def '+self.expr+ ':'
                                    self.dictionary         = {
                                    'functions'             : [],
                                    'func_names'            : []
                                    }
                                    self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                                self.line ).MAIN( def_key = 'indirect' )
                                    if self.error is None: 
                                        self.list_of_args = argm.arg( self.name).arguments()
                                        self.final_values, self.error = m2D.MATRIX_2D( self.DataBase, self.line, self.value,
                                                        self.name, self.dictionary[ 'functions' ]).MATRIX_2D( self.main_name, self.normal_expr, self.list_of_args )
                                    else: pass    
                                else: self.error = er.ERRORS( self.line ).ERROR22( self.name, 'ndarray( )' )
                            else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                    else: self.error = er.ERRORS( self.line ).ERROR31( self.main_name )
                
                elif self.main_name in  self.DataBase[ 'open' ][ 'name' ]:
                    self.idd    = self.DataBase[ 'open' ][ 'name' ].index( self.main_name )
                    self.value  = [self.DataBase[ 'open' ][ 'name' ][self.idd],self.DataBase[ 'open' ][ 'file' ][self.idd],
                                   self.DataBase[ 'open' ][ 'action' ][self.idd],self.DataBase[ 'open' ][ 'status' ][self.idd],
                                   self.DataBase[ 'open' ][ 'encoding' ][self.idd]]
                    
                    if self.main_name == self.main_expr: 
                        if self.name != self.expr:
                            if self.name in self.fileios:
                                self.historyOfFunctions.append( self.name )
                                self.expression         = 'def '+self.expr+ ':'
                                self.dictionary         = {
                                'functions'             : [],
                                'func_names'            : []
                                }
                                self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                            self.line ).MAIN( def_key = 'indirect' )
                                if self.error is None: 
                                    self.final_values, self.error = readfile.READFILE( self.DataBase, self.line, self.value,
                                                        self.name, self.dictionary[ 'functions' ]).READFILE( self.main_name, self.normal_expr)
                                else: pass    
                            else: self.error = er.ERRORS( self.line ).ERROR22( self.name, 'iosfile()' )
                        else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                    else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )               
                else: self.error = er.ERRORS( self.line ).ERROR13( self.main_name, 'class' )
        
        else: self.error = er.ERRORS( self.line ).ERROR0( self.normal_expr )
        
        return self.final_values, self.value_from_db, self.initialize_values, self.error

    def FINAL_TREATEMENT(self):
        self.error                  = None 
        self.final_values           = None
        self.initialize_values      = None
        self.value_from_db          = None
        self.normal_expr            = ''
        
        self.main_name      = self.master[ 'names' ][ 0 ]
        
        for i, _str_ in enumerate( self.master['expressions'] ):
            if i < len(self.master[ 'expressions'])-1:
                self.normal_expr += _str_+'.'
            else: self.normal_expr += _str_
        
        if len( self.master[ 'names' ]) <= 100:
            if len( self.master[ 'names' ])   == 2:
                self.sub_name  = self.master[ 'names' ][ 1 ]
                self.sub_expr  = self.master[ 'expressions' ][ 1 ]
                
                if self.main_name not in self.DataBase['modulesImport']['fileNames']: 
                    self.mod = load.LOAD(self.DataBase['modulesImport']['mainClassNames'], self.main_name).LOAD()
                    if self.mod['key'] is False:
                        self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                                                       self.DataBase, self.line ).TREATMENT( )                    
                    else:
                        self.n1 = self.DataBase['modulesImport']['class_names'][self.mod['id1']].index( self.main_name )
                        self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                                                        self.DataBase, self.line ).TREATMENT( loading = True, idd1 = self.mod['id1'],
                                                                                           idd2 = self.n1, length = 2)
                else:
                    self.mod = loading.LOAD(self.DataBase[ 'modulesImport' ][ 'modulesLoadF' ], self.sub_name).LOAD()
                    if self.mod['key'] is True: 
                        if self.sub_expr != self.sub_name:
                            self.master['names']        = [self.sub_name]
                            self.master['expressions']  = self.sub_expr 
                            self.master['type']         = "function"
                            
                            self.allNames               = self.DataBase[ 'modulesImport' ][ 'modulesLoadF' ][self.mod['id1']]['func_names']
                            self._functions_            = self.DataBase[ 'modulesImport' ][ 'modulesLoadF' ][self.mod['id1']]['functions']
                
                            self.DataBase[ 'modulesImport' ]['mainFuncNames'].append(self.allNames )
                            self.DataBase[ 'modulesImport' ]['func_names'].append(self.allNames )
                            self.DataBase[ 'modulesImport' ]['functions'].append(self._functions_)
                         
                            self.final_values, self.value_from_db, self.initialize_values, self.error = func.FUNCTION_TREATMENT( self.master,
                                                                    self.DataBase, self.line ).TREATMENT( self.normal_expr, self.master, 
                                                                                                         _main_ = self.main_name )
                            self.DataBase[ 'modulesImport' ]['mainFuncNames']   = self.DataBase[ 'modulesImport' ]['mainFuncNames'][ : -1]
                            self.DataBase[ 'modulesImport' ]['func_names']      = self.DataBase[ 'modulesImport' ]['func_names'][ : -1]
                            self.DataBase[ 'modulesImport' ]['functions']       = self.DataBase[ 'modulesImport' ]['functions'][ : -1 ]
                            
                        else: self.error = er.ERRORS(self.line).ERROR42(self.main_name, self.sub_name)
                    else: 
                        self.n1 = self.DataBase['modulesImport']['fileNames'].index( self.main_name )
                        self.new_main_name = self.DataBase['modulesImport']['alias'][ self.n1 ][self.main_name]
                        self.mod = load.LOAD(self.DataBase['modulesImport']['class_names'], self.new_main_name).LOAD()
                        if self.mod['key'] is True: 
                            self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                                                        self.DataBase, self.line ).TREATMENT( loading = True, idd1 = self.mod['id1'],
                                                                                                idd2 = self.mod['id2'], length = 2)
                        else:  self.error = er.ERRORS(self.line).ERROR46( self.main_name, self.sub_name )
                    
            elif len( self.master[ 'names' ]) == 3:
                self._master_ = self.master.copy()
                if self.main_name in self.DataBase['modulesImport']['fileNames']: 
                    self.master['names']        = self.master['names'][1 : ]
                    self.master['expressions']  = self.master['expressions'][1 : ]
                    self.sub_name = self.master['names'][ 0 ]
                    
                    self.mod = loading.LOAD(self.DataBase['modulesImport'][ 'modulesLoadC' ], self.sub_name).LOAD( 'class_names' )
                    if self.mod['key'] is True: 
                        self.db = self.DataBase.copy()
                        self.n   = self.DataBase['modulesImport']['fileNames'].index(self.main_name)
                        load.LOAD(None, None).GLOBAL_VARS(self.db, self.DataBase['modulesImport']['variables'], self.n, typ = 'class')
                        self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                            self.db, self.line ).TREATMENT( self.main_name+'.', loading = True, idd1 = self.mod['id1'], 
                                                                                 idd2 = self.mod['id2'] )
                        del self.db
                    else: 
                        self.new_master, self.rest = n_v.NESTED(self._master_, self.DataBase, self.line).SUB_NESTED_CLASS(  )
                        self.error = er.ERRORS(self.line).ERROR45(self.rest['names'][0], self.rest['names'][1]) 
                else: 
                    if  self.main_name in self.DataBase['class_names']:
                        self.sub_name       = self.master['names'][ 1 ]
                        self.location       = self.DataBase['class_names'].index( self.main_name )
                        
                        self.locValue       = self.DataBase['classes'][self.location][ 0 ][ 0 ]
                        
                        try:
                            if self.sub_name in self.locValue['sub_classes']['class_names']:
                                self.allNames               = self.locValue[ 'sub_classes' ]['class_names']
                                self._functions_            = self.locValue[ 'sub_classes' ]['classes']
                                
                                self.data = {
                                    'class_names'   : self.allNames,
                                    'classes'       : self._functions_ 
                                }
                                
                                self.DataBase[ 'modulesImport' ]['modulesLoadC'].append( self.data )
                                self.mod = loading.LOAD(self.DataBase['modulesImport'][ 'modulesLoadC' ], self.sub_name).LOAD( 'class_names' )
                                
                                self.master['names']        = self.master['names'][1 : ]
                                self.master['expressions']  = self.master['expressions'][ 1 :]
                                self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                                self.DataBase, self.line ).TREATMENT( self.main_name+'.', loading = True, idd1 = self.mod['id1'], 
                                                                                    idd2 = self.mod['id2'], length = 3, tabulation = 3 )
                                
                                self.DataBase[ 'modulesImport' ]['modulesLoadC']  = self.DataBase[ 'modulesImport' ]['modulesLoadC'][ : -1]                          
                            else:  self.error = er.ERRORS(self.line).ERROR44(self.main_name, self.sub_name) 
                        except TypeError:
                            self.check_type,self.is_found  = False, False
                            self.new_master, self.rest = n_v.NESTED(self._master_, self.DataBase, self.line).SUB_NESTED_CLASS(  ) 
                            if self.sub_name in self.DataBase['variables']['vars']:
                                self.is_found = True
                                self.index =  self.DataBase['variables']['vars'].index(self.sub_name)  
                                if type(self.DataBase['variables']['values'][self.index]) in [type(list()), type(dict()), type(np.array([1]))]:
                                    self.att_values = self.DataBase['variables']['values'][self.index].copy()
                                    self.check_type = True
                                else: self.att_values = self.DataBase['variables']['values'][self.index]
                            else:
                                self.DataBase['variables']['vars'].append(self.sub_name)
                                self.att_values = self.DataBase['variables']['values'].append("None")
                                self.index =  self.DataBase['variables']['vars'].index(self.sub_name)  
                            
                            self.final_values, self.value_from_db, self.initialize_values, self.error = n_v.NESTED(self.new_master, 
                                                                                    self.DataBase, self.line).SUB_NESTED_VAR( self.index )
                            
                            if self.error is None:
                                self.final_values, self.value_from_db, self.initialize_values, self.error = n_v.NESTED(self.rest, 
                                                                                        self.DataBase, self.line).SUB_NESTED_VAR( self.index )
                                if self.error is None:
                                    if self.is_found is True:
                                        if self.check_type is True: self.DataBase['variables']['values'][self.index] = self.att_values.copy()
                                        else: self.DataBase['variables']['values'][self.index] = self.att_values
                                    else:
                                        del self.DataBase['variables']['values'][self.index]
                                        del self.DataBase['variables']['vars'][self.index]
                                else: pass
                            else: pass
                    elif  self.main_name in self.DataBase['variables']['vars']: 
                        self.index = self.DataBase['variables']['vars'].index(self.main_name)
                        self.check_type = False 
                        if  type(self.DataBase['variables']['values'][self.index]) in [type(list()), type(dict()), type(np.array([1]))]:
                            self.storage_this_vars = self.DataBase['variables']['values'][self.index].copy()
                            self.check_type = True 
                        else: self.storage_this_vars = self.DataBase['variables']['values'][self.index]
                        self.final_values, self.value_from_db, self.initialize_values, self.error = n_v.NESTED(self.master, 
                                                                                    self.DataBase, self.line).SUB_NESTED_VAR( self.index )
                        if self.error is None:
                            if self.check_type is False: self.DataBase['variables']['values'][self.index] = self.storage_this_vars
                            else: self.DataBase['variables']['values'][self.index] = self.storage_this_vars.copy()
                            self.check_type = False
                        else: pass   
                    else: self.error = er.ERRORS(self.line).ERROR13(self.main_name)
                
            elif len( self.master[ 'names' ]) == 4:
                if self.main_name in self.DataBase['modulesImport']['fileNames']: 
                    self.location       = self.DataBase['modulesImport']['fileNames'].index(self.main_name)
                    self.sub_name       = self.master[ 'names' ][ 1 ]
                    self.locValue       = self.DataBase['modulesImport'][ 'modulesLoadC' ][ self.location ]
                    
                    if self.sub_name in self.locValue['class_names']:
                        self.sub_location   = self.locValue['class_names'].index( self.sub_name )
                    
                        self.sub_locValue   = self.locValue['classes'][ self.sub_location][ 0 ][ 0 ]
                        self.sub_sub_name   = self.master[ 'names' ][ 2 ]
                        
                        if self.sub_sub_name in self.sub_locValue['sub_classes']['class_names']:           
                            self.allNames               = self.sub_locValue[ 'sub_classes' ]['class_names']
                            self._functions_            = self.sub_locValue[ 'sub_classes' ]['classes']
                            
                            self.data = {
                                'class_names'   : self.allNames,
                                'classes'       : self._functions_ 
                            }
                            self.db = self.DataBase.copy()
                            
                            self.DataBase[ 'modulesImport' ]['modulesLoadC'].append( self.data )
                            self.mod = loading.LOAD(self.DataBase['modulesImport'][ 'modulesLoadC' ], self.sub_sub_name).LOAD( 'class_names' )
                            self.n   = self.DataBase['modulesImport']['fileNames'].index(self.main_name)
                         
                            load.LOAD(None, None).GLOBAL_VARS(self.DataBase, self.DataBase['modulesImport']['variables'], self.n, typ = 'class')
                            
                            self.master['names']        = self.master['names'][2 : ]
                            self.master['expressions']  = self.master['expressions'][ 2 :]
                            self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                            self.DataBase, self.line ).TREATMENT( self.main_name+'.', loading = True, idd1 = self.mod['id1'], 
                                                                                 idd2 = self.mod['id2'], length = 3, tabulation = 3 )
                            
                            #self.DataBase[ 'modulesImport' ]['modulesLoadC']  = self.DataBase[ 'modulesImport' ]['modulesLoadC'][ : -1]
                            self.DataBase = self.db.copy()
                            del self.db
                                                    
                        else: self.error = er.ERRORS(self.line).ERROR44(self.sub_name, self.sub_sub_name)
                    else: self.error = er.ERRORS(self.line).ERROR45(self.main_name, self.sub_name)
                elif  self.main_name in self.DataBase['variables']['vars']:
                    self.index = self.DataBase['variables']['vars'].index(self.main_name)
                    self.check_type = False 
                    if  type(self.DataBase['variables']['values'][self.index]) in [type(list()), type(dict()), type(np.array([1]))]:
                        self.storage_this_vars = self.DataBase['variables']['values'][self.index].copy()
                        self.check_type = True 
                    else: self.storage_this_vars = self.DataBase['variables']['values'][self.index]
                    self.final_values, self.value_from_db, self.initialize_values, self.error = n_v.NESTED(self.master, 
                                                                                self.DataBase, self.line).SUB_NESTED_VAR( self.index )
                    if self.error is None:
                        if self.check_type is False: self.DataBase['variables']['values'][self.index] = self.storage_this_vars
                        else: self.DataBase['variables']['values'][self.index] = self.storage_this_vars.copy()
                        self.check_type = False
                    else: pass 
                else: self.error = er.ERRORS(self.line).ERROR43(self.main_name)
            
            else:
                if  self.main_name in self.DataBase['variables']['vars']:
                    self.index = self.DataBase['variables']['vars'].index(self.main_name)
                    self.check_type = False 
                    if  type(self.DataBase['variables']['values'][self.index]) in [type(list()), type(dict()), type(np.array([1]))]:
                        self.storage_this_vars = self.DataBase['variables']['values'][self.index].copy()
                        self.check_type = True 
                    else: self.storage_this_vars = self.DataBase['variables']['values'][self.index]
                    self.final_values, self.value_from_db, self.initialize_values, self.error = n_v.NESTED(self.master, 
                                                                                self.DataBase, self.line).SUB_NESTED_VAR( self.index )
                    if self.error is None:
                        if self.check_type is False: self.DataBase['variables']['values'][self.index] = self.storage_this_vars
                        else: self.DataBase['variables']['values'][self.index] = self.storage_this_vars.copy()
                        self.check_type = False
                    else: pass 
                else: self.error = er.ERRORS(self.line).ERROR43(self.main_name)
        else : self.error = er.ERRORS( self.line ).ERROR0( self.normal_expr )
        
        return self.final_values, self.value_from_db, self.initialize_values, self.error
        

    



    

   

    

 

        

         
