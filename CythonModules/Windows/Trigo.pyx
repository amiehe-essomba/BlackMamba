import                              math
from src.transform                  import error as er

cdef class Maths:
    cdef public:
        unsigned long long int line 
    cdef:
        dict error 
        dict final_value

    def __cinit__(self, line ):
        self.line           = line  
        self.error          = {"s":None}
        self.final_value    = {"s":None}

    cpdef Maths (self, list keys):
        return Maths( self.line ).Trigo( keys )
    cdef Trigo(self, list keys):
        try:
            if      keys[0] == 'sin'     : self.final_value['s'] = math.sin( keys[1] )
            elif    keys[0] == 'cos'     : self.final_value['s'] = math.cos( keys[1])
            elif    keys[0] == 'tan'     : self.final_value['s'] = math.tan( keys[1] )
            elif    keys[0] == 'asin'    : self.final_value['s'] = math.asin( keys[1] )
            elif    keys[0] == 'acos'    : self.final_value['s'] = math.acos( keys[1] )
            elif    keys[0] == 'atan'    : self.final_value['s'] = math.atan( keys[1] )
            elif    keys[0] == 'sinh'    : self.final_value['s'] = math.sinh( keys[1] )
            elif    keys[0] == 'cosh'    : self.final_value['s'] = math.cosh( keys[1] )
            elif    keys[0] == 'tanh'    : self.final_value['s'] = math.tanh( keys[1] )
            elif    keys[0] == 'deg'     : self.final_value['s'] = math.degrees( keys[1] )
            elif    keys[0] == 'rad'     : self.final_value['s'] = math.radians( keys[1] )
            elif    keys[0] == 'asinh'   : self.final_value['s'] = math.asinh( keys[1] )
            elif    keys[0] == 'acosh'   : self.final_value['s'] = math.acosh( keys[1] )
            elif    keys[0] == 'atanh'   : self.final_value['s'] = math.atanh( keys[1] )
            elif    keys[0] == 'gamma'   : self.final_value['s'] = math.gamma( keys[1] )
            elif    keys[0] == 'exp'     : self.final_value['s'] = math.exp( keys[1] )
            elif    keys[0] == 'log'     : 
                try: self.final_value['s'] = math.log( keys[1] )
                except (ValueError, TypeError): pass
            elif    keys[0] == 'log1'    : 
                try: self.final_value['s'] = math.log1( keys[1])
                except (ValueError, TypeError): pass
            elif    keys[0] == 'log2'    : 
                try: self.final_value['s'] = math.log2( keys[1])
                except (ValueError, TypeError) : pass
            elif    keys[0] == 'log10'   : 
                try:  self.final_value['s'] = math.log10( keys[1] )
                except (ValueError, TypeError): pass
            elif    keys[0] == 'sqrt'    :
                try: self.final_value['s'] = math.sqrt( keys[1] )
                except (ValueError, TypeError) : pass
            elif    keys[0] == 'erf'     : self.final_value['s'] = math.erf( keys[1])
            elif    keys[0] == 'erfc'    : self.final_value['s'] = math.erfc( keys[1] )
            elif    keys[0] == 'facto'   : 
                if keys[1] >= 0:  self.final_value['s'] = math.factorial( keys[1] ) 
                else: self.error['s'] = "error"
            elif    keys[0] == 'floor'   : self.final_value['s'] = math.floor( keys[1] )
            elif    keys[0] == 'ceil'    : self.final_value['s'] = math.ceil( keys[1] )
            elif    keys[0] == 'abs'     : self.final_value['s'] = math.fabs( keys[1] )
            elif    keys[0] == 'rexp'    : self.final_value['s'] = math.frexp( keys[1] )
            elif    keys[0] == 'pgcd'    : self.final_value['s'] = math.gcd( keys[1] )
            elif    keys[0] == 'modf'    : self.final_value['s'] = math.modf( keys[1] )
            elif    keys[0] == 'mod'     : self.final_value['s'] = math.fmod( keys[1][ 0 ], keys[1][ 1 ] )
            elif    keys[0] == 'round'   : self.final_value['s'] = round( keys[1][ 0 ], keys[1][ 1 ])
            elif    keys[0] == 'csign'   : self.final_value['s'] = math.copysign( keys[1][ 0 ], keys[1][ 1 ] )
            elif    keys[0] == 'inv_rexp': self.final_value['s'] = math.ldexp( keys[1][ 0 ], keys[1][ 1 ] )
            elif    keys[0] == 'isclose' : self.final_value['s'] = math.isclose( keys[1][ 0 ], keys[1][ 2 ], rel_tol=keys[1][ 1 ], abs_tol=keys[1][ 3 ] )
            elif    keys[0] == 'sorted'  :
                items = list(keys[1][0].items())
                self.final_value['s'] = sorted(items, key = lambda x : x[0], reverse=keys[1][1])
                self.final_value['s'] = dict(self.final_value)
        except TypeError: pass
        except ZeroDivisionError: self.error['s'] = er.ERRORS( self.line ).ERROR4( self.normal_string )
        except ValueError: pass

        return  self.final_value['s'], self.error['s']
