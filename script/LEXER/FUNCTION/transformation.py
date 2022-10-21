import                              random
import                              math
import                              numpy as np
from statistics                     import variance, pvariance
from script                         import control_string
from script.LEXER                   import particular_str_selection
from script.PARXER.LEXER_CONFIGURE  import numeric_lexer
from script.MATHS                   import arithmetic_object as arr
from script.DATA_BASE               import ansi
from src.transform                  import error as er
from src.transform                  import statistics as st
from src.transform                  import matrix_modules as mm
from src.transform                  import matrix_statistics as mstat
from src.transform                  import open_check as oc
from script.STDIN.LinuxSTDIN        import bm_configure as bm
try:
    from CythonModules.Linux        import making_stat as ms
    from CythonModules.Linux        import fileError as fe 
    from CythonModules.Linux        import bm_statistics as bms
except ImportError:
    from CythonModules.Windows      import making_stat as ms
    from CythonModules.Windows      import fileError as fe 
    from CythonModules.Windows      import bm_statistics as bms
    
try: from CythonModules.Linux       import help
except ImportError :
    from CythonModules.Windows      import help
try:from CythonModules.Linux        import Tuple
except ImportError :
    from CythonModule.Windows       import Tuple 

try: from CythonModules.Windows     import arithmetic_analyze as aa
except ImportError: 
    from CythonModules.Linux        import arithmetic_analyze as aa

try: from CythonModules.Windows     import array_to_list as atl
except ImportError: 
    from CythonModules.Linux        import array_to_list as atl


