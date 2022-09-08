class CASE_TREATMENT:
    def __init__(self,
                main_master : any,
                master      : any,
                ):
        self.master             = master
        self.main_master        = main_master

    def CASE(self):
        self.error              = None
        self.type               = type( self.master )
        self._return_           = None

        if self.type != type( tuple() ):
            if self.main_master == self.master :  self._return_ = True
            else: self._return_ = False
        else:
            for value in self.master :
                if value == self.main_master:
                    self._return_ = True
                    break
                else:  self._return_ = False

        return  self._return_