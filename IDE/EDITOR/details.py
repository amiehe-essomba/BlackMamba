import sys
import time
from IDE.EDITOR                             import string_to_chr 
from script.STDIN.LinuxSTDIN                import bm_configure as bm
from script.STDIN.LinuxSTDIN                import ascii
from IDE.EDITOR                             import examples as e    

class Details:
    def __init__(self, srt : str = "", line : int = 1):
        self.left       = bm.init.bold+bm.fg.red_L+'>'
        self.right      = bm.init.bold+bm.fg.red_L+'<'
        self.re         = bm.init.reset
        self.w          = bm.bg.black_L+bm.init.bold+bm.fg.white_L
        self.ww         = bm.init.bold+bm.fg.white_L
        self.srt        = " " * len(srt) + "     "
        self.r          = bm.init.bold+bm.fg.rbg(255, 0, 0)
        self.line       = line 
    def Details(self, string_name: str):
        
        r = bm.init.reset
        c = bm.init.bold+bm.init.blink+bm.fg.rbg(255, 0, 255)
        m = bm.init.bold+bm.init.blink+bm.fg.rbg(0, 255, 255)
        w = bm.init.bold+bm.fg.rbg(255, 255, 255)
        self.list, self.len, self.L   = e.code_example(string_name[0], string_name).code()
        
        if self.list is not None:
            self.asc        = ascii.frame(True)
            self.index      = 0 
            self.value      = None
            self.val1       = f'{w}[{m}q{r}{w}] = {c}exit{r}'
            self.val1_l     = len('[q] = exit')
            self.empty      = " "
            self.val1       = f"{self.asc['v']} " + self.val1+self.re + self.w+self.empty * (self.len-self.val1_l)+f"{self.asc['v']}"
            self.store_id   = []
            self.string     = ""
            self.err        = None
            
            #sys.stdout.write(bm.save.save)
            sys.stdout.write("\n")
            sys.stdout.write(self.srt + '  '+self.w+self.asc['ul']+self.asc['h']*(self.len+1)+self.asc['ur'] + self.re+'\n')

            for j, name in enumerate(self.list):
                name = f"{self.asc['v']} " + name +self.re + self.w+self.empty * (self.len - self.L[j])+f"{self.asc['v']}"+self.re
                sys.stdout.write(self.srt + '  '+self.w+ name +self.re+'\n')
                if j == 0: sys.stdout.write(self.srt + '  '+self.w+self.asc['vl']+self.asc['h']*(self.len+1)+self.asc['vr'] + self.re+'\n') 
                else: pass
                
            sys.stdout.write(self.srt + '  '+self.w+f"{self.asc['v']}"+' '*(self.len+1)+f"{self.asc['v']}" + self.re+'\n')
            sys.stdout.write(self.srt + '  '+self.w+self.asc['vl']+self.asc['h']*(self.len+1)+self.asc['vr'] + self.re+'\n')
            sys.stdout.write(self.srt + '  '+self.w+ self.val1+self.re+'\n')
            sys.stdout.write(self.srt + '  '+self.w+self.asc['dl']+self.asc['h']*(self.len+1)+self.asc['dr'] + self.re+'\n')
           
            self.m = len(self.list)+4
            for j in range(self.m):
                sys.stdout.write(bm.move_cursor.UP(pos=1))
            
            sys.stdout.write(bm.move_cursor.RIGHT(pos=len(self.srt)))
        
            #sys.stdout.write(bm.save.save)
            sys.stdout.flush() 
            
            while True:
                try:
                    self.char = string_to_chr.convert()
                    if self.char:
                        _ = self.char[1]
                        self.char = self.char[0]
                        # breaking without selecting (q)
                        if self.char == 113 : 
                            sys.stdout.write(bm.move_cursor.UP(pos=2))
                            sys.stdout.write(bm.clear.screen(pos=0))
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            break
                        else : pass
                        sys.stdout.flush() 
                    else: pass
                except KeyboardInterrupt:
                    pass
        else: pass 