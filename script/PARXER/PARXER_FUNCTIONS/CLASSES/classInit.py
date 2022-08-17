from msilib.schema import Error
import                                              random
from script.DATA_BASE                               import data_base as db
from script.STDIN.LinuxSTDIN                        import bm_configure as bm
from script.LEXER.FUNCTION                          import main
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS       import functions as func
from script.LEXER.FUNCTION                          import print_value
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation
from script                                         import control_string
try:
    from CythonModules.Windows                      import fileError as fe 
except ImportError:
    from CythonModules.Linux                        import fileError as fe 
    

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
                                    
                    self.function_names     = self.main_body[ 'function_names' ]
                    self.inheritanceClass   = self.main_body[ 'class_inheritance' ]
                                
                    if self.main_body[ 'init_function' ] is None: 
                        
                        self._variables_        = None
                        self.key                = False
                        self._function_names_   = None 
                        self._functions_        = None
                        
                        if self.main_expr != self.main_name:
                            self._ = CHECK(self.main_expr, self.main_name, self.DataBase, self.line ).CHECK()
                            if self._ is True: pass 
                            else: self.error = ERRORS( self.line ).ERROR14( self.main_name, 'class' )
                        else: pass 
                        
                        if self.error is None:
                            if self.inheritanceClass is None: pass 
                            else: 
                                self.key = True
                                self._function_names_, self._functions_, self._variables_, self.error = ININHERITANCE( self.DataBase, self.line ,
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
                                                self._return_, self.error = func.FUNCTION(  self.dictionary[ 'functions' ] , self.DataBase, 
                                                                                        self.line ).DOUBLE_INIT_FUNCTION( self.normal_expr, self.name )
                                                if self.error is None:
                                                    self._new_data_base_, self.error = func.FUNCTION( self.my_function[ 1 ], self.DataBase,
                                                                    self.line).INIT_FUNCTION( self.normal_expr, self._return_ )
                                                    if self.error is None: 
                                                        self.new_data_base           = self._new_data_base_[ 'data_base' ]
                                                        
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
                                                        
                                                        self.final_values, self.value_from_db, self.initialize_values, self.error = RUN_FUNCTION( self.DataBase, self.line,
                                                                self.new_data_base, self._new_data_base_).RUN( self.all_data_analyses, self.name ,
                                                                                                        tabulation = tabulation )
                                                    else: pass 
                                                else: pass 
                                            else: pass
                                        else:self.error = ERRORS( self.line ).ERROR13( self.main_name, self.name )
                                    else: self.error = ERRORS( self.line ).ERROR13( self.main_name, self.name )
                                else: 
                                    if self.key is False: self.error = ERRORS( self.line ).ERROR21( self.main_name, self.name )
                                    else: 
                                        self._vars_     = []
                                        self._values_   = []
                                                
                                        _, _, self._variables_, self.error = ININHERITANCE( self.DataBase, self.line ,
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
                                                else: self.error = ERRORS( self.line ).ERROR21( self.main_name, self.name )
                                            else: self.error = ERRORS( self.line ).ERROR21( self.main_name, self.name )
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
                            self._return_, self.error = func.FUNCTION(  self.dictionary[ 'functions' ] , self.DataBase, 
                                                                self.line ).DOUBLE_INIT_FUNCTION( self.normal_expr, 'initialize' )
                        
                            if self.error is None:
                                self._new_data_base_, self.error = func.FUNCTION( [ self.function_init ], self.DataBase,
                                                        self.line).INIT_FUNCTION( self.normal_expr, self._return_ )
                                if self.error is None:
                                    self.new_data_base1          = self._new_data_base_[ 'data_base' ]
                                    
                                    if self.new_data_base1[ 'empty_values' ] is None: pass 
                                    else: 
                                        self.empty_values   = self.new_data_base1[ 'empty_values' ]
                                        self.error          = ERRORS( self.line ).ERROR15( 'initialize' , self.empty_values )
                                        
                                    self._, self.value, self.variables, self.error = RUN_FUNCTION( self.DataBase, self.line,
                                                                    self.new_data_base1, self._new_data_base_).RUN(self.all_data_analyses_init, 
                                                                                    'initialize', tabulation = tabulation)
                                    
                                    if self.error is None:
                                        if self.expr != self.name: 
                                            self._variables_    = None
                                            self.key            = False
                                            if self.inheritanceClass is None: pass 
                                            else: 
                                                self.key = True
                                                self._function_names_, self._functions_, self._variables_, self.error = ININHERITANCE( self.DataBase, self.line ,
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
                                                            self._return_, self.error = func.FUNCTION(  self.dictionary[ 'functions' ] , self.DataBase, 
                                                                                    self.line ).DOUBLE_INIT_FUNCTION( self.normal_expr, self.name )
                                                            if self.error is None:
                                                                self._new_data_base_, self.error = func.FUNCTION( self.my_function[ 1 ] , self.DataBase,
                                                                                self.line).INIT_FUNCTION( self.normal_expr, self._return_ )
                                                                
                                                                if self.error is None:
                                                                    self.new_data_base           = self._new_data_base_[ 'data_base' ]
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
                                                                    self.final_values, self.value_from_db, self.initialize_values, self.error = RUN_FUNCTION( self.DataBase, self.line,
                                                                                self.new_data_base, self._new_data_base_).RUN( self.all_data_analyses, self.name,
                                                                                                                              tabulation = tabulation)
                                                                    
                                                                else: pass 
                                                            else: pass
                                                        else: pass
                                                    else:self.error = ERRORS( self.line ).ERROR13( self.main_name, self.name )
                                                else: self.error = ERRORS( self.line ).ERROR13( self.main_name, self.name )
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
                                                _, _, self._variables_, self.error = ININHERITANCE( self.DataBase, self.line ,
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
                                                    else: self.error = ERRORS( self.line ).ERROR21( self.main_name, self.name )
                                                else: self.error = ERRORS( self.line ).ERROR21( self.main_name, self.name )
                                            else: pass
                                    else: pass
                                else: pass
                            else: pass
                        else: pass   
                except KeyError: self.error = ERRORS( self.line).ERROR13( self.main_name )
                    
            else: 
                self.strFunctions       = [ 'upper', 'lower', 'capitalize', 'empty', 'enumerate', 'split', 'join', 'format', 'index', 'rstrip', 'lstrip',
                                            'count', 'endwith', 'startwith', 'replace', 'size']
                self.dictFunctions      = [ 'empty', 'get', 'clear', 'copy', 'remove', 'init'] 
                self.cplxFunctions      = [ 'img', 'real', 'norm', 'conj' ] 
                self.tupleFunctions     = [ 'empty', 'init', 'enumerate', 'size', 'choice', 'index', 'count'] 
                self.listFunctions      = [ 'empty', 'clear', 'copy', 'remove', 'init', 'index', 'count', 'sorted', 'add', 'insert', 'random', 'enumerate',
                                            'size', 'round', 'rand', 'choice' ]
                self.fileios            = ['readline', 'readlines', 'read', 'writeline', 'writelines', 'close', 'write' ]
                
                if self.main_name in self.DataBase[ 'variables' ][ 'vars' ]: 
                    
                    self.idd    = self.DataBase[ 'variables' ][ 'vars' ].index( self.main_name )
                    self.value  = self.DataBase[ 'variables' ][ 'values' ][ self.idd ]
                    
                    if   type( self.value ) == type( str() )    :
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
                                        self.final_values, self.error = STRING( self.DataBase, self.line, self.value,
                                                                            self.name, self.dictionary[ 'functions' ]).STR( self.main_name, self.normal_expr)
                                    else: pass    
                                else: self.error = ERRORS( self.line ).ERROR22( self.name )
                            else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        
                    elif type( self.value ) == type( dict() )   :
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
                                        self.final_values, self.error = DICTIONARY( self.DataBase, self.line, self.value,
                                                                            self.name, self.dictionary[ 'functions' ]).DICT( self.main_name, self.normal_expr )
                                    else: pass    
                                else: self.error = ERRORS( self.line ).ERROR22( self.name, 'dictionary( )' )
                            else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                    
                    elif type( self.value ) == type( list() )   :
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
                                        self.final_values, self.error = LIST( self.DataBase, self.line, self.value,
                                                                self.name, self.dictionary[ 'functions' ]).LIST( self.main_name, self.normal_expr )
                                    else: pass    
                                else: self.error = ERRORS( self.line ).ERROR22( self.name, 'list( )' )
                            else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                    
                    elif type( self.value ) == type( tuple() )  :
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
                                        self.final_values, self.error = TUPLE( self.DataBase, self.line, self.value,
                                                                self.name, self.dictionary[ 'functions' ]).TUPLE(self.main_name, self.normal_expr )
                                    else: pass    
                                else: self.error = ERRORS( self.line ).ERROR22( self.name, 'tuple( )' )
                            else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                    
                    elif type( self.value ) == type( complex() ):
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
                                        self.final_values, self.error = CPLX( self.DataBase, self.line, self.value,
                                                                self.name, self.dictionary[ 'functions' ]).CPLX( )
                                    else: pass    
                                else: self.error = ERRORS( self.line ).ERROR22( self.name, 'complex( )' )
                            else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                        else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                    
                    else: self.error = ERRORS( self.line ).ERROR31( self.main_name )
                
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
                                    self.final_values, self.error = READFILE( self.DataBase, self.line, self.value,
                                                        self.name, self.dictionary[ 'functions' ]).READFILE( self.main_name, self.normal_expr)
                                else: pass    
                            else: self.error = ERRORS( self.line ).ERROR22( self.name, 'iosfile()' )
                        else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                    else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
                
                else: self.error = ERRORS( self.line ).ERROR13( self.main_name, 'class' )
        
        else: self.error = ERRORS( self.line ).ERROR0( self.normal_expr )
        
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
        
        if len( self.master[ 'names' ]) <= 4:
            if len( self.master[ 'names' ])   == 2:
                self.sub_name  = self.master[ 'names' ][ 1 ]
                self.sub_expr  = self.master[ 'expressions' ][ 1 ]
                
                if self.main_name not in self.DataBase['modulesImport']['fileNames']: 
                    self.mod = func.LOAD(self.DataBase['modulesImport']['mainClassNames'], self.main_name).LOAD()
                    if self.mod['key'] is False:
                        self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                                                       self.DataBase, self.line ).TREATMENT( )                    
                    else:
                        self.n1 = self.DataBase['modulesImport']['class_names'][self.mod['id1']] .index( self.main_name )
                        self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                                                        self.DataBase, self.line ).TREATMENT( loading = True, idd1 = self.mod['id1'],
                                                                                                idd2 = self.n1, length = 2)
                else:
                    self.mod = LOAD(self.DataBase[ 'modulesImport' ][ 'modulesLoadF' ], self.sub_name).LOAD()
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
                            
                        else: self.error = ERRORS(self.line).ERROR42(self.main_name, self.sub_name)
                    else: 
                        self.n1 = self.DataBase['modulesImport']['fileNames'].index( self.main_name )
                        self.new_main_name = self.DataBase['modulesImport']['alias'][ self.n1 ][self.main_name]
                        self.mod = func.LOAD(self.DataBase['modulesImport']['class_names'], self.new_main_name).LOAD()
                        if self.mod['key'] is True: 
                            self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                                                        self.DataBase, self.line ).TREATMENT( loading = True, idd1 = self.mod['id1'],
                                                                                                idd2 = self.mod['id2'], length = 2)
                        else:  self.error = ERRORS(self.line).ERROR46( self.main_name, self.sub_name )
                    
            elif len( self.master[ 'names' ]) == 3:
                if self.main_name in self.DataBase['modulesImport']['fileNames']: 
                    self.master['names']        = self.master['names'][1 : ]
                    self.master['expressions']  = self.master['expressions'][1 : ]
                    
                    self.sub_name = self.master['names'][ 0 ]
                    
                    self.mod = LOAD(self.DataBase['modulesImport'][ 'modulesLoadC' ], self.sub_name).LOAD( 'class_names' )
                    
                    if self.mod['key'] is True: 
                        self.db = self.DataBase.copy()
                        self.n   = self.DataBase['modulesImport']['fileNames'].index(self.main_name)
                        func.LOAD(None, None).GLOBAL_VARS(self.db, self.DataBase['modulesImport']['variables'], self.n, typ = 'class')
                        self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                            self.db, self.line ).TREATMENT( self.main_name+'.', loading = True, idd1 = self.mod['id1'], 
                                                                                 idd2 = self.mod['id2'] )
                        del self.db
                    else: self.error = ERRORS(self.line).ERROR45(self.main_name, self.sub_name)
                    
                else: 
                    if  self.main_name in self.DataBase['class_names']:
                        self.sub_name       = self.master['names'][ 1 ]
                        self.location       = self.DataBase['class_names'].index( self.main_name )
                        
                        self.locValue       = self.DataBase['classes'][self.location][ 0 ][ 0 ]
                        
                        if self.sub_name in self.locValue['sub_classes']['class_names']:
                            self.allNames               = self.locValue[ 'sub_classes' ]['class_names']
                            self._functions_            = self.locValue[ 'sub_classes' ]['classes']
                            
                            self.data = {
                                'class_names'   : self.allNames,
                                'classes'       : self._functions_ 
                            }
                            
                            self.DataBase[ 'modulesImport' ]['modulesLoadC'].append( self.data )
                            self.mod = LOAD(self.DataBase['modulesImport'][ 'modulesLoadC' ], self.sub_name).LOAD( 'class_names' )
                            
                            self.master['names']        = self.master['names'][1 : ]
                            self.master['expressions']  = self.master['expressions'][ 1 :]
                            self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                            self.DataBase, self.line ).TREATMENT( self.main_name+'.', loading = True, idd1 = self.mod['id1'], 
                                                                                 idd2 = self.mod['id2'], length = 3, tabulation = 3 )
                            
                            self.DataBase[ 'modulesImport' ]['modulesLoadC']  = self.DataBase[ 'modulesImport' ]['modulesLoadC'][ : -1]
                                              
                        else:  self.error = ERRORS(self.line).ERROR44(self.main_name, self.sub_name)
                        
                    else: self.error = ERRORS(self.line).ERROR13(self.main_name)
                
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
                            self.mod = LOAD(self.DataBase['modulesImport'][ 'modulesLoadC' ], self.sub_sub_name).LOAD( 'class_names' )
                            self.n   = self.DataBase['modulesImport']['fileNames'].index(self.main_name)
                         
                            func.LOAD(None, None).GLOBAL_VARS(self.DataBase, self.DataBase['modulesImport']['variables'], self.n, typ = 'class')
                            
                            self.master['names']        = self.master['names'][2 : ]
                            self.master['expressions']  = self.master['expressions'][ 2 :]
                            self.final_values, self.value_from_db, self.initialize_values, self.error = CLASS_TREATMENT( self.master, 
                                            self.DataBase, self.line ).TREATMENT( self.main_name+'.', loading = True, idd1 = self.mod['id1'], 
                                                                                 idd2 = self.mod['id2'], length = 3, tabulation = 3 )
                            
                            #self.DataBase[ 'modulesImport' ]['modulesLoadC']  = self.DataBase[ 'modulesImport' ]['modulesLoadC'][ : -1]
                            self.DataBase = self.db.copy()
                            del self.db
                                                    
                        else: self.error = ERRORS(self.line).ERROR44(self.sub_name, self.sub_sub_name)
                    else: self.error = ERRORS(self.line).ERROR45(self.main_name, self.sub_name)
                else: self.error = ERRORS(self.line).ERROR43(self.main_name)
    
        else : self.error = ERRORS( self.line ).ERROR0( self.normal_expr )
        
        return self.final_values, self.value_from_db, self.initialize_values, self.error
               
