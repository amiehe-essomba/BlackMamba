from script                                             import control_string

class INTERNAL_BLOCKS:
    def __init__(self, 
                normal_string   : str, 
                data_base       : dict, 
                line            : int
                ):
        self.line           = line
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def BLOCKS(self, 
               tabulation: int = 1
               ):
        self.tabulation     = tabulation
        self.back_end       = self.tabulation - 1
        self._return_       = None
        self.error          = None
        self.value          = None

        self.normal_string          = self.normal_string[ self.back_end : ]

        try:
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                self.value      = self.normal_string
                self._return_   = 'any'

            else:
                self._return_   = 'empty'
                self.error      = None

        except IndexError:
            self.error      = None
            self._return_   = 'empty'
            self.value      = ''

        return self._return_, self.value, self.error