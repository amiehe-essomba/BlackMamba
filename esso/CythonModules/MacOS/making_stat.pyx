from statistics                 import variance, stdev, pstdev, pvariance
from statistics                 import harmonic_mean, median, median_low, median_high, median_grouped, mode, quantiles, multimode
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from CythonModules.Windows      import fileError as fe 
from CythonModules.Windows      import arithmetic_analyze as aa
from numpy                      import quantile
from math                       import sqrt

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
                    covXY =  ( sumUp / length )
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
            avgY, error   = GetValue( Y, line ).mean( length, ob_type )
            if not error:
                avgX, error   = GetValue( X, line ).mean( length, ob_type )

                if not error:
                    try:
                        beta    = covXY / varX
                        alpha   = avgY - beta * avgX
                    except ZeroDivisionError: error = ERRORS(line).ERROR6(func=func)
                else: error += func
            else : error += func
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
                try:
                    coefXY   =  covXY / coefXY
                except ZeroDivisionError: error = ERRORS(line).ERROR6(func=func)
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

    cpdef grouped( self, str ob_type = 'list' )                                                                         :
        cdef :
            int length, idd
            list master, master2 

        value   = 0.0
        error   = ''
        func    = bm.fg.rbg(0, 255, 0   )+' in grouped( ).' + bm.init.reset 
        master1 = []
        master  = []

        if self.listOfValue:
            for _value_ in self.listOfValue :
                try:
                    value += _value_ * 1.0
                    if not master1:
                        master1.append( _value_ )
                        master.append( (_value_, 1))
                    else:
                        if _value_ not in master1:
                            master1.append( _value_ )
                            master.append( (_value_, 1))
                        else:
                            idd = master1.index( _value_ )
                            try:
                                master[idd] = list( master[idd] )
                                master[idd][1] += 1
                                master[idd] = tuple(master[idd])
                            except TypeError:
                                error = ERRORS( self.line ).ERROR1( master[idd][1], 1, func )
                                break
                except TypeError:
                    error = ERRORS( self.line ).ERROR1( value, _value_, func )
                    break
                else: pass

        else: error = ERRORS( self.line ).ERROR2( ob_type, func )

        return master, error

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
    
    cpdef harmonic_mean(self, str ob_type = 'list')                                                                     :
        cdef :
            int length 

        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'harmonic_mean' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        result  = 0.0
        
        if self.listOfValue:
            length          = len( self.listOfValue )
            for _value_ in self.listOfValue:
                try:
                    value += 1.0 / _value_
                except TypeError:
                    error = ERRORS( self.line ).ERROR1(value , _value_, func )
                    break
                except ZeroDivisionError: 
                    error = ERRORS( self.line ).ERROR6( func )
                    break
            
            if not error: 
                try : result  = length / value
                except ZeroDivisionError: error = ERRORS( self.line ).ERROR6( func )
            else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )
       
        return result, error
    
    cpdef geometric_mean(self, str ob_type = 'list')                                                                    :
        cdef :
            int length 

        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'geometric_mean' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        result  = 0.0
        
        if self.listOfValue:
            length = len( self.listOfValue )
            for _value_ in self.listOfValue:
                try:
                    value *=_value_
                except TypeError:
                    error = ERRORS( self.line ).ERROR1(value , _value_, func )
                    break   

            if not error: 
                try: result = sqrt( value ) ** length 
                except ValueError : error = ERRORS( self.line ).ERROR7( value, func )
            else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )
       
        return result, error
    
    cpdef mean_grouped(self, str ob_type = 'list')                                                                      :
        cdef :
            int length 
            list master

        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'mean_grouped' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        result  = 0.0
        
        if self.listOfValue:
            master, error = GetValue( self.listOfValue, self.line ).grouped( ob_type )
            if not error:
                length = len( self.listOfValue )
                for x, _value_ in master :
                    try:
                        value += _value_ * x
                    except TypeError:
                        error = ERRORS( self.line ).ERROR1(value , _value_, func )
                        break   

                if not error: result = value / float(length)
                else: pass
            else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )
       
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
    
    cpdef cov_corr_linear_r( self, list Index, str cal_type = 'cov', str ob_type1 = 'list', str ob_type2 = 'list', str _type_ = 'pop' )     :
        
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
            
            if   cal_type == 'med': result = median( self.listOfValue )
            elif cal_type == 'medl': result = median_low( self.listOfValue )
            elif cal_type == 'medg': result = median_grouped( self.listOfValue )
            else: result = median_high( self.listOfValue )
            
        else: result = 0.0

        return float(result), error
    
    cpdef quantiles( self, str ob_type = 'list', numeric = 1, str mod = 'quantiles' )                                                                        :

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
            error   = None 
            if mod == 'quantiles': result  = quantiles( self.listOfValue, n = numeric )
            else: result  = quantile( self.listOfValue, numeric )
        else: result = None

        return result, error
    
    cpdef mod_mulmod( self, str cal_type = 'mode', str ob_type = 'list' )  :
        error = ''
        func  = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( cal_type ) + bm.init.reset

        if cal_type == 'mode':      
            if self.listOfValue : return mode( self.listOfValue ), None
            else:
                error = error = ERRORS( self.line ).ERROR2( ob_type, func )
                return None, error 
        else:     
            if self.listOfValue: return multimode( self.listOfValue ), None
            else:
                error = error = ERRORS( self.line ).ERROR2( ob_type, func )
                return None, error 

    cpdef kurtosis(self, str ob_type = 'list', str _type_ = 'pop'):
        cdef:
            float varX
            float avgX
            int length
            float summ
            

        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'kurtosis' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        summ    = 0.0
        result  = 0.0

        if self.listOfValue:
            varX, error = GetValue( self.listOfValue, self.line ).var_std( 'var', _type_, ob_type )
            if not error:
                length = len( self.listOfValue )
                avgX, error   = GetValue( self.listOfValue, self.line ).mean( length, ob_type )
                if not error :
                    for i, x in enumerate( self.listOfValue ):
                        try: summ += (x - avgX) ** 4
                        except TypeError:
                            error = ERRORS( self.line ).ERROR1(value , x, func )
                            break
                    
                    if not error:
                        varX = varX ** 2
                        if _type_ == 'pop': result = summ / (length * varX)
                        else:
                            try: result = summ / ((length-1) * varX)
                            except ZeroDivisionError: result = summ / (length * varX)
                    else: pass
                else: pass
            else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )
       
        return result, error

    cpdef iquantile(self, str ob_type = 'list', str _type_ = 'pop'):
        cdef:
            float q1
            float q3
        
        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'iquantile' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        result  = 0.0
   
        q1, error = GetValue( self.listOfValue, self.line ).quantiles(ob_type = ob_type, numeric = 0.25, mod = 'quantile' ) 
        if not error:
            q3, error   = GetValue( self.listOfValue, self.line ).quantiles(ob_type = ob_type, numeric = 0.75, mod = 'quantile' ) 
            if not error :  result = q3 - q1
            else: pass
        else: pass

        return float(result), error

    cpdef q1_q3(self, str ob_type = 'list', str _type_ = 'Q1'):
        
        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'iquantile' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        result  = 0.0

        if _type_ == 'Q1':
            result, error = GetValue( self.listOfValue, self.line ).quantiles(ob_type = ob_type, numeric = 0.25, mod = 'quantile' ) 
        else:
            result, error   = GetValue( self.listOfValue, self.line ).quantiles(ob_type = ob_type, numeric = 0.75, mod = 'quantile' ) 
      
        return float(result), error

    cpdef lower_upper_fence(self, str ob_type = 'list', str _type_ = 'pop', cal_type = 'lf'):
        cdef:
            float q1
            float iq
            float q3
    
        if cal_type == 'lf': func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'lower_fence' ) + bm.init.reset 
        else: func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'upper_fence' ) + bm.init.reset 

        value   = 0.0
        error   = ''
        result  = 0.0
   
        iq, error   = GetValue( self.listOfValue, self.line ).iquantile(ob_type = ob_type, _type_=_type_ ) 
        
        if not error:
            if   cal_type == 'lf':
                q1, error = GetValue( self.listOfValue, self.line ).quantiles(ob_type = ob_type, numeric = 0.25, mod = 'quantile' ) 
                if not error :  result = q1 - 1.5 * iq
                else: pass
            elif cal_type == 'uf':
                q3, error = GetValue( self.listOfValue, self.line ).quantiles(ob_type = ob_type, numeric = 0.75, mod = 'quantile' ) 
                if not error :  result = q3 + 1.5 * iq
                else: pass
        else: pass
       
        return result, error

    cpdef mad(self, str ob_type = 'list'):
        cdef:
            float avgX
            int length
          
        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'mad' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        result  = 0.0
        
        if self.listOfValue:
            length          = len( self.listOfValue )
            avgX, error     = GetValue( self.listOfValue, self.line ).mean( length, ob_type )
            if not error:
                for _value_ in self.listOfValue:
                    try:
                        value += abs( _value_ - avgX )
                    except TypeError:
                        error = ERRORS( self.line ).ERROR1(value , _value_, func )
                        break
                    else: pass
                
                if not error: result = (value / length)
                else: pass
            else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )
        
        return result, error
    
    cpdef rsd(self, str ob_type = 'list', str _type_ = 'pop'):
        cdef:
            float avgX
            int length
            float stdX
          
        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'rsd' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        result  = 0.0
        
        if self.listOfValue:
            length          = len( self.listOfValue )
            avgX, error     = GetValue( self.listOfValue, self.line ).mean( length, ob_type )
            if not error:
                stdX, error     = GetValue( self.listOfValue, self.line ).var_std( 'std', _type_, ob_type )
                if not error: 
                    result = (stdX / avgX) * 100
                else: pass
            else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )
        
        return result, error
    
    cpdef std_error(self, str ob_type = 'list', str _type_ = 'pop'):
        cdef:
            int length
            double stdX = 0.0
          
        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'std_error' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        result  = 0.0
        
        if self.listOfValue:
            length          = len( self.listOfValue )
            stdX, error     = GetValue( self.listOfValue, self.line ).var_std( 'std', _type_, ob_type )
            if not error: 
                if _type_ == 'pop':  result = stdX / sqrt(length)
                else:
                    try:  result = stdX / sqrt(length-1)
                    except ZeroDivisionError: result = stdX / sqrt(length)
            else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )
        
        return result, error
    
    cpdef skewness(self, str ob_type = 'list', str _type_ = 'pop'):
        cdef:
            float avgX
            int   length
            double stdX = 0.0
            float m2, m3
          
        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'skewness' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        result  = 0.0
        m2, m3  = 0.0, 0.0
        
        if self.listOfValue:
            length          = len( self.listOfValue )
            avgX, error     = GetValue( self.listOfValue, self.line ).mean( length, ob_type )
            if not error:
                for _value_ in self.listOfValue:
                    try:
                        m2 += ( _value_ - avgX ) ** 2
                        m3 += ( _value_ - avgX ) ** 3
                    except TypeError:
                        error = ERRORS( self.line ).ERROR1(m2 , _value_, func )
                        break
                    else: pass
                
                if not error: 
                    stdX = stdX ** 3
                    if _type_ == 'pop':
                        m2 /= length
                        m3 /= length
                        result = m3 / (m2 ** (3/2))
                    else:
                        try: 
                            m2 /= (length-1)
                            m3 /= (length-1)
                            result = m3 / (m2 ** (3/2))
                        except ZeroDivisionError: 
                            m2 /= length
                            m3 /= length
                            result = m3 / (m2 ** (3/2))
                else: pass
            else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )
       
        return result, error

    cpdef sum_square(self, str ob_type = 'list'):
      
        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'sum_square' ) + bm.init.reset 
        error   = ''
        result  = 0.0
        
        if self.listOfValue:
            for _value_ in self.listOfValue:
                try:
                    result += _value_ ** 2
                except TypeError:
                    error = ERRORS( self.line ).ERROR1(result , _value_, func )
                    break
                else: pass
            
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )
       
        return result, error

    
    cpdef rms(self, str ob_type = 'list'):
        cdef:
            float avgX
            int length
          
        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'rms' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        result  = 0.0
       
        if self.listOfValue:
            length          = len( self.listOfValue )
            avgX, error     = GetValue( self.listOfValue, self.line ).mean( length, ob_type )
            if not error:
                for _value_ in self.listOfValue:
                    try:
                        value += ( _value_ - avgX ) ** 2
                    except TypeError:
                        error = ERRORS( self.line ).ERROR1(value , _value_, func )
                        break
                    else: pass
                
                if not error:  result = sqrt( value / length)
                else: pass
            else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )
       
        return result, error
    
    cpdef midrange(self, str ob_type = 'list'):
        cdef:
            float minX, maxX
            int length
          
        func    = bm.fg.rbg(0, 255, 0   ) + ' in {}( ).'.format( 'midlerange' ) + bm.init.reset 
        value   = 0.0
        error   = ''
        result  = 0.0
       
        if self.listOfValue:
            length          = len( self.listOfValue )
            minX, error     = GetValue( self.listOfValue, self.line ).min_max( 'min', ob_type )
            if not error:
                maxX, error     = GetValue( self.listOfValue, self.line ).min_max( 'max', ob_type )
                if not error:  result = (minX + maxX) / 2.0
                else: pass
            else: pass
        else: error = ERRORS( self.line ).ERROR2( ob_type, func )
       
        return result, error

