from script.STDIN.LinuxSTDIN       import ascii as a
from script.STDIN.LinuxSTDIN       import bm_configure as bm
from CythonModules.Windows         import fileError as fe 
import pandas as pd

cdef str head(unsigned long int nraw,  unsigned long int ncol, list data, unsigned int max_id = 1, 
                            bint show_id = False, bint s = False):
    cdef:
        str chaine =  "" 
        unsigned long i

    for i in range(nraw):
        if i != nraw-1: chaine += a.frame(s)["h"]*data[i]+a.frame(s)['m1']
        else:chaine += a.frame(s)["h"]*data[i]
    chaine = a.frame(s)["ul"]+chaine+a.frame(s)["ur"]
    
    if show_id is False: pass 
    else: chaine = " "*(max_id+1) + chaine

    return chaine

cdef str top(unsigned long int nraw,  unsigned long int ncol, list data, unsigned int max_id = 1, 
                            bint show_id = False, unsigned int style = 1, bint s = False):
    cdef:
        str chaine = ""
        unsigned long i
    
    for i in range(nraw):
        if i != nraw-1: chaine += a.frame(s)["h"]*data[i]+a.frame(s)['m3']
        else:chaine += a.frame(s)["h"]*data[i]
    

    if show_id is False: chaine = a.frame(s)["vl"]+chaine+a.frame(s)["vr"]
    else:
        chaine = a.frame(s)['m3']+chaine+a.frame(s)["vr"]
        if style == 0:
            chaine = a.frame(s)["ul"] + a.frame(s)["h"] * max_id + chaine
        else:
            chaine = a.frame(s)["vl"] + a.frame(s)["h"] * max_id + chaine
            
    return chaine

cdef str bottom(unsigned long int nraw,  unsigned long int ncol, list data, unsigned int max_id = 1, 
                bint show_id = False, bint s = False):
    cdef:
        str chaine = ""
        unsigned long i
    
    for i in range(nraw):
        if i != nraw-1: chaine += a.frame(s)["h"]*data[i]+a.frame(s)['m2']
        else:chaine += a.frame(s)["h"]*data[i]
    
    if show_id is False: chaine = a.frame(s)["dl"]+chaine+a.frame(s)["dr"]
    else: 
        chaine = a.frame(s)['m2']+chaine+a.frame(s)["dr"]
        chaine =  a.frame(s)["dl"]+ a.frame(s)["h"]*max_id + chaine

    return chaine

cdef midle(unsigned long int nraw,  unsigned long int ncol, list data, dict all_data, dict all_len, list keys,
                        unsigned int max_id = 1, bint show_id = False, list frame_id_data = [], bint s = False):
    cdef:
        str chaine = ""
        unsigned long i, j, n,  m
        list sub_len 
    
    if show_id is False: chaine += a.frame(s)['v']
    else: chaine += " "*(max_id+1) +a.frame(s)['v']

    for i in range(nraw):
        n = data[i]-len(keys[i])
        chaine += " "*n+bm.words(str(keys[i]), bm.fg.rbg(255, 255, 255)).final()+bm.init.reset +a.frame(s)['v']
        
    chaine += '\n'+top(nraw, ncol, data, max_id, show_id, 0, s)+"\n"


    for j in range(ncol):
        sub_len = []
        chaine += a.frame(s)['v']
        if show_id is False: pass
        else: 
            m = max_id - len(frame_id_data[j])
            chaine +=" "*m+bm.words(frame_id_data[j], bm.fg.rbg(255, 255, 255)).final()+bm.init.reset+a.frame(s)['v']

        for i in range(nraw):
           n = data[i]-all_len[i][j]
           chaine += " "*n+bm.words(all_data[i][j], bm.fg.rbg(255, 255, 255)).final()+bm.init.reset +a.frame(s)['v']
        if j != ncol -1: chaine += '\n'+top(nraw, ncol, data, max_id, show_id, 1, s)+"\n" 
        else: pass

    return chaine

