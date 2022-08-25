from script   import control_string

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