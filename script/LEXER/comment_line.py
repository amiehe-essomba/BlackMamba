"""
module used to analyse main string and make it comment if
the symbol < # > is used at the beginning of each line.
to make line a comment line is simple, set < # > at the beginning like this

# that's is a comment line

"""

from statement.error import error
from script import  control_string

class COMMENT_LINE:
    def __init__(self,
        master      : str,      # concatenate main string
        data_base   : dict,     # the data base
        line        : int       # current line
        ):

        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.char               = [ '#' ]

    def COMMENT( self ):
        self.string             = ''
        self.error              = None
        self.idd                = None

        self.master, self.error = self.control.DELETE_SPACE( self.master )
        try:
            # if the first character of master if < # > the line is a comment line and then string takes < comment >
            # value , it means that this line will be not exercuted,
            # if string takes < string > value this will be exercuted by the lexer and the tokens will be
            # produiced by the lexer to be analysing by the perxer

            for i, s in enumerate(self.master):
                if s == '#':
                    self.idd = i
                    break
                else: pass

            if self.idd is not None:
                if self.idd == 0: self.string = 'comment'
                else:
                    self.ns, self.err = self.control.DELETE_SPACE(self.master[ : self.idd])
                    if self.err is None: self.string = 'stringcomment'
                    else: self.error = error.ERRORS( self.line ).ERROR0( self.master )
            else: self.string = 'string'

        except IndexError: pass

        # returning the new string and error if got
        return self.string, self.idd, self.error

