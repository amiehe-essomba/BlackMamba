from script.PARXER                                          import numerical_value
from script.PARXER.VAR_NAME                                 import get_var_name
from script.PARXER.PRINT                                    import show_data
from script.PARXER                                          import parxerError as pE

class ASSEMBLY( ):
    def __init__(self, master: dict, data_base: dict, line: int ):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.num_parxer     = numerical_value
        self.variables      = self.data_base[ 'variables' ][ 'vars' ]
        self._values_       = self.data_base[ 'variables' ][ 'values' ]
        self.global_vars    = self.data_base[ 'global_vars' ][ 'vars' ]
        self.global_values  = self.data_base[ 'global_vars' ][ 'values' ]
        
        try:
            self._if_egal_  = self.master[ 'if_egal' ]
            self.main_value = self.master[ 'all_data' ]
        except: self._if_egal_ = 'comment'

    def ASSEMBLY(self,
                 main_string    : str,
                 key            : bool = False,
                 interpreter    : bool = False,
                 locked         : bool = False
                 ):
        
        
        self.error          = None
        self._return_       = None
        self.key_return     = False

        if self._if_egal_ == 'comment' : pass

        if self._if_egal_ is None:
            self._return_, self.error = self.num_parxer.NUMERICAL( self.master, self.data_base, self.line ).ANALYSE( main_string )
            if self.error is None:
                if not self.data_base[ 'no_printed_values' ]:
                    if self._return_ is not None:
                        if interpreter is False:
                            if locked is False: 
                                for value in self._return_:
                                    show_data.SHOW( value, self.data_base, key ).SHOW()
                            else: pass
                        else: pass
                    else: pass
                else: self.data_base[ 'no_printed_values' ] = []
            else:
                if self.data_base[ 'no_printed_values' ]: self.data_base[ 'no_printed_values' ] = []
                else : pass

        elif self._if_egal_ == True:

            self._operator_     = self.main_value[ 'operator' ]
            self.var_names      = self.main_value[ 'variable' ]

            for i,  name in enumerate( self.var_names ):
                self.name, self.error = get_var_name.GET_VAR(name, self.data_base, self.line).GET_VAR()
                if self.error is None:
                    self.var_names[ i ] = self.name
                else: break

            if self.error is None:
                self._return_, self.error = self.num_parxer.NUMERICAL( self.master, self.data_base,
                                                                      self.line ).ANALYSE( main_string )
                if self.error is None:
                    if not self.data_base[ 'no_printed_values' ] :
                        for i in range( len( self.var_names ) ):
                            if   type( self.var_names[ i ] ) == type( str() )   :
                                if self.var_names[ i ] in self.variables:
                                    if type( self._return_[ i ] ) == type( str() ):
                                        try:
                                            if '"' in self._return_[ i ][ 0 ]: pass
                                            else: pass
                                        except IndexError: pass
                                    else: pass

                                    self.idd = self.variables.index( self.var_names[ i ] )
                                    self._values_[ self.idd ] = self._return_[ i ]

                                    if self.global_vars:
                                        if self.var_names[ i ] in self.global_vars:
                                            self.idd = self.global_vars.index( self.var_names[ i ] )
                                            self.global_values[ self.idd ] = self._return_[ i ]
                                        else: pass
                                    else:pass

                                else:
                                    if type( self._return_[ i ] ) == type( str() ):
                                        try:
                                            if '"' in self._return_[ i ][ 0 ]: pass
                                            else: pass
                                        except IndexError: pass
                                    else: pass

                                    self.variables.append( self.var_names[ i ] )
                                    self._values_.append( self._return_[ i ] )

                                    if self.global_vars:
                                        if self.var_names[ i ] in self.global_vars:
                                            self.idd = self.global_vars.index( self.var_names[ i ] )
                                            self.global_values[ self.idd ] = self._return_[ i ]
                                        else: pass
                                    else: pass
                            elif type( self.var_names[ i ] ) == type( list() )  :

                                self._name_ = self.var_names[ i ][ 0 ][ 'name' ]
                                self.info   = self.var_names[ i ][ 0 ][ 'info' ]

                                if type( self._return_[ i ] ) == type( str() ):
                                    try:
                                        if '"' in self._return_[ 0 ][ i ]: pass
                                        else: pass
                                    except IndexError: pass
                                else: pass

                                self.idd            = self.variables.index( self._name_ )
                                self.__value__      = self._values_[ self.idd ]

                                for j, _in_ in enumerate( self.info ):
                                    try:
                                        if j != len( self.info ) - 1:
                                            if type( _in_ ) != type( list() ):
                                                self.__value__ = self.__value__[ _in_ ]

                                            else:
                                                for w in _in_:
                                                    self.__value__ = self.__value__[ w ]
                                        else:
                                            if type( _in_ ) != type( list() ):
                                                self.__value__[ _in_ ]  = self._return_[ i ]

                                            else:
                                                for w in _in_:
                                                    if w != len( _in_ ) - 1 :
                                                        self.__value__ = self.__value__[ w ]
                                                    else:
                                                        self.__value__[ w ] = self._return_[ i ]

                                    except TypeError:
                                        self.error = pE.ERRORS( self.line ).ERROR1( self.__value__, 'a list()')
                                        break

                                if self.global_vars:
                                    if self._name_ in self.global_vars:
                                        self._idd_ = self.global_vars.index( self._name_ )
                                        self.global_values[ self._idd_ ] = self._values_[ self.idd ]
                                    else: pass
                                else: pass
                            elif type( self.var_names[ i ] ) == type( dict() )  :
                                self._name_         = self.var_names[ i ][ 'name' ]
                                self._keys_         = self.var_names[ i ][ 'keys' ]

                                if type( self._return_[ i ] ) == type( str() ):
                                    try:
                                        if '"' in self._return_[ 0 ][ i ]: pass
                                        else: pass
                                    except IndexError: pass
                                else: pass

                                self.list_keys  = list( self.var_names[ i ] .keys()  )
                                self.idd        = self.variables.index( self._name_ )
                                self.__value__  = self._values_[ self.idd ]

                                if 'info' not in self.list_keys:
                                    for j, keys in enumerate( self._keys_ ):
                                        if j != len( self._keys_ ) - 1:
                                            self.__value__ = self.__value__[ keys ]
                                        else:
                                            self.__value__[ keys ] = self._return_[ i ]
                                else:
                                    self.info = self.var_names[ i ][ 'info' ]
                                    self.all_info = self.info + self._keys_

                                    for j, _in_ in enumerate( self.all_info ):
                                        if j != len( self.all_info ) - 1:
                                            self.__value__ = self.__value__[ _in_ ]
                                        else:
                                            self.__value__[_in_] = self._return_[ i ]

                                if self.global_vars:
                                    if self._name_ in self.global_vars:
                                        self._idd_ = self.global_vars.index( self._name_ )
                                        self.global_values[ self._idd_ ] = self._values_[ self.idd ]
                                    else: pass
                                else: pass

                        self.data_base[ 'variables' ]   = {
                            'vars'                      : self.variables,
                            'values'                    : self._values_,
                        }
                        self.data_base[ 'global_vars' ] = {
                            'vars'                      : self.global_vars,
                            'values'                    : self.global_values,
                        }
                        self.data_base['matrix'] = None
                    else:
                        self.error = pE.ERRORS( self.line ).ERROR2( self.data_base[ 'assigment' ] )
                        self.data_base[ 'no_printed_values' ]   = []
                        self.data_base[ 'assigment' ]           = None
                else: pass
            else: pass

        return self.error