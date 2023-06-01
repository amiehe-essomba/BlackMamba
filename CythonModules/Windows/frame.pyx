import pandas as pd
import numpy 
from script.STDIN.LinuxSTDIN       import ascii as a
from script.STDIN.LinuxSTDIN       import bm_configure as bm
from CythonModules.Windows         import fileError as fe 
from windows                       import screenConfig
from CythonModules.Windows         import array_to_list        as atl

cdef str head(unsigned long int nraw,  unsigned long int ncol, list data, unsigned int max_id = 1, 
                            bint show_id = False, bint s = False, bint split =False):
    cdef:
        str chaine =  "" 
        unsigned long i, j = 0

    for i in range(nraw):
        if split is False : 
            if i != nraw-1: chaine += a.frame(s)["h"]*data[i]+a.frame(s)['m1']
            else: chaine += a.frame(s)["h"]*data[i]
        else:
            if i != nraw-1: chaine += a.frame(s)["h"]*data[i]+a.frame(s)['ur']
            else: chaine += " " * 2 + a.frame(s)["ul"] + a.frame(s)["h"]*data[i]

    chaine = a.frame(s)["ul"]+chaine+a.frame(s)["ur"]
    
    if show_id is False: pass 
    else: chaine = " "*(max_id+1) + chaine

    return chaine

cdef str top(unsigned long int nraw,  unsigned long int ncol, list data, unsigned int max_id = 1, 
                            bint show_id = False, unsigned int style = 1, bint s = False, bint split = False):
    cdef:
        str chaine = ""
        unsigned long i, j=0
    
    for i in range(nraw):
        if split is False:
            if i != nraw-1: chaine += a.frame(s)["h"]*data[i]+a.frame(s)['m3']
            else: chaine += a.frame(s)["h"]*data[i]
        else:
            if i != nraw-1: chaine += a.frame(s)["h"]*data[i]+a.frame(s)['vr']
            else: chaine += " " * 2 + a.frame(s)["vl"] + a.frame(s)["h"]*data[i]
        
    if show_id is False: chaine = a.frame(s)["vl"]+chaine+a.frame(s)["vr"]
    else:
        chaine = a.frame(s)['m3']+chaine+a.frame(s)["vr"]
        if style == 0:
            chaine = a.frame(s)["ul"] + a.frame(s)["h"] * max_id + chaine
        else:
            chaine = a.frame(s)["vl"] + a.frame(s)["h"] * max_id + chaine
            
    return chaine

cdef str bottom(unsigned long int nraw,  unsigned long int ncol, list data, unsigned int max_id = 1, 
                bint show_id = False, bint s = False, bint split = False):
    cdef:
        str chaine = ""
        unsigned long i, j=0
    
    for i in range(nraw):
        if split is False:
            if i != nraw-1: chaine += a.frame(s)["h"]*data[i]+a.frame(s)['m2']
            else:chaine += a.frame(s)["h"]*data[i]
        else:
            if i != nraw-1: chaine += a.frame(s)["h"]*data[i]+a.frame(s)['dr']
            else: chaine += " " * 2 + a.frame(s)["dl"] + a.frame(s)["h"]*data[i]
    
    if show_id is False: chaine = a.frame(s)["dl"]+chaine+a.frame(s)["dr"]
    else: 
        chaine = a.frame(s)['m2']+chaine+a.frame(s)["dr"]
        chaine =  a.frame(s)["dl"]+ a.frame(s)["h"]*max_id + chaine

    return chaine

cdef str bottom_(unsigned long int nraw,  unsigned long int ncol, list data, unsigned int max_id = 1, 
                bint show_id = False, bint s = False, bint split = False):
    cdef:
        str chaine = ""
        unsigned long i, j=0
    
    for i in range(nraw):
        if split is False:
            if i != nraw-1: chaine += a.frame(s)["h"]*data[i]+a.frame(s)['m1']
            else:chaine += a.frame(s)["h"]*data[i]
        else:
            if i != nraw-1: chaine += a.frame(s)["h"]*data[i]+a.frame(s)['ur']
            else:chaine += " " * 2 + a.frame(s)["ul"]+  a.frame(s)["h"]*data[i]
    
    if show_id is False: chaine = a.frame(s)["ul"]+chaine+a.frame(s)["ur"]
    else: 
        chaine = a.frame(s)['m1']+chaine+a.frame(s)["ur"]
        chaine =  a.frame(s)["ul"]+ a.frame(s)["h"]*max_id + chaine

    return chaine

