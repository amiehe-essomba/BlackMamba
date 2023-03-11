import numpy as np 
from script.STDIN.LinuxSTDIN     import bm_configure as bm
from script.STDIN.LinuxSTDIN     import ascii
import pandas as pd
from CythonModules.Linux         import frame
from src.classes.matrix          import checking_2D as c2D


cdef run( master):
    cdef:
        bint table = False
        unsigned long int n
    if type(master) in [type(int()), type(float()), type(complex()) , type(bool()), type(None)]: master = str(master)
    elif type(master) == type(list()): master = str( LIST(master).LIST())
    elif type(master) == type(tuple()): master = str( TUPLE(master).TUPLE())
    elif type(master) == type(str()): master = String( master)
    elif type(master) == type(dict()): master = str( DICT(master).DICT())
    elif type(master) == type(np.array([1])): master, n = ARRAY({"s": master}).ARRAY()
    else: pass 

    return bm.words(master, bm.fg.rbg(255, 255, 255)).final()+bm.init.reset

def String( str master):
    if master:
        if len( master ) <= 20: pass
        else: master = master[: 19 ] + '....' + master[-1]
    else: pass

    return master 

cdef class LIST:
    cdef public:
        list master 
    def __cinit__(self, master):
        self.master = master

    cdef list LIST(self):
        cdef:
            list my_list = []
            list master_init
            unsigned long int ncol, nrow
        
        if self.master:
            if len( self.master ) <= 5: my_list = self.master.copy()
            elif len( self.master ) > 5:
                my_list = self.master[ : 4 ]
                my_list.append('....')
                my_list.append(self.master[ -1 ])

            for i in range(len(my_list)):
                if   type(my_list[i]) in [type(int()), type(float()), type(complex()) , type(bool()), type(None)]: my_list[i] = my_list[i] 
                elif type(my_list[i]) in [type(list())]  : my_list[i] = LIST( my_list[i] ).SubLIST() 
                elif type(my_list[i]) in [type(str())]   : my_list[i] = String( my_list[i] )
                elif type(my_list[i]) in [type(tuple())] : my_list[i] = TUPLE( my_list[i] ).TUPLE() 
                elif type(my_list[i]) in [type(dict())]  : my_list[i] = DICT( my_list[i] ).DICT() 
                elif type(my_list[i]) in [type(np.array([1]))]:
                    master_init, nrow, ncol = c2D.Array( my_list[i] )
                    my_list[i] = LIST( master_init ).SubLIST()
                else: pass 
        else: pass 

        return my_list

    cdef list SubLIST(self):
        cdef:
            list my_list = []
        if self.master:
            if len( self.master ) <= 5: my_list = self.master.copy()
            elif len( self.master ) > 5:
                my_list = self.master[ : 4 ]
                my_list.append('....')
                my_list.append(self.master[ -1 ])

            for i in range(len(my_list)):
                if   type(my_list[i]) in [type(int()), type(float()), type(complex()) , type(bool()), type(None)]: my_list[i] = my_list[i]
                elif type(my_list[i]) in [type(list())]  : my_list[i] = LIST( my_list[i] ).LIST() 
                elif type(my_list[i]) in [type(str())]   : my_list[i] = String( my_list[i] )
                elif type(my_list[i]) in [type(tuple())] : my_list[i] = TUPLE( my_list[i] ).TUPLE() 
                elif type(my_list[i]) in [type(dict())]  : my_list[i] = DICT( my_list[i] ).DICT() 
                elif type(my_list[i]) in [type(np.array([1]))]:
                    master_init, nrow, ncol = c2D.Array( my_list[i] )
                    my_list[i] = LIST( master_init ).LIST()
                else: pass
        return my_list

