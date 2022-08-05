# used to analyze < begin and try >
# try:                  | begin:
#   instruction         |   intructions
# end:                  | end:

# returning < type> = 'begin:' or "try:">, <  None type > and < None type if not got an error >

from statement                       import error as er
from script                          import control_string

class STRUCT:
    def __init__(self, data_base: dict, line : int):
        self.data_base      = data_base
        self.line           = line
        self.control        = control_string.STRING_ANALYSE(self.data_base, self.line)

    def STRUCT(self, num: int = 3, normal_tring : str = ''):
        self.normal_string      = normal_tring
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