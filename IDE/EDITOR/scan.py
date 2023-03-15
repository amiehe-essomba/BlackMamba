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
# ** copyright 2023 amiehe-essomba         #         
############################################
#############################################################


import sys
from script                                                 import control_string
from script.STDIN.LinuxSTDIN                                import bm_configure     as bm
from script.PARXER.PARXER_FUNCTIONS._IF_                    import IfError

class windows:
    def __init__(self, data_base : dict):
        # main data base
        self.data_base  = data_base
        # string module analyses 
        self.analyse    = control_string.STRING_ANALYSE(self.data_base, 1)

    def terminal(self, c: str = '', terminal_name : str = 'pegasus'):
        # input initialization
        self.input      = '{}>>>{} {}'.format(bm.fg.yellow_L, c, bm.init.reset)
        # root of input 
        self.main_input = '{}>>>{} {}'.format(bm.fg.yellow_L, c, bm.init.reset)
        # lenght of the root 
        self.length     = len(self.input)
        # index initialization 
        self.index      = self.length
        # sub length initialization 
        self.sub_length = len('{}{}{}'.format(bm.fg.yellow_L, c, bm.init.reset))
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
        # false if clean line is not activated else true
        self.clear_line = False         
        
        # write input initialized 
        sys.stdout.write(bm.string().syntax_highlight(name=self.input))
        #flush 
        sys.stdout.flush()
        
        while True:
            try:
                # get an input 
                self.char = bm.read().readchar()
                #print(self.char)
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
                        # write the new string
                        sys.stdout.write(self.input)
                        break
                    else:
                        # write the new string
                        self.input = self.input[: self.length] + bm.init.bold+bm.fg.rbg(255, 255, 255)+self.mainString+bm.init.reset
                        sys.stdout.write(self.input)
                        break
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
                else: sys.stdout.write(self.main_input+bm.string().syntax_highlight( bm.words(string=self.mainString, color=bm.fg.white_L).final() ))
                # move cusor left again 
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                # updating cursor position on the line 
                if self.index > 0:  sys.stdout.write(bm.move_cursor.RIGHT(self.index - self.sub_length))
                else:   pass

                # flush
                sys.stdout.flush()
                   
            #keyboardInterrupt
            except KeyboardInterrupt:
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break
            # EOF
            except TypeError:
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break
            
        return self.mainString, self.error 
    
class colors:
    def __init__(self, cc: str, blink : bool = False):
        self.string  = cc
        self.blink   = blink
    def color(self):
        c = ""
        if   self.string == 'white'     : c = bm.fg.rbg(255, 255, 255)
        elif self.string == 'yellow'    : c = bm.fg.rbg(255, 255, 0)
        elif self.string == 'red'       : c = bm.fg.rbg(255, 0, 0)
        elif self.string == 'blue'      : c = bm.fg.rbg(0, 0, 255)
        elif self.string == 'green'     : c = bm.fg.rbg(0, 255, 0)
        elif self.string == 'black'     : c = bm.fg.rbg(0, 0, 0)
        elif self.string == 'orange'    : c = bm.fg.rbg(255, 102, 0)
        elif self.string == 'cyan'      : c = bm.fg.rbg(0, 255, 255)
        elif self.string == 'magenta'   : c = bm.fg.rbg(255, 0, 255)
        
        if self.blink is False: return c 
        else: return bm.init.blink+c