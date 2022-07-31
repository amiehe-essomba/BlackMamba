from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import end
from script.STDIN.WinSTDIN                              import stdin
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:  from CythonModules.Windows                        import fileError as fe 
except ImportError: from CythonModules.Linux            import fileError as fe

class COMMENT_STATEMENT:
    def __init__(self, master:any, data_base:dict, line:int):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string

    def COMMENT(self, tabulation : int = 0, loop_list: any = None):
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
        self.max                    = 100
        self.locked                 = False
        self.comment_storage        = []
        self.comment_name           = None
        self.loop_list              = loop_list
        
        ############################################################################

        if self.loop_list:
            for j, _string_ in enumerate(self.loop_list):
                
                self.if_line    += 1
                self.line       += 1
                
                k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)
                if k == 0: k = 1
                else: pass

                try:
                    self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                self.line ).STDIN_FOR_INTERPRETER( k, _string_ )
            
                    if self.error is None:
                        if self.active_tab is True:
                            if self.locked is False:
                                self.get_block, self.value, self.error = end.INTERNAL_BLOCKS( self.string,
                                                self.normal_string, self.data_base, self.line ).BLOCKS( k + 1 )

                                if self.error  is None:
                                    self.comment_storage.append( self.value )

                                    if self.get_block == 'empty':
                                        if self.space <= self.max:
                                            self.space += 1
                                        else:
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break

                                    elif self.get_block == 'any':
                                        self.store_value.append( self.normal_string )
                                        self.space = 0

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

                                        break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( )
                                        break

                                elif self.get_block == 'save:'    :
                                    if self.locked is False:
                                        self.locked = True
                                        self.comment_name = self.value

                                    else:
                                        self.error = ERRORS( self.line ).ERROR3()
                                        break

                                elif self.get_block == 'empty'    :
                                    if self.space <= self.max: self.space += 1
                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break

                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break
                            else: break
                    else: break
                        
                except EOFError:
                    self.error = ERRORS( self.line ).ERROR4()
                    break

            self.error = COMMENT_TRANSFORMS( self.comment_storage, self.data_base, self.error,
                                            self.comment_name ).TRANSTORMATION()
        else: self.error  = ERRORS( self.line ).ERROR4()
        #############################################################################

        return self.error

class COMMENT_TRANSFORMS:
    def __init__(self, master:list, data_base: dict, error: str, name: any ):
        self.master         = master
        self.error          = error
        self.name           = name
        self.data_base      = data_base

    def TRANSTORMATION(self):
        if self.error is None:
            self.long_chaine    = ""
            if self.master:
                for i, str_ in enumerate(self.master ):
                    if i < len( self.master ) - 1:
                        string = '{}\n'.format( str_ )
                        self.long_chaine += string
                    else:
                        string = "{}".format(str_)
                        self.long_chaine += string

                self.long_chaine = self.long_chaine.replace( '"', "'")
                self.long_chaine = '"'+str( self.long_chaine )+'"'

            else: pass

            if self.name is None:
                pass
            else:
                self.vars   = self.data_base[ 'variables' ][ 'vars' ]
                self.values = self.data_base[ 'variables' ][ 'values' ]

                if self.name in self.vars:
                    self.idd = self.vars.index( self.name )
                    self.values[ self.idd ] = self.long_chaine

                else:
                    self.vars.append( self.name )
                    self.values.append( self.long_chaine )

                self.data_base[ 'variables' ][ 'vars' ]     = self.vars
                self.data_base[ 'variables' ][ 'values' ]   = self.values

        else: pass

        return self.error

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