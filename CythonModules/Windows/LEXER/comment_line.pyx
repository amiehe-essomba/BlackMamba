"""
module used to analyse main string and make it comment if
the symbol < # > is used at the beginning of each line.
to make line a comment line is simple, set < # > at the beginning like this

# that's is a comment line

"""

from statement.error    import error
from script             import control_string

cdef class COMMENT_LINE:
    cdef public:
        str master 
        dict data_base
        unsigned long int line 
    cdef:
        str error
        list Char 
        str string 
        signed long int idd 

    def __cinit__(self,
        master      ,    # concatenate main string
        data_base   ,    # the data base
        line        ,    # current line
        ):

        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.error              = ''
        self.Char               = [ '#' ]
        self.string             = ''
        self.idd                = -1

    cpdef tuple COMMENT( self ):
        cdef :
            long int i 
            str s, err, ns
        
        try:
            self.master, self.error = control_string.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( self.master, "cython" )
        except TypeError: pass


        try:
            # if the first character of master if < # > the line is a comment line and then string takes < comment >
            # value , it means that this line will be not exercuted,
            # if string takes < string > value this will be exercuted by the lexer and the tokens will be
            # produiced by the lexer to be analysing by the perxer

            for i, s in enumerate( self.master ):
                if s not in self.Char:
                    self.idd = i
                    break
                else: pass

            if self.idd != -1:
                if self.idd == 0: self.string = 'comment'
                else:
                    try:
                        self.ns, err = control_string.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE(self.master[ : self.idd], "cython")
                        if not err: self.string = 'stringcomment'
                        else: self.error = error.ERRORS( self.line ).ERROR0( self.master )
                    except TypeError:
                        self.string = 'stringcomment'
                        self.error  = ''

            else: self.string = 'string'

        except IndexError: pass

        # returning the new string and error if got
        return self.string, self.idd, self.error