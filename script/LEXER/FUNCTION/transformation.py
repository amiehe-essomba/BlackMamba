import                              random
import                              math
import                              sys
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
from CythonModules.Linux            import dictionary as dic 
from CythonModules.Linux            import Trigo 
from CythonModules.Linux            import Open 
from CythonModules.Linux            import making_stat as ms
from CythonModules.Linux            import fileError as fe 
from CythonModules.Linux            import bm_statistics as bms
from CythonModules.Linux            import help
from CythonModules.Linux            import Tuple
from CythonModules.Linux            import arithmetic_analyze as aa
from CythonModules.Linux            import array_to_list as atl  
from CythonModules.Linux            import frame
from CythonModules.Linux            import progress_bar
from CythonModules.Linux            import Trees
from IDE.EDITOR                     import scan
from IDE.EDITOR                     import test 
from IDE.EDITOR                     import true_cursor_pos as cursor_pos
from src.transform                  import datatype as dt

def color_ansi( master, func, line):
    err = None
    list_ = ['r', 'g', 'b']
    for i, j in enumerate(master):
        if 0 <= j <= 256: pass 
        else: 
            err = er.ERRORS( line ).ERROR40( func, list_[i] )
            break 
    return err

class C_F_I_S:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.selection          = particular_str_selection
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_par            = numeric_lexer

    def FUNCTION(self, function = '_int_', term : str = 'orion'):
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
                        if   len( self.list_of_values ) == 1:
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
                                            elif self._value_[ -1 ] in [ 'DataFrame' ]:
                                                func = bm.fg.rbg(0, 255, 0   )+f' in {self._value_[ 1 ]}( ).' +bm.fg.rbg(255,255,255)+\
                                                            ' / '+bm.fg.rbg(255, 255, 0)+"class " +bm.fg.rbg(0, 0, 255) +"data"+ bm.init.reset 
                                                if   self._value_[ 1 ] == "frame":
                                                    self.final_value, s, ss, self.error  = frame.FRAME(self._value_[0], self.line).FRAME(True)
                                                elif self._value_[ 1 ] == "set_id":
                                                    self.final_value, s, ss, self.error  = frame.FRAME(self._value_[0], self.line).FRAME(True)
                                                    if self.error is None:
                                                        self.id_ = self._value_[2]
                                                        self.keys_ = list(self.final_value.keys())
                                                        if self.id_< len(self.keys_):
                                                            self.final_value.set_index(self.keys_[self.id_], inplace=True)    
                                                        else: self.error = er.ERRORS( self.line ).ERROR45( func=func )
                                                    else: pass
                                                elif self._value_[ 1 ] == "select":
                                                    self.final_value, s, ss, self.error  = frame.FRAME(self._value_[0], self.line).FRAME(True)
                                                    if self.error is None:
                                                        self.id_    = self._value_[2]
                                                        self.keys_  = list(self.final_value.keys())
                                                        try: 
                                                            self.name = self.keys_[ self.id_]
                                                            self.final_value = self._value_[0][ self.name ]
                                                        except IndexError : self.error = er.ERRORS( self.line ).ERROR45( func=func )
                                                    else:pass
                                                elif self._value_[ 1 ] == "show":
                                                    show, s, ss, self.error  = frame.FRAME(self._value_[0], self.line).FRAME(True)
                                                    if self.error is None:
                                                        show_id = self._value_[2]
                                                        show, s, ss, self.error  = frame.FRAME({"s":show, 'id':list(show.index)}, self.line).FRAME(False, 'DataFrame', show_id)
                                                        if self.error is None: 
                                                            b = bm.fg.blue_L
                                                            o = bm.fg.rbg(252, 127, 0 )
                                                            w = bm.fg.white_L
                                                            r = bm.init.reset
                                                            self.s1    = bm.init.bold+'{}[{} result{} ]{} : {}'.format(b, o, b,  w, r )
                                                            sys.stdout.write( self.s1+"\n\n"+s+'\n')
                                                            #print(s)
                                                        else: pass 
                                                    else: pass
                                                    
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
                                                        if   self._value_[4] == 'sorted': self.final_value = np.sort( self.final_value )
                                                        elif self._value_[4] == 'dtype': self.final_value = dt.data( str(np.array( self.final_value.dtype  ) ) ).type()
                                                        elif self._value_[4] == 'size': self.final_value = np.array( self.final_value ).size
                                                        else: self.final_value, self.error = mstat.R(self.final_value, self._value_, self.line).R()
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
                                            func = bm.fg.rbg(0, 255, 0   )+' in sget( ).' + bm.init.reset
                                            s1, s2, s3 =  self._value_[0],  self._value_[1],  self._value_[2]
                                
                                            self.final_value = f"{bm.init.bold}{input( s1 )}" 
                                            self.final_value = bm.remove_ansi_chars().chars( self.final_value )
                                            if s2 is None:
                                                if s3 is False: pass 
                                                else: 
                                                    if len(self.final_value) == 1: pass 
                                                    else: self.error = er.ERRORS( self.line ).ERROR39( func=func)
                                            else: 
                                                if s3 is False: self.final_value = self.final_value.split(s2)
                                                else:
                                                    if len(self.final_value) == 1: pass 
                                                    else: self.error = er.ERRORS( self.line ).ERROR39( func=func)
                                        elif function in [ '__open__'  ]    :
                                            self._open_  = self._value_[ 'open']
                                            self._open_, self.error = oc.OPEN_CHECK( self._open_, self.data_base, self.line ).CHECK()
                                            
                                            if self.error is None:
                                                self.final_value, self.error = Open.Open(self.data_base, self.line).Open(self._open_)
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
                                    self.final_value, self.error = dic.dic(self.line).dic( dict(s=self._values_), self.list_of_values)
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
                                    self.final_value, self.error = Trigo.Maths( self.line).Maths( self._values_)
                                elif function == '__scan__'     :
                                    func = bm.fg.rbg(0, 255, 0   )+f' in {self._values_[ 0 ]}( ).' + bm.init.reset 
                                    if   self._values_[ 0 ] == "ascii":
                                        try:
                                            self.final_value = ord(self._values_[1])
                                        except TypeError: self.error = er.ERRORS( self.line ).ERROR41( func )
                                    elif self._values_[ 0 ] == "ansi":
                                        try: self.final_value = ""+chr(self._values_[1])
                                        except ValueError: self.error = er.ERRORS( self.line ).ERROR42( func )
                                        except OverflowError: self.error = er.ERRORS( self.line ).ERROR43( func )
                                    elif self._values_[ 0 ] == "fg":
                                        self.error = color_ansi(self._values_[ 1 ], func, self.line)
                                        if self.error is None:
                                            self.final_value = bm.fg.rbg(self._values_[ 1 ][0], self._values_[ 1 ][1], self._values_[ 1 ][2])
                                        else: pass
                                    elif self._values_[ 0 ] == "bg":
                                        self.error = color_ansi(self._values_[ 1 ], func, self.line)
                                        if self.error is None:
                                            self.final_value = bm.bg.rgb(self._values_[ 1 ][0], self._values_[ 1 ][1], self._values_[ 1 ][2])
                                        else: pass
                                    elif self._values_[ 0 ] == "reset"           : self.final_value = ""+bm.init.reset
                                    elif self._values_[ 0 ] == "bold"            : self.final_value = ""+bm.init.bold
                                    elif self._values_[ 0 ] == "blink"           : self.final_value = ""+bm.init.blink
                                    elif self._values_[ 0 ] == "underline"       : self.final_value = ""+bm.init.underline
                                    elif self._values_[ 0 ] == "italic"          : self.final_value = ""+bm.init.italic
                                    elif self._values_[ 0 ] == "reverse"         : self.final_value = ""+bm.init.reverse
                                    elif self._values_[ 0 ] == "hide"            : self.final_value = ""+bm.init.hide
                                    elif self._values_[ 0 ] == "rapid_blink"     : self.final_value = ""+bm.init.rapid_blink
                                    elif self._values_[ 0 ] == "double_underline": self.final_value = ""+bm.init.double_underline
                                    elif self._values_[ 0 ] == "position"        : self.final_value = cursor_pos.cursor()    
                                    elif self._values_[ 0 ] == "up"              : self.final_value = ""; sys.stdout.write(bm.move_cursor.UP(pos=self._values_[1]) )
                                    elif self._values_[ 0 ] == "down"            : self.final_value = ""; sys.stdout.write(bm.move_cursor.DOWN(pos=self._values_[1]) )
                                    elif self._values_[ 0 ] == "left"            : self.final_value = ""; sys.stdout.write(bm.move_cursor.LEFT(pos=self._values_[1]) ) 
                                    elif self._values_[ 0 ] == "right"           : self.final_value = ""; sys.stdout.write(bm.move_cursor.RIGHT(pos=self._values_[1]) ) 
                                    elif self._values_[ 0 ] == "save"            : self.final_value = ""; sys.stdout.write(bm.save.save)  
                                    elif self._values_[ 0 ] == "restore"         : self.final_value = ""; sys.stdout.write(bm.save.restore)
                                    elif self._values_[ 0 ] == "move_to"         : self.final_value = ""; sys.stdout.write(bm.cursorPos().to(self._values_[1][0], self._values_[1][1])) #cursorPos
                                    elif self._values_[ 0 ] == "dim"             : self.final_value = test.get_linux_ter()
                                    elif self._values_[ 0 ] == "progress_bar"    : progress_bar.progress(self._values_[1][0], self._values_[1][1]).bar(self._values_[1][2])
                                    elif self._values_[ 0 ] == "Trees"           : 
                                        b = bm.fg.blue_L
                                        o = bm.fg.rbg(252, 127, 0 )
                                        w = bm.fg.white_L
                                        r = bm.init.reset
                                        self.s1    = bm.init.bold+'{}[{} result{} ]{} : {}'.format(b, o, b,  w, r )
                                        self.s = Trees.Trees( self._values_[1][0]).Trees(self._values_[1][1]) 
                                        sys.stdout.write( self.s1+"\n\n"+self.s+'\n')
                                    elif self._values_[ 0 ] == "unicode"         : 
                                        self.seg = self._values_[ 1 ].split("[")
                                        if len(self.seg) > 1:
                                            if self.seg[0] in ['\\u001b']:
                                                self.sub_s = u"\u001b["
                                                for n, s in enumerate(self.seg[1:]):
                                                    if n != len(self.seg[1:])-1: self.sub_s += s + "["
                                                    else:self.sub_s += s
                                                self.final_value = self.sub_s
                                            else: self.error = er.ERRORS( self.line ).ERROR4( self.normal_string )
                                        else: self.error = er.ERRORS( self.line ).ERROR4( self.normal_string )
                                else: self.error = er.ERRORS( self.line ).ERROR4( self.normal_string )
                            else: pass                   
                        elif len(self.list_of_values )  == 5:
                            self._values_ = []
                            for value in self.list_of_values:
                                self.value = value
                                self._value_, self.error = self.lex_par.NUMERCAL_LEXER(self.value,
                                                                    self.data_base, self.line).LEXER(  self.value )
                                if self.error is None: self._values_.append( self._value_ )
                                else: break
                            if self.error is None:
                                if function == '__scan__'    :
                                    func = bm.fg.rbg(0, 255, 0   )+' in scan( ).' + bm.init.reset 
    
                                    if self._values_[1] in ['orion', 'pegasus']: 
                                        _colors_ = ['white', 'blue', 'black', 'red', 'cyan', 'magenta', 'orange', 'green', 'yellow']
                                        if self._values_[2] in _colors_:
                                            blink = self._values_[3]
                                            hide  = self._values_[4]
                                            c =  scan.colors(cc=self._values_[2], blink=blink).color()
                                            self.final_value, self.error = scan.scan(self.data_base, 
                                                self.line).STR(key=self._values_[0], terminal_name=self._values_[1], c=c, blink=blink, hide=hide)
                                        else: self.error = er.ERRORS( self.line ).ERROR38( func, _colors_ )
                                    else: self.error = er.ERRORS( self.line ).ERROR37(func )
                                else: self.error = er.ERRORS( self.line ).ERROR4( self.normal_string )
                            else: pass
                        else:self.error = er.ERRORS( self.line ).ERROR4( self.normal_string )
                    else: pass
                else: self.error = er.ERRORS( self.line ).ERROR0( self.normal_string )
            else: self.error = er.ERRORS( self.line ).ERROR1( self.normal_string, self.master )
        else: self.error = er.ERRORS( self.line ).ERROR0( self.normal_string )

        return self.final_value, self.error



  



