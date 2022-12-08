from script.TRANSPILER.TUPLE import tuples

cdef class DATA:
    cdef public:
        dict master, data_base
        unsigned long long int line 
    cdef:
        dict error, true_data
        list all_data_vars 
        str active_function
        bint is_op
        str operator  
        list vars, vals, ar_ops, lo_ops, bo_ops

    def __cinit__(self,master, data_base, line):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.error          = {"s":None}
        self.active_function= ""
        self.true_data      = {"s":None}

    cpdef SORTING(self):

        cdef :
            signed long int i 
            str key_names
            str numerical_string = ""
        
        self.all_data_vars      = list( self.master.keys() )

        for i, key_names in enumerate( self.all_data_vars ) :
            if key_names != 'if_egal':
                if self.master[ key_names ] is None: pass
                else:
                    self.active_function = key_names
                    break
            else: pass

        if self.active_function == 'all_data': 
            self.true_data['s'] = self.master['all_data'].copy()
            self.is_op          = self.master['if_egal']
            if self.is_op   is True:
                self.vars       = self.master['all_data']['variable'].copy()
                self.vals       = self.master['all_data']['value'].copy()
                self.ar_ops     = self.master['all_data']['arithmetic_operator'].copy()
                self.lo_ops     = self.master['all_data']['logical_operator'].copy()
                self.bo_ops     = self.master['all_data']['bool_operator'].copy()

                for i in range(len( self.vars ) ):
                    numerical_string = numeric( self.vals[i], self.vars[i], self.ar_ops[i], '=',
                            self.data_base, self.line).numeric()
            else: pass
        else: pass 


        return numerical_string

cdef class numeric:
    cdef public :
        list master
        str variable, sep
        list operators 
        dict data_base 
        unsigned long long int line
    cdef:
        dict error 

    def __cinit__(self, master=[], variable="", operators=[], sep="", data_base={}, line=0):
        self.master             = master
        self.variable           = variable
        self.operators          = operators 
        self.data_base          = data_base 
        self.line               = line
        self.error              = {'s':None}
        self.sep                = sep 

    cdef str numeric(self):
        
        cdef:
            signed long i, j
            str string = self.variable + self.sep
            list value  
            dict sub_value
            list  lex
            str str_tuple = ''


        for i in range( len(self.master ) ):
            if list( self.master[i].keys() )[ 0 ] == 'names':
                if self.master[i]['type']  in [None, 'numeric', 'complex']:
                    if i < len( self.master )-1: 
                        string += self.master[i]['numeric'][ 0 ] + self.operators[i]
                    else: string += self.master[i]['numeric'][ 0 ] 
                elif self.master[i]['type']  in ['tuple']:
                    lex, self.error['s'] = tuples.TUPLE(self.master[i], self.data_base, self.line).MAIN_TUPLE(main_string='')
                    for j in range( len( lex ) ):
                        if j < len(lex)-1:
                            str_tuple += numeric( lex[j]['value'][ 0 ], '', lex [j]['arithmetic_operator'],'',
                                self.data_base, self.line).numeric()+','
                        else:
                            str_tuple += numeric( lex[j]['value'][ 0 ], '', lex[j]['arithmetic_operator'],'',
                                self.data_base, self.line).numeric()
                    string += '(' + str_tuple+')'
                else: pass 
            else:
                value       = self.master[i]['values']
                sub_value   = value[1][0]
                string     += value[0]
                if sub_value['type'] in [None, 'numeric', 'complex']:
                    if i  < len( self.master )-1: string +=self.master[i]['operators'][0]+sub_value['numeric'][ 0 ] + self.operators[i]
                    else: string += self.master[i]['operators'][0]+sub_value['numeric'][ 0 ]
                else: pass
             
        return string 

class logical:
    pass 
class boolean:
    pass