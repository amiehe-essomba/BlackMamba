from src.functions                  import error            as er
from script.DATA_BASE               import data_base        as db
from script.STDIN.LinuxSTDIN        import bm_configure     as bm
from src.functions                  import updating_data, type_of_data
from script.PARXER.LEXER_CONFIGURE  import numeric_lexer
#from numba                          import jit
#from numba.experimental             import jitclass

class FUNCTION:
    def __init__(self, 
        master          : list, 
        data_base       : dict, 
        line            : int
        ):
        
        self.master             = master[ 0 ]
        self.line               = line
        self.data_base          = data_base
        self.global_vars        = self.data_base[ 'global_vars' ]

    def INIT_FUNCTION(self, main_string: str, info_data: dict):
        self.error              = None
        self.function_type      = None
        ###########################################################################
        self.keys               = list( self.master.keys() )
        self.function_name      = self.keys[ 0 ]

        self.get_informations   = self.master[ self.function_name ]
        self.type_of_data       = self.get_informations[ 'type' ][ : ]
        self.arguments          = self.get_informations[ 'arguments' ][ : ]
        self.values             = self.get_informations[ 'value' ][ : ]
        self.int_values         = self.values[ : ]
        self.emty_values        = []
        self.anonymous          = False 
        self.anonymous_data     = []
        
        try:  self.anonymous          = self.get_informations[ 'anonymous' ]
        except KeyError: pass 
        try:
            self.function_type  = self.get_informations[ 'type_return' ]
        except KeyError: pass 
        
        ###########################################################################
        self.computed_values    = info_data[ 'values_computed' ]
        self.external_vars      = info_data[ 'vars' ]
        self.external_values    = info_data[ 'values' ]
        self.location           = info_data[ 'location' ]

        self.lenght_exernal     = len( self.computed_values )
        self.lenght_internal    = len( self.arguments )
        self.sub_length         = 0

        for value in self.values:
            if value is not None: self.sub_length += 1
            else: pass

        self.difference         = self.lenght_internal - self.sub_length

        ###########################################################################
        self.function_names, self.function_expr  = db.DATA_BASE().FUNCTIONS()
        self.def_data_base      =  db.DATA_BASE().STORAGE().copy()

        if self.arguments:
            if self.external_vars:
                if self.anonymous is False:
                    self.check_arguments = []
                    for args in self.external_vars:
                        if not  self.check_arguments:  self.check_arguments.append( args )
                        else:
                            if args not in self.check_arguments:  self.check_arguments.append( args )
                            else:
                                self.error = er.ERRORS( self.line ).ERROR16( self.function_name, args )
                                break
                             
                    if self.error is None:
                        if self.lenght_exernal <= self.lenght_internal:
                            for w, vars in enumerate( self.external_vars ):
                                if vars in self.arguments :
                                    self.idd    = self.arguments.index( vars )
                                    self.values[ self.idd ] = self.computed_values[ self.location[ w ] ]
                                else:  self.error  = er.ERRORS(self.line).ERROR11(self.function_name, vars)

                            if self.error is None:
                                if self.lenght_exernal == len( self.external_vars ): pass
                                else:
                                    loc             = self.location[ : ]
                                    self.location   = sorted( loc, reverse = True )
                                    for i in self.location:
                                        del self.computed_values[ i ]

                                    for value in self.computed_values:
                                        if None in self.values:
                                            self.index = self.values.index( None )
                                            self.values[ self.index ] = value
                                        else: pass

                                for i, value in enumerate( self.values ):
                                    if value is None: self.emty_values.append( ( self.arguments[ i ], i ) )
                                    else: pass

                                if self.emty_values:  self.error = er.ERRORS(self.line).ERROR15(self.function_name, self.emty_values )
                                else: pass
                            else: pass
                        else:  self.error = er.ERRORS(self.line).ERROR12(self.function_name, self.lenght_internal)
                    else: pass
                else: self.error = er.ERRORS(self.line).ERROR26()
            else:
                if self.computed_values:
                    if self.anonymous is False:
                        if self.lenght_internal == 1 :
                            if self.arguments[ 0 ] is None:  self.error = er.ERRORS(self.line).ERROR14( self.function_name )
                            else:
                                if self.lenght_exernal == 1:
                                    for s, value in enumerate( self.computed_values ):
                                        self.values[ s ] = value
                                else: self.error = er.ERRORS(self.line).ERROR12(self.function_name, self.lenght_internal)
                        else:
                            if self.lenght_internal >= self.lenght_exernal:
                                try:
                                    for s, value in enumerate( self.computed_values ):
                                        self.values[ s ] = value

                                    for i, value in enumerate( self.values ):
                                        if value is None:
                                            self.emty_values.append( ( self.arguments[ i ], i ) )
                                        else: pass
                                    if self.emty_values:  self.error = er.ERRORS(self.line).ERROR15(self.function_name, self.emty_values )
                                    else : pass
                                except IndexError: pass
                            else:  self.error = er.ERRORS(self.line).ERROR12( self.function_name, self.lenght_internal )
                    else: self.anonymous_data = self.computed_values.copy()
                else:
                    if self.anonymous is False:
                        if self.lenght_internal == 1:
                            if self.arguments[ 0 ] is None:
                                del self.values[ 0 ]
                                del self.arguments[ 0 ]

                            else:
                                if self.values[ 0 ] is None:  self.error = er.ERRORS(self.line).ERROR15(self.function_name, [(self.arguments[0],0) ])
                                else: pass
                        else:
                            for i, value in enumerate( self.values ):
                                if value is None: self.emty_values.append( (self.arguments[ i ], i ) )
                                else: pass

                            if self.emty_values:  self.error = er.ERRORS(self.line).ERROR15(self.function_name, self.emty_values )
                            else: pass
                    else:
                        del self.values[ 0 ]
                        del self.arguments[ 0 ]
        else:
            if self.external_vars:  self.error = er.ERRORS(self.line).ERROR11( self.function_name, self.external_vars[0] )
            elif self.computed_values:  self.error = er.ERRORS(self.line).ERROR12(self.function_name, 0 )
            else: pass

        if self.error is None:
            if self.anonymous is False:
                self.list_types = ''
                self.func = bm.fg.rbg(0,255,0)+' in {}( ).'.format(self.function_name)+bm.init.reset
                if self.values:
                    for i, value in enumerate( self.values ):
                        self.error = type_of_data.CHECK_TYPE_OF_DATA( self.type_of_data[ i ] ).CHECK_TYPE( self.line, self.arguments[ i ], self.function_name )
                        if self.error is None:
                            if type( value ) == type( str() ):
                                if value not in [ None, '@670532821@656188185@670532821@']:
                                    self._values_, self.error = numeric_lexer.NUMERCAL_LEXER( value, self.data_base,
                                                                                            self.line).LEXER( value )
                                    if self.error is None:
                                        self._type_         = type_of_data.CHECK_TYPE_OF_DATA( self._values_ ).DATA()
                                        
                                        if 'any' in self.type_of_data[ i ] :
                                            if len( self.type_of_data[ i ] ) == 1: self.values[ i ]    = self._values_ 
                                            else: 
                                                for x, _typ_ in enumerate( self.type_of_data[ i ] ):
                                                    if _typ_ == 'any': pass 
                                                    else:
                                                        self.str_type   = type_of_data.CHECK_TYPE_OF_DATA( _typ_ ).TYPE()
                                                        if x < len( self.type_of_data[ i ] ) - 1: self.list_types += self.str_type + ', '
                                                        else                                    : self.list_types += 'or ' + self.str_type
                                                self.error = er.ERRORS( self.line ).ERROR18( self.list_types, self.func )
                                                break
                                        else:
                                            if self._type_ not in self.type_of_data[ i ]:
                                                for x, _typ_ in enumerate( self.type_of_data[ i ] ):
                                                    self.str_type   = type_of_data.CHECK_TYPE_OF_DATA( _typ_ ).TYPE()
                                                    if x < len( self.type_of_data[ i ] ) - 1: self.list_types += self.str_type + ', or '
                                                    else                                    : self.list_types += self.str_type
                                                        
                                                self.error = er.ERRORS( self.line ).ERROR3( self.arguments[i], self.list_types, self.func)
                                                break
                                            else: self.values[ i ] = self._values_ 
                                    else: break
                                else: self.values[ i ] = '@670532821@656188185@670532821@'
                            else: pass
                        else: break
                else: pass
            else: pass
            
            if self.anonymous_data: 
                for i , value in enumerate( self.anonymous_data):
                    self._values_, self.error =numeric_lexer.NUMERCAL_LEXER( value, self.data_base, self.line).LEXER( value )
                    if self.error is None: self.anonymous_data[i] = self._values_ 
                    else:break
                if self.error is None:
                    if 'anonymous' in self.global_vars['vars']:
                        self.idd = self.global_vars['vars'].index("anonymous")
                        self.global_vars['values'][self.idd] = self.anonymous_data.copy()
                    else:
                        self.global_vars['vars'].append('anonymous')
                        self.global_vars['values'].append(self.anonymous_data.copy())
                else: pass
            else: 
                if  self.anonymous is False: pass 
                else: self.error = er.ERRORS(self.line).ERROR27( self.function_name )
            if self.error is None:
                updating_data.UPDATE_DATA_BASE( self.values.copy(), self.arguments.copy(), self.global_vars.copy() ).UPDATE( self.def_data_base )
            else: pass
        else: pass

        self._return_     = {
            'data_base'         : self.def_data_base,
            'vars'              : self.arguments,
            'values'            : self.int_values,
            'type'              : self.function_type,
            'anonymous'         : self.anonymous
        }
    
        return  self._return_, self.error

    def DOUBLE_INIT_FUNCTION(self, main_string: str, function_name: str):
        self.error              = None
        self.function_name      = function_name

        self.get_informations   = self.master[ self.function_name ]
        self.type_of_data       = self.get_informations[ 'type' ]
        self.arguments          = self.get_informations[ 'arguments' ]
        self.values             = self.get_informations[ 'value' ]
        self.new_list_of_data   = []
        self.location           = []

        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] is None:
                del self.arguments[ 0 ]
                del self.values[ 0 ]
            else: pass
        else: pass

        if self.values:
            self.decrement = 0
            for i, value in enumerate( self.values ):
                if value is not None:
                    if self.error is None:
                        self.new_list_of_data.append( value )
                        self.location.append( i )
                    else: break
                else:
                    self.new_list_of_data.append( self.arguments[ i - self.decrement ] )
                    self.values[ i ]    = self.arguments[ i - self.decrement ]
                    del self.arguments[ i - self.decrement ]
                    self.decrement += 1
        else: pass

        self._return_ = {
            'values_computed'   : self.new_list_of_data,
            'values'            : self.values,
            'vars'              : self.arguments,
            'location'          : self.location
        }

        return self._return_,  self.error