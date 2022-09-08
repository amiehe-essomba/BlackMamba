from script                                     import control_string
from classes                                    import ClassError as ce
from statement.error                            import error as er
from statement.comment                          import externalBlocks

class INTERNAL_BLOCKS:
    def __init__(self,
                 normal_string  : str,          # main string
                 data_base      : dict,         # data base
                 line           : int           # current line
                 ):
        self.line               = line
        self.normal_string      = normal_string
        self.data_base          = data_base
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )

    def BLOCKS(self,
               tabulation       : int,          # tabulation
               loop             : bool = False  # if loop is activated
               ):
        """
        :param tabulation:
        :param loop: {default value = False }
        :return: {self._return_ : str, self.value : any, self.error : str}
        """
        self.tabulation         = tabulation
        self.back_end           = self.tabulation - 1
        self._return_           = None
        self.error              = None
        self.value              = None
        self.normal_string      = self.normal_string[ self.back_end : ]

        try:
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                try:
                    if self.normal_string[ 0 ] != '#':
                        if   self.normal_string[ : 3 ]  == 'def'     :
                            if self.normal_string[ -1 ] == ':':
                                if self.normal_string[ 3 ] in [ ' ' ]:
                                    self.value = self.normal_string
                                    self._return_, self.error = INTERNAL_BLOCKS(self.normal_string,
                                                        self.data_base, self.line).BLOCK_TREATMENT( num = 3, function='def')
                                else:
                                    try:
                                        if self.normal_string[ 3 ] in [' ']:  self.error = er.ERRORS(self.line).ERROR1( 'def' )
                                        else:
                                            self._return_   = 'any'
                                            self.value      = self.normal_string
                                    except IndexError: self.error = er.ERRORS(self.line).ERROR1( 'def' )
                            else:   self.error = er.ERRORS(self.line).ERROR1( 'def' )
                        elif self.normal_string[ : 5 ]  == 'class'   :
                            if self.normal_string[ -1 ] == ':':
                                if self.normal_string[ 5 ] in [ ' ' ]:
                                    self.value = self.normal_string
                                    self._return_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                                    self.data_base, self.line).BLOCK_TREATMENT(num=5, function='class')
                                else:
                                    try:
                                        if self.normal_string[ 5 ] in [ ' ' ]: self.error = er.ERRORS(self.line).ERROR1( 'class' )
                                        else:
                                            self._return_ = 'any'
                                            self.value = self.normal_string
                                    except IndexError:  self.error = er.ERRORS(self.line).ERROR1( 'class' )
                            else: self.error = er.ERRORS(self.line).ERROR1( 'class' )
                        elif self.normal_string[ : 3 ]  == 'end'     :
                            if loop is True:
                                if self.normal_string[-1] == ':':
                                    self._return_ = 'end:'
                                    self.error = externalBlocks.EXTERNAL(self.data_base, self.line).EXTERNAL(snum=3, normal_string=self.normal_string)
                                else:
                                    if self.normal_string in ['end']:  self.error = er.ERRORS(self.line).ERROR1('end')
                                    else:  self.error = er.ERRORS(self.line).ERROR4()
                            else:  self.error = er.ERRORS(self.line).ERROR4()
                        else: self.error      = er.ERRORS( self.line ).ERROR4()
                    else:  self._return_ = 'comment_line'
                except IndexError:  self.error = er.ERRORS( self.line ).ERROR0( self.normal_string )
            else:
                self._return_   = 'empty'
                self.error      = None
        except IndexError:
            self._return_   = 'empty'
            self.error      = None

        return self._return_, self.value, self.error

    def BLOCK_TREATMENT(self,
                num             : int = 5,      # number of chars
                function        : any = 'class' # function type [ class or def ]
                ):
        """
        :param num: {default value = 5 }
        :param function: {default value = 'class' }
        :return: {self._return_ : str, self.error : str }
        """
        self.error                          = None
        self._return_                       = None
        self.new_normal_string              = self.normal_string[ num : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None:  self._return_ = function+':'
        else: self.error = er.ERRORS( self.line ).ERROR0( self.normal_string )

        return self._return_, self.error