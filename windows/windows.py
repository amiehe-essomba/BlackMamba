#############################################################
#############################################################
# Black Mamba orion and pegasus code iditor for Windows     #
# This version has currently two code iditors:              #
#                                                           #
#                                                           #
# * pegasus is the default editor                           #
# * orion is the optimized code editor with a syntaxis      #
# * coloration                                              #
# basically we can use both without any problems because    #
# they work very well.                                      #
#                                                           #
#                                                           #
# * To select a terminal it's very simple, just do this     #
#                                                           #
#       * mamba --T orion                                   #
#       * mamba --T pegasus                                 #
#############################################################
############################################                #
# ** created by : amiehe-essomba           #                #
# ** updated by: amiehe-essomba            #                #
# ** copyright 2023 amiehe-essomba         #                #
############################################                #
#############################################################


import sys, os 
from windows                    import data
from script                     import control_string
from windows                    import screenConfig, buildString
from ctypes                     import windll
from IDE.EDITOR                 import string_to_chr 
from script.STDIN.LinuxSTDIN    import bm_configure                 as bm
from IDE.EDITOR                 import pull_editor                  as PE
from windows                    import traceback                    as TB
from script.PARXER.WINParxer    import parxer
from script.LEXER.FUNCTION      import main


def write(terminal_name='pegasus', string = "", decorator = "", color = "", reset = '', show = False):
    if terminal_name == 'orion':
        # key word activation
        newString = decorator + bm.string().syntax_highlight( name=bm.words(string=string, color= color).final() )
        if show is False: sys.stdout.write( newString ) 
        else : print(newString)
    else:
        # any activation keyword
        newString = decorator +  color+ string + reset
        if show is False: sys.stdout.write(newString)
        else: print(newString)

def buildingString(Data : dict, a : int, b : int, drop_str : str, typ : str= "input"):
    beta = len( drop_str )
    if typ == 'input':
        Data['input']  = Data['input'][ : a] + drop_str +  Data['input'][b : ]
        Data['index'] += beta-1
        for k in range(beta-1):
            Data['get'].append(1)
    else:
        Data['string'] = Data['string'][ : a] + drop_str +  Data['string'][b : ]
        Data['I_S']   += beta-1
       
def re_write(terminal : str, indicator: int, Data : dict,  color : str ="", x : int = 0, y: int=0):
    if indicator not in {65, 66}:
        # moving cursor left 
        if indicator != 14:
            sys.stdout.write( bm.move_cursor.UP( pos= 1) + 
            bm.move_cursor.LEFT( pos = 1000 ) )
        else: sys.stdout.write( bm.move_cursor.LEFT( pos = 1000 ) )
        # erasing entire line 
        sys.stdout.write( bm.clear.line( pos = 2 ) )
        # writing string 
        write(terminal, Data['input'], Data['main_input'], color, bm.init.reset)
        # move cusror on left egain
    else: pass
            
