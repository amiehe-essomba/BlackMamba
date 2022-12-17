from script.STDIN.LinuxSTDIN   import ascii as a


cdef sym(unsigned int n):
    return a.parenthesis(n)

cdef class handling:
    cdef public:
        list master:
    def __cinit__(self, master):
        self.master     = master
    cdef lists(self, unsigned int style = 0):
        cdef:
            unsigned long i
            str string = ""

        if self.master:
            for i in r
        else:
            pass


