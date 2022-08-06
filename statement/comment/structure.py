# used to analyze < begin and try >
# try:                  | begin:
#   instruction         |   intructions
# end:                  | end:

# returning < type> = 'begin:' or "try:">, <  None type > and < None type if not got an error >

from statement.error                 import error as er
from statement.error                 import tryError as te
from script                          import control_string
from script.LEXER                    import particular_str_selection

class STRUCT:
    def __init__(self, data_base: dict, line : int):
        self.data_base      = data_base
        self.line           = line
        self.control        = control_string.STRING_ANALYSE(self.data_base, self.line)
        self.selection      = particular_str_selection

    def STRUCT(self,
               num          : int = 3,
               normal_string: str = ''
               ):
        """
        used to handle the < begin> and < try> statement\n.
        ###################\n
        begin:
            < string here >
            < string here >
        end :\n
        ###################\n
        try:
            < instructions >
        :exception < type of exception >:
            < instructions >
        :finally:
            < instruction >
        end:\n
        ##################\n
        :param num:
        :param normal_tring:
        :return:
        """

        self.normal_string      = normal_string
        self.error              = None
        self._return_           = None
        self.key                = None
        self.new_normal_string  = None
        self.value              = None
        self.func = ['begin' if num == 5 else 'try'][0]

        try:
            if self.normal_string[ -1 ] == ':':
                self.key = True
                self.new_normal_string = self.normal_string[num: -1]
                self.new_normal_string, self.error = self.control.DELETE_SPACE(self.new_normal_string)
            else:
                self.key = False
                self.new_normal_string = self.normal_string[num:]
                self.new_normal_string, self.error = self.control.DELETE_SPACE(self.new_normal_string)

            if self.error is None:
                if self.key is True:  self.error = er.ERRORS(self.line).ERROR0(self.normal_string)
                else:
                    self.value = self.control.DELETE_SPACE(self.normal_string)
                    self._return_ = 'any'
            else:
                if self.key is True:
                    self.error = None
                    self._return_ = self.func + ':'
                else: self.error = er.ERRORS(self.line).ERROR1(self.func)
        except IndexError:
            if self.normal_string[ -1 ] == ':':
                self.error = None
                self._return_ = self.func + ':'
            else: self.error = er.ERRORS(self.line).ERROR1(self.func)

        return self._return_, self.value, self.error

    def EXCEPTIONS(self, normal_string : str = ''):

        """
        This module was creatd for handling all exceptions type to avoid any type of
        error when running the code. it give us two many posssibilities :\n
        ########################\n
        try:
            < instructions >
        :exception :
            < instructions >
        :finally :
            < instructions >
        end:\n
        ########################\n
        try:
            < instructions >
        :exception < exception >, < exception >, < exception >:
            < instructions >
        :finally :
            < instructions >
        end:\n
        #######################

        :param normal_string:
        :return:
        """

        self.error              = None
        self._return_           = None
        self.normal_string      = normal_string

        self.exception_names    = [
            'SyntaxError', 'ValueError', 'EOFError', 'OSError', 'KeyError', 'NameError'    ,
            'TypeError', 'ArithmeticError', 'IndexError', 'FileModeError',  'OverFlowError',
            'AttributeError', 'ModuleError', 'DomainError', 'ModuleLoadError', 'FileError' ,
            'ExceptionNameError', 'EncodingError',  'IndentationError', 'ZeroDivisionError',
            'DecodingError', 'UnicodeError', 'DirectoryNotFoundError', 'FileNotFoundError' ,
            'CircularLoadingError'
        ]

        self.new_normal_string = self.normal_string[6: -1]

        if self.new_normal_string != '':
            if self.new_normal_string[ 0 ] in [ ' ' ]:
                self.new_normal_string, self.error = self.control.DELETE_SPACE(string=self.new_normal_string)
                if self.error is None:
                    self.all_exceptions, self.error = self.selection.SELECTION( master=self.new_normal_string,
                                 long_chaine=self.new_normal_string, data_base=self.data_base, line=self.line).CHAR_SELECTION(char = ',')
                    if self.error is None:
                        for i, _exceptions_ in enumerate( self.all_exceptions ):
                            self.name, self.error = self.control.DELETE_SPACE( string=_exceptions_ )
                            if self.error is None:
                                self.name, self.error = self.control.CHECK_NAME(name_string=self.name)
                                if self.error is None:  self.all_exceptions[ i ] = self.name
                                else:  break
                            else:
                                self.error = ERRORS(self.line).ERROR0(self.new_normal_string)
                                break

                        if self.error is None:
                            for i, _exceptions_ in enumerate( self.all_exceptions ):
                                if _exceptions_ in self.exception_names:  pass
                                else:
                                    self.error = te.ERRORS(self.line).ERROR5( _exceptions_ )
                                    break

                            if self.error is None:
                                if len(self.all_exceptions) == 1: self._return_ = self.all_exceptions[ 0 ]
                                else:  self._return_ = tuple( self.all_exceptions )
                            else: pass
                        else: pass
                    else:  pass
                else:
                    self.error = None
                    self._return_ = self.exception_names[ : ]
            else: self.error = te.ERRORS(self.line).ERROR4()
        else:  self._return_ = self.exception_names.copy()

        return self._return_, self.error