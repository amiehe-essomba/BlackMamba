from colorama import Fore, Style

cdef class GetValue:
    cdef :
        public list    listOfValue
        public int     line
    
    cdef :
        int     length
        float   value
        float   result
        str     error
        str     magenta
        str     green
        str     white
        str     red
        str     yellow
        str     cyan
        str     blue
        str     reset
        str     type1
        str     type2
        str     type3


    def __init__(self, listOfValue, line = 0 ) :
        self.listOfValue                = listOfValue
        self.line                       = line


    cpdef mean( self, int length ):
        value   = 0.0
        error   = ''
        red     = Fore.RED
        magenta = Fore.MAGENTA
        green   = Fore.GREEN
        white   = Fore.WHITE
        yellow  = Fore.YELLOW
        cyan    = Fore.CYAN
        blue    = Fore.BLUE
        reset   = Style.RESET_ALL

        type1   = '{}a float(){}'.format(green, reset)
        type2   = '{}an integer(){}'.format(red, reset)
        type3   = '{}a boolean(){}'.format(cyan, reset)

        for _value_ in self.listOfValue :
            try:
                value += _value_
            except TypeError:

                error  = '{}{} : {}{} {}is not {}, {}, or {} {}type.'.format(magenta, 'TypeError', blue, _value_, magenta, type1, type2, type3, magenta)
                error += ' {}line : {}{} {}in function mean( ). {}'.format(white, yellow, self.line, green, reset)
                break
            else: pass

        if not error:
            result = value / float( length )
        else: result = None

        return result, error

    cpdef sum( self ):

        value   = 0.0
        error   = ''
        red     = Fore.RED
        magenta = Fore.MAGENTA
        green   = Fore.GREEN
        white   = Fore.WHITE
        yellow  = Fore.YELLOW
        cyan    = Fore.CYAN
        blue    = Fore.BLUE
        reset   = Style.RESET_ALL

        type1   = '{}a float(){}'.format(green, reset)
        type2   = '{}an integer(){}'.format(red, reset)
        type3   = '{}a boolean(){}'.format(cyan, reset)

        for _value_ in self.listOfValue:
            try:
                value += _value_
            except TypeError:

                error  = '{}{} : {}{} {}is not {}, {}, or {} {}type.'.format(magenta, 'TypeError', blue, _value_, magenta, type1, type2, type3, magenta)
                error += ' {}line : {}{} {}in function sum( ). {}'.format(white, yellow, self.line, green, reset)
                break
            else: pass


        if not error: result = value
        else: result = None

        return result, error