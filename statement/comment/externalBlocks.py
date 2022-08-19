"""
created to take into account the external block without supplementary arguments:
{ end, default, else finally }
"""
from script                                             import control_string
from statement                                          import error as er
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import cmtError as ce

class EXTERNAL:
    def __init__(self, data_base : dict, line : int):
        self.data_base          = data_base
        self.line               = line
        self.control            = control_string.STRING_ANALYSE(self.data_base, self.line)

    def EXTERNAL(self, 
                num            : int, 
                normal_string  : str,
                tabulation     : int  = 1,
                split          : bool = True
                ):
        
        self.tabulation         = tabulation
        self.backend            = self.tabulation-1
        self.error              = None
        self.normal_string      = normal_string

        if split is True : pass 
        else: self.normal_string = self.normal_string[ self.backend : ]
            
        self.new_normal_string  = self.normal_string[num : -1]
        self.new_normal_string, self.error = self.control.DELETE_SPACE(self.new_normal_string)

        if self.error is None   :  self.error = er.ERRORS(self.line).ERROR0(self.normal_string)
        else                    : self.error = None

        return self.error

class SAVE_COMMENT:
    def __init__(self, 
                master      : str, 
                data_base   : dict, 
                line        : int
                ):
        self.line           = line
        self.master         = master[: -1]
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def SAVE(self, 
             tabulation : int = 1, 
             split      : bool = True
             ):
        self.error          = None
        self._return_       = None
        self.tabulation     = tabulation
        self.backend        = self.tabulation - 1
        
        if split is True : pass 
        else: self.master = self.master[ self.backend : ]

        if self.master[ : 4] == 'save':
            try:
                if self.master[ 4 ] in [ ' ' ]:
                    self.string = self.master[ 4: ]
                    self.string, self.error = self.control.DELETE_SPACE( self.string )
                    if self.error is None:
                        try:
                            if self.string[ :2 ] == 'as':
                                if self.string[ 2 ] in [ ' ' ]:
                                    self.new_tring = self.string[ 2 : ]
                                    self.new_tring, self.error = self.control.DELETE_SPACE( self.new_tring )
                                    if self.error is None:
                                        self.name, self.error = self.control.CHECK_NAME( self.new_tring )
                                        if self.error is None:
                                            self._return_ = self.name
                                        else: pass
                                    else:  self.error = ce.ERRORS( self.line ).ERROR0( self.master )
                                else:  self.error = ce.ERRORS(self.line).ERROR0(self.string)
                            else:  self.error = ce.ERRORS( self.line ).ERROR0( self.string )
                        except IndexError:  self.error =ce. ERRORS(self.line).ERROR0(self.string)
                    else:  self.error = ce.ERRORS( self.line ).ERROR0( self.master)
                else:  self.error = ce.ERRORS( self.line ).ERROR4()
            except IndexError:  self.error = ce.ERRORS( self.line ).ERROR4()
        else:  self.error = ce.ERRORS( self.line ).ERROR4()

        return  self._return_, self.error

    
