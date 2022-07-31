"""
module used to analyse main string and make it comment if
the symbol < # > is used at the beginning of each line.
to make line a comment line is simple, set < # > at the beginning like this

# that's is a comment line

"""

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

        self.master, self.error = self.control.DELETE_SPACE( self.master )
        try:
            # if the first character of master if < # > the line is a comment line and then string takes < comment >
            # value , it means that this line will be not exercuted,
            # if string takes < string > value this will be exercuted by the lexer and the tokens will be
            # produiced by the lexer to be analysing by the perxer

            if self.master[ 0 ] in self.char:
                self.string     = 'comment'
            else: self.string   = 'string'

        except IndexError: pass

        # returning the new string and error if got
        return self.string, self.error

