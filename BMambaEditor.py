 ############################################################
#############################################################
# Black Mamba orion and pegasus code iditor for Linux       #
# This version has currently two code iditors:              #
#                                                           #
#                                                           #
# * pegasus is the default editor                           #
# * orion is the optimized code editor with a syntaxis      #
#   color                                                   #
# basically we can use both without any problems because    #
# they work very well.                                      #
#                                                           #
#                                                           #
# * to select a terminal it's very simple, just do this     #
#                                                           #
#       * mamba --T orion                                   #
#       * mamba --T pegasus                                 #
#############################################################
############################################                #
# ** created by : amiehe-essomba           #                #
# ** updating by: amiehe-essomba           #                #
# ** copyright 2023 amiehe-essomba         #                #
############################################                #
#############################################################


import sys, os
import time
from ctypes                     import windll
from script                     import control_string
from script.STDIN.LinuxSTDIN    import bm_configure     as bm
from script.DATA_BASE           import data_base        as db
from IDE.EDITOR                 import header, string_to_chr 
from IDE.EDITOR                 import test
from IDE.EDITOR                 import true_cursor_pos as cursor_pos
from IDE.EDITOR                 import cursor, figure_file
from IDE.EDITOR                 import left_right as LR
from IDE.EDITOR                 import string_build as SB
from IDE.EDITOR                 import pull_editor as PE
from IDE.EDITOR                 import drop_box as DR
from script.STDIN.LinuxSTDIN    import ascii

def counter(n):
    asc     = ascii.frame(True)
    r       = bm.init.reset
    bold    = bm.init.bold
    y       = bold+bm.fg.rbg(255, 255, 255)
    c       = bold+bm.fg.rbg(255, 255, 255)
    len_    = len(str(n))
    max_    = 5
    space   = " " * (max_-len_)
    if (max_-len_) >= 0:  s       = f"{y}{asc['v']}[{space}{c}{n}{y}]{asc['v']}{r} "
    else:  s = ""

    return s, len(f"[{space}{n}]   ")

def title(max_):
    asc     = ascii.frame(True)
    bold    = bm.init.bold
    w       = bold+bm.fg.rbg(255, 255, 255)
    c       = bold+bm.fg.rbg(255, 255, 255)
    r       = bm.init.reset
    s       = "BLACK MAMBA EDITOR V 1.0.0".center(max_-2)
    sys.stdout.write(c+f"{asc['ul']}"+f"{asc['h']}"* (max_-2)+f"{asc['ur']}"+r+"\n")
    sys.stdout.write(c+f"{asc['v']}"+bold+w+s+c+f"{asc['v']}"+r+"\n")

def bottom(max_):
    asc     = ascii.frame(True)
    bold    = bm.init.bold
    w       = bold+bm.fg.rbg(255, 255, 255)
    c       = bold+bm.fg.rbg(255, 255, 255)
    r       = bm.init.reset
    sys.stdout.write(c+f"{asc['dl']}"+f"{asc['h']}"*7+f"{asc['m2']}"+f"{asc['h']}"* (max_-2-8)+f"{asc['dr']}"+r+"\n")
    
def middle(max_, n, x, y):
    asc     = ascii.frame(True)
    bold    = bm.init.bold
    c       = bold+bm.fg.rbg(255, 255, 255)
    r       = bm.init.reset
    for i in range(n-1):
        i += 1
        inp, len_ = counter(i)
        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
        sys.stdout.write(inp+bm.cursorPos.to(max_, y)+c+f"{asc['v']}"+bm.cursorPos.to(x, y)+r+"\n")
        y += 1
        
def write_in_file(name : str, data : list):
    with open(name, 'w') as f:
        for i,s in enumerate(data):
            if i != len(data)-1: f.wriet(s+'\n')
            else: f.write(s)
    f.close()
    
