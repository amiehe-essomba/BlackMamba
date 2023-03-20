import sys
import time
from IDE.EDITOR                             import string_to_chr, details
from script.STDIN.LinuxSTDIN                import bm_configure as bm
from script.STDIN.LinuxSTDIN                import ascii
from src.classes                            import error 


class new_windows:
    def __init__(self, srt : str = "", line : int = 1):
        self.left       = bm.init.bold+bm.fg.red_L+'>'
        self.right      = bm.init.bold+bm.fg.red_L+'<'
        self.re         = bm.init.reset
        self.w          = bm.bg.black_L+bm.init.bold+bm.fg.white_L
        self.ww         = bm.init.bold+bm.fg.white_L
        self.srt        = " " * len(srt) + "     "
        self.r          = bm.init.bold+bm.fg.rbg(255, 0, 0)
        self.line       = line 
    def cursor_pos(self, list_of_values: list):
        def number(num : int):
            if num <= 9:  return self.ww+'[ '+self.r+f"{num}"+self.re+self.ww+']'+self.re
            else:         return self.ww+'[' +self.r+f"{num}"+self.re+self.ww+']'+self.re
        
        def select_number( str_ : str ):
            try:
                num = int( str_[1:] )
            except TypeError: num = 0
            return num 
        
        def id_pos( num , w, m, r ):
            l = len(num)
            s = " " * (6-l+1)
            v =  f'{w}[ {m}i{r} {w}]    = {c}{num}{r}'+s
            return v 
        
        r = bm.init.reset
        c = bm.init.bold+bm.init.blink+bm.fg.rbg(255, 0, 255)
        m = bm.init.bold+bm.init.blink+bm.fg.rbg(0, 255, 255)
        w = bm.init.bold+bm.fg.rbg(255, 255, 255)
        self.asc        = ascii.frame(True)
        self.list       = list_of_values 
        self.index      = 0 
        self.value      = None
        self.len        = 18
        self.val1       = f'{w}[{m}Enter{r}{w}] = {c}select{r}  '
        self.val2       = f'{w}[{m}q{r}{w}]     = {c}exit{r}    '
        self.val3       = f'{w}[{m}d{r}{w}]     = {c}details{r} '
        self.empty      = " "
        self.val1       = f"{self.asc['v']} " + self.val1+self.re + self.w+self.empty * (self.len - len(self.val1))+f"{self.asc['v']}"
        self.val2       = f"{self.asc['v']} " + self.val2+self.re + self.w+self.empty * (self.len - len(self.val2))+f"{self.asc['v']}"
        self.val3       = f"{self.asc['v']} " + self.val3+self.re + self.w+self.empty * (self.len - len(self.val3))+f"{self.asc['v']}"
        self.store_id   = []
        self.string     = ""
        self.err        = None
        
        sys.stdout.write(bm.save.save)
        sys.stdout.write("\n")
        sys.stdout.write(self.srt + '  '+self.w+self.asc['ul']+self.asc['h']*(self.len+1)+self.asc['ur'] + self.re+'\n')

        for j, name in enumerate(self.list):
            name = f"{self.asc['v']} " + bm.words(name, self.w).final() +self.re + self.w+self.empty * (self.len - len(name))+f"{self.asc['v']}"+self.re+' '+number(j)
            sys.stdout.write(self.srt + '  '+self.w+ name +self.re+'\n')
            
        sys.stdout.write(self.srt + '  '+self.w+f"{self.asc['v']}"+' '*(self.len+1)+f"{self.asc['v']}" + self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+self.asc['vl']+self.asc['h']*(self.len+1)+self.asc['vr'] + self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+ self.val1+self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+ self.val2+self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+ self.val3+self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+self.asc['dl']+self.asc['h']*(self.len+1)+self.asc['dr'] + self.re+'\n')
        
        self.m = len(self.list)+6
        for j in range(self.m):
            sys.stdout.write(bm.move_cursor.UP(pos=1))
        
        sys.stdout.write(bm.move_cursor.RIGHT(pos=len(self.srt)))
    
        sys.stdout.write(bm.save.save)
        sys.stdout.flush() 
        
        while True:
            try:
                self.char = string_to_chr.convert()
                if self.char:
                    _ = self.char[1]
                    self.char = self.char[0]
                    # keyboardInterrupt
                    if   self.char == 3:
                        sys.stdout.write(bm.save.restore)
                        sys.stdout.write(bm.move_cursor.UP(pos=1))
                        sys.stdout.write(bm.clear.screen(pos=0))
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        self.value = None
                        return
                    #moving up and down 
                    elif self.char == 27:
                        self.string = ""
                        next1, next2 = 91, _
                        if next1 == 91:
                            try:
                                # moving cursor down
                                if   next2 == 66:
                                    if self.index < len(self.list)-1:
                                        self.index += 1
                                        sys.stdout.write(bm.move_cursor.DOWN(pos=1))
                                        self.store_id.append(self.index)
                                    else: pass
                                # moving cursor left
                                elif next2 == 65: 
                                    if self.index > 0: 
                                        self.index -=1 
                                        sys.stdout.write(bm.move_cursor.UP(pos=1))
                                        self.store_id.append(self.index)
                                    else: pass
                                else: pass
                            except IndexError: pass
                        else: pass            
                    # selction 
                    elif self.char in {10, 13}: # Enter
                        try:
                            if self.string:
                                self.index = select_number( self.string )
                                #time.sleep(2.0)
                                try: self.value = self.list[ self.index ]
                                except IndexError: 
                                    self.err = error.ERRORS( self.line ).ERROR62( self.index )
                                    self.value = None
                                    sys.stdout.write(bm.save.restore)
                                    sys.stdout.write(bm.move_cursor.UP(pos=1))
                                    sys.stdout.write(bm.clear.screen(pos=0))
                                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                    break
                            else: self.value = self.list[ self.index ]
                            sys.stdout.write(bm.save.restore)
                            sys.stdout.write(bm.move_cursor.UP(pos=1))
                            sys.stdout.write(bm.clear.screen(pos=0))
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            break
                        except IndexError: 
                            sys.stdout.write(bm.save.restore)
                            sys.stdout.write(bm.move_cursor.UP(pos=1))
                            sys.stdout.write(bm.clear.screen(pos=0))
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            self.err = error.ERRORS( self.line ).ERROR62( self.index )
                            self.value = None
                            break
                    # breaking without selecting (q)
                    elif self.char == 113 : 
                        sys.stdout.write(bm.save.restore)
                        sys.stdout.write(bm.move_cursor.UP(pos=1))
                        sys.stdout.write(bm.clear.screen(pos=0))
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        self.value = None
                        return
                    # index selection mode [0, ...., 9] pressed a number
                    elif self.char in [x for x in range(48, 58)]: 
                        if self.string: self.string += chr(self.char)
                        else: 
                            if self.index <= len(self.list)-1:
                                self.index = int( chr(self.char))
                                if self.index  <= len(self.list)-1:
                                    if not self.store_id: sys.stdout.write(bm.move_cursor.DOWN(pos=self.index))
                                    else: 
                                        if   self.store_id[-1] == self.index: pass
                                        elif self.store_id[-1] > self.index :
                                            new_id =  abs(self.store_id[-1] - self.index )
                                            sys.stdout.write(bm.move_cursor.UP(pos=new_id))
                                        else: 
                                            new_id =  abs(self.store_id[-1] - self.index )
                                            sys.stdout.write(bm.move_cursor.DOWN(pos=new_id))
                                    self.store_id.append(self.index)
                                else:
                                    sys.stdout.write(bm.save.restore)
                                    sys.stdout.write(bm.move_cursor.UP(pos=1))
                                    sys.stdout.write(bm.clear.screen(pos=0))
                                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                    self.err = error.ERRORS( self.line ).ERROR62( self.index )
                                    self.value = None
                                    break
                            else: 
                                sys.stdout.write(bm.save.restore)
                                sys.stdout.write(bm.move_cursor.UP(pos=1))
                                sys.stdout.write(bm.clear.screen(pos=0))
                                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                self.err = error.ERRORS( self.line ).ERROR62( self.index )
                                self.value = None
                                break
                    # bottom pressed <b>
                    elif self.char == 98:
                        self.string = ""
                        if self.index < len(self.list)-1:
                            self.index = len(self.list)-1
                            if not self.store_id: sys.stdout.write(bm.move_cursor.DOWN(pos=self.index))
                            else: 
                                if   self.store_id[-1] == self.index: pass
                                else: 
                                    new_id =  abs(self.store_id[-1] - self.index )
                                    sys.stdout.write(bm.move_cursor.DOWN(pos=new_id))
                            self.store_id.append(self.index)
                        else: pass
                    # top pressed <t>
                    elif self.char == 116:
                        self.string = ""
                        if self.index <= len(self.list)-1:
                            self.index = 0
                            if not self.store_id: pass
                            else: 
                                if   self.store_id[-1] == self.index: pass
                                else:  
                                    new_id =  abs(self.store_id[-1] - self.index )
                                    sys.stdout.write(bm.move_cursor.UP(pos=new_id))
                            self.store_id.append(self.index)
                        else: pass     
                    # middle pressed < m >
                    elif self.char == 109:
                        self.string = ""
                        if len(self.list) > 4 and len(self.list) % 2 == 0:
                            self.index = int( len(self.list) / 2)
                            if not self.store_id: sys.stdout.write(bm.move_cursor.DOWN(pos=self.index))
                            else: 
                                if   self.store_id[-1] == self.index: pass
                                elif self.store_id[-1] > self.index :
                                    new_id =  abs(self.store_id[-1] - self.index )
                                    sys.stdout.write(bm.move_cursor.UP(pos=new_id))
                                else: 
                                    new_id =  abs(self.store_id[-1] - self.index )
                                    sys.stdout.write(bm.move_cursor.DOWN(pos=new_id))              
                            self.store_id.append(self.index)
                        else: pass
                    # indexation <i>
                    elif self.char == 105: 
                        if not self.string: self.string += chr(self.char)
                        else: 
                            self.string = ""
                            self.string += chr(self.char)  
                    # get more details <d>
                    elif  self.char == 100:
                        sys.stdout.write(bm.save.restore)
                        sys.stdout.write(bm.move_cursor.UP(pos=1))
                        sys.stdout.write(bm.clear.screen(pos=0))
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        details.Details(self.srt, self.line).Details(self.list)
                    else : pass
                    sys.stdout.flush() 
                else: pass
            except KeyError:
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                return
        
        return self.value, self.err
