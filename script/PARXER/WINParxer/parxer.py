from script.PARXER.PRINT                                    import show_data
from script.LEXER.FUNCTION                                  import print_value
from statement                                              import mainStatement        as MS
from script.PARXER.PARXER_FUNCTIONS._UNLESS_                import unless_statement
from script.PARXER.PARXER_FUNCTIONS._IF_                    import if_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_                import switch_statement
from script.PARXER.PARXER_FUNCTIONS.WHILE                   import while_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_         import comment              as cmt
from script.PARXER.PARXER_FUNCTIONS._TRY_                   import try_statement
from script.PARXER.PARXER_FUNCTIONS._FOR_.IF.WINDOWS        import WindowsIF            as wIF
from script.PARXER.PARXER_FUNCTIONS._FOR_.UNLESS            import WindowsUnless        as wU
from script.PARXER.PARXER_FUNCTIONS._FOR_.SWITCH.WINDOWS    import WindowsSwitch        as WSw
from script.PARXER.PARXER_FUNCTIONS._FOR_                   import for_block_treatment
from script.PARXER                                          import module_load_treatment 
from script.STDIN.LinuxSTDIN                                import bm_configure         as bm
from src.modulesLoading                                     import modules, moduleMain 
from script.PARXER.PARXER_FUNCTIONS._FOR_.WHILE.WINDOWS     import WindowsWhile         as WWh
from script.PARXER.PARXER_FUNCTIONS._FOR_.BEGIN.WINDOWS     import begin
from src.functions.windows                                  import windowsDef           as WD
from src.classes.windows                                    import windowsClass         as WC
from script.PARXER                                          import partial_assembly
from script.PARXER.PARXER_FUNCTIONS._FOR_.FOR.WIN           import WindowsFor           as wFor
from script.PARXER.PARXER_FUNCTIONS._FOR_.TRY.WIN           import WindowsTry           as wTry
from loop                                                   import mainFor
from CythonModules.Windows.PARTIAL_PARSER                   import partial

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
        
    def GLOBAL_ASSEMBLY(self, 
            main_string     : str,              # main string 
            interpreter     : bool  = False,    # interpreter is activated
            term            : str   = '',       # terminal type
            traceback       : dict  = {},       # trace back for modules loaded
            callbacks       : dict  = {}        # history of callbacks
            ):
        
        # value to return 
        self._return_           = None
        # key lexer 
        self.key_return         = None
        # error 
        self.error              = None
        # if function if activated 
        self.active_function    = None
        # key lexer items 
        self.all_data_vars      = list( self.master.keys() )
        # list of function which can be returned by the lexer 
        self.structure          = [ 'begin', 'if', 'loop_for', 'loop_until', 'loop_while', 'try', 'unless', 'switch' ]

        # checking data 
        for i , data in enumerate( self.all_data_vars ):
            # not assigned values 
            if data != 'if_egal':
                if self.master[ data ] is None: pass
                else:
                    self.active_function = data
                    break
            else: pass

        # when active_function detected some functions 
        if self.active_function == 'all_data':
            # numerical calculation 
            if   self.master[ 'function' ] is None      :
                self.error = partial_assembly.ASSEMBLY( self.master, self.data_base, self.line).ASSEMBLY( main_string, interpreter )
                #self.error = partial.ASSEMBLY( self.master, self.data_base, self.line).ASSEMBLY( main_string, interpreter )
                self.data_base['matrix'] = None
            # active_function detected if function 
            elif self.master[ 'function' ] == 'if'      :
                self.newLine                    = self.line 
                # computing the boolean value
                self._return_, self.error = MS.MAIN(master = main_string, data_base=self.data_base,
                                line=self.newLine).MAIN(typ = 'if', opposite = False, interpreter = True, function = None)
                if self.error is None:
                    # initialization 
                    self.data_base[ 'print' ] = []
                    # running if IDE
                    self.listTransform, self.error = wIF.EXTERNAL_IF_WINDOWS(data_base=self.data_base,
                                    line=self.newLine, term=term).TERMINAL(bool_value = self._return_, tabulation=1, _type_='conditional',
                                    c = bm.fg.rbg(255,255,255), callbacks=callbacks )

                    if self.error is None:
                        # runnnig the interpreter 
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
            # active_function detected unless function 
            elif self.master[ 'function' ] == 'unless'  :
                self.newLine                    = self.line 
                self._return_, self.error       = MS.MAIN( main_string, self.data_base, self.newLine).MAIN(  typ='unless',
                                        opposite=True, interpreter=True )
               
                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.listTransform, self.error = wU.EXTERNAL_UNLESS_WINDOWS(data_base=self.data_base,
                                    line=self.newLine, term=term).TERMINAL(bool_value = self._return_,
                                    tabulation=1, _type_='conditional', c = bm.fg.rbg(255,255,255), callbacks=callbacks )
                    if self.error is None:
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
            # active_function detected switch  function 
            elif self.master[ 'function' ] == 'switch'  :
                self.newLine                    = self.line 
                self._return_, self.error = MS.MAIN(main_string, self.data_base, self.newLine).MAIN(typ='switch',
                                                opposite=False, interpreter=True)
                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.listTransform, self.error = WSw.EXTERNAL_SWITCH_WINDOWS(data_base=self.data_base,
                                    line=self.newLine, term=term).TERMINAL(bool_value = self._return_,
                                    tabulation=1, _type_='conditional',  c = bm.fg.rbg(255,255,255), callbacks=callbacks )
                    if self.error is None:
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
            # active_function detected for function 
            elif self.master[ 'function' ] == 'for'     :
                self.newLine                    = self.line 
                self._, self.value, self.error =  mainFor.FOR_BLOCK(normal_string =main_string, data_base=self.data_base, 
                                                line=self.newLine).FOR( function = 'loop', interpreter = interpreter,   locked=False)

                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.listTransform, self.tab, self.error = wFor.EXTERNAL_FOR_WINDOWS(data_base=self.data_base,
                                    line=self.newLine , term=term).TERMINAL( tabulation=1, _type_='loop', c = bm.fg.rbg(255,255,255) )
                                    
                    if self.error is None:
                        self.got_errors, self.error = for_block_treatment.TREATMENT( self.data_base, self.newLine ).FOR( main_string, 
                                self.value['value'], self.value['variable'], loop_list = (self.listTransform, self.tab, self.error) )


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

                                    if self.got_errors: pass #print( self.got_errors[ i ])
                                    else: pass
                            else: pass
                        else: pass
                    self.data_base['print'] = []

                else: self.error = self.error
            # active_function detected while function 
            elif self.master[ 'function' ] == 'while'   :
                self.newLine                    = self.line 
                self._return_, self.error = MS.MAIN(master = main_string, data_base=self.data_base,
                                line=self.newLine).MAIN(typ = 'while', opposite = False, interpreter = True, function = 'loop')
                if self.error is None:
                    self.data_base[ 'print' ] = []
                    self.listTransform, self.error = WWh.EXTERNAL_WHILE_WINDOWS(data_base=self.data_base,
                                    line=self.line, term=term).TERMINAL(bool_value = self._return_, tabulation=1, _type_='loop',
                                    c = bm.fg.rbg(255,255,255), callbacks=callbacks )

                    if self.error is None:
                        self.newLine                    = self.line 
                        self.error = while_statement.EXTERNAL_WHILE_LOOP_STATEMENT( None , self.data_base,
                                            self.newLine ).WHILE_STATEMENT( self._return_, 1, self.listTransform, main_string = main_string )
                        
                        if self.error is None:  self.data_base['print'] = []
                        else: pass 
                    else: pass
                else: pass
            else: pass
        # no functions detected 
        else:
            # multi-line comments 
            if   self.master[ 'begin'  ] is True        :
                self.newLine                   = self.line
                self.listTransform, self.error = begin.COMMENT_WINDOWS(data_base=self.data_base,
                                        line=self.newLine, term=term).COMMENT( tabulation=1, c=bm.fg.rbg(153, 153, 255))
                if self.error is None:
                    self.error = cmt.COMMENT_LOOP_STATEMENT( None, self.data_base, self.newLine ).COMMENT( 1, self.listTransform )
                else: pass              
            # delecting variable
            elif self.master[ 'delete' ] is True        : pass
            # global variable
            elif self.master[ 'global' ] is True        : pass
            # printing values
            elif self.master[ 'print'  ] is not None    : pass
            # modules transformed
            elif self.master[ 'transformation' ] is not None: pass
            # try statment 
            elif self.master[ 'try' ] is True:
                self.data_base[ 'print' ] = []
                self.newLine                    = self.line 
                self.listTransform, self.error = wTry.EXTERNAL_TRY_WINDOWS(data_base=self.data_base, line=self.newLine, 
                                term=term ).TERMINAL(tabulation=1, _type_ = 'try', c=bm.fg.rbg(255,255,255), callbacks=callbacks )
                if self.error is None:
                    self._finally_key_, self.error = try_statement.EXTERNAL_TRY_FOR_STATEMENT(None,
                                                        self.data_base, self.newLine ).TRY_STATEMENT(1, self.listTransform)
                    if self.error is None:
                        if self.data_base[ 'print' ] is not None:
                            self.list_of_values = self.data_base[ 'print' ]
                            for i, value in enumerate( self.list_of_values ):
                                if i < len( self.list_of_values) - 1:
                                    print_value.PRINT_PRINT( value, data_base=self.data_base ).PRINT_PRINT( key = False, loop = True )
                                else:
                                    print_value.PRINT_PRINT( value, data_base=self.data_base ).PRINT_PRINT( key = False, loop = True )
                        else:  pass
                    else: pass
                else: pass    
            else:
                # running def
                if   self.data_base[ 'current_func' ]  is not None:
                    self.error = WD.EXTERNAL_DEF_WINDOWS(data_base=self.data_base, 
                                        line=self.line, term=term).TERMINAL(tabulation=1, c=bm.fg.rbg(255,255,255) )
                    if self.error is None: pass
                    else: pass
                # runnnig classes
                elif self.data_base[ 'current_class' ] is not None:
                    self.error = WC.EXTERNAL_CLASS_WINDOWS(data_base=self.data_base, 
                                        line=self.line, extra=self.master['class'], term=term).TERMINAL(tabulation=1, c=bm.fg.rbg(255,255,255) )
                    if self.error is None: pass
                    else: pass
                # running modules importation 
                elif self.data_base[ 'importation' ]   is not None:
                    self.modules = self.data_base[ 'importation' ] 
                    # checking the modules loaded exist in Lib or current directory
                    self.dataS, self.info, self.error = moduleMain.TREATMENT( self.modules, self.data_base,  self.line ).MODULE_MAIN( main_string )
                    if self.error is None:
                        # load module defined 
                        self.error = modules.MODULES( self.data_base, self.line, self.dataS, self.info ).LOAD()
                        if self.error is None:
                            # storing the modules loaded
                            self.error = module_load_treatment.CLASSIFICATION( self.data_base, 
                                    self.line ).CLASSIFICATION( self.data_base[ 'modulesImport' ], 
                                    info = self.data_base[ 'importation' ], trace=traceback )
                        else: pass
                    else: pass
                    
                    self.data_base[ 'importation' ] = None
                   
        return  self._return_, self.key_return, self.error