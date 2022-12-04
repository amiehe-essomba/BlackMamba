from script.PARXER                                          import numerical_value as NV
from script.PARXER.VAR_NAME                                 import get_var_name
from script.PARXER.PRINT                                    import show_data
from CythonModules.Windows.PARTIAL_PARSER                   import parserError as pE


cdef class ASSEMBLY:
    cdef public :
        unsigned long long int line 
        dict master 
        dict data_base 
    cdef:
        list variables, _values_, global_values, global_vars
        dict _return_, main_value, _if_egal_, error, _keys_, all_info, var_names
        list _operator_,  list_keys
        unsigned long long idd 
        dict _name_, info

    def __cinit__(self, master, data_base, line ):
        self.master         = master
        self.data_base      = data_base 
        self.line           = line  
        self.variables      = self.data_base[ 'variables' ][ 'vars' ]
        self._values_       = self.data_base[ 'variables' ][ 'values' ]
        self.global_vars    = self.data_base[ 'global_vars' ][ 'vars' ]
        self.global_values  = self.data_base[ 'global_vars' ][ 'values' ]
        self._return_       = {'s':None}
        self._if_egal_      = {'s':None}
        self.error          = {'s':None}
        self._name_         = {"s":None}
        self.info           = {"s":None}
        self._keys_         = {'s':None}
        self.all_info       = {"s":None}
        self.idd            = 0
        self.list_keys      = []
        self.var_names      = {"s":""}
    
    cpdef str ASSEMBLY(self, str main_string, bint key=False, bint interpreter=False, bint locked=False):

        cdef:
            signed long i, j, k, l
            dict name
            unsigned long _idd_
        name = {"s":""}
        try:
            self._if_egal_['s']     = self.master[ 'if_egal' ]
            self.main_value         = self.master[ 'all_data' ]
        except: self._if_egal_['s'] = 'comment'

        if   self._if_egal_['s'] == 'comment' : pass
        elif self._if_egal_['s'] is None:
            self._return_['s'], self.error['s'] = NV.NUMERICAL( self.master, self.data_base, self.line ).ANALYSE( main_string )
            if self.error['s'] is None:
                if not self.data_base[ 'no_printed_values' ]:
                    if self._return_['s'] is not None:
                        if interpreter is False:
                            if locked is False: 
                                if self.data_base['def_return'] in [None, True]:
                                    for i in range(len(self._return_['s'])):
                                        show_data.SHOW( self._return_['s'][ i ], self.data_base, key ).SHOW()
                                else: pass
                            else: pass
                        else: pass
                    else: pass
                else: self.data_base[ 'no_printed_values' ] = []
            else:
                if self.data_base[ 'no_printed_values' ]: self.data_base[ 'no_printed_values' ] = []
                else : pass

        elif self._if_egal_['s'] is True:

            #self._operator_     = self.main_value[ 'operator' ]
            self.var_names['s']      = self.main_value[ 'variable' ]
            
            for i in range(len(self.var_names['s'])):
                name['s'], self.error['s'] = get_var_name.GET_VAR(self.var_names['s'][ i ], self.data_base, self.line).GET_VAR()
                if self.error['s'] is None: self.var_names['s'][ i ] = name['s']
                else: break
            
            if self.error['s'] is None:
                self._return_['s'], self.error['s'] = NV.NUMERICAL( self.master, self.data_base,  self.line ).ANALYSE( main_string )
                if self.error['s'] is None:
                    if not self.data_base[ 'no_printed_values' ] :
                        for i in range( len( self.var_names['s'] ) ):
                            if   type( self.var_names['s'][ i ] ) == type( str() )   :
                                if self.var_names['s'][ i ] in self.variables:
                                    self.idd = self.variables.index( self.var_names['s'][ i ] )
                                    self._values_[ self.idd ] = self._return_['s'][ i ]

                                    if self.global_vars:
                                        if self.var_names['s'][ i ] in self.global_vars:
                                            self.idd = self.global_vars.index( self.var_names['s'][ i ] )
                                            self.global_values[ self.idd ] = self._return_['s'][ i ]
                                        else: pass
                                    else:pass
                                
                                else:
                                    self.variables.append( self.var_names['s'][ i ] )
                                    self._values_.append( self._return_['s'][ i ] )

                                    if self.global_vars:
                                        if self.var_names['s'][ i ] in self.global_vars:
                                            self.idd = self.global_vars.index( self.var_names['s'][ i ] )
                                            self.global_values[ self.idd ] = self._return_['s'][ i ]
                                        else: pass
                                    else: pass
                            elif type( self.var_names['s'][ i ] ) == type( list() )  :
                                self._name_['s'] = self.var_names['s'][ i ][ 0 ][ 'name' ]
                                self.info['s']   = self.var_names['s'][ i ][ 0 ][ 'info' ]

                                self.idd            = self.variables.index( self._name_['s'] )
                                self._return_['p']  = self._values_[ self.idd ]
                               
                                for j in range(len(self.info['s'])):
                                    try:
                                        if j != len( self.info['s'] ) - 1:
                                            if type( self.info['s'][ j ] ) != type( list() ):
                                                self._return_['p'] = self._return_['p'][ self.info['s'][ j ] ]
                                            else:
                                                for k in range(len(self.info['s'][ j ])):
                                                    self._return_['p'] = self._return_['p'][ self.info['s'][ j ][ k ] ]
                                        else:
                                            if type( self.info['s'][ j ] ) != type( list() ):
                                                self._return_['p'][ self.info['s'][ j ] ] = self._return_['s'][ i ]
                                            else:
                                                for k in  range(len(self.info['s'][ j ])):
                                                    if k != len( self.info['s'][ j ] ) - 1 :
                                                        self._return_['p'] = self._return_['p'][ self.info['s'][ j ][ k ] ]
                                                    else:  self._return_['p'][ self.info['s'][ j ][ k ] ] = self._return_['s'][ i ]
                                    except TypeError:
                                        self.error['s'] = pE.ERRORS( self.line ).ERROR1( self._return_['p'], 'a list()')
                                        break
                                self._values_[ self.idd ] = self._return_['p']
                                if self.global_vars:
                                    if self._name_['s'] in self.global_vars:
                                        _idd_ = self.global_vars.index( self._name_['s'] )
                                        self.global_values[ _idd_ ] = self._return_['p']
                                    else: pass
                                else: pass
                            elif type( self.var_names['s'][ i ] ) == type( dict() )  :
                                self._name_['s']         = self.var_names['s'][ i ][ 'name' ]
                                self._keys_['s']         = self.var_names['s'][ i ][ 'keys' ]

                                self.list_keys      = list( self.var_names['s'][ i ].keys()  )
                                self.idd            = self.variables.index( self._name_['s'] )
                                self._return_['p']  = self._values_[ self.idd ]

                                if 'info' not in self.list_keys:
                                    for j in range(len(self._keys_['s'])):
                                        if j != len( self._keys_['s'] ) - 1:
                                            self._return_['p'] = self._return_['p'][ self._keys_['s'][ j ] ]
                                        else:  self._return_['p'][ self._keys_['s'][ j ] ] = self._return_['s'][ i ]
                                else:
                                    self.info['s']          = self.var_names['s'][ i ][ 'info' ]
                                    self.all_info['s']      = self.info['s'] + self._keys_['s']

                                    for j in range(len(self.all_info['s'])):
                                        if j != len( self.all_info['s'] ) - 1:
                                            self._return_['p'] = self._return_['p'][ self.all_info['s'][ j ] ]
                                        else: self._return_['p'][ self.all_info['s'][ j ] ] = self._return_['s'][ i ]
                                    
                                self._values_[ self.idd ] = self._return_['p']
                                if self.global_vars:
                                    if self._name_ in self.global_vars:
                                        _idd_ = self.global_vars.index( self._name_ )
                                        self.global_values[ _idd_ ] = self._return_['p']
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
                        self.error['s'] = pE.ERRORS( self.line ).ERROR2( self.data_base[ 'assigment' ] )
                        self.data_base[ 'no_printed_values' ]   = []
                        self.data_base[ 'assigment' ]           = None
                else: pass
            else: pass

        
        self.data_base['def_return'] = None 
        
        return self.error['s']