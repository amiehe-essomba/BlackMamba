import numpy
from script.STDIN.LinuxSTDIN                    import bm_configure as bm

cdef class CONVERSION:
    cdef public:
        unsigned long int line 
    cdef:
        str _return_ 
        str str cyan, red, green, yellow, magenta, white, blue, reset

    def __cinit__(self, line):
        self.line           = line 
        self._return_       = ''
        self.orange         = bm.fg.rbg(252, 127, 0 )
        self.cyan           = bm.fg.cyan_L
        self.red            = bm.fg.red_L
        self.green          = bm.fg.rbg(0, 255, 0)
        self.yellow         = bm.fg.rbg(255, 255, 0)
        self.magenta        = bm.fg.magenta_M
        self.white          = bm.fg.white_L
        self.blue           = bm.fg.blue_L
        self.reset          = bm.init.reset
    
    cdef str CONVERSION(self, master):
        cdef:
            list all_Float      = [ numpy.float16, numpy.float32, numpy.float64 ]
            list all_Int        = [ numpy.int8, numpy.int16, numpy.int32, numpy.int64 ]

        if   type( master ) == type( int() )            :   self._return_ = '{}{}integer(){}'.format(bm.fg.blue, self.red, bm.fg.blue)
        elif type( master ) == type( float() )          :   self._return_ = '{}{}float(){}'.format(bm.fg.blue, self.green, bm.fg.blue)
        elif type( master ) == type( bool() )           :   self._return_ = '{}{}boolean(){}'.format(bm.fg.blue, self.cyan, bm.fg.blue)
        elif type( master ) == type( complex() )        :   self._return_ = '{}{}complex(){}'.format(bm.fg.blue, bm.fg.cyan, bm.fg.blue)
        elif type( master ) == type( list() )           :   self._return_ = '{}{}list(){}'.format(bm.fg.blue, self.yellow , bm.fg.blue)
        elif type( master ) == type( tuple() )          :   self._return_ = '{}{}tuple(){}'.format(bm.fg.blue, self.blue, bm.fg.blue)
        elif type( master ) == type( dict() )           :   self._return_ = '{}{}dictionary(){}'.format( bm.fg.blue, self.magenta, bm.fg.blue)
        elif type( master ) == type( str() )            :   self._return_ = '{}{}string(){}'.format(bm.fg.blue, bm.fg.rbg(255,140,100 ), bm.fg.blue)
        elif type( master ) == type( range( 1 ) )       :   self._return_ = '{}{}range(){}'.format(bm.fg.blue, bm.fg.green_L, bm.fg.blue)
        elif type( master ) == type( None )             :   self._return_ = '{}{}none(){}'.format(bm.fg.blue, self.orange, bm.fg.blue)
        elif type( master ) in all_Float                :   self._return_ = '{}{}float(){}'.format(bm.fg.blue, self.green, bm.fg.blue)
        elif type( master ) in all_Int                  :   self._return_ = '{}{}integer(){}'.format(bm.fg.blue, self.red, bm.fg.blue)
        elif type( master ) == type( numpy.array([1]))  :   self._return_ = '{}{}ndarray(){}'.format(bm.fg.blue, bm.fg.rbg(255,165,0), bm.fg.blue)
        else:  self._return_ = 'type not found'

        return self._return_+ bm.init.reset