class CHECK:
    def __init__(self, 
                master      : str, 
                name        : str, 
                DataBase    : dict, 
                line        : int
                ):
        self.master             = master 
        self.line               = line
        self.DataBase           = DataBase
        self.ClassName          = name
        self.control            = control_string.STRING_ANALYSE( self.DataBase, self.line )
        
    def CHECK( self ):
        self.key = False
        
        self.string             = self.master[ len( self.ClassName )+1 : - 1 ]
        self.name, self.error   = self.control.DELETE_SPACE( self.string )
        
        if self.error is None: pass
        else: self.key = True
        
        return self.key 
        
class RUN_FUNCTION:
    def __init__(self, 
                DataBase        : dict, 
                line            : int, 
                new_data_base   : dict, 
                _new_data_base_ : dict 
                ) :
        self.DataBase           = DataBase
        self.line               = line 
        self.new_data_base      = new_data_base
        self._new_data_base_    = _new_data_base_
        
    def RUN( self,  all_data_analyses: list, functionName : str, tabulation: int =2)   :
        self.all_data_analyses  = all_data_analyses
        self.error              = None
        self.initialize_values  = None
        self.functionName       = functionName
        self.final_values       = None
        self.vars               = None 
        self._values_           = None
        
        
        self.new_data_base[ 'classes' ]         = self.DataBase[ 'classes' ]
        self.new_data_base[ 'class_names' ]     = self.DataBase[ 'class_names' ]
        self.new_data_base[ 'func_names' ]      = self.DataBase[ 'func_names' ]
        self.new_data_base[ 'functions' ]       = self.DataBase[ 'functions' ]
        
        self.new_data_base[ 'print' ]   = []
                                            
        if self.new_data_base[ 'empty_values' ] is None:
            
            self.error = func.EXTERNAL_DEF_LOOP_STATEMENT( None, self.new_data_base,
                                        self.line ).DEF_STATEMENT( tabulation, self.all_data_analyses )
            if self.error is None:
                self.vars                   = self.new_data_base[ 'variables' ]['vars'][:]
                self._values_               = self.new_data_base[ 'variables' ]['values'][:]
                self.initialize_values      = self.new_data_base[ 'variables' ]
                self.DataBase[ 'irene' ]    = self.new_data_base[ 'irene' ]
                self.keyActivation          = False

                if self.new_data_base[ 'return' ] is not None:
                    
                    if len( self.new_data_base[ 'return' ] ) == 1:
                        self.final_values = self.new_data_base[ 'return' ][ 0 ]
                    else: self.final_values = tuple( self.new_data_base[ 'return' ] )
                    
                    if self.new_data_base[ 'print' ] is not None:
                        self.print_values   = True
                        self.list_of_values = self.new_data_base[ 'print' ]
                        for i, value in enumerate( self.list_of_values ):
                            print_value.PRINT_PRINT( value, self.DataBase ).PRINT_PRINT( key = False )

                        self.new_data_base[ 'print' ]   = []
                    else: pass
                    func.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,
                                                            self._new_data_base_ )
                else:
                    
                    if self.new_data_base[ 'sub_print' ] is None:
                        if self.new_data_base[ 'transformation' ] is None:
                            if self.new_data_base[ 'return' ] is not None:
                                self.final_values   = self.new_data_base[ 'return' ]
                                self.keyActivation  = True
                            else: pass
                            
                        else:
                            self.final_values = self.new_data_base[ 'transformation' ]
                            self.new_data_base[ 'transformation' ]      = None
                            self.keyActivation                          = True
                            
                        if self.new_data_base[ 'print' ] :
                            self.print_values   = True
                            self.list_of_values = self.new_data_base[ 'print' ]

                            for i, value in enumerate( self.list_of_values ):
                                print_value.PRINT_PRINT( value, self.DataBase ).PRINT_PRINT( key = False )

                            self.new_data_base[ 'print' ]       = []
                        else: 
                            if self.keyActivation is True: pass 
                            else: 
                                if self.functionName == 'initialize': pass 
                                else: self.DataBase[ 'no_printed_values' ].append( None )
                            
                        func.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,
                                                            self._new_data_base_ )
                    else:
                        self.DataBase[ 'no_printed_values' ].append( self.new_data_base[ 'sub_print' ] )
                        func.UPDATE_DATA_BASE(None, None, None).INITIALIZATION(self.new_data_base,
                                                        self._new_data_base_)
            else: pass
        else:   
            self.empty_values   = self.new_data_base[ 'empty_values' ]
            self.error          = ERRORS( self.line ).ERROR15( self.functionName , self.empty_values )

        self.initialize_values  = {
            'vars'              : self.vars,
            'values'            : self._values_
        }
      
        return self.final_values, self.DataBase[ 'no_printed_values' ], self.initialize_values, self.error
 
