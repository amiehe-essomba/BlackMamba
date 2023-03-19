import time, sys
from script.STDIN.LinuxSTDIN        import bm_configure as bm

cdef hor(m, n, p):
    cdef:
        str s1 = chr(9646)
        str s2 = bm.fg.rbg(255, 0, 255)+chr(9646)+bm.init.reset
    bar = s2*m + s1*(n-m) + bm.init.bold + f"  {m*p}/100%"+bm.init.reset

    return bar 
cdef ver(m, n, p):
    cdef:
        str s1 =  chr(9632)  
        str s2 =  bm.fg.rbg(255, 0, 0)+chr(9632)+bm.init.reset
    bar = s2*m + s1*(n-m)+ bm.init.bold + f"  {m*p}/100%"+bm.init.reset
    return bar 

cdef simple(m, n, p):
    cdef:
        str s = "#"

    bar = "["+ s*m + " "*(n-m)+"]"+ f"  {m*p}/100%"
    return bar 

cdef class progress:
    cdef public:
        unsigned long int start, stop

    def __cinit__(self, start, stop):
        self.start  = start
        self.stop   = stop
    cpdef bar(self,  unsigned int style = 0):
        cdef:
            unsigned long int i, n, m 
            str bar = ""

        if (self.stop - self.start) % 4 == 0: 
            n = int((self.stop - self.start)/ 4)
            m = 4
        elif (self.stop - self.start) % 3 == 0: 
            n = int((self.stop - self.start)/ 3)
            m = 3
        elif (self.stop - self.start) % 5 == 0: 
            n = int((self.stop - self.start)/ 5)
            m = 5
        elif (self.stop - self.start) % 7 == 0: 
            n = int((self.stop - self.start) / 7)
            m = 7
        else:
            n = (self.stop - self.start) 
            m = 1

        for i in range(self.start, self.stop):
            time.sleep(0.1)
            width = (i+1)/m

            if style == 0: bar = simple(width, n, m)
            elif style == 1: bar = hor(width, n, m)
            else: bar = ver(width, n, m)

            sys.stdout.write(bm.move_cursor.LEFT(pos=1000)+bar)
            sys.stdout.flush()
        print
 