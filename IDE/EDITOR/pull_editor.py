import sys
import os
from script.STDIN.LinuxSTDIN                import bm_configure as bm
from  time                                  import sleep
#from IDE.EDITOR                             import examples     as exp
from IDE.EDITOR                             import cursor_pos   as cp
from IDE.EDITOR                             import func_class   as FC
from IDE.EDITOR                             import string_to_chr 
from CythonModules.Windows                  import merge_list as ML 
from IDE.EDITOR                             import true_cursor_pos as cursor_pos
from IDE.EDITOR                             import test


class list_of_keys:
    def __init__(self, firstChar : str, data_base : dict):
        self.firstChar = firstChar 
        self.data_base = data_base 
        
    def list(self):    
            
        self.a = ['as', 'add', 'any', 'anonymous']
        self.b = ['begin', 'bool', 'break']
        self.c = ['class', 'cplx', 'close', 'case', 'continue', 'count', 'capitalize', 'clear', 'copy', 'conj', 'choice']
        self.d = ['def', 'default']
        self.e = ['end', 'else', 'elif', 'exit', 'enumerate', 'empty', 'endwith']
        self.f = ['func', 'for', 'from', 'False']
        self.g = ['get', 'global']
        self.h = ['head']
        self.i = ['int', 'if', 'in', 'index', 'init', 'img', 'insert', 'initialize']
        self.j = ['join']
        self.k = ['kurtosis']
        self.l = ['lower','local', 'lstrip','load', 'license', 'lambda']
        self.m = ['matrix', 'module', "merge"]
        self.n = ['none', 'None', 'not', 'norm', 'ndarray', 'None']
        self.o = ['open']
        self.p = ['pass', 'print']
        self.q = ['queue']
        self.r = ['rstrip', 'replace', 'remove', 'random', 'round', 'readline', 'readlines', 'read', 'return', 'range']
        self.s = ['set', 'switch', 'split', 'startwith', 'size', 'sorted']
        self.t = ['table', 'True']
        self.u = ['unless', 'until', 'upper']
        self.v = ['var']
        self.w = ['while','with', 'write', 'writeline', 'writelines']
        self.x = ['']
        self.y = ['yield']
        self.z = ['zip']
        
        if   self.firstChar == 'a': return self.a
        elif self.firstChar == 'b': return self.b
        elif self.firstChar == 'c': return self.c
        elif self.firstChar == 'd': return self.d
        elif self.firstChar == 'e': return self.e
        elif self.firstChar == 'f': return self.f
        elif self.firstChar == 'g': return self.g
        elif self.firstChar == 'h': return self.h
        elif self.firstChar == 'i': return self.i
        elif self.firstChar == 'j': return self.j
        elif self.firstChar == 'k': return self.k
        elif self.firstChar == 'l': return self.l
        elif self.firstChar == 'm': return self.m
        elif self.firstChar == 'n': return self.n
        elif self.firstChar == 'o': return self.o
        elif self.firstChar == 'p': return self.p
        elif self.firstChar == 'q': return self.q
        elif self.firstChar == 'r': return self.r
        elif self.firstChar == 's': return self.s
        elif self.firstChar == 't': return self.t
        elif self.firstChar == 'u': return self.u
        elif self.firstChar == 'v': return self.v
        elif self.firstChar == 'w': return self.w
        elif self.firstChar == 'x': return self.x
        elif self.firstChar == 'y': return self.y
        elif self.firstChar == 'z': return self.z
            
