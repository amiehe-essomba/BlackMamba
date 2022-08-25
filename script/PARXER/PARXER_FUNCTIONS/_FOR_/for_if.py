import  sys, os, re
from script                                             import control_string
from script.STDIN.WinSTDIN                              import stdin
from statement                                          import InternalStatement as IS
from statement                                          import externalIF as eIF
from script.PARXER.PARXER_FUNCTIONS._IF_                import IfError
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_unless, for_begin, for_switch, for_try, for_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.LEXER.FUNCTION                              import main
from script.STDIN.LinuxSTDIN                            import bm_configure as bm

class EXTERNAL_IF_STATEMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def IF_STATEMENT(self, 
                    bool_value  : bool, 
                    tabulation  : int = 1,
                    _type_      : str = 'conditional'
                    ):
        """
        :param bool_value:
        :param tabulation:
        :param _type_:  {default value = 'conditional'}
        :return:
        """
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_else             = 0
        #self.if_line                = self.line

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'if' ]
        self.color                  = bm.fg.rbg(0,255, 0)
        ke                          = bm.fg.rbg(255,255, 0)
        self.loop                   = []
        self.max_emtyLine           = 5

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            try:
                self.string, self.normal_string, self.active_tab, self.error = stdin.STDIN( self.data_base,
                                            self.if_line ).STDIN({ '0': ke, '1': self.color }, self.tabulation )

                if self.error is None:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                data_base=self.data_base, line=self.if_line).BLOCKS(tabulation = self.tabulation + 1, function = _type_,
                                                                                 interpreter = False)
                        if self.error  is None:
                            if self.get_block   == 'begin:'  :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                self._values_, self.error = for_begin.COMMENT_STATEMENT( master=self.master, data_base=self.data_base,
                                                        line=self.if_line  ).COMMENT( tabulation=self.tabulation + 1, color=self.color )
                                if self.error is None:
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else: break
                            elif self.get_block == 'if:'     :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                self._values_, self.error = INTERNAL_IF_STATEMENT( master=self.master,
                                            data_base=self.data_base, line=self.if_line ).IF_STATEMENT( bool_value= self.value,
                                                                                tabulation=self.tabulation + 1, _type_ = _type_)

                                if self.error is None:
                                    self.history.append('if')
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else:  break
                            elif self.get_block == 'try:'    :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )

                                self._values_, self.error = for_try.INTERNAL_TRY_STATEMENT( master=self.master,
                                        data_base=self.data_base, line=self.if_line ).TRY_STATEMENT(
                                                                    tabulation = self.tabulation + 1, _type_=_type_)

                                if self.error is None:
                                    self.history.append( 'try' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else: break
                            elif self.get_block == 'unless:' :
                                self.store_value.append(self.normal_string)
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_unless.EXTERNAL_UNLESS_STATEMENT( master=self.master,
                                            data_base=self.data_base, line=self.if_line ).UNLESS_STATEMENT( bool_value = self.value,
                                                                        tabulation = self.tabulation + 1, _type_ = _type_)
                                if self.error is None:
                                    self.history.append( 'unless' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else:  break
                            elif self.get_block == 'for:'    :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )

                                loop, tab, self.error = for_statement.EXTERNAL_FOR_STATEMENT( master=self.master,
                                                            data_base=self.data_base, line=self.if_line ).FOR_STATEMENT( tabulation = self.tabulation+1 )
                                if self.error is None:
                                    self.history.append( 'for' )
                                    self.space = 0
                                    self.loop.append( (loop, tab, self.error) )
                                else: break
                            elif self.get_block == 'switch:' :
                                self.store_value.append(self.normal_string)
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_switch.SWITCH_STATEMENT( master=self.master,
                                            data_base=self.data_base, line=self.if_line ).SWITCH( main_values=self.value,
                                                                            tabulation=self.tabulation + 1, _type_=_type_)

                                if self.error is None:
                                    self.history.append( 'switch' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else:  break
                            elif self.get_block == 'empty'   :
                                self.store_value.append(self.normal_string)
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append( (self.normal_string, True) )
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR4()
                                    break
                            elif self.get_block == 'any'     :
                                self.store_value.append( self.normal_string )
                                self.space = 0
                                self.error      = main.SCANNER(master=self.value, data_base=self.data_base,  line=self.if_line).SCANNER(_id_ = 1,
                                                                                            _type_= _type_, _key_=True)
                                if self.error is None: self.loop.append( (self.normal_string, True) )
                                else: break
                        else:  break
                    else:
                        self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                                        data_base=self.data_base, line=self.if_line).BLOCKS(tabulation=self.tabulation,
                                                        function=_type_, interpreter=False)

                        if self.error is None:
                            if   self.get_block == 'end:'  :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append( (self.normal_string, False) )
                                    break
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                    break
                            elif self.get_block == 'elif:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'elif' )
                                        self.store_value        = []
                                        self.loop.append( (self.normal_string, False) )
                                    else:
                                        self.error = IfError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                        break
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR1( 'else' )
                                    break
                            elif self.get_block == 'else:' :
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append( 'else' )
                                        self.loop.append( (self.normal_string, False) )
                                    else:
                                        self.error = IfError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ] )
                                        break

                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR3( 'else' )
                                    break
                            elif self.get_block == 'empty' :
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR4()
                                    break
                            else:
                                self.error = IfError.ERRORS( self.if_line ).ERROR4()
                                break
                        else: break
                else:
                    if self.tabulation == 1:  break
                    else:
                        self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string,
                                                normal_string=self.normal_string, data_base=self.data_base, line=self.if_line).BLOCKS(
                                                tabulation=self.tabulation, function=_type_, interpreter=False)
                        if self.error is None:
                            if   self.get_block == 'end:'   :
                                if self.store_value:
                                    del self.store_value[:]
                                    del self.history[:]
                                    self.loop.append((self.normal_string, False))
                                    break
                                else:
                                    self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                    break
                            elif self.get_block == 'elif:'  :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append('elif')
                                        self.store_value = []
                                        self.loop.append((self.normal_string, False))
                                    else:
                                        self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                        break
                                else:
                                    self.error = IfError.ERRORS(self.if_line).ERROR1('else')
                                    break
                            elif self.get_block == 'else:'  :
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else += 1
                                        self.key_else_activation = True
                                        self.store_value = []
                                        self.history.append('else')
                                        self.loop.append((self.normal_string, False))
                                    else:
                                        self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                        break

                                else:
                                    self.error = IfError.ERRORS(self.if_line).ERROR3('else')
                                    break
                            elif self.get_block == 'empty'  :
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append((self.normal_string, False))
                                else:
                                    self.error = IfError.ERRORS(self.if_line).ERROR4()
                                    break
                            else:
                                self.error = IfError.ERRORS(self.if_line).ERROR4()
                                break
                        else:  break
            except KeyboardInterrupt:
                self.error = IfError.ERRORS( self.if_line ).ERROR4()
                break

        ############################################################################

        return self.loop , self.error

