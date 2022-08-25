from src.classes                                    import error as er 
from src.classes.Chars                              import Global, Join, Replace, Split

class STRING:
    def __init__(self, DataBase: dict, line:int, master: str, function, FunctionInfo : list ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        
    def STR( self , mainName: str , mainString : str = ''):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.values         = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if   self.function in [ 'lower' ]            :
            if None in self.arguments: self._return_ = self.master.lower()
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'upper' ]            :
            if None in self.arguments:  self._return_ = self.master.upper() 
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'split' ]            :
            self._return_, self.error = Split.STRING( self.DataBase, self.line, self.master,
                                    self.function, [self.FunctionInfo] ).SPLIT( mainString  )  
        elif self.function in [ 'join'  ]            :
            self._return_, self.error = Join.STRING( self.DataBase, self.line, self.master,
                                    self.function, [self.FunctionInfo] ).JOIN( mainString  )  
        elif self.function in [ 'empty' ]            :
            if None in self.arguments: 
                if    self.master: self._return_ = False
                else: self._return_ = True
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'size'  ]            :
            if None in self.arguments: 
                self._return_ = len( self.master )
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'replace'  ]         :
            self._return_, self.error = Replace.STRING( self.DataBase, self.line, self.master,
                                    self.function, [self.FunctionInfo] ).REPLACE( mainName, mainString  ) 
        elif self.function in [ 'capitalize']        :
            if None in self.arguments: self._return_ = self.master.capitalize( )
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'enumerate' ]        :
            if  None in self.arguments:
                if self.master:
                    self._return_ = []
                    for i, value in enumerate( self.master ):
                        self._return_.append( (i, value) )
                else: self.error = er.ERRORS( self.line ).ERROR24( 'string' )     
            else:self.error = er.ERRORS( self.line ).ERROR14( self.function )    
        elif self.function in [ 'index', 'count', 'startwith', 'endwith' ] :
            self._return_, self.error = Global.STRING( self.DataBase, self.line, self.master,
                                    self.function, [self.FunctionInfo] ).GLOBAL( self.function, mainString  ) 
        
        return self._return_, self.error

    
    