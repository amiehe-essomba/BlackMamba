class UPDATE:
    def __init__(self, database : dict):
        self.database       = database
    def UPDATE(self,
               before   : dict, # DataBase before any computing
               dafter   : dict, # DataBase updated after computing
               error    : any   # error got after computing
               ):
        self.error = error # init error

        if self.error is not None:
            # values and variables before any calculations
            self.values_before          = before['variables_vals'].copy()
            self.variables_before       = before['variables_vars'].copy()
            self.global_vars_before     = before['global_vars'].copy()
            self.global_values_before   = before['global_vals'].copy()

            # values and variables after calculations
            self.values_after           = after['variables_vals'].copy()
            self.variables_after        = after['variables_vars'].copy()
            self.global_vars_after      = after['global_vars'].copy()
            self.global_values_after    = after['global_vals'].copy()

            # let's start with the local variables
            if self.variables_after:
                # if variables_after  is different from variables_before
                for i, vars in enumerate( self.variables_after ):
                    if vars in self.variables_before:
                        self.idd = self.variables_after.index( vars )
                        if self.values_after[ self.idd ] == self.values_before[self.idd]: pass
                        else: self.values_after[ self.idd ] = self.values_before[self.idd]
                    else:
                        self.idd = self.variables_after.index( vars )
                        del self.values_after[ self.idd ]
                        del self.variables_after[ self.idd ]
            else: pass

            # let's keep checking with the global variables
            if self.global_vars_after:
                # if global_vars_after is different from de global_vars_before
                for i, vars in enumerate( self.global_vars_after ):
                    if vars in self.global_vars_before:
                        self.idd = self.global_vars_after.index( vars )
                        if self.global_values_after[self.idd] == self.global_values_before[self.idd]: pass
                        else:  self.global_values_after[self.idd] = self.global_values_before[self.idd]
                    else:
                        self.idd = self.global_vars_after.index( vars )
                        del self.global_values_after[self.idd]
                        del self.global_vars_after[self.idd]
            else: pass

            #####################################################################
            # initialization of the memory if < black mamba detected any changes
            # local an global variables
            self.final_variables = {
                'vars'      : self.variables_after,
                'values'    : self.values_after
            }
            self.final_global_vars = {
                'vars'      : self.global_vars_after,
                'values'    : self.global_values_after
            }

            self.data_base[ 'variables' ]     = self.final_variables.copy()
            self.data_base[ 'global_vars' ]   = self.final_global_vars.copy()
            ######################################################################
        else:  pass

        return self.error

    def BEFORE(self):
        # building the DataBase before computing
        self.DataBase = {
            'variables_vars'     : self.data_base[ 'variables' ][ 'vars'].copy(),
            'variables_vals'     : self.data_base[ 'variables' ][ 'values' ].copy(),
            'global_vars'        : self.data_base[ 'global_vars' ][ 'vars' ].copy(),
            'global_vals'        : self.data_base[ 'global_vars' ][ 'values' ].copy()
        }
        return self.DataBase

    def AFTER(self):
        # updating the DataBase after computing
        self.DataBase = {
            'variables_vars'        : self.data_base[ 'variables' ][ 'vars' ].copy(),
            'variables_vals'        : self.data_base[ 'variables' ][ 'values' ].copy(),
            'global_vars'           : self.data_base[ 'global_vars' ][ 'vars' ].copy(),
            'global_vals'           : self.data_base[ 'global_vars' ][ 'values' ].copy()
        }
        return self.DataBase