class STRING:
    def __init__(self, DataBase: dict, line:int, master: str, function, FunctionInfo : list ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        self.lexer          = main_lexer
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        
    def STR( self , mainName: str , mainString : str = ''):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.values         = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if   self.function in [ 'lower' ]            :
            if None in self.arguments: self._return_ = self.master.lower()
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'upper' ]            :
            if None in self.arguments:  self._return_ = self.master.upper() 
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'split' ]            :
            self._return_, self.error = STRING( self.DataBase, self.line, self.master,
                                    self.function, [self.FunctionInfo] ).SPLIT( mainString  )  
        elif self.function in [ 'join'  ]            :
            self._return_, self.error = STRING( self.DataBase, self.line, self.master,
                                    self.function, [self.FunctionInfo] ).JOIN( mainString  )  
        elif self.function in [ 'empty' ]            :
            if None in self.arguments: 
                if    self.master: self._return_ = False
                else: self._return_ = True
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'size'  ]            :
            if None in self.arguments: 
                self._return_ = len( self.master )
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'replace'  ]         :
            self._return_, self.error = STRING( self.DataBase, self.line, self.master,
                                    self.function, [self.FunctionInfo] ).REPLACE( mainName, mainString  ) 
        elif self.function in [ 'capitalize']        :
            if None in self.arguments: self._return_ = self.master.capitalize( )
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'enumerate' ]        :
            if  None in self.arguments:
                if self.master:
                    self._return_ = []
                    for i, value in enumerate( self.master ):
                        self._return_.append( (i, value) )
                else: self.error = ERRORS( self.line ).ERROR24( 'string' )     
            else:self.error = ERRORS( self.line ).ERROR14( self.function )    
        elif self.function in [ 'index', 'count', 'startwith', 'endwith' ] :
            self._return_, self.error = STRING( self.DataBase, self.line, self.master,
                                    self.function, [self.FunctionInfo] ).GLOBAL( self.function, mainString  ) 
        
        return self._return_, self.error

    def SPLIT( self,  mainString: str = '') :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.values         = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'master': 
                if self.values[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                else: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.values[ 0 ],
                                                                    self.values[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if type( self.newValues ) == type( str() ):
                                            if self.master:
                                                self._return_   = tuple( self.master.split( sep = self.newValues ) )
                                            else: self.error = ERRORS( self.line ).ERROR24( 'string' )
                                        else: self.error = ERRORS( self.line ).ERROR3( 'master', 'a string()')   
                                    else: pass 
                                else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            else:
                if self.arguments[ 0 ] is None:
                    if self.master: self._return_   = tuple( self.master.split() )
                    else: self.error = ERRORS( self.line ).ERROR24( 'string' )
                else:
                    if self.values[ 0 ] is None:
                        if self.master:
                            self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                    self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase,self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues = self.final_val[ 0 ]
                                                if type( self.newValues ) == type( str() ):
                                                    self._return_   =  tuple( self.master.split( sep = self.newValues ) )
                                                else: self.error = ERRORS( self.line ).ERROR3( 'master', 'a string()')   
                                            else: pass 
                                        else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass
                        else: self.error = ERRORS( self.line ).ERROR24( 'string' )
                    else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error
    
    def JOIN( self,  mainString: str = '')  :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.values         = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'master': 
                if self.values[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                else: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.values[ 0 ],
                                                                    self.values[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if type( self.newValues ) == type( tuple() ):
                                            #if self.master:
                                            try:
                                                self._return_   = self.master.join( self.newValues ) 
                                            except TypeError: self.error = ERRORS( self.line ).ERROR32( self.newValues )
                                            #else: self.error = ERRORS( self.line ).ERROR24( 'list' )
                                        else: self.error = ERRORS( self.line ).ERROR3( 'master', 'a tuple()')   
                                    else: pass 
                                else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            else:
                if self.arguments[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] )
                else:
                    if self.values[ 0 ] is None:
                        self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                        if self.error is None:
                            if 'operator' not in list( self.dict_value.keys() ): 
                                self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                            self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                if self.error is None: 
                                    self.all_data = self.lex[ 'all_data' ]
                                    if self.all_data is not None:
                                        self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                        self.DataBase,self.line).ANALYSE( mainString )
                                        if self.error is None:
                                            self.newValues = self.final_val[ 0 ]
                                            if type( self.newValues ) == type( tuple() ):
                                                #if self.master:
                                                try:
                                                    self._return_   =  self.master.join( self.newValues )
                                                except TypeError : self.error = ERRORS( self.line ).ERROR32( self.newValues )
                                                #else: self.error = ERRORS( self.line ).ERROR24( 'list' )
                                            else: self.error = ERRORS( self.line ).ERROR3( 'master', 'a tuple()')   
                                        else: pass 
                                    else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                                else: pass
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                    else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error
    
    def GLOBAL( self,  typ: str = 'index', mainString: str = '')  :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.values         = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'master': 
                if self.values[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                else: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.values[ 0 ],
                                                                    self.values[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if type( self.newValues ) == type( str() ):
                                            if self.master:
                                                if   typ == 'index'         :
                                                    try:
                                                        self._return_   = self.master.index( self.newValues ) 
                                                    except ValueError: self.error = ERRORS( self.line ).ERROR33( self.newValues )
                                                elif typ == 'count:'        :
                                                        self._return_   =  self.master.count( self.newValues )
                                                elif typ == 'starwith:'     :
                                                        self._return_   =  self.master.startswith( self.newValues )
                                                elif typ == 'endwith:'      :
                                                        self._return_   =  self.master.endswith( self.newValues )
                                                else: pass
                                            else: self.error = ERRORS( self.line ).ERROR24( 'string' )
                                        else: self.error = ERRORS( self.line ).ERROR3( 'master', 'a string()')   
                                    else: pass 
                                else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            else:
                if self.arguments[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] )
                else:
                    if self.values[ 0 ] is None:
                        self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                        if self.error is None:
                            if 'operator' not in list( self.dict_value.keys() ): 
                                self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                            self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                if self.error is None: 
                                    self.all_data = self.lex[ 'all_data' ]
                                    if self.all_data is not None:
                                        self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                        self.DataBase,self.line).ANALYSE( mainString )
                                        if self.error is None:
                                            self.newValues = self.final_val[ 0 ]
                                            if type( self.newValues ) == type( str() ):
                                                if self.master:
                                                    if   typ == 'index'         :
                                                        try:
                                                            self._return_   =  self.master.index( self.newValues )
                                                        except ValueError : self.error = ERRORS( self.line ).ERROR33( self.newValues )
                                                    elif typ == 'count:'        :
                                                        self._return_   =  self.master.count( self.newValues )
                                                    elif typ == 'starwith:'     :
                                                            self._return_   =  self.master.startswith( self.newValues )
                                                    elif typ == 'endwith:'      :
                                                        self._return_   =  self.master.endswith( self.newValues )
                                                    else: pass
                                                else: self.error = ERRORS( self.line ).ERROR24( 'string' )
                                            else: self.error = ERRORS( self.line ).ERROR3( 'master', 'a string()')   
                                        else: pass 
                                    else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                                else: pass
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                    else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = ERRORS( self.line ).ERROR12( self.function, 1)
    
        return self._return_, self.error
    
    def REPLACE (self, mainName: str, mainString:  str)    :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 2:
            if   self.arguments[ 0 ] == 'oldStr'   :
                if   self.arguments[ 1 ] == 'newStr'    : 
                    if   self.value[ 0 ]    is None  and self.value[ 1 ] is not None :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['oldStr']] ) 
                    elif self.value[ 1 ]    is None  and self.value[ 0 ] is not None :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['newStr']] )
                    elif self.value[ 0 ]    is None  and self.value[ 1 ] is None     :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['oldStr'], ['newStr']] )
                    else: 
                        self.newValues = []
                        for value in self.value:
                            self.dict_value, self.error = self.affectation.AFFECTATION(value,
                                                                    value, self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase,self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues.append( self.final_val[ 0 ] )
                                            else: pass 
                                        else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass

                        if self.error is None:
                            try: 
                                if type( self.newValues[ 0 ] ) == type( str() ) :
                                    if type( self.newValues[ 1 ] ) == type( str() ) :
                                        self._return_ = self.master.replace(self.newValues[ 0 ], self.newValues[ 1 ])
                                        del self.newValues
                                    else: self.error = ERRORS( self.line ).ERROR3( "newStr", 'a string()' )
                                else: self.error = ERRORS( self.line ).ERROR3( "oldStr", 'a string()' )
                            except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                        else: pass      
                elif self.arguments[ 1 ] == 'oldStr'       : 
                    self.error = ERRORS( self.line ).ERROR16( self.function, 'oldStr')
                else:
                    if self.value[ 1 ] is None :
                        if self.value[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['oldStr']] ) 
                        else:
                            self.newValues = []
                            self.allValues = [ self.value[ 0 ], self.arguments[ 1 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION( value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ): 
                                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None: 
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                    self.DataBase, self.line).ANALYSE( mainString )
                                                if self.error is None:
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                        else: pass 
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass 
                            
                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( str() ) :
                                        if type( self.newValues[ 1 ] ) == type( str() ) : 
                                            self._return_ = self.master.replace( self.newValues[ 0 ], self.newValues[ 1 ])
                                            del self.newValues
                                            del self.allValues
                                        else: self.error = ERRORS( self.line ).ERROR3( "newStr", 'a string()' )
                                    else: self.error = ERRORS( self.line ).ERROR3( "oldStr", 'a string()' )
                                except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                            else: pass   
                    else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )
                    
            elif self.arguments[ 0 ] == 'newStr': 
                if   self.arguments[ 1 ] == 'oldStr'       : 
                    if   self.value[ 0 ]    is None  and self.value[ 1 ] is not None :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['newStr']] ) 
                    elif self.value[ 1 ]    is None  and self.value[ 0 ] is not None :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['oldStr']] )
                    elif self.value[ 0 ]    is None  and self.value[ 1 ] is None     :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['oldStr'], ['newStr']] )
                    else: 
                        self.newValues = []
                        for value in self.value:
                            self.dict_value, self.error = self.affectation.AFFECTATION(value,
                                                                    value, self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase,self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues.append( self.final_val[ 0 ] )
                                            else: pass 
                                        else: pass 
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass

                        if self.error is None:
                            try: 
                                if type( self.newValues[ 1 ] ) == type( str() ) :
                                    if type( self.newValues[ 1 ] ) == type( str() ) :
                                        self._return_ = self.master.replace( self.newValues[ 1 ], self.newValues[ 0 ])
                                        del self.newValues
                                    else: self.error = ERRORS( self.line ).ERROR3( "newStr", 'a string' )
                                else: self.error = ERRORS( self.line ).ERROR3( "oldStr", 'a string' )
                            except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                        else: pass
                elif self.arguments[ 1 ] == 'newStr'    :
                    self.error = ERRORS( self.line ).ERROR16( self.function, 'newStr')
                else:
                    if self.value[ 1 ] is None :
                        if self.value[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['newStr']] ) 
                        else:
                            self.newValues = []
                            self.allValues = [ self.arguments[ 1 ], self.value[ 0 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION( value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ): 
                                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None: 
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                    self.DataBase, self.line).ANALYSE( mainString )
                                                if self.error is None:
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                                        else: pass 
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass 
                            
                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( str() ) :
                                        if type( self.newValues[ 1 ] ) == type( str() ) :
                                            self.master.insert( self.newValues[ 0 ], self.newValues[ 1 ])
                                            self._return_ = self.master[ : ]
                                            del self.newValues
                                            del self.allValues
                                        else: self.error = ERRORS( self.line ).ERROR3( "newStr", 'a string()' )
                                    else: self.error = ERRORS( self.line ).ERROR3( "oldStr", 'a string()' )
                                except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                            else: pass   
                    else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )
            
            else:
                if self.value[ 0 ] is None: 
                    if self.arguments[ 1 ] == 'newStr': 
                        if self.value[ 1 ] is None  : self.error = ERRORS( self.line ).ERROR15( self.function, [['newStr']] ) 
                        else: 
                            self.newValues = []
                            self.allValues = [ self.arguments[ 0 ], self.value[ 1 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION(value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ): 
                                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None: 
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                self.DataBase,self.line).ANALYSE( mainString )
                                                if self.error is None:
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                                        else: pass
                                    else: 
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass

                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( str() ) :
                                        if type( self.newValues[ 1 ] ) == type( str() ) :
                                            self._return_ = self.master.replace( self.newValues[ 0 ], self.newValues[ 1 ])
                                            del self.newValues
                                            del self.allValues
                                        else: self.error = ERRORS( self.line ).ERROR3( "newStr", 'a string()' )
                                    else: self.error = ERRORS( self.line ).ERROR3( "oldStr", 'a string()' )
                                except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                            else: pass
                    else:
                        if self.value[ 1 ] is None :
                            self.newValues = []
                            self.allValues = [ self.arguments[ 0 ], self.arguments[ 1 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION( value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ): 
                                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None: 
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                    self.DataBase, self.line).ANALYSE( mainString )
                                                if self.error is None:
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                        else: pass 
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass 
                            
                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( str() ) :
                                        if type( self.newValues[ 1 ] ) == type( str() ) :
                                            self._return_ = self.master.replace( self.newValues[ 0 ], self.newValues[ 1 ])
                                            del self.newValues
                                            del self.allValues 
                                        else: self.error = ERRORS( self.line ).ERROR3( "newStr", 'a string()' )
                                    else: self.error = ERRORS( self.line ).ERROR3( "oldStr", 'a string()' )
                                except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                            else: pass   
                        else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )
                else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else:  self.error = ERRORS( self.line ).ERROR12( self.function, 2)

        return self._return_, self.error
             
class DICTIONARY:
    def __init__(self, DataBase: dict, line:int, master: str, function, FunctionInfo : list ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        self.lexer          = main_lexer
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        
    def DICT( self, mainName: str, mainString: str ):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
            
        if   self.function in [ 'get'   ]            :
            if len( self.arguments ) == 1:
                if   self.arguments[ 0 ] in [ 'type' ]:
                    if self.value[ 0 ] is not None:
                        self.dict_value, self.error = self.affectation.AFFECTATION( self.value[ 0 ],
                                                                self.value[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                        if self.error is None:
                            if 'operator' not in list( self.dict_value.keys() ): 
                                self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                            self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                if self.error is None: 
                                    self.all_data = self.lex[ 'all_data' ]
                                    if self.all_data is not None:
                                        self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                        self.DataBase,self.line).ANALYSE( mainString )
                                        if self.error is None:
                                            self.newValues = self.final_val[ 0 ]
                                            if type( self.newValues ) == type( str() ):
                                                if self.master:
                                                    if self.newValues == 'keys':
                                                        self._return_ = list( self.master.keys())
                                                    elif self.newValues == 'items': 
                                                        self._return_ = list( self.master.items() )
                                                    elif self.newValues == 'values': 
                                                        self.ss = []
                                                        if self.master:
                                                            for s in self.master.items():
                                                                self.ss.append( s[ 1 ] )
                                                            self._return_ = self.ss.copy()
                                                        else: self.error = ERRORS( self.line ).ERROR24( )
                                                    elif self.value[ 0 ] is None: 
                                                        self.error = ERRORS( self.line ).ERROR15( self.function, [['type']] )  
                                                    else :  self.error =  ERRORS( self.line ).ERROR23( self.value[ 0 ] ) 
                                                else: self.error = ERRORS( self.line ).ERROR24( )
                                            else: self.error = ERRORS( self.line ).ERROR3( "name", 'a string()' )
                                        else: pass 
                                    else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                else: pass
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                    else: self.error = ERRORS( self.line ).ERROR15( self.function, [['type']] )
                else:
                    if self.value[ 0 ] is None: 
                        if  self.arguments[ 0 ] is not None:
                            self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase,self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues = self.final_val[ 0 ]
                                                if type( self.newValues ) == type( str() ):
                                                    if self.master:
                                                        if self.newValues == 'keys':
                                                            self._return_ = list( self.master.keys())
                                                        elif self.newValues == 'items': 
                                                            self._return_ = list( self.master.items() )
                                                        elif self.newValues == 'values': 
                                                            self.ss = []
                                                            if self.master:
                                                                for s in self.master.items():
                                                                    self.ss.append( s[ 1 ] )
                                                                self._return_ = self.ss.copy()
                                                            else: self.error = ERRORS( self.line ).ERROR24( )
                                                        elif self.arguments[ 0 ] is None: 
                                                            self.error = ERRORS( self.line ).ERROR15( self.function, [['type']] )  
                                                        else :  
                                                            self.error =  ERRORS( self.line ).ERROR23( self.value[ 0 ] ) 
                                                    else: self.error = ERRORS( self.line ).ERROR24( )
                                                else: self.error = ERRORS( self.line ).ERROR3( "name", 'a string()' )
                                            else: pass 
                                        else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass 
                        else: self.error = ERRORS( self.line ).ERROR15( self.function, [['type']] )
                    else: self.error =  ERRORS( self.line ).ERROR23( self.arguments[ 0 ] )             
            else: self.error = ERRORS( self.line ).ERROR12( self.function, 1)

        elif self.function in [ 'empty' ]            :
            if None in self.arguments: 
                if    self.master: self._return_ = False
                else: self._return_ = True
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        
        elif self.function in [ 'copy'  ]            :
            if None in self.arguments: self._return_ = self.master.copy()
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        
        elif self.function in [ 'clear' ]            :
            if None in self.arguments: self._return_ = self.master.clear()
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        
        elif self.function in [ 'remove']            :
            if len( self.arguments ) == 1: 
                if self.arguments[ 0 ] in [ 'key' ]:
                    if  self.value[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['name']] ) 
                    else:
                        if self.master:
                            self.dict_value, self.error = self.affectation.AFFECTATION( self.value[ 0 ],
                                                                    self.value[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase,self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues = self.final_val[ 0 ]
                                                if type( self.newValues ) == type( str() ):
                                                    if self.newValues in list( self.master.keys() ):
                                                        self._return_ = self.master.pop( self.newValues )
                                                    else: self.error = ERRORS( self.line ).ERROR25( self.value[ 0 ] )
                                                else: self.error = ERRORS( self.line ).ERROR3( "key", 'a string()' )
                                            else: pass 
                                        else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass
                        else: self.error = ERRORS( self.line ).ERROR24( )
                elif self.arguments[ 0 ] is None:  self.error = ERRORS( self.line ).ERROR15( self.function, [['key']] )
                else:
                    if self.value[ 0 ] is None :
                        if self.master:
                            self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                    self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase,self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues = self.final_val[ 0 ]
                                                if type( self.newValues ) == type( str() ):
                                                    if self.newValues in list( self.master.keys() ):
                                                        self._return_ = self.master.pop( self.newValues )
                                                    else: self.error = ERRORS( self.line ).ERROR25( self.arguments[ 0 ] )
                                                else: self.error = ERRORS( self.line ).ERROR3( "key", 'a string()' )
                                            else: pass 
                                        else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass                             
                        else: self.error = ERRORS( self.line ).ERROR24( )
                    else: ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )                   
            else: self.error = ERRORS( self.line ).ERROR12( self.function, 1)
               
        elif self.function in [ 'init'  ]            :
            if None in self.arguments: 
                self._return_ = {}
                self.idd =  self.DataBase[ 'variables' ][ 'vars' ].index( mainName )
                self.DataBase[ 'variables' ][ 'values' ][ self.idd ] = {}
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        
        return self._return_, self.error     
       
class LIST:
    def __init__(self, 
                DataBase    : dict, 
                line        : int, 
                master      : str, 
                function    : any, 
                FunctionInfo: list 
                ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        self.lexer          = main_lexer
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        
    def LIST(   self, mainName: str, mainString:  str )   :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
            
        if   self.function in [ 'empty' ]            :
            if None in self.arguments: 
                if    self.master: self._return_ = False
                else: self._return_ = True
            else: self.error = ERRORS( self.line ).ERROR14( self.function ) 
        elif self.function in [ 'copy'  ]            :
            if None in self.arguments: self._return_ = self.master.copy()
            else: self.error = ERRORS( self.line ).ERROR14( self.function ) 
        elif self.function in [ 'clear' ]            :
            if None in self.arguments: 
                self.master.clear()
                self._return_ =  self.master
            else: self.error = ERRORS( self.line ).ERROR14( self.function )      
        elif self.function in [ 'insert']            :
            self._return_, self.error = LIST( self.DataBase, self.line, self.master,
                                                self.function, [self.FunctionInfo] ).INSERT( mainName, mainString  )   
        elif self.function in ['sorted' ]            :
            self._return_, self.error = LIST( self.DataBase, self.line, self.master,
                                                self.function, [self.FunctionInfo] ).SOERTED( mainName, mainString )  
        elif self.function in [ 'size'  ]            :
            if None in self.arguments: 
                self._return_ = len( self.master )
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'init'  ]            :
            self._return_ = []
            self.idd =  self.DataBase[ 'variables' ][ 'vars' ].index( mainName )
            self.DataBase[ 'variables' ][ 'values' ][ self.idd ] = []
        elif self.function in [ 'choice']            :
            if None in self.arguments:
                if self.master:
                    self._return_ = random.choice( self.master )
                else: self.error = ERRORS( self.line ).ERROR24( 'list / tuple' )    
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'enumerate' ]        :
            if None in self.arguments:
                if self.master:
                    self._return_ = []
                    for i, value in enumerate( self.master ):
                        self._return_.append( (i, value) )
                else: self.error = ERRORS( self.line ).ERROR24( 'list' )    
            else: self.error = ERRORS( self.line ).ERROR14( self.function )      
        elif self.function in ['random', 'rand' ]    :
            if self.function == 'random':
                self._return_, self.error = LIST( self.DataBase, self.line, self.master,
                                                 self.function, [self.FunctionInfo] ).RANDOM( mainName, mainString ) 
            else:
                self._return_, self.error = LIST( self.DataBase, self.line, self.master,
                                                 self.function, [self.FunctionInfo] ).RANDOM( mainName, mainString, 'float' ) 
        elif self.function in [ 'count', 'index', 'remove', 'add', 'round' ]   :
            if len( self.arguments ) == 1: 
                if self.arguments[ 0 ] in [ 'master' ]:
                    if  self.value[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                    else:
                        self.dict_value, self.error = self.affectation.AFFECTATION(self.value[ 0 ],
                                                                self.value[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                        if self.error is None:
                            if 'operator' not in list( self.dict_value.keys() ): 
                                self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                            self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                if self.error is None: 
                                    self.all_data = self.lex[ 'all_data' ]
                                    if self.all_data is not None:
                                        self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                        if self.error is None:
                                            if   self.function in [ 'count', 'index' ]:
                                                try:
                                                    if self.function in [ 'count' ]:
                                                        self._return_ = self.master.count( self.final_val[ 0 ] )
                                                    else: 
                                                        try: self._return_ = self.master.index( self.final_val[ 0 ] )
                                                        except ValueError : self.error = ERRORS( self.line ).ERROR27( self.value[ 0 ] )
                                                except ValueError: self.error = ERRORS( self.line ).ERROR27( self.value[ 0 ] )
                                            elif self.function in [ 'remove' ]:
                                                if type( self.final_val[ 0 ] ) == type( int() ):
                                                    try: 
                                                        del self.master[ self.final_val[ 0 ] ]
                                                        self._return_ = self.master[ : ]
                                                    except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                                                else: self.error = ERRORS( self.line ).ERROR3( "master" )
                                            elif self.function in [ 'insert' ]:
                                                if type( self.final_val[ 0 ] ) == type( tuple() ):
                                                    try: 
                                                        if len( self.final_val[ 0 ] ) == 2:
                                                            if type( self.final_val[ 0 ][ 0 ] ) == type( int() ) :
                                                                self.master.insert( self.final_val[ 0 ][ 0 ], self.final_val[ 0 ][ 1 ] )
                                                                self._return_ = self.master[ : ]
                                                            else: self.error = ERRORS( self.line ).ERROR3( "master[ 0 ]" )
                                                        else: self.error = ERRORS( self.line ).ERROR29()
                                                    except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                                                else: self.error = ERRORS( self.line ).ERROR3( "master", 'a tuple()' )
                                            elif self.function in [ 'add'    ]:
                                                self.master.append( self.final_val[ 0 ] )
                                                self._return_ = self.master[ : ]
                                            elif self.function in [ 'round'  ]:
                                                self.new = self.master[ : ]
                                                if type( self.final_val[ 0 ] ) == type( int() ) :
                                                    if self.final_val[ 0 ] >= 0:
                                                        if self.master:
                                                            for i in range( len( self.master)):
                                                                if type( self.master[ i ]) in [ type(int()), type(float()), type(bool())]:
                                                                    self.new.append( round( self.master[ i ], self.final_val[0]) )
                                                                else: 
                                                                    self.master = self.new
                                                                    self.error = ERRORS( self.line ).ERROR35( i )
                                                                    break
                                                            self._return_ = self.new
                                                            
                                                        else: self.error = ERRORS( self.line ).ERROR24( 'list')
                                                    else: self.error = ERRORS( self.line ).ERROR34( 'master')
                                                else: self.error = ERRORS( self.line ).ERROR3( 'master' )
                                        else: pass
                                    else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                else: pass 
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                elif self.arguments[ 0 ] is None:  self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] )
                else:
                    if self.value[ 0 ] is None :
                        self.dict_value, self.error = self.affectation.AFFECTATION(self.arguments[ 0 ],
                                                                self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                        if self.error is None:
                            if 'operator' not in list( self.dict_value.keys() ): 
                                self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                            self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                if self.error is None: 
                                    self.all_data = self.lex[ 'all_data' ]
                                    if self.all_data is not None:
                                        self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase, self.line).ANALYSE( mainString )
                                        if self.error is None:
                                            if   self.function in [ 'count', 'index' ]  :
                                                #if type( self.final_val[ 0 ] ) == type( str() ):
                                                try:
                                                    if self.function in [ 'count' ]:
                                                        self._return_ = self.master.count( self.final_val[ 0 ] )
                                                    else: 
                                                        try: self._return_ = self.master.index( self.final_val[ 0 ] )
                                                        except ValueError : self.error = ERRORS( self.line ).ERROR27( self.arguments[ 0 ] )
                                                except ValueError : self.error = ERRORS( self.line ).ERROR27( self.value[ 0 ] )
                                            elif self.function in [ 'remove' ]          :
                                                if type( self.final_val[ 0 ] ) == type( int() ):
                                                    try: 
                                                        del self.master[ self.final_val[ 0 ] ]
                                                        self._return_ = self.master[ : ]
                                                    except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                                                else: self.error = ERRORS( self.line ).ERROR3( "master" )
                                            elif self.function in [ 'add' ]             :
                                                self.master.append( self.final_val[ 0 ] )
                                                self._return_ = self.master[ : ]
                                            elif self.function in [ 'round'  ]          :
                                                self.new = []
                                                if type( self.final_val[ 0 ] ) == type( int() ) :
                                                    if self.final_val[ 0 ] >= 0:
                                                        if self.master:
                                                            for i in range( len( self.master)):
                                                                if type( self.master[ i ]) in [ type(int()), type(float()), type(bool())]:
                                                                    self.new.append( round( self.master[ i ], self.final_val[0]) )
                                                                else: 
                                                                    self.master = self.new
                                                                    self.error = ERRORS( self.line ).ERROR35( i )
                                                                    break
                                                            self._return_ = self.new
                                                            
                                                        else: self.error = ERRORS( self.line ).ERROR24( 'list')
                                                    else: self.error = ERRORS( self.line ).ERROR34( 'master')
                                                else: self.error = ERRORS( self.line ).ERROR3( 'master' )
                                        else: pass
                                else: pass 
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                    else: ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
            else: self.error = ERRORS( self.line ).ERROR12( self.function, 1)                   
        
        return self._return_, self.error  
            
    def INSERT (self, mainName: str, mainString:  str)    :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 

        if len( self.arguments ) == 2:
            if   self.arguments[ 0 ] == 'pos'   :
                if   self.arguments[ 1 ] == 'master'    : 
                    if   self.value[ 0 ]    is None  and self.value[ 1 ] is not None :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['pos']] ) 
                    elif self.value[ 1 ]    is None  and self.value[ 0 ] is not None :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] )
                    elif self.value[ 0 ]    is None  and self.value[ 1 ] is None     :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['pos'], ['master']] )
                    else: 
                        self.newValues = []
                        for value in self.value:
                            self.dict_value, self.error = self.affectation.AFFECTATION(value,
                                                                    value, self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase,self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues.append( self.final_val[ 0 ] )
                                            else: pass 
                                        else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass

                        if self.error is None:
                            try: 
                                if type( self.newValues[ 0 ] ) == type( int() ) :
                                    self.master.insert( self.newValues[ 0 ], self.newValues[ 1 ])
                                    self._return_ = self.master[ : ]
                                    del self.newValues
                                else: self.error = ERRORS( self.line ).ERROR3( "pos" )
                            except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                        else: pass      
                elif self.arguments[ 1 ] == 'pos'       : 
                    self.error = ERRORS( self.line ).ERROR16( self.function, 'pos')
                else:
                    if self.value[ 1 ] is None :
                        if self.value[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['pos']] ) 
                        else:
                            self.newValues = []
                            self.allValues = [ self.value[ 0 ], self.arguments[ 1 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION( value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ): 
                                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None: 
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                    self.DataBase, self.line).ANALYSE( mainString )
                                                if self.error is None:
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                        else: pass 
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass 
                            
                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( int() ) :
                                        self.master.insert( self.newValues[ 0 ], self.newValues[ 1 ])
                                        self._return_ = self.master[ : ]
                                        del self.newValues
                                        del self.allValues
                                    else: self.error = ERRORS( self.line ).ERROR3( "pos" )
                                except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                            else: pass   
                    else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )
                    
            elif self.arguments[ 0 ] == 'master': 
                if   self.arguments[ 1 ] == 'pos'       : 
                    if   self.value[ 0 ]    is None  and self.value[ 1 ] is not None :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                    elif self.value[ 1 ]    is None  and self.value[ 0 ] is not None :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['pos']] )
                    elif self.value[ 0 ]    is None  and self.value[ 1 ] is None     :  
                        self.error = ERRORS( self.line ).ERROR15( self.function, [['pos'], ['master']] )
                    else: 
                        self.newValues = []
                        for value in self.value:
                            self.dict_value, self.error = self.affectation.AFFECTATION(value,
                                                                    value, self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase,self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues.append( self.final_val[ 0 ] )
                                            else: pass 
                                        else: pass 
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass

                        if self.error is None:
                            try: 
                                if type( self.newValues[ 1 ] ) == type( int() ) :
                                    self.master.insert( self.newValues[ 1 ], self.newValues[ 0 ])
                                    self._return_ = self.master[ : ]
                                    del self.newValues
                                else: self.error = ERRORS( self.line ).ERROR3( "pos" )
                            except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                        else: pass
                elif self.arguments[ 1 ] == 'master'    :
                    self.error = ERRORS( self.line ).ERROR16( self.function, 'master')
                else:
                    if self.value[ 1 ] is None :
                        if self.value[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                        else:
                            self.newValues = []
                            self.allValues = [ self.arguments[ 1 ], self.value[ 0 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION( value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ): 
                                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None: 
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                    self.DataBase, self.line).ANALYSE( mainString )
                                                if self.error is None:
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                                        else: pass 
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass 
                            
                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( int() ) :
                                        self.master.insert( self.newValues[ 0 ], self.newValues[ 1 ])
                                        self._return_ = self.master[ : ]
                                        del self.newValues
                                        del self.allValues
                                    else: self.error = ERRORS( self.line ).ERROR3( "pos" )
                                except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                            else: pass   
                    else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )
            
            else:
                if self.value[ 0 ] is None: 
                    if self.arguments[ 1 ] == 'master': 
                        if self.value[ 1 ] is None  : self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                        else: 
                            self.newValues = []
                            self.allValues = [ self.arguments[ 0 ], self.value[ 1 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION(value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ): 
                                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None: 
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                self.DataBase,self.line).ANALYSE( mainString )
                                                if self.error is None:
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                                        else: pass
                                    else: 
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass

                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( int() ) :
                                        self.master.insert( self.newValues[ 0 ], self.newValues[ 1 ])
                                        self._return_ = self.master[ : ]
                                        del self.newValues
                                        del self.allValues
                                    else: self.error = ERRORS( self.line ).ERROR3( "pos" )
                                except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                            else: pass
                    else:
                        if self.value[ 1 ] is None :
                            self.newValues = []
                            self.allValues = [ self.arguments[ 0 ], self.arguments[ 1 ] ]
                            for value in self.allValues:
                                self.dict_value, self.error = self.affectation.AFFECTATION( value,
                                                                        value, self.DataBase, self.line ).DEEP_CHECKING()
                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ): 
                                        self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                    self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None: 
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                    self.DataBase, self.line).ANALYSE( mainString )
                                                if self.error is None:
                                                    self.newValues.append( self.final_val[ 0 ] )
                                                else: pass 
                                            else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                        else: pass 
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                                else: pass 
                            
                            if self.error is None:
                                try: 
                                    if type( self.newValues[ 0 ] ) == type( int() ) :
                                        self.master.insert( self.newValues[ 0 ], self.newValues[ 1 ])
                                        self._return_ = self.master[ : ]
                                        del self.newValues
                                        del self.allValues
                                    else: self.error = ERRORS( self.line ).ERROR3( "pos" )
                                except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                            else: pass   
                        else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 1 ] )
                else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else:  self.error = ERRORS( self.line ).ERROR12( self.function, 2)

        return self._return_, self.error 
      
    def SOERTED(self, mainName: str, mainString:  str)    :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'reverse': 
                if self.value[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['reverse']] ) 
                else: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.value[ 0 ],
                                                                    self.value[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if type( self.newValues ) == type( bool() ):
                                            if self.master:
                                                try:
                                                    self._return_   = sorted( self.master , reverse=self.newValues)
                                                    self.master     = self._return_
                                                except TypeError:
                                                    for i in range( len( self.master )):
                                                        if type( self.master[i]) not in [ type(float()), type(int()), type(bool())]:
                                                            self.error = ERRORS( self.line ).ERROR35( i )
                                                            break
                                                        else: pass
                                            else: self.error = ERRORS( self.line ).ERROR24( 'list' )
                                        else: self.error = ERRORS( self.line ).ERROR3( "reverse", 'a boolean()')   
                                    else: pass 
                                else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            else:
                if self.arguments[ 0 ] is None:
                    if self.master:
                        try:
                            self._return_   = sorted( self.master , reverse=False)
                            self.master     = self._return_
                        except TypeError:
                            for i in range( len( self.master )):
                                if type( self.master[i]) not in [ type(float()), type(int()), type(bool())]:
                                    self.error = ERRORS( self.line ).ERROR35( i )
                                    break
                            else: pass
                    else: self.error = ERRORS( self.line ).ERROR24( 'list' )
                else:
                    if self.value[ 0 ] is None:
                        if self.master:
                            self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                    self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase,self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues = self.final_val[ 0 ]
                                                if type( self.newValues ) == type( bool() ):
                                                    if self.master:
                                                        try:
                                                            self._return_   = sorted( self.master , reverse=self.newValues)
                                                            self.master     = self._return_
                                                        except TypeError:
                                                            for i in range( len( self.master )):
                                                                if type( self.master[i]) not in [ type(float()), type(int()), type(bool())]:
                                                                    self.error = ERRORS( self.line ).ERROR35( i )
                                                                    break
                                                                else: pass
                                                    else: self.error = ERRORS( self.line ).ERROR24( 'list' )
                                                else: self.error = ERRORS( self.line ).ERROR3( "reverse", 'a boolean()')   
                                            else: pass 
                                        else: self.error = ERRORS( self.line ).ERROR0( mainString ) 
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass
                        else: self.error = ERRORS( self.line ).ERROR24( 'list' )
                    else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error
        
    def RANDOM (self, 
                mainName    : str, 
                mainString  : str, 
                typ         : str = 'normal'
                )    :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'numeric': 
                if self.value[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['numeric']] ) 
                else: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.value[ 0 ],
                                                                    self.value[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if type( self.newValues ) == type( int() ):
                                            if abs( self.newValues ) > 0:
                                                self.matrix = []
                                                for i in range( abs( self.newValues ) ):
                                                    if typ == 'normal':
                                                        if  self.newValues > 0:
                                                            self.matrix.append( random.randint( 0, self.newValues ) )
                                                        else:
                                                            self.matrix.append( random.randint( self.newValues, 0 ) )
                                                    else:
                                                        if  self.newValues > 0:
                                                            self.matrix.append( random.random( ) )
                                                        else:
                                                            self.matrix.append( - random.random( ) )
                                                        
                                                self._return_   = self.matrix
                                                if mainName == 'list.': pass 
                                                else:
                                                    self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                    self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_ 
                                            else: self.error = ERRORS( self.line ).ERROR30()
                                        elif type( self.newValues ) == type( tuple() ):
                                            try:
                                                if len( self.newValues ) == 2:
                                                    self.n, self.m = self.newValues[0], self.newValues[1]
                                                    if type( self.n ) == type( int() ):                 
                                                        if type(self.m) == type( int() ):
                                                            if self.n > 0:
                                                                if  abs( self.m ) > 0:
                                                                    self.matrix = []
                                                                    for i in range( abs( self.n ) ):
                                                                        if typ == 'normal':
                                                                            if  self.m > 0:  self.matrix.append( random.randint( 0, self.m ) )
                                                                            else:  self.matrix.append( random.randint( self.m, 0 ) )
                                                                        else: self.error = ERRORS( self.line ).ERROR3( )
                                                                    
                                                                    if self.error is None:
                                                                        self._return_   = self.matrix
                                                                        if mainName == 'list.': pass 
                                                                        else:
                                                                            self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                                            self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_
                                                                    else: pass
                                                                else: self.error = ERRORS( self.line ).ERROR30( s= 'max_num')
                                                            else: self.error = ERRORS( self.line ).ERROR47( ) 
                                                        elif type(self.m) == type( tuple() ):
                                                            if self.n > 0:
                                                                if len(self.m) == 2: 
                                                                    if type(self.m[0]) == type( int() ):
                                                                        if type(self.m[1]) == type(int()):
                                                                            if self.m[0] != self.m[1]: 
                                                                                self.matrix = []
                                                                                for i in range( abs( self.n ) ):
                                                                                    if typ == 'normal':
                                                                                        self.matrix.append( random.randint( min(self.m), max(self.m) ) )
                                                                                    else: self.error = ERRORS( self.line ).ERROR3( )
                                                                                
                                                                                if self.error is None:
                                                                                    self._return_   = self.matrix
                                                                                    if mainName == 'list.': pass 
                                                                                    else:
                                                                                        self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                                                        self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_
                                                                                else: pass
                                                                            else: self.error = ERRORS( self.line ).ERROR48( )
                                                                        else: self.error = ERRORS( self.line ).ERROR3( "max_num2" )
                                                                    else: self.error = ERRORS( self.line ).ERROR3( "max_num1" )
                                                                else: self.error = ERRORS( self.line ).ERROR29( "max_num" )
                                                            else: self.error = ERRORS( self.line ).ERROR47( ) 
                                                        else: self.error = ERRORS( self.line ).ERROR3( "max_num" ) 
                                                    else: self.error = ERRORS( self.line ).ERROR3( "max_step" ) 
                                                else : self.error = ERRORS( self.line ).ERROR29( "numeric" )
                                            except IndexError : pass
                                        else: self.error = ERRORS( self.line ).ERROR49( "numeric" )  
                                    else: pass
                                else: self.error = ERRORS( self.line ).ERROR0( mainString )
                            else: pass
                        else: 
                            self.operator   = self.dict_value[ 'operator' ]
                            self.error      = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            elif self.arguments[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['numeric']] ) 
            else: 
                if self.value[ 0 ] is None: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                    self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if   type( self.newValues ) == type( int() ):
                                            if abs( self.newValues ) > 0:
                                                self.matrix = []
                                                for i in range( abs( self.newValues ) ):
                                                    if typ == 'normal':
                                                        if  self.newValues > 0:
                                                            self.matrix.append( random.randint( 0, self.newValues ) )
                                                        else:
                                                            self.matrix.append( random.randint( self.newValues, 0 ) )
                                                    else:
                                                        if  self.newValues > 0:
                                                            self.matrix.append( random.random( ) )
                                                        else:
                                                            self.matrix.append( - random.random( ) )
                                                self._return_   = self.matrix
                                                if mainName == 'list.': pass 
                                                else:
                                                    self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                    self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_ 
                                            else: self.error = ERRORS( self.line ).ERROR30()
                                        elif type( self.newValues ) == type( tuple() ):
                                            try:
                                                if len( self.newValues ) == 2:
                                                    self.n, self.m = self.newValues[0], self.newValues[1]
                                                    if type( self.n ) == type( int() ):                 
                                                        if type(self.m) == type( int() ):
                                                            if self.n > 0:
                                                                if  abs( self.m ) > 0:
                                                                    self.matrix = []
                                                                    for i in range( abs( self.n ) ):
                                                                        if typ == 'normal':
                                                                            if  self.m > 0:  self.matrix.append( random.randint( 0, self.m ) )
                                                                            else:  self.matrix.append( random.randint( self.m, 0 ) )
                                                                        else: self.error = ERRORS( self.line ).ERROR3( )
                                                                    
                                                                    if self.error is None:
                                                                        self._return_   = self.matrix
                                                                        if mainName == 'list.': pass 
                                                                        else:
                                                                            self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                                            self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_
                                                                    else: pass
                                                                else: self.error = ERRORS( self.line ).ERROR30( s= 'max_num')
                                                            else: self.error = ERRORS( self.line ).ERROR47( ) 
                                                        elif type(self.m) == type( tuple() ):
                                                            if self.n > 0:
                                                                if len(self.m) == 2: 
                                                                    if type(self.m[0]) == type( int() ):
                                                                        if type(self.m[1]) == type(int()):
                                                                            if self.m[0] != self.m[1]: 
                                                                                self.matrix = []
                                                                                for i in range( abs( self.n ) ):
                                                                                    if typ == 'normal':
                                                                                        self.matrix.append( random.randint( min(self.m), max(self.m) ) )
                                                                                    else: self.error = ERRORS( self.line ).ERROR3( )
                                                                                
                                                                                if self.error is None:
                                                                                    self._return_   = self.matrix
                                                                                    if mainName == 'list.': pass 
                                                                                    else:
                                                                                        self.idd = self.DataBase['variables'][ 'vars' ].index( mainName )
                                                                                        self.DataBase['variables'][ 'values' ][ self.idd ] = self._return_
                                                                                else: pass
                                                                            else: self.error = ERRORS( self.line ).ERROR48( )
                                                                        else: self.error = ERRORS( self.line ).ERROR3( "max_num2" )
                                                                    else: self.error = ERRORS( self.line ).ERROR3( "max_num1" )
                                                                else: self.error = ERRORS( self.line ).ERROR29( "max_num" )
                                                            else: self.error = ERRORS( self.line ).ERROR47( ) 
                                                        else: self.error = ERRORS( self.line ).ERROR3( "max_num" ) 
                                                    else: self.error = ERRORS( self.line ).ERROR3( "max_step" ) 
                                                else : self.error = ERRORS( self.line ).ERROR29( "numeric" )
                                            except IndexError : pass
                                        else: self.error = ERRORS( self.line ).ERROR49( "numeric" )   
                                    else: pass
                                else: self.error = ERRORS( self.line ).ERROR0( mainString )
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
                else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error

