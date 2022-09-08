from script.PARXER                                          import numerical_value
from script.PARXER.VAR_NAME                                 import get_var_name
from script.PARXER.PRINT                                    import show_data
from script.LEXER.FUNCTION                                  import print_value
from statement                                              import mainStatement as MS
from script.STDIN.WinSTDIN                                  import stdin
from script.PARXER.PARXER_FUNCTIONS._IF_                    import if_statement, if_inter
from script.PARXER.PARXER_FUNCTIONS._IF_                    import end_else_elif
from script.PARXER.PARXER_FUNCTIONS._UNLESS_                import unless_statement, unless_interpreter
from script.PARXER.PARXER_FUNCTIONS._UNLESS_                import end_else_elif as _end_else_elif_
from script.PARXER.PARXER_FUNCTIONS._SWITCH_                import end_case_default, switch_statement
from script.PARXER.PARXER_FUNCTIONS.WHILE                   import while_statement
from script.PARXER.PARXER_FUNCTIONS._FOR_                   import end_for_else, for_interpreter
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_         import comment as cmt
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_         import cmt_interpreter as cmt_int
from script.PARXER.PARXER_FUNCTIONS._TRY_                   import try_statement
from script.PARXER.PARXER_FUNCTIONS._FOR_                   import for_try
from script.PARXER.PARXER_FUNCTIONS._FOR_.IF.WINDOWS        import WindowsIF as wIF
from script.PARXER.PARXER_FUNCTIONS._FOR_.UNLESS            import WindowsUnless as wU
from script.PARXER.PARXER_FUNCTIONS._FOR_.SWITCH.WINDOWS    import WindowsSwitch as WSw
from script.PARXER.PARXER_FUNCTIONS._FOR_                   import for_block_treatment, for_begin
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS               import def_interpreter
from script.PARXER.PARXER_FUNCTIONS.CLASSES                 import class_interpreter
from script.PARXER                                          import module_load_treatment 
from script.STDIN.LinuxSTDIN                                import bm_configure as bm
from src.modulesLoading                                     import modules, moduleMain 
from script.PARXER.PARXER_FUNCTIONS._FOR_.WHILE.WINDOWS     import WindowsWhile as WWh
from script.PARXER.PARXER_FUNCTIONS._FOR_.BEGIN.WINDOWS     import begin
from src.functions.windows                                  import windowsDef as WD
from src.classes.windows                                    import windowsClass as WC


