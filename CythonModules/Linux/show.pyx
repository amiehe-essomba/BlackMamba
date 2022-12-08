import numpy as np 
from script.STDIN.LinuxSTDIN     import bm_configure as bm
from script.STDIN.LinuxSTDIN     import ascii


cdef run( master):
    if type(master) in [type(int()), type(float()), type(complex()) , type(bool()), type(None)]: master = str(master)
    elif type(master) == type(list()): master = str( LIST(master).LIST())
    elif type(master) == type(tuple()): master = str( TUPLE(master).TUPLE())
    elif type(master) == type(str()): master = String( master)
    elif type(master) == type(dict()): master = str( DICT(master).DICT())
    else: pass 

    return bm.words(master, bm.fg.rbg(255, 255, 255)).final()+bm.init.reset

def String( str master):
    if master:
        if len( master ) <= 10: pass
        else: master = master[: 9 ] + '....' + master[-1]
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
            str  string
        try:
            if shape[1] == 1: 
                for j in range(shape[0]):
                    if type(self.master['s'][0]) == type(complex()): string = "( {bm.fg.cyan+str(self.master['s'][0])+bm.init.reset} )"
                    else: string = ""#f"( {run( self.master['s'][0] )} )"
            for i in range(shape[0]):
                pass
        except IndexError:
            pass

            

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
                else: self.final[i] = run( self.master[i] )
        else: pass 

        return self.final


        

