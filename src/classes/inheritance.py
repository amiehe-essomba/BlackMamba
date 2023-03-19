from src.classes                                    import error as er 
from script.STDIN.LinuxSTDIN                        import bm_configure as bm
from src.classes                                    import run_func
from script.LEXER.FUNCTION                          import main
from src.functions                                  import function


class INHERITANCE:
    def __init__(self, 
            DataBase: dict, 
            line: int, 
            inheritanceClass: str
            ):
        
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
                    self._return_, self.error = function.FUNCTION(  self.dictionary[ 'functions' ] , self.DataBase, 
                                                        self.line ).DOUBLE_INIT_FUNCTION( mainString, 'initialize' )
                    if self.error is None:
                        self.__newBase__, self.error = function.FUNCTION( [ self.function_init ], self.DataBase,
                                                self.line).INIT_FUNCTION( mainString, self._return_ )
                        if self.error is None:
                            self.newBase           = self.__newBase__[ 'data_base' ]
                            if self.newBase[ 'empty_values' ] is None : pass 
                            else: 
                                self.empty_values   = self.newBase[ 'empty_values' ]
                                self.error          = er.ERRORS( self.line ).ERROR15( 'initialize' , self.empty_values )
                            
                            if self.error is None:
                                self._, self.value, self.variables, self.error = run_func.RUN_FUNCTION( self.DataBase, self.line,
                                                            self.newBase, self.__newBase__).RUN(self.all_data_analyses_init, 'initialize')
                            else: pass 
                        else: pass 
                    else: pass 
                else: pass
                 
                self.function_names = self.function_names.copy()#[1 : ] 
        else:  self.error = er.ERRORS( self.line ).ERROR13( self.inheritanceClass, 'class' )
        
        if self.error is None:pass 
        else: self.error += self.err 
            
        return self.function_names, self.functions, self.variables, self.error 