from script                             import  control_string
from script.LEXER                       import particular_str_selection
from script.PARXER.INTERNAL_FUNCTION    import get_list
from script.PARXER.LEXER_CONFIGURE      import partial_lexer
from script.PARXER.INTERNAL_FUNCTION    import get_dictionary
from script.PARXER                      import numerical_value
from script.STDIN.WinSTDIN              import stdin
from CythonModules.Windows              import fileError    as fe
from script.STDIN.LinuxSTDIN            import bm_configure     as bm

class NAME_CHECKING:

    def __init__(self, master:str, data_base: dict, line:int):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.analyze        = control_string.STRING_ANALYSE(self.data_base, self.line)
        self.variables      = self.data_base[ 'variables' ][ 'vars' ]
        self._values_       = self.data_base[ 'variables' ][ 'values' ]
        self.selection      = particular_str_selection
        self.chars          = self.analyze.UPPER_CASE()+self.analyze.LOWER_CASE()

    def MAIN_CHECKING(self):
        self.error          = None
        self.name           = None
        self._return_       = None
        self.info           = None
        self.key_names      = None

        self.main_dict, self.error = partial_lexer.PARTIAL_LEXER( self.master, self.data_base, self.line ).LEXER( self.master )
        if self.error is None:
            self.list_values = list( self.main_dict.keys() )
            if 'values' not in self.list_values:
                self.type = self.main_dict[ 'type' ]
                if self.type is None:
                    self._name_ = self.main_dict[ 'numeric' ][ 0 ]
                    self.name, self.error = self.analyze.CHECK_NAME( self._name_ )
                    if self.error is None:  self._return_ = self.name
                    else: pass

                elif self.type == 'list':
                    self._name_ = self.main_dict['numeric'][ 0 ]
                    self._return_, self.info, self.error = NAME_CHECKING( self._name_, self.data_base, self.line ).TYPE1( self.main_dict )
                else: self.error = ERRORS( self.line ).ERROR7( self.master )
            else:
                self._return_, self.key_names, self.info, self.error = numerical_value.DICT( self.main_dict,
                                                                self.data_base, self.line).VAR_NAMES( self.master )
        else:  pass

        return self._return_, self.key_names, self.info,  self.error

    def TYPE1(self, value: dict):
        self.error                  = None
        self.main_list              = value
        self.string                 = ''
        self.idd                    = None
        self.info                   = None
        self.name                   = None

        for i, str_ in enumerate( self.master ):
            if str_ in ['[', '(', '{', '$']:
                self.idd = i
                break
            else: self.string += str_

        if self.idd != 0:
            self._name_, self.error = self.analyze.DELETE_SPACE( self.string )
            if self.error is None:
                self._name_, self.error = self.analyze.CHECK_NAME(self._name_)
                if self.error is None:
                    self.name = self._name_
                    self.final_value, self.info, self.data, self.error = get_list.LIST( self.main_list,
                                            self.data_base, self.line).VAR_NAMES( self.master )
            else: self.error = ERRORS( self.line ).ERROR0( self.master )

            return self.name,  self.info,  self.error

        else:
            self.name, self.error = self.analyze.CHECK_NAME( self.master )
            return None, None, self.error

class ERRORS:
    def __init__(self, line):
        self.line       = line
        self.cyan       = bm.init.bold + bm.fg.rbg(0,255,255)
        self.red        = bm.init.bold + bm.fg.rbg(255,0,0)
        self.green      = bm.init.bold + bm.fg.rbg(0,255,0)
        self.yellow     = bm.init.bold + bm.fg.rbg(255,255,0)
        self.magenta    = bm.init.bold + bm.fg.rbg(255,0,255)
        self.white      = bm.init.bold + bm.fg.rbg(255,255,255)
        self.blue       = bm.init.bold + bm.fg.rbg(0,0,255)
        self.reset      = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError').Errors()+'invalid syntax in {}<< {} >> '.format(self.white, self.cyan,  string) + error
        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error  =  fe.FileErrors( 'NameError').Errors()+'{}{} {}was not found. '.format(self.cyan, string, self.white) + error
        return self.error+self.reset

    def ERROR2(self, string: str):
        error = '{}due to {}EMPTY {}value. {}line: {}{}'.format(self.white, self.green, self.white, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>, '.format(self.white, self.cyan, string) + error
        return self.error+self.reset

    def ERROR3(self, string: str, char: str):
        error = '{}due to many {}<< : >> {}in {}<< {} >> . {}line: {}{}'.format(self.white, self.red, self.white, self.green, 
                                                                            char, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>, '.format(self.white, self.cyan, string) + error
        return self.error+self.reset

    def ERROR4(self, string: str):
        error = '{}is not  {}a list() {}or {}a tuple() {}type . {}line: {}{}'.format(self.white, self.yellow, 
                                                            self.white, self.blue, self.red, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError').Errors()+'{}{} '.format(self.magenta, string) + error
        return self.error+self.resetror

    def ERROR5(self, string: str):
        error = '{}is not  {}dict() {}type . {}line: {}{}'.format(self.white, self.cyan, self.red, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError').Errors()+'{}{} '.format(self.magenta, string) + error
        return self.error+self.reset

    def ERROR6(self, string1: str, string2: str):
        error       = '{}in {}<< {} >>. {}line: {}{}'.format(self.white, self.red, string2, self.white, self.yellow, self.line)
        self.error  =  fe.FileErrors( 'KeyError').Errors()+'{}{} {}was not found '.format(self.blue, string1, self.white) + error
        return self.error+self.reset

    def ERROR7(self, string: str):
        self._str_ = '{}type {}help( {}var_name{} ) {}for more informations. '.format(self.white, self.magenta, self.yellow, self.magenta, self.white)
        error = '{}as a character in {}<< {} >>. {}line: {}{}.\n{}'.format(self.white, self.green, string, self.white, self.yellow, self.line,
                                                                           self._str_)
        self.error =  fe.FileErrors( 'NameError').Errors()+'{}you cannot use {}space '.format(self.white, self.red) + error
        return self.error+self.reset