cdef class TUPLE:
    cdef public:
        tuple master 
    def __cinit__(self, master):
        self.master = master 
    cdef tuple TUPLE(self):
        cdef:
            list my_list = []
        if self.master:
            if len( self.master ) <= 5: my_list = list(self.master)
            elif len( self.master ) > 5: 
                my_list = list(self.master[ : 4 ])
                my_list.append('....')
                my_list.append(self.master[ -1 ])

            for i in range(len(my_list)):
                if   type(my_list[i]) in [type(int()), type(float()), type(complex()) , type(bool()), type(None)]: my_list[i] = my_list[i] 
                elif type(my_list[i]) == type(list())    : my_list[i] = LIST(my_list[i] ).LIST() 
                elif type(my_list[i]) in [type(str())]   : my_list[i] = String( my_list[i] )
                elif type(my_list[i]) in [type(tuple())] : my_list[i] = TUPLE( my_list[i] ).SubTUPLE() 
                elif type(my_list[i]) in [type(dict())]  : my_list[i] = DICT( my_list[i] ).DICT() 
                else: pass 
        else: pass

        return tuple(my_list)
    
    cdef tuple SubTUPLE(self):
        cdef:
            list my_list = []
        if self.master:
            if len( self.master ) <= 5: my_list = list(self.master)
            elif len( self.master ) > 5: 
                my_list = list(self.master[ : 4 ])
                my_list.append('....')
                my_list.append(self.master[ -1 ])

            for i in range(len(my_list)):
                if   type(my_list[i]) in [type(int()), type(float()), type(complex()) , type(bool()), type(None)]: my_list[i] = my_list[i] 
                elif type(my_list[i]) == type(list())    : my_list[i] = LIST(my_list[i] ).LIST() 
                elif type(my_list[i]) in [type(str())]   : my_list[i] = String( my_list[i] )
                elif type(my_list[i]) in [type(tuple())] : my_list[i] = TUPLE( my_list[i] ).TUPLE() 
                elif type(my_list[i]) in [type(dict())]  : my_list[i] = DICT( my_list[i] ).DICT() 
                else: pass 
        else: pass

        return tuple(my_list)

cdef class DICT:
    cdef public:
        cdef master 
    def __cinit__(self, master):
        self.master = master
    cdef dict DICT(self):
        cdef :
            dict my_dict ={}
            list my_list = list(self.master.items())
            tuple my_tuple = ()
            dict s = {'s':None}

        if my_list:
            if len(my_list) <= 5: pass
            else:
                my_tuple = my_list[-1]
                my_list  = my_list[: 4 ]
                my_list.append('....')
                my_list.append(my_tuple)
            
            for i in range(len(my_list)):
                s['s'] = my_list[i][1]
                if type(s['s'] ) in [type(int()), type(float()), type(complex()) , type(bool()), type(None)]: my_list[i] = (my_list[i][0], s['s']  ) 
                elif type(s['s'] ) == type(list())    : my_list[i] = (my_list[i][0], LIST( s['s']  ).LIST() )
                elif type(s['s'] ) in [type(str())]   : my_list[i] = (my_list[i][0], String( s['s']  ) )
                elif type(s['s'] ) in [type(tuple())] : my_list[i] = (my_list[i][0], TUPLE( s['s']  ).TUPLE() ) 
                elif type(s['s'] ) in [type(dict())]  : my_list[i] = (my_list[i][0], DICT( s['s']  ).SubDICT() )
                else: pass 
        else: pass

        return dict(my_list)
    
    cdef dict SubDICT(self):
        cdef :
            dict my_dict ={}
            list my_list = list(self.master.items())
            tuple my_tuple = ()
            dict s = {'s':None}

        if my_list:
            if len(my_list) <= 5: pass
            else:
                my_tuple = my_list[-1]
                my_list  = my_list[: 4 ]
                my_list.append('....')
                my_list.append(my_tuple)
            
            for i in range(len(my_list)):
                s['s'] = my_list[i][1]
                if type(s['s'] ) in [type(int()), type(float()), type(complex()) , type(bool()), type(None)]: my_list[i] = (my_list[i][0], s['s'] )
                elif type(s['s'] ) == type(list())    : my_list[i] = (my_list[i][0], LIST( s['s']  ).LIST() ) 
                elif type(s['s'] ) in [type(str())]   : my_list[i] = (my_list[i][0], String( s['s']  ) )
                elif type(s['s'] ) in [type(tuple())] : my_list[i] = (my_list[i][0], TUPLE( s['s']  ).TUPLE()  )
                elif type(s['s'] ) in [type(dict())]  : my_list[i] = (my_list[i][0],  DICT( s['s']  ).DICT() )
                else: pass
        else: pass

        return dict(my_list)

