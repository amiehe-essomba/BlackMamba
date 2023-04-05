def SUM( list value ):
    cdef :
        double summ = 0.0

    for _sum_ in value:
        summ += _sum_ 

    return summ 

def SUMM( value ):
    return SUM( value )