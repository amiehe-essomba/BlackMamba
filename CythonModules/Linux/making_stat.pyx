from statistics                 import variance, stdev, pstdev, pvariance
from statistics                 import harmonic_mean, median, median_low, median_high, median_grouped, mode, quantiles, multimode
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from CythonModules.Linux        import fileError as fe 
from CythonModules.Linux        import arithmetic_analyze as aa

cdef CovXY(list X, list Y, str ob_type = 'list', int line = 0, str _type_ = 'pop'   )           :
    cdef :
        float       valueX, valueY
        float       meanX, meanY
        float       sumUp, covXY
        int         i
        long        length 
        str         error, func

    sumUp           = 0.0
    func            = bm.fg.rbg(255, 255, 0   ) + ' used in cov( ) ' + bm.init.reset
    length          = len( X )
    covXY           = 0.0
    meanX, error    = GetValue( X, line ).mean( length, ob_type )
    if not error:
        meanY, error = GetValue( Y, line ).mean( length, ob_type )
        if not error:
            for i in range( length ):
                valueX      = ( X[ i ] - meanX )
                valueY      = ( Y[ i ] - meanY )
                sumUp       += valueX * valueY
            
            try:
                if _type_ == 'pop':
                    covXY /=  ( sumUp / length )
                else:
                    covXY = ( sumUp / (length - 1 ) )
            except ZeroDivisionError :
                covXY = ( sumUp /  length )
        else: error += func 
    else: error += func

    return covXY, error
    
cdef Linear_R(list X, list Y, str ob_type = 'list', int line = 0, str _type_ = 'pop')           :
    cdef :
        float      covXY 
        float      varX
        float      beta, alpha
        float      avgX, avgY
        long       length 
        str        func

    func            = bm.fg.rbg(255, 255, 0   ) + ' used in linearR( ) ' + bm.init.reset
    beta            = 0.0 
    alpha           = 0.0 
    varX            = 0.0 
    covXY           = 0.0 
    covXY, error = CovXY( X, Y, ob_type, line,  _type_)
    if not error:
        varX, error = GetValue( X, line ).var_std( 'var', _type_, ob_type )
        if not error:
            length = len( Y )
            avgY   = GetValue( Y, line ).mean( length, ob_type )
            avgX   = GetValue( X, line ).mean( length, ob_type )

            beta    = covXY / varX
            alpha   = avgY - beta * avgX

        else: error += func
    else: error += func

    return beta, alpha, error

cdef CoefXY(list X, list Y, str ob_type = 'list', int line = 0, str _type_ = 'pop'  )           :
    cdef :
        float       valueX, valueY
        float       meanX, meanY
        float       sumDownX, sumDownY, coefXY, covXY
        int         i
        long        length 
        str         error, func

    func            = bm.fg.rbg(255, 255, 0   ) + ' used in cor( ) ' + bm.init.reset
    sumDownX        = 0.0 
    sumDownY        = 0.0
    coefXY          = 0.0 
    covXY           = 0.0
    length          = len( X )
    meanX, error    = GetValue( X, line ).mean( length, ob_type )
    if not error:
        meanY,error = GetValue( Y, line ).mean( length, ob_type )
        if not error:
            for i in range( length ):
                valueX = ( X[ i ] - meanX )
                valueY = ( Y[ i ] - meanY )

                sumDownX += valueX ** 2 
                sumDownY += valueY ** 2
            
            if _type_ == 'pop':
                coefXY   = (( sumDownX / length ) ** 0.5 ) * (( sumDownY / length )** 0.5)
            else:
                try:
                    coefXY  = (( sumDownX / (length - 1) ) ** 0.5 ) * (( sumDownY / ( length - 1 ) )** 0.5)
                except ZeroDivisionError:
                    coefXY   = (( sumDownX / length ) ** 0.5 ) * (( sumDownY / length )** 0.5)

            covXY, error  = CovXY( X, Y, ob_type, line, _type_)
            if not error:
                coefXY   =  covXY / coefXY
            else:
                error += func 
                coefXY = 0.0
        else: error += func 
    else: error += func

    return coefXY, error



