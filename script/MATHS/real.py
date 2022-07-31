from colorama import Fore, init, Back, Style
from script.PARXER import  numerical_value

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX


class REAL:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base

    def REAL(self):
        self.value          = None
        self.error          = None

        try:
            self.value      = float( self.master )
        except ValueError:
            self.error = numerical_value.ERRORS( self.line ).ERROR4( self.master, 'a float')

        return self.value, self.error