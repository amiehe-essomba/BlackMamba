import sys
from IDE.EDITOR                             import string_to_chr, details
from script.STDIN.LinuxSTDIN                import bm_configure as bm
from script.STDIN.LinuxSTDIN                import ascii
from src.classes                            import error 
from IDE.EDITOR                             import true_cursor_pos as cursor_pos
from IDE.EDITOR                             import test
from script                                 import control_string

def top(max_):
    asc     = ascii.frame(True)
    bold    = bm.init.bold
    w       = bold+bm.fg.rbg(255, 255, 255)
    c       = bold+bm.fg.rbg(0, 0, 0)
    r       = bm.init.reset
    s       = 'file output name'.center(max_-2)
    g       = bm.fg.rbg(0, 0, 255)
    sys.stdout.write(c+f"{asc['ul']}"+f"{asc['h']}"*(max_-2)+f"{asc['ur']}"+r+"\n")
    sys.stdout.write(c+f"{asc['v']}"+bold+w+s+c+f"{asc['v']}"+r+"\n")
    
def bottom(max_):
    asc     = ascii.frame(True)
    bold    = bm.init.bold
    w       = bold+bm.fg.rbg(255, 255, 255)
    c       = bold+bm.fg.rbg(0, 0, 0)
    r       = bm.init.reset
    sys.stdout.write(c+f"{asc['dl']}"+f"{asc['h']}"*(max_-2)+f"{asc['dr']}"+r+"\n")

class files:
    def __init__(self, database : dict, data: list):
        self.database = database
        self.data     = data
    def save(self):
        self.acs    = ascii.frame(True)
        self.string = ''
        self.I      = 0
        self.c      = bm.init.bold+bm.fg.rbg(255,255,255)
        self.r      = bm.init.reset
        self.chars  = control_string.STRING_ANALYSE(1, {}).UPPER_CASE()+ control_string.STRING_ANALYSE(0, {}).LOWER_CASE()+['_', '.'] 
        self.n      = 8
        self.b      = bm.init.bold+bm.fg.rbg(0, 0, 0)
        self.main_input = self.b + self.acs['v'] + self.r + self.c + "name : " * (1)+self.r
        self.max_x, self.max_y = test.get_win_ter()
        self.max_x = self.max_x // 2
        
        sys.stdout.write("\n\n")
        top(self.max_x)
        sys.stdout.write(self.b+f"{self.acs['vl']}" + f"{self.acs['h']}"*(self.max_x-2) + f"{self.acs['vr']}"+self.r+"\n")
        sys.stdout.write(self.main_input)
        self.pos_x, self.pos_y      = cursor_pos.cursor()
        sys.stdout.write(bm.move_cursor.RIGHT(pos=self.max_x-self.n-1)+self.b+f"{self.acs['v']}"+bm.move_cursor.LEFT(pos=1000)+self.r+'\n')  
        bottom(self.max_x)
        
        sys.stdout.write(bm.cursorPos.to(int(self.pos_x), int(self.pos_y)))
        sys.stdout.flush()
        
        while True:
            try:
                self.char = string_to_chr.convert()
                if self.char:
                    _ = self.char[1]
                    self.char = self.char[0]
                    if self.char is not None : 
                        if 32 <= self.char <= 126: 
                            self.max_x, self.max_y      = test.get_win_ter()
                            self.pos_x, self.pos_y      = cursor_pos.cursor()
                            if chr(self.char) in self.chars: 
                                if int(self.pos_x) < self.max_x:
                                    self.string  = self.string[ : self.I] + chr(self.char) + self.string[ self.I : ]
                                    self.I += 1
                                    #sys.stdout.write(bm.save.save )
                                else: pass
                            else: pass
                        elif   self.char == 3:  break
                        #moving up and down 
                        elif self.char in {8, 127}: 
                            self.pos_x, self.pos_y      = cursor_pos.cursor()
                            if int(self.pos_x) > self.n+1:
                                self.string  = self.string[ : self.I-1] + self.string[ self.I : ]
                                self.I -= 1
                            else: pass
                        # selction 
                        elif self.char in {10, 13}: 
                            self.string, err = control_string.STRING_ANALYSE({}, 1).DELETE_SPACE( self.string )
                            if err is None:
                                self.database['name'] = self.string
                                with open(self.string, 'w') as f:
                                    for i, s in enumerate(self.data):
                                        if i != len(self.data)-1: f.write(s+'\n')
                                        else: f.write(s+'\n')
                                f.close()
                                break
                            else: pass
                        else : pass
                    
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        sys.stdout.write(bm.clear.line(pos=2))
                        sys.stdout.write(self.main_input + self.string + 
                                bm.move_cursor.RIGHT(pos=self.max_x//2-len(self.string)-self.n-1) + self.b+ 
                                f"{self.acs['v']}" + bm.move_cursor.LEFT(pos=1000)
                                +self.r)
                         
                        pos = len(self.string) + self.n 
                        sys.stdout.write(bm.move_cursor.RIGHT(pos=pos) )
                        
                        sys.stdout.flush()
                    else: pass
                else: pass
            except KeyboardInterrupt: break 
            
        return self.database.copy()
        
        