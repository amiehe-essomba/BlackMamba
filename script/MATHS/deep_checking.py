class DEEP_CHECKING:
    def __init__(self, master: list):
        self.master         = master

    def CHECKING(self, _sign_: str = '+'):
        self.string         = ''
        self.store          = []

        if len( self.master ) <= 1: pass
        else:
            for i, str_ in enumerate( self.master ):
                if str_:
                    if str_[ 0 ] not in [ '-' ]:
                        if str_[ 0 ] in [str( x ) for x in range(10)] and str_[ -1 ] in ['e', 'E']:
                            self.string = str_ + _sign_ + self.master[ i + 1]
                            self.store.append( (self.string, i ) )
                            self.string = ''
                        else: pass
                    else:  pass
                else: pass 
                
            if self.store:
                for str_index in self.store:
                    self.string, self.idd = str_index
                    self.master[ self.idd ] = self.string

                for str_index in self.store:
                    self.string, self.idd = str_index
                    del self.master[ self.idd + 1 ]
            else: pass

        return  self.master