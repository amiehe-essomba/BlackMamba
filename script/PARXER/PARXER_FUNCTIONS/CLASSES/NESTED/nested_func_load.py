import pandas as pd
import numpy as np
from script.LEXER.FUNCTION                          import main
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS       import functions as func
from src.classes                                    import error as er
from src.classes                                    import loading, readfile, check_char, run_func, inheritance
from src.classes.Chars                              import Char
from src.classes.Lists                              import Lists
from src.classes.Cplx                               import cplx 
from src.classes.frame                              import frame
from src.classes.Tuples                             import Tuples
from src.classes.Unions                             import union   
from src.classes.matrix                             import matrix_2D as m2D  
from src.classes.matrix                             import arguments as argm
from src.functions                                  import loading as load         
from src.functions                                  import function            
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS       import externalLoading as extL  
from script.PARXER.PARXER_FUNCTIONS.CLASSES.NESTED  import nested_vars as n_v

class NESTED:
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
           
    def NESTED(self, idd : int = 0):
        self.error                  = None 
        self.final_values           = None
        self.initialize_values      = None
        self.value_from_db          = None
        self.normal_expr            = ''
        self.main_name              = self.master[ 'names' ][ 0 ]
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
            
                if self.error is None: 
                    if type(self.final_values) in [type(list()), type(dict()), type(np.array([1]))]:
                        self.DataBase['variables']['values'][idd] = self.final_values.copy()
                    else: self.DataBase['variables']['values'][idd] = self.final_values
                else: pass 
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
                                                                
                    if self.error is None: 
                        if type(self.final_values) in [type(list()), type(dict()), type(np.array([1]))]:
                            self.DataBase['variables']['values'][idd] = self.final_values.copy()
                        else: self.DataBase['variables']['values'][idd] = self.final_values
                    else: pass
                else:  self.error = er.ERRORS(self.line).ERROR46( self.main_name, self.sub_name )
                    
        return self.final_values, self.value_from_db, self.initialize_values, self.error

    def SUB_NESTED_FUNC_LOAD(self, idd : int = 0):
        self.error                  = None 
        self.final_values           = None
        self.initialize_values      = None
        self.value_from_db          = None
        self.normal_expr            = ''
        
        self.names = self.master[ 'names' ]
        self.add_params = self.master[ 'add_params' ]
        self.expressions = self.master[ 'expressions' ]
        self.new_master = self.master.copy()
        self.att = self.names[0]
        
        for i in range(len(self.names)-1):
            self.new_master['add_params'] = [self.add_params[0], self.add_params[i+1]]
            self.new_master['expressions' ] = [self.expressions[0], self.expressions[i+1]]
            if i == 0:
                self.new_master['names'] = [self.names[0], self.names[i+1]]
                self.final_values, self.value_from_db, self.initialize_values, self.error = NESTED( self.new_master, self.DataBase, self.line).NESTED()
            else:
                self.new_master['names'] = [self.names[0], self.names[i+1]]
                self.final_values, self.value_from_db, self.initialize_values, self.error = n_v.NESTED( self.new_master, self.DataBase, self.line).NESTED()
            
            if self.error is None: 
                if type(self.final_values) in [type(list()), type(dict()), type(np.array([1]))]:
                    self.DataBase['variables']['values'][idd] = self.final_values.copy()
                else: self.DataBase['variables']['values'][idd] = self.final_values
            else: break 
        
        return self.final_values, self.value_from_db, self.initialize_values, self.error
        
