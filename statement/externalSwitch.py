from script                                     import control_string
from statement.error                            import switchError as se
from statement.comment                          import externalBlocks
from statement                                  import mainStatement as MS

class EXTERNAL_BLOCKS:
    def __init__(self,
                 string         : str,  # concatenated string
                 normal_string  : str,  # normal string
                 data_base      : dict, # data base
                 line           : int   # current line
                 ):
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def BLOCKS(self,
               tabulation   : int,          # tabulation number
               function     : any  = None,  # function type ('loop', 'conditional', 'def', 'class', 'try')
               interpreter  : bool = False  # interpreter
               ):

        self.tabulation                 = tabulation
        self.back_end                   = self.tabulation - 1
        self._return_                   = None
        self.value                      = None
        self.error                      = None

        self.string                     = self.string[ self.back_end : ]
        self.normal_string              = self.normal_string[ self.back_end : ]

        try:
            self.string, self.error         = self.control.DELETE_SPACE( self.string )
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                try:
                    if   self.normal_string[: 3]   == 'end'     :
                        if self.normal_string[ -1 ] == ':':
                            self._return_ = 'end:'
                            self.error = externalBlocks.EXTERNAL(self.data_base, self.line).EXTERNAL(num=3,
                                                                    normal_string=self.normal_string, split=True)
                        else:
                            if self.normal_string in ['end']: self.error = se.ERRORS(line=self.line).ERROR1(string='end')
                            else: self.error = se.ERRORS(self.line).ERROR4()
                    elif self.normal_string[ : 4 ] == 'case'    :
                        if self.normal_string[ -1 ] == ':':
                            if self.normal_string[ 4 ] in [ ' ' ]:
                                self._return_ = 'case:'
                                self.value, self.error = MS.MAIN(self.normal_string, self.data_base, self.line).MAIN(typ='case',
                                                            opposite=False, interpreter=interpreter, function=function)
                            else:
                                try:
                                    if self.normal_string[ 4 ] in [' ']:  self.error = se.ERRORS(self.line).ERROR1('case')
                                    else:
                                        self._return_ = 'any'
                                        self.value = self.normal_string
                                except IndexError:  self.error = se.ERRORS(line=self.line).ERROR1(string='case')
                        else:  self.error = se.ERRORS(self.line).ERROR1(string='case')
                    elif self.normal_string[ : 7 ] == 'default' :
                        if self.normal_string[ -1 ] == ':':
                            self._return_ = 'default:'
                            self.error = externalBlocks.EXTERNAL(data_base=self.data_base, line=self.line).EXTERNAL(
                                num=7,  normal_string=self.normal_string, tabulation=self.tabulation, split=True)
                        else:
                            if self.normal_string in ['default']:  self.error = se.ERRORS(self.line).ERROR1('default')
                            else:  self.error = se.ERRORS(self.line).ERROR4()
                    else:self.error = se.ERRORS( self.line ).ERROR4()
                except IndexError:  self.error = se.ERRORS( self.line ).ERROR0(string= self.normal_string )
            else:
                self._return_   = 'empty'
                self.error      = None
        except IndexError:
            self._return_   = 'empty'
            self.error      = None

        return self._return_, self.value, self.error