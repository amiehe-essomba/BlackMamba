import                              random
import                              math
import                              os
import                              numpy as np
from                                tkinter     import *
from os                             import listdir
from os.path                        import isfile
from statistics                     import variance, stdev, pvariance, pstdev
from script                         import control_string
from script.LEXER                   import particular_str_selection
from script.PARXER.LEXER_CONFIGURE  import numeric_lexer
from script.MATHS                   import arithmetic_object as arr
from script.PARXER                  import numerical_value
from script.DATA_BASE               import ansi
from random                         import randint
from script.STDIN.LinuxSTDIN        import bm_configure as bm
try:
    from CythonModules.Linux        import making_stat as ms
    from CythonModules.Linux        import fileError as fe 
except ImportError:
    from CythonModules.Windows      import making_stat as ms
    from CythonModules.Windows      import fileError as fe 
    from CythonModules.Windows      import bm_statistics as bms
try: from CythonModules.Linux       import help
except : from CythonModules.Windows import help
try: from CythonModules.Linux       import Tuple
except : from CythonModules.Windows import Tuple
try: from CythonModules.Windows     import arithmetic_analyze as aa
except: from CythonModules.Linux    import arithmetic_analyze as aa
try: from CythonModules.Windows     import array_to_list as atl
except: from CythonModules.Linux    import array_to_list as atl


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
                                                self.error = ERRORS( self.line ).ERROR2( self.value, func=func )
                                        elif function in [ '_float_'   ]    :
                                            try:
                                                self.final_value = float(  self._value_ )
                                            except (ValueError, TypeError):
                                                func = bm.fg.rbg(0, 255, 0   )+' in float( ).' + bm.init.reset 
                                                self.error = ERRORS( self.line ).ERROR2( self.value, 'a float', func )
                                        elif function in [ '_complex_' ]    :
                                            try:
                                                self.final_value = complex( self._value_ )
                                            except (ValueError, TypeError):
                                                func = bm.fg.rbg(0, 255, 0   )+' in complex( ).' + bm.init.reset 
                                                self.error = ERRORS( self.line ).ERROR2( self.value, 'a complex', func )
                                        elif function in [ '_string_'  ]    :
                                            try:
                                                if self._value_:
                                                    self.final_value = str( self._value_ )
                                                else:
                                                    self.final_value = '""'
                                            except (ValueError, TypeError):
                                                func = bm.fg.rbg(0, 255, 0   )+' in string( ).' + bm.init.reset 
                                                self.error = ERRORS( self.line ).ERROR2( self.value, 'a string',func=func )
                                        elif function in [ '_boolean_' ]    :
                                            try:
                                                self.final_value = bool( self._value_ )
                                            except (ValueError, TypeError):
                                                func = bm.fg.rbg(0, 255, 0   )+' in boolean( ).' + bm.init.reset 
                                                self.error = ERRORS( self.line ).ERROR2( self.value, 'a boolean', func )
                                        elif function in [ '_list_'    ]    :
                                            func = bm.fg.rbg(0, 255, 0   )+' in list( ).' + bm.init.reset 
                                            try:
                                                if type(self._value_) == self.type[-1]:
                                                    self.final_value = atl.ndarray(list(self._value_), self.line).List()
                                                else:  self.final_value = list( self._value_ )
                                            except (ValueError, TypeError):
                                                self.error = ERRORS( self.line ).ERROR2( self.value, 'a list', func )
                                        elif function in [ '_tuple_'   ]    :
                                            self.final_value, self.error = Tuple.Tuple( self.line ).Tuple(Obj = self._value_, String=self.value )                                       
                                        elif function in [ '_sqrt_'    ]    :
                                            func = bm.fg.rbg(0, 255, 0   )+' in sqrt( ).' + bm.init.reset 
                                            if type( self._value_ ) in [type(float()), type(int()), type(bool())]:
                                                if self._value_ >= 0:
                                                    self.final_value = self._value_ ** (0.5)
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR7( self.value, func )
                                            else:
                                                self.error = ERRORS( self.line ).ERROR8( self.value, func )
                                        elif function in [ '_length_'  ]    :
                                            if type( self._value_ ) in [type(list()), type(tuple()), type( range(1))]:
                                                self.final_value = len( self._value_ )
                                            elif type( self._value_ ) == type( str() ):
                                                self.final_value = len( self._value_ )
                                            else:
                                                func = bm.fg.rbg(0, 255, 0   )+' in length( ).' + bm.init.reset 
                                                self.error = ERRORS( self.line ).ERROR9( self.value, func=func )
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
                                                            self.error = ERRORS(self.line).ERROR10(self.sum,
                                                                                        self._value_[ 0 ], func = func )
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR11( self.value, func=func )
                                            else:
                                                self.error = ERRORS( self.line ).ERROR13( self.value, func=func )
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
                                                self.error = ERRORS( self.line ).ERROR13( self.value, func=func )                                     
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
                                                    self.error = ERRORS( self.line ).ERROR11( self.value, func=func )
                                            else:
                                                self.error = ERRORS( self.line ).ERROR13( self.value, func=func ) 
                                        elif function in [ '_std_'     ]    :
                                            if self._value_[ -1 ] in ['cov', 'cor', 'linearR']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).COV_CORR_LINEAR() 
                                            elif self._value_[ -1 ] in ['quantiles', 'quantile']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).QUANTILE() 
                                            elif self._value_[ -1 ] in ['mode', 'mul_mode']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).MOD_MULMOD() 
                                            elif self._value_[ -1 ] in ['med', 'medl', 'medg', 'medh']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).MED_MEDH_MEDL_MEDG() 
                                            elif self._value_[ -1 ] in ['iquantile']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).IQUANTILE()
                                            elif self._value_[ -1 ] in ['kurtosis']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).KURTOSIS()
                                            elif self._value_[ -1 ] in ['skewness']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).SKEWNESS()
                                            elif self._value_[ -1 ] in ['mad']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).MAD()
                                            elif self._value_[ -1 ] in ['lower_fence', 'upper_fence']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).LOWER_UPPER_FENCE()
                                            elif self._value_[ -1 ] in ['rms']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).RMS()
                                            elif self._value_[ -1 ] in ['rsd']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).RSD()
                                            elif self._value_[ -1 ] in ['std_error']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).STD_ERRPR()
                                            elif self._value_[ -1 ] in ['midrange']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).MIDRANGE()
                                            elif self._value_[ -1 ] in ['sum_square']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).SUM_SQUARE()
                                            elif self._value_[ -1 ] in ['grouped']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).GROUPED()
                                            elif self._value_[ -1 ] in ['Q1', 'Q3']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).Q1_Q3()
                                            elif self._value_[ -1 ] in ['facto']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).FACTORIAL()
                                            elif self._value_[ -1 ] in ['harmonic_mean']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).H_MEAN()
                                            elif self._value_[ -1 ] in ['geometric_mean']:
                                                self.final_value, self.error = STAT( self._value_, self.value, self.line ).G_MEAN()
                                            elif self._value_[ -1 ] in [ 'License' ]:
                                                bm.open_graven().open_graven_web()
                                            elif self._value_[ -1 ] in [ 'help' ]:
                                                help.HELP(self._value_[ 0 ]).HELP()
                                            elif self._value_[ -1 ] in [ 'matrix' ]:
                                                self.typ = [type(list()), type(tuple()), type(range(1))]
                                                if type(self._value_[0]) == type(list()): pass
                                                else: self._value_[0] = list(self._value_[0])

                                                self.final_value, self.error = MATRIX(self._value_[0], self._value_[1],self._value_[2],
                                                                          self._value_[3], self.line).MATRIX(self._value_[5], ctype=self._value_[4])

                                                if self.error is None:
                                                    self.func = bm.fg.rbg(0, 255, 0) + ' in {}( ).'.format( self._value_[4] ) + bm.init.reset
                                                    if self._value_[4] is None:  self.final_value = np.array( self.final_value )
                                                    else:
                                                        if self._value_[4] == 'sorted':
                                                            self.final_value = np.sort( self.final_value )
                                                        else:
                                                            self.final_value, self.error = R(self.final_value, self._value_, self.line).R()
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
                                                    else: self.error = ERRORS( self.line ).ERROR11( self.value, func=func )
                                                else: self.error = ERRORS( self.line ).ERROR13( self.value, func=func )                    
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
                                                    self.error = ERRORS( self.line ).ERROR11( self.value, func=func )
                                            else:
                                                self.error = ERRORS( self.line ).ERROR13( self.value, func=func )                
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
                                                    else:  self.error = ERRORS(self.line).ERROR11(self.value, func = func )
                                                else: self.error = ERRORS( self.line ).ERROR11( self.value, func=func )
                                            else:  self.error = ERRORS( self.line ).ERROR13( self.value, func=func )
                                        elif function in [ '_rang_'    ]    :
                                            if len( self._value_ ) == 3:
                                                self.start, self.end, self.step = self._value_
                                                if self.start < self.end:
                                                    if self.step < self.end:
                                                        self.final_value = range( self.start, self.end, self.step )
                                                    else:
                                                        self.error = ERRORS(self.line).ERROR12('step', 'stoped')
                                                else:
                                                    self.error = ERRORS(self.line).ERROR12('started', 'stoped')
                                            elif len( self._value_ ) == 2:
                                                self.start, self.end = self._value_
                                                if self.start < self.end:
                                                    self.final_value = range( self.start, self.end )
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR12( 'started', 'stoped' )
                                            else:
                                                self.final_value = range(self._value_[ 0 ])
                                        elif function in [ '__ansii__' ]    :
                                            func = bm.fg.rbg(0, 255, 0   )+' in ansi( ).' + bm.init.reset 
                                
                                            if type( self._value_ ) == type( tuple() ):
                                                if len( self._value_ ) == 2:
                                                    self.back_end       = self._value_[ 0 ]
                                                    self.front_end      = self._value_[ 1 ]
                                                    self.final_value, self.error = ansi.output( self.front_end,
                                                                            self.line, self.back_end ).output()
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR15( self.value , func=func )
                                            else:
                                                self.error = ERRORS( self.line ).ERROR14( self.value, 'a tuple()', func=func )
                                        elif function in [ '__show__'  ]    :
                                            self.final_value = u"{}".format(self._value_)
                                        elif function in [ '_get_line_']    :
                                            self.final_value = self.line-1
                                        elif function in [ '__scan__'  ]    :
                                            self.final_value = input( self._value_ )
                                        elif function in [ '__open__'  ]    :
                                            self._open_  = self._value_[ 'open']
                                            self._open_, self.error = OPEN_CHECK( self._open_, self.data_base, self.line ).CHECK()
                                            
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
                                                        self.error = ERRORS( self.line ).ERROR18( self._open_[ 0 ] )
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
                                    else: self.error = ERRORS( self.line ).ERROR3( self.value )
                                else: self.error = self.error
                            else: self.error = ERRORS( self.line ).ERROR0( self.normal_string )
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
                                                        else: self.error = ERRORS( self.line ).ERROR5( self.list_of_values[ 0 ], func = func )
                                                    else:
                                                        if type( self._values_[ 0 ][ 0 ] ) == type( str() ):
                                                            self.name = self._values_[ 0 ][ 0 ]
                                                            self._dictionary_[ self.name ] = self._values_[ 1 ][ 0 ]
                                                        else: self.error = ERRORS( self.line ).ERROR5( self.list_of_values[ 0 ], func = func )
                                                else:
                                                    for i, name in enumerate( self._values_[ 0 ] ):
                                                        if type( name ) == type( str() ):
                                                            self._dictionary_[ name ] = self._values_[ 1 ][ i ]
                                                        else:
                                                            self.error = ERRORS( self.line ).ERROR5( name, func = func )
                                                            break

                                                if self.error is None:
                                                    self.final_value = self._dictionary_
                                                else: self.error = self.error
                                            else: self.error = ERRORS(self.line).ERROR5('values', 'a list', func = func)
                                        else: self.error = ERRORS(self.line).ERROR5('keys', 'a list', func = func)
                                    else: self.error = ERRORS(self.line).ERROR6('keys', 'values', func = func)
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
                                    except ZeroDivisionError: pass
                                    except ValueError: pass
                                else: self.error = ERRORS( self.line ).ERROR4( self.normal_string )
                            else: pass
                        else:self.error = ERRORS( self.line ).ERROR4( self.normal_string )
                    else: self.error = self.error
                else: self.error = ERRORS( self.line ).ERROR0( self.normal_string )
            else: self.error = ERRORS( self.line ).ERROR1( self.normal_string, self.master )
        else: self.error = ERRORS( self.line ).ERROR0( self.normal_string )

        return self.final_value, self.error