cdef class GetValue:
    cdef :
        public list    listOfValue
        public int     line
    
    cdef :
        int     length
        float   value
        float   result
        str     error
        int     i
        str     func
     
    def __init__(self, listOfValue, line = 0 )                                                                          :
        self.listOfValue                = listOfValue
        self.line                       = line


    cpdef mean( self, int length, str ob_type = 'list' )                                                                :
        value   = 0.0
        error   = ''
        func    = bm.fg.rbg(0, 255, 0   )+' in mean( ).' + bm.init.reset 

        if self.listOfValue:
            for _value_ in self.listOfValue :
                try:
                    value += _value_
                except TypeError:
                    error = ERRORS( self.line ).ERROR1( value , _value_, func )
                    break
                else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )

        if not error: 
            error = None    
            result = value / float( length )
        else: result = 0.0

        return result, error

    cpdef sum( self, str ob_type = 'list' )                                                                             :

        value   = 0.0
        error   = ''
        func    = bm.fg.rbg(0, 255, 0   )+' in sum( ).' + bm.init.reset 

        if self.listOfValue:
            for _value_ in self.listOfValue:
                try:
                    value += _value_
                except TypeError:
                    error = ERRORS( self.line ).ERROR1( value , _value_, func )
                    break
                else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )

        if not error : 
            error   = None
            result  = value
        else: result = 0.0

        return result, error

    cpdef min_max( self, str cal_type = 'min', str ob_type = 'list' )                                                   :

        value   = 0.0
        error   = ''
        func    = bm.fg.rbg(0, 255, 0   )+' in {}( ).'.format( cal_type) +  bm.init.reset 

        if self.listOfValue:
            for _value_ in self.listOfValue:
                try:
                    value += _value_
                except TypeError:
                    error = ERRORS( self.line ).ERROR1(value , _value_, func )
                    break
                else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )

        if not error : 
            error = None
            if cal_type == 'min': result = min( self.listOfValue )
            else: result = max( self.listOfValue )
        else: result = 0.0

        return result, error
    

    cpdef var_std( self, str cal_type = 'var', str _type_ = 'pop', str ob_type = 'list' )                               :

        value   = 0.0
        error   = ''
        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( cal_type ) + bm.init.reset 
        
        if ob_type in ['list', 'tuple' ]:
            if self.listOfValue:
                for _value_ in self.listOfValue:
                    try:
                        value += _value_
                    except TypeError:
                        error = ERRORS( self.line ).ERROR1(value , _value_, func )
                        break
                    else: pass
            else: error = ERRORS( self.line ).ERROR2( ob_type, func )
        else: pass

        if not error: 
            error = None
            if _type_ == 'pop':
                if cal_type == 'var': result = pvariance( self.listOfValue )
                else: result = pstdev( self.listOfValue )
            elif _type_ == 'sam':
                if cal_type == 'var': result = variance( self.listOfValue )
                else: result = stdev( self.listOfValue )
            else: error = ERRORS( self.line ).ERROR3( _type_, func )
        else: result = 0.0

        return result, error
    
    cpdef cov_corr_linear_r( self, list Index, str cal_type = 'cov', str ob_type1 = 'list', str ob_type2 = 'list',str _type_ = 'pop' )     :
        
        cdef:
            float   result , r
            str     error 

        r           = 0.0
        result      = 0.0
        error       = ''
        func        = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( cal_type ) + bm.init.reset

        if ob_type1 == ob_type2:
            if len( self.listOfValue ) == len( Index ):
                if Index:
                    if cal_type == 'cov':
                        result, error = CovXY( self.listOfValue, Index, ob_type1, self.line, _type_ )
                    elif cal_type == 'linearR':
                        result, r, error = Linear_R( self.listOfValue, Index, ob_type1, self.line, _type_ )
                    elif cal_type == 'cor':
                        result, error = CoefXY( self.listOfValue, Index, ob_type1, self.line, _type_ )
                else: error = ERRORS( self.line ).ERROR2( ob_type1, func )
            else: error = ERRORS( self.line ).ERROR4( ob_type1, func )
        else: error = ERRORS( self.line ).ERROR1(self.listOfValue, Index, func )

        if not error: pass 
        else: result = 0.0

        return result, r,  error

       
    cpdef med_medh_medl_medg( self, str cal_type = 'med', str ob_type = 'list' )                                        :

        value   = 0.0
        error   = ''
        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( cal_type ) + bm.init.reset

        if self.listOfValue:
            for _value_ in self.listOfValue:
                try:
                    value += _value_
                except TypeError:
                    error = ERRORS( self.line ).ERROR1(value , _value_, func )
                    break
                else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )

        if not error: 
            error = None
            
            if cal_type == 'med': result = median( self.listOfValue )
            elif cal_type == 'medl': result = median_low( self.listOfValue )
            elif cal_type == 'medg': result = median_grouped( self.listOfValue )
            else: result = median_high( self.listOfValue )
            
        else: result = 0.0

        return result, error
    
    cpdef quantile( self, str ob_type = 'list' )                                                                        :

        value   = 0.0
        error   = ''
        func    = bm.fg.rbg(0, 255, 0   ) + ' in quantile( ).' + bm.init.reset

        if self.listOfValue:
            for _value_ in self.listOfValue:
                try:
                    value += _value_
                except TypeError:
                    error = ERRORS( self.line ).ERROR1(value , _value_, func )
                    break
                else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )

        if not error: 
            error = None 
            result = quantiles( self.listOfValue )
        else: result = None

        return result, error
    
    cpdef mod_mulmod( self, str cal_type = 'mode', str ob_type = 'list' )                                               :
        error = ''
        func  = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( cal_type ) + bm.init.reset

        if cal_type == 'mode':      
            if self.listOfValue :
                return mode( self.listOfValue ), None
            else:
                error = error = ERRORS( self.line ).ERROR2( ob_type, func )
                return None, error 
        else:     
            if self.listOfValue:                                         
                return multimode( self.listOfValue ), None
            else:
                error = error = ERRORS( self.line ).ERROR2( ob_type, func )
                return None, error 

