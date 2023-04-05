from script                                 import control_string
from script.LEXER                           import float_or_function
from CythonModules.Windows.LEXER.particular import particular_str_selection as PSS
from script.STDIN.LinuxSTDIN                import bm_configure as bm
from CythonModules.Windows                  import fileError as fe 

cdef class DICTIONNARY:
    cdef public:
        str master
        dict data_base 
        unsigned long int line 
    
    cdef :
        str error 

    def __cinit__(self, master, data_base, line):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.error          = ""

    cdef ANALYSES(self, str main_string):
        cdef:
            list final, final_value, init
            signed long long int i
            str name
        
        final_value = []

        self.master, self.error  = control_string.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( self.master, name="cython" )
        if not self.error :
            final, self.error = PSS.SELECTION(self.master, self.master, self.data_base, self.line).CHAR_SELECTION( '$' )
 
            if not self.error:
                if len( final ) == 1: final_value.append( self.master )
                else:
                    for i in range(len(final)):
                        if final[i] == '':
                            self.error = ERRORS(self.line).ERROR1( self.master )
                            break 
                        else: pass 
                    
                    if not self.error:
                        init           = final[1 : ]
                        name, self.error = control_string.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( final[ 0 ], name="cython")
                        if not self.error:
                            final_value.append( name )
                            
                            for i in range(len(init)):
                                name, self.error = control_string.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( init[i], name="cython" )
                                if not self.error:
                                    name, self.error = control_string.STRING_ANALYSE( self.data_base, self.line ).CHECK_NAME( name, name="cython" )
                                    if not self.error: final_value.append( name )
                                    else: break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                            else: self.error = ERRORS( self.line ).ERROR0( self.master )
                        else: self.error = ERRORS( self.line ).ERROR0( self.master )
                    else:  pass
            else: pass
        else: self.error = ERRORS( self.line ).ERROR0(self.master)

        return final_value, self.error

cdef class ERRORS:
    cdef public:
        unsigned long long int line 
    cdef:
        str cyan, red, green, yellow, magenta, white, blue, reset, error
    def __cinit__(self, line):
        self.line       = line
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset
        self.error      = ''

    cdef str ERROR0(self, str string):
        self.error = ' {}line: {}{}'.format( self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>.'.format(self.white, self.cyan, string)+self.error

        return self.error+self.reset

    cdef str ERROR1(self, str string):
        self.error = '{}due to bad {}<< {}$ {}>> {}position. {}line: {}{}'.format(self.white,  self.blue, self.magenta, self.blue,
                                                    self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {}{} {}>>. '.format(self.white, self.cyan, 
                                                    self.red, string, self.cyan) + self.error

        return self.error+self.reset
                                       
                    