class OPEN_CHECK:
    def __init__(self, master: list, DataBase: dict, line: int) :
        self.master         = master 
        self.DataBase       = DataBase
        self.line           = line
        self.control        = control_string.STRING_ANALYSE( self.DataBase, self.line )
        
    def CHECK( self ):
        self.error          = None 
        self.name           = self.master[ 0 ]
        self.file           = self.master[ 1 ]
        self.action         = self.master[ 2 ]
        self.status         = self.master[ 3 ]
        self.encoding       = self.master[ 4 ]
        self.currently_path = os.getcwd()
        self.CurrentFiles   = listdir( self.currently_path)
        
        self.name, self.error = self.control.CHECK_NAME( self.name )
        
        if self.error is None: 
            if self.action in [ 'read', 'write']:
                if   self.action == 'read'      :
                    self.action = 'r'
                elif self.action == 'write'     :
                    self.action = 'w'
                    
                if self.status in [ 'new', 'old']: 
                    
                    if self.encoding is None: pass
                    else: 
                        if self.encoding in [ 'utf-8', 'ascii', 'utf-16', 'latin-1', 'cp1252'] : pass 
                        else: self.error = ERRORS( self.line ).ERROR24()
                    
                    if self.error is None:
                        if "/" in self.file: pass
                        elif "\\" in self.file: 
                            try:
                                self.s = '{}{}'.format('\\','\\')
                                self.path = self.file.split(self.s)
                                if self.path[ -1 ] == '':
                                    if len( self.path ) > 3:
                                        self.name = self.path[ -2 ]
                                        self.string = ''
                                        
                                        for v in self.path[: -2]:
                                            if v != '': self.string += v 
                                            else: self.string += self.s
                                            
                                        self.path = self.string
                                        self.listfir_path = listdir( self.path )
                                        
                                        if self.name in self.self.listfir_path:
                                            if isfile( self.name ): pass 
                                            else: self.error = ERRORS( self.line ).ERROR19( self.name )
                                        else: self.error = ERRORS( self.line ).ERROR21( self.name )
                                    else: self.error = ERRORS( self.line ).ERROR20( self.file )
                                else: self.error = ERRORS( self.line ).ERROR20( self.file )
                            except OSError:
                                self.error = ERRORS( self.line ).ERROR20( self.path )
                            except FileNotFoundError: 
                                self.error = ERRORS( self.line ).ERROR21( self.name )
                        else: 
                            if self.status == 'old':
                                if self.file in self.CurrentFiles :
                                    if isfile( self.file ): pass
                                    else: self.error = ERRORS( self.line ).ERROR19( self.file ) 
                                else: self.error = ERRORS( self.line ).ERROR21( self.file)
                            else: pass
                    else: pass
                else: self.error = ERRORS( self.line ).ERROR22()
            else: self.error = ERRORS( self.line ).ERROR23()
        else: pass
        
        return [ self.name, self.file, self.action, self.status, self.encoding ], self.error 

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
                    else: self.error = ERRORS( self.line ).ERROR6( 'master1', 'master2', func=func ) 
                else: self.error = ERRORS( self.line ).ERROR11( self._value_[ 1 ], func=func ) 
            else: self.error = ERRORS( self.line ).ERROR11( self._value_[ 0 ], func=func ) 
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func ) 
        
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
                    else: self.error = ERRORS( self.line ).ERROR25( 'numeric', func=func )
                else:
                    if 0 < self._value_[ 1 ] <= 1.0: pass 
                    else:
                        if self._value_[ 1 ] < 1.0: self.error = ERRORS( self.line ).ERROR25( 'numeric', func=func ) 
                        else:  self.error = ERRORS( self.line ).ERROR26( 'numeric', func=func ) 
                
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
            else: self.error = ERRORS( self.line ).ERROR11( self._value_[ 0 ], func=func ) 
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
        
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
            else: self.error = ERRORS( self.line ).ERROR11( self._value_[ 0 ], func=func ) 
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
            else: self.error = ERRORS( self.line ).ERROR11( self._value_[ 0 ], func=func ) 
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR13( self._value_[ 0 ], func=func )
        
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
        else: self.error = ERRORS( self.line ).ERROR27(self._value_[ 0 ], func)
                
        return self.final_value, self.error
    
