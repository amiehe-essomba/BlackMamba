from script                                             import control_string
from script.LEXER                                       import particular_str_selection
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from CythonModules.Windows                              import fileError    as fe 



class LAMBDA:
    def __init__(self, data_base, line):
        self.data_base      = data_base
        self.line           = line
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line)
        self.selection      = particular_str_selection

    def LAMBDA(self, value: str = ""):
        self.error          = None
        self.main_string    = value
        self.long_string    = 'lambda ' + self.main_string
        self.lambda_value   = None
        self.list_of_values, self.error = self.selection.SELECTION( self.main_string, self.main_string,
                                                                    self.data_base, self.line ).CHAR_SELECTION( ':' )
        
        if self.error is None:
            if len(self.list_of_values) == 2:
                for i, _value_ in enumerate( self.list_of_values ):
                    self.string, self.error = self.control.DELETE_SPACE( _value_ )
                    if self.error is None:
                        self.list_of_values[ i ] =  self.string 
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.string )
                        break
                if self.error is None:
                    if len( self.list_of_values ) == 2:
                        self.attributes, self.error = self.selection.SELECTION( self.list_of_values[ 0 ], self.list_of_values,
                                                                    self.data_base, self.line ).CHAR_SELECTION( ' ' )
                        if self.error is None:
                            self.alpha = []
                            for i, _s_ in enumerate( self.attributes ):
                                if _s_:
                                    _name_, self.error = self.control.CHECK_NAME(_s_)
                                    if self.error is None: self.alpha.append(_name_) 
                                    else: break
                                else: pass
                            if self.error is None: 
                                if self.alpha: self.list_of_values[0] = self.alpha.copy()
                                else: self.error = ERRORS( self.line ).ERROR0( self.long_string )
                            else: pass 
                        else: pass 
                    else: self.error = ERRORS( self.line ).ERROR0( self.long_string )
            else: self.error = ERRORS( self.line ).ERROR0( self.long_string )
        else: pass 
        
        return self.list_of_values, self.error

class ERRORS:
    def __init__(self, line):
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}was not found. {}line: {}{}.'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors()+'{}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.error