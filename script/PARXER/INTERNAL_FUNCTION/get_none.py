class NONE:
    def __init__(self, master: any, data_base : any, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.variables          = self.data_base[ 'variables' ][ 'vars' ]

    def NONE(self):
        self.error              = None
        self.type               = self.master[ 'type' ]
        self.main_dict          = self.master[ 'numeric' ][ 0 ]

        self._return_           = None

        return self._return_, self.error

    def MAIN_NONE(self, main_string: str):
        self.error              = None
        self.numeric            = self.master[ 'numeric' ]
        self._return_           = None

        if self.numeric is not None: self._return_, self.error = NONE( self.master, self.data_base, self.line ).NONE()
        else: pass

        return self._return_, self.error