class TUPLE:
    def __init__(self, 
                DataBase    : dict, 
                line        : int, 
                master      : str, 
                function    : any, 
                FunctionInfo: list 
                ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        self.lexer          = main_lexer
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        
    def TUPLE( self, mainName: str = '', mainString : str = '' ):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if   self.function in [ 'empty' ]            :
            if None in self.arguments: 
                if    self.master: self._return_ = False
                else: self._return_ = True
            else: self.error = ERRORS( self.line ).ERROR14( self.function ) 
        elif self.function in [ 'init'  ]            :
            if None in self.arguments:
                self._return_ = ()
                self.idd =  self.DataBase[ 'variables' ][ 'vars' ].index( mainName )
                self.DataBase[ 'variables' ][ 'values' ][ self.idd ] = ()
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'size'  ]            :
            if None in self.arguments: 
                self._return_ = len( self.master )
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'enumerate' ]        :
            if None in self.arguments:
                if self.master:
                    self._return_ = []
                    for i, value in enumerate( self.master ):
                        self._return_.append( (i, value) )
                    self._return_ = tuple( self._return_ )
                else: self.error = ERRORS( self.line ).ERROR24( 'tuple' )    
            else: self.error = ERRORS( self.line ).ERROR14( self.function )  
        elif self.function in [ 'choice']            :
            if None in self.arguments:
                if self.master:
                    self._return_ = random.choice( self.master )
                else: self.error = ERRORS( self.line ).ERROR24( 'list / tuple' )    
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in ['count', 'index']     :
            if len( self.arguments ) == 1: 
                if self.arguments[ 0 ] in [ 'master' ]:
                    if  self.value[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                    else:
                        self.dict_value, self.error = self.affectation.AFFECTATION(self.value[ 0 ],
                                                                self.value[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                        if self.error is None:
                            if 'operator' not in list( self.dict_value.keys() ): 
                                self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                            self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                if self.error is None: 
                                    self.all_data = self.lex[ 'all_data' ]
                                    if self.all_data is not None:
                                        self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                        if self.error is None:
                                            if   self.function in [ 'count', 'index' ]:
                                                try:
                                                    if self.function in [ 'count' ]:
                                                        self._return_ = self.master.count( self.final_val[ 0 ] )
                                                    else: 
                                                        try: self._return_ = self.master.index( self.final_val[ 0 ] )
                                                        except ValueError : self.error = ERRORS( self.line ).ERROR27( self.value[ 0 ], 'tuple' )
                                                except ValueError: self.error = ERRORS( self.line ).ERROR27( self.value[ 0 ], 'tuple' )
                                            elif self.function in [ 'remove' ]:
                                                if type( self.final_val[ 0 ] ) == type( int() ):
                                                    try: 
                                                        del self.master[ self.final_val[ 0 ] ]
                                                        self._return_ = self.master[ : ]
                                                    except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                                                else: self.error = ERRORS( self.line ).ERROR3( "master" )
                                            elif self.function in [ 'insert' ]:
                                                if type( self.final_val[ 0 ] ) == type( tuple() ):
                                                    try: 
                                                        if len( self.final_val[ 0 ] ) == 2:
                                                            if type( self.final_val[ 0 ][ 0 ] ) == type( int() ) :
                                                                self.master.insert( self.final_val[ 0 ][ 0 ], self.final_val[ 0 ][ 1 ] )
                                                                self._return_ = self.master[ : ]
                                                            else: self.error = ERRORS( self.line ).ERROR3( "master[ 0 ]" )
                                                        else: self.error = ERRORS( self.line ).ERROR29()
                                                    except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                                                else: self.error = ERRORS( self.line ).ERROR3( "master", 'a tuple()' )
                                            elif self.function in [ 'add'    ]:
                                                self.master.append( self.final_val[ 0 ] )
                                                self._return_ = self.master[ : ]
                                            elif self.function in [ 'round'  ]:
                                                self.new = self.master[ : ]
                                                if type( self.final_val[ 0 ] ) == type( int() ) :
                                                    if self.final_val[ 0 ] >= 0:
                                                        if self.master:
                                                            for i in range( len( self.master)):
                                                                if type( self.master[ i ]) in [ type(int()), type(float()), type(bool())]:
                                                                    self.new.append( round( self.master[ i ], self.final_val[0]) )
                                                                else: 
                                                                    self.master = self.new
                                                                    self.error = ERRORS( self.line ).ERROR35( i )
                                                                    break
                                                            self._return_ = self.new
                                                            
                                                        else: self.error = ERRORS( self.line ).ERROR24( 'list')
                                                    else: self.error = ERRORS( self.line ).ERROR34( 'master')
                                                else: self.error = ERRORS( self.line ).ERROR3( 'master' )
                                        else: pass
                                    else: self.error = ERRORS( self.line ).ERROR0( mainString )
                                else: pass 
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                elif self.arguments[ 0 ] is None:  self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] )
                else:
                    if self.value[ 0 ] is None :
                        self.dict_value, self.error = self.affectation.AFFECTATION(self.arguments[ 0 ],
                                                                self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                        if self.error is None:
                            if 'operator' not in list( self.dict_value.keys() ): 
                                self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                            self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                if self.error is None: 
                                    self.all_data = self.lex[ 'all_data' ]
                                    if self.all_data is not None:
                                        self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase, self.line).ANALYSE( mainString )
                                        if self.error is None:
                                            if   self.function in [ 'count', 'index' ]  :
                                                try:
                                                    if self.function in [ 'count' ]:
                                                        self._return_ = self.master.count( self.final_val[ 0 ] )
                                                    else: 
                                                        try: self._return_ = self.master.index( self.final_val[ 0 ] )
                                                        except ValueError : self.error = ERRORS( self.line ).ERROR27( self.arguments[ 0 ], 'tuple' )
                                                except ValueError: self.error = ERRORS( self.line ).ERROR27( self.value[ 0 ], 'tuple' )
                                            elif self.function in [ 'remove' ]          :
                                                if type( self.final_val[ 0 ] ) == type( int() ):
                                                    try: 
                                                        del self.master[ self.final_val[ 0 ] ]
                                                        self._return_ = self.master[ : ]
                                                    except IndexError : self.error = ERRORS( self.line ).ERROR28( )
                                                else: self.error = ERRORS( self.line ).ERROR3( "master" )
                                            elif self.function in [ 'add' ]             :
                                                self.master.append( self.final_val[ 0 ] )
                                                self._return_ = self.master[ : ]
                                            elif self.function in [ 'round'  ]          :
                                                self.new = []
                                                if type( self.final_val[ 0 ] ) == type( int() ) :
                                                    if self.final_val[ 0 ] >= 0:
                                                        if self.master:
                                                            for i in range( len( self.master)):
                                                                if type( self.master[ i ]) in [ type(int()), type(float()), type(bool())]:
                                                                    self.new.append( round( self.master[ i ], self.final_val[0]) )
                                                                else: 
                                                                    self.master = self.new
                                                                    self.error = ERRORS( self.line ).ERROR35( i )
                                                                    break
                                                            self._return_ = self.new
                                                            
                                                        else: self.error = ERRORS( self.line ).ERROR24( 'list')
                                                    else: self.error = ERRORS( self.line ).ERROR34( 'master')
                                                else: self.error = ERRORS( self.line ).ERROR3( 'master' )
                                        else: pass
                                else: pass 
                            else: 
                                self.operator = self.dict_value[ 'operator' ]
                                self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                        else: pass
                    else: ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
            else: self.error = ERRORS( self.line ).ERROR12( self.function, 1)                   
             
        return self._return_, self.error  
    
class CPLX:
    def __init__(self, DataBase: dict, line:int, master: str, function: any, FunctionInfo : list ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        
    def CPLX( self ):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
         
        if   self.function in [ 'img'  ]      :
            if None in self.arguments: 
                self._return_ = self.master.imag
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'real' ]      :
            if None in self.arguments: 
                self._return_ = self.master.real
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'norm' ]      :
            if None in self.arguments:
                self.real = self.master.real
                self.img  = self.master.imag 
                self._return_ = (self.real ** 2 + self.img ** 2) ** (0.5)   
            else: self.error = ERRORS( self.line ).ERROR14( self.function )  
        elif self.function in [ 'conj' ]      :
            if None in self.arguments: 
                img = self.master.imag
                real= self.master.real 
                c = str(real) + '-' + str(img) + 'j'
                self._return_ = complex( c )
            else: self.error = ERRORS( self.line ).ERROR14( self.function )
        
        return self._return_, self.error 
   
