from src.classes                                    import error as er 

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
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'real' ]      :
            if None in self.arguments: 
                self._return_ = self.master.real
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'norm' ]      :
            if None in self.arguments:
                self.real = self.master.real
                self.img  = self.master.imag 
                self._return_ = (self.real ** 2 + self.img ** 2) ** (0.5)   
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )  
        elif self.function in [ 'conj' ]      :
            if None in self.arguments: 
                img = self.master.imag
                real= self.master.real 
                c = str(real) + '-' + str(img) + 'j'
                self._return_ = complex( c )
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        
        return self._return_, self.error 