class INTERNAL_IF_STATEMENT:
    def __init__(self, 
                master      :any, 
                data_base   :dict, 
                line        :int
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def IF_STATEMENT(self,
                    bool_value  : bool,
                    tabulation  : int,
                    _type_      : str = 'conditional'
                    ):
        """
        :param bool_value:
        :param tabulation:
        :param _type_: {default value = 'conditional'}
        :return:
        """
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_else             = 0
        self.if_line                = self.line

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'if' ]
        self.color                  = bm.fg.rbg(0,255, 255)
        ke                          = bm.fg.rbg(255,255,0)
        self.loop                   = []
        self.max_emtyLine           = 5

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.if_line ).STDIN({'0': ke, '1': self.color}, self.tabulation )
                if self.error is None:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string,
                                    normal_string=self.normal_string, data_base=self.data_base,  line=self.if_line).BLOCKS(
                                    tabulation=self.tabulation + 1, function=_type_, interpreter=False)

                        if self.error  is None:
                            if self.get_block   == 'begin:'     :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                self._values_, self.error = for_begin.COMMENT_STATEMENT( master=self.master, data_base=self.data_base,
                                                                 line=self.if_line).COMMENT( tabulation=self.tabulation + 1, color= self.color )
                                if self.error is None:
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else: break
                            elif self.get_block == 'if:'        :
                                self.store_value.append(self.normal_string)
                                self.loop.append( (self.normal_string, True) )
                                self._values_, self.error = EXTERNAL_IF_STATEMENT(  master=self.master,
                                        data_base=self.data_base, line=self.if_line).IF_STATEMENT( bool_value=self.value,
                                                                            tabulation=self.tabulation + 1, _type_=_type_)
                                if self.error is None:
                                    self.history.append( 'if' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else:  break
                            elif self.get_block == 'try:'       :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                self._values_, self.error = for_try.INTERNAL_TRY_STATEMENT( master=self.master,
                                        data_base=self.data_base, line=self.if_line ).TRY_STATEMENT( tabulation = self.tabulation + 1, _type_=_type_)

                                if self.error is None:
                                    self.history.append( 'try' )
                                    self.space = 0
                                    self.loop.append( self._values_ )

                                else: break
                            elif self.get_block == 'unless:'    :
                                self.store_value.append(self.normal_string)
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_unless.EXTERNAL_UNLESS_STATEMENT( master=self.master,
                                            data_base=self.data_base, line=self.if_line ).UNLESS_STATEMENT( bool_value=self.value,
                                                                        tabulation=self.tabulation + 1, _type_=_type_)
                                if self.error is None:
                                    self.history.append( 'unless' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else:  break
                            elif self.get_block == 'for:'       :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                loop, tab, self.error = for_statement.EXTERNAL_FOR_STATEMENT( master=self.master,
                                                            data_base=self.data_base, line=self.if_line ).FOR_STATEMENT( tabulation=self.tabulation+1 )
                                if self.error is None:
                                    self.history.append( 'for' )
                                    self.space = 0
                                    self.loop.append( (loop, tab, self.error) )
                                else: break
                            elif self.get_block == 'switch:'    :
                                self.store_value.append(self.normal_string)
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_switch.SWITCH_STATEMENT( master=self.master,
                                            data_base=self.data_base, line=self.if_line ).SWITCH( main_values=self.value,
                                                                        tabulation=self.tabulation + 1, _type_=_type_)
                                if self.error is None:
                                    self.history.append( 'switch' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else:  break
                            elif self.get_block == 'empty'      :
                                self.store_value.append(self.normal_string)
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append( self.normal_string )
                                else:  self.error = IfError.ERRORS( self.if_line ).ERROR4()
                            elif self.get_block == 'any'        :
                                self.store_value.append(self.normal_string)
                                self.space = 0
                                self.error      = main.SCANNER(master=self.value, data_base=self.data_base,
                                                            line=self.if_line).SCANNER(_id_ = 1, _type_= _type_, _key_=True)
                                if self.error is None: self.loop.append( (self.normal_string, True) )
                                else: break
                        else: break
                    else:
                        self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string,
                                normal_string=self.normal_string,  data_base=self.data_base,  line=self.if_line).BLOCKS(
                                                tabulation=self.tabulation, function=_type_, interpreter=False)

                        if self.error is None:
                            if self.get_block   == 'end:' :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append( (self.normal_string, False) )
                                    break
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                    break
                            elif self.get_block == 'elif:':
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'elif' )
                                        self.store_value        = []
                                        self.loop.append( (self.normal_string, False) )
                                    else:
                                        self.error = IfError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                        break
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR1( 'else' )
                                    break
                            elif self.get_block == 'else:':
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append('else')
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = IfError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR3( 'else' )
                                    break
                            elif self.get_block == 'empty':
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR4()
                                    break
                            else:
                                self.error = IfError.ERRORS( self.if_line ).ERROR4()
                                break
                        else:  break
                else:
                    self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string,
                                 normal_string=self.normal_string, data_base=self.data_base, line=self.if_line).BLOCKS(
                                                        tabulation=self.tabulation, function=_type_, interpreter=False)

                    if self.error is None:
                        if self.get_block   == 'end:' :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.loop.append( (self.normal_string, False) )
                                break
                            else:
                                self.error = IfError.ERRORS( self.if_line ).ERROR2(self.history[ -1 ])
                                break
                        elif self.get_block == 'elif:':
                            if self.key_else_activation == None:
                                if self.store_value:
                                    self.history.append( 'elif' )
                                    self.store_value            = []
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR2(self.history[ -1 ])
                                    break
                            else:
                                self.error = IfError.ERRORS( self.if_line ).ERROR1( 'else' )
                                break
                        elif self.get_block == 'else:':
                            if self.index_else < 1:
                                if self.store_value:
                                    self.index_else             += 1
                                    self.key_else_activation    = True
                                    self.store_value            = []
                                    self.history.append( 'else' )
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR2(self.history[ -1 ])
                                    break
                            else:
                                self.error = IfError.ERRORS( self.if_line ).ERROR3( 'else' )
                                break
                        elif self.get_block == 'empty':
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.loop.append( (self.normal_string, False) )
                            else:
                                self.error = ERRORS( self.if_line ).ERROR4()
                                break
                        else:
                            self.error = ERRORS( self.if_line ).ERROR4()
                            break
                    else:  break
            except KeyboardInterrupt:
                self.error = IfError.ERRORS( self.if_line ).ERROR4()
                break

        ############################################################################

        return self.loop , self.error

