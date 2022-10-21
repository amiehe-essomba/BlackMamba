cdef class DICT:
    cdef public :
        list master 
        dict data_base 
        unsigned long int line 
    cdef:
        str error 
        list variables, _values_, key_names, list_keys
        dict _val_

    def __cinit__(self, master, data_base, line):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.variables      = self.data_base[ 'variables' ][ 'vars' ]
        self._values_       = self.data_base[ 'variables' ][ 'values' ]
        self.error          = ""
        self.list_keys      = []
        self._val_          = {}

    cdef DICT_CHECK(self, str main_string ):

        cdef:
            str main_dict 
            unsigned long int index 
            unsigned int i, j
            dict main_dict_value, Input, _return_ 
            str dict_type = ""
            list name, final


        self.key_names      = self.master[ 'names' ]
        self._val_          = self.master[ 'values' ][ 0 ]
        self.list_keys      = list( self._val_.keys() )

        try:
            main_dict      = self._val_[ 'numeric' ][ 0 ]
            _return_       = {}

            if   self._val_[ 'type' ] is None          :
                if self.variables:
                    main_dict, self.error = STRING_ANALYSE( self.data_base, self.line ).CHECK_NAME( main_dict, True, name="cython" )
                    if not self.error:
                        if main_dict in self.variables:
                            index = self.variables.index( main_dict )
                            
                            if type( self._values_[ index ] ) == type( dict() ):
                                main_dict_value    = self._values_[ index ]
                                for j in range( len( self.key_names ) ):
                                    if self.key_names[ j ] in list( main_dict_value.keys() ):
                                        main_dict_value = main_dict_value[ self.key_names[ j ] ]
                                        if j != len( self.key_names ) - 1:
                                            if type( main_dict_value ) == type( dict() ): pass
                                            else:
                                                self.error = ERRORS( self.line).ERROR3( main_dict_value, 'a dictionary()')
                                                break
                                        else:  pass
                                    else:
                                        self.error = ERRORS( self.line ).ERROR5( main_dict_value.keys(), self.key_names[j] )
                                        break

                                if not self.error :
                                    _return_   = main_dict_value
                                    dict_type  = type( _return_ )
                                else: pass

                            else: self.error = ERRORS( self.line ).ERROR3( main_dict, 'a dictionary()')
                        else:  self.error = ERRORS( self.line ).ERROR2( main_dict )
                    else: pass
                else:
                    main_dict, self.error = self.control.CHECK_NAME(main_dict)
                    if not self.error:  self.error = ERRORS( self.line ).ERROR2( main_dict )
                    else: pass
            elif self._val_[ 'type' ] == 'dictionnary' :
                Input = {'numeric': [ main_dict ], 'type': 'dictionnary' }
                _return_, self.error = get_dictionary.DICTIONARY(Input, self.data_base,
                                                                            self.line ).MAIN_DICT( main_string )
                if not self.error:
                    for j in range(len(self.key_names)):
                        if self.key_names[j] in list( _return_.keys() ):
                            if j == len( self.key_names ) - 1:  
                                if type(_return_[ self.key_names[j]  ]) == type(dict()): _return_ = _return_[ self.key_names[j]  ]
                                else: final = [_return_[ self.key_names[j]  ]]
                            else:
                                if type(_return_[ self.key_names[j]  ]) == type(dict()): _return_ = _return_[ self.key_names[j]  ]
                                else:
                                    self.error = ERRORS( self.line ).ERROR3(_return_[ self.key_names[j]  ], 'a dictionary()')
                                    break
                        else:
                            self.error = ERRORS( self.line ).ERROR5( _return_[ self.key_names[j]  ], self.key_names[j])
                            break
                else: pass

            elif self._val_[ 'type' ] == 'list'        :
                Input = {'numeric': [ main_dict ], 'type': 'list'}
                _return_, self.error = get_list.LIST(Input, self.data_base, self.line).MAIN_LIST(main_string)

                if not self.error:
                    if type( _return_) == type( dict()) :
                        self.names = list( self._return_.keys() )
                        for j in range(len(self.key_names)):
                            if self.key_names[j] in list( _return_.keys() ):
                                self._return_ = self._return_[ self.key_names[j]  ]
                                if j == len(self.key_names) - 1:  
                                    if type(_return_[ self.key_names[j]  ]) == type(dict()) : _return_ = _return_[ self.key_names[j]  ]
                                    else: final = [_return_ = _return_[ self.key_names[j]  ]]
                                else:
                                    if type(_return_[ self.key_names[j]  ]) == type(dict()) : _return_ = _return_[ self.key_names[j]  ]
                                    else:
                                        self.error = ERRORS(self.line).ERROR3(_return_[ self.key_names[j]  ], 'a dictionary()')
                                        break
                            else:
                                self.error = ERRORS(self.line).ERROR5(_return_[ self.key_names[j]  ], keys)
                                break
                    else: self.error = ERRORS( self.line ).ERROR3( _return_, 'a dictionary()')
                else: pass
            elif self._val_[ 'type' ] == 'numeric'     :
                self.error = ERRORS( self.line ).ERROR0( main_string )
        except TypeError: pass