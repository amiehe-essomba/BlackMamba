from src.transform                  import error as er
from script.STDIN.LinuxSTDIN        import bm_configure as bm
from CythonModules.Windows          import making_stat  as ms


class STAT:
    def __init__(self, _value_ : any, value: any, line : int):
        self._value_    = _value_ 
        self.value      = value
        self.line       = line
    
    def COV_CORR_LINEAR( self ):
        self.error          = None
        self.final_value    = None
        self._              = None 
        
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 2 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
            if self._value_[ 0 ]:
                if self._value_[ 1 ]:
                    if len(self._value_[ 0 ]) == len(self._value_[ 1 ]):
                        _type_      = self._value_[ 3 ]
                        cal_type    = self._value_[ 2 ]
                        if   type( self._value_[ 0 ] ) in [type( range(1) )]    :
                            if type( self._value_[ 1 ] ) == type( range( 1 ) )  :
                                self.final_value, self._, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).cov_corr_linear_r( list( self._value_[ 1 ]),
                                                                        cal_type = cal_type, ob_type1 = 'range', ob_type2 = 'range', _type_ = _type_)                           
                                if self.error == '': self.error = None 
                                else: pass
                            elif type( self._value_[ 1 ] ) == type( tuple() )   :
                                self.final_value, self._, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).cov_corr_linear_r( list( self._value_[ 1 ]),
                                                                        cal_type = cal_type, ob_type1 = 'range', ob_type2 = 'tuple', _type_ = _type_)                         
                                if self.error == '': self.error = None 
                                else: pass
                            elif type( self._value_[ 1 ] ) == type( list() )    :
                                self.final_value, self._, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).cov_corr_linear_r( self._value_[ 1 ],
                                                                        cal_type = cal_type, ob_type1 = 'range', ob_type2 = 'list', _type_ = _type_)                         
                                if self.error == '': self.error = None 
                                else: pass
                        elif type( self._value_[ 0 ] ) in [type( tuple( ) )]    :
                            if type( self._value_[ 1 ] ) == type( range( 1 ) ):
                                self.final_value, self._, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).cov_corr_linear_r( list( self._value_[ 1 ]),
                                                                        cal_type = cal_type, ob_type1 = 'tuple', ob_type2 = 'range', _type_ = 'pop')                           
                                if self.error == '': self.error = None 
                                else: pass
                            elif type( self._value_[ 1 ] ) == type( list( 1 ) ):
                                self.final_value, self._, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).cov_corr_linear_r( list( self._value_[ 1 ]),
                                                                        cal_type = cal_type, ob_type1 = 'tuple', ob_type2 = 'tuple', _type_ = 'pop')                         
                                if self.error == '': self.error = None 
                                else: pass
                            elif type( self._value_[ 1 ] ) == type( list() ):
                                self.final_value, self._, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).cov_corr_linear_r( self._value_[ 1 ],
                                                                        cal_type = cal_type, ob_type1 = 'tuple', ob_type2 = 'list', _type_ = 'pop')                         
                                if self.error == '': self.error = None 
                                else: pass
                        else:
                            if type( self._value_[ 1 ] ) in [type(tuple())]:
                                self.final_value, self._, self.error = ms.GetValue( self._value_[ 0 ], self.line ).cov_corr_linear_r( list( self._value_[ 1 ]),
                                                                        cal_type = cal_type, ob_type1 = 'list', ob_type2 = 'typle', _type_ = _type_)
                                if self.error == '': self.error = None 
                                else: pass
                            elif type( self._value_[ 1 ] ) in [type( range( 1 ) )]:
                                self.final_value, self._, self.error = ms.GetValue( self._value_[ 0 ], self.line ).cov_corr_linear_r( list( self._value_[ 1 ]),
                                                                        cal_type = cal_type, ob_type1 = 'list', ob_type2 = 'range', _type_ = _type_)
                                if self.error == '': self.error = None 
                                else: pass
                            else:
                                self.final_value, self._, self.error = ms.GetValue( self._value_[ 0 ], self.line ).cov_corr_linear_r( self._value_[ 1 ], 
                                                                        cal_type = cal_type, ob_type1 = 'list', ob_type2 = 'list', _type_ = _type_)
                    
                                if self.error == '': self.error = None 
                                else: pass      
                    else: self.error = er.ERRORS( self.line ).ERROR6( 'master1', 'master2', func=func ) 
                else: self.error = er.ERRORS( self.line ).ERROR11( self._value_[ 1 ], func=func ) 
            else: self.error = er.ERRORS( self.line ).ERROR11( self._value_[ 0 ], func=func ) 
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func ) 
        
        if self._value_[ 2 ] == 'linearR':  return (self.final_value, self._), self.error
        else : return self.final_value, self.error
    
    def QUANTILE( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 2 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
            if self._value_[ 0 ]:
                if self._value_[ 2 ] == 'quantiles':
                    if 0 < self._value_[ 1 ]: pass 
                    else: self.error = er.ERRORS( self.line ).ERROR25( 'numeric', func=func )
                else:
                    if 0 < self._value_[ 1 ] <= 1.0: pass 
                    else:
                        if self._value_[ 1 ] < 1.0: self.error = er.ERRORS( self.line ).ERROR25( 'numeric', func=func ) 
                        else:  self.error = er.ERRORS( self.line ).ERROR26( 'numeric', func=func ) 
                
                if self.error is None:
                    if type(self._value_[ 0 ]) in [type(range(1))]: 
                        self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).quantiles(ob_type = 'range',
                                                                                numeric = self._value_[ 1 ], mod = self._value_[ 2 ] )                           
                        if self.error == '': self.error = None 
                        else: pass
                    elif type(self._value_[ 0 ]) in [type(tuple())]: 
                        self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).quantiles(ob_type = 'tuple',
                                                                                numeric = self._value_[ 1 ], mod = self._value_[ 2 ] )                           
                        if self.error == '': self.error = None 
                        else: pass
                    elif type(self._value_[ 0 ]) in [type(list())]: 
                        self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).quantiles(ob_type = 'list',
                                                                                numeric = self._value_[ 1 ], mod = self._value_[ 2 ] )                         
                        if self.error == '': self.error = None 
                        else: pass
                else: pass
            else: self.error = er.ERRORS( self.line ).ERROR11( self._value_[ 0 ], func=func ) 
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        
        return self.final_value, self.error
    
    def MOD_MULMOD( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 1 ]) + bm.init.reset 
        cal_type            = self._value_[ 1 ]
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
            if self._value_[ 0 ]:
                if type(self._value_[ 0 ]) in [type(range(1))]: 
                    self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).mod_mulmod(cal_type = cal_type, ob_type = 'range')                           
                    if self.error == '': self.error = None 
                    else: pass
                elif type(self._value_[ 0 ]) in [type(tuple())]: 
                    self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).mod_mulmod(cal_type = cal_type, ob_type = 'tuple')                           
                    if self.error == '': self.error = None 
                    else: pass
                elif type(self._value_[ 0 ]) in [type(list())]: 
                    self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).mod_mulmod(cal_type = cal_type, ob_type = 'list')                           
                    if self.error == '': self.error = None 
                    else: pass
            else: self.error = er.ERRORS( self.line ).ERROR11( self._value_[ 0 ], func=func ) 
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error
     
    def MED_MEDH_MEDL_MEDG( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 1 ]) + bm.init.reset 
        cal_type            = self._value_[ 1 ]
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
            if self._value_[ 0 ]:
                if type(self._value_[ 0 ]) in [type(range(1))]: 
                    self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).med_medh_medl_medg(cal_type = cal_type, ob_type = 'range')                           
                    if self.error == '': self.error = None 
                    else: pass
                elif type(self._value_[ 0 ]) in [type(tuple())]: 
                    self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).med_medh_medl_medg(cal_type = cal_type, ob_type = 'tuple')                           
                    if self.error == '': self.error = None 
                    else: pass
                elif type(self._value_[ 0 ]) in [type(list())]:
                    self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).med_medh_medl_medg(cal_type = cal_type, ob_type = 'list')                           
                    if self.error == '': self.error = None 
                    else: pass
            else: self.error = er.ERRORS( self.line ).ERROR11( self._value_[ 0 ], func=func ) 
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error
    
    def KURTOSIS( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 2 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
            _type_ = self._value_[ 1 ]
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).kurtosis( ob_type = 'range', _type_ = _type_)                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).kurtosis( ob_type = 'tuple', _type_ = _type_)                      
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).kurtosis( ob_type = 'list', _type_ = _type_)                        
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error
    
    def SKEWNESS( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 2 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
            _type_ = self._value_[ 1 ]
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).skewness( ob_type = 'range', _type_ = _type_)                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).skewness( ob_type = 'tuple', _type_ = _type_)                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).skewness( ob_type = 'list', _type_ = _type_)                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error
     
    def IQUANTILE( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 2 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
            _type_ = self._value_[ 1 ]
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).iquantile( ob_type = 'range', _type_ = _type_)                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).iquantile( ob_type = 'tuple', _type_ = _type_)                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).iquantile( ob_type = 'list', _type_ = _type_)                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error  

    def MAD( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 1 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
        
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).mad( ob_type = 'range')                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).mad( ob_type = 'tuple')                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).mad( ob_type = 'list')                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error 

    def RMS( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 1 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
        
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).rms( ob_type = 'range')                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).rms( ob_type = 'tuple')                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).rms( ob_type = 'list')                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error
    
    def SUM_SQUARE( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 1 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
        
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).sum_square( ob_type = 'range')                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).sum_square( ob_type = 'tuple')                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).sum_square( ob_type = 'list')                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error
    
    def MIDRANGE( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 1 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
        
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).midrange( ob_type = 'range')                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).midrange( ob_type = 'tuple')                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).midrange( ob_type = 'list')                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error

    def RSD( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 2 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
            _type_ = self._value_[ 1 ]
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).rsd( ob_type = 'range', _type_ = _type_)                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).rsd( ob_type = 'tuple', _type_ = _type_)                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).rsd( ob_type = 'list', _type_ = _type_)                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error 

    def Q1_Q3( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 2 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
            _type_ = self._value_[ 1 ]
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).q1_q3( ob_type = 'range', _type_ = _type_)                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).q1_q3( ob_type = 'tuple', _type_ = _type_)                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).q1_q3( ob_type = 'list', _type_ = _type_)                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error
    
    def STD_ERRPR( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 2 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
            _type_ = self._value_[ 1 ]
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).std_error( ob_type = 'range', _type_ = _type_)                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).std_error( ob_type = 'tuple', _type_ = _type_)                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).std_error( ob_type = 'list', _type_ = _type_)                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error 
    
    def LOWER_UPPER_FENCE( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 2 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
            _type_      = self._value_[ 1 ]
            cal_type    = self._value_[ 2 ]
            
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).lower_upper_fence( ob_type = 'range', _type_ = _type_,
                                                                                                    cal_type=cal_type)                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).lower_upper_fence( ob_type = 'tuple', _type_ = _type_,
                                                                                                    cal_type=cal_type)                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).lower_upper_fence( ob_type = 'list', _type_ = _type_,
                                                                                                    cal_type=cal_type)                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error  
             
    def GROUPED( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 1 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
        
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).grouped( ob_type = 'range')                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).grouped( ob_type = 'tuple')                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).grouped( ob_type = 'list')                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error
    
    def H_MEAN( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 1 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
        
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).harmonic_mean( ob_type = 'range')                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).harmonic_mean( ob_type = 'tuple')                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).harmonic_mean( ob_type = 'list')                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error
    
    def G_MEAN( self ):
        self.error          = None
        self.final_value    = None
        self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 1 ]) + bm.init.reset 
        
        if type( self._value_[ 0 ] ) in self.type_accepted:
        
            if type(self._value_[ 0 ]) in [type(range(1))]: 
                self.final_value,  self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).geometric_mean( ob_type = 'range')                           
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(tuple())]: 
                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).geometric_mean( ob_type = 'tuple')                       
                if self.error == '': self.error = None 
                else: pass
            elif type(self._value_[ 0 ]) in [type(list())]:
                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).geometric_mean( ob_type = 'list')                         
                if self.error == '': self.error = None 
                else: pass
        else: self.error = er.ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        return self.final_value, self.error
    
    def FACTORIAL(self):
        self.final_value    = 1
        self.error          = None
        func                = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format(self._value_[ 1 ]) + bm.init.reset 
        
        if self._value_[ 0 ] >= 0:
            for i in range( self._value_[ 0 ]+1 ):
                if i == 0:  i = 1
                else: pass 

                self.final_value *= i 
        else: self.error = er.ERRORS( self.line ).ERROR27(self._value_[ 0 ], func)
                
        return self.final_value, self.error