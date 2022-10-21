from CythonModules.Linux.DEEP_PARSER       import error 

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
            self.error = error.ERRORS( self.line ).ERROR4( self.master, 'a float')

        return self.value, self.error