class windows:
    def __init__(self, data_base: dict):
        # main data base
        self.data_base  = data_base
        # contriling string
        self.analyse    = control_string.STRING_ANALYSE(self.data_base, 1)
        self.acs        = ascii.frame(True)

    def terminal(self, c: str = '', terminal_name : str = 'pegasus'):
        s1, s2  = counter(0)
        # set color on yellow
        self.bold           = bm.init.bold
        self.black          = bm.fg.rbg(255, 255, 255)
        self.c              = self.bold+bm.fg.rbg(255, 255, 0)
        if terminal_name == 'orion': pass
        else: self.c        = self.bold+c
        # reset color
        self.reset          = bm.init.reset
        # input initialized
        self.input          = s1 
        # input main used to build the final string s
        self.main_input     = s1 
        # initial length of the input
        self.length         = len(self.input)
        # initialisation of index associated to the input
        self.index          = self.length
        # length of the foutth first char of input
        self.size           = s2 #len('>>> ')
        # string used to handling the output that is the must inmportant string
        self.s              = ""
        # string used for the code,
        self.string         = ''
        # index associated to the string string value
        self.I_S            = 0
        # initialisation of index I associated to the string s value
        self.I              = 0
        # history of data associated to the string  input
        self.liste          = []
        # history of data associated to the value returns by the function readchar
        self.get            = []
        # initialisation of integer idd used to get the next of previous
        # values stored in the different histories of lists
        self.idd            = 0
        # initialization of list associated to the string s
        self.sub_liste      = []
        # the memory contains the history of get value
        self.memory         = []
        # initilization of last
        self.last           = 0
        # initialisation of list associated to the index value
        self.tabular        = []
        # initialisation of list associated to I value
        self.sub_tabular    = []
        # initialisation of the list associated to last value
        self.last_tabular   = []
        # move cursor
        self.remove_tab     = 0
        # storing cursor position
        self.remove_tabular = []
        # initialization of the list associated to string
        self.string_tab     = []
        # initialization of associated to I_S
        self.string_tabular = []
        ###########################################################
        self.str_drop_down       = ''
        # dropdown index 
        self.drop                = 0
        # line 
        self.if_line             = 0 #
        # dropdown list fo storing
        self.drop_list_str       = [] 
        # dropdown list of index  
        self.drop_list_id        = [] 
        # storig identity and last str_drop_down 
        self.drop_drop           = {'id':[], 'str': []}
        # index of drop_drop 
        self.drop_idd            = 0
        # alphabetic char + underscore char
        self.sss                 = control_string.STRING_ANALYSE(1, {}).UPPER_CASE()+ \
                                   control_string.STRING_ANALYSE(0, {}).LOWER_CASE()+['_']       
        # when Ctrl+ option are used 
        self.indicator           = None
        # line max 
        self.if_line_max         = 0
        self.up_locked           = False
        ###########################################################
        # accounting line
        self.if_line        = 0
        # error variable
        self.error          = None
        # accounting space line
        self.space          = 0
        # detecting if indentation was used
        self.active_tab     = None
        # move curor up fist time 
        self.key_up_first_time      = True
        # storing key_up_first_time
        self.key_up_id              = False 
        self.indexation             = {0 : {'action' : 'FREE', # [FREE, LOCKED]
                                            'status' : 'I',    # [I, D] 
                                            'do'     : 'ADDS',  # [ADD, INSERT, INDEX]
                                            'cursor' : 'NO', # [NO, UP, DOWN, ENTER]
                                            'last'   : ''
                                            }
                                       }
        # action to do after one of these commands is pressed 
        # it means UP, DOWN or ENTER is pressed
        self.action                 = None
        # fixing the x-axis border 
        self.border_x_limit         = True 
        # last line 
        self.last_line              = {"last":0, "now" : 0}
        self.np                     = 0
        self.k                      = 0
        ###########################################################
        # currently cursor position (x, y)
        self.pos_x, self.pos_y      = cursor_pos.cursor()
        # terminal dimension (max_x, max_y)
        self.max_x, self.max_y      = test.get_win_ter()
        self.last_line['last']      = self.max_y-2
        k  = windll.kernel32
        k.SetConsoleMode( k.GetStdHandle(-11), 7)
        # clear entire line
        sys.stdout.write(bm.clear.line(pos=0))
        # move cursor left
        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
        # print the input value
        title(self.max_x)
        sys.stdout.write(self.black+f"{self.acs['vl']}" + f"{self.acs['h']}"* 7 + f"{self.acs['m1']}"+ 
                         f"{self.acs['h']}"*(self.max_x-2-8)+ f"{self.acs['vr']}"+self.reset+"\n")
        
        sys.stdout.write(self.input)
        sys.stdout.write(bm.save.save)
        sys.stdout.write(bm.move_cursor.RIGHT(pos=self.max_x-1)+self.black+f"{self.acs['v']}"+'\n')
        # currently cursor position (x, y)
        self.pos_x, self.pos_y      = cursor_pos.cursor()
        middle(self.max_x, int(self.max_y)-5 ,int(self.pos_x), int(self.pos_y))
        #sys.stdout.write(bm.move_cursor.DOWN(pos=1))
        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
        bottom(self.max_x)
        #sys.stdout.write(bm.save.restore)
        sys.stdout.write(bm.cursorPos.to(self.size+1, 4))
        sys.stdout.write(bm.save.save)
        sys.stdout.flush()
        ###########################################################
        self.max_size_init          = 11 # no optional key (crtl+n , ......)
        self.save_cursor_position   = bm.save.save
        self.indicator_pos          = 0
        # indicator_max 
        self.indicator_max          = 1
        # checking if key_max_activation could be activated  for handling terminal tools
        #self.key_max_activation     = DR.size(self.max_x, self.max_y, self.pos_x, self.pos_y)
        # writing data 
        self.storing_data_for_writing  = [] 
        self.data_storing_file      = {'name' : None}
        ###########################################################
        
        while True:
            try:
                # get input
                self.char = string_to_chr.convert()
                if self.char:
                    _ = self.char[1]
                    self.char = self.char[0]
                    if self.char is not None:
                        #building of str_drop_down only when ord( self.char ) is in self.sss 
                        if 32 <= self.char <= 126:
                            if self.border_x_limit is True:
                                self.pos_x, self.pos_y = cursor_pos.cursor()
                                if (self.max_x - int(self.pos_x)) > 1:
                                    sys.stdout.write(bm.clear.line(pos=0))
                                    if chr(self.char) in self.sss:
                                        self.str_drop_down = self.str_drop_down[ : self.drop] + chr( self.char ) + self.str_drop_down[ self.drop : ]
                                        self.drop += 1
                                    else:
                                        # initialization
                                        self.drop_drop['id'].append( self.drop )
                                        self.drop_drop['str'].append( self.str_drop_down) 
                                        self.drop = 0
                                        self.str_drop_down = ""
                                    if len(self.s) <= self.max_x : self.border_x_limit = True 
                                    else: self.border_x_limit = False
                                else: self.border_x_limit = False
                            else: pass
                        #delecting char in the str_drop_down string 
                        elif self.char in {8, 127}:
                            if self.border_x_limit is True:
                                #sys.stdout.write(bm.clear.screen(pos=0))
                                if self.str_drop_down:
                                    # dropsown string :
                                    self.str_drop_down = self.str_drop_down[ : self.drop - 1] + self.str_drop_down[ self.drop : ]
                                    # dropdown index 
                                    self.drop    -= 1
                                else: pass
                            else: pass
                        else:
                            if self.char in [10, 13, 27, 7, 14]: pass 
                            else:
                                # initialization
                                self.drop_drop['id'].append( self.drop )
                                self.drop_drop['str'].append( self.str_drop_down) 
                                self.drop = 0
                                self.str_drop_down = ""
                                sys.stdout.write(bm.clear.screen(pos=0))
                       
                        # breaking loop while with the keyboardError ctrl+c
                        if self.char == 3:
                            os.system('cls')
                            sys.stdout.write(bm.clear.screen(pos=1))
                            sys.stdout.write(bm.cursorPos.to(0,0))
                            sys.stdout.write(bm.clear.screen(pos=0))
                            sys.stdout.write(bm.move_cursor.DOWN(pos=1))
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            sys.stdout.write(bm.clear.line(pos=0))
                            self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                            print(self._keyboard_)
                            return
                        # writing char
                        elif 32 <= self.char <= 126:
                            ######################################
                            # each character has 1 as length     #
                            # have a look on ansi char           #
                            ######################################
                            if self.border_x_limit is True:
                                # building input
                                self.input  = self.input[: self.index + self.last] + chr(self.char) + self.input[ self.index + self.last:]
                                # building s
                                self.s      = self.s[: self.I] + chr(self.char) + self.s[self.I:]
                                # building string
                                self.string = self.string[: self.I_S] + chr(self.char) + self.string[self.I_S:]
                                # increasing index of a step = 1
                                self.index += 1
                                # increasing I of a step = 1
                                self.I     += 1
                                # increasing I_S of step = 1
                                self.I_S   += 1
                                # storing char in get
                                self.get.append(self.char)
                                
                                # fixing the cursor position conditions
                                if len(self.s) < self.max_x : self.border_x_limit = True 
                                else: self.border_x_limit = False
                                
                            else: pass
                        # moving cursor up, down, left, reight
                        elif self.char == 27:
                            next1, next2 = 91,  _[0]
                            #rint(next1, next2)
                            if next1 == 91:
                                try:
                                    # move cursor to left <-
                                    if   next2 == 68:
                                        if self.I > 0:
                                            try:
                                                # without indentation
                                                if 32 <= self.get[self.I - 1] <= 126:
                                                    self.I     -= 1
                                                    self.index += 1
                                                    self.last  -= 2
                                                    self.I_S   -= 1
                                                    
                                                    self.str_drop_down, self.drop = LR.String( self.string, self.I_S, self.sss )
                                                # when identation is detected
                                                elif self.get[self.I - 1] == 9:
                                                    self.I     -= 4
                                                    self.index += 4
                                                    self.last  -= 8
                                                    self.I_S   -= 4
                                            except IndexError: pass
                                        else:  pass
                                    # move cursor to right ->
                                    elif next2 == 67:
                                        if self.I < len(self.s):
                                            try:
                                                # without indentation
                                                if 32 <= self.get[self.I] <= 126:
                                                    self.I += 1
                                                    self.index  -= 1
                                                    self.last   += 2
                                                    self.I_S    += 1
                                                    
                                                    self.str_drop_down, self.drop = LR.String( self.string, self.I_S, self.sss )
                                                # when identation is detected
                                                elif self.get[self.I] == 9:
                                                    self.I      += 4
                                                    self.index  -= 4
                                                    self.last   += 8
                                                    self.I_S    += 4
                                            except IndexError: pass
                                        else:  pass
                                    # get the previous value stored in the list
                                    elif next2 == 65:  # up
                                        if self.liste:
                                            try:
                                                if self.indexation[self.if_line]['cursor']   == 'NO': 
                                                    if self.indexation[self.if_line]['action'] == 'FREE':
                                                        self.liste.append(self.input)
                                                        self.sub_liste.append(self.s), self.tabular.append(self.index), self.sub_tabular.append(self.I)
                                                        self.last_tabular.append(self.last),self.remove_tabular.append(self.remove_tab)
                                                        self.string_tab.append(self.I_S), self.string_tabular.append(self.string)
                                                        self.memory.append(self.get) , self.drop_list_str.append( self.str_drop_down)
                                                        self.drop_list_id.append(self.drop)
                                                        self.indexation[self.if_line]['action'] = 'LOCKED' 
                                                        self.indexation[self.if_line]['last'] = self.string
                                                        self.indexation[self.if_line]['cursor'] = 'UP'
                                                    else: pass
                                                else : 
                                                    if self.indexation[self.if_line]['status'] == 'I': pass   
                                                    else:
                                                        if self.indexation[self.if_line]['action'] == 'FREE':
                                                            v = self.if_line
                                                            self.liste[v],self.sub_liste[v]                 = self.input, self.s
                                                            self.tabular[v], self.sub_tabular[v]            = self.index, self.I
                                                            self.last_tabular[v], self.remove_tabular[v]    = self.last, self.remove_tab
                                                            self.string_tab[v], self.string_tabular[v]      = self.I_S, self.string
                                                            self.memory[v], self.drop_list_str[v]           = self.get, self.str_drop_down
                                                            self.drop_list_id[v]                            = self.drop  
                                                            self.indexation[self.if_line]['action'] = 'LOCKED' 
                                                            self.indexation[self.if_line]['last'] = self.string
                                                            self.indexation[self.if_line]['cursor'] = 'UP'
                                                        else: pass
                                                    
                                                if 0 < self.if_line:
                                                    self.idd = self.if_line - 1
                                                    # previous input
                                                    self.input  = self.liste[self.idd]
                                                    # previous s
                                                    self.s      = self.sub_liste[self.idd]
                                                    # previous string
                                                    self.string = self.string_tabular[self.idd]
                                                    # restoring the prvious get of s
                                                    self.get    = self.memory[self.idd]
                                                    # restoring cursor position in the input
                                                    self.index  = self.tabular[self.idd]
                                                    # restoring cursor position in s
                                                    self.I      = self.sub_tabular[self.idd]
                                                    # restoring cursor position in string
                                                    self.I_S    = self.string_tab[self.idd]
                                                    # restoring the value of last
                                                    self.last   = self.last_tabular[self.idd]
                                                    # restoring remove_tab from index
                                                    self.remove_tab = self.remove_tabular[self.idd]
                                                    if self.drop_list_str:
                                                        self.str_drop_down = self.drop_list_str[ self.idd ]
                                                        self.drop = self.drop_list_id[ self.idd ]
                                                    else: pass
                                                    
                                                    self.if_line -= 1
                                                    self.indexation[self.if_line]['last']       = self.string
                                                    self.indexation[self.if_line]['cursor']     = 'UP'
                                                    self.indexation[self.if_line]['do']         = 'INDEX'
                                                    #################################################################
                                                    self.main_input, self.size = counter(self.if_line)
                                                    self.length = len(self.main_input)
                                                    self.last_line['now']  = self.if_line
                                                    #################################################################
                                                    
                                                    self.pos_x, self.pos_y = cursor_pos.cursor()
                                                    if self.max_y - int(self.pos_y) != self.max_y-1:
                                                        sys.stdout.write(bm.cursorPos.to(int(self.pos_x), int(self.pos_y)-1)) 
                                                        self.up_locked = False
                                                    else: self.up_locked = True
                                                else: pass
                                            except IndexError:
                                                pass
                                                # any changes here when local IndexError is detected
                                        else:  pass
                                    # get the next value stored in the list
                                    elif next2 == 66:
                                        if self.liste:
                                            try:
                                                if self.indexation[self.if_line]['cursor']   == 'NO': pass
                                                else : 
                                                    if self.indexation[self.if_line]['status'] == 'I': pass   
                                                    else:
                                                        if self.indexation[self.if_line]['action'] == 'FREE':
                                                            v = self.if_line
                                                            self.liste[v],self.sub_liste[v]                 = self.input, self.s
                                                            self.tabular[v], self.sub_tabular[v]            = self.index, self.I
                                                            self.last_tabular[v], self.remove_tabular[v]    = self.last, self.remove_tab
                                                            self.string_tab[v], self.string_tabular[v]      = self.I_S, self.string
                                                            self.memory[v], self.drop_list_str[v]           = self.get, self.str_drop_down
                                                            self.drop_list_id[v]                            = self.drop
                                                            
                                                            self.indexation[self.if_line]['action'] = 'LOCKED' 
                                                            self.indexation[self.if_line]['last'] = self.string
                                                            self.indexation[self.if_line]['cursor'] = 'DOWN'
                                                        else: pass
                                                    
                                                if self.if_line < self.if_line_max:
                                                    self.idd    = self.if_line + 1
                                                    self.input  = self.liste[self.idd]
                                                    # next s
                                                    self.s      = self.sub_liste[self.idd]
                                                    # next string
                                                    self.string = self.string_tabular[self.idd]
                                                    # restoring the prvious get of s
                                                    self.get    = self.memory[self.idd]
                                                    # restoring cursor position in the input
                                                    self.index  = self.tabular[self.idd]
                                                    # restoring cursor position in s
                                                    self.I      = self.sub_tabular[self.idd]
                                                    # restoring cursor position in string
                                                    self.I_S    = self.string_tab[self.idd]
                                                    # restoring the value of last
                                                    self.last   = self.last_tabular[self.idd]
                                                    # restoring remove_tab from index
                                                    self.remove_tab = self.remove_tabular[self.idd]
                                                    
                                                    if self.drop_list_str:
                                                        self.str_drop_down = self.drop_list_str[ self.idd ]
                                                        self.drop = self.drop_list_id[ self.idd ]
                                                    else: pass 
                                                    
                                                    self.indexation[self.if_line]['last']       = self.string
                                                    self.indexation[self.if_line]['cursor']     = 'DOWN'
                                                    self.indexation[self.if_line]['do']         = 'INDEX'
                                                    self.if_line += 1
                                                    #################################################################
                                                    self.main_input, self.size = counter(self.if_line)
                                                    self.length = len(self.main_input)
                                                    self.last_line['now']  = self.if_line
                                                    #################################################################
                                                    self.pos_x, self.pos_y = cursor_pos.cursor()
                                                    sys.stdout.write(bm.cursorPos.to(int(self.pos_x), int(self.pos_y)+1))                                                    
                                                else: pass
                                            except IndexError:
                                                # any changes here when local IndexError is detected
                                                pass
                                        else:   pass
                                    # ctrl-up is handled 
                                    elif next2 == 49:
                                        if self.str_drop_down:
                                            next3, next4, next5 = 0, 0, _[1] #ord(sys.stdin.read(1)), ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                                            if next5 in {67, 68}: pass # ctrl-left, ctrl-right is handled 
                                            # ctrl-up is handled 
                                            elif next5 == 65: 
                                                self.indicator = 65 
                                                if self.indicator_pos >= 1: self.indicator_pos -= 1
                                                else: pass 
                                            # ctrl-down is handled 
                                            elif next5 == 66: 
                                                self.indicator = 66
                                                if self.indicator_pos < self.indicator_max : self.indicator_pos += 1
                                                else: pass 
                                            else: pass
                                        else: pass
                                except IndexError:  pass
                            else:  pass
                        # delecting char
                        elif self.char in {8, 127}:
                            # if s is not empty
                            if self.s:
                                # initialize key name of an indentation case
                                self.name = 0
                                self.key = False

                                try:
                                    # checking if I > 0
                                    if self.I - 1 >= 0:
                                        # new char initialized
                                        self.char = self.get[self.I - 1]
                                        # writable char
                                        if 32 <= self.get[self.I - 1] <= 126:
                                            self.name = 1
                                            # delecting the value in get associated to the index I-1
                                            del self.get[self.I - 1]
                                        # indentation cas
                                        elif self.get[self.I - 1] in {9}:
                                            self.name = 1
                                            # when indentation is detected for loop is used to take into account the four value of space
                                            # it means that inden = " " * 4
                                            for i in range(4):
                                                # building input
                                                self.input = self.input[: self.index + self.last - self.name] + self.input[
                                                                                                                self.index + self.last:]
                                                # decreasing index of -1
                                                self.index     -= 1
                                                # building s
                                                self.s          = self.s[: self.I - 1] + self.s[self.I:]
                                                # decreating I of -1
                                                self.I         -= 1
                                                # delecting the value in get associated to the index I-1
                                                del self.get[self.I]

                                            # building string
                                            self.string = self.string[: self.I_S - 1] + self.string[self.I_S:]
                                            # decreasing I_S of -1
                                            self.I_S -= 1
                                            # set key of True
                                            self.key = True
                                        else:  pass

                                        # if key is False it means s has not indentation
                                        if self.key is False:
                                            # building input
                                            self.input = self.input[: self.index + self.last - self.name] + self.input[
                                                                                                            self.index + self.last:]
                                            # decreasing index of -name with name = 1
                                            self.index -= self.name
                                            # building s
                                            self.s      = self.s[: self.I - 1] + self.s[self.I:]
                                            # building string
                                            self.string = self.string[: self.I_S - 1] + self.string[self.I_S:]
                                            # decreasing I and I_S of -1
                                            self.I     -= 1
                                            self.I_S   -= 1
                                        else:   pass
                                        
                                        # fixing the cursor position conditions
                                        if self.max_x >= int(self.pos_x) and  len(self.s) <= self.max_x : self.border_x_limit = True 
                                        else: self.border_x_limit = False 
                                    else:  pass
                                except IndexError:  pass
                            else: pass
                        # indentation Tab
                        elif self.char == 9:
                            if self.border_x_limit is True:
                                self.pos_x, self.pos_y = cursor_pos.cursor()
                                if (self.max_x - int(self.pos_x)) >= 5:
                                    self.tt         = '    '
                                    self.input      = self.input[: self.index + self.last] + str(self.tt) + self.input[
                                                                                                    self.index + self.last:]
                                    self.s          = self.s[: self.I] + str(self.tt) + self.s[self.I:]
                                    # string takes the true value of char
                                    self.string     = self.string[: self.I_S] + chr(self.char) + self.string[self.I_S:]
                                    self.index     += 4
                                    self.I         += 4
                                    self.I_S       += 1

                                    for i in range(4):
                                        self.get.append(self.char)
                                else: pass 
                                
                                if len(self.s) <= self.max_x : self.border_x_limit = True 
                                else: self.border_x_limit = False
                            else: pass
                        # clear entire string ctrl+l
                        elif self.char == 12:
                            # move cursor left
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            # clear entire line
                            sys.stdout.write(bm.clear.line(pos=0))
                            # write main_input
                            sys.stdout.write(self.main_input)
                            # move cursor left egain
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                            # initialization block
                            self.input  = self.main_input
                            self.index  = self.length
                            self.s      = ''
                            self.string = ''
                            self.I      = 0
                            self.I_S    = 0
                            self.get    = []
                            self.idd    = 0
                            self.last   = 0
                            self.remove_tab = 0
                        # move cursor at end of line ctrl+d
                        elif self.char == 4:
                            while self.I < len(self.s):
                                try:
                                    # without indentation
                                    if 32 <= self.get[self.I] <= 126:
                                        self.I     += 1
                                        self.index -= 1
                                        self.last  += 2
                                        self.I_S   += 1
                                    # when identation is detected
                                    elif self.get[self.I] == 9:
                                        self.I     += 4
                                        self.index -= 4
                                        self.last  += 8
                                        self.I_S   += 4
                                except IndexError:  pass
                        # move cursor at the beginning of line ctrl+q
                        elif self.char in{1, 17}: 
                            while self.I > 0:
                                try:
                                    # without indentation
                                    if 32 <= self.get[self.I - 1] <= 126:
                                        self.I     -= 1
                                        self.index += 1
                                        self.last  -= 2
                                        self.I_S   -= 1
                                    # when identation is detected
                                    elif self.get[self.I - 1] == 9:
                                        self.I     -= 4
                                        self.index += 4
                                        self.last  -= 8
                                        self.I_S   -= 4
                                except IndexError:  pass
                        # clear entire screen and restore cursor position ctrl+s
                        elif self.char == 19: 
                            self.indicator = self.char 
                        # crtl+g
                        elif self.char == 7: # crtl+g
                            self.indicator = self.char               
                        # auto slection mode ctrl+n
                        elif self.char == 14:
                            self.indicator = self.char
                        # End-Of-File Error ctrl+z
                        elif self.char == 26:
                            sys.stdout.write(bm.clear.screen(pos=1))
                            sys.stdout.write(bm.cursorPos.to(0,0))
                            sys.stdout.write(bm.clear.screen(pos=0))
                            sys.stdout.write(bm.move_cursor.DOWN(pos=1))
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            sys.stdout.write(bm.clear.line(pos=0))
                            self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                            print(self._end_of_file_)
                            return
                        # printing and initializing of values "enter"
                        elif self.char in {10, 13}:
                            # storing input
                            self.pos_x, self.pos_y = cursor_pos.cursor()
                            self.if_line_max    += 1
                            self.if_line        += 1
                        
                            if self.indexation[self.if_line-1]['cursor'] == 'NO':
                                v = self.if_line-1
                                if self.indexation[self.if_line-1]['do'] == 'ADDS':
                                    self.liste.append(self.input)
                                    self.sub_liste.append(self.s), self.tabular.append(self.index), self.sub_tabular.append(self.I)
                                    self.last_tabular.append(self.last),self.remove_tabular.append(self.remove_tab)
                                    self.string_tab.append(self.I_S), self.string_tabular.append(self.string)
                                    self.memory.append(self.get) , self.drop_list_str.append( self.str_drop_down)
                                    self.drop_list_id.append(self.drop)
                                elif self.indexation[self.if_line-1]['do'] == 'INSERTS':
                                    self.liste.insert(v, self.input),        self.sub_liste.insert(v, self.s)
                                    self.tabular.insert(v, self.index),      self.sub_tabular.insert(v, self.I) 
                                    self.last_tabular.insert(v, self.last),  self.remove_tabular.insert(v, self.remove_tab)   
                                    self.string_tab.insert(v, self.I_S) ,    self.string_tabular.insert(v, self.string )    
                                    self.memory.insert(v, self.get)                                            
                                    self.drop_list_str.insert(v, self.str_drop_down) , self.drop_list_id.insert(self.if_line,  self.drop)
                                    
                                    for k in range(self.if_line_max - self.if_line):
                                        self.indexation[self.if_line+k] = {'action' : 'FREE', 'status' : 'I', 'do' : 'ADDS', 'cursor' : 'NO', 'last'   : '' }
                                        self.indexation[self.if_line+k]['status']   = 'I' 
                                        self.indexation[self.if_line+k]['action']   = 'LOCKED'  
                                        self.indexation[self.if_line+k]['cursor']   = 'ENTER' 
                                        self.indexation[self.if_line+k]['do']       = 'NOTHING'
                                        self.indexation[self.if_line+k]['last']     = self.string_tabular[self.if_line+k]
                            else:
                                if self.indexation[self.if_line-1]['action'] == 'FREE':
                                    if self.indexation[self.if_line-1]['cursor'] in ['UP', 'DOWN']:
                                        v = self.if_line-1
                                        self.liste[v],self.sub_liste[v]                 = self.input, self.s
                                        self.tabular[v], self.sub_tabular[v]            = self.index, self.I
                                        self.last_tabular[v], self.remove_tabular[v]    = self.last, self.remove_tab
                                        self.string_tab[v], self.string_tabular[v]      = self.I_S, self.string
                                        self.memory[v], self.drop_list_str[v]           = self.get, self.str_drop_down
                                        self.drop_list_id[v]                            = self.drop  
                                        v += 1
                                        self.liste.insert(v, ''),      self.sub_liste.insert(v, '')
                                        self.tabular.insert(v, 0),      self.sub_tabular.insert(v, 0) 
                                        self.last_tabular.insert(v, 0),  self.remove_tabular.insert(v, 0)   
                                        self.string_tab.insert(v, 0) ,    self.string_tabular.insert(v, '' )    
                                        self.memory.insert(v, [])                                            
                                        self.drop_list_str.insert(v, '') , self.drop_list_id.insert(self.if_line,  0)
                                        
                                        self.indexation[self.if_line_max] = {'action' : 'FREE', 'status' : 'I', 'do' : 'ADDS', 'cursor' : 'NO', 'last'   : '' }
                                        self.indexation[self.if_line_max]['status']   = 'I' 
                                        self.indexation[self.if_line_max]['action']   = 'LOCKED'  
                                        self.indexation[self.if_line_max]['cursor']   = 'ENTER' 
                                        self.indexation[self.if_line_max]['do']       = 'NOTHING'
                                        self.indexation[self.if_line_max]['last']     = self.string_tabular[-1]
                                    else:
                                        self.liste.insert(v, self.input),        self.sub_liste.insert(v, self.s)
                                        self.tabular.insert(v, self.index),      self.sub_tabular.insert(v, self.I) 
                                        self.last_tabular.insert(v, self.last),  self.remove_tabular.insert(v, self.remove_tab)   
                                        self.string_tab.insert(v, self.I_S) ,    self.string_tabular.insert(v, self.string )    
                                        self.memory.insert(v, self.get)                                            
                                        self.drop_list_str.insert(v, self.str_drop_down) , self.drop_list_id.insert(self.if_line,  self.drop)
                                else: pass
                            
                            if self.index > 0:
                                pos = len(self.s) + self.size + len(self.input) - self.index
                                sys.stdout.write(bm.move_cursor.RIGHT(pos=pos))
                            else: pass
                            
                            # move cursor of left
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                            if terminal_name == 'orion': 
                                sys.stdout.write(self.main_input + self.bold+bm.words(string=self.s, color=bm.fg.rbg(255,  255, 255)).final()+
                                            bm.move_cursor.RIGHT(pos=self.max_x-1)+bm.clear.line(pos=0)+self.black+f"{self.acs['v']}"+
                                            self.reset+bm.move_cursor.LEFT(pos=int(self.pos_x))+'\n')
                                
                                if self.if_line !=  self.if_line_max:
                                    if self.sub_liste[self.if_line : ]:
                                        sys.stdout.write(bm.save.save)
                                        sys.stdout.write(bm.clear.screen(pos=0))
                                        _id_ = 0
                                       
                                        for _ss_ in  self.sub_liste[self.if_line : ]:
                                            __s__, __l__ = counter(self.if_line+_id_)
                                            sys.stdout.write( __s__+ self.bold+bm.words(string=_ss_, color=bm.fg.rbg(255,  255, 255)).final()+
                                                    bm.move_cursor.RIGHT(pos=self.max_x-1)+bm.clear.line(pos=0)+self.black+f"{self.acs['v']}"+
                                                    self.reset+bm.move_cursor.LEFT(pos=int(self.pos_x)) + "\n")
                                            _id_ += 1
                                        sys.stdout.write(bm.save.restore)
                                    else: pass
                                else: pass
                            else:   print(self.main_input + self.bold+bm.fg.rbg(255, 255, 255) + self.s + bm.init.reset)
                                
                            if self.string: pass
                            else: pass

                            # initialization block
                            self.indexation[self.if_line-1]['last'] = self.string
                            self.main_input, self.size = counter(self.if_line)
                            self.input          = self.main_input
                            self.index          = len(self.main_input)
                            self.s              = ''
                            self.string         = ''
                            self.I              = 0
                            self.I_S            = 0
                            self.get            = []
                            self.idd            = 0
                            self.last           = 0
                            self.remove_tab     = 0
                            self.str_drop_down  = ''
                            self.drop           = 0   
                            self.drop_drop      = {'id':[], 'str':[]}     
                            self.drop_idd       = 0 
                            self.border_x_limit = True 
                            self.last_line['now']  = self.if_line
                            self.indexation[self.if_line-1]['status'] = 'I' 
                            self.indexation[self.if_line-1]['action'] = 'LOCKED'
                            self.indexation[self.if_line-1]['do']     = 'NOTHING'
                            self.indexation[self.if_line-1]['cursor'] = 'ENTER'
                            self.indexation[self.if_line] = {'action' : 'FREE', 
                                                            'status' : 'I', 
                                                            'do' : 'ADDS', 
                                                            'cursor' : 'NO', 
                                                            'last'   : '' }
                            self.indexation[self.if_line]['status']   = 'I' 
                            self.indexation[self.if_line]['action']   = 'FREE'  
                            self.indexation[self.if_line]['cursor']   = 'NO' 
                            self.indexation[self.if_line]['last']     = ''
                            
                            if self.if_line == self.if_line_max: self.indexation[self.if_line]['do']     = 'ADDS' 
                            else: self.indexation[self.if_line]['do']   = 'INSERTS' 
                            
                            if self.last_line['last'] >= int(self.pos_y):
                                sys.stdout.write(self.input)
                                sys.stdout.write(bm.move_cursor.RIGHT(pos=self.max_x-1)+self.black+f"{self.acs['v']}")
                                sys.stdout.write(bm.move_cursor.LEFT(pos=self.max_x-self.size-1))
                            else:
                                self.last_line['last'] = self.if_line_max
                                sys.stdout.write(bm.cursorPos.to(self.size, self.if_line+4))
                            
                        try:
                            if self.indexation[self.if_line]['last'] != self.string:
                                self.indexation[self.if_line]['status']  = 'D' 
                                self.indexation[self.if_line]['action'] = 'FREE'
                            else: 
                                self.indexation[self.if_line]['status'] = 'I'
                                if  self.indexation[self.if_line]['cursor'] == 'NO': pass
                                else: self.indexation[self.if_line]['action'] = 'LOCKED'
                        except KeyError: pass
                        
                        self.pos_x, self.pos_y      = cursor_pos.cursor()
                        # move cursor on left
                        sys.stdout.write(bm.cursorPos.to(self.size+1, self.pos_y))
                        # clear entire line
                        sys.stdout.write(bm.clear.line(pos=0))
                        
                        if terminal_name == 'orion':
                            sys.stdout.write(
                                bm.string().syntax_highlight(
                                name=bm.words(string=self.s, color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final())+
                                bm.move_cursor.RIGHT(pos=self.max_x-1)+
                                self.black+f"{self.acs['v']}"+ bm.cursorPos.to(self.pos_x, self.pos_y)
                                )
                        else: sys.stdout.write(self.main_input + bm.init.bold+bm.fg.rbg(255, 255, 255) + self.s + bm.init.reset)
                        
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        
                        if self.index > 0:
                            # computing the right position 
                            pos = len(self.s) + self.size + len(self.input) - self.index
                            # putting cursor a the correct position 
                            sys.stdout.write(bm.move_cursor.RIGHT(pos=pos))
                        else: pass
                        
                        self.pos_x, self.pos_y      = cursor_pos.cursor()
                        
                        if self.indicator == 19: 
                            if self.data_storing_file['name'] is None:
                                if self.string_tabular:
                                    sys.stdout.write(bm.save.save)
                                    self.data_storing_file = figure_file.files(self.data_storing_file, self.string_tabular).save()
                                    sys.stdout.write(bm.move_cursor.UP(pos=5))
                                    sys.stdout.write(bm.clear.screen(pos=0))
                                    sys.stdout.write(bm.save.restore)
                                else: pass
                            else: 
                                if self.string_tabular:  write_in_file(self.data_storing_file['name'], self.string_tabular)
                                else: pass
                            self.indicator = None
                        else: pass
                        
                        if self.last_line['now'] == self.last_line['last']: 
                            if self.last_line['last'] >= int(self.pos_y): 
                                sys.stdout.write(bm.move_cursor.RIGHT(pos=self.max_x-1)+
                                    self.black+f"{self.acs['v']}")
                                sys.stdout.write(bm.cursorPos.to(self.pos_x, int(self.pos_y)))
                            else:
                                sys.stdout.write(bm.clear.screen(0))
                                sys.stdout.write(bm.move_cursor.RIGHT(pos=self.max_x-1)+
                                    self.black+f"{self.acs['v']}")
                                sys.stdout.write(bm.move_cursor.DOWN(pos=1))
                                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                bottom(self.max_x)
                                sys.stdout.write(bm.cursorPos.to(self.pos_x, int(self.pos_y)-1))
                        else: 
                            if self.last_line['last'] >= int(self.pos_y): 
                                sys.stdout.write(bm.move_cursor.RIGHT(pos=self.max_x-1)+
                                    self.black+f"{self.acs['v']}")
                                sys.stdout.write(bm.cursorPos.to(self.pos_x, self.pos_y))
                            else:
                                sys.stdout.write(bm.cursorPos.to(1000, self.last_line['last']+4))
                                sys.stdout.write(bm.clear.screen(0))
                                sys.stdout.write(bm.move_cursor.DOWN(pos=1))
                                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                bottom(self.max_x)
                                sys.stdout.write(bm.cursorPos.to(self.pos_x, int(self.pos_y)-1))
                             
                        if self.indexation[self.if_line]['cursor'] == "UP":
                            if self.up_locked is False : pass 
                            else:
                                self.np += 1
                                sys.stdout.write(bm.clear.screen(2))
                                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                
                                for i in range(self.if_line, self.if_line_max-self.np+1):
                                    try: self.s = self.sub_liste[i]
                                    except IndexError: self.s = ""
                                    self.main_input, self.size = counter(i)
                                    sys.stdout.write(bm.clear.line(pos=0))
                                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                    sys.stdout.write(
                                        self.main_input+
                                        bm.string().syntax_highlight(
                                        name=bm.words(string=self.s, color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final())+
                                        bm.move_cursor.RIGHT(pos=self.max_x-1)+
                                        self.black+f"{self.acs['v']}"+ '\n'
                                        )
                                    self.pos_x, self.pos_y      = cursor_pos.cursor()
                                bottom(self.max_x)
                                
                                self.index  = self.tabular[self.if_line]
                                self.input  = self.liste[self.if_line]
                                self.s      =  self.sub_liste[self.if_line]
                                
                                sys.stdout.write(bm.cursorPos.to(x=self.size, y=1))
                                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                
                                if self.index > 0:
                                    # computing the right position 
                                    pos = len(self.s) + self.size + len(self.input) - self.index
                                    # putting cursor a the correct position 
                                    sys.stdout.write(bm.move_cursor.RIGHT(pos=pos))
                                else: pass
                                
                                if self.if_line == 0:  self.up_locked=False
                                else: pass
                        else: pass 
                        
                        try:     
                            if self.indexation[self.if_line-1]['cursor'] == "DOWN":
                                if int(self.pos_y) > self.max_y - 2:
                                    if self.np > 0:
                                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                        sys.stdout.write(bm.clear.screen(pos=0))
                                        sys.stdout.write(
                                            self.main_input+
                                            bm.string().syntax_highlight(
                                            name=bm.words(string=self.s, color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final())+
                                            bm.move_cursor.RIGHT(pos=self.max_x-1)+
                                            self.black+f"{self.acs['v']}"+"\n"
                                            )
                                        sys.stdout.write(bm.clear.screen(pos=0))
                                        sys.stdout.write(bm.move_cursor.UP(pos=1))
                                        sys.stdout.write(bm.move_cursor.RIGHT(pos=self.size))
                                        self.pos_x, self.pos_y      = cursor_pos.cursor()
                                        sys.stdout.write(bm.move_cursor.DOWN(pos=1)+bm.move_cursor.LEFT(pos=1000))
                                        bottom(self.max_x)
                                        sys.stdout.write(bm.cursorPos.to(self.pos_x, self.pos_y))
                                        self.np -= 1
                                        if self.np == 0: self.indexation[self.if_line-1]['cursor'] = 'NO' 
                                        else: pass 
                                        
                                    else: pass
                            else: pass
                        except KeyError : pass 
                        
                        #sys.stdout.write(f"{self.if_line_max} - {self.if_line} - {self.pos_y} - {self.max_y} - {self.indexation[self.if_line-1]['cursor']}")
                        sys.stdout.flush()
                    else: pass
                else: pass
            except KeyboardInterrupt:
                #os.system('cls')
                sys.stdout.write(bm.clear.screen(2)+bm.cursorPos.to(0, 0))
                self._keyboard_ = bm.bg.red_L + bm.fg.rbg(255,255,255) +"KeyboardInterrupt" + bm.init.reset
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000)+f"{self._keyboard_}\n")
                return
            except ValueError:
                os.system('cls')
                self._end_of_file_ = bm.bg.red_L + bm.fg.rbg(255,255,255) + "EOFError" + bm.init.reset
                print(self._end_of_file_)
                self.input = '{}>>> {}'.format(self.c, bm.init.reset)
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.flush()
            except IndexError: pass


if __name__ == '__main__':
    
    term = 'orion'
    try:
        #os.system('cls')
        sys.stdout.write(bm.clear.screen(2))
        #sys.stdout.write(bm.clear.move_and_clear(2))
        sys.stdout.write(bm.save.save)
        data_base = db.DATA_BASE().STORAGE().copy()
        windows( data_base=data_base).terminal(c=bm.fg.rbg(255, 255, 255), terminal_name=term)
    except KeyboardInterrupt:  pass
    except IndexError: pass
    
    
    
    