class ERRORS:
    def __init__(self, line: int):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset 

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() + '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error 
        
        return self.error + self.reset 

    def ERROR1(self, string: str, char:str):
        error = '{}<< * >> {}was not defined at beginning of {}<< {} >>. {}line: {}{}'.format(self.green, self.white, 
                                                                                self.cyan, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() + '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error 
        
        return self.error + self.reset 

    def ERROR2(self, string: str, _char_ = 'an integer', func = ''):
        error = '{}to  {}{}() {}type. {}line: {}{}.'.format(self.white, self.red, _char_, self.yellow, self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}impossible to convert {}<< {} >> '.format(self.white, self.cyan, string) + error + func
        
        return self.error + self.reset

    def ERROR3(self, string: str):
        type = '{}a complex(), {}a float(), {}an integer() {}or a string() {}type'.format(self.blue, self.green, self.red, 
                                                                                            self.magenta, self.yellow)
        error = '{}is not {}. {}line: {}{}'.format(self.white, type, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format( self.cyan, string) + error
        
        return self.error+self.reset

    def ERROR4(self, string: str):
        error = '{}line: {}{}'.format( self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        
        return self.error+self.resert

    def ERROR5(self, string: str, _char_ = 'a string', func: str = ''):
        error = '{}is not  {}{}() {}type. {}line: {}{}'.format(self.white, self.yellow, _char_, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format( self.cyan, string) + error + func
        
        return self.error+self.reset 

    def ERROR6(self, string: str, key: str, func : str = ''):
        error = '{}and {}<< {} >> {}have not the same {}length. {}line: {}{}'.format(self.white, self.magenta, key, self.yellow, self.white, self.white, 
                                                                                   self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format( self.cyan, string) + error + func
        
        return self.error+self.reset 

    def ERROR7(self, value: str, func : str = ''):
        error = '{} is negative. {}line: {}{}'.format(self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'DomainError' ).Errors() + '{}<< {} >>'.format(self.cyan, value) + error + func
        
        return self.error+self.reset

    def ERROR8(self, string: str, func: str = ''):
        error = '{}is not  {}a float(), {}a boolean() {}or an integer() {}type. {}line: {}{}'.format(self.white, self.green, self.blue, 
                                                                self.red, self.yellow, self.white, self.yellow, self.line)
      
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error

    def ERROR9(self, string: str, func: str = ''):
        error = '{}is not  {}a list(), {}a tuple(), {}a range() {}or a string() {}type. {}line: {}{}'.format(self.white, self.yellow, self.blue,
                                                         self.green, self.magenta, self.yellow, self.white, self.yellow, self.line)  
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error+self.reset

    def ERROR10(self, type1: any, type2: any, func :str = ''):
        typ11 = numerical_value.FINAL_VALUE( type1, {}, self.line, None ).CONVERSION()
        typ22 = numerical_value.FINAL_VALUE( type2, {}, self.line, None ).CONVERSION()

        typ1, typ2 = ERRORS(self.line).ERROR34(type1, type2)

        self.error = '{}unsupported operand between {}<< {}{} : {} >> {} and {}<< {}{} : {} >>. {}line: {}{}'.format(
                        self.yellow, self.white, typ11, self.white, typ1, self.yellow, self.white, typ22, self.white, typ2,
                        self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ArithmeticError').Errors() + self.error + func

        return self.error+self.reset 

    def ERROR11(self, string: str, func:str = ''):
        error = '{}is {}EMPTY. {}line: {}{}'.format( self.white, self.yellow, self.white, self.yellow, self.line)      
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error+self.reset

    def ERROR12(self, first: str, last: str):
        error = '{}<< {} >> {}is lower than {}<< {} >> . {}line: {}{}'.format(self.red, last, self.white, self.green, first,
                                                                        self.white, self.yellow, self.line) 
        self.error = fe.FileErrors( 'DomainError' ).Errors() + error
        return self.error+self.reset

    def ERROR13(self, string: str, func:str = ''):
        error = '{}is not  {}a list(), {} a range() {}or a tuple() {}type. {}line: {}{}'.format(self.white, self.yellow, self.green,
                                                                    self.blue, self.yellow, self.white, self.yellow, self.line)        
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error+self.reset

    def ERROR14(self, string: str, _type_ = 'string()', c = bm.fg.blue_L, func : str= ''):
        error = '{}is not  {}{} {}type. {}line: {}{}'.format(self.white, c, _type_, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func
        return self.error+self.reset

    def ERROR15(self, string: str, num:int = 2, func :str = ''):
        error = '{}is not lower than {}{}. {}line: {}{}'.format(self.white, self.red, num, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error+self.reset

    def ERROR16(self, string: str, num:int = 2):
        error = '{}is not egal to {}{}. {}line: {}{}'.format(self.white, self.red, num, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}length( {} ) '.format(self.cyan, string) + error + error

        return self.error+self.reset

    def ERROR17(self):
        error = '{}is bigger than {}input[ {}1{} ]. {}line: {}{}'.format(self.white, self.cyna, self.red, self.cyan, 
                                                                         self.white, self.yellow, self.line)        
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}input[ {}0{} ] '.format(self.cyan, self.red, self.cyan) + error

        return self.error+self.reset
    
    def ERROR18(self, name: str):
        error = '{}before {}new opening. {}line: {}{}'.format(self.white, self.cyan, self.white, self.yellow, self.line)        
        self.error = fe.FileErrors( 'FileError' ).Errors() + '{}close {}{} '.format(self.white, self.red, name) + error

        return self.error+self.reset
    
    def ERROR19(self, string: str):
        error = '{}is not a file. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileError' ).Errors() +'{}{} '.format(self.cyan, string) + error
        
        return self.error+self.reset
    
    def ERROR20(self, string: str):
        error = '{}is incorrect. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'OSError' ).Errors() + '{}directory path {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR21(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileNotFoundError' ).Errors() + '{}file {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR22(self):
        error = '{}is not in the list {}[ {}new{}, {}old {}]. {}line: {}{}'.format(self.white, self.red, self.green, self.white, self.magenta, self.red,
                                                                                  self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}status '.format( self.cyan) + error

        return self.error+self.reset
    
    def ERROR23(self):
        error = '{}is not in the list {}[ {}read{}, {}write{} ]. {}line: {}{}'.format(self.white, self.red, self.green, 
                                        self.white, self.magenta, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}action '.format( self.cyan ) + error

        return self.error+self.reset
    
    def ERROR24(self):
        s = '{}[ {}utf-8  {}ascii  {}latin-1  {}cp1252  {}utf-16  {}utf-32{} ]'.format(self.red, self.green, self.magenta,
                                                                           self.yellow, self.red, self.blue, self.cyan, self.red)
        error = '{}Making your choice in {}. {}line: {}{}'.format(self.white, s, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}bad encoding value. '.format( self.cyan ) + error

        return self.error+self.reset
    
    def ERROR25(self, num: any, func :str = ''):
    
        error = '{}cannot be negative or egal to 0. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format(self.cyan, num) + error + func

        return self.error+self.reset
        
    def ERROR26(self, num: any, func :str = ''):
        
        error = '{}cannot be bigger than 1.0. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format(self.cyan, num) + error + func

        return self.error+self.reset
    
    def ERROR27(self, num: any, func :str = ''):
        
        error = '{}cannot be negative. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format(self.cyan, num) + error + func

        return self.error+self.reset

    def ERROR28(self,):
        error = '{}is {}EMPTY. {}line: {}{}'.format(self.white, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}master '.format(self.cyan) + error

        return self.error + self.reset

    def ERROR29(self, string : str = 'nrow'):
        error = '{}should be {}positive {}or {}-1. {}line: {}{}'.format(self.white, self.yellow, self.white, self.red,
                                                                        self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}{} '.format(self.cyan, string) + error

        return self.error + self.reset

    def ERROR30(self, string : str = 'ncol'):
        error = '{}cannot be {}negative {}when {}nrow {}is negative. {}line: {}{}'.format(self.white, self.yellow, self.white, self.cyan,
                                        self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}{} '.format(self.cyan, string) + error

        return self.error + self.reset

    def ERROR31(self, s= '>'):
        error = '{}line: {}{}'.format( self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}nrow * ncol {} length( master ) '.format(self.cyan, s) + error

        return self.error + self.reset

    def ERROR32(self, s= 'nrow'):
        error = '{}and {}reverse is True {}line: {}{}'.format(self.white, self.yellow,  self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}{} {}is {}-1 '.format(self.cyan, s, self.white, self.red) + error

        return self.error + self.reset

    def ERROR33(self, s= 'axis', ss = ''):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}{} {}>= {}{} '.format(self.cyan, s, self.white, self.red, ss) + error

        return self.error + self.reset

    def ERROR34(self, object1 : any, object2: any):

        if type(object1) in [type(list()), type(tuple())]:
            if len(object1) < 4:  result1 = object1
            else:
                if type(object1) in [type(list())]:
                    result1 = f'[{object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]}]'
                else:
                    result1 = f'({object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]})'
        elif type(object1) == type(str()):
            if object1:
                if len(object1) < 6: result1 = object1
                else:  result1 = object1[: 2] + ' ... ' + object1[-2:]
            else:  result1 = object1
        else:  result1 = object1

        if type(object2) in [type(list()), type(tuple())]:
            if len(object2) < 4:  result2 = object2
            else:
                if type(object2) in [type(list())]:
                    result2 = f'[{object2[0]}, {object2[1]}, ....., {object2[-2]}, {object2[-1]}]'
                else:
                    result2 = f'({object2[0]}, {object2[1]}, ....., {object2[-2]}, {object2[-1]})'
        elif type(object2) == type(str()):
            if object2:
                if len(object2) < 6:  result2 = object2
                else:
                    result2 = object2[: 2] + ' ... ' + object2[-2:]
            else:  result2 = object2
        else: result2 = object2

        return result1, result2

class MATRIX:
    def __init__(self, master : list, nrow : int , ncol : int, reverse: bool, line: int):
        self.master     = master
        self.nrow       = nrow
        self.ncol       = ncol
        self.reverse    = reverse
        self.line       = line

    def MATRIX(self, axis: any, ctype: str='sum'):
        self.step       = 0
        self.newList    = []
        self.prev       = []
        self.error      = None
        self.type       = [type(int()), type(float()), type(bool())]

        if self.master:
            if self.nrow > 0:
                if self.ncol > 0:
                    if self.nrow * self.ncol == len( self.master):
                        if self.reverse is False:
                            self.step = self.ncol
                            self.prev.append( 0 )
                            if axis is None:
                                for i in range(self.nrow):
                                    self.prev.append( self.ncol * (i+1) )
                                    self.ms = self.master[self.prev[i]: self.prev[i + 1]]
                                    self.newList.append(self.ms)
                            else:
                                for i in range(self.nrow):
                                    try:
                                        self.prev.append( self.ncol * (i+1) )
                                        self.ms = self.master[ self.prev[ i ]: self.prev[ i+1 ]][axis]
                                        self.newList.append( self.ms )
                                    except IndexError:
                                        self.error = ERRORS( self.line ).ERROR33(ss='ncol')
                                        break
                        else:
                            if axis is None:
                                for i in range(self.nrow):
                                    self.ss     = []
                                    self.w      = 0
                                    for j in range( self.ncol ):
                                        self.w = self.nrow * j + i
                                        self.ss.append(self.master[ self.w ])
                                    self.newList.append( self.ss )
                            else:
                                for i in range(self.nrow):
                                    self.ss     = []
                                    self.w      = 0
                                    for j in range( self.ncol ):
                                        self.w = self.nrow * j + i
                                        self.ss.append(self.master[ self.w ])

                                    try: self.newList.append( self.ss[axis] )
                                    except IndexError :
                                        self.error = ERRORS(self.line).ERROR33(ss='ncol')
                                        break
                    else:
                        if self.nrow * self.ncol > len( self.master) : self.error = ERRORS( self.line ).ERROR31('>')
                        else : self.error = ERRORS( self.line ).ERROR31('<')
                elif self.ncol == -1:
                    if len( self.master ) == self.nrow:
                        if self.reverse is False:
                            if axis is None: self.newList.append( self.master )
                            else:
                                try:  self.newList.append( self.master[axis] )
                                except IndexError: self.error = ERRORS( self.line ).ERROR33(ss='length( master )')
                        else: self.error = ERRORS( self.line ).ERROR32( 'ncol')
                    else:
                        if self.nrow > len( self.master) : self.error = ERRORS( self.line ).ERROR31('>')
                        else : self.error = ERRORS( self.line ).ERROR31('<')
                else: self.error = ERRORS( self.line ).ERROR29( string = 'ncol')
            elif self.nrow == -1:
                if self.ncol > 0:
                    if self.ncol == len( self.master):
                        if self.reverse is False:
                            if axis is None:
                                for s in self.master:
                                    self.newList.append([s])
                            else:
                                try:  self.newList.append([self.master[axis]])
                                except IndexError: self.error = ERRORS( self.line ).ERROR33(ss='length( master )')
                        else: self.error = ERRORS( self.line ).ERROR32( 'nrow')
                    else:
                        if self.ncol > len( self.master) : self.error = ERRORS( self.line ).ERROR31('>')
                        else : self.error = ERRORS( self.line ).ERROR31('<')
                else: self.error = ERRORS( self.line ).ERROR29( string = 'nrow')
            else: self.error = ERRORS( self.line ).ERROR30( string = 'nrow')
        else: self.error = ERRORS( self.line ).ERROR28()

        return  self.newList, self.error

class R:
    def __init__(self, master : list, _value_ : list, line : int):
        self.master     = master
        self.line       = line
        self._value_    = _value_
    def R(self):
        self.error      = None
        self.type       = [type(list()), type(tuple()), type(range(1))]
        self.func       = bm.fg.rbg(0, 255, 0) + ' in {}( ).'.format(self._value_[4]) + bm.init.reset
        self.master_inv = None
        self.master_v   = []

        if   self._value_[4] == 'sum':
            if self._value_[5] is None:
                for x, _value_ in enumerate(self.master):
                    if type(_value_) in self.type:
                        self._, self.error = ms.GetValue(list(_value_), self.line).sum()
                        if not self.error:
                            self.error = None
                            self.master[x] = self._
                        else:  break
                    else:
                        self.error = ERRORS(self.line).ERROR13(_value_, self.func)
                        break
                if self.error is None:  self.master = np.array(self.master)
                else:  pass
            else:  self.master, self.error = ms.GetValue(self.master, self.line).sum()
        elif self._value_[4] in ['ndim']:
            self.master = list(np.array(self.master).shape)
        elif self._value_[4] in ['std', 'var']:
            if self._value_[5] is None:
                for x, _value_ in enumerate(self.master):
                    if type(_value_) in self.type:
                        self._, self.error = ms.GetValue(list(_value_), self.line).var_std(
                            self._value_[4], _type_='sam', ob_type='list')
                        if not self.error:
                            self.error = None
                            self.master[x] = self._
                        else:  break
                    else:
                        self.error = ERRORS(self.line).ERROR13(_value_, self.func)
                        break
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self.master, self.error = ms.GetValue(self.master, self.line).var_std(
                    self._value_[4], _type_='sam', ob_type='list')
        elif self._value_[4] in ['pstd', 'pvar']:
            if self._value_[5] is None:
                for x, _value_ in enumerate(self.master):
                    if type(_value_) in self.type:
                        self._, self.error = ms.GetValue(list(_value_), self.line).var_std(
                            self._value_[4], _type_='pop', ob_type='list')
                        if not self.error:
                            self.error = None
                            self.master[x] = self._
                        else:  break
                    else:
                        self.error = ERRORS(self.line).ERROR13(_value_, self.func)
                        break
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self.master, self.error = ms.GetValue(self.master, self.line).var_std(
                    self._value_[4], _type_='pop', ob_type='list')
        elif self._value_[4] == 'mean':
            if self._value_[5] is None:
                for x, _value_ in enumerate(self.master):
                    if type(_value_) in self.type:
                        self._, self.error = ms.GetValue(list(_value_), self.line).mean(len(_value_))
                        if not self.error:
                            self.error = None
                            self.master[x] = self._
                        else:  break
                    else:
                        self.error = ERRORS(self.line).ERROR13(_value_, self.func)
                        break
                if self.error is None:  self.master = np.array(self.master)
                else:  pass
            else:  self.master, self.error = ms.GetValue(self.master, self.line).mean(len(self.master))
        elif self._value_[4] in ['min', 'max']:
            if self._value_[5] is None:
                for x, _value_ in enumerate(self.master):
                    if type(_value_) in self.type:
                        self._, self.error = ms.GetValue(list(_value_), self.line).min_max(self._value_[4])
                        if not self.error:
                            self.error = None
                            self.master[x] = self._
                        else:  break
                    else:
                        self.error = ERRORS(self.line).ERROR13(_value_, self.func)
                        break
                if self.error is None:  self.master = np.array(self.master)
                else:  pass
            else:  self.master, self.error = ms.GetValue(self.master, self.line).min_max(self._value_[4])
        elif self._value_[4] in ['cov', 'cor', 'linearR']:
            if self._value_[3] is True: self._value_[3] = False
            else: self._value_[3] = True

            self.ss = []
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self.master_inv, self.error = MATRIX(self._value_[0], self._value_[1], self._value_[2],
                                        self._value_[3], self.line).MATRIX(x, ctype=self._value_[4])
                    self.master_v   = []
                    for y in range(len(self.master_inv)):
                        self._val_ = [self.master_inv, self.master[y], self._value_[4], "pop", self._value_[4]]
                        self.s, self.error = STAT(self._val_, '', self.line).COV_CORR_LINEAR()
                        if self.error is None: self.master_v.append(self.s)
                        else: break
                    if self.error is None: self.ss.append(self.master_v)
                    else: break
                if self.error is None: self.master = np.array(self.ss)
                else: pass
            else:
                self._value_ = [self.master, self.master_inv, self._value_[4], "pop", self._value_[4]]
                self.master, self.error = STAT(self._value_, '', self.line).COV_CORR_LINEAR()
        elif self._value_[4] in ['quantile']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], self._value_[6], self._value_[4]]
                    self.s, self.error = STAT( self._val_, "", self.line ).QUANTILE()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, self._value_[6], self._value_[4]]  
                self.master, self.error = STAT( self._val_, "", self.line ).QUANTILE()        
        elif self._value_[4] in ['iquantile']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], 'pop', self._value_[4]]
                    self.s, self.error = STAT( self._val_, "", self.line ).IQUANTILE()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, "pop", self._value_[4]]  
                self.master, self.error = STAT( self._val_, "", self.line ).IQUANTILE()
        elif self._value_[4] in ['kurtosis']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], 'pop', self._value_[4]]
                    self.s, self.error = STAT( self._val_, "", self.line ).KURTOSIS()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, "pop", self._value_[4]]  
                self.master, self.error = STAT( self._val_, "", self.line ).KURTOSIS()
        elif self._value_[4] in ['sum_square']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], self._value_[4]]
                    self.s, self.error = STAT( self._val_, "", self.line ).SUM_SQUARE()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, self._value_[4]]  
                self.master, self.error = STAT( self._val_, "", self.line ).SUM_SQUARE()      
        elif self._value_[4] in ['grouped']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], self._value_[4]]
                    self.s, self.error = STAT( self._val_, "", self.line ).GROUPED()
    
                    if self.error is None: self.master[x] =self.s
                    else: break
                    
                if self.error is None: pass # self.master = np.array(self.master, dtype=object)
                else: pass
            else:
                self._val_ = [self.master, self._value_[4]]  
                self.master, self.error = STAT( self._val_, "", self.line ).GROUPED()
        elif self._value_[4] in ['Q1', 'Q3']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], self._value_[4], self._value_[4]]
                    self.s, self.error = STAT( self._val_, "", self.line ).Q1_Q3()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, self._value_[4], self._value_[4]]  
                self.master, self.error = STAT( self._val_, "", self.line ).Q1_Q3()         
        elif self._value_[4] in ['round']:
            if self._value_[5] is None:
                
                for x in range(len(self.master)):
                    if self.master[x]:
                        for y in range(len(self.master[x])):
                            if type(self.master[x][y]) in [type(float())]:
                                self.master[x][y] = round(self.master[x][y], self._value_[6])
                            else: pass
                    else: break
                
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:  
                for x in range(len(self.master)):
                    if type(self.master[x]) in [type(float())]:
                        self.master[x] = round(self.master[x],self._value_[6]) 
                    else: pass
                
                self.master = np.array(self.master)
                             
        return self.master, self.error