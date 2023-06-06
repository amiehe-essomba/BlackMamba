from script                                         import control_string
from script.PARXER.LEXER_CONFIGURE                  import numeric_lexer
from statement.error                                import error as er
from statement.comment                              import structure
from statement                                      import mainStatement as MS
from loop                                           import mainFor
from functions                                      import errorDef as ed
from statement.comment                              import externalBlocks
from script.STDIN.LinuxSTDIN                        import bm_configure as bm
try                 :  from CythonModules.Windows   import fileError as fe
except ImportError  :  from CythonModules.Linux     import fileError as fe


class INTERNAL_BLOCKS:
    def __init__(self,
                 string         : str,          # concatenated string
                 normal_string  : str,          # normal string
                 data_base      : dict,         # data base
                 line           : int           # current line
                 ):

        self.line               = line
        self.string             = string
        self.normal_string      = normal_string
        self.data_base          = data_base
        self.control            = control_string.STRING_ANALYSE(self.data_base, self.line)
        self.lex_parxer         = numeric_lexer
        self.chars              = self.control.LOWER_CASE() + self.control.UPPER_CASE() + ['_']

    def BLOCKS(self,
               tabulation       : int,              # tabulation
               function         : any   = 'def',    # functionn
               interpreter      : bool  = False,    # interpreter
               class_name       : str   = '',       # class name
               class_key        : bool  = False,    # if initialize function was created
               func_name        : str   = '',       # function name
               loop             : any   = None,     # if loop
               locked           : bool  = False
               ):
        """
        this module is used to make a treatment of internal function in the function < def of func >
        :param tabulation:
        :param function:
        :param interpreter:
        :param class_name:
        :param class_key:
        :param func_name:
        :param loop:
        :return: three value :function type, :value, and :error
        """
        self.tabulation         = tabulation
        self.back_end           = self.tabulation - 1
        self._return_           = None
        self.error              = None
        self.value              = None

        self.string             = self.string[  self.back_end : ]
        self.normal_string      = self.normal_string[ self.back_end : ]
        self.badFunctions       = ['elif', 'else', 'except', 'finally', 'case', 'default', 'func', 'class']
        self.err                = '{} / {}class {}{}( )'.format(bm.fg.white_L, bm.fg.red_L, bm.fg.blue_L,
                                                 class_name) + bm.init.reset
        try:
            self.string, self.error = self.control.DELETE_SPACE(self.string)
            self.normal_string, self.error = self.control.DELETE_SPACE(self.normal_string)
            
            if self.error is None:
                try:
                    if self.normal_string[ 0 ] != '#':
                        if   self.normal_string[: 2] == 'if'        :
                            if self.normal_string[-1] == ':':
                                if self.normal_string[2] in [' ']:
                                    self._return_ = 'if:'
                                    self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                        typ='if', opposite=False, interpreter=interpreter, function=function)
                                else: self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                            else:
                                try:
                                    if self.normal_string[2] in [' ']:  self.error = er.ERRORS(self.line).ERROR1('if')
                                    else:
                                        self._return_ = 'any'
                                        self.value = self.normal_string
                                except IndexError: self.error = er.ERRORS(self.line).ERROR1('if')
                        elif self.normal_string[: 3] == 'for'       :
                            self._return_, self.value, self.error = mainFor.FOR_BLOCK(self.data_base, self.line, 
                                                  self.normal_string).FOR( function=function, interpreter=interpreter, locked=locked)  
                        elif self.normal_string[: 6] == 'unless'    :
                            if self.normal_string[-1] == ':':
                                if self.normal_string[6] in [' ']:
                                    self._return_ = 'unless:'
                                    self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                        typ='unless', opposite=True, interpreter=interpreter, function=function)
                                else: self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                            else:
                                try:
                                    if self.normal_string[6] in [' ']: self.error = er.ERRORS(self.line).ERROR1('if')
                                    else:
                                        self._return_ = 'any'
                                        self.value = self.normal_string
                                except IndexError:  self.error = er.ERRORS(self.line).ERROR1('unless')
                        elif self.normal_string[: 5] == 'until'     :
                            if self.normal_string[-1] == ':':
                                if self.normal_string[5] in [' ']:
                                    self._return_ = 'until:'
                                    self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                        typ='until', opposite=True, interpreter=interpreter, function=function)
                                else:  self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                            else:
                                try:
                                    if self.normal_string[5] in [' ']:  self.error = er.ERRORS(self.line).ERROR1('until')
                                    else:
                                        self._return_ = 'any'
                                        self.value = self.normal_string
                                except IndexError: self.error = er.ERRORS(self.line).ERROR1('until')
                        elif self.normal_string[: 5] == 'while'     :
                            if self.normal_string[-1] == ':':
                                if self.normal_string[5] in [' ']:
                                    self._return_ = 'while:'
                                    self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                        typ='while', opposite=False, interpreter=interpreter, function=function)
                                else: self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                            else:
                                try:
                                    if self.normal_string[5] in [' ']:  self.error = er.ERRORS(self.line).ERROR1('while')
                                    else:
                                        self._return_ = 'any'
                                        self.value = self.normal_string
                                except IndexError: self.error = er.ERRORS(self.line).ERROR1('while')
                        elif self.normal_string[: 6] == 'switch'    :
                            if self.normal_string[-1] == ':':
                                if self.normal_string[6] in [' ']:
                                    self._return_ = 'switch:'
                                    self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(
                                        typ='switch', opposite=False, interpreter=interpreter, function=function)
                                else:  self.error = er.ERRORS(self.line).ERROR5(self.normal_string)
                            else:
                                try:
                                    if self.normal_string[6] in [' ']:  self.error = er.ERRORS(self.line).ERROR1('switch')
                                    else:
                                        self._return_ = 'any'
                                        self.value = self.normal_string
                                except IndexError: self.error = er.ERRORS(self.line).ERROR1('switch')
                        elif self.normal_string[: 3] == 'try'       :
                            self._return_, self.value, self.error = structure.STRUCT(self.data_base, self.line).STRUCT(num=3,
                                                                                              normal_string=self.normal_string)
                        elif self.normal_string[: 5] == 'begin'     :
                            self._return_, self.value, self.error = structure.STRUCT(self.data_base, self.line).STRUCT(num=5,
                                                                                              normal_string=self.normal_string)
                        elif self.normal_string[: 3] == 'def'       :
                            if self.normal_string[ 3 ] == ' ':
                                self._return_   = 'def:'
                                self.value      = self.normal_string
                            else:
                                self._return_   = 'any'
                                self.value      = 't'*self.back_end+self.normal_string
                        elif self.normal_string[: 3] == 'end'       :
                            if loop is True:
                                if self.normal_string[-1] == ':':
                                    self._return_   = 'end:'
                                    self.error      = externalBlocks.EXTERNAL(self.data_base, self.line).EXTERNAL(num=3,
                                                                                                     normal_string=self.normal_string)
                                else:
                                    if self.normal_string in ['end']: self.error = er.ERRORS(self.line).ERROR1('end')
                                    else: self.error = er.ERRORS(self.line).ERROR4()
                            else: self.error = er.ERRORS(self.line).ERROR4()
                        else:
                            if self.normal_string[-1] != ':':
                                if self.normal_string not in self.badFunctions:
                                    if class_key is False:
                                        self._return_ = 'any'
                                        self.value = 't' * self.back_end + self.normal_string
                                    elif class_key is True:
                                        self._return_ = 'any'
                                        self.value, self.error = SELF_METHOD(self.normal_string, self.data_base, self.line).SELF_METHOD()
                                        if self.error == None: self.value = 't' * self.back_end + self.value
                                        else: pass
                                else:  _, self.error = self.control.CHECK_NAME(self.normal_string)
                            else: self.error = er.ERRORS(self.line).ERROR0(self.normal_string)
                    else:  self._return_ = 'comment_line'
                except IndexError: self.error = er.ERRORS(self.line).ERROR4()
            else:
                self._return_   = 'empty'
                self.error      = None
        except IndexError:
            self.error      = None
            self._return_   = 'empty'

        if self.error is None: pass
        else:
            if class_name:
                self.error += bm.fg.rbg(0, 255, 0) + ' in {}( )'.format( func_name ) + bm.init.reset
                self.error += self.err
            else:  self.error += bm.fg.rbg(0, 255, 0) + ' in {}( )'.format( func_name ) + bm.init.reset

        return self._return_, self.value, self.error

class SELF_METHOD:
    def __init__(self,
                 master     : str,      # string
                 data_base  : dict,     # data base
                 line       : int       # current line
                 ):
        self.master         = master
        self.line           = line
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE(self.data_base, self.line)

    def SELF_METHOD( self ):
        """
        only used when the function initialize is created:
        for declarating variable or to make variable global, the self methode is
        used

        :return:  two values { newString and error }
        """
        self.error      = None
        self.newString  = ''
        try:
            if self.master[ : 5] == 'self.':
                self.newString = self.master[ 5 : ]
                self.newString, self.error = self.control.DELETE_SPACE( self.newString )
                if self.error is None: pass
                else: self.error = ed.ERRORS( self.line ).ERROR0( self.master )
            else: self.error = ed.ERRORS( self.line ).ERROR6( self.master )
        except IndexError: self.error = ed.ERRORS( self.line ).ERROR6( self.master )

        return self.newString, self.error