cdef class FRAME:
    cdef public:
        dict master 
        unsigned long int line
    cdef:
        dict error 
    def __cinit__(self, master, line):
        self.master = master.copy()
        self.line   = line
        self.error  = {"s":None}
    
    cpdef FRAME(self, bint Frame = True, str _typ_ = "dictionary", bint show_index = False, bint _s_ = False):
        cdef:
            list keys, values, typ
            unsigned long length, i, j
            list store = []
            unsigned long l
            dict data = {}
            dict str_len = {}
            str chaine = bm.fg.rbg(255,255,255)
            dict pan = {'s':None}
            unsigned long int nraw, ncol
            list frame_id, frame_id_
            unsigned long int frame_id_max 
            list _values_

        typ=[type(None), type(int()), type(float()), type(bool()), type(str())]

        if type(self.master) == type(dict()) :
            if _typ_ == 'dictionary':
                keys = list(self.master.keys())
                values = list(self.master.values())
            else:
                values = []
                keys = list(self.master['s'].keys())

                for i in range(len(keys)):
                    values.append(self.master['s'][keys[i]].tolist())
                frame_id = self.master['id']
                self.master = {}

            length = len(keys)

            if len(keys) <= 15:
                if values:
                    for i in range(length):
                        str_len[i] = []
                        try:
                            values[i] = list(values[i])
                            if type(values[i]) == type(list()):
                                if len(values[i]) == len(values[0]):
                                    if values[i]:
                                        l = len(keys[i])
                                        for j in range(len(values[i])):
                                            if type(values[i][j]) in typ: 
                                                data[i] = values[i]
                                                str_len[i].append( len( str(values[i][j]) ) )
                                                self.master[keys[i]] = list(values[i])
                                                if len(str(str(values[i][j]))) > l: l = len(str(str(values[i][j])))
                                                else: pass 
                                                values[i][j] = str(values[i][j])
                                            else: 
                                                self.error['s'] = ERRORS(self.line).ERROR2(i, j)
                                                break
                                        if self.error['s'] is None: store.append(l)
                                        else: break
                                    else: 
                                        self.error['s'] = ERRORS(self.line).ERROR1(i, 'c')
                                        break 
                                else:
                                    self.error['s'] = ERRORS(self.line).ERROR3() 
                                    break
                            else: 
                                self.error['s'] = ERRORS(self.line).ERROR4(i) 
                                break
                        except (TypeError, ValueError): 
                            self.error['s'] = ERRORS(self.line).ERROR4(i) 
                            break

                    if self.error['s'] is None:
                        if len(values[0]) <=15:
                            if Frame is True: pan['s'] = pd.DataFrame(self.master)
                            else:
                                frame_id_ = [len(str(x)) for x in frame_id]
                                frame_id_max = max(frame_id_)
                                frame_id_ = [str(x) for x in frame_id]
                                chaine += head(length, len(data[0]), store, frame_id_max, show_index, _s_)+"\n"
                                chaine += midle(length, len(data[0]), store, data, str_len, keys, frame_id_max, show_index, frame_id_, _s_)+"\n"
                                chaine += bottom(length, len(data[0]), store, frame_id_max, show_index, _s_)
                                pan['s'] = pd.DataFrame(self.master)
                        else: pass 
                    else:pass      
                else: self.error['s'] = ERRORS( self.line).ERROR0()
            else: pass

        if _s_ is False: return pan['s'], chaine+bm.init.reset, self.master, self.error['s']
        else: return f"\n{chaine}"+bm.init.reset

cdef class ERRORS:
    cdef public:
        unsigned long int line 
    cdef:
        str red, cyan, white, yellow, m, reset, error, green
    
    def __cinit__(self,line):
        self.line = line
        self.error= ""
        self.red = bm.fg.rbg(255, 0, 0)
        self.yellow = bm.fg.rbg(255, 255, 0)
        self.cyan = bm.fg.rbg(255, 0, 255)
        self.m = bm.fg.rbg(0, 255, 255)
        self.white = bm.fg.rbg(255, 255, 255)
        self.green = bm.fg.rbg(0, 255, 0)
        self.reset = bm.init.reset

    cdef ERROR0(self):
        cdef:
            str err 
        
        err = "{}line : {}{}.".format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+"{}data.frame {}bad input data. ".format( self.red, self.white )+err

        return self.error+self.reset

    cdef ERROR1(self,  unsigned long int nrow, char c="r"):
        cdef:
            str err 
        
        if c=='r':
            err = "{}nrow = {}{}. {}line : {}{}.".format(self.white, self.red, nrow, self.white, self.yellow, self.line)
        else:
            err = "{}ncol = {}{}. {}line : {}{}.".fomat(self.white, self.red, nrow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+"Some lists in {}data.frame {}contain any value. ".format(self.white, self.red, self.white)+err

        return self.error+self.reset
    
    cdef ERROR2(self, unsigned long int nraw, unsigned long int ncol):
        cdef:
            str err 
            str chaine 

        chaine = self.red+"an interger(),"+self.green+" a float(),"+self.m+" a string(),"+self.cyan+" a boolean(),"+self.yellow+" or a none()"+self.reset
        
        err = "{}is not an {} {}type. {}line : {}{}.".format(self.white, chaine, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+"{}value in nraw = {}{} {}and ncol = {}{} ".format(self.white, self.red, 
                                                                        nraw, self.white, self.red, ncol)+err

        return self.error+self.reset

    cdef ERROR3(self):
        cdef:
            str err 
            
        err = "{}have not the same length. {}line : {}{}.".format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+"{}all columns in {}data.frame ".format(self.white, self.red )+err

        return self.error+self.reset
    
    cdef ERROR4(self, unsigned long int ncol):
        cdef:
            str err 
            str chaine 

        chaine = self.cyan+"a list()"+self.m+" or a tuple()"+self.reset
        
        err = "{}is not an {} {}type. {}line : {}{}.".format(self.white, chaine, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+"{}data.frame ncol = {}{} ".format( self.red, self.cyan,  ncol)+err

        return self.error+self.reset