cdef midle(list nrow,  unsigned long int ncol, list data, dict all_data, dict all_len, list keys,
            unsigned int max_id = 1, bint show_id = False, list frame_id_data = [], 
            bint s = False, bint step_nrow = False, bint step_col = False, unsigned long int limit = 0, 
            bint head = False, bint tail = False):
    cdef:
        str chaine = ""
        unsigned long long int i, j,  m, h, LEN = 0, MAX = 12, LEN_ = 0
        list sub_len 
        unsigned long long nraw = len(nrow)
        unsigned long long int n
        list size = [], size_ = [], SIZE = []
    
    if show_id is False: chaine += a.frame(s)['v']
    else: chaine += " "*(max_id+1) +a.frame(s)['v']

    for i in range(nraw):
        n = data[i]-len(keys[i])
        if tail is False :
            chaine += " "*n+bm.words(str(keys[i]), bm.fg.rbg(255, 255, 255)).final()+bm.init.reset +a.frame(s)['v']
        else: 
            if i != nraw - 1:
                chaine += " "*n+bm.words(str(keys[i]), bm.fg.rbg(255, 255, 255)).final()+bm.init.reset +a.frame(s)['v']
            else:
                chaine += " " * 2 + a.frame(s)['v']
                chaine += " " * n+bm.words(str(keys[i]), bm.fg.rbg(255, 255, 255)).final()+bm.init.reset +a.frame(s)['v']

    if step_nrow is False:
        #locked tail && head
        SIZE  = [h for h in range(ncol) ]
        chaine += '\n'+top(nraw, ncol, data, max_id, show_id, 0, s, split=tail )+"\n"

        for h, j in enumerate(SIZE) : 
            sub_len = []
            chaine += a.frame(s)['v']
            if show_id is False: pass
            else: 
                m = max_id - len(frame_id_data[j])
                chaine +=" "*m+bm.words(frame_id_data[j], bm.fg.rbg(255, 255, 255)).final()+bm.init.reset+a.frame(s)['v']

            for m, i in enumerate(nrow):
                n = data[m] - all_len[i][j]
                if tail is False:
                    chaine += " "*n+bm.words(str(all_data[i][j]), bm.fg.rbg(255, 255, 255)).final()+bm.init.reset +a.frame(s)['v']
                else:
                    if m != len(nrow)-1:
                        chaine += " "*n+bm.words(str(all_data[i][j]), bm.fg.rbg(255, 255, 255)).final()+bm.init.reset +a.frame(s)['v']
                    else:
                        chaine += " " * 2 +a.frame(s)['v']
                        chaine += " "*n+bm.words(str(all_data[i][j]), bm.fg.rbg(255, 255, 255)).final()+bm.init.reset +a.frame(s)['v']
            if j != ncol-1: chaine += '\n'+top(nraw, ncol, data, max_id, show_id, 1, s,split=tail)+"\n" 
            else: pass
        
    else:
        SIZE    = [h for h in range(ncol)  ]
        size    = SIZE[ : MAX] + SIZE[-2 : ]
        chaine  += '\n'+top(nraw, ncol, data, max_id, show_id, 0, s, split=tail )+"\n"

        for h, j in enumerate(SIZE): 
            if j in size:
                sub_len = []
                chaine += a.frame(s)['v']
                if show_id is False: pass
                else: 
                    m = max_id - len(frame_id_data[j])
                    chaine +=" "*m+bm.words(frame_id_data[j], bm.fg.rbg(255, 255, 255)).final()+bm.init.reset+a.frame(s)['v']

                for m, i in enumerate(nrow):
                    n = data[m] - all_len[i][j]
                    if tail is False:
                        chaine += " "*n+bm.words(all_data[i][j], bm.fg.rbg(255, 255, 255)).final()+bm.init.reset +a.frame(s)['v']
                    else:
                        if m != len(nrow)-1:
                            chaine += " "*n+bm.words(str(all_data[i][j]), bm.fg.rbg(255, 255, 255)).final()+bm.init.reset +a.frame(s)['v']
                        else:
                            chaine += " " * 2 +a.frame(s)['v']
                            chaine += " "*n+bm.words(str(all_data[i][j]), bm.fg.rbg(255, 255, 255)).final()+bm.init.reset +a.frame(s)['v']
                if j not in [MAX-1, size[-1]]: chaine += '\n'+top(nraw, ncol, data, max_id, show_id, 1, s, split=tail )+"\n" 
                else: pass 
            else:
                if LEN < 2: 
                    if LEN == 0 : chaine += "\n"+bottom(nraw, ncol, data, max_id, show_id, s, split=tail )+ '\n' 
                    else: chaine += '\n'+ bottom_(nraw, ncol, data, max_id, show_id, s, split=tail)+'\n'
                else: pass
                LEN += 1
    
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
    
    cpdef FRAME(self, bint Frame = True, str _typ_ = "dictionary", bint show_index = False, bint _s_ = False,
                            bint Head = False, bint Tail = False):
        cdef:
            list keys, values, typ
            unsigned long length, i, j, limit 
            list store = [], size = []
            unsigned long l
            dict data = {}
            dict str_len = {}
            str chaine = bm.fg.rbg(255,255,255)
            dict pan = {'s':None}
            unsigned long int nraw, ncol, _sum_
            list frame_id = [], frame_id_= []
            unsigned long int frame_id_max = 0
            list _values_ = [], _keys_ = []
            unsigned long long int LONG, LONG0 = 0
            unsigned long int x_max, max_y
            dict to_return = {}
            list _list_ = [], x_sum = []
            dict my_dict = {}, master_dict = {}
            unsigned long long int _summ_ = 0
            bint split = False
            unsigned long long int idd_index = 0
        
        x_max, max_y = screenConfig.cursorMax()

        typ=[type(None), type(int()), type(float()), type(bool()), type(str()),
            numpy.int8, numpy.int16, numpy.int32, numpy.int64, 
            numpy.float16, numpy.float32, numpy.float64,
            numpy.complex64, numpy.complex128, numpy.complex64] 

        if type(self.master) == type(dict()) :
            if _typ_ == 'dictionary':
                keys            = list(self.master.keys())
                values          = list(self.master.values())
                my_dict         = self.master.copy()
                del self.master
            else:
                my_dict         = self.master['s'].to_dict(orient='list').copy()
                values          = list(my_dict.values()).copy()
                keys            = list(my_dict.keys()).copy()
                frame_id        = self.master['id']
                to_return['s']  = self.master['s'].copy()
                _list_          = values.copy()
                del self.master

            length = len(keys)
         
            if values:
                if frame_id:
                    for i in range(len(frame_id)):
                        if len(str(frame_id[i])) > idd_index: idd_index = len(str(frame_id[i]))
                        else: pass 
                else:  idd_index = len(str(length))

                for i in range(length):
                    if (_summ_ + 50 + idd_index ) < x_max:
                        x_sum.append(i)
                        str_len[i] = []
                        
                        try:
                            if type(values[i]) == type(list()):
                                if i == 0 : LONG0, LONG = len(values[i]), len(values[i])
                                else : LONG= len(values[i])
                            elif type(values[i]) == type(numpy.array([1])):
                                if len(values[i].shape) == 1: pass 
                                else:
                                    if values[i].shape[1] == 1: pass
                                    else: 
                                        self.error['s'] = ERRORS(self.line).ERROR5(keys[i], LONG0) 
                                        break
                                
                                if self.error['s'] is None:
                                    values[i] = atl.ndarray(list(values[i]), self.line).List()
                                    if i == 0 : LONG0, LONG = len(values[i]), len(values[i])
                                    else : LONG= len(values[i])
                                else: break
                            else:
                                self.error['s'] = ERRORS(self.line).ERROR6(i) 
                                break

                            if self.error['s'] is None:
                                if LONG0 == LONG :
                                    if LONG != 0:
                                        l = len(keys[i])
                                        if l > 15:
                                            keys[i] = keys[i][ : 6] + "..." + keys[i][-6 : ]
                                            l = len(keys[i])
                                        else: pass 
                                        _keys_.append( keys[i] )
                                        master_dict[keys[i]] = list(values[i].copy())
                                        data[i] = values[i].copy() 
                                        for j in range(LONG):
                                            if type(values[i][j]) in typ: 
                                                data[i][j] = str( data[i][j] )

                                                if len( data[i][j] ) > l: 
                                                    if len( data[i][j]  ) < 15 : l = len( data[i][j] )
                                                    else: 
                                                        data[i][j] = data[i][j][ : 6] + "..." + data[i][j][ -6 : ]
                                                        l = len( data[i][j] )
                                                else: pass 
                                                str_len[i].append( len( data[i][j] ) )
                                            else: 
                                                self.error['s'] = ERRORS(self.line).ERROR2(i, j)
                                                break
                                        
                                        if self.error['s'] is None: 
                                            store.append(l)
                                            _summ_ += l
                                        else: break
                                    else: 
                                        self.error['s'] = ERRORS(self.line).ERROR1(i, 'c')
                                        break 
                                else:
                                    self.error['s'] = ERRORS(self.line).ERROR3() 
                                    break
                            else:  break
                        except (TypeError, ValueError) :
                            self.error['s'] = ERRORS(self.line).ERROR4(i) 
                            break
                    else:
                        if i == (length - 2) : _summ_ = 0
                        else: pass
                
                if self.error['s'] is None:
                    if Frame is True: pan['s'] = pd.DataFrame( my_dict  )
                    else:
                        if _keys_:
                            length = len( x_sum ) 
                            x_sum  = list(data.keys())
                            if len(keys) == len(_keys_): pass 
                            else: split = True 
                            
                            keys   = _keys_
                            
                            if len(frame_id) < 15:
                                frame_id_ = [len(str(x)) for x in frame_id]
                                frame_id_max = max(frame_id_)
                                frame_id_ = [str(x) for x in frame_id]
                                chaine += head(length, len(data[0]), store, frame_id_max, show_index, _s_, split=split)+"\n"
                                chaine += midle(x_sum, len(data[0]), store, data, str_len, keys, frame_id_max, show_index, 
                                                frame_id_, _s_, tail=split, head=Head,step_col=False, step_nrow=False, limit=0)+"\n"
                                chaine += bottom(length, len(data[0]), store, frame_id_max, show_index, _s_, split=split)
                            
                            else:
                                frame_id_ = [len(str(x)) for x in frame_id]
                                frame_id_max = max(frame_id_)
                                frame_id_ = [str(x) for x in frame_id]
                                chaine += head(length, len(data[0]), store, frame_id_max, show_index, _s_, split=split)+"\n"
                                chaine += midle(x_sum, len(data[0]), store, data, str_len, keys, frame_id_max, show_index, 
                                            frame_id_, _s_, step_nrow=True, step_col=False, limit=0, tail=split, head=Head)+"\n"
                                chaine += bottom(length, len(data[0]), store, frame_id_max, show_index, _s_, split=split)
                                
                            pan['s'] = pd.DataFrame( my_dict )
                        else : self.error['s'] = ERRORS( self.line ).ERROR8()
                else: pass      
                
            else: self.error['s'] = ERRORS( self.line ).ERROR0()

        if _s_ is False: 
            if Tail is True : return pan['s'].tail(), chaine+bm.init.reset, my_dict.copy(), self.error['s']
            elif Head is True : return pan['s'].head(), chaine+bm.init.reset, my_dict.copy(), self.error['s']
            else:  return pan['s'], chaine+bm.init.reset, master_dict.copy(), self.error['s']
        else: return f"\n{chaine}"+bm.init.reset