class IDE:
    def __init__(self, data_base : dict = {}):
        # main data base
        self.data_base                      = data_base
        # contriling string
        self.analyse                        = control_string.STRING_ANALYSE(self.data_base, 1)
        
    def terminal(self, c: str = '', terminal_name : str = 'pegasus'):
        # reset color
        self.reset                          = bm.init.reset
        # initialization of data 
        self.Data                           = data.base(c=c, reset=self.reset, tab=0)
        # getting max size (max_x, max_y) of the window 
        self.max_x, self.max_y              = screenConfig.cursorMax()
        # when Ctrl+ option are used 
        self.indicator                      = None
        # fixing the x-axis border 
        self.border_x_limit                 = True 
        # scroll list size 
        self.scroll_size                    = 11
        # story
        self.histoty_tracback               = {
            'TrueFileNames'                 : None,
            "all_modules_load"              : None,
            "modules"                       : None
        }
        self.error                          = None
        ##########################################################################
        k  = windll.kernel32
        k.SetConsoleMode( k.GetStdHandle( -11 ), 7)
        # clear entire line
        sys.stdout.write( bm.clear.line(pos = 0) )
        # move cursor left
        sys.stdout.write( bm.move_cursor.LEFT(pos = 1000) )
        # print the input value
        sys.stdout.write( self.Data['main_input'] )
        # getting the cursor coordiantes (x, y)
        self.X, self.y                      = screenConfig.cursor()
        sys.stdout.flush()
        ##########################################################################
        self.move                   = bm.move_cursor
        self.clear                  = bm.clear 
        self.bold                   = bm.init.bold
        self.color                  = self.bold + bm.fg.rbg(255, 255, 255)
        self.x                      = self.Data['size']+1
        sys.stdout.write(self.move.TO(self.x, self.y))
        # flush
        sys.stdout.flush()
        ##########################################################################
        # Y_max 
        self.max_size_init          = 11 
        # save cursor line 
        self.save_cursor_position   = bm.save.save
        # indictor position initialization 
        self.indicator_pos          = 0
        # indicator_max 
        self.indicator_max          = 1
        # checking if key_max_activation could be activated  for handling terminal tools
        self.key_max_activation     = True 
        # self.index and self.if_line 
        self.index, self.if_line    = 0, 0 
        ##########################################################################

        while True:
            try:
                # get windows (max_x, max_y) at each time 
                self.max_x, self.max_y              = screenConfig.cursorMax()
                # get user input, char is a list of two dimensional
                self.char = string_to_chr.convert()
                if self.char:
                    _ = self.char[1]
                    self.char = self.char[0]
                    if self.char is not None:
                        # breaking loop while with the keyboardError ctrl+c
                        if self.char == 3               :
                            os.system('cls')
                            sys.stdout.write(bm.clear.screen(pos=2))
                            sys.stdout.write(bm.cursorPos.to(0,0))
                            sys.stdout.write(bm.clear.screen(pos=0))
                            sys.stdout.write(bm.move_cursor.DOWN(pos=1))
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            sys.stdout.write(bm.clear.line(pos=0))
                            self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                            print(self._keyboard_)
                            return
                        
                        # indentation Tab
                        elif self.char == 9             :
                            if  self.x < (self.max_x - 4) :  
                                self.tt                  = ' ' * 4
                                self.Data['string']      =  self.Data['string'][ : self.Data["I_S"] ] + chr( self.char ) + self.Data['string'][ self.Data["I_S"] : ]
                                self.Data['input']       =  self.Data['input'][ : self.Data["index"] ] + str( self.tt ) + self.Data['input'][ self.Data["index"] : ]
                                self.Data['index']      += 4
                                self.Data['I_S']        += 1
                                self.x                  += 4
                                self.Data['get'].append([1 for x in range(4)])
                            else: pass 

                        # writing char
                        elif 32 <= self.char <= 126     :
                            ##################################################
                            # each character has 1 as length                 #
                            # have a look on ansi char                       #
                            # https://en.wikipedia.org/wiki/ANSI_escape_code #
                            ##################################################
                            if self.border_x_limit is True: 
                                # building string
                                self.Data['string']         = self.Data['string'][ : self.Data['I_S']] + chr( self.char ) + \
                                            self.Data['string'][ self.Data['I_S'] : ]
                                # building input
                                self.Data['input']          = self.Data['input'][ : self.Data['index']] + chr( self.char ) + \
                                            self.Data['input'][ self.Data['index'] : ]
                                # increasing index of a step = 1
                                self.Data['index']          += 1
                                # increasing I_S of step = 1
                                self.Data['I_S']            += 1
                                # storing char in get
                                self.Data['get'].append(1)
                                # increase cursor position of +1
                                self.x                      += 1

                                # fixing the cursor position conditions
                                if self.x < self.max_x : self.border_x_limit = True 
                                else: self.border_x_limit = False 
                            else: pass 

                        # delecting char <backspace>
                        elif self.char in {127, 8}      :
                            if self.x > ( self.Data['size'] + 1):#self.Data['get']:
                                self.Data['string']         =  self.Data['string'][ : self.Data["I_S"] - 1] + self.Data['string'][ self.Data["I_S"] : ]
                                self.Data['I_S']           -= 1
                                if type( self.Data['get'][self.Data['I_S']] ) == type(list()):
                                    self.Data['input']      =  self.Data['input'][ : self.Data["index"] - 4] + self.Data['input'][ self.Data["index"] : ]
                                    self.x                 -= 4
                                    self.Data['index']     -= 4
                                else:
                                    self.Data['input']      =  self.Data['input'][ : self.Data["index"] - 1] + self.Data['input'][ self.Data["index"] : ]
                                    self.x                 -= 1
                                    self.Data['index']     -= 1
                                
                                del self.Data['get'][self.Data['I_S']]
                            else: pass
                        
                        # moving cursor (up, down, left, right)
                        elif self.char == 27            :
                            if type(_) is type(list()): next1 = _[0]
                            else: next1 = _
                            
                            if next1 in {68, 67, 66, 65, 49} :
                                # move left 
                                if   next1 == 68:
                                    if self.Data['I_S'] > 0:
                                        try:
                                            self.Data['I_S']        -= 1
                                            if type(self.Data['get'][self.Data['I_S']]) == type(list()):
                                                self.x              -= 4
                                                self.Data['index']  -= 4
                                            else:
                                                self.x              -= 1
                                                self.Data['index']  -= 1
                                        except IndexError : pass
                                    else: pass
                                # move right
                                elif next1 == 67:
                                    if self.x <=  (self.Data['size'] + len(self.Data['input'])):  
                                        try:
                                            if type(self.Data['get'][self.Data['I_S']]) == type(list()):
                                                self.x              += 4
                                                self.Data['index']  += 4
                                            else:
                                                self.x              += 1
                                                self.Data['index']  += 1
                                            self.Data['I_S']        += 1
                                        except IndexError: pass
                                    else: pass 
                                # get the previous value stored in the list
                                elif next1 == 65:  # up
                                    if self.Data['liste']:
                                        try: 
                                            if self.index > 0 :
                                                self.index                 -= 1
                                                self.Data['input']          = self.Data['liste'][self.index]
                                                self.Data['string']         = self.Data['string_tabular'][self.index]
                                                self.Data['index']          = self.Data['tabular'][self.index]
                                                self.Data['I_S']            = self.Data['string_tab'][self.index]
                                                self.Data['get']            = self.Data['memory'][self.index].copy()
                                                self.x, self.Y              = self.Data['x_y'][self.index]
                                            else: pass
                                        except IndexError : pass 
                                    else: pass 
                                # get the next value stored in the list
                                elif next1 == 66:  # down
                                    if self.Data['liste']:
                                        try: 
                                            if self.index < len(self.Data['liste']) :
                                                self.index                 += 1
                                                self.Data['input']          = self.Data['liste'][self.index]
                                                self.Data['string']         = self.Data['string_tabular'][self.index]
                                                self.Data['index']          = self.Data['tabular'][self.index]
                                                self.Data['I_S']            = self.Data['string_tab'][self.index]
                                                self.Data['get']            = self.Data['memory'][self.index].copy()
                                                self.x, self.Y              = self.Data['x_y'][self.index]
                                            else: pass
                                        except IndexError : pass 
                                    else: pass 
                                # ctrl + left or ctrl + right
                                elif next1 == 49: 
                                    if self.Data['str_drop_down'] : 
                                        next2 =  _[1]
                                        # ctrl-up, ctrl-down is handled 
                                        if next2 in {67, 68}: pass 
                                        # ctrl-right is handled 
                                        elif next2 == 65: 
                                            self.indicator = 65 
                                            if self.indicator_pos >= 1: self.indicator_pos -= 1
                                            else: pass
                                        # ctrl-left is handled 
                                        elif next2 == 66: 
                                            self.indicator = 66
                                            if self.indicator_pos < self.indicator_max : self.indicator_pos += 1
                                            else: pass 
                                        else: pass
                                    else: pass
                            elif next1 is None: pass
                            else: pass 

                            next1, next2, next3, next4, next5 = 0, 0, 0, 0, 0

                        # clear entire string ctrl+l
                        elif self.char == 12            :
                            # move cursor left
                            sys.stdout.write(self.move.LEFT( pos = 1000 ))
                            # clear entire line
                            sys.stdout.write(self.clear.line( pos = 0 ))
                           
                            # initialization block
                            self.x                   = self.Data['size'] + 1
                            self.Data['string']      = ""
                            self.Data['input']       = ""
                            self.Data['get']         = []
                            self.Data["I_S"]         = 0
                            self.Data["index"]       = 0
                          
                        # move cursor at end of line ctrl+d
                        elif self.char == 4             :
                            self.Data['I_S']        = len(self.Data['string'])
                            self.Data['index']      = len(self.Data['input'])
                            self.x                  = len(self.Data['input']) + self.Data['size'] + 1

                        # clear entire screen and restore cursor position ctrl+s
                        elif self.char == 19: 
                            sys.stdout.write(self.clear.screen(pos = 1))
                            sys.stdout.write(self.move.TO( self.x, 0))
                            sys.stdout.write(bm.save.save)
                            self.X, self.y           = screenConfig.cursor()

                        # move cursor at the beginning of line ctrl+q
                        elif self.char in{1, 17}        : 
                            self.Data['I_S']        = 0
                            self.Data['index']      = 0
                            self.x                  = self.Data['size'] + 1
                        
                        # <crtl+t> or <ctrl + n> 
                        elif self.char in {20, 14}      : 
                            self.indicator = self.char 
                        
                        # End-Of-File Error ctrl+z
                        elif self.char == 26            :
                            sys.stdout.write(self.clear.screen(pos=1))
                            sys.stdout.write(self.move.TO(0,0))
                            sys.stdout.write(self.clear.screen(pos=0))
                            sys.stdout.write(self.move.DOWN(pos=1))
                            sys.stdout.write(self.move.LEFT(pos=1000))
                            sys.stdout.write(self.clear.line(pos=0))
                            self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                            print(self._end_of_file_)
                            return
                        
                        # <ctrl+alt+down> => <down >
                        elif self.char in {1001}        : 
                            self.indicator = 66
                            self.indicator_pos += 1
                        
                        # <ctrl+alt+up> => <up>
                        elif self.char in {1000}        : 
                            self.indicator = 65 
                            if self.indicator_pos >= 1: self.indicator_pos -= 1
                            else: pass

                        # enter is pressed 
                        elif self.char in {10, 13}      :
                            # moving cursor left 
                            sys.stdout.write( self.move.LEFT( pos = 1000 ) )
                            # erasing entire line 
                            sys.stdout.write( self.clear.line( pos = 2 ) )
                            # writing string 
                            write(terminal_name, self.Data['input'], self.Data['main_input'], self.color, self.reset, show=True)
                            #####################################################################################
                            if self.Data['string']:
                                # running lexer
                                self.lexer, self.normal_string, self.error = main.MAIN(
                                                master = self.Data['string'],
                                                data_base=self.data_base, 
                                                line=self.if_line).MAIN()
                                if self.error is None :
                                    if self.lexer is not None:
                                        # running parser
                                        self.num, self.key, self.error = parxer.ASSEMBLY(
                                            master=self.lexer, 
                                            data_base=self.data_base,
                                            line=self.if_line).GLOBAL_ASSEMBLY(
                                                        main_string=self.normal_string, 
                                                        interpreter = False, term=terminal_name, 
                                                        traceback=self.histoty_tracback,
                                                        callbacks = self.Data.copy()
                                            )
                                       
                                        if self.error is None: pass 
                                        else: 
                                            sys.stdout.write(bm.move_cursor.LEFT(1000))
                                            sys.stdout.write(bm.clear.screen(0))
                                            print(f"\n{self.error}\n")
                                            #self.error = TB.traceback.init(self.data_base,  self.histoty_tracback, self.error)
                                    else:  pass
                                else :
                                    sys.stdout.write(bm.move_cursor.LEFT(1000))
                                    sys.stdout.write(bm.clear.screen(0)) 
                                    print(f"\n{self.error}\n")
                                    #self.error = TB.traceback.init(self.data_base,  self.histoty_tracback, self.error)
                            else: pass
                            #####################################################################################
                            # initializing all variables
                            self.if_line            += 1 
                            self.X, self.y           = screenConfig.cursor()
                            self.x                   = self.Data['size'] + 1  
                            self.Data['string']      = ""
                            self.Data['input']       = "" 
                            self.Data['get']         = []
                            self.Data["I_S"]         = 0 
                            self.Data["index"]       = 0 
                            self.index               = self.if_line
                            self.error               = None
                            #####################################################################################
                            self.Data['string_tabular'].append( [] )
                            self.Data['liste'].append( [] )
                            self.Data['string_tab'].append( [] )
                            self.Data['tabular'].append( [] )
                            self.Data['x_y'].append( [] )
                            self.Data['memory'].append( [] )
                            #####################################################################################
                            self.indicator_pos      = 0
                            self.indicator          = None
                            self.indicator_max      = 1
                            self.scroll_size        = 11
                            #####################################################################################
                        else: pass 

                        if self.border_x_limit is True  :
                            self.Data['drop_idd'], self.Data['str_drop_down'], self.a, self.b = buildString.string( 
                                                    self.Data['input'], self.Data['index']-1 )
                            _, _, self.a_, self.b_ = buildString.string( self.Data['string'], self.Data['I_S']-1 )
                            
                            # checking windows dimension 
                     
                            if self.max_x > 30 and self.max_y > 20:
                                # checkng if str_drop_down exists
                                if self.Data['str_drop_down']:
                                    # saving cursor position 
                                    sys.stdout.write(bm.save.save)
                                    # clean screen from the cursor position untill the end of the line 
                                    sys.stdout.write( self.move.DOWN( pos = 1 ) + 
                                                  self.clear.screen(pos=0) + self.move.UP( pos = 1 ) )
                                    if self.indicator is None:
                                        verbose, _, self.scroll_size, self.error = PE.DropDown(
                                            data_base = self.data_base, line=self.if_line).MENU( self.Data['str_drop_down'], 
                                        self.Data['input'], self.indicator, self.indicator_pos, (self.max_x-self.x))
                                       
                                        # restoring cursor position
                                        sys.stdout.write(bm.save.restore) 
                                        # computing the new params( x, y)

                                        self.X, self.y           = screenConfig.cursor()
                                        # moving cursor on the right position 
                                        sys.stdout.write(self.move.TO(self.x, self.y)) 
                                        #self.X, self.y           = screenConfig.cursor()
                                        #####################################################
                                        sys.stdout.flush()
                                    else: 
                                        sys.stdout.write(bm.clear.screen(pos=0))
                                        verbose, _, self.scroll_size, self.indicator_pos, self.error = PE.DropDown(data_base = self.data_base, 
                                                    line=self.if_line).MENU( self.Data['str_drop_down'], self.Data['string'], self.indicator, 
                                                    self.indicator_pos, (self.max_x-self.x), iter=True)
                                     
                                        if self.error is None: 
                                            if verbose is not None: 
                                                if (self.max_x - (self.x + len(verbose))) > 0:
                                                    if self.indicator in {7, 14, 20}:
                                                        # input and index
                                                        buildingString(self.Data, self.a, self.b, verbose)
                                                        # string and I_S
                                                        buildingString(self.Data, self.a_, self.b_, verbose, typ="string")
                                                        # re-writing the string 
                                                        re_write(terminal_name, self.indicator, self.Data.copy(), self.color)
                                                        # new x position 
                                                        self.x                   += len(verbose) - len(self.Data['str_drop_down'])
                                                        sys.stdout.write(self.move.DOWN(pos = 1))
                                                        self.X, self.y           = screenConfig.cursor()
                                                        # moving cursor on the right position 
                                                        sys.stdout.write(self.move.TO(self.x, self.y) )
                                                        sys.stdout.flush()
                                                        verbose, self.indicator  = None, None
                                                    else:
                                                        sys.stdout.write( self.move.UP(pos = self.scroll_size ) )
                                                        sys.stdout.flush()
                                                else: pass  
                                            else: pass

                                            #sys.stdout.write(bm.save.restore) 
                                            sys.stdout.write(self.move.UP(pos = 1))
                                            self.X, self.y           = screenConfig.cursor()
                                            # moving cursor on the right position 
                                            sys.stdout.write(self.move.TO(self.x, self.y) )
                                            sys.stdout.flush()
                                            self.indicator = None
                                        else:
                                            sys.stdout.write(self.error+"\n\n")
                                            self.error = None
                                            # writing string again after erasing entire line 
                                            write(terminal_name, self.Data['input'], self.Data['main_input'], self.color, self.reset)
                                else:
                                    # initialization 
                                    self.indicator_pos, self.indicator      = 0, None
                                    #destroying all string under cursor position 
                                    sys.stdout.write(self.clear.screen(pos=0)) 
                                    sys.stdout.flush()
                            else: pass
                            sys.stdout.flush()

                            # moving cursor left 
                            sys.stdout.write( self.move.LEFT( pos = 1000 ) )
                            # erasing entire line 
                            sys.stdout.write( self.clear.line( pos = 2 ) )
                            # writing string 
                            write(terminal_name, self.Data['input'], self.Data['main_input'], self.color, self.reset)
                            # move cusror on left egain
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                            # replace the cussor 
                            sys.stdout.write(self.move.TO(self.x, self.y) ) 
                            sys.stdout.flush()
                        else: pass

                        #############################################################################
                        ################### Updating the data stored in each lists  #################
                        self.Data['x_y'][self.if_line]              = (self.x, self.y)
                        self.Data['string_tabular'][self.if_line]   = self.Data['string']
                        self.Data['string_tab'][self.if_line]       = self.Data['I_S']
                        self.Data['liste'][self.if_line]            = self.Data['input']   
                        self.Data['tabular'][self.if_line]          = self.Data['index'] 
                        self.Data['memory'][self.if_line]           = self.Data['get'].copy() 
                        #############################################################################
                    else: pass
                else: pass
            except KeyboardInterrupt:
                os.system('cls')
                sys.stdout.write(bm.clear.screen(pos=2))
                sys.stdout.write(bm.cursorPos.to(0,0))
                sys.stdout.write(bm.clear.screen(pos=0))
                sys.stdout.write(bm.move_cursor.DOWN(pos=1))
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                sys.stdout.write(bm.clear.line(pos=0))
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                return
            
            except EOFError:
                os.system('cls')
                self._end_of_file_ = bm.bg.red_L + bm.fg.rbg(255,255,255) + "EOFError" + bm.init.reset
                print(self._end_of_file_)
                self.input = '{}>>> {}'.format(self.c, bm.init.reset)
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.flush()
        

