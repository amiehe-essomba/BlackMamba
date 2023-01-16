from loop                                                   import mainFor
from script.PARXER.PRINT                                    import show_data
from script.LEXER.FUNCTION                                  import print_value
from script.PARXER.PARXER_FUNCTIONS._IF_                    import if_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_                import switch_statement
from script.PARXER.PARXER_FUNCTIONS._TRY_                   import try_statement
from script.PARXER.PARXER_FUNCTIONS._FOR_                   import for_block_treatment
from script.PARXER                                          import module_load_treatment 
from script.PARXER                                          import partial_assembly
from script.STDIN.WinSTDIN                                  import stdin, if_stdin
from script.PARXER.PARXER_FUNCTIONS._IF_                    import if_inter
from script.PARXER.PARXER_FUNCTIONS._SWITCH_                import switch_inter
from script.PARXER.PARXER_FUNCTIONS._UNLESS_                import unless_interpreter
from script.PARXER.PARXER_FUNCTIONS._FOR_                   import for_interpreter
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS               import def_interpreter
from script.PARXER.PARXER_FUNCTIONS.CLASSES                 import class_interpreter
from src.modulesLoading                                     import modules, moduleMain 
from script.PARXER.PARXER_FUNCTIONS._UNLESS_                import unless_statement     as US
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_         import cmt_interpreter      as cmt_int
from statement                                              import mainStatement        as MS

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
        
    def GLOBAL_ASSEMBLY_FOR_INTERPRETER(self, 
            main_string     : str, 
            interpreter     : bool  = False, 
            MainList        : list  = [], 
            baseFileName    : str   = ''
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
                self.newLine                    = self.line
                           
                self.data_base[ 'print' ]       = []
                self.NewLIST                    = stdin.STDIN(self.data_base, self.newLine ).GROUPBY(1, MainList)
                #self.NewLIST                    = if_stdin.STDIN(self.data_base, self.line ).STRUCT(1, MainList)
                self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                
                self.listTransform ,self.error  = if_inter.EXTERNAL_IF_STATEMENT( None, self.data_base,
                                                                        self.newLine ).IF_STATEMENT(1, self.NewLIST )
                self._return_, self.error = MS.MAIN(master = main_string, data_base=self.data_base,
                                line=self.newLine).MAIN(typ = 'if', opposite = False, interpreter = True, function = None)
                #print(self.NewLIST, "########")
                #print(self.listTransform, "@@", self._return_)
                if self.error is None:
                    self.MainStringTransform        = 't'+main_string
                    self.listTransform              = [(self.MainStringTransform , True), self.listTransform]
                    
                    self.error = if_statement.EXTERNAL_IF_LOOP_STATEMENT( None , self.data_base,
                                        self.newLine ).IF_STATEMENT( bool_value=self._return_, tabulation=1, loop_list=self.listTransform )
                    if self.error is None:
                        if self.data_base[ 'print' ] is not None:
                            self.list_of_values = self.data_base[ 'print' ]
                            for i, value in enumerate( self.list_of_values ):
                                if i < len( self.list_of_values ) - 1:
                                    print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                                else:
                                    print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )   
                        else: pass
                        self.data_base['print'] = []
                    else: pass
                else: pass          
            elif self.master[ 'function' ] == 'unless'  :
                self.newLine                    = self.line
                
                self.NewLIST                    = stdin.STDIN(self.data_base, self.newLine ).GROUPBY(1, MainList)
                self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                
                self.listTransform, self.error = unless_interpreter.EXTERNAL_UNLESS_STATEMENT(master=None, data_base=self.data_base,
                        line=self.newLine).UNLESS_STATEMENT(tabulation =  1, loop_list = self.NewLIST )
                
                if self.error is None:
                    self.MainStringTransform        = 't'+main_string
                    self.listTransform              = [(self.MainStringTransform , True), self.listTransform]
                    
                    self.error = US.EXTERNAL_UNLESS_FOR_STATEMENT( master=None , data_base=self.data_base, 
                            line=self.newLine ).UNLESS_STATEMENT( bool_value=True, tabulation=1, loop_list=self.listTransform )
                    
                    if self.error is None:
                        if self.error is None:
                            if self.data_base[ 'print' ] is not None:
                                self.list_of_values = self.data_base[ 'print' ]
                                for i, value in enumerate( self.list_of_values ):
                                    if i < len( self.list_of_values ) - 1:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                                    else:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )
                                        
                            else: pass
                            self.data_base['print'] = []
                        else: pass
                    else: pass
                else: pass
            elif self.master[ 'function' ] == 'switch'  :
                self.newLine                    = self.line
                self._return_, self.error = MS.MAIN(main_string, self.data_base, self.newLine).MAIN(typ='switch',
                                                opposite=False, interpreter=True)
                if self.error is None:
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.newLine ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                
                    self.listTransform, self.error = switch_inter.SWITCH(master=None, data_base=self.data_base,
                            line=self.newLine).SWITCH(tabulation = 1, loop_list = self.NewLIST )
                                        
                    self.error = switch_statement.SWITCH_LOOP_STATEMENT(master=None, data_base=self.data_base, 
                                        line=self.newLine).SWITCH(main_values=self._return_, tabulation=1, loop_list=self.listTransform)
                    
                    if self.error is None:
                        if self.error is None:
                            if self.data_base[ 'print' ] is not None:
                                self.list_of_values = self.data_base[ 'print' ]
                                for i, value in enumerate( self.list_of_values ):
                                    if i < len( self.list_of_values ) - 1:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                                    else:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )
                                        
                            else: pass
                            self.data_base['print'] = []
                        else: pass
                    else: pass
                else: pass
            elif self.master[ 'function' ] == 'for'     :
                self.newLine                    = self.line
                
                self._, self.value, self.error  =  mainFor.FOR_BLOCK(normal_string =main_string, data_base=self.data_base, 
                                                line=self.newLine).FOR( function = 'loop', interpreter = interpreter,   locked=False)
                
                if self.error is None:
                    self.data_base['variables']['vars'].append(self.value['variable'])
                    self.data_base['variables']['values'].append(self.value['value'][-1])
                    
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.newLine ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                    
                    self.listTransform = for_interpreter.EXTERNAL_FOR_STATEMENT( None, self.data_base,
                                                                        self.newLine ).FOR_STATEMENT(1, self.NewLIST )
                    
                    self.data_base[ 'print' ] = []
                    self.got_errors, self.error = for_block_treatment.TREATMENT( self.data_base,
                                                    self.newLine ).FOR( main_string, self.value, self.name, True, self.listTransform )

                    if self.error is None:
                        if self.data_base[ 'print' ] is not None:
                            self.list_of_values = self.data_base[ 'print' ]
                            for i, value in enumerate( self.list_of_values ):
                                if len( self.value ) == 1 :
                                    for sub_value in value:
                                        if i < len( self.list_of_values) - 1:
                                            show_data.SHOW( sub_value, self.data_base, False ).SHOW( loop = True)
                                        else:
                                           show_data.SHOW( sub_value, self.data_base, False ).SHOW( loop = False) 
                                else:
                                    if i < len( self.list_of_values) - 1:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                                    else:
                                        print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = False )

                                if self.got_errors:
                                    print( self.got_errors[ i ])
                                else: pass
                        else: pass
                    else: pass
                    self.data_base['print'] = []

                else: self.error = self.error
            else: pass
        else:
            if   self.master[ 'begin'  ] is True:
                self.newLine  = self.line 
                self.NewLIST                    = stdin.STDIN(self.data_base, self.newLine ).GROUPBY(1, MainList )
                self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                self.error = cmt_int.COMMENT_STATEMENT( None, self.data_base, self.newLine ).COMMENT( 1, self.NewLIST )             
            elif self.master[ 'delete' ] is True: pass
            elif self.master[ 'global' ] is True: pass
            elif self.master[ 'print'  ]            is not None: pass
            elif self.master[ 'transformation' ]    is not None: pass
            elif self.master[ 'try' ]    is True:
                self.data_base[ 'print' ] = []
                self._, self.error = try_statement.EXTERNAL_TRY_STATEMENT(None,
                                                    self.data_base, self.line ).TRY_STATEMENT(tabulation = 1)

                if self.data_base[ 'print' ] is not None:
                    self.list_of_values = self.data_base[ 'print' ]
                    for i, value in enumerate( self.list_of_values ):
                        if i < len( self.list_of_values) - 1:
                            print_value.PRINT_PRINT( value ).PRINT_PRINT( key = False, loop = True )
                        else:
                            print_value.PRINT_PRINT( value ).PRINT_PRINT( key = False, loop = True )
                else:  pass
            else:
                if   self.data_base[ 'current_func' ]  is not None:
                    self.newLine                    = self.line
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.newLine  ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                    self.MainStringTransform        = main_string
                    self.listTransform              = self.NewLIST 
                    
                    self.error = def_interpreter.EXTERNAL_DEF_STATEMENT( None, self.data_base, self.newLine  ).DEF( tabulation = 1, 
                                                                        loop_list = self.listTransform )
                    if self.error is None: pass
                    else: pass                   
                elif self.data_base[ 'current_class' ] is not None:
                    self.newLine                    = self.line
                    self.NewLIST                    = stdin.STDIN(self.data_base, self.newLine  ).GROUPBY(1, MainList)
                    self.data_base['globalIndex']   = len( self.NewLIST ) + self.data_base['starter']
                    self.MainStringTransform        = main_string
                    self.listTransform              = self.NewLIST 
                    
                    self.error = class_interpreter.EXTERNAL_CLASS_STATEMENT( None, self.data_base, self.newLine , self.master['class']).CLASSES(  tabulation = 1, 
                                                                        loop_list = self.listTransform )
                    if self.error is None: pass
                    else: pass                    
                elif self.data_base[ 'importation' ]   is not None:
                    self.newLine = self.line
                    self.modules = self.data_base[ 'importation' ] 
                    self.dataS, self.info, self.error = moduleMain.TREATMENT( self.modules, self.data_base, 
                                                                    self.newLine, 'linux' ).MODULE_MAIN( main_string, baseFileName = baseFileName )
                    if self.error is None:
                        self.error = modules.MODULES( self.data_base, self.newLine, self.dataS, self.info ).LOAD()
                        if self.error is None:
                            self.error = module_load_treatment.CLASSIFICATION( self.data_base, self.newLine ).CLASSIFICATION( self.data_base[ 'modulesImport' ], 
                                                                                    baseFileName = baseFileName, info = self.data_base[ 'importation' ])                    
                        else: pass
                    else: pass
                    self.data_base[ 'importation' ] = None
                   
        return  self._return_, self.key_return, self.error