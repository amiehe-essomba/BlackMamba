from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import end
from script.STDIN.WinSTDIN                              import stdin
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:  from CythonModules.Windows                        import fileError as fe 
except ImportError: from CythonModules.Linux            import fileError as fe

ae = bm.fg.cyan_L
ve = bm.fg.rbg(0,0,0)
we = bm.fg.rbg(255,255,255)

class COMMENT_STATEMENT:
    def __init__(self, master:any, data_base:dict, line:int):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string

    def COMMENT(self, tabulation : int = 0, color : str = ''):
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = [ ]
        self.if_line                = 0

        ############################################################################

        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'comment' ]
        self.color                  = ve
        self.max                    = 1000
        self.locked                 = False
        self.comment_storage        = []
        self.comment_name           = None
        self.loop                   = []
    
        ############################################################################

        while self.end != 'end:' :
            self.line       += 1

            try:
                if self.locked is False:
                    pass
                else:
                    self.color = color

                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.line ).STDIN({ '0': ae, '1': self.color }, self.tabulation, _type_='cmt' )
                if self.error is None:
                    if self.active_tab is True:
                        if self.locked is False:
                            self.get_block, self.value, self.error = end.INTERNAL_BLOCKS( self.string,
                                            self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )

                            if self.error  is None:
                                self.comment_storage.append( self.value )

                                if self.get_block == 'empty':
                                    if self.space <= self.max:
                                        self.space += 1
                                        self.loop.append((self.normal_string, True))
                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break

                                elif self.get_block == 'any':
                                    self.store_value.append( self.normal_string )
                                    self.space = 0
                                    self.loop.append((self.normal_string, True))

                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break

                            else: break
                        else:
                            self.error = ERRORS( self.line ).ERROR4()
                            break

                    else:
                        self.get_block, self.value, self.error = end.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'     :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append((self.normal_string, False))
                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR2( )
                                    break

                            elif self.get_block == 'save:'    :
                                if self.store_value:
                                    if self.locked is False:
                                        self.locked = True
                                        self.comment_name = self.value
                                        self.loop.append((self.normal_string, False))
                                    else:
                                        self.error = ERRORS( self.line ).ERROR3()
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR2( )
                                    break
                                
                            elif self.get_block == 'empty'    :
                                if self.space <= self.max:
                                    self.space += 1
                                    self.loop.append((self.normal_string, False))
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break

                            else:
                                self.error = ERRORS( self.line ).ERROR4()
                                break

                        else:  break

                else:
                    if self.tabulation == 1:  break

                    else:
                        self.get_block, self.value, self.error = end.EXTERNAL_BLOCKS(self.string,
                                            self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'    :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append((self.normal_string, False))
                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR2( )
                                    break

                            elif self.get_block == 'save:'   :
                                if self.store_value:
                                    
                                    if self.locked is False:
                                        self.locked = True
                                        self.comment_name = self.value
                                        self.loop.append((self.normal_string, False))
                                    else:
                                        self.error = ERRORS( self.line ).ERROR3()
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR2( )
                                    break

                            elif self.get_block == 'empty'   :
                                if self.space <= self.mas:
                                    self.space += 1
                                    self.loop.append((self.normal_string, False))
                                else:
                                    self.error = ERRORS(  self.line ).ERROR4()
                                    break
                            
                            else:
                                self.error = ERRORS( self.line ).ERROR4()
                                break

                        else: break

            except EOFError:
                self.error = ERRORS( self.line ).ERROR4()
                break

            except KeyboardInterrupt:
                self.error = ERRORS( self.line ).ERROR4()
                break

        #############################################################################

        return self.loop, self.error

class ERRORS:
    def __init__(self, line: int):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,
                                                                                                       self.cyan, string) + error

        return self.error+self.reset
      
    def ERROR2(self):
        error = '{}<< begin >> {}statement block is {}EMPTY. {}line: {}{}'.format(self.red, self.white, self.yellow, 
                                                                                  self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. '.format( self.white ) + error

        return self.error+self.reset

    def ERROR3(self):
        error = '{}many {}<< save >> {}statement blocks. {}line: {}{}'.format(self.red, self.blue, self.yellow,
                                                                              self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. '.format(self.white) + error

        return self.error+self.reset

    def ERROR4(self):
        self.error =  fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                    self.white, self.yellow, self.line )
        return self.error+self.reset