class EXTERNAL_IF_WINDOWS:
    def __init__(self,
                 master     : any,
                 data_base  : dict,
                 line       : int
                 ):

        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.analyse        = control_string.STRING_ANALYSE(self.data_base, self.line)

    def TERMINAL(self,
                 bool_value : bool,
                 tabulation : int,
                 _type_     : str = 'conditional',
                 c          : str = ''
                 ):

        """
        :param bool_value:
        :param tabulation:
        :param _type_:
        :param c:
        :return:
        """
        ######################################################
        
        self.color          = bm.fg.rbg(255,255,0)
        self.input          = '{}... {}'.format(self.color, bm.init.reset)
        self.length         = len(self.input)
        self.index          = self.length
        self.sub_length     = len('{}{}'.format( self.color, bm.init.reset))
        self.tab            = 1
        self.Input          = ''
        self.Index          = 0
        self.col            = []
        self.error          = None
        self.if_line        = self.line
        self.tabulation     = tabulation

        ######################################################
        self.string         = ''
        self.normal_string  = ''
        self.end            = ''
        self.store_value    = []
        self.index_else     = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.history                = ['if']
        self.loop                   = []
        self.max_emtyLine           = 5
        self.c                      = c
        self.previous_c             = c
        self.mainString             = ''
        self.mainIndex              = 0

        ############################################################################

        sys.stdout.write(bm.clear.line(2))
        sys.stdout.write(bm.move_cursor.LEFT(1000))
        sys.stdout.write(bm.string().syntax_highlight(name = self.input))
        sys.stdout.flush()

        while True:
            try:
                self.char = bm.read().readchar()
                if self.char  not in {10, 13}:
                    self.input      = self.input[: self.index] + chr(self.char) + self.input[self.index:]
                    self.mainString = self.mainString[: self.mainIndex] + chr(self.char) + self.mainString[  self.mainIndex:]
                    self.index      += 1
                    self.mainIndex  += 1

                elif self.char in {10, 13}:  # enter
                    self.if_line += 1
                    sys.stdout.write(bm.move_cursor.LEFT(1000))
                    self.clear_input = self.mainString
                    if self.clear_input:
                        ####################################################################
                        _, self._, self.err = self.analyse.BUILD_CON(string=self.clear_input,tabulation=self.tabulation)
                        if self.err is None:
                            if (self._ -1 )>= 0:
                                self.input = self.input[: self.length] + bm.words(string=self.mainString,  color=self.c).final()
                            else:
                                self.input = self.input[: self.length] + bm.words(string=self.mainString,  color=self.previous_c).final()
                        else: self.input = self.input[: self.length] + bm.words(string=self.mainString,  color=self.previous_c).final()

                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        sys.stdout.write(bm.move_cursor.UP(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(self.input)
                        sys.stdout.flush()
                        sys.stdout.write(bm.move_cursor.DOWN(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(bm.move_cursor.LEFT(1000))

                        ######################################################################

                        self.string, self.active_tab, self.error = self.analyse.BUILD_CON(string=self.clear_input, tabulation=self.tabulation)
                        
                        if self.error is None:
                            self.normal_string = self.analyse.BUILD_NON_CON(string=self.clear_input,tabulation=self.tabulation)
                            if self.active_tab is True :
                                if self.error is None:
                                    self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string,
                                                normal_string=self.normal_string,
                                                data_base=self.data_base, line=self.if_line).BLOCKS(
                                                tabulation=self.tabulation + 1, function=_type_,  interpreter=False)

                                    if self.error is None:
                                        if   self.get_block == 'begin:'     :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))
                                            self._values_, self.error = for_begin.COMMENT_WINDOWS(master=self.master,
                                                        data_base=self.data_base,
                                                        line=self.if_line).COMMENT( tabulation=self.tabulation+1, c=c)
                                            if self.error is None:
                                                self.history.append('begin')
                                                self.space = 0
                                                self.loop.append(self._values_)
                                            else:  break
                                        elif self.get_block == 'if:'        :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))
                                            self._values_, self.error = INTERNAL_IF_WINDOWS(master=self.master,
                                                 data_base=self.data_base, line=self.if_line).TERMINAL(
                                                bool_value=self.value, tabulation=self.tabulation + 1, _type_=_type_, c= c)

                                            if self.error is None:
                                                self.history.append('if')
                                                self.space = 0
                                                self.loop.append(self._values_)
                                            else: break
                                        elif self.get_block == 'try:'       :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))

                                            self._values_, self.error = for_try.INTERNAL_TRY_STATEMENT(
                                                master=self.master, data_base=self.data_base, line=self.if_line).TRY_STATEMENT(
                                                tabulation=self.tabulation + 1, _type_=_type_)

                                            if self.error is None:
                                                self.history.append('try')
                                                self.space = 0
                                                self.loop.append(self._values_)
                                            else: break
                                        elif self.get_block == 'unless:'    :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))
                                            self._values_, self.error = for_unless.EXTERNAL_UNLESS_STATEMENT(
                                                master=self.master,  data_base=self.data_base, line=self.if_line).UNLESS_STATEMENT(
                                                bool_value=self.value,  tabulation=self.tabulation + 1, _type_=_type_)
                                            if self.error is None:
                                                self.history.append('unless')
                                                self.space = 0
                                                self.loop.append(self._values_)
                                            else: break
                                        elif self.get_block == 'for:'       :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))

                                            loop, tab, self.error = for_statement.EXTERNAL_FOR_STATEMENT(
                                                master=self.master,
                                                data_base=self.data_base, line=self.if_line).FOR_STATEMENT(
                                                tabulation=self.tabulation + 1)
                                            if self.error is None:
                                                self.history.append('for')
                                                self.space = 0
                                                self.loop.append((loop, tab, self.error))
                                            else: break
                                        elif self.get_block == 'switch:'    :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))
                                            self._values_, self.error = for_switch.SWITCH_STATEMENT(master=self.master,
                                                            data_base=self.data_base, line=self.if_line).SWITCH(
                                                            main_values=self.value,  tabulation=self.tabulation + 1, _type_=_type_)

                                            if self.error is None:
                                                self.history.append('switch')
                                                self.space = 0
                                                self.loop.append(self._values_)
                                            else: break
                                        elif self.get_block == 'empty'      :
                                            self.store_value.append(self.normal_string)
                                            if self.space <= self.max_emtyLine:
                                                self.space += 1
                                                self.loop.append((self.normal_string, True))
                                            else:
                                                self.error = IfError.ERRORS(self.if_line).ERROR4()
                                                break
                                        elif self.get_block == 'any'        :
                                            self.store_value.append(self.normal_string)
                                            self.space = 0
                                            self.error = main.SCANNER(master=self.value, data_base=self.data_base,
                                                    line=self.if_line).SCANNER(_id_=1,  _type_=_type_,  _key_=True)
                                            if self.error is None: self.loop.append((self.normal_string, True))
                                            else: break
                                    else: break
                                else: break
                            else:
                                self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string,
                                         normal_string=self.normal_string, data_base=self.data_base,
                                         line=self.if_line).BLOCKS(tabulation=self.tabulation, function=_type_, interpreter=False)

                                if self.error is None:
                                    if   self.get_block == 'end:'   :
                                        if self.store_value:
                                            del self.store_value[:]
                                            del self.history[:]
                                            self.loop.append((self.normal_string, False))
                                            break
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                            break
                                    elif self.get_block == 'elif:'  :
                                        if self.key_else_activation == None:
                                            if self.store_value:
                                                self.history.append('elif')
                                                self.store_value = []
                                                self.loop.append((self.normal_string, False))
                                            else:
                                                self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                                break
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR1('else')
                                            break
                                    elif self.get_block == 'else:'  :
                                        if self.index_else < 1:
                                            if self.store_value:
                                                self.index_else += 1
                                                self.key_else_activation = True
                                                self.store_value = []
                                                self.history.append('else')
                                                self.loop.append((self.normal_string, False))
                                            else:
                                                self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                                break
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR3('else')
                                            break
                                    elif self.get_block == 'empty'  :
                                        if self.space <= self.max_emtyLine:
                                            self.space += 1
                                            self.loop.append((self.normal_string, False))
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                                            break
                                    else:
                                        self.error = IfError.ERRORS(self.if_line).ERROR4()
                                        break
                                else:  break
                        else:
                            self.normal_string = self.analyse.BUILD_NON_CON(string=self.clear_input,  tabulation=self.tabulation)
                            self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string,
                                        normal_string=self.normal_string,  data_base=self.data_base,
                                        line=self.if_line).BLOCKS(  tabulation=self.tabulation, function=_type_,
                                                                      interpreter=False)

                            if self.error is None:
                                if   self.get_block == 'end:' :
                                    if self.store_value:
                                        del self.store_value[:]
                                        del self.history[:]
                                        self.loop.append((self.normal_string, False))
                                        break
                                    else:
                                        self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                        break
                                elif self.get_block == 'elif:':
                                    if self.key_else_activation == None:
                                        if self.store_value:
                                            self.history.append('elif')
                                            self.store_value = []
                                            self.loop.append((self.normal_string, False))
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                            break
                                    else:
                                        self.error = IfError.ERRORS(self.if_line).ERROR1('else')
                                        break
                                elif self.get_block == 'else:':
                                    if self.index_else < 1:
                                        if self.store_value:
                                            self.index_else += 1
                                            self.key_else_activation = True
                                            self.store_value = []
                                            self.history.append('else')
                                            self.loop.append((self.normal_string, False))
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                            break
                                    else:
                                        self.error = IfError.ERRORS(self.if_line).ERROR3('else')
                                        break
                                elif self.get_block == 'empty':
                                    if self.space <= self.max_emtyLine:
                                        self.space += 1
                                        self.loop.append((self.normal_string, False))
                                    else:
                                        self.error = IfError.ERRORS(self.if_line).ERROR4()
                                        break
                                else:
                                    self.error = IfError.ERRORS(self.if_line).ERROR4()
                                    break
                            else: break
                    else:
                        if self.space <= self.max_emtyLine:
                            self.space += 1
                            self.loop.append((self.normal_string, False))
                        else:
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break

                    self.input      = '{}... {}'.format(self.color, bm.init.reset)
                    self.index      = self.length
                    self.mainString = ''
                    self.mainIndex  = 0
                elif self.char == 9:  # tabular
                    self.tabular = '\t'
                    self.input = self.input[: self.index] + self.tabular + self.input[self.index:]
                    self.index += 1

                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                sys.stdout.write(bm.clear.line(pos=0))
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                if self.index > 0:  sys.stdout.write(bm.move_cursor.RIGHT(pos=self.index - self.sub_length))
                else:  pass
                sys.stdout.flush()

            except KeyboardInterrupt:
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break

            except TypeError:
                self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                print(self._end_of_file_)
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break

        return self.loop, self.error

