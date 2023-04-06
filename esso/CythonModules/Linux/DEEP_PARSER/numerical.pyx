from CythonModules.Linux.DEEP_PARSER          import boolean_checking     as BC   
from CythonModules.Linux.DEEP_PARSER          import arithmetic_checking  as AC

cdef class NUMERICAL:
    cdef public :
        dict master 
        unsigned long long int line  
        dict data_base 
    
    cdef :
        dict error, numeric, values
        list boolean_operator, logical_operator, arithmetic_operator

    def __cinit__(self, master, data_base, line):
        self.master         = master
        self.data_base      = data_base 
        self.line           = line 
        self.error          = {"s":None}
        self.numeric        = {"s":None}
        self.values         = {"s":None}

    cpdef ANALYSE(self, str main_string, bint loop = False):
        self.values["s"]            = self.master['all_data']['value']
        self.boolean_operator       = self.master['all_data']['bool_operator']
        self.logical_operator       = self.master['all_data']['logical_operator']
        self.arithmetic_operator    = self.master['all_data']['arithmetic_operator']
        
        if loop is  False: 
            self.numeric["s"], self.error["s"] = BC.NUMERICAL(self.master, self.data_base, self.line).BOOLEAN_CHECKING(
                                        self.values['s'], self.arithmetic_operator, self.logical_operator,
                                        self.logical_operator, main_string)
        else: 
            self.numeric["s"], self.error["s"] = AC.NUMERICAL(self.master, self.data_base, self.line).ARITHMETIC_CHECKING(
                                        self.values["s"], self.arithmetic_operator)
        
        return self.numeric['s'], self.error['s']
