import                                              random
from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation
from src.classes.Lists                              import inserting, random_init, sorting
from src.classes.Lists                              import to_array as ta
import numpy as np 


class RANGE:
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
        
    def RANGE(   self, mainName: str, mainString:  str )   :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
 
        if self.function in [ 'size'  ]            :
            if None in self.arguments: 
                self._return_ = len( self.master )
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'choice']            :
            if None in self.arguments:
                if self.master:
                    self._return_ = random.choice( self.master )
                else: self.error =  er.ERRORS( self.line ).ERROR24( 'list / tuple / range' )    
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'to_array']          :
            self._return_, self.error = ta.TO( self.DataBase, self.line, list( self.master ),
                                                 self.function, [self.FunctionInfo] ).ARRAY( mainName, mainString )
        elif self.function in [ 'enumerate' ]        :
            if None in self.arguments:
                if self.master:
                    self._return_ = []
                    for i, value in enumerate( list( self.master ) ):
                        self._return_.append( (i, value) )
                else: self.error =  er.ERRORS( self.line ).ERROR24( 'range' )    
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function )      
                           
        elif self.function in [ 'sum' ]        :
            if None in self.arguments:
                if self.master:
                    self._return_ = float( np.array(self.master, dtype='f8').sum() )
                else: self.error =  er.ERRORS( self.line ).ERROR24( 'range' )    
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function )  
        
        elif self.function in [ 'std' ]        :
            if None in self.arguments:
                if self.master:
                    self._return_ = float( np.array(self.master, dtype='f8').std() )
                else: self.error =  er.ERRORS( self.line ).ERROR24( 'range' )    
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function )
        
        elif self.function in [ 'mean' ]        :
            if None in self.arguments:
                if self.master:
                    self._return_ = float( np.array(self.master, dtype='f8').mean() )
                else: self.error =  er.ERRORS( self.line ).ERROR24( 'range' )    
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'var' ]        :
            if None in self.arguments:
                if self.master:
                    self._return_ = float( np.array(self.master, dtype='f8').var() )
                else: self.error =  er.ERRORS( self.line ).ERROR24( 'range' )    
            else: self.error =  er.ERRORS( self.line ).ERROR14( self.function )
        return self._return_, self.error  