cdef class Range:
    cdef public:
        listOfValue 
        int     line 
    def __init__( self, listOfValue, line ):
        self.listOfValue        = listOfValue
        self.line               = line 

    cpdef var_std( self, str cal_type = 'var', str _type_ = 'pop'):
        if _type_ == 'pop':
            if cal_type == 'var': return pvariance( self.listOfValue ), None
            elif cal_type == 'sum' : return sum(self.listOfValue ), None
            else: return pstdev( self.listOfValue ), None
        elif _type_ == 'sam':
            if cal_type == 'var': return variance( self.listOfValue ), None
            elif cal_type == 'sum' : return sum(self.listOfValue ), None
            else: return stdev( self.listOfValue ), None
    
    cdef SUM( self ):
        cdef :
            int i  
            long _sum_  

        _sum_ = 0 

        for i in range( len( self.listOfValue )):
            _sum_ += self.listOfValue[ i ]

        return _sum_

cdef class ERRORS:
    cdef public int line 
    cdef :
        str error
        str yellow_l 
        str white_l
        str blue_l
        str magenta
        str green
        str cyan
        str reset

    def __init__( self, line ):
        self.line       = line
        self.yellow_l   = bm.fg.yellow_L 
        self.white_l    = bm.fg.white_L 
        self.blue_l     = bm.fg.blue_L
        self.magenta    = bm.fg.magenta
        self.green      = bm.fg.green
        self.cyan       = bm.fg.cyan
        self.reset      = bm.init.reset

    cdef str ERROR1( self, typ1, typ2 , str func = '')      :

        typ11 = aa.FINAL_VALUE( [], {}, self.line, [] ).CONVERSION( typ1 )
        typ22 = aa.FINAL_VALUE( [], {}, self.line, [] ).CONVERSION( typ2 )

        typ1, typ2  = ERRORS( self.line ).TYPE( typ1, typ2)

        error = '{}unsupported operand between {}<< {}{} : {} >> {} and {}<< {}{} : {} >>. {}line: {}{}'.format(self.yellow_l, self.white_l, typ11, self.white_l, typ1,
                                self.yellow_l, self.white_l, typ22, self.white_l, typ2, self.white_l, self.yellow_l, self.line )
        error = fe.FileErrors( 'ArithmeticError' ).Errors() + error + func

        return error + self.reset 
    
    cdef str ERROR2( self , str ob_type , str func = '')    :
        error = '{}line : {}{}'.format( self.white_l, self.yellow_l, self.line )
        error = fe.FileErrors( 'ValueError' ).Errors() + '{}EMPTY {}{}. '.format(self.yellow_l, self.blue_l, ob_type) + error + func
		
        return error + self.reset

    cdef str ERROR3( self , str string , str func = '')     :
        error = '{}line : {}{}'.format( self.white_l, self.yellow_l, self.line )
        error = fe.FileErrors( 'AttributeError' ).Errors() + '{}{} {}is not in the list {}[pop, sam]. '.format(self.blue_l, string, self.yellow_l, 
                                            self.magenta) + error + func
		
        return error + self.reset

    cdef str ERROR4( self, str ob_type, str func = '' )     :
        error = '{}line : {}{}'.format(self.white_l, self.yellow_l, self.line)
        error = fe.FileErrors( 'ValuecError' ).Errors() + '{}{}s {}have not the same {}size. '.format( self.magenta, 
											ob_type, self.green, self.cyan) + error + func

        return error + self.reset
    
    cdef TYPE(self, object1 , object2 ):
        cdef:
            result1 
            result2 
        
        if type( object1 ) in [ type( list() ), type( tuple()) ]:
            if len( object1 ) < 4 : result1 = object1
            else: 
                if type( object1 ) in [ type( list() ) ]: 
                    result1 = f'[{object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]}]'
                else:
                    result1 = f'({object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]})'
        elif type( object1 ) == type( str() ):
            if object1:
                if len( object1 ) < 6: pass 
                else:
                    result1 = object1[ : 2 ] + ' ... ' + object1[ -2: ]
            else: pass 
        else: result1 = object1
        
        if type( object2 ) in [ type( list() ), type( tuple()) ]:
            if len( object2 ) < 4 : result2 = object2
            else: 
                if type( object2 ) in [ type( list() ) ]:
                    result2 = f'[{object2[0]}, {object2[1]}, ....., {object2[-2]}, {object2[-1]}]'
                else:
                    result2 = f'({object2[0]}, {object2[1]}, ....., {object2[-2]}, {object2[-1]})'
        elif type( object2 ) == type( str() ):
            if object2:
                if len( object2 ) < 6: pass 
                else:
                    result2 = object2[ : 2 ] + ' ... ' + object2[ -2 : ]
            else: pass
        else: result2 = object2
                
        return result1, result2
    