cdef class ERRORS:.
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
        self.error = fe.FileErrors( 'ValueError' ).Errors()+"{}table {}bad input data. ".format( self.red, self.white )+err

        return self.error+self.reset

    cdef ERROR1(self,  unsigned long int nrow, char c="r"):
        cdef:
            str err 
        
        if c=='r':
            err = "{}nrow = {}{}. {}line : {}{}.".format(self.white, self.red, nrow, self.white, self.yellow, self.line)
        else:
            err = "{}ncol = {}{}. {}line : {}{}.".format(self.white, self.red, nrow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+"{}Some lists in {}table {}contain any value. ".format(self.white, self.red, self.white)+err

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
            
        err = "{}have not the same size. {}line : {}{}.".format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+"{}all columns in {}table ".format(self.white, self.red )+err

        return self.error+self.reset
    
    cdef ERROR4(self, unsigned long int ncol):
        cdef:
            str err 
            str chaine 

        chaine = self.cyan+"a list()"+self.m+" or a tuple()"+self.reset
        
        err = "{}is not an {} {}type. {}line : {}{}.".format(self.white, chaine, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+"{}table ncol = {}{} ".format( self.red, self.cyan,  ncol)+err

        return self.error+self.reset

    cdef ERROR5(self, str string, unsigned long nrow ):
        cdef:
            str err 
            str chaine         
        err = "{}should be {}[{}, 1]. {}line : {}{}.".format(self.white, self.yellow, nrow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+"{}table item {}<{}> ".format( self.red, self.cyan,  string)+err

        return self.error+self.reset

    cdef ERROR6(self, unsigned long int ncol):
        cdef:
            str err 
            str chaine 

        chaine = self.cyan+"a list() "+self.yellow+"a ndarray() " + self.m+" or a tuple()"+self.reset
        
        err = "{}is not an {} {}type. {}line : {}{}.".format(self.white, chaine, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+"{}table ncol = {}{} ".format( self.red, self.cyan,  ncol)+err

        return self.error+self.reset
    
    cdef ERROR7(self, unsigned long int ncol, unsigned long int nrow):
        cdef:
            str err 
 
        err = "{}should be {}1d array. {}line : {}{}.".format(self.white, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+"{}table (ncol, row) : {}({},{}) ".format( self.red, self.cyan,  ncol, nrow)+err

        return self.error+self.reset

    cdef ERROR8(self):
        cdef:
            str err 
 
        err = "{}to output data. {}line : {}{}.".format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'Warning' ).Errors()+"{}ScreenSize {}too small".format( self.red, self.white)+err

        return self.error+self.reset
