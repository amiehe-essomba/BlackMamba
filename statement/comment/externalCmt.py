from script                                             import control_string
from statement                                          import error as er
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import cmtError as ce
from statement.comment                                  import externalBlocks

class EXTERNAL_BLOCKS:
    def __init__(self, 
                normal_string   : str , 
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
        
        self.tabulation                 = tabulation
        self.back_end                   = self.tabulation - 1
        self._return_                   = None
        self.value                      = None
        self.error                      = None

        self.normal_string              = self.normal_string[ self.back_end : ]

        try:
            self.normal_string, self.error  = self.control.DELETE_SPACE( string=self.normal_string )

            if self.error is None:
                try:
                    if   self.normal_string[ : 3 ] == 'end' :
                        if  self.normal_string[ -1 ] == ':':
                            self.error = externalBlocks.EXTERNAL(data_base=self.data_base, line=self.line).EXTERNAL(num=3,
                                                            normal_string=self.normal_string, tabulation=self.tabulation, split=True)
                            if self.error is None:  self._return_ = 'end:'
                            else: pass
                        else: self.error = ce.ERRORS(self.line).ERROR1( string='begin' )

                    elif self.normal_string[ : 4 ] == 'save':
                        if self.normal_string[ - 1] == ':':
                            self.value, self.error = externalBlocks.SAVE_COMMENT( master= self.normal_string, data_base=self.data_base,
                                                                    line= self.line ).SAVE(tabulation=self.tabulation, split=True)
                            if self.error is None: self._return_ = 'save:'
                            else:pass
                        else: self.error = ce.ERRORS(self.line).ERROR1( string='save' )
                    
                    else: self.error = ce.ERRORS( self.line ).ERROR4()
                except IndexError:  self.error = ce.ERRORS( self.line ).ERROR0( string=self.normal_string )
            else:
                self._return_   = 'empty'
                self.error      = None
        except IndexError:
            self._return_ = 'empty'
            self.error = None

        return self._return_, self.value, self.error