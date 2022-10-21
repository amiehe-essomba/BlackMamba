from script.LEXER.FUNCTION import main
from script.PARXER import parxer_assembly

class LEXER_AND_PARXER:
    def __init__(self, master:str, data_base:dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.main               = main

    def ANALYZE(self, _id_:int = 1, _type_:any = None ):
        self.error                  = None
        self.lexer                  = None
        
        self.lexer, self.string, self.error  = self.main.MAIN( self.master, self.data_base, self.line).MAIN(_id_, _type_, True)
      
        if self.error is None:
            self.error = parxer_assembly.ASSEMBLY( self.lexer, self.data_base, self.line ).ASSEMBLY( self.master, True )
        else: self.error = self.error

        return  self.error

class NEXT_ANALYZE:
    def __init__(self, master: str, data_base : dict, line : int):
        self.line               = line
        self.data_base          = data_base
        self.master             = master
        self.main               = main

    def SUB_ANALYSZE(self, _id_:int = 1, _type_:any = None):# index : int = 0, lexer_init = None):
        self.error  = None

        self.lexer, self.string, self.error = self.main.MAIN(self.master, self.data_base, self.line).MAIN(_id_, _type_, True)
        if self.error is None:
            self.error = parxer_assembly.ASSEMBLY(self.lexer, self.data_base, self.line).ASSEMBLY( self.master, True )
        else: self.error = self.error

        return self.error

class MAIN:
    def __init__(self, master:str, data_base:dict, line: int):
        self.line = line
        self.master = master
        self.data_base = data_base
        self.main = main

    def MAIN_LEXER(self, _id_:int = 1, _type_:any = None):
        self.error          = None
        self.lexer, self.string, self.error = self.main.MAIN(self.master, self.data_base, self.line).MAIN( _id_, _type_,
                                                                                                          True)
        if self.error is None:
            pass
        else:
            self.error = self.error

        return self.lexer, self.error

