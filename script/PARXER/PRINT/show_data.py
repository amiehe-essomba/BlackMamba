""" small code wrote to print values on the screen using key word < print * > 
    *   SHOW used to print something without using the keyword < print * >
    *   but it recommended to use print to view computed data.
    *   taking habbits to use print.
Returns:
    no returned values
"""
from    urllib.parse import parse_qs
from    script.STDIN.LinuxSTDIN    import bm_configure as bm
import numpy

class SHOW :
    def __init__(self,
                    master      : any,              # master can take any value (list, tuple, .....)
                    data_base   : dict,             # data base
                    key         : bool              # key to print or not value, if key == False print is activated
                                                    # else print is set on False. in the program to print value we need to use
                                                    # | print * something |, else anything will no appear on the screen.
                 ):
        self.master         = master
        self.key            = key
        self.data_base      = data_base
        self.cyan           = bm.fg.cyan_L
        self.red            = bm.fg.red_L
        self.green          = bm.fg.green_L
        self.yellow         = bm.fg.yellow_L
        self.magenta        = bm.fg.magenta_M
        self.white          = bm.fg.white_L
        self.blue           = bm.fg.blue_L
        self.orange         = bm.fg.rbg(252, 127, 0 )
        self.reset          = bm.init.reset

    def SHOW(self, 
             loop : bool = False        # for loop statement ( for, while ), default value is False
             ):
        # get master type
        self.type       = type( self.master )
        self.color      = ''

        # calor set in function of the master type
        self.color      = SHOW( self.type, self.data_base, self.key ).TYPE()

        # convert master to a string()
        self.master     = str( self.master )

        self.string2    = bm.init.bold+'{}{}{}'.format(self.color, self.master, self.reset)
        self.string1    = bm.init.bold+'{}[{} result{} ]{} : {}'.format( self.blue, self.orange, self.blue,  self.white, self.reset )

        if self.type == type( str() ):
            try:
                if self.master[ 0 ] not in [ '"', "'"]:
                    if self.data_base[ 'irene' ] is None:
                        self.string2 = "{}'".format(self.color) + self.string2 + "{}'".format( self.color )
                    else: self.data_base[ 'irene' ] = None
                else: pass
            except IndexError :
                self.string2 = '{}"'.format(self.color) + '{}"'.format( self.color )
        else: pass

        self.string2 = LineFeed(self.string2, self.type)
        self.string = bm.init.bold+self.string1 + self.string2

        # print master if key is set on False
        if loop is False:
            #self.string += bm.init.reset
            if self.key == False:  print( '{}{}\n'.format(self.string, bm.init.reset ) )
            else: pass
        else:
            #self.string += bm.init.reset
            if self.key == False:  print( f"{self.string}{bm.init.reset}" )
            else: pass

    def PRINT(self):
        # i build this module for the loop < for and while >
        # the structural conditional and loop do not use the same print function
        # however as you can see it a little bit similar to the show function

        # get type
        self.type   = type( self.master )

        # get color
        self.color  = SHOW( self.type, self.data_base, self.key ).TYPE()

        # put master as a string()
        self.master = str( self.master )

        self.string = '{}{}{}'.format(self.color, self.master, self.reset)

        if self.type == type( str() ):
            try:
                if self.master[ 0 ] not in [ '"', "'"]:
                    if self.data_base[ 'irene' ] is None:
                        self.string = '{}"'.format( self.color ) + self.string + '{}"'.format( self.color )
                    else: self.data_base[ 'irene' ] =  None
                else: pass
            except IndexError:  self.string = '{}"'.format(self.color) + '{}"'.format( self.color )
        else: pass

        # string modified in function of the type of master object.
        return self.string

    def TYPE(self):

        # i used this module to attribute a color in function of the type of master
        # it means that if type( master ) == list() , when we'll print master on the
        # screen the color of the string will be yellow

        self._return_       = ''
        self.all_Float      = [ numpy.float16, numpy.float32, numpy.float64 ]
        self.all_Int        = [ numpy.int8, numpy.int16, numpy.int32, numpy.int64 ]

        if   self.master == type( list())       :   self._return_ = bm.fg.rbg(255, 255, 0)
        elif self.master == type( dict() )      :   self._return_ = self.magenta
        elif self.master == type( int() )       :   self._return_ = self.red
        elif self.master == type( float() )     :   self._return_ = bm.fg.rbg(0, 255, 0)
        elif self.master == type( tuple() )     :   self._return_ = self.blue
        elif self.master == type( bool() )      :   self._return_ = self.cyan
        elif self.master == type( complex() )   :   self._return_ = bm.fg.cyan
        elif self.master == type( None )        :   self._return_ = bm.fg.rbg(252, 127, 0 )
        elif self.master == type( str() )       :   self._return_ = bm.fg.rbg(255,140,100 )
        elif self.master == type( range(2) )    :   self._return_ = self.green
        elif self.master in self.all_Float      :   self._return_ = bm.fg.rbg(0, 255, 0)
        elif self.master in self.all_Int        :   self._return_ = self.red
        elif self.master == type(numpy.array([0])): self._return_ = bm.fg.rbg(255,165,0)
        else:                                       self._return_ = bm.fg.rbg(255, 0, 0)

        return self._return_

def LineFeed( string : str, typ : any):
    if typ in [type(str()), type(numpy.array([0]))]:
        if '\n' in string:
            if '\n' == string[0]: pass 
            else: string = '\n'+string 
        else: pass 
    else: pass
    
    return string
    
    
