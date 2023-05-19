
from statement.error                 import tryError as te
from statement.error                 import error as er
from statement.comment               import externalBlocks
from statement.comment               import structure
from script                          import control_string


class EXTERNAL_BLOCKS:
    def __init__(self,
            string         : str,
            normal_string  : str,
            data_base      : dict,
            line           : int
            ):
        
        self.line               = line
        self.string             = string
        self.normal_string      = normal_string
        self.data_base          = data_base
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )

    def BLOCKS(self, tabulation: int)   :

        """
        handling the external <try> statement.\n
        < except > < finally > and < end >\n
        #############################\n
        :param tabulation:
        :return: {self._return_ : str, self.value : any, self.error : str}
        """
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
                    if   self.normal_string[ : 3 ] == 'end'     :
                        if self.normal_string[-1] == ':':
                            self._return_ = 'end:'
                            self.error = externalBlocks.EXTERNAL(self.data_base, self.line).EXTERNAL(num=3,  normal_string=self.normal_string)
                        else:
                            if self.normal_string in ['end']: self.error = te.ERRORS(self.line).ERROR1('end')
                            else:  self.error = te.ERRORS(self.line).ERROR4()
                    elif self.normal_string[ : 6 ] == 'except'  :
                        if self.normal_string[ -1 ] == ':':
                            if self.normal_string[ 6 ] in [ ' ' ]:
                                self._return_   = 'except:'
                                self.value, self.error = structure.STRUCT(self.data_base, self.line).EXCEPTIONS(normal_string=self.normal_string)
                            else:  er.ERRORS(self.line).ERROR5(self.normal_string)
                        else:
                            try:
                                if self.normal_string[ 6 ] in [ ' ' ]:
                                    self.error = er.ERRORS(self.line).ERROR1('except')
                                else:
                                    self._return_   = 'any'
                                    self.value      = self.normal_string
                            except IndexError: self.error = te.ERRORS(self.line).ERROR1('except')
                    elif self.normal_string[ : 7 ] == 'finally' :
                        if self.normal_string[-1] == ':':
                            self._return_ = 'finally:'
                            self.error = externalBlocks.EXTERNAL(self.data_base, self.line).EXTERNAL(num=7,  normal_string=self.normal_string)
                        else:
                            if self.normal_string in ['finally']: self.error = te.ERRORS(self.line).ERROR1('finally')
                            else: self.error = te.ERRORS(self.line).ERROR4()
                    else: self.error = te.ERRORS( self.line ).ERROR4()
                except IndexError: self.error = er.ERRORS(self.line).ERROR0(self.normal_string)
            else:
                self._return_   = 'empty'
                self.error      = None
        except IndexError:
            self._return_   = 'empty'
            self.error      = None

        return self._return_, self.value, self.error