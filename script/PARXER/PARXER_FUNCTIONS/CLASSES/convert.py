from script.LEXER.FUNCTION                      import main
from script.PARXER.WINParxer                    import parxer_file_interpreter as PFI

class convert:
    def __init__(self, db : dict, line : int): 
        self.db     = db
        self.line   = line 
    def convert(self, data_from_file : list, locked : bool = False, baseFileName : str = ""):
        self.lineI          = 0
        self.baseFileName   = baseFileName
        self.error          = None 

        for x, string in enumerate( data_from_file ):
            self.lineI  += 1
            
            if string:
                if self.db['globalIndex'] is None:
                    try:
                        self.db['starter'] = x+1
                        self.lexer, self.normal_string, self.error = main.MAIN(string, self.db, 
                                (self.lineI + self.line) ).MAIN( interpreter = True, MainList = data_from_file[x+1: ] )
                        
                        if self.error is None:
                            self.new_array = data_from_file[x+1: ]
                            if self.lexer is not None:
                                nnum, self.key, self.error = PFI.ASSEMBLY(master = self.lexer, data_base = self.db, 
                                    line = (self.lineI + self.line)).GLOBAL_ASSEMBLY_FILE_INTERPRETER(main_string = self.normal_string,
                                    interpreter=True, MainList=self.new_array, baseFileName=self.baseFileName, locked=locked)
                                if self.error is None: pass
                                else:  break
                            else: pass
                        else:  break
                    except EOFError: break
                else:
                    if x < self.db['globalIndex']+1: pass 
                    else:
                        try:
                            self.db['starter'] = x+1
                            self.lexer, self.normal_string, self.error = main.MAIN(string, self.db, 
                                    (self.lineI + self.line)).MAIN( interpreter = True,  MainList = data_from_file[x+1: ] )
                            
                            if self.error is None:
                                if self.lexer is not None:
                                    self.new_array = data_from_file[x+1: ]
                                    num, self.key, self.error = PFI.ASSEMBLY(master = self.lexer, data_base = self.db, 
                                        line = (self.lineI + self.line)).GLOBAL_ASSEMBLY_FILE_INTERPRETER(main_string = self.normal_string,
                                        interpreter=True, MainList=self.new_array, baseFileName=self.baseFileName, locked=locked)
                                    if self.error is None: pass
                                    else:  break
                                else: pass
                            else: break
                        except EOFError: break
            else: pass

        return self.db , self.error