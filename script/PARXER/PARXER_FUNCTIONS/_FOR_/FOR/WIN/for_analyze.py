from script.LEXER.FUNCTION                              import main
from script.PARXER                                      import parxer_assembly
import cython

@cython.cclass
class NEXT_ANALYZE:
    def __init__(self, master: str, data_base : dict, line : int):
        self.line               = line
        self.data_base          = data_base
        self.master             = master
        self.main               = main
        
    @cython.cfunc
    def SUB_ANALYZE(self, _id_:int = 1, _type_:any = None):
        self.error          = None
        self.lexer, self.string, self.error = self.main.MAIN(self.master, self.data_base, self.line).MAIN(_id_, _type_, True)
        if self.error is None:
            self.error = parxer_assembly.ASSEMBLY(self.lexer, self.data_base, self.line).ASSEMBLY( self.master, True )
        else: pass

        return self.lexer, self.error

    @cython.cfunc
    def SUB_SUB_ANALYZE(self, _lexer_ : dict = None):
        self.lexer          = _lexer_
        self.error = parxer_assembly.ASSEMBLY(self.lexer, self.data_base, self.line).ASSEMBLY( self.master, True )
        
        return self.error