from rich import print 
from rich.table import table, Column

cdef class TAB:
    cdef public:
        str title, caption
        unsigned long int width
        bint expand
    def __cinit__(self):
        pass
    cpdef tab(self, unsigned int id, str title_justify, str style, str title_style, 
        str cation_style, unsigned int m_width, unsigned int ratio)