class INTERNAL_IF_WINDOWS:
    def __init__(self,
                 master     : any,
                 data_base  : dict,
                 line       : int
                 ):

        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.analyse        = control_string.STRING_ANALYSE(self.data_base, self.line)

    def TERMINAL(self,
                bool_value : bool,
                tabulation : int,
                _type_     : str = 'conditional',
                c          : str = ''
            ):

        """
        :param bool_value:
        :param tabulation:
        :param _type_:
        :param c:
        :return:
        """

        self.color          = bm.fg.rbg(255,255,0)
        self.input          = '{}... {}'.format(self.color, bm.init.reset)
        self.length         = len(self.input)
        self.index          = self.length
        self.sub_length     = len('{}{}'.format( self.color, bm.init.reset))
        self.tab            = 1
        self.Input          = ''
        self.Index          = 0
        self.col            = []
        self.if_line        = 0
        self.error          = None
        self.if_line        = self.line
        self.tabulation     = tabulation

        ######################################################
        self.string         = ''
        self.normal_string  = ''
        self.end            = ''
        self.store_value    = []
        self.index_else     = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.history                = ['if']
        self.loop                   = []
        self.max_emtyLine           = 5
        self.c                      = c
        self.previous_c             = c
        self.mainString             = ''
        self.mainIndex              = 0

        ############################################################################

        sys.stdout.write(bm.clear.line(2))
        sys.stdout.write(bm.move_cursor.LEFT(1000))
        sys.stdout.write(bm.string().syntax_highlight(name = self.input))
        sys.stdout.flush()

        while True:
            try:
                self.char = bm.read().readchar()
                if self.char not in {10, 13}:
                    self.input      = self.input[: self.index] + chr(self.char) + self.input[self.index:]
                    self.mainString = self.mainString[: self.mainIndex] + chr(self.char) + self.mainString[  self.mainIndex:]
                    self.index      += 1
                    self.mainIndex  += 1

                elif self.char in {10, 13}:  # enter
                    self.if_line += 1
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    self.s = self.input
                    self.clear_input = bm.chars().ansi_remove_chars(name=self.input[self.length:])

                    if self.clear_input:
                        ####################################################################
                        _, self._, self.err = self.analyse.BUILD_CON(string=self.clear_input, tabulation=self.tabulation)
                        if self.err is None:
                            if (self._ - 1) >= 0:
                                self.input = self.input[: self.length] + bm.words(string=self.mainString, color=self.c).final()
                            else:
                                self.input = self.input[: self.length] + bm.words(string=self.mainString, color=self.previous_c).final()
                        else:
                            self.input = self.input[: self.length] + bm.words(string=self.mainString,  color=self.previous_c).final()

                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        sys.stdout.write(bm.move_cursor.UP(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(self.input)
                        sys.stdout.flush()
                        sys.stdout.write(bm.move_cursor.DOWN(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(bm.move_cursor.LEFT(1000))
                        ######################################################################

                        self.string, self.active_tab, self.error = self.analyse.BUILD_CON(string=self.clear_input,
                                                                                    tabulation=self.tabulation)
                        if self.error is None:
                            self.normal_string = self.analyse.BUILD_NON_CON(string=self.clear_input,tabulation=self.tabulation)
                            if self.active_tab is True :
                                if self.error is None:
                                    self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string,
                                                normal_string=self.normal_string,
                                                data_base=self.data_base, line=self.if_line).BLOCKS(
                                                tabulation=self.tabulation + 1, function=_type_,  interpreter=False)

                                    if self.error is None:
                                        if   self.get_block == 'begin:'     :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))
                                            self._values_, self.error = for_begin.COMMENT_STATEMENT(master=self.master,
                                                        data_base=self.data_base,
                                                        line=self.if_line).COMMENT( tabulation=self.tabulation + 1, color=c)
                                            if self.error is None:
                                                self.history.append('begin')
                                                self.space = 0
                                                self.loop.append(self._values_)
                                            else:  break
                                        elif self.get_block == 'if:'        :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))
                                            self._values_, self.error = EXTERNAL_IF_WINDOWS(master=self.master,
                                                 data_base=self.data_base, line=self.if_line).TERMINAL(
                                                bool_value=self.value, tabulation=self.tabulation + 1, _type_=_type_, c=c)

                                            if self.error is None:
                                                self.history.append('if')
                                                self.space = 0
                                                self.loop.append(self._values_)
                                            else: break
                                        elif self.get_block == 'try:'       :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))

                                            self._values_, self.error = for_try.INTERNAL_TRY_STATEMENT(
                                                master=self.master, data_base=self.data_base, line=self.if_line).TRY_STATEMENT(
                                                tabulation=self.tabulation + 1, _type_=_type_)

                                            if self.error is None:
                                                self.history.append('try')
                                                self.space = 0
                                                self.loop.append(self._values_)
                                            else: break
                                        elif self.get_block == 'unless:'    :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))
                                            self._values_, self.error = for_unless.EXTERNAL_UNLESS_STATEMENT(
                                                master=self.master,  data_base=self.data_base, line=self.if_line).UNLESS_STATEMENT(
                                                bool_value=self.value,  tabulation=self.tabulation + 1, _type_=_type_)
                                            if self.error is None:
                                                self.history.append('unless')
                                                self.space = 0
                                                self.loop.append(self._values_)
                                            else: break
                                        elif self.get_block == 'for:'       :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))

                                            loop, tab, self.error = for_statement.EXTERNAL_FOR_STATEMENT(
                                                master=self.master,
                                                data_base=self.data_base, line=self.if_line).FOR_STATEMENT(
                                                tabulation=self.tabulation + 1)
                                            if self.error is None:
                                                self.history.append('for')
                                                self.space = 0
                                                self.loop.append((loop, tab, self.error))
                                            else: break
                                        elif self.get_block == 'switch:'    :
                                            self.store_value.append(self.normal_string)
                                            self.loop.append((self.normal_string, True))
                                            self._values_, self.error = for_switch.SWITCH_STATEMENT(master=self.master,
                                                            data_base=self.data_base, line=self.if_line).SWITCH(
                                                            main_values=self.value,  tabulation=self.tabulation + 1, _type_=_type_)

                                            if self.error is None:
                                                self.history.append('switch')
                                                self.space = 0
                                                self.loop.append(self._values_)
                                            else: break
                                        elif self.get_block == 'empty'      :
                                            self.store_value.append(self.normal_string)
                                            if self.space <= self.max_emtyLine:
                                                self.space += 1
                                                self.loop.append((self.normal_string, True))
                                            else:
                                                self.error = IfError.ERRORS(self.if_line).ERROR4()
                                                break
                                        elif self.get_block == 'any'        :
                                            self.store_value.append(self.normal_string)
                                            self.space = 0
                                            self.error = main.SCANNER(master=self.value, data_base=self.data_base,
                                                    line=self.if_line).SCANNER(_id_=1,  _type_=_type_,  _key_=True)
                                            if self.error is None: self.loop.append((self.normal_string, True))
                                            else: break
                                    else: break
                                else: break
                            else:
                                self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string,
                                         normal_string=self.normal_string, data_base=self.data_base,
                                         line=self.if_line).BLOCKS(tabulation=self.tabulation, function=_type_, interpreter=False)

                                if self.error is None:
                                    if   self.get_block == 'end:'   :
                                        if self.store_value:
                                            del self.store_value[:]
                                            del self.history[:]
                                            self.loop.append((self.normal_string, False))
                                            break
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                            break
                                    elif self.get_block == 'elif:'  :
                                        if self.key_else_activation == None:
                                            if self.store_value:
                                                self.history.append('elif')
                                                self.store_value = []
                                                self.loop.append((self.normal_string, False))
                                            else:
                                                self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                                break
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR1('else')
                                            break
                                    elif self.get_block == 'else:'  :
                                        if self.index_else < 1:
                                            if self.store_value:
                                                self.index_else += 1
                                                self.key_else_activation = True
                                                self.store_value = []
                                                self.history.append('else')
                                                self.loop.append((self.normal_string, False))
                                            else:
                                                self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                                break
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR3('else')
                                            break
                                    elif self.get_block == 'empty'  :
                                        if self.space <= self.max_emtyLine:
                                            self.space += 1
                                            self.loop.append((self.normal_string, False))
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                                            break
                                    else:
                                        self.error = IfError.ERRORS(self.if_line).ERROR4()
                                        break
                                else:  break
                        else:
                            if self.tabulation == 1:  break
                            else:
                                self.normal_string = self.analyse.BUILD_NON_CON(string=self.clear_input, tabulation=self.tabulation)
                                self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string,
                                         normal_string=self.normal_string, data_base=self.data_base,
                                          line=self.if_line).BLOCKS(  tabulation=self.tabulation, function=_type_, interpreter=False)

                                if self.error is None:
                                    if   self.get_block == 'end:' :
                                        if self.store_value:
                                            del self.store_value[:]
                                            del self.history[:]
                                            self.loop.append((self.normal_string, False))
                                            break
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                            break
                                    elif self.get_block == 'elif:':
                                        if self.key_else_activation == None:
                                            if self.store_value:
                                                self.history.append('elif')
                                                self.store_value = []
                                                self.loop.append((self.normal_string, False))
                                            else:
                                                self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                                break
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR1('else')
                                            break
                                    elif self.get_block == 'else:':
                                        if self.index_else < 1:
                                            if self.store_value:
                                                self.index_else += 1
                                                self.key_else_activation = True
                                                self.store_value = []
                                                self.history.append('else')
                                                self.loop.append((self.normal_string, False))
                                            else:
                                                self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                                break
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR3('else')
                                            break
                                    elif self.get_block == 'empty':
                                        if self.space <= self.max_emtyLine:
                                            self.space += 1
                                            self.loop.append((self.normal_string, False))
                                        else:
                                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                                            break
                                    else:
                                        self.error = IfError.ERRORS(self.if_line).ERROR4()
                                        break
                                else:  break
                    else:
                        if self.space <= self.max_emtyLine:
                            self.space += 1
                            self.loop.append((self.normal_string, False))
                        else:
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break

                    self.input      = '{}... {}'.format(self.color, bm.init.reset)
                    self.index      = self.length
                    self.mainString = ''
                    self.mainIndex  = 0

                elif self.char == 9:  # tabular
                    self.tabular = '\t'
                    self.input = self.input[: self.index] + self.tabular + self.input[self.index:]
                    self.index += 4

                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                sys.stdout.write(bm.clear.line(pos=0))
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                if self.index > 0:  sys.stdout.write(bm.move_cursor.RIGHT(pos=self.index - self.sub_length))
                else:  pass
                sys.stdout.flush()

            except KeyboardInterrupt:
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break

            except TypeError:
                self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                print(self._end_of_file_)
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break

        return self.loop, self.error



