from script.LEXER import var_name_checking

class GET_VAR:
    def __init__(self, master: str, data_base: dict, line:int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.variable       = var_name_checking

    def GET_VAR(self):
        self.error          = None
        self._return_var_   = None

        self.var, self.key_names, self.info, self.error = self.variable.NAME_CHECKING(self.master,
                                                                            self.data_base, self.line ).MAIN_CHECKING()
        if self.error is None:

            if self.info is None and self.key_names is None:
                self._return_var_ = self.var

            elif self.key_names is None and type( self.info) == type( list() ):
                self._return_var_ = {
                    'name'      : self.var,
                    'info'      : self.info }

                self._return_var_ = [ self._return_var_ ]
            elif self.key_names is not None:
                if self.info is None:
                    self._return_var_ = {
                        'name' : self.var,
                        'keys' : self.key_names
                    }
                else:
                    self._return_var_ = {
                        'name' : self.var,
                        'keys' : self.key_names,
                        'info' : self.info
                    }
        else:
            self.error = self.error

        return self._return_var_, self.error