class IDE:
    def __init__(self, idd : int, firstChar : str, data_base: dict):
        self.data_base  = data_base
        self.idd        = idd
        self.firstChar  = firstChar
        self.w          = bm.bg.black_L+ bm.init.bold+bm.fg.rbg(255,255,255)
        self.re         = bm.init.reset
        self.cursor     = bm.init.bold+bm.fg.rbg(255,0,0) + chr(9654)+self.re
        self.cursor_inv = ' '+bm.init.bold+bm.fg.rbg(255,0,0) +self.re   # + chr(9658)+self.re
        self.r          = bm.fg.rbg(255,0,0)
        self.ww         = bm.init.bold+bm.fg.rbg(255,255,255)
        self.o          = bm.init.bold+bm.fg.rbg(255,0,255)+f'{chr(10148)*2} (O)' + bm.init.reset
        self.cl         = bm.init.bold+bm.fg.rbg(0,255,255) +f'{chr(10148)*2} (C)' + bm.init.reset
        self.g          = bm.init.bold+bm.fg.rbg(0,255,0)+ f'{chr(10148)*2} (F)' + bm.init.reset
        self.var        = bm.init.bold+bm.fg.rbg(255,255,0)+ f'{chr(10148)*2} (V)' + bm.init.reset
    def Linux(self, inp : list, true_chaine : str = "", pos:int=0, move_cursor_down : int = 0):
        
        self.vr, self.fc, self.cc = FC.F_C(self.data_base).F_C(inp, self.firstChar, self.idd)
        self.input      =  inp[0]
        self.empty      = " "
        self.len        = 16
        self.locked     = False
        self.index      = 0
        self.disp       = len(true_chaine)+4
        self.srt        = " " * self.disp
        self.classes    = sorted(inp[3])
        self.func       = sorted(inp[2])
        self.vars       = sorted(inp[1])
        
        self.os         = chr(9553)
        self.mn         = chr(9552)
        self.plu        = chr(9556)
        self.pld        = chr(9562)
        self.pru        = chr(9559)
        self.prd        = chr(9565)
        
        self.ver        = bm.init.bold+self.ww+" "+ self.mn*10+ self.pru
        self.emp        = bm.init.bold+self.ww+"   "+ " "*10+ self.os
        self.complet    = False 
        self.head1      = False 
        self.head2      = False
        self.noChar     = False 
        self.lockChar   = False 
        self.pointer    = 0
        self.already    = False
        self.index_test = None
        self.max_       = 40
        self.index_head = 0
        self.name       = bm.init.bold+bm.fg.rbg(255, 255, 0)+bm.init.rapid_blink+"BLACK MAMBA"+self.re+bm.bg.black_L
        
        self.lev1   = bm.init.bold+self.ww+"   "+" "*2+ "+"*(self.max_+2)
        self.nex    = bm.init.bold+self.ww+"   "+" "*2+ "+" + " "*self.max_+"+"
        self.list_is_empty = False
        self.pos_x, self.pos_y = cursor_pos.cursor()
        self.max_x, self.max_y = test.get_win_ter()
        self._s_ = self.srt+'  '+' '+' '*(self.len+1)+' '
        self.border_x_limit = self.max_x - int(self.pos_x) #(self.max_x) - (len(self._s_)+int(self.pos_x))
        
        sys.stdout.write(bm.save.save)
        sys.stdout.write("\n")
        
        for i in range(move_cursor_down):
            sys.stdout.write("\n") 
        
        for i in range(move_cursor_down):
            sys.stdout.write(bm.move_cursor.UP(pos=1))
        sys.stdout.write(bm.move_cursor.UP(pos=1))
        sys.stdout.write(bm.move_cursor.RIGHT(pos=int(self.pos_x) -1))
        if self.border_x_limit < self.len+10 : self.srt = ''
        else: pass 
    
        sys.stdout.write(bm.save.save)
        sys.stdout.flush()
            
        sys.stdout.write("\n")
        
        for i, value in enumerate(self.input):
            if self.idd == 1:
                self.noChar = True
                self.index += 1
                
                if i == 0:
                    value = f"{self.os} " + bm.words(value, self.w).final() + self.w+self.empty * (self.len - len(value))+self.r+self.os
                    if   self.input[0] in self.classes: value += self.re+self.ww+self.cl
                    elif self.input[0] in self.func   : value += self.re+self.ww+self.g
                    elif self.input[0] in self.vars   : value += self.re+self.ww+self.var
                    else: value += self.re+self.ww+self.o
                    
                    if not self.input[0]: self.list_is_empty = True 
                    else: 
                        sys.stdout.write(self.srt + '  '+self.w+self.plu+self.mn*(self.len+1)+self.pru + self.re+'\n')
                        if pos == i: sys.stdout.write(self.srt + self.cursor + " " + self.w + self.r + value + self.re+'\n')
                        else: sys.stdout.write(self.srt + " " + " " + self.w + value + self.re+'\n')
                    
                    if i != len(self.input)-1: pass 
                    else: 
                        self.head1      = True
                        self.head2      = True
                        self.complet    = True
                else: 
                    value = f"{self.os} " + bm.words(value, self.w).final() + self.w+self.empty * (self.len - len(value))+self.w+self.os
                    if   self.input[i] in self.classes: value += self.re+self.ww+self.cl
                    elif self.input[i] in self.func   : value += self.re+self.ww+self.g
                    elif self.input[i] in self.vars   : value += self.re+self.ww+self.var
                    else: value += self.re+self.ww+self.o
                    if i != pos:  sys.stdout.write(self.srt + "  "+self.w + value+ self.re+'\n')
                    else: sys.stdout.write(self.srt + self.cursor + " " + self.w + self.r + value + self.re+'\n') ####
                    
                    self.head1      = True
                    self.head2      = True
                    self.complet    = True
                    
            else:
                try:
                    if self.firstChar == value[ : self.idd]:
                        self.lockChar   = True
                        self.noChar     = True
                        self.index     += 1
                        self.pointer    = len(self.input)
                        if self.index_head == 0:  
                            sys.stdout.write(self.srt + '  '+self.w+self.plu+self.mn*(self.len+1)+self.pru + self.re+'\n')
                            self.index_head = 1
                        else: pass
                        
                        if i == pos:   value = f"{self.os} " + bm.words(value, self.w).final() + self.w+self.r+self.empty * (self.len - len(value))+self.os
                        else:          value = f"{self.os} "  + bm.words(value, self.w).final() + self.w+self.empty * (self.len - len(value))+self.os
                        
                        if self.locked is False:
                            if   self.input[i] in self.classes: value += self.re+self.ww+self.cl
                            elif self.input[i] in self.func   : value += self.re+self.ww+self.g
                            elif self.input[i] in self.vars   : value += self.re+self.ww+self.var
                            else: value += self.re+self.ww+self.o
                                
                            if self.already is False:
                                if i == pos: sys.stdout.write(self.srt + self.cursor + " " + self.w + self.r +  value+self.re+'\n')
                                else: sys.stdout.write(self.srt + " " + " " + self.w  +  value+self.re+'\n')                
                                self.already = True
                            else: pass
                            
                            if self.pointer == 2 and i < self.pointer-1:
                                self.head1 = False
                                if self.already is False: self.already = True
                                else: pass
                            elif self.pointer == 2 and i == self.pointer-1:
                                if self.already is False: self.head1 = True
                                else: pass
                            elif self.pointer == 3:
                                if self.already is False:
                                    self.head2 =True
                                    self.already = True
                                else: pass
                            elif 3 < self.pointer < 8 :
                                if self.already is False:
                                    self.already = True
                                else: pass
                            elif self.pointer == 8 :
                                if self.already is False:
                                    self.complet = True
                                    self.alreday = True
                                else: pass
                            else: pass
                            self.locked         = True
                            self.index_test     = i
                        else:
                            
                            if   self.input[i] in self.classes: value += self.re+self.ww+self.cl
                            elif self.input[i] in self.func   : value += self.re+self.ww+self.g
                            elif self.input[i] in self.vars   : value += self.re+self.ww+self.var
                            else: value += self.re+self.ww+self.o
                            if i == pos: sys.stdout.write(self.srt + self.cursor + " " + self.w + self.r +  value+self.re+'\n')
                            else: sys.stdout.write(self.srt + "  "+self.w + value + self.re+'\n')
                        
                    else:
                        self.list_is_empty = True 
                        if self.lockChar is False : self.noChar = False
                        else: pass
                except  IndexError : self.noChar = True
                        
        if self.noChar is True:
            if self.head1 is True:
                if self.head2 is True :  
                    if self.list_is_empty is False: sys.stdout.write(self.srt + '  '+self.w+self.pld+self.mn*(self.len+1)+self.prd + self.re+'\n')
                    else: pass
                else:
                    if len(self.firstChar) == 1 : sys.stdout.write(self.srt + '  '+self.ww+self.pld+self.mn*(self.len+1)+self.prd + self.re+'\n')
                    else: sys.stdout.write(self.srt + '  '+self.ww+self.pld+self.mn*(self.len+1)+self.prd + ' '* 5 + self.re+'\n')      
            else:  sys.stdout.write(self.srt + '  '+self.w+self.pld+self.mn*(self.len+1)+self.prd+ self.re+self.ww+' '*5+self.re+'\n')
                 
            if self.head2 is True: pass
            else:
                if len(self.firstChar) == 2 :  sys.stdout.write(self.srt + '  '+self.ww+' '+' '*(self.len+1)+' ' +' '*5+self.re+'\n')
                else:  sys.stdout.write(self.srt + '  '+self.ww+' '+' '*(self.len+1)+' ' +' '*5+ self.re+'\n')

            if self.complet is True: pass
            else:
                if self.idd != 1:
                    if len(self.input) > 8: n = len(self.input)-8+14
                    elif len(self.input) == 8: n = 12
                    else: n = 8-len(self.input)+12
                else: n=1
            if self.idd == 1:
                sys.stdout.write('\n')
                sys.stdout.write(self.srt + '  '+self.w+self.plu+self.mn*(self.len+1)+self.pru + self.re+'\n')
                sys.stdout.write(self.srt + '  '+self.w+self.os+ self.name+ " " *(self.len+1-11)+self.os+ self.re+self.ww+' '*5+self.re+'\n')
                sys.stdout.write(self.srt + '  '+self.w+self.pld+self.mn*(self.len+1)+self.prd+ self.re+self.ww+' '*5+self.re+'\n')
                
            else:
                sys.stdout.write(self.srt + '  '+self.w+self.plu+self.mn*(self.len+1)+self.pru + self.re+'\n')
                sys.stdout.write(self.srt + '  '+self.w+self.os+ self.name+ " " *(self.len+1-11)+self.os+ self.re+self.ww+' '*5+self.re+'\n')
                sys.stdout.write(self.srt + '  '+self.w+self.pld+self.mn*(self.len+1)+self.prd+ self.re+self.ww+' '*5+self.re+'\n')
        else: 
            if self.list_is_empty is False: pass  
            else: pass
        
        sys.stdout.flush()
        
        return self.index
	
