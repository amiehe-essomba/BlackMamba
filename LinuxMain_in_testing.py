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
############################################
# **created by : amiehe-essomba            #
# **updating by: amiehe-essomba            #
# ** copyright 2022 amiehe-essomba         #         
############################################
#############################################################


import sys, os
from script.STDIN.LinuxSTDIN                import readchar
from script.LEXER.FUNCTION                  import main
from script.PARXER.WINParxer                import parxer
from script.DATA_BASE                       import data_base as db
from script                                 import control_string
from script.STDIN.LinuxSTDIN                import bm_configure as bm
from IDE.EDITOR                             import string_buid as SB
from IDE.EDITOR                             import pull_editor as PE
from IDE.EDITOR                             import left_right as LR
from IDE.EDITOR                             import cursor
from IDE.EDITOR                             import test 
from IDE.EDITOR                     		import header
from IDE.EDITOR                             import true_cursor_pos as cursor_pos

class linux:
    def __init__(self, data_base: dict):

        # main data base
        self.data_base  = data_base
        # contriling string
        self.analyse    = control_string.STRING_ANALYSE(self.data_base, 1)

    def terminal(self, c: str = '', terminal_name : str = 'pegasus'):

        # set color on yellow
        self.bold           = bm.init.bold
        self.c              = bm.fg.rbg(255, 255, 0)
        if terminal_name == 'orion': pass
        else: self.c        = c
        # reset color
        self.reset          = bm.init.reset
        # input initialized
        self.input          = '{}{} {}'.format(self.c, chr(9654)*3, self.reset)
        # input main used to build the final string s
        self.main_input     = '{}{} {}'.format(self.c, chr(9654)*3, self.reset)
        # initial length of the input
        self.length         = len(self.input)
        # initialisation of index associated to the input
        self.index          = self.length
        # length of the foutth first char of input
        self.size           = len('>>> ')
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
        ###########################################################
        # accounting line
        self.if_line        = 0
        # error variable
        self.error          = None
        # accounting space line
        self.space          = 0
        # detecting if indentation was used
        self.active_tab     = None
        # history of commands
        ###########################################################
        # clear entire line
        sys.stdout.write(bm.clear.line(pos=0))
        # move cursor left
        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
        # print the input value
        sys.stdout.write(self.input)
        # save cursor position
        #sys.stdout.write(bm.save.save)
        # flush
        sys.stdout.flush()
        ###########################################################
        self.pos_x, self.pos_y      = cursor_pos.cursor()
        self.pos_x, self.posy       = int(self.pos_x), int( self.pos_y)
        self.max_x, self.max_y      = test.get_linux_ter()
        self.key_max_activation     = True
        self.save_cursor_position   = bm.save.save
        self.indicator_pos          = 0
        self.indicator_max          = 1
            
        ###########################################################
        
        while True:
            try:
                # get input
                self.char = readchar.readchar()#; print(self.char)
                
                #building of str_drop_down only when ord( self.char ) is in self.sss 
                if 32 <= self.char <= 126:
                    sys.stdout.write(bm.clear.screen(pos=0))
                    if chr(self.char) in self.sss:
                        self.str_drop_down = self.str_drop_down[ : self.drop] + chr( self.char ) + self.str_drop_down[ self.drop : ]
                        self.drop += 1
                    else:
                        # initialization
                        self.drop_drop['id'].append( self.drop )
                        self.drop_drop['str'].append( self.str_drop_down) 
                        self.drop = 0
                        self.str_drop_down = ""
                #delecting char in the str_drop_down string 
                elif self.char in {8, 127}:
                    sys.stdout.write(bm.clear.screen(pos=0))
                    if self.str_drop_down:
                        # dropsown string :
                        self.str_drop_down = self.str_drop_down[ : self.drop - 1] + self.str_drop_down[ self.drop : ]
                        # dropdown index 
                        self.drop    -= 1
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
                    # building input
                    self.input  = self.input[: self.index + self.last] + chr(self.char) + self.input[
                                                                                         self.index + self.last:]
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
                # moving cursor up, down, left, reight
                elif self.char == 27:
                    next1, next2 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
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
                                        # idd is decreased of -1
                                        self.idd -= 1
                                        if len(self.liste) >= abs(self.idd):
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
                                        else:  self.idd += 1
                                    except IndexError:
                                        # any changes here when local IndexError is detected
                                        pass
                                else:   pass
                            # get the next value stored in the list
                            elif next2 == 66:
                                if self.liste:
                                    try:
                                        # idd is increased of 1
                                        self.idd += 1
                                        # next input
                                        if len(self.liste) > self.idd:
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
                                        else: self.idd -= 1
                                    except IndexError:
                                        # any changes here when local IndexError is detected
                                        pass
                                else:   pass
                            # ctrl-up is handled 
                            elif next2 == 49:
                                if self.str_drop_down:
                                    next3, next4, next5 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
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
                            else:  pass
                        except IndexError:  pass
                    else: pass
                # indentation Tab
                elif self.char == 9:

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
                elif self.char == 17: 
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
                    sys.stdout.write(bm.clear.screen(pos=1))
                    sys.stdout.write(bm.cursorPos.to( self.pos_x, 0))
                    sys.stdout.write(bm.save.save)
                    #header.header()
                    self.pos_x, self.pos_y = cursor_pos.cursor()
                    self.pos_x, self.posy = int(self.pos_x), int( self.pos_y)
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
                    sys.stdout.write(bm.clear.screen(pos=0))
                    if self.index > 0:
                        pos = len(self.s) + self.size + len(self.input) - self.index
                        sys.stdout.write(bm.move_cursor.RIGHT(pos=pos))
                    else: pass
                    self.if_line += 1
                    # move cursor of left
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    # print the final input with its transformations
                    if terminal_name == 'orion': print(self.main_input + self.bold+bm.words(string=self.s, color=bm.fg.rbg(255,  255, 255)).final())
                    else:   print(self.main_input + self.bold+bm.fg.rbg(255, 255, 255) + self.s + bm.init.reset)

                    # storing input
                    self.liste.append(self.input)
                    # storing s
                    self.sub_liste.append(self.s)
                    # storing index
                    self.tabular.append(self.index)
                    # storing I
                    self.sub_tabular.append(self.I)
                    # storing last
                    self.last_tabular.append(self.last)
                    # storing remove_tab
                    self.remove_tabular.append(self.remove_tab)
                    # storing I_S
                    self.string_tab.append(self.I_S)
                    # storing string
                    self.string_tabular.append(self.string)
                    # storing get
                    self.memory.append(self.get)
                    # storing str_drop_down
                    self.drop_list_str.append( self.str_drop_down)
                    # storing str_drop_down index
                    self.drop_list_id.append(self.drop)
                    
                    if self.string:
                        # running lexer
                        self.lexer, self.normal_string, self.error = main.MAIN(self.string, self.data_base, self.if_line).MAIN()
                        if self.error is None :
                            if self.lexer is not None:
                               
                                # running parser
                                self.num, self.key, self.error = parxer.ASSEMBLY(self.lexer, self.data_base,
                                        self.if_line).GLOBAL_ASSEMBLY(main_string=self.normal_string, interpreter = False, term=terminal_name)
                                if self.error is None: pass
                                else:
                                    sys.stdout.write(bm.clear.line(2))
                                    sys.stdout.write(bm.move_cursor.LEFT(1000))
                                    print('{}\n'.format(bm.init.bold+self.error))
                                    self.error = None
                            else:  pass
                        else:
                            sys.stdout.write(bm.clear.line(2))
                            sys.stdout.write(bm.move_cursor.LEFT(1000))
                            print('{}\n'.format(bm.init.bold+self.error))
                            self.error = None
                    else: pass

                    # initialization block
                    self.input          = self.main_input
                    self.index          = self.length
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
                    self.pos_x, self.pos_y = cursor_pos.cursor()
                    
                    if   (int(self.max_y)-int(self.pos_y)) > 14 : self.key_max_activation = True
                    else: self.key_max_activation = False
                    
                    if self.key_max_activation  is False: pass
                    else:
                        if (int(self.max_x)-int(self.pos_x)) > 20 : self.key_max_activation = True
                        else: self.key_max_activation = False

                # move cursor on left
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                # clear entire line
                sys.stdout.write(bm.clear.line(pos=0))

                if terminal_name == 'orion':
                    # key word activation
                    sys.stdout.write(self.main_input + bm.string().syntax_highlight(
                        name=bm.words(string=self.s, color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()))
                else:
                    # any activation keyword
                    sys.stdout.write(self.main_input + bm.init.bold+bm.fg.rbg(255, 255, 255) + self.s + bm.init.reset)
                # move cusror on left egain
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                # put cursor on the right position
                if self.index > 0:
                    pos = len(self.s) + self.size + len(self.input) - self.index
                    sys.stdout.write(bm.move_cursor.RIGHT(pos=pos))
                else: pass

                if self.str_drop_down:
                    if self.key_max_activation is True:
                        sys.stdout.write(bm.save.save)
                        if self.indicator is None:
                            v, self.indicator_max = PE.DropDown(data_base = self.data_base,line=self.if_line).MENU( self.str_drop_down, 
                                                                                            self.string, self.indicator, self.indicator_pos)
                        else:
                            sys.stdout.write(bm.clear.screen(pos=0))
                            v, self.indicator_max = PE.DropDown(data_base = self.data_base, line=self.if_line).MENU( self.str_drop_down, 
                                                                            self.string, self.indicator, self.indicator_pos)
                            if v is not  None:
                                if self.indicator == 7: sys.stdout.write(bm.move_cursor.UP(pos=1))
                                if self.indicator in {65, 66} : sys.stdout.write(bm.save.restore)
                                else: pass        
                                try:
                                    if self.indicator not in {65, 66}:
                                        self.string = self.string[ : len(self.string)-len(self.str_drop_down)] + v 
                                        self.error,  kappa, self.pos, self.get = SB.string( self.string ).build()

                                        self.input  = kappa[0][0]
                                        self.index  = kappa[0][1]
                                        self.s      = kappa[1][0]
                                        self.I      = kappa[1][1]
                                        self.string = kappa[2][0]
                                        self.I_S    = kappa[2][1]

                                        if self.indicator == 14: self.str_drop_down = v; self.drop = len(v)
                                        else: pass
                                        # move cursor on left
                                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                        # clear entire line
                                        sys.stdout.write(bm.clear.line(pos=0))
                                        sys.stdout.write(self.main_input+bm.string().syntax_highlight(name=bm.words(string=self.s, color=bm.fg.rbg(255, 255, 255)).final()))
                                        sys.stdout.write(bm.save.save)
                                    else: pass
                                except  TypeError: pass 
                            else:
                                sys.stdout.write(bm.move_cursor.UP(pos=1))

                                if self.index > 0:
                                    pos = len(self.s) + self.size + len(self.input) - self.index
                                    sys.stdout.write(bm.move_cursor.RIGHT(pos=pos))
                                else: pass
                                sys.stdout.write(bm.save.save)
                        sys.stdout.write(bm.save.restore)
                    else: pass
                else: pass 
                if self.indicator in {65, 66}: pass 
                else:   self.indicator_pos, self.indicator_max = 0, 1
                self.indicator = None
                sys.stdout.flush()
            except KeyboardInterrupt:
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                return
            except SyntaxError:
                self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                print(self._end_of_file_)
                self.input = '{}>>> {}'.format(self.c, bm.init.reset)
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.flush()

if __name__ == '__main__':
    
    terminal = 'orion'
    try:
        os.system('clear')
        sys.stdout.write(bm.save.save)
        #bm.head().head(sys='Linux', term = terminal)
        header.header()
        data_base = db.DATA_BASE().STORAGE().copy()
        linux( data_base=data_base).terminal(c=bm.fg.rbg(255, 255, 255), terminal_name=terminal)
    except KeyboardInterrupt:  pass
    except SyntaxError: pass
