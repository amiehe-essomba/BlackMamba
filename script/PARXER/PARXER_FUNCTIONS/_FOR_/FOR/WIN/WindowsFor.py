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
from script.STDIN.LinuxSTDIN                        import readchar
from script.PARXER.PARXER_FUNCTIONS._IF_            import IfError
from script.LEXER.FUNCTION                          import main
from script                                         import control_string
from script.STDIN.LinuxSTDIN                        import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS._FOR_.FOR.WIN   import externalFor as eFor

class EXTERNAL_FOR_WINDOWS:
    def __init__(self, 
        data_base   : dict, 
        line        : int,
        term        : str 
        ):
        
        # current line 
        self.line               = line
        # main data base
        self.data_base          = data_base
        # terminal type
        self.term               = term
        #contriling string
        self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)

    def TERMINAL( self, 
            tabulation  : int,  
            c           : str   = '',
            _type_      : str   = 'loop',
            ):
        
        self.if_line            = 0
        self.error              = None
     
        ##########################################################
        self.space              = 0
        self.active_tab         = None
        self.tabulation         = tabulation
        self.history            = [ 'for' ]
        self.loop               = []
        self.store_value        = []
        ##########################################################
        self.for_cancel         = False
        self.max_emtyLine       = 5
        ##########################################################
        # false if clean line is not activated else true
        self.clear_line = False      
        ##########################################################
        
        # set color on yellow
        self.c                   = bm.fg.rbg(255,255,0)
        if self.term == 'orion': pass 
        else: self.c             = bm.fg.rbg(255,255,255)
        # reset color
        self.reset               = bm.init.reset
        # input initialized
        self.input               = '{}... {}'.format(self.c, self.reset)
        # input main used to build the final string s
        self.main_input          = '{}... {}'.format(self.c, self.reset)
        # initial length of the input 
        self.length              = len(self.input)
        # initialisation of index associated to the input 
        self.index               = self.length
        # length of the foutth first char of input 
        self.size                = len('... ')
        # string used to handling the output that is the must inmportant string
        self.s                   = ""
        # string used for the code, 
        self.string              = ''
        # index associated to the string string value
        self.I_S                 = 0
        # initialisation of index I associated to the string s value
        self.I                   = 0    
        # history of data associated to the string  input 
        self.liste               = []
        # history of data associated to the value returns by the function readchar 
        self.get                 = []
        # initialisation of integer idd used to get the next of previous 
        # values stored in the different histories of lists 
        self.idd                 = 0
        # initialization of list associated to the string s
        self.sub_liste           = []
        # the memory contains the history of get value
        self.memory              = []
        # initilization of last
        self.last                = 0
        # initialisation of list associated to the index value
        self.tabular             = []
        # initialisation of list associated to I value
        self.sub_tabular         = []
        # initialisation of the list associated to last value
        self.last_tabular        = []
        # move cursor 
        self.remove_tab          = 0
        # storing cursor position 
        self.remove_tabular      = []
        # initialization of the list associated to string 
        self.string_tab          = []
        # initialization of associated to I_S
        self.string_tabular      = []
        ###########################################################
        # clear entire line
        sys.stdout.write(bm.clear.line(pos=0))
        #move cursor left
        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))  
        # print the input value
        sys.stdout.write(self.input)
        # save cursor position
        sys.stdout.write(bm.save.save)
        # flush
        sys.stdout.flush()
        ###########################################################
        while True:
            try:
                # get input 
                self.char = readchar.readchar() 
          
                #breaking loop while with the keyboardError
                if self.char == 3: 
                    self.error = IfError.ERRORS(self.if_line).ERROR4()
                    break
                # writing char
                elif 32 <= self.char <= 126:
                    ######################################
                    # each character has 1 as length     #   
                    # have a look on ansi char           #
                    ######################################
                    # building input   
                    self.input       = self.input[ : self.index +self.last] + chr(self.char) + self.input[ self.index+self.last : ]
                    # building s 
                    self.s           = self.s[ : self.I] + chr(self.char) + self.s[self.I : ]
                    # building string 
                    self.string      = self.string[ : self.I_S] + chr(self.char) + self.string[ self.I_S : ]
                    # increasing index of a step = 1
                    self.index       += 1
                    # increasing I of a step = 1
                    self.I           += 1
                    # increasing I_S of step = 1
                    self.I_S         += 1 
                    # storing char in get
                    self.get.append(self.char)
                # moving cursor up, down, left, reight
                elif self.char == 27    :
                    next1, next2 = ord( sys.stdin.read(1)), ord( sys.stdin.read(1))
                    if next1 == 91:
                        try:
                            # move cursor to left
                            if   next2 == 68:
                                if self.I > 0:
                                    try:
                                        # without indentation 
                                        if 32 <= self.get[self.I-1] <= 126:
                                            self.I     -= 1
                                            self.index += 1
                                            self.last  -= 2
                                            self.I_S   -= 1
                                        # when identation is detected 
                                        elif self.get[self.I-1] == 9:
                                            self.I     -= 4
                                            self.index += 4
                                            self.last  -= 8
                                            self.I_S   -= 4
                                    except IndexError: pass
                                else: pass
                            # move cursor to right
                            elif next2 == 67:
                                if self.I < len(self.s):
                                    try:
                                        # without indentation 
                                        if 32 <= self.get[self.I] <= 126:
                                            self.I       += 1 
                                            self.index   -= 1
                                            self.last    += 2
                                            self.I_S     += 1
                                        # when identation is detected 
                                        elif self.get[self.I] == 9: 
                                            self.I       += 4
                                            self.index   -= 4
                                            self.last    += 8
                                            self.I_S     += 4
                                    except IndexError: pass
                                else: pass
                            # get the previous value stored in the list 
                            elif next2 == 65: #up
                                if self.liste:
                                    try:
                                        # idd is decreased of -1 
                                        self.idd    -= 1
                                        if len( self.liste ) >= abs( self.idd ):
                                            # previous input 
                                            self.input   = self.liste[ self.idd ]
                                            # previous s
                                            self.s       = self.sub_liste[ self.idd ]
                                            # previous string 
                                            self.string  = self.string_tabular[ self.idd ]
                                            # restoring the prvious get of s 
                                            self.get     = self.memory[ self.idd ]
                                            # restoring cursor position in the input 
                                            self.index   = self.tabular[ self.idd ]
                                            # restoring cursor position in s
                                            self.I       = self.sub_tabular[ self.idd ]
                                            # restoring cursor position in string 
                                            self.I_S     = self.string_tab[ self.idd ]
                                            # restoring the value of last 
                                            self.last    = self.last_tabular[ self.idd ]
                                            # restoring remove_tab from index
                                            self.remove_tab = self.remove_tabular[ self.idd ]
                                        else: self.idd += 1
                                    except IndexError: 
                                        # any changes here when local IndexError is detected 
                                        pass
                                else: pass
                            # get the next value stored in the list 
                            elif next2 == 66:
                                if self.liste:
                                    try:
                                        # idd is increased of 1
                                        self.idd     += 1
                                        # next input 
                                        if len( self.liste ) > self.idd:
                                            self.input   = self.liste[ self.idd ]
                                            # next s
                                            self.s       = self.sub_liste[ self.idd ]
                                            # next string 
                                            self.string  = self.string_tabular[ self.idd ]
                                            # restoring the prvious get of s 
                                            self.get     = self.memory[ self.idd ]
                                            # restoring cursor position in the input 
                                            self.index   = self.tabular[ self.idd ]
                                            # restoring cursor position in s
                                            self.I       = self.sub_tabular[ self.idd ]
                                            # restoring cursor position in string 
                                            self.I_S     = self.string_tab[ self.idd ]
                                            # restoring the value of last 
                                            self.last    = self.last_tabular[ self.idd ]
                                            # restoring remove_tab from index
                                            self.remove_tab = self.remove_tabular[ self.idd ]
                                        else: self.idd -= 1
                                    except IndexError: 
                                        # any changes here when local IndexError is detected 
                                        pass
                                else: pass
                        except IndexError: pass
                    else: pass  
                # delecting char 
                elif self.char in {127, 8}   :
                    # if s is not empty
                    if self.s:
                        # initialize key name of an indentation case
                        self.name = 0
                        self.key  = False
                        
                        try:
                            # checking if I > 0
                            if self.I-1 >=0:
                                # new char initialized 
                                self.char = self.get[self.I-1]
                                # writable char
                                if 32 <= self.get[self.I-1] <= 126:
                                    self.name = 1
                                    # delecting the value in get associated to the index I-1
                                    del self.get[self.I-1]
                                # indentation cas 
                                elif self.get[self.I-1] in {9}: 
                                    self.name = 1
                                    # when indentation is detected for loop is used to take into account the four value of space
                                    # it means that inden = " " * 4
                                    for i in range(4):
                                        # building input 
                                        self.input    = self.input[ : self.index + self.last - self.name] + self.input[ self.index + self.last : ]
                                        # decreasing index of -1
                                        self.index   -= 1
                                        # building s 
                                        self.s        = self.s[ : self.I - 1] + self.s[self.I : ]
                                        # decreating I of -1
                                        self.I       -= 1
                                        # delecting the value in get associated to the index I-1
                                        del self.get[self.I]
                                    
                                    # building string 
                                    self.string  = self.string[ : self.I_S-1]+self.string[ self.I_S : ]
                                    #decreasing I_S of -1
                                    self.I_S    -= 1  
                                    # set key of True
                                    self.key     = True
                                else: pass
                                
                                # if key is False it means s has not indentation 
                                if self.key is False: 
                                    # building input 
                                    self.input   = self.input[ : self.index + self.last - self.name] + self.input[ self.index + self.last : ]
                                    # decreasing index of -name with name = 1
                                    self.index  -= self.name 
                                    # building s 
                                    self.s       = self.s[ : self.I - 1] + self.s[self.I : ]
                                    # building string 
                                    self.string  = self.string[ : self.I_S - 1] + self.string[ self.I_S : ]
                                    # decreasing I and I_S of -1
                                    self.I      -= 1
                                    self.I_S    -= 1
                                else: pass
                            else: pass
                        except IndexError: pass  
                    else: pass
                # indentation 
                elif self.char == 9     :
                    
                    self.tt = '    '
                    self.input        = self.input[ : self.index + self.last ] + str(self.tt) + self.input[ self.index + self.last : ] 
                    self.s            = self.s[ : self.I] + str(self.tt) + self.s[self.I : ]  
                    # string takes the true value of char
                    self.string       = self.string[ : self.I_S] + chr(self.char) + self.string[ self.I_S : ]
                    self.index       += 4 
                    self.I           += 4
                    self.I_S         += 1
                    
                    for i in range(4):
                        self.get.append( self.char )
                #clear entire string
                elif self.char == 12    :
                    # move cursor left 
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    # clear entire line 
                    sys.stdout.write(bm.clear.line(pos=0))
                    # write main_input 
                    sys.stdout.write(self.main_input)
                    # move cursor left egain 
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    
                    # initialization block
                    self.input           = self.main_input
                    self.index           = self.length
                    self.s               = ''
                    self.string          = ''
                    self.I               = 0
                    self.I_S             = 0
                    self.get             = []
                    self.idd             = 0   
                    self.last            = 0
                    self.remove_tab      = 0              
                # move cursor at end of line 
                elif self.char == 4     :
                    while self.I < len(self.s):
                        try:
                            # without indentation 
                            if 32 <= self.get[self.I] <= 126:
                                self.I       += 1 
                                self.index   -= 1
                                self.last    += 2
                                self.I_S     += 1
                            # when identation is detected 
                            elif self.get[self.I] == 9: 
                                self.I       += 4
                                self.index   -= 4
                                self.last    += 8
                                self.I_S     += 4
                        except IndexError: pass                    
                # move cursor at the beginning of line 
                elif self.char == 17    :
                    while self.I > 0:
                        try:
                            # without indentation 
                            if 32 <= self.get[self.I-1] <= 126:
                                self.I     -= 1
                                self.index += 1
                                self.last  -= 2
                                self.I_S   -= 1
                            # when identation is detected 
                            elif self.get[self.I-1] == 9:
                                self.I     -= 4
                                self.index += 4
                                self.last  -= 8
                                self.I_S   -= 4
                        except IndexError: pass                 
                # clear entire screen and restore cursor position
                elif self.char == 19    :
                    sys.stdout.write(bm.clear.screen(pos=2))
                    sys.stdout.write(bm.save.restore)                  
                #End-Of-File Error
                elif self.char == 26    :
                    self.error = IfError.ERRORS(self.if_line).ERROR4()
                    break
                # printing and initializing of values
                elif self.char in {10, 13}:
                    self.if_line += 1
                    # move cursor of left 
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    # print the final input with its transformations 
                    if self.term == 'orion':  print(self.main_input+bm.words(string=self.s, color=bm.fg.rbg(255,255,255)).final())
                    else: print(self.main_input+bm.fg.rbg(255,255,255)+self.s+bm.init.reset)

                    # storing input 
                    self.liste.append( self.input )
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

                    if self.string:
                        #calling the main module IF 
                        self.loop, self.for_cancel, self.error = eFor.EXTERNAL_FOR(master=self.string, data_base = self.data_base, line=self.if_line,
                            history=self.history, store_value=self.store_value, space=self.space ).FOR(tabulation=self.tabulation, 
                            loop=self.loop, _type_=_type_ , c=c, term=self.term)
                        # break while loop if error is not None
                        if self.error is None:
                            if self.for_cancel is True:  break
                            else:  pass
                        else:  break
                    else:
                        # if no string
                        if self.space <= self.max_emtyLine:
                            self.space += 1
                            self.string = self.analyse.BUILD_NON_CON(string=self.string,tabulation=self.tabulation)
                            self.loop.append((self.string, False))
                        else:
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break

                    # initialization block
                    self.input           = self.main_input
                    self.index           = self.length
                    self.s               = ''
                    self.string          = ''
                    self.I               = 0
                    self.I_S             = 0
                    self.get             = []
                    self.idd             = 0   
                    self.last            = 0
                    self.remove_tab      = 0      
                # move cursor on left
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                # clear entire line
                sys.stdout.write(bm.clear.line(pos=0))
                
                if self.term == 'orion':
                    # key word activation 
                    sys.stdout.write(self.main_input+bm.string().syntax_highlight(name=bm.words(string=self.s, color=bm.fg.rbg(255,255,255)).final()))
                else:
                    # any activation keyword 
                    sys.stdout.write(self.main_input+bm.fg.rbg(255,255,255)+self.s+bm.init.reset)
                # move cusror on left egain 
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                # put cursor on the right position 
                if self.index > 0:
                    pos = len(self.s) + self.size + len(self.input) - self.index
                    sys.stdout.write(bm.move_cursor.RIGHT(pos=pos))
                else: pass
                sys.stdout.flush()          
            except KeyboardInterrupt:
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break
            except TypeError:
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break

        return {'for' : self.loop},  self.tabulation, self.error