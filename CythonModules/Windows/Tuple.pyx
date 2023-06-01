from script.STDIN.LinuxSTDIN      import bm_configure as bm
from CythonModules.Windows        import fileError as fe 

cdef class Tuple:
    cdef public :
        int line 
    def __init__(self, line):
        self.line       = line 
    cpdef Tuple(self, Obj, str String=''):

        cdef : 
            int i 
            str error 
            str func 


        error = ''
        func = bm.fg.rbg(0, 255, 0   )+' in tuple( ).' + bm.init.reset 

        if type( Obj ) in [ type(list()), type(tuple())]: 
            if Obj:
                for i in range(len(Obj)):
                    if type(Obj[i] ) not in [type(list()), type(dict())]: pass 
                    else: 
                        if type(Obj[i] ) == type( list()): 
                            error = ERROR1(line=self.line, string='a list' )
                            break
                        else: 
                            error = ERROR1(line=self.line, string='a dictionary' )
                            break 
                if error: return None, error
                else: 
                    try:  return tuple(Obj), None
                    except (TypeError, ValueError):
                        error = ERROR2(line=self.line, string=String, _char_='a tuple', func=func)
                        return None, error
            else: return (), None

        elif type( Obj ) == type( dict()) : 
            if Obj: 
                error = ERROR3(line=self.line,  _char_='a tuple', func=func)
                return None, error 
            else: return (), None
        else:
            try:  return  tuple(Obj) , None
            except (TypeError, ValueError) : 
                error = ERROR2(line=self.line, string=String, _char_='a tuple', func=func)
                return None, error

cdef str ERROR1( int line, str string = 'a list' ):
    cdef :
        str error , err
        str cyan, white, yellow, reset 

    cyan       = bm.fg.cyan_L
    yellow     = bm.fg.yellow_L
    white      = bm.fg.white_L
    reset      = bm.init.reset

    err = '{}{}. {}line: {}{}'.format(yellow, string, white, yellow, line)
    error = fe.FileErrors( 'TypeError' ).Errors()+'{}tuple {}object cannot contain '.format(cyan, white) + err

    return error+reset

cdef str ERROR2( int line, str string, str _char_ = 'an integer', str func = '') :
    cdef :
        str error , err
        str cyan, white, yellow, reset 

    cyan       = bm.fg.cyan_L
    yellow     = bm.fg.yellow_L
    white      = bm.fg.white_L
    red        = bm.fg.red_L
    reset      = bm.init.reset

    err = '{}to  {}{}() {}type. {}line: {}{}.'.format(white, red, _char_, yellow, white, yellow, line )
    error = fe.FileErrors( 'ValueError' ).Errors() + '{}impossible to convert {}<< {} >> '.format(white, cyan, string) + err + func
    
    return error+reset

cdef str ERROR3( int line,  str _char_ = 'an integer', str func = '') :
    cdef :
        str error , err
        str cyan, white, yellow, reset 

    cyan       = bm.fg.cyan_L
    yellow     = bm.fg.yellow_L
    white      = bm.fg.white_L
    red        = bm.fg.red_L
    m          = bm.magenta_M
    reset      = bm.init.reset

    err = '{}to  {}{}() {}type. {}line: {}{}.'.format(white, red, _char_, yellow, white, yellow, line )
    error = fe.FileErrors( 'ValueError' ).Errors() + '{}impossible to convert {}a non-EMPTY {}dictionary '.format(white, cyan, m) + err + func
    
    return error+reset

 