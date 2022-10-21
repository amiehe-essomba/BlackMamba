from statement.error               import error as er
from script                        import control_string
from statement.comment             import externalBlocks

class EXTERNAL_BLOCKS:
    def __init__(self,
                 normal_string          : str,
                 data_base              : dict,
                 line                   : int
                 ):
        self.line           = line
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def BLOCKS(self, tabulation: int):
        self.tabulation                 = tabulation
        self.back_end                   = self.tabulation - 1
        self._return_                   = None
        self.value                      = None
        self.error                      = None
        self.normal_string              = self.normal_string[ self.back_end : ]

        try:
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                try:
                    if   self.normal_string[ : 3 ] == 'end'  :
                        if self.normal_string[-1] == ':':
                            self._return_ = 'end:'
                            self.error = externalBlocks.EXTERNAL(self.data_base, self.line).EXTERNAL(num=3, normal_string=self.normal_string)
                        else:
                            if self.normal_string in ['end']: self.error = er.ERRORS(self.line).ERROR1('end')
                            else:  self.error = er.ERRORS(self.line).ERROR4()
                    else:   self.error = er.ERRORS( self.line ).ERROR4()
                except IndexError:  self.error = er.ERRORS( self.line ).ERROR0( self.normal_string )
            else:
                self._return_   = 'empty'
                self.error      = None
        except IndexError:
            self._return_   = 'empty'
            self.error      = None

        return self._return_, self.value, self.error