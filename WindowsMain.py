############################################################
#############################################################
# Black Mamba orion and pegasus code iditor for Windows     #
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
# **copyright 2023 amiehe-essomba          #         
############################################
#############################################################

import sys, os
from ctypes                     import windll
from script.LEXER.FUNCTION      import main
from script                     import control_string
from script.PARXER.WINParxer    import parxer
from script.STDIN.LinuxSTDIN    import bm_configure     as bm
from script.DATA_BASE           import data_base        as db
#from rich.console               import Console
from IDE.EDITOR                 import header, string_to_chr 

#console = Console()


class windows:
    def __init__(self, data_base : dict):
        # main data base
        self.data_base  = data_base
        # string module analyses 
        self.analyse    = control_string.STRING_ANALYSE(self.data_base, 1)

    def terminal(self, c: str = '', terminal_name : str = 'pegasus'):
        # input initialization
        self.y = bm.init.bold + bm.fg.rbg(255, 255, 0)
        self.input      = '{}>>>{} {}'.format(self.y , c, bm.init.reset)
        # root of input 
        self.main_input = '{}>>>{} {}'.format(self.y, c, bm.init.reset)
        # lenght of the root 
        self.length     = len(self.input)
        # index initialization 
        self.index      = self.length
        # length of the fouth first char of input
        self.size           = len('>>> ')
        # sub length initialization 
        self.sub_length = len('{}{}{}'.format(self.y, c, bm.init.reset))
        # index char in Input 
        self.Index      = 0      
        # line        
        self.line       = 0    
        # key         
        self.key        = False  
        # String used in BM for calculations        
        self.mainString = ''      
        # String index      
        self.mainIndex  = 0    
        # save cursor position          
        self.cursor     = []
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
        # false if clean line is not activated else true
        self.clear_line = False         
        k  = windll.kernel32
        k.SetConsoleMode( k.GetStdHandle(-11), 7)
        
        # write input initialized 
        sys.stdout.write(bm.string().syntax_highlight(name=self.input))
        #flush 
        sys.stdout.flush()
        
        while True:
            try:
                #self.char_ = keyboard.read_key()  #bm.read().readchar()
                self.char = string_to_chr.convert()#string( self.char_)
                if self.char :  
                    if 32 <= self.char[0] <= 126:
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
                    elif self.char[0] in {8, 127}:
                        sys.stdout.write(bm.clear.screen(pos=0))
                        if self.str_drop_down:
                            # dropsown string :
                            self.str_drop_down = self.str_drop_down[ : self.drop - 1] + self.str_drop_down[ self.drop : ]
                            # dropdown index 
                            self.drop    -= 1
                        else: pass
                    else:
                        if self.char[0] in [10, 13, 27, 7, 14]: pass 
                        else:
                            # initialization
                            self.drop_drop['id'].append( self.drop )
                            self.drop_drop['str'].append( self.str_drop_down) 
                            self.drop = 0
                            self.str_drop_down = ""
                            sys.stdout.write(bm.clear.screen(pos=0))
                    
                    # breaking loop while with the keyboardError ctrl+c
                    if self.char[0] == 3:
                        sys.stdout.write(bm.clear.screen(pos=1))
                        sys.stdout.write(bm.cursorPos.to(0,0))
                        sys.stdout.write(bm.clear.screen(pos=0))
                        sys.stdout.write(bm.move_cursor.DOWN(pos=1))
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        sys.stdout.write(bm.clear.line(pos=0))
                        self._keyboard_ = bm.init.bold + bm.bg.rgb(255, 0, 0) + bm.fg.rbg(255,255,255) + "KeyboardInterrupt" + bm.init.reset
                        print(self._keyboard_)
                        return
                    elif 32 <= self.char[0] <= 126:
                        ######################################
                        # each character has 1 as length     #
                        # have a look on ansi char           #
                        ######################################
                        # building input
                        self.input       = self.input[ : self.index + self.last ] + chr( self.char[0] ) + self.input[ self.index +self.last : ]
                        self.mainString  = self.mainString[ : self.mainIndex ] + chr( self.char[0] ) + self.mainString[ self.mainIndex : ]
                        self.string = self.string[: self.I_S] + chr( self.char[0] ) + self.string[self.I_S:]
                        self.index       += 1
                        self.mainIndex   += 1
                        self.I_S         += 1
                        # storing char in get
                        self.get.append(self.char[0])
                    elif self.char[0] == 27:
                        next2, next1 = self.char[1],  91
                        #rint(next1, next2)
                        if next1 == 91:
                            try:
                                # move cursor to left <-
                                if   next2 == 68:
                                    if self.I > 0:
                                        try:
                                            # without indentation
                                            if 32 <= self.get[self.I - 1] <= 126:
                                                self.mainIndex      -= 1
                                                self.index          += 1
                                                self.last           -= 2
                                                self.I_S            -= 1
                                                
                                                self.str_drop_down, self.drop = LR.String( self.string, self.I_S, self.sss )
                                            # when identation is detected
                                            elif self.get[self.I - 1] == 9:
                                                self.mainIndex      -= 4
                                                self.index          += 4
                                                self.last           -= 8
                                                self.I_S            -= 4
                                        except IndexError: pass
                                    else:  pass
                                # move cursor to right ->
                                elif next2 == 67:
                                    if self.I < len(self.s):
                                        try:
                                            # without indentation
                                            if 32 <= self.get[self.I] <= 126:
                                                self.mainIndex  += 1
                                                self.index      -= 1
                                                self.last       += 2
                                                self.I_S        += 1
                                                self.str_drop_down, self.drop = LR.String( self.string, self.I_S, self.sss )
                                            # when identation is detected
                                            elif self.get[self.I] == 9:
                                                self.mainIndex      += 4
                                                self.index          -= 4
                                                self.last           += 8
                                                self.I_S            += 4
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
                                                self.input          = self.liste[self.idd]
                                                # previous s
                                                self.s              = self.sub_liste[self.idd]
                                                # previous string
                                                self.string         = self.string_tabular[self.idd]
                                                # restoring the prvious get of s
                                                self.get            = self.memory[self.idd]
                                                # restoring cursor position in the input
                                                self.index          = self.tabular[self.idd]
                                                # restoring cursor position in s
                                                self.mainIndex      = self.sub_tabular[self.idd]
                                                # restoring cursor position in string
                                                self.I_S            = self.string_tab[self.idd]
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
                                                self.input          = self.liste[self.idd]
                                                # next s
                                                self.s              = self.sub_liste[self.idd]
                                                # next string
                                                self.string         = self.string_tabular[self.idd]
                                                # restoring the prvious get of s
                                                self.get            = self.memory[self.idd]
                                                # restoring cursor position in the input
                                                self.index          = self.tabular[self.idd]
                                                # restoring cursor position in s
                                                self.mainIndex      = self.sub_tabular[self.idd]
                                                # restoring cursor position in string
                                                self.I_S            = self.string_tab[self.idd]
                                                # restoring the value of last
                                                self.last           = self.last_tabular[self.idd]
                                                # restoring remove_tab from index
                                                self.remove_tab     = self.remove_tabular[self.idd]
                                                if self.drop_list_str:
                                                    self.str_drop_down = self.drop_list_str[ self.idd ]
                                                    self.drop = self.drop_list_id[ self.idd ]
                                                else: pass                  
                    if self.char not in {10, 13}:
                        # clear entire line
                        if self.char == 12:
                            # move cursor left 
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            # clear entire line 
                            sys.stdout.write(bm.clear.line(pos=2))
                            # write input
                            sys.stdout.write(self.main_input)
                            #move cursor left again
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            
                            # block init
                            self.input      = self.main_input
                            self.index      = self.length
                            self.key        = False
                            self.mainString = ''
                            self.mainIndex  = 0
                            self.clear_line = True
                        # clear entire screen
                        elif self.char == 19:
                            #os.system('cls')
                            sys.stdout.write(bm.clear.screen(pos=2))
                            sys.stdout.write(bm.save.restore)
                        # write char
                        else:
                            self.input       = self.input[ : self.index ] + chr( self.char ) + self.input[ self.index : ]
                            self.mainString  = self.mainString[ : self.mainIndex ] + chr( self.char ) + self.mainString[ self.mainIndex : ]
                            self.index       += 1
                            self.mainIndex   += 1
                    
                            
                    elif self.char in {10, 13}:  # enter
                        self.line += 1
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        
                        ####################################################################
                        if terminal_name == 'orion':
                            # Syntaxis color 
                            self.input = self.input[: self.length] + bm.init.bold + bm.words(string=self.mainString, color=bm.fg.rbg(255, 255, 255)).final()
                            #moving cursor left
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            # moving cursor up
                            sys.stdout.write(bm.move_cursor.UP(1))
                            # clear entire line
                            sys.stdout.write(bm.clear.line(2))
                            # write the new string
                            sys.stdout.write(self.input)
                            # flush
                            sys.stdout.flush()
                            if self.clear_line is False:
                                # moving cursor down
                                sys.stdout.write(bm.move_cursor.DOWN(1))
                                # clear entire line
                                sys.stdout.write(bm.clear.line(2))
                            else: self.clear_line = False
                            # movin cursor left
                            sys.stdout.write(bm.move_cursor.LEFT(1000))
                        else:
                            self.input = self.input[: self.length] + bm.init.bold+bm.fg.rbg(255, 255, 255)+self.mainString+bm.init.reset
                            # move cursor left
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            # clear entire line 
                            sys.stdout.write(bm.clear.line(2))
                            # write input 
                            sys.stdout.write(self.input)
                            # move left again 
                            sys.stdout.write(bm.move_cursor.LEFT(1000))
                            if self.clear_line is False: pass 
                            else:
                                # moving cursor up
                                sys.stdout.write(bm.move_cursor.UP(1))
                                # clear entire line 
                                sys.stdout.write(bm.clear.line(2))
                                # move cursor left
                                sys.stdout.write(bm.move_cursor.LEFT(1000))
                                # clear_line initialized to False
                                self.clear_line = False
                        ######################################################################
                        if self.mainString:
                            # running lexer 
                            self.lexer, self.normal_string, self.error = main.MAIN(self.mainString, self.data_base, self.line).MAIN()
                            if self.error is None :
                                if self.lexer is not None:
                                    
                                    # running parser 
                                    self.num, self.key, self.error = parxer.ASSEMBLY(self.lexer, self.data_base,
                                            self.line).GLOBAL_ASSEMBLY(main_string=self.normal_string, interpreter = False, term=terminal_name)
                                    if self.error is None: self.cursor.append(bm.get_cursor_pos.pos)   
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
                        else:  pass

                        # initialization 
                        self.input      = self.main_input
                        self.index      = self.length
                        self.key        = False
                        self.mainString = ''
                        self.mainIndex  = 0
                    # tabular
                    elif self.char == 9:  
                        self.tabular = '\t'
                        self.input = self.input[: self.index] + self.tabular + self.input[self.index:]
                        self.index += 1
                                            
                    # moving cursor left
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    # clear line 
                    sys.stdout.write(bm.clear.line(pos=0))
                    # write string
                    if terminal_name == "pegasus":
                        sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                    else:
                        sys.stdout.write(self.main_input+bm.string().syntax_highlight( bm.words(string=self.mainString, color=bm.fg.white_L).final() ))
                    # move cusor left again 
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                    # updating cursor position on the line 
                    if self.index > 0:  sys.stdout.write(bm.move_cursor.RIGHT(self.index - self.sub_length))
                    else:   pass

                    # flush
                    sys.stdout.flush()
                else: pass
            #keyboardInterrupt
            except KeyboardInterrupt:
                sys.stdout.write(bm.clear.screen(pos=1))
                sys.stdout.write(bm.cursorPos.to(0,0))
                sys.stdout.write(bm.clear.screen(pos=0))
                sys.stdout.write(bm.move_cursor.DOWN(pos=1))
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                sys.stdout.write(bm.clear.line(pos=0))
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset+bm.init.reset
                print(bm.init.bold+self._keyboard_)
                return
            # EOF
            except IndexError:
                self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset+bm.init.reset
                print(bm.init.bold+self._end_of_file_)
                self.input = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset)
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.flush()
                return

if __name__ == '__main__':

    term = 'orion'
    try:
        os.system('cls')
        sys.stdout.write(bm.save.save)
        if term == 'orion': header.header(terminal='orion terminal')
        else: header.header(terminal='pegasus terminal')
        
        data_base = db.DATA_BASE().STORAGE().copy()
        windows( data_base=data_base).terminal(c=bm.fg.rbg(255, 255, 255), terminal_name=term)
    except KeyboardInterrupt:  pass
    except IndexError: pass