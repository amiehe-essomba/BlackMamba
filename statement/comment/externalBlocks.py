from script                     import control_string
from statement                  import error as er

class EXTERNAL:
    def __init__(self, data_base : dict, line : int):
        self.data_base      = data_base
        self.line           = line
        self.control        = control_string.STRING_ANALYSE(self.data_base, self.line)

    def EXTERNAL(self, num : int, normal_string : str):
        self.error          = None
        self.normal_string  = normal_string

        self.new_normal_string = self.normal_string[num : -1]
        self.new_normal_string, self.error = self.control.DELETE_SPACE(self.new_normal_string)

        if self.error is None:  self.error = er.ERRORS(self.line).ERROR0(self.normal_string)
        else: self.error = None

        return self.error