class  DropDown:
    def __init__(self, data_base: dict, line: int, key:bool=True):
        self.line               = line
        self.data_base          = data_base
        self.key 				= key
    
    def MENU(self, string : str = 'r', true_chaine : str = "", indicator = None, pos : int = 0, d_max_x : int = 1) :
        ouput               = ""
        np                  = 1
        self.max_size       = 6
        self.new            = []
        err                 = None
                
        if self.key is True:
            try:
                firtsChar   = string[0]
                all_values  = list_of_keys(firtsChar, {}).list()
                self.vr, self.fc, self.cc = FC.F_C(self.data_base).F_C(all_values, string, len(string))  
                all_values  = sorted(all_values)
                
                if   indicator is None  : 
                    for s in all_values:
                        if string in s[:len(string)]:  self.new.append(s)
                        else: pass 
                     
                    if self.new:
                        np = len(self.new)
                        if np < 5: np -= 1 
                        else:  self.new = self.new[:5]
                        idd = self.max_size + len(self.new)
                        self.index = IDE(len(string), string, self.data_base).Linux( 
                                inp = [self.new, self.vr, self.fc, self.cc], true_chaine= true_chaine, move_cursor_down=idd )
                        self.max_size += self.index
                    else: pass 
                elif indicator in {7}   :
                    self.idd        = len(string)
                    self.new_data = []
                    self.len_ = 0
                    
                    if string:
                        for s in all_values:
                            try:
                                if string == s[:self.idd] : 
                                    self.new_data.append(s)
                                    if self.len_ >= len(s): pass 
                                    else: self.len_ = len(s)
                                else: pass
                            except IndexError: pass
                    else: pass
                    
                    if self.new_data:
                        self.max_size += len(self.new_data)
                        if all_values: 
                            ouput, err = cp.new_windows( string, self.line ).cursor_pos( sorted(self.new_data), true_chaine, self.len_ )
                            if err is None:
                                if len(ouput) > d_max_x: ouput =""
                                else: pass
                        else: pass
                    else: self.max_size = 1
                elif indicator in {14}  :
                    if all_values: 
                        try: val = all_values[pos]
                        except IndexError: val = all_values[pos-1]
                        ouput = val
                        self.max_size = 1
                    else: pass
                elif indicator in {65, 66}:
                    for s in all_values:
                        if string in s[:len(string)]:  self.new.append(s)
                        else: pass 
                        
                    if self.new:
                        np = len(self.new)
                        if np < 5: np -= 1 
                        else:
                            if  pos < 5 :  self.new = self.new[:5]
                            else: self.new , pos = self.new[pos-5: pos], 4
                     
                        self.index = IDE(len(string), string, self.data_base).Linux( 
                                inp = [self.new, self.vr, self.fc, self.cc], true_chaine= true_chaine, pos=pos )
                        self.max_size += self.index
                    else: pass
                    ouput = all_values[pos]
            except TypeError: pass 
            except IndexError: pass
        else: pass

        return ouput, np, self.max_size, err
        