class C_F_I_S:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.selection          = particular_str_selection
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_par            = numeric_lexer

    def FUNCTION(self, function = '_int_'):
        self.error              = None
        self.normal_string      = function + ' ' + self.master
        self.list_of_values     = None
        self.final_value        = None

        self.master, self.error = self.control.DELETE_SPACE( self.master )
        if self.error is None:
            if self.master[ 0 ] == '*':
                self.master, self.error = self.control.DELETE_SPACE( self.master[1 : ])
                if self.error is None:
                    self.list_of_values, self.error = self.selection.SELECTION( self.master, self.master,
                                                                        self.data_base, self.line).CHAR_SELECTION( ',' )
                    if self.error is None:
                        if len( self.list_of_values )   == 1:
                            self.value, self.error = self.control.DELETE_SPACE( self.list_of_values[ 0 ] )
                            if self.error is None:
                                self._value_, self.error = self.lex_par.NUMERCAL_LEXER( self.value, self.data_base,
                                                                                    self.line ).LEXER( self.value )
                              
                                if self.error is None:
                                    self.type =  [ type( int() ), type( float() ), type( complex()), type( str() ),
                                            type( bool()), type(list()), type(tuple()), type(dict()), type(range(1)), type(np.array([])) ]
                                    if type( self._value_ ) in self.type:
                                        if   function in [ '_int_'     ]    :
                                            try:
                                                self.final_value = int( float(  self._value_ ) )
                                            except (ValueError, TypeError):
                                                func = bm.fg.rbg(0, 255, 0   )+' in integer( ).' + bm.init.reset 
                                                self.error = er.ERRORS( self.line ).ERROR2( self.value, func=func )
                                        elif function in [ '_float_'   ]    :
                                            try:
                                                self.final_value = float(  self._value_ )
                                            except (ValueError, TypeError):
                                                func = bm.fg.rbg(0, 255, 0   )+' in float( ).' + bm.init.reset 
                                                self.error = er.ERRORS( self.line ).ERROR2( self.value, 'a float', func )
                                        elif function in [ '_complex_' ]    :
                                            try:
                                                self.final_value = complex( self._value_ )
                                            except (ValueError, TypeError):
                                                func = bm.fg.rbg(0, 255, 0   )+' in complex( ).' + bm.init.reset 
                                                self.error = er.ERRORS( self.line ).ERROR2( self.value, 'a complex', func )
                                        elif function in [ '_string_'  ]    :
                                            try:
                                                if self._value_:
                                                    self.final_value = str( self._value_ )
                                                else:
                                                    self.final_value = '""'
                                            except (ValueError, TypeError):
                                                func = bm.fg.rbg(0, 255, 0   )+' in string( ).' + bm.init.reset 
                                                self.error = er.ERRORS( self.line ).ERROR2( self.value, 'a string',func=func )
                                        elif function in [ '_boolean_' ]    :
                                            try:
                                                self.final_value = bool( self._value_ )
                                            except (ValueError, TypeError):
                                                func = bm.fg.rbg(0, 255, 0   )+' in boolean( ).' + bm.init.reset 
                                                self.error = er.ERRORS( self.line ).ERROR2( self.value, 'a boolean', func )
                                        elif function in [ '_list_'    ]    :
                                            func = bm.fg.rbg(0, 255, 0   )+' in list( ).' + bm.init.reset 
                                            try:
                                                if type(self._value_) == self.type[-1]:
                                                    self.final_value = atl.ndarray(list(self._value_), self.line).List()
                                                else:  self.final_value = list( self._value_ )
                                            except (ValueError, TypeError):
                                                self.error = er.ERRORS( self.line ).ERROR2( self.value, 'a list', func )
                                        elif function in [ '_tuple_'   ]    :
                                            self.final_value, self.error = Tuple.Tuple( self.line ).Tuple(Obj = self._value_, String=self.value )                                       
                                        elif function in [ '_sqrt_'    ]    :
                                            func = bm.fg.rbg(0, 255, 0   )+' in sqrt( ).' + bm.init.reset 
                                            if type( self._value_ ) in [type(float()), type(int()), type(bool())]:
                                                if self._value_ >= 0:
                                                    self.final_value = self._value_ ** (0.5)
                                                else:
                                                    self.error = er.ERRORS( self.line ).ERROR7( self.value, func )
                                            else:
                                                self.error = er.ERRORS( self.line ).ERROR8( self.value, func )
                                        elif function in [ '_length_'  ]    :
                                            if type( self._value_ ) in [type(list()), type(tuple()), type( range(1))]:
                                                self.final_value = len( self._value_ )
                                            elif type( self._value_ ) == type( str() ):
                                                self.final_value = len( self._value_ )
                                            else:
                                                func = bm.fg.rbg(0, 255, 0   )+' in length( ).' + bm.init.reset 
                                                self.error = er.ERRORS( self.line ).ERROR9( self.value, func=func )
                                        elif function in [ '_sum_'     ]    :
                                            self._typ_          = [type(float()), type(bool()), type(int())]
                                            self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
                                            func = bm.fg.rbg(0, 255, 0   )+' in sum( ).' + bm.init.reset 
            
                                            if type( self._value_ ) in self.type_accepted:
                                                if self._value_:
                                                    if len( self._value_ ) > 1:
                                                        if type( self._value_ ) == type( range( 1 ) ):
                                                            self.final_value = sum( self._value_ )
                                                        else:
                                                            try:
                                                                self.final_value, self.error = ms.GetValue( self._value_, self.line ).sum()
                                                                if self.error == '': self.error = None 
                                                                else: pass
                                                            except TypeError:        
                                                                self.final_value, self.error = ms.GetValue( list( self._value_), self.line ).sum()
                                                                if self.error == '': self.error = None 
                                                                else: pass
                                           
                                                    else:
                                                        self.sum    = 0
                                                        if type( self._value_[ 0 ] ) in self._typ_:
                                                            self.final_value = self._value_[ 0 ]
                                                        else:
                                                            self.error = er.ERRORS(self.line).ERROR10(self.sum,
                                                                                        self._value_[ 0 ], func = func )
                                                else:
                                                    self.error = er.ERRORS( self.line ).ERROR11( self.value, func=func )
                                            else:
                                                self.error = er.ERRORS( self.line ).ERROR13( self.value, func=func )
                                        elif function in [ '_min_'     ]    :
                                            self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
                                            func = bm.fg.rbg(0, 255, 0   )+' in min( ).' + bm.init.reset 
                                            if type( self._value_ ) in self.type_accepted:
                                                #if self._value_:
                                                 
                                                if type( self._value_ ) == type( range( 1 ) ):
                                                    self.final_value = self._value_[ 0 ] 
                                                else:
                                                    try:
                                                        self.final_value, self.error = ms.GetValue( self._value_, self.line ).min_max( 'min' )
                                                        if self.error == '': self.error = None 
                                                        else: pass
                                                    except TypeError:        
                                                        self.final_value, self.error = ms.GetValue( list( self._value_), self.line ).min_max( 'min' )
                                                        if self.error == '': self.error = None 
                                                        else: pass
                                                #else:
                                                #    self.error = ERRORS( self.line ).ERROR11( self.value, func=func )
                                            else:
                                                self.error = er.ERRORS( self.line ).ERROR13( self.value, func=func )                                     
                                        elif function in [ '_var_'     ]    :
                                            self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
                                            func = bm.fg.rbg(0, 255, 0   )+' in var( ).' + bm.init.reset 
                                
                                            if type( self._value_[ 0 ] ) in self.type_accepted:
                                                if self._value_[ 0 ]:
                                                    if self._value_[ 1 ] == 'pop':
                                                        if type( self._value_[ 0 ] ) == type( range( 1 ) ):
                                                            self.final_value = pvariance( self._value_[ 0 ] ) 
                                                        else:
                                                            try:
                                                                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).var_std( 'var',
                                                                                                                        _type_ = 'pop', ob_type = 'list' )
                                                                if self.error == '': self.error = None 
                                                                else: pass
                                                            except TypeError:        
                                                                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).var_std( 'var',
                                                                                                                                        _type_ = 'pop', ob_type = 'tuple' )
                                                                if self.error == '': self.error = None 
                                                                else: pass
                                                                
                                                    elif self._value_[ 1 ] == 'sam':
                                                        if type( self._value_[ 0 ] ) == type( range( 1 ) ):
                                                            self.final_value = variance( self._value_[ 0 ] ) 
                                                        else:
                                                            try:
                                                                self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).var_std( 'var',
                                                                                                                        _type_ = 'sam', ob_type = 'list' )
                                                                if self.error == '': self.error = None 
                                                                else: pass
                                                            except TypeError:        
                                                                self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).var_std( 'var',
                                                                                                                                        _type_ = 'sam', ob_type = 'tuple' )
                                                                if self.error == '': self.error = None 
                                                else:
                                                    self.error = er.ERRORS( self.line ).ERROR11( self.value, func=func )
                                            else:
                                                self.error = er.ERRORS( self.line ).ERROR13( self.value, func=func ) 
                                        elif function in [ '_std_'     ]    :
                                            if self._value_[ -1 ] in ['cov', 'cor', 'linearR']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).COV_CORR_LINEAR() 
                                            elif self._value_[ -1 ] in ['quantiles', 'quantile']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).QUANTILE() 
                                            elif self._value_[ -1 ] in ['mode', 'mul_mode']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).MOD_MULMOD() 
                                            elif self._value_[ -1 ] in ['med', 'medl', 'medg', 'medh']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).MED_MEDH_MEDL_MEDG() 
                                            elif self._value_[ -1 ] in ['iquantile']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).IQUANTILE()
                                            elif self._value_[ -1 ] in ['kurtosis']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).KURTOSIS()
                                            elif self._value_[ -1 ] in ['skewness']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).SKEWNESS()
                                            elif self._value_[ -1 ] in ['mad']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).MAD()
                                            elif self._value_[ -1 ] in ['lower_fence', 'upper_fence']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).LOWER_UPPER_FENCE()
                                            elif self._value_[ -1 ] in ['rms']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).RMS()
                                            elif self._value_[ -1 ] in ['rsd']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).RSD()
                                            elif self._value_[ -1 ] in ['std_error']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).STD_ERRPR()
                                            elif self._value_[ -1 ] in ['midrange']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).MIDRANGE()
                                            elif self._value_[ -1 ] in ['sum_square']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).SUM_SQUARE()
                                            elif self._value_[ -1 ] in ['grouped']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).GROUPED()
                                            elif self._value_[ -1 ] in ['Q1', 'Q3']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).Q1_Q3()
                                            elif self._value_[ -1 ] in ['facto']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).FACTORIAL()
                                            elif self._value_[ -1 ] in ['harmonic_mean']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).H_MEAN()
                                            elif self._value_[ -1 ] in ['geometric_mean']:
                                                self.final_value, self.error = st.STAT( self._value_, self.value, self.line ).G_MEAN()
                                            elif self._value_[ -1 ] in [ 'License' ]:
                                                bm.open_graven().open_graven_web()
                                            elif self._value_[ -1 ] in [ 'help' ]:
                                                help.HELP(self._value_[ 0 ]).HELP()
                                            elif self._value_[ -1 ] in [ 'matrix' ]:
                                                
                                                self.typ = [type(list()), type(tuple()), type(range(1))]
                                                if type(self._value_[0]) == type(list()): pass
                                                else: self._value_[0] = list(self._value_[0])

                                                self.final_value, self.error = mm.MATRIX(self._value_[0], self._value_[1],self._value_[2],
                                                                          self._value_[3], self.line).MATRIX(self._value_[5], ctype=self._value_[4])

                                                if self.error is None:
                                                    self.func = bm.fg.rbg(0, 255, 0) + ' in {}( ).'.format( self._value_[4] ) + bm.init.reset
                                                    if self._value_[4] is None:  self.final_value = np.array( self.final_value )
                                                    else:
                                                        if self._value_[4] == 'sorted':
                                                            self.final_value = np.sort( self.final_value )
                                                        else:
                                                            self.final_value, self.error = mstat.R(self.final_value, self._value_, self.line).R()
                                                else: pass

                                                self.data_base['matrix'] = True
                                            else:
                                                self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
                                                func = bm.fg.rbg(0, 255, 0   )+' in std( ).' + bm.init.reset 
                                            
                                                if type( self._value_[ 0 ] ) in self.type_accepted:
                                                    if self._value_[ 0 ]:
                                                        
                                                        if self._value_[ 1 ] == 'pop':
                                                            if type( self._value_[ 0 ] ) == type( range( 1 ) ):
                                                                #self.final_value = pstdev( self._value_[ 0 ] ) 
                                                                self.final_value, self.error = ms.Range( self._value_[ 0 ], self.line ).var_std( 'std', 'pop' )                           
                                                                if self.error == '': self.error = None 
                                                                else: pass
                                                            else:
                                                                try:
                                                                    self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).var_std( 'std',
                                                                                                                                _type_ = 'pop', ob_type = 'list')
                                                                    if self.error == '': self.error = None 
                                                                    else: pass
                                                                except TypeError:        
                                                                    self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).var_std( 'std',
                                                                                                                                    _type_ = 'pop', ob_type = 'tuple')
                                                                    if self.error == '': self.error = None 
                                                                    else: pass
                                                        elif self._value_[ 1 ] == 'sam':
                                                            if type( self._value_[ 0 ] ) == type( range( 1 ) ):
                                                                #self.final_value = stdev( self._value_[ 0 ] ) 
                                                                self.final_value, self.error = ms.Range( self._value_[ 0 ], self.line ).var_std( 'std', 'sam' )                           
                                                                if self.error == '': self.error = None 
                                                                else: pass
                                                            else:
                                                                try:
                                                                    self.final_value, self.error = ms.GetValue( self._value_[ 0 ], self.line ).var_std( 'std',
                                                                                                                                _type_ = 'sam', ob_type = 'list')
                                                                    if self.error == '': self.error = None 
                                                                    else: pass
                                                                except TypeError:        
                                                                    self.final_value, self.error = ms.GetValue( list( self._value_[ 0 ]), self.line ).var_std( 'std',
                                                                                                                                    _type_ = 'sam', ob_type = 'tuple')
                                                                    if self.error == '': self.error = None 
                                                                    else: pass
                                                    else: self.error = er.ERRORS( self.line ).ERROR11( self.value, func=func )
                                                else: self.error = er.ERRORS( self.line ).ERROR13( self.value, func=func )                    
                                        elif function in [ '_max_'     ]    :
                                            self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
                                            func = bm.fg.rbg(0, 255, 0   )+' in max( ).' + bm.init.reset 
                                            
                                            if type( self._value_ ) in self.type_accepted:
                                                if self._value_:
                                                 
                                                    if type( self._value_ ) == type( range( 1 ) ):
                                                        self.final_value = self._value_[ -1 ] 
                                                    else:
                                                        try:
                                                            self.final_value, self.error = ms.GetValue( self._value_, self.line ).min_max( 'max')
                                                            if self.error == '': self.error = None 
                                                            else: pass
                                                        except TypeError:        
                                                            self.final_value, self.error = ms.GetValue( list( self._value_), self.line ).min_max( 'max' )
                                                            if self.error == '': self.error = None 
                                                            else: pass
                                                else:
                                                    self.error = er.ERRORS( self.line ).ERROR11( self.value, func=func )
                                            else:
                                                self.error = er.ERRORS( self.line ).ERROR13( self.value, func=func )                
                                        elif function in [ '_mean_'    ]    :
                                            self._typ_          = [type(float()), type(bool()), type(int())]
                                            self.type_accepted  = [type(list()), type(tuple()), type(range(1))]
                                            func = bm.fg.rbg(0, 255, 0   )+' in mean( ).' + bm.init.reset 
                                           
                                            if type( self._value_ ) in self.type_accepted:
                                                if self._value_:
                                                    if len( self._value_ ) >= 1:
                                                        if type( self._value_ ) == type( range( 1 ) ):
                                                            self.mean, self.error = arr.ARITHMETICS( self.data_base,
                                                                                    self.line ).OBJECT_DIV(                  
                                                                sum( self._value_ ), len( self._value_) )
                                                                
                                                            if self.error is None: self.final_value = self.mean
                                                            else: self.error + func

                                                        else:
                                                            try:
                                                                self.final_value, self.error = ms.GetValue( self._value_, self.line).mean( len( self._value_) )
                                                                if self.error == '': self.error = None
                                                                else: pass
                                                            except TypeError:
                                                                self.final_value, self.error = ms.GetValue( list( self._value_), self.line).mean( len( self._value_) )
                                                                if self.error == '': self.error = None
                                                                else: pass
                                                    else:  self.error = er.ERRORS(self.line).ERROR11(self.value, func = func )
                                                else: self.error = er.ERRORS( self.line ).ERROR11( self.value, func=func )
                                            else:  self.error = er.ERRORS( self.line ).ERROR13( self.value, func=func )
                                        elif function in [ '_rang_'    ]    :
                                            if len( self._value_ ) == 3:
                                                self.start, self.end, self.step = self._value_
                                                if self.start < self.end:
                                                    if self.step < self.end: self.final_value = range( self.start, self.end, self.step )
                                                    else:  self.error = er.ERRORS(self.line).ERROR12('step', 'stoped')
                                                else:  self.error = er.ERRORS(self.line).ERROR12('started', 'stoped')
                                            elif len( self._value_ ) == 2:
                                                self.start, self.end = self._value_
                                                if self.start < self.end:  self.final_value = range( self.start, self.end )
                                                else:  self.error = er.ERRORS( self.line ).ERROR12( 'started', 'stoped' )
                                            else: self.final_value = range(self._value_[ 0 ])
                                        elif function in [ '__ansii__' ]    :
                                            func = bm.fg.rbg(0, 255, 0   )+' in ansi( ).' + bm.init.reset 
                                
                                            if type( self._value_ ) == type( tuple() ):
                                                if len( self._value_ ) == 2:
                                                    self.back_end       = self._value_[ 0 ]
                                                    self.front_end      = self._value_[ 1 ]
                                                    self.final_value, self.error = ansi.output( self.front_end,
                                                                            self.line, self.back_end ).output()
                                                else: self.error = er.ERRORS( self.line ).ERROR15( self.value , func=func )
                                            else: self.error = er.ERRORS( self.line ).ERROR14( self.value, 'a tuple()', func=func )
                                        elif function in [ '__show__'  ]    :
                                            self.final_value = u"{}".format(self._value_)
                                        elif function in [ '_get_line_']    :
                                            self.final_value = self.line-1
                                        elif function in [ '__scan__'  ]    :
                                            self.final_value = input( self._value_ )
                                        elif function in [ '__open__'  ]    :
                                            self._open_  = self._value_[ 'open']
                                            self._open_, self.error = oc.OPEN_CHECK( self._open_, self.data_base, self.line ).CHECK()
                                            
                                            if self.error is None:
                                                if not self.data_base[ 'open' ][ 'name' ]:
                                                    self.data_base[ 'open' ][ 'name' ].append(self._open_[ 0 ])
                                                    self.data_base[ 'open' ][ 'file' ].append(self._open_[ 1 ])   
                                                    self.data_base[ 'open' ][ 'action' ].append(self._open_[ 2 ])   
                                                    self.data_base[ 'open' ][ 'status' ].append(self._open_[ 3 ])  
                                                    self.data_base[ 'open' ][ 'encoding' ].append(self._open_[ 4 ])
                                                    self.data_base[ 'open'][ 'nonCloseKey' ].append( self._open_[ 0 ] )
                                                    self.data_base[ 'open' ]
                                                else:
                                                    if self._open_[ 0 ] in self.data_base[ 'open' ][ 'name' ]:
                                                        self.error = er.ERRORS( self.line ).ERROR18( self._open_[ 0 ] )
                                                    else:
                                                        self.data_base[ 'open' ][ 'name' ].append(self._open_[ 0 ])
                                                        self.data_base[ 'open' ][ 'file' ].append(self._open_[ 1 ])   
                                                        self.data_base[ 'open' ][ 'action' ].append(self._open_[ 2 ])   
                                                        self.data_base[ 'open' ][ 'status' ].append(self._open_[ 3 ])  
                                                        self.data_base[ 'open' ][ 'encoding' ].append(self._open_[ 4 ])
                                                        self.data_base[ 'open'][ 'nonCloseKey' ].append( self._open_[ 0 ] )
                                                        self.final_value = self.data_base[ 'open' ]
                                                self.final_value = self.data_base[ 'open']
                                            else: pass
                                    else: self.error = er.ERRORS( self.line ).ERROR3( self.value )
                                else: self.error = self.error
                            else: self.error = er.ERRORS( self.line ).ERROR0( self.normal_string )
                        elif len( self.list_of_values ) == 2:
                            self._values_ = []
                            for value in self.list_of_values:
                                self.value = value
                                self._value_, self.error = self.lex_par.NUMERCAL_LEXER(self.value,
                                                                    self.data_base, self.line).LEXER(  self.value )
                                if self.error is None: self._values_.append( self._value_ )
                                else: break

                            if self.error is None:
                                if   function == '_dictionary_' :
                                    func = bm.fg.rbg(0, 255, 0   )+' in dictionary( ).' + bm.init.reset 
                                    if len(self._values_[ 0 ]) == len( self._values_[ 1 ]):
                                        if  type( self._values_[ 0 ]) == type(list()):
                                            if type( self._values_[ 1 ]) == type( list()):
                                                self._dictionary_ = {}
                                                if len( self._values_[ 0 ] ) == 1 :
                                                    if self._values_[ 0 ][ 0 ] is None:
                                                        if self._values_[ 1 ][ 0 ] is None: pass
                                                        else: self.error = er.ERRORS( self.line ).ERROR5( self.list_of_values[ 0 ], func = func )
                                                    else:
                                                        if type( self._values_[ 0 ][ 0 ] ) == type( str() ):
                                                            self.name = self._values_[ 0 ][ 0 ]
                                                            self._dictionary_[ self.name ] = self._values_[ 1 ][ 0 ]
                                                        else: self.error = er.ERRORS( self.line ).ERROR5( self.list_of_values[ 0 ], func = func )
                                                else:
                                                    for i, name in enumerate( self._values_[ 0 ] ):
                                                        if type( name ) == type( str() ):
                                                            self._dictionary_[ name ] = self._values_[ 1 ][ i ]
                                                        else:
                                                            self.error = er.ERRORS( self.line ).ERROR5( name, func = func )
                                                            break

                                                if self.error is None:
                                                    self.final_value = self._dictionary_
                                                else: self.error = self.error
                                            else: self.error = er.ERRORS(self.line).ERROR5('values', 'a list', func = func)
                                        else: self.error = er.ERRORS(self.line).ERROR5('keys', 'a list', func = func)
                                    else: self.error = er.ERRORS(self.line).ERROR6('keys', 'values', func = func)
                                elif function == '__rand__'     :
                                    self.__type__       = self._values_[ 1 ]
                                    self.__value__      = self._values_[ 0 ]
                                    if   self.__type__ == 'unif':
                                        self.final_value = random.uniform( self.__value__[ 0 ], self.__value__[ 1 ] )
                                    elif self.__type__ == 'int':
                                        self.final_value = random.randint( self.__value__[ 0 ], self.__value__[ 1 ] )
                                    elif self.__type__ == 'norm':
                                        self.final_value = random.random()
                                elif function == '__maths__'    :
                                    try:
                                        if      self._values_[ 0 ] == 'sin'     : self.final_value = math.sin( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'cos'     : self.final_value = math.cos( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'tan'     : self.final_value = math.tan( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'asin'    : self.final_value = math.asin( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'acos'    : self.final_value = math.acos( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'atan'    : self.final_value = math.atan( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'sinh'    : self.final_value = math.sinh( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'cosh'    : self.final_value = math.cosh( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'tanh'    : self.final_value = math.tanh( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'deg'     : self.final_value = math.degrees( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'rad'     : self.final_value = math.radians( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'asinh'   : self.final_value = math.asinh( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'acosh'   : self.final_value = math.acosh( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'atanh'   : self.final_value = math.atanh( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'gamma'   : self.final_value = math.gamma( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'exp'     : self.final_value = math.exp( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'log'     : self.final_value = math.log( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'log2'    : self.final_value = math.log2( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'log10'   : self.final_value = math.log10( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'sqrt'    : self.final_value = math.sqrt( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'erf'     : self.final_value = math.erf( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'erfc'    : self.final_value = math.erfc( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'facto'   : self.final_value = math.factorial( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'floor'   : self.final_value = math.floor( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'ceil'    : self.final_value = math.ceil( self._values_[ 1 ] )
                                        elif    self._values_[ 0 ] == 'round'   : self.final_value = round( self._values_[ 1 ][ 0 ], self._values_[ 1 ][ 1 ])
                                    except TypeError: pass
                                    except ZeroDivisionError: self.error = er.ERRORS( self.line ).ERROR4( self.normal_string )
                                    except ValueError: pass
                                else: self.error = er.ERRORS( self.line ).ERROR4( self.normal_string )
                            else: pass
                        else:self.error = er.ERRORS( self.line ).ERROR4( self.normal_string )
                    else: pass
                else: self.error = er.ERRORS( self.line ).ERROR0( self.normal_string )
            else: self.error = er.ERRORS( self.line ).ERROR1( self.normal_string, self.master )
        else: self.error = er.ERRORS( self.line ).ERROR0( self.normal_string )

        return self.final_value, self.error



  