cdef class Range:
    cdef public:
        listOfValue 
        int     line 
    def __init__( self, listOfValue, line ):
        self.listOfValue        = listOfValue
        self.line               = line 

    cpdef var_std( self, str cal_type = 'var', str _type_ = 'pop'):
        cdef :
            double summ = 0.0 

        if _type_ == 'pop':
            if cal_type == 'var'    : return pvariance( self.listOfValue ), None
            elif cal_type == 'sum'  :
                for _sum_ in self.listOfValue:
                    summ += _sum_
                
                return summ, None 

            else: return pstdev( self.listOfValue ), None
        elif _type_ == 'sam':
            if cal_type == 'var'    : return variance( self.listOfValue ), None
            elif cal_type == 'sum'  : return sum(self.listOfValue ), None
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

        typ1, typ2  = ERRORS( self.line ).TYPE( typ1, typ2 )

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
        error = fe.FileErrors( 'ValueError' ).Errors() + '{}{}s {}have not the same {}size. '.format( self.magenta, 
											ob_type, self.green, self.cyan) + error + func

        return error + self.reset
    
    cdef str ERROR5(self, str string = 'variance', str func = ''):
        error = '{}line : {}{}'.format(self.white_l, self.yellow_l, self.line)
        error = fe.FileErrors( 'ValueError' ).Errors() + '{}{} {}= {}0.0 '.format( self.magenta, string, self.white_l,
                                             self.cyan) + error + func
        return error+ self.reset

    cdef str ERROR6(self, str func = ''):
        error = '{}line : {}{}'.format(self.white_l, self.yellow_l, self.line)
        error = fe.FileErrors( 'ZeroDivisionError' ).Errors() + '{}division by 0.0. '.format( self.yellow_l) + error + func

        return error+ self.reset
    
    cdef str ERROR7(self, float value, str func = ''):
        error = '{} is negative. {}line: {}{}'.format(self.green, self.white, self.yellow, self.line)
        error = fe.FileErrors( 'DomainError' ).Errors() + '{}<< {} >>'.format( self.cyan, value) + error+func

        return error+self.reset

    cdef TYPE(self, object1 , object2 ):
        cdef:
            result1 
            result2 

        result1  = ''
        result2  = ''
        if type( object1 ) in [ type( list() ), type( tuple()) ]:
            if len( object1 ) < 4 : result1 = object1
            else: 
                if type( object1 ) in [ type( list() ) ]: 
                    result1 = f'[{object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]}]'
                else:
                    result1 = f'({object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]})'
        elif type( object1 ) == type( str() ):
            if object1:
                if len( object1 ) < 6: result1 = object1
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
                if len( object2 ) < 6: result2 = object2
                else:
                    result2 = object2[ : 2 ] + ' ... ' + object2[ -2 : ]
            else: pass
        else: result2 = object2
                
        return result1, result2
    
