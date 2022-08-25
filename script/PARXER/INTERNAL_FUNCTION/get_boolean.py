
class BOOLEAN:
    def __init__(self, master: any, data_base : any, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.variables          = self.data_base[ 'variables' ][ 'vars' ]

    def BOOLEAN(self):
        self.error              = None
        self.type               = self.master[ 'type' ]
        self.main_dict          = self.master[ 'numeric' ][ 0 ]
        self._return_           = None

        if self.main_dict == 'True': self._return_ = True
        elif self.main_dict == 'False':  self._return_ = False

        return self._return_, self.error

    def MAIN_BOOLEAN(self, main_string: str):
        self.error              = None
        self.numeric            = self.master[ 'numeric' ]
        self._return_           = None

        if self.numeric is not None: self._return_, self.error = BOOLEAN( self.master, self.data_base, self.line ).BOOLEAN()
        else: pass

        return self._return_, self.error
