from colorama import Fore, init, Back, Style

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class BOOLEAN:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base

    def BOOLEAN(self):
        self.value          = None

        try:
            if self.master == 'True':
                self.value = True
            else:
                self.value = False
        except ValueError:
            pass

        return self.value