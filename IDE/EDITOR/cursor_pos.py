from logging import exception
import sys
import termios, sys,tty
from script.STDIN.LinuxSTDIN  import bm_configure as bm


def readchar():
    fd              = sys.stdin.fileno()
    old_settings    = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin)
        ch = ord( sys.stdin.read(1) )
    finally: termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch 

class new_windows:
    def __init__(self, srt : str = ""):
        self.left       = bm.init.bold+bm.fg.red_L+'>'
        self.right      = bm.init.bold+bm.fg.red_L+'<'
        self.re         = bm.init.reset
        self.w          = bm.bg.black_L+bm.init.bold+bm.fg.white_L
        self.ww         = bm.init.bold+bm.fg.white_L
        self.srt        = " " * len(srt) + "     "
        self.r          = bm.init.bold+bm.fg.rbg(255, 0, 0)
        
    def cursor_pos(self, list_of_values: list):
        def number(num : int):
            if num <= 9:  return self.ww+'[ '+self.r+f"{num}"+self.re+self.ww+']'+self.re
            else: return self.ww+'['+self.r+f"{num}"+self.re+self.ww+']'+self.re
          
        self.list       = list_of_values #[str(x) for x in range(10)]
        self.index      = 0 
        self.value      = None
        self.len        = 18
        self.val1       = '[Enter ] = select'
        self.val2       = '[ q ]    = exit'
        self.empty      = " "
        self.val1       = "| " + self.val1+self.re + self.w+self.empty * (self.len - len(self.val1))+'|'
        self.val2       = "| " + self.val2+self.re + self.w+self.empty * (self.len - len(self.val2))+'|'
        self.store_id   = []
        
        sys.stdout.write(bm.save.save)
        sys.stdout.write("\n")
        sys.stdout.write(self.srt + '  '+self.w+'+'+'-'*(self.len+1)+'+' + self.re+'\n')

        for j, name in enumerate(self.list):
            name = "| " + bm.words(name, self.w).final() +self.re + self.w+self.empty * (self.len - len(name))+'|'+self.re+' '+number(j)
            sys.stdout.write(self.srt + '  '+self.w+ name +self.re+'\n')
            
        sys.stdout.write(self.srt + '  '+self.w+'|'+' '*(self.len+1)+'|' + self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+'+'+'-'*(self.len+1)+'+' + self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+ self.val1+self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+ self.val2+self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+'+'+'-'*(self.len+1)+'+' + self.re+'\n')
        
        for j in range(0, len(self.list)+5):
            sys.stdout.write(bm.move_cursor.UP(pos=1))
        
        sys.stdout.write(bm.move_cursor.RIGHT(pos=len(self.srt)))
    
        sys.stdout.write(bm.save.save)
        sys.stdout.flush() 
        
        while True:
            try:
                self.char = readchar()
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
                    
                    next1, next2 = ord( sys.stdin.read(1)), ord( sys.stdin.read(1))
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
                        self.value = self.list[ self.index ]
                        sys.stdout.write(bm.save.restore)
                        sys.stdout.write(bm.move_cursor.UP(pos=1))
                        sys.stdout.write(bm.clear.screen(pos=0))
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        break
                    except IndexError: pass
                # breaking without selecting (q)
                elif self.char == 113 : 
                    sys.stdout.write(bm.save.restore)
                    sys.stdout.write(bm.move_cursor.UP(pos=1))
                    sys.stdout.write(bm.clear.screen(pos=0))
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    self.value = None
                    return
                # index selection mode [0, ...., 9]
                elif self.char in [x for x in range(48, 58)]: 
                    if self.index <= len(self.list)-1:
                        self.index = int( chr(self.char))
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
                # bottom
                elif self.char == 98:
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
                # top
                elif self.char == 116:
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
                # middle
                elif self.char == 109:
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
                else : pass
                    
                sys.stdout.flush() 
                
            except KeyError:
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                return
            
        return self.value
if __name__ == "__main__":
    sys.stdout.write(bm.save.save)
    var = new_windows().cursor_pos()
    print(var)
        