cdef class ARRAY:
    cdef public :
        dict master 
    def __cinit__(self, master):
        self.master = master
    cdef ARRAY(self):
        cdef:
            list shape = list( self.master['s'].shape)
            list brackets = ascii.parenthesis('2')
            unsigned long int nrow, ncol
            list master_init 
            unsigned long int i, j, k, max_ = 0, m = 0
            list store = []
            str string = "\n[", str_
            list store_
        
        master_init, nrow, ncol, store_ = c2D.Array( self.master['s'] )
        
        for i in range(len(master_init)):
            if type(master_init[i]) == type(list()):
                for j in range(len(master_init[i])):
                    if max_ > len(str(master_init[i][j])): pass 
                    else: max_ = len(str(master_init[i][j])) 
                store.append(max_)
            else: store.append( len( str( master_init[i] ) ) )

        max_ = max(store) 
        for i in range(len(master_init)):
            if type( master_init[i]) == type(list()):
                if i == 0: string += "["
                else: string += " ["
                for j in range( len( master_init[i] ) ):
                    if type(master_init[i][j]) not in [type(list()), type(tuple())]:
                        string += " "*(max_-len(str(master_init[i][j]))) + str(master_init[i][j])
                        if j < len(master_init[i])-1: string += " "
                        else: string += "]"
                    else:  str_, k = ARRAY({"s" : np.array(master_init[i])}).subARRAY1()
                
                if i < len(master_init)-1: 
                    string += "\n" 
                    m += 1
                else: string += "]"
            else:
                string += " "*(max_-len(str(master_init[i]))) + str(master_init[i])
                if i < len(master_init)-1: string += " " 
                else: string += "]"
        
        return string,  m

    cdef subARRAY1(self):
        cdef:
            list shape = list( self.master['s'].shape)
            list brackets = ascii.parenthesis('2')
            unsigned long int nrow, ncol
            list master_init 
            unsigned long int i, j, k, max_ = 0, m = 0
            list store = [], store_
            str string = "\n["

        master_init, nrow, ncol, store_ = c2D.Array( self.master['s'] )
        
        for i in range(len(master_init)):
            if type(master_init[i]) == type(list()):
                for j in range(len(master_init[i])):
                    if max_ > len(str(master_init[i][j])): pass 
                    else: max_ = len(str(master_init[i][j])) 
                store.append(max_)
            else: store.append( len( str( master_init[i] ) ) )

        max_ = max(store) 
        for i in range(len(master_init)):
            if type( master_init[i]) == type(list()):
                if i == 0: string += "["
                else: string += " ["
                for j in range( len( master_init[i] ) ):
                    if type(master_init[i][j]) not in [type(list()), type(tuple())]:
                        string += " "*(max_-len(str(master_init[i][j]))) + str(master_init[i][j])
                        if j < len(master_init[i])-1: string += " "
                        else: string += "]"
                    else:  str_, k = ARRAY({"s" : np.array(master_init[i])}).subARRAY()
                
                if i < len(master_init)-1: 
                    string += "\n" 
                    m += 1
                else: string += "]"
            else:
                string += " "*(max_-len(str(master_init[i]))) + str(master_init[i])
                if i < len(master_init)-1: string += " " 
                else: string += "]"
        
        return string, m


cdef class show:
    cdef public:
        list master 
    cdef:
        str error 
        dict final
    def __cinit__(self, master) :
        self.master = master[0]
        self.error  =  ""
        self.final  = {}
    
    cpdef dict Print(self, unsigned long integer = 0):
        if self.master: 
            for i in range(len(self.master)):
                if type(self.master[i]) == type(complex()): self.final[i] = bm.fg.cyan+str(self.master[i])+bm.init.reset
                elif type(self.master[i]) == type(pd.DataFrame({"s":[1,2]})): 
                    self.final[i] = frame.FRAME({"s": self.master[i], 'id':list(self.master[i].index)}, 1).FRAME(False, 'DataFrame', True, True)
                else: self.final[i] = run( self.master[i] )
        else: pass 
        return self.final


        