class ASSEMBLY( ):
    def __init__(self, master: dict, data_base: dict, line: int ):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.num_parxer     = numerical_value
        self.variables      = self.data_base[ 'variables' ][ 'vars' ]
        self._values_       = self.data_base[ 'variables' ][ 'values' ]
        self.global_vars    = self.data_base[ 'global_vars' ][ 'vars' ]
        self.global_values  = self.data_base[ 'global_vars' ][ 'values' ]
        
        try:
            self._if_egal_  = self.master[ 'if_egal' ]
            self.main_value = self.master[ 'all_data' ]
        except: self._if_egal_ = 'comment'


    def GLOBAL_ASSEMBLY(self, 
            main_string     : str, 
            interpreter     : bool  = False, 
            term            : str   = ''
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
                self.error = ASSEMBLY( self.master, self.data_base, self.line).ASSEMBLY( main_string, interpreter )
                self.data_base['matrix'] = None
            elif self.master[ 'function' ] == 'if'      :
                self._return_, self.error = MS.MAIN(master = main_string, data_base=self.data_base,
                                line=self.line).MAIN(typ = 'if', opposite = False, interpreter = True, function = None)
                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.listTransform, self.error = wIF.EXTERNAL_IF_WINDOWS(data_base=self.data_base,
                                    line=self.line, term=term).TERMINAL(bool_value = self._return_, tabulation=1, _type_='conditional',
                                    c = bm.fg.rbg(255,255,255) )

                    if self.error is None:
                        self.newLine                    = self.line 
                        self.error = if_statement.EXTERNAL_IF_LOOP_STATEMENT( None , self.data_base,
                                            self.newLine ).IF_STATEMENT( self._return_, 1, self.listTransform )
                        
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
            elif self.master[ 'function' ] == 'unless'  :
                self._return_, self.error = MS.MAIN( main_string, self.data_base, self.line).MAIN(  typ='unless',
                                        opposite=True, interpreter=True )
               
                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.listTransform, self.error = wU.EXTERNAL_UNLESS_WINDOWS(data_base=self.data_base,
                                    line=self.line, term=term).TERMINAL(bool_value = self._return_,
                                    tabulation=1, _type_='conditional', c = bm.fg.rbg(255,255,255) )
                    if self.error is None:
                        self.newLine                    = self.line 
                        self.error = unless_statement.EXTERNAL_UNLESS_FOR_STATEMENT( None , self.data_base,
                                            self.newLine ).UNLESS_STATEMENT( self._return_, 1, self.listTransform )
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
                self._return_, self.error = MS.MAIN(main_string, self.data_base, self.line).MAIN(typ='switch',
                                                opposite=False, interpreter=True)
                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.listTransform, self.error = WSw.EXTERNAL_SWITCH_WINDOWS(data_base=self.data_base,
                                    line=self.line, term=term).TERMINAL(bool_value = self._return_,
                                    tabulation=1, _type_='conditional',  c = bm.fg.rbg(255,255,255) )
                    if self.error is None:
                        self.newLine                    = self.line 
                        self.error = switch_statement.SWITCH_LOOP_STATEMENT( None , self.data_base,
                                            self.newLine ).SWITCH( self._return_, 1, self.listTransform )
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
                self.value, self.name, self.operator, self.error = end_for_else.MAIN_FOR( self.master, self.data_base,
                                                                self.line ).BOCKS( main_string )

                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.got_errors, self.error = for_block_treatment.TREATMENT( self.data_base,
                                                    self.line ).FOR( main_string, self.value, self.name )

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
            elif self.master[ 'function' ] == 'while'   :
                self._return_, self.error = MS.MAIN(master = main_string, data_base=self.data_base,
                                line=self.line).MAIN(typ = 'while', opposite = False, interpreter = True, function = 'loop')
                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.listTransform, self.error = WWh.EXTERNAL_WHILE_WINDOWS(data_base=self.data_base,
                                    line=self.line, term=term).TERMINAL(bool_value = self._return_, tabulation=1, _type_='loop',
                                    c = bm.fg.rbg(255,255,255) )

                    if self.error is None:
                        self.newLine                    = self.line 
                        self.error = while_statement.EXTERNAL_WHILE_LOOP_STATEMENT( None , self.data_base,
                                            self.newLine ).WHILE_STATEMENT( self._return_, 1, self.listTransform, main_string = main_string )
                        
                        if self.error is None:  self.data_base['print'] = []
                        else: pass 
                    else: pass
                else: pass
            else: print(self.master)
        else:
            if   self.master[ 'begin'  ] is True    :
                self.newLine                   = self.line
                self.listTransform, self.error = begin.COMMENT_WINDOWS(data_base=self.data_base,
                                        line=self.line, term=term).COMMENT( tabulation=1, c=bm.fg.rbg(153, 153, 255))
                if self.error is None:
                    self.error = cmt.COMMENT_LOOP_STATEMENT( None, self.data_base, self.newLine ).COMMENT( 1, self.listTransform )
                else: pass              
            elif self.master[ 'delete' ] is True    : pass
            elif self.master[ 'global' ] is True    : pass
            elif self.master[ 'print'  ] is not None: pass
            elif self.master[ 'transformation' ] is not None: pass
            elif self.master[ 'try' ] is True:
                self.data_base[ 'print' ] = []
                self.newLine                    = self.line 

                self.listTransform, self.error = for_try.EXTERNAL_TRY_STATEMENT( None,
                                            self.data_base, self.newLine ).TRY_STATEMENT( tabulation = 1)
            
                if self.error is None:
                    self._finally_key_, self.error = try_statement.EXTERNAL_TRY_FOR_STATEMENT(None,
                                                        self.data_base, self.newLine ).TRY_STATEMENT(1, self.listTransform)
                    #self._, self.error = try_statement.EXTERNAL_TRY_STATEMENT(None,
                    #                                    self.data_base, self.line ).TRY_STATEMENT(tabulation = 1)
                    if self.error is None:
                        if self.data_base[ 'print' ] is not None:
                            self.list_of_values = self.data_base[ 'print' ]
                            for i, value in enumerate( self.list_of_values ):
                                if i < len( self.list_of_values) - 1:
                                    print_value.PRINT_PRINT( value ).PRINT_PRINT( key = False, loop = True )
                                else:
                                    print_value.PRINT_PRINT( value ).PRINT_PRINT( key = False, loop = True )
                        else:  pass
                    else: pass
                else: pass
            else:
                if   self.data_base[ 'current_func' ]  is not None:
                    self.error = WD.EXTERNAL_DEF_WINDOWS(data_base=self.data_base, 
                                        line=self.line, term=term).TERMINAL(tabulation=1, c=bm.fg.rbg(255,255,255) )
                    if self.error is None: pass
                    else: pass
                elif self.data_base[ 'current_class' ] is not None:
                    self.error = WC.EXTERNAL_CLASS_WINDOWS(data_base=self.data_base, 
                                        line=self.line, extra=self.master['class'], term=term).TERMINAL(tabulation=1, c=bm.fg.rbg(255,255,255) )
                    if self.error is None: pass
                    else: pass
                elif self.data_base[ 'importation' ]   is not None:
                    self.modules = self.data_base[ 'importation' ] 
                    self.dataS, self.info, self.error = moduleMain.TREATMENT( self.modules, self.data_base,  self.line ).MODULE_MAIN( main_string )
                    if self.error is None:
                        self.error = modules.MODULES( self.data_base, self.line, self.dataS, self.info ).LOAD()
                        if self.error is None:
                            self.error = module_load_treatment.CLASSIFICATION( self.data_base, self.line ).CLASSIFICATION( self.data_base[ 'modulesImport' ], 
                                                                                    info = self.data_base[ 'importation' ])

                        else: pass
                    else: pass
                    
                    self.data_base[ 'importation' ] = None
                   
        return  self._return_, self.key_return, self.error