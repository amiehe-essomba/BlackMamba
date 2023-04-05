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
from script.STDIN.LinuxSTDIN   import bm_configure as bm


class string:
    def __init__(self, data_storage : str ):
        self.data_storage = data_storage
        
    def build(self, c: str = ''):
        # set color on yellow
        self.c              = bm.fg.rbg(255, 255, 0)
        # reset color
        self.reset          = bm.init.reset
        self.input               = '{}>>> {}'.format(self.c, self.reset)
        # input main used to build the final string s
        self.main_input          = '{}>>> {}'.format(self.c, self.reset)
        # initial length of the input 
        self.length              = len(self.input)
        # initialisation of index associated to the input 
        self.index               = self.length
        # length of the foutth first char of input 
        self.size                = len('>>> ')
        # string used to handling the output that is the must inmportant string
        self.s              = ""
        # string used for the code,
        self.string         = ''
        # index associated to the string string value
        self.I_S            = 0
        # initialisation of index I associated to the string s value
        self.I              = 0
        self.last           = 0
        self.get            = []
  
        ###########################################################
        # accounting line
        self.if_line        = 0
        # error variable
        self.error          = None
        self.pos            = None
        
        for chars in self.data_storage:
            try:
                # get input
                self.char = ord( chars )
                
                if 32 <= self.char <= 126:
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
                    
                # tabulation
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
                
                # put cursor on the right position
                if self.index > 0: self.pos = len(self.s) + self.size + len(self.input) - self.index
                else: pass
                
            except KeyboardInterrupt:
                self.error= bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                break
            except TypeError:
                self.error = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                break

        return self.error, [(self.input, self.index), (self.s, self.I), (self.string, self.I_S)], self.pos, self.get