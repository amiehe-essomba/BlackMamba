cdef extern from "mat.h":
    cdef double SUM( int a[], int n)

cdef class ir:
    cdef: 
        public int a 
        public int n 
    def __cinit__(self, a, n):
        self.a      = a
        self.n      = n

    cpdef ir(self):
        
        return SUM(self.a, self.n)