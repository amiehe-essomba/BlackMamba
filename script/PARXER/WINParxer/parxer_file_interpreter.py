from statement                                              import mainStatement                as MS
from script.PARXER                                          import module_load_treatment 
from src.modulesLoading                                     import modules, moduleMain 
from script.PARXER                                          import partial_assembly
from loop                                                   import mainFor
from script.STDIN.WinSTDIN                                  import stdin
from script.PARXER.PARXER_FUNCTIONS._IF_                    import if_inter
from script.PARXER.PARXER_FUNCTIONS._FOR_                   import for_interpreter
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS               import def_interpreter
from script.PARXER.PARXER_FUNCTIONS.CLASSES                 import class_interpreter

class ASSEMBLY( ):
    def __init__(self, 
        master      : dict, 
        data_base   : dict, 
        line        : int 
        ):
        
        # current line 
        self.line           = line
        # lexer 
        self.master         = master
        # main data base
        self.data_base      = data_base
    
    def GLOBAL_ASSEMBLY_FILE_INTERPRETER(self, 
            main_string     : str, 
            interpreter     : bool  = False, 
            MainList        : list  = [], 
            baseFileName    : str   = '',
            locked          : bool  = True
            ):
        
        self._return_           = None
        self.key_return         = None
        self.error              = None
        self.active_function    = None
        self.all_data_vars      = list( self.master.keys() )
        self.structure          = [ 'begin', 'if', 'loop_for', 'loop_until', 'loop_while', 'try', 'unless', 'switch' ]

        for i , data in enumerate( self.all_data_vars ):
            if data != 'if_egal':
                if self.master[ data ] is None: pass
                else:
                    self.active_function = data
                    break
            else: pass

        if self.active_function == 'all_data':
            if   self.master[ 'function' ] is None      :
                self.error = partial_assembly.ASSEMBLY( self.master, self.data_base, self.line).ASSEMBLY( main_string, interpreter )        
            elif self.master[ 'function' ] == 'if'      :
                self._return_, self.error = MS.MAIN(master = main_string, data_base=self.data_base,
                                line=self.newLine).MAIN(typ = 'if', opposite = False, interpreter = True, function = None)
                
                if self.error is None:
                    self.data_base[ 'print' ]       = []
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                    self.newLine                    = self.line
                    
                    self.listTransform ,self.error  = if_inter.EXTERNAL_IF_STATEMENT( None, self.data_base,
                                                                         self.line ).IF_STATEMENT(1, self.NewLIST )
                else: pass
            elif self.master[ 'function' ] == 'for'     :
                self._, self.value, self.error =  mainFor.FOR_BLOCK(normal_string =main_string, data_base=self.data_base, 
                                                line=self.newLine).FOR( function = 'loop', interpreter = interpreter,   locked=False)
                
                if self.error is None:
                    self.data_base['variables']['vars'].append(self.value['variable'])
                    self.data_base['variables']['values'].append(self.value['value'][-1])
                    
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                    self.newLine                    = self.line
                    
                    self.listTransform = for_interpreter.EXTERNAL_FOR_STATEMENT( None, self.data_base,
                                                                         self.line ).FOR_STATEMENT(1, self.NewLIST )
                else : pass         
            else: pass 
            
        else:
            if   self.data_base[ 'current_func' ]  is not None:
                
                self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                self.newLine                    = self.line
                self.MainStringTransform        = main_string
                self.listTransform              = self.NewLIST 
                
                self.error = def_interpreter.EXTERNAL_DEF_STATEMENT( None, self.data_base, self.line ).DEF( tabulation = 1, 
                                                                    loop_list = self.listTransform )
                    
            elif self.data_base[ 'current_class' ] is not None:
                self.NewLIST                    = stdin.STDIN(self.data_base, self.line ).GROUPBY(1, MainList)
                self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                self.newLine                    = self.line
                self.MainStringTransform        = main_string
                self.listTransform              = self.NewLIST 
                
                self.error = class_interpreter.EXTERNAL_CLASS_STATEMENT( 
                            main_string, self.data_base, self.line, 
                            self.master['class']).CLASSES(  
                            tabulation = 1, 
                            loop_list = self.listTransform 
                            )
                if self.error is None: pass
                else: pass           
            elif self.data_base[ 'importation' ]   is not None:
                self.data_base[ 'loading' ]    = True
                self.modules = self.data_base[ 'importation' ] 
                self.dataS, self.info, self.error = moduleMain.TREATMENT( self.modules, self.data_base, 
                                                                                    self.line ).MODULE_MAIN( main_string )
                if self.error is None:
                    self.error = modules.MODULES( self.data_base, self.line, self.dataS, self.info ).LOAD()
                    if self.error is None:
                        self.error = module_load_treatment.CLASSIFICATION( self.data_base, self.line ).CLASSIFICATION( 
                            self.data_base[ 'modulesImport' ], 
                            info = self.data_base[ 'importation' ]
                            )
                    else: pass
                else: pass
                self.data_base[ 'importation' ] = None
                
        return  self._return_, self.key_return, self.error