class READFILE:
    def __init__(self, DataBase: dict, line:int, master: str, function: any, FunctionInfo : list ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        self.lexer          = main_lexer
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        
    def READFILE( self, mainName: str = '', mainString: str = '' ):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        self.fileS          = []

        try:
            if   self.function in [ 'readlines'  ]              :
                self._return_, self.error = READFILE(self.DataBase, self.line, self.master, self.function,
                                                        [self.FunctionInfo]).READLINE( mainName, mainString )
                if self.error is None:
                    try:
                        if self.master[ 2 ] in [ 'r' ]:
                            if self._return_ is not None:
                                if self.master[ 4 ] is None:
                                    with open( self.master[ 1 ], self.master[ 2 ]) as file:
                                        for line in file.readlines( self._return_ ):
                                            self.fileS.append( line.rstrip() )
                                else:
                                    with open( self.master[ 1 ], self.master[ 2 ], encoding=self.master[4], errors='surrogateescape') as file:
                                        for line in file.readlines( self._return_ ):
                                            self.fileS.append( line.rstrip() )
                            else:
                                if self.master[ 4 ] is None:
                                    with open( self.master[ 1 ], self.master[ 2 ]) as file:
                                        for line in file.readlines():
                                            self.fileS.append( line.rstrip() )
                                else:
                                    with open( self.master[ 1 ], self.master[ 2 ], encoding=self.master[4], errors='surrogateescape') as file:
                                        for line in file.readlines( self._return_ ):
                                            self.fileS.append( line.rstrip() )
                                            
                            self._return_ = self.fileS
                        else: self.error = ERRORS( self.line ).ERROR37( self.master[ 1 ], self.master[ 2 ] ) 
                    except FileNotFoundError: self.error = ERRORS( self.line ).ERROR36( self.master[ 1 ])  
                else: pass            
            elif self.function in [ 'write', 'writeline'  ]     :
                if self.master[ 2 ] in [ 'w' ] :
                    self.__return__, self.error = READFILE(self.DataBase, self.line, self.master, self.function,
                                                        [self.FunctionInfo]).WRITELINE( mainName, mainString )
                    if self.error is None:
                        if self.master[ 3 ] == 'old': self.master[ 2 ] = 'a'
                        else: pass
                        
                        file = open( self.master[ 1 ], self.master[ 2 ])
                        file.write( self.__return__ )
                        self.DataBase[ 'no_printed_values' ].append( None )
                    else: pass
                else: self.error = ERRORS( self.line ).ERROR37( self.master[ 1 ], self.master[ 2 ] ) 
            elif self.function in [ 'writelines'  ]             :
                if self.master[ 2 ] in [ 'w' ] :
                    self.__return__, self.error = READFILE(self.DataBase, self.line, self.master, self.function,
                                                        [self.FunctionInfo]).WRITELINE( mainName, mainString, 'list' )
                    if self.error is None:
                        if self.master[ 3 ] == 'old': self.master[ 2 ] = 'a'
                        else: pass
                        
                        file = open( self.master[ 1 ], self.master[ 2 ])
                        try:
                            if self.__return__ :
                                file.writelines( self.__return__ )
                            else: self.error = ERRORS( self.line ).ERROR24( 'list' )
                        except TypeError:
                            if self.self.__return__:
                                for l, _str_ in enumerate( self.__return__ ):
                                    if type( _str_ ) in [ type(str())] : pass 
                                    else: 
                                        self.error = ERRORS( self.line ).ERROR38( l )
                                        break
                            else: pass
                        self.DataBase[ 'no_printed_values' ].append( None )
                    else: pass
                else: self.error = ERRORS( self.line ).ERROR37( self.master[ 1 ], self.master[ 2 ] ) 
            elif self.function in [ 'readline', 'read' ]        :
                if self.master[ 2 ] in [ 'r' ]:
                    self._return_, self.error = READFILE(self.DataBase, self.line, self.master, self.function,
                                                        [self.FunctionInfo]).READLINE( mainName, mainString )
                    if self.error is None:
                        try:
                            file = open( self.master[ 1 ], self.master[ 2 ])
                            if self._return_ is not None:
                                self._return_ = file.readline( self._return_ )
                            else: self._return_ = file.readline() 
                        except FileNotFoundError: self.error = ERRORS( self.line ).ERROR36( self.master[ 1 ])
                    else: pass 
                else: self.error = ERRORS( self.line ).ERROR37( self.master[ 1 ], self.master[ 2 ] ) 
            elif self.function in [ 'close' ]:
                if None in self.arguments:
                    self.DataBase[ 'no_printed_values' ].append( None )
                    if mainName in self.DataBase[ 'open' ]['nonCloseKey']:
                        self.idd = self.DataBase[ 'open' ]['nonCloseKey'].index( mainName )
                        del self.DataBase[ 'open' ]['nonCloseKey'][ self.idd ]
                        del self.DataBase[ 'open' ]['name'][ self.idd ]
                        del self.DataBase[ 'open' ]['file'][ self.idd ]
                        del self.DataBase[ 'open' ]['action'][ self.idd ]
                        del self.DataBase[ 'open' ]['status'][ self.idd ]
                        del self.DataBase[ 'open' ]['encoding'][ self.idd ]
                    else: pass
                else: self.error = ERRORS( self.line ).ERROR14( self.function )
        
        except UnicodeDecodeError   : self.error = ERRORS( self.line ).ERROR40() 
        except UnicodeEncodeError   : self.error = ERRORS( self.line ).ERROR39()
        except UnicodeError         : self.error = ERRORS( self.line ).ERROR41() 
             
        return self._return_, self.error 
    
    def READLINE (self, mainName: str, mainString:  str)    :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'numeric': 
                if self.value[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['numeric']] ) 
                else: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.value[ 0 ],
                                                                    self.value[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if type( self.newValues ) == type( int() ):
                                            if self.newValues  >= 0:
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = ERRORS( self.line ).ERROR30()
                                        else: self.error = ERRORS( self.line ).ERROR3( "numeric" )   
                                    else: pass
                                else: self.error = ERRORS( self.line ).ERROR0( mainString )
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            elif self.arguments[ 0 ] is None: self._return_ = None
            else: 
                if self.value[ 0 ] is None: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                    self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if type( self.newValues ) == type( int() ):
                                            if self.newValues >= 0:
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = ERRORS( self.line ).ERROR30()
                                        else: self.error = ERRORS( self.line ).ERROR3( "numeric" )   
                                    else: pass
                                else: self.error = ERRORS( self.line ).ERROR0( mainString )
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
                else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error
    
    def WRITELINE (self, mainName: str, mainString:  str, typ : str = 'str')   :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'master': 
                if self.value[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                else: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.value[ 0 ],
                                                                    self.value[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if typ == 'str':
                                            if type( self.newValues ) == type( str() ):
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = ERRORS( self.line ).ERROR3( "master", ' a string()' )   
                                        elif typ == 'list':
                                            if type( self.newValues ) == type( list() ):
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = ERRORS( self.line ).ERROR3( "master", ' a list()' )  
                                    else: pass
                                else: self.error = ERRORS( self.line ).ERROR0( mainString )
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            elif self.arguments[ 0 ] is None: self.error = ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
            else: 
                if self.value[ 0 ] is None: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                    self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if typ == 'str':
                                            if type( self.newValues ) == type( str() ):
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = ERRORS( self.line ).ERROR3( "master", ' a string()' )   
                                        elif typ == 'list':
                                            if type( self.newValues ) == type( list() ):
                                                self._return_ = self.final_val[ 0 ]
                                            else: self.error = ERRORS( self.line ).ERROR3( "master", ' a list()' )  
                                    else: pass
                                else: self.error = ERRORS( self.line ).ERROR0( mainString )
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
                else: self.error = ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error
    
class ININHERITANCE:
    def __init__(self, DataBase: dict, line: int, inheritanceClass: str):
        self.DataBase               = DataBase 
        self.line                   = line 
        self.inheritanceClass       = inheritanceClass
        self.classNames             = self.DataBase[ 'class_names' ]
        self.classes                = self.DataBase[ 'classes' ]
        
    def CLASSES( self, mainString: str ):
        self.error                  = None 
        self.variables              = None 
        self.function_names         = None
        self.functions              = None
        self.err                    = bm.fg.rbg(0, 255, 0)+' in {} {}class.'.format(self.inheritanceClass, bm.fg.red)+bm.init.reset 
        
        if self.inheritanceClass in self.classNames: 
            self.index              = self.classNames.index( self.inheritanceClass )
            self.my_class           = self.classes[ self.index ]
            self.main_body          = self.my_class[ 0 ][ 0 ]
            self.function_names     = self.main_body[ 'function_names' ]
            self.functions          = self.main_body[ 'functions' ] 
            self.main_initialize    = self.main_body[ 'init_function' ]
            
            if self.main_initialize  is None: pass
            else:
                self.function_init          = self.main_initialize[ 'function' ][ 1 ][ 0 ]
                self.init_arguments         = self.function_init[ 'initialize' ][ 'arguments' ]
                self.all_data_analyses_init = self.function_init[ 'initialize' ][ 'history_of_data' ]
                self.dictionary         = {
                    'functions'         : [],
                    'func_names'        : []
                }
                
                self.int_expression     = 'def initialize( ):'
                self.lexer, self.normal_expression, self.error = main.MAIN( self.int_expression, self.dictionary,
                                                                    self.line ).MAIN( def_key = 'indirect' )
                if self.error is None:
                    self._return_, self.error = func.FUNCTION(  self.dictionary[ 'functions' ] , self.DataBase, 
                                                        self.line ).DOUBLE_INIT_FUNCTION( mainString, 'initialize' )
                    if self.error is None:
                        self.__newBase__, self.error = func.FUNCTION( [ self.function_init ], self.DataBase,
                                                self.line).INIT_FUNCTION( mainString, self._return_ )
                        if self.error is None:
                            self.newBase           = self.__newBase__[ 'data_base' ]
                            if self.newBase[ 'empty_values' ] is None: pass 
                            else: 
                                self.empty_values   = self.self.newBase[ 'empty_values' ]
                                self.error          = ERRORS( self.line ).ERROR15( 'initialize' , self.empty_values )
                            
                            if self.error is None:
                                self._, self.value, self.variables, self.error = RUN_FUNCTION( self.DataBase, self.line,
                                                            self.newBase, self.__newBase__).RUN(self.all_data_analyses_init, 'initialize')
                            else: pass 
                        else: pass 
                    else: pass 
                else: pass
                 
                self.function_names = self.function_names#[1 : ] 
                              
        else:                                                                                            
            self.error = ERRORS( self.line ).ERROR13( self.inheritanceClass, 'class' )
        
        if self.error is None:pass 
        else: self.error += self.err 
            
        return self.function_names, self.functions, self.variables, self.error 
 
class LOAD:
    def __init__(self, moduleLoadNames : list, className: str):
        self.moduleLoadNames        = moduleLoadNames 
        self.className              = className
        
    def LOAD(self, typ : str = 'func_names'):
        self.key        = False 
        self.id1        = 0
        self.id2        = 0
        
        for i, mod in enumerate(self.moduleLoadNames):
            if self.key is False: pass 
            else: break 
            if mod: 
                for j, sub_mod in enumerate(mod[typ]):
                    if sub_mod == self.className:
                        self.key = True
                        self.id1 = i
                        self.id2 = j
                        break 
                    else: pass
            else: pass
        
        return {'key' : self.key, 'id1' : self.id1, 'id2' : self.id2}

    def INITIALIZE(self, new_data_base: dict, classes : list):
        self.n = 0
        for i, name in enumerate(self.moduleLoadNames):
            
            if name != self.funcName:
                if name in new_data_base['class_names']:
                    self.index = new_data_base['class_names'].index(name)
                    new_data_base['classes'][self.index] = classes[i]
                else:
                    self.n += 1
                    new_data_base['classes'].append(classes[i]) 
                    new_data_base['class_names'].append(name) 
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
        error = '{}a tuple(), {}or a string(), {}type. {}line: {}{}'.format(self.blue, self.cyan, self.yellow, self.white, self.yellow, self.line)
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
        self.error =  fe.FileErrors( 'IndentationError' ).ErrorIden()
        return self.error

    def ERROR11(self, string: str, key: str): #
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

    def ERROR13(self, string:str, name = 'class'): #
        self.error = None 
        
        if name == 'class':
            error = '{}was not found. {}line: {}{}'.format(self.green,  self.white, self.yellow, self.line )
            self.error = fe.FileErrors( 'NameError' ).Errors()+'{}{} name {}ERROR. {}<< {} >> '.format(self.white,
                                                                            name, self.yellow, self.cyan, string) + error
        else:
            error = '{}has not {}<< {} >> {} as a function. {}line: {}{}'.format( self.white, self.red, name, self.yellow, self.white,
                                                                                 self.yellow, self.line )
            self.error = fe.FileErrors( 'NameError' ).Errors()+'{}class {}<< {} >> '.format(self.white, self.cyan, string) + error
                                                                           
        
        return self.error+self.reset

    def ERROR14(self, string: str, typ = ''): #
        error = '{}takes {}no arguments. {}line: {}{}'.format(self.white, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}{}( ) {}{} '.format(self.cyan, string, self.red, typ) + error

        return self.error+self.reset

    def ERROR15(self, string: str, value: list): #
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{} in {}<< {}( ) >> '.format(self.white, self.cyan, string) + error

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
     
    def ERROR21(self, string: str, name: str  ): #
        error = '{}has not {}<< {} >> {}as argument. {}line: {}{}'.format(self.white, self.blue, name, self.yellow, 
                                                                          self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'AttributeError' ).Errors()+'{}{} {}class '.format(self.cyan, string, self.red) + error

        return self.error+self.reset

    def ERROR22(self, string: str, name = 'string()'): #
        error = '{}has not {}<< {} >> {}as a function. {}line: {}{}'.format(self.white, self.green, string, self.red,
                                                                             self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors()+'{}{} {}type '.format(self.cyan, name, self.yellow) + error

        return self.error+self.reset
    
    def ERROR23(self, string: str): #
        error = '{}is not in the list {}[ {}keys{}, {}items {}]. {}line: {}{}'.format(self.white, self.green, self.red, self.white, self.magenta, self.green,
                                                                             self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}{} '.format(self.cyan, string) + error

        return self.error+self.reset 
    
    def ERROR24(self, string: str = 'dictionary'): #
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line )                                   
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}EMPTY {}{} .'.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR25(self,  key: str): #
        error = '{}was not found in the {}dictionary(). {}line: {}{}'.format(self.white, self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'KeyError' ).Errors()+'{}<< {} >> '.format(self.cyan, key) + error

        return self.error+self.reset

    def ERROR26(self, string: str, char: str): #
        error = '{}due to {}<< {} >>. {}line: {}{}'.format(self.white, self.red, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan , string) + error

        return self.error+self.reset 
    
    def ERROR27(self, string: str, s : str='list' ): #
        error = '{}was not found in the {}{}. {}line: {}{}'.format(self.white, self.yellow, s, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}<< {} >> '.format(self.cyan , string) + error

        return self.error+self.reset
    
    def ERROR28(self, func = 'list', c:str = ''): #
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'IndexError' ).Errors()+'{}{} {}index {}out of range. '.format(self.yellow, func, self.red, self.white) + error

        return self.error+self.reset
    
    def ERROR29(self, s : str = 'master'): #
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}length( {}{}{} ) {}!= {}2. '.format(self.cyan, self.red, s, self.cyan, self.white, 
                                                                self.cyan) + error

        return self.error+self.reset
    
    def ERROR30(self, s : str = 'numeric'): #
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}abs( {}{}{} ) {}is lower than {}0. '.format(self.cyan, self.red, s, self.cyan, self.white, 
                                                                self.cyan) + error

        return self.error+self.reset
    
    def ERROR31(self, value): #
        error = '{}a tuple(), {} a dictionary() {}or a string(), {}type. {}line: {}{}'.format(self.blue, self.magenta, self.cyan, self.yellow, 
                                                                                            self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> {}is not {}a list(), '.format(self.cyan, value, self.white, self.yellow) + error
        return self.error+self.reset
    
    def ERROR32(self, value: list): #
        falseValue = None
        for v in value :
            if type( v ) != type( str() ):
                falseValue = v 
                break 
        
        self.error = ERRORS( self.line ).ERROR3( falseValue, 'a string()')
      
        return self.error+self.reset

    def ERROR33(self, value: str): #
        error = '{}was not found in the {}string. {}line: {}{}.'.format(self.white, self.magenta, 
                                                                            self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}<< {} >> '.format(self.cyan, value) + error
        return self.error+self.reset
    
    
    def ERROR34(self, value: str): #
        error = '{}cannot be negative. {}line: {}{}.'.format(self.white, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}{} '.format(self.cyan, value) + error
        return self.error+self.reset
    
    def ERROR35(self, value: int): #
        error = '{}is not {}string(), {}a float() or {}an integer() {}type. {}line: {}{}.'.format(self.white, self.magenta, self.green, 
                                                                    self.red, self.yellow,self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}list index {}<< {} >> '.format(self.white, self.cyan, value) + error
        return self.error+self.reset
    
    def ERROR36(self, string: str): #
        error = '{}was not found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileNotFoundError' ).Errors() + '{}file {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR37(self, string: str, mode: str): #
        if mode == 'w': mode = 'write'
        else: mode = 'read'
        
        error = '{}is {}{} only {}mode. {}line: {}{}'.format(self.white, self.red, mode, self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileModeError' ).Errors() + '{}file {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR38(self, idd : int): #
        
        error = '{}is not a {}a string() {}type. {}line: {}{}'.format(self.white, self.magenta, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}list index {}{} '.format( self.white, self.cyan, idd) + error

        return self.error+self.reset
    
    def ERROR39(self): #
        
        error = '{}line: {}{}'.format( self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'EncodingError' ).Errors() + '{}got an encoding {}ERROR '.format( self.white, self.yellow ) + error

        return self.error+self.reset
    
    def ERROR40(self): #
        
        error = '{}line: {}{}'.format( self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'DecodingError' ).Errors() + '{}got a decoding {}ERROR '.format( self.white, self.yellow ) + error

        return self.error+self.reset
    
    def ERROR41(self): #
        
        error = '{}line: {}{}'.format( self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'UnicodeError' ).Errors() + '{}got a unicode {}ERROR '.format( self.white, self.yellow ) + error

        return self.error+self.reset
    
    def ERROR42(self, string: str, name: str): #
        
        error = '{}as {}function {}or {}class. {}line: {}{}'.format( self.white, self.cyan, self.white, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors() + '{}{} {}has not {}{} '.format( self.red, string, self.white, self.green, name ) + error

        return self.error+self.reset
    
    def ERROR43(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleError' ).Errors() +'{}The module {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR44(self, string: str, name: str):
        error = '{}has not {}{} {}as class. {}line: {}{}'.format(self.white, self.red, name, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}The class {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR45(self, string: str, name: str):
        error = '{}has not {}{} {}as class. {}line: {}{}'.format(self.white, self.red, name, self.yellow,
                                                                                 self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}The module {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR46(self, string: str, name: str):
        error = '{}has not {}{} {}as function. {}line: {}{}'.format(self.white, self.red, name,  self.blue,
                                                                                 self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}The module {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR47(self, s: str = 'max_step'):
        error = '{}cannot be {}<= 0. {}line: {}{}'.format(self.white, self.red,  self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() +'{}{} '.format(self.cyan, s) + error

        return self.error+self.reset

    def ERROR48(self, s1: str = 'max_num1', s2 : str = 'max_num2'):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() +'{}{} {}== {}{} '.format(self.cyan, s1, self.red, self.cyan, s2) + error

        return self.error+self.reset

    def ERROR49(self, value : str = 'master'):
        error = '{}a tuple(), {}or {}an integer(), {}type. {}line: {}{}'.format(self.blue, self.white, self.red, self.yellow, self.white,
                                                                                self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> {}is not '.format(self.cyan, value, self.white) + error
        return self.error+self.reset
    
    def ERROR50(self, value : str = 'master'):
        error = '{}a tuple(), {}or {}a list(), {}type. {}line: {}{}'.format(self.blue, self.white, self.yellow, self.yellow, self.white,
                                                                                self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> {}is not '.format(self.cyan, value, self.white) + error
        return self.error+self.reset
         
class DB:
    functionNames, functions = db.DATA_BASE().FUNCTIONS()
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
        'class_names'       : [],
        'func_names'        : [],
        'current_func'      : None,
        'current_class'     : None,
        'no_printed_values' : [],
    }
    
    globalDataBase          = {
        'global_vars'       : {
            'vars'          : [],
            'values'        : []
            },
        'variables'         : {
            'vars'          : [],
            'values'        : []
            },
        'irene'             : None,
        'functions'         : [],
        'classes'           : [],
        'class_names'       : [],
        'func_names'        : [],
        'loop_for'          : [],
        'loop_while'        : [],
        'loop_until'        : [],
        'continue'          : None, 
        'next'              : None,
        'pass'              : None,
        'break'             : None,
        'exit'              : None,
        'try'               : None,
        'begin'             : None,
        'if'                : [],
        'switch'            : [],
        'unless'            : [],
        'return'            : {
            'def'           : [],
            'class'         : []
            },
        'print'             : [],
        'sub_print'         : None,
        'current_func'      : None,
        'current_class'     : None,
        'transformation'    : None,
        'no_printed_values' : [],
        'line'              : None,
        'encoding'          : None,
        'importation'       : None,
        'LIB'               : {
            'func_names'    : functionNames,
            'functions'     : functions,
            'class_names'   : [],
            'classes'       : []
            },
        'modulesImport'     : {
            'moduleNames'   : [],
            'fileNames'     : [],
            'expressions'   : [],
            'variables'     : {
                'vars'      : [],
                'values'    : []
            },
            'classes'       : [],
            'class_names'   : [],
            'functions'     : [],
            'func_names'    : [],
            'mainFuncNames' : [],
            'mainClassNames': [],
            'modules'       : [],
            'modulesLoadC'  : [],
            'modulesLoadF'  : [],
            'init'          : []
        },
        'open'              : {        
            'name'          : [],          
            'file'          : [],          
            'action'        : [],         
            'status'        : [],       
            'encoding'      : [],     
            'nonCloseKey'   : []
        },
        'globalIndex'       : None,
        'starter'           : 0,
        'subFunctionNames'  : [],
        'subclassNames'     : []
    }
