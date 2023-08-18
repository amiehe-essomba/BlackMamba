#############################################################
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
# ** created  by : amiehe-essomba          #                #
# ** updating by : amiehe-essomba          #                #
# ** modified by : elena royer             #                #  
# ** copyright 2023 amiehe-essomba         #                #
############################################                #
#############################################################


import sys, os
from windows                                            import customized_term as ct
from ctypes                                             import windll
from windows                                            import data
from script                                             import control_string
from script.STDIN.LinuxSTDIN                            import bm_configure     as bm
from script.DATA_BASE                                   import data_base        as db
from IDE.EDITOR                                         import header, string_to_chr 
from IDE.EDITOR                                         import test
from IDE.EDITOR                                         import true_cursor_pos  as cursor_pos
from IDE.EDITOR                                         import cursor
from IDE.EDITOR                                         import left_right       as LR
from IDE.EDITOR                                         import string_build     as SB
from IDE.EDITOR                                         import pull_editor      as PE
from IDE.EDITOR                                         import drop_box         as DR
from script.PARXER.PARXER_FUNCTIONS._IF_                import IfError
from script.PARXER.PARXER_FUNCTIONS._FOR_.TRY.WIN       import externalTry      as eTry
from windows                                            import screenConfig, buildString

class EXTERNAL_TRY_WINDOWS:
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
            _type_      : str   = 'try',
            callbacks   : dict  = {}
            ):
        
        # set color on yellow
        self.bold           = bm.init.bold
        self.c              = self.bold+bm.fg.rbg(255, 255, 0)
        self.t              = 4
        if self.term == 'orion': pass
        else: self.c        = self.bold+c

        # tabulation
        self.tabulation                     = tabulation
        # reset
        self.reset                          = bm.init.reset
        # initialization of data 
        self.Data                           = data.base(c=self.c, reset=self.reset, key='...', tab=self.tabulation, active=False)
        # getting max size (max_x, max_y) of the window 
        self.max_x, self.max_y              = screenConfig.cursorMax()
        # when Ctrl+ option are used 
        self.indicator                      = None #
        # fixing the x-axis border 
        self.border_x_limit                 = True 
        # scroll list size 
        self.scroll_size                    = 11 #
        # story
        self.error                          = None
        # callbacks
        self.callbacks                      = callbacks
        # updating data 
        self.Data, self._index_             = ct.updating_callbacks(self.callbacks, self.Data)
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
        self.x                      = self.Data['size'] + 1 + self.tabulation * self.t
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
        self.index, self.if_line    = self._index_, self._index_
        ##########################################################################
        self.max_emtyLine        = 5
        self.try_cancel          = False 
        # struc for sub-function
        # struc for sub-function
        self.try_block         = {
            'index_finally'         : 0,
            'locked_error'          : [],
            'get_errors'            : [],
            'key_else_activation'   : None,
            'finally_key'           : False,
            'except_key'            : False,
            'active_calculations'   : False
        }
        # false if clean line is not activated else true
        self.clear_line          = False 
        # activation of tab
        self.active_tab          = None
        # history value
        self.history             = [ 'try' ]
        # loop
        self.loop                = []
        # storing value
        self.store_value         = []
        # accounting space line
        self.space          = 0
        # detecting if indentation was used
        self.active_tab     = None
        
        ##########################################################################

        while True:
            try:
                # get input
                self.char = string_to_chr.convert()
                if self.char:
                    _ = self.char[1]
                    self.char = self.char[0]
                    if self.char is not None:
                        if self.char == 3               :
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break

                        # indentation Tab
                        elif self.char == 9             :
                            if  self.x < (self.max_x - 4) :  
                                self.tt                  = ' ' * 4
                                self.Data['string']      =  self.Data['string'][ : self.Data["I_S"] ] + \
                                                                chr( self.char ) + self.Data['string'][ self.Data["I_S"] : ]
                                self.Data['input']       =  self.Data['input'][ : self.Data["index"] ] + \
                                                                str( self.tt ) + self.Data['input'][ self.Data["index"] : ]
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
                            if self.x > ( self.Data['size'] + 1):
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
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break
                        
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
                            ct.write(self.term, self.Data['input'], self.Data['main_input'], self.color, self.reset, show=True)
                            #####################################################################################
                            if self.Data['string']:
                                #calling the main module DEF 
                                #calling the main module TRY 
                                self.loop, self.try_cancel, self.error = eTry.EXTERNAL_TRY(master=self.Data['string'], 
                                        data_base = self.data_base, line=self.if_line, history=self.history, 
                                        store_value=self.store_value, space=self.space, 
                                        try_block=self.try_block).TRY(tabulation=self.tabulation,  loop=self.loop, 
                                        _type_=_type_ , c=c, term=self.term, callbacks=self.Data.copy())
                                
                                #break while loop if error is not None
                                if self.error is None: 
                                    if self.try_cancel is True : break 
                                    else: pass
                                else: break
                            else: 
                                # if no string
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.Data['string'] = self.analyse.BUILD_NON_CON(string=self.Data['string'], tabulation=self.tabulation)
                                    self.loop.append((self.Data['string'], False))
                                else:
                                    self.error = IfError.ERRORS(self.if_line).ERROR4()
                                    break
                            
                            #####################################################################################
                            # initializing all variables
                            self.if_line            += 1 
                            self.X, self.y           = screenConfig.cursor()
                            self.x                   = self.Data['size'] + 1 + self.tabulation * self.t
                            self.Data['string']      = "" + "\t" * self.tabulation
                            self.Data['input']       = "" + " " * (self.tabulation  * self.t)
                            self.Data['get']         = [[1 for i in range(4)] for j in range(self.tabulation)]
                            self.Data["I_S"]         = 0 + self.tabulation
                            self.Data["index"]       = 0 + self.tabulation * self.t
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
                                                        ct.buildingString(self.Data, self.a, self.b, verbose)
                                                        # string and I_S
                                                        ct.buildingString(self.Data, self.a_, self.b_, verbose, typ="string")
                                                        # re-writing the string 
                                                        ct.re_write(self.term, self.indicator, self.Data.copy(), self.color)
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
                                            ct.write(self.term, self.Data['input'], self.Data['main_input'], self.color, self.reset)
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
                            ct.write(self.term, self.Data['input'], self.Data['main_input'], self.color, self.reset)
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
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break
            except EOFError:
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break

        """
        # set color on yellow
        self.bold           = bm.init.bold
        self.c              = self.bold+bm.fg.rbg(255, 255, 0)
        if self.term == 'orion': pass
        else: self.c        = self.bold+c
        # reset color
        self.reset          = bm.init.reset
        # input initialized
        self.input          = '{}{} {}'.format(self.c,  "."*3, self.reset)
        # input main used to build the final string s
        self.main_input     = '{}{} {}'.format(self.c, "."*3, self.reset)
        # initial length of the input
        self.length         = len(self.input)
        # initialisation of index associated to the input
        self.index          = self.length
        # length of the foutth first char of input
        self.size           = len('... ')
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
        self.max_emtyLine        = 5
        self.try_cancel          = False 
        # struc for sub-function
        # struc for sub-function
        self.try_block         = {
            'index_finally'         : 0,
            'locked_error'          : [],
            'get_errors'            : [],
            'key_else_activation'   : None,
            'finally_key'           : False,
            'except_key'            : False,
            'active_calculations'   : False
        }
        # false if clean line is not activated else true
        self.clear_line          = False 
        self.active_tab          = None
        self.tabulation          = tabulation
        self.history             = [ 'try' ]
        self.loop                = []
        self.store_value         = []
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
        # fixing the x-axis border 
        self.border_x_limit      = True
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
        # currently cursor position (x, y)
        self.pos_x, self.pos_y      = cursor_pos.cursor()
        # terminal dimension (max_x, max_y)
        self.max_x, self.max_y      = test.get_win_ter()
        k  = windll.kernel32
        k.SetConsoleMode( k.GetStdHandle(-11), 7)
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
        self.max_x, self.max_y      = test.get_win_ter()
        self.save_cursor_position   = bm.save.save
        self.indicator_pos          = 0
        self.indicator_max          = 1
        self.key_max_activation     = True
        ###########################################################
        
        while True:
            try:
                # get input
                self.char = string_to_chr.convert()
                if self.char:
                    _ = self.char[1]
                    self.char = self.char[0]
                    if self.char is not None:
                        #if self.char is not None:
                        #building of str_drop_down only when ord( self.char ) is in self.sss 
                        if 32 <= self.char <= 126:
                            if self.border_x_limit is True:
                                self.pos_x, self.pos_y = cursor_pos.cursor()
                                if (self.max_x - int(self.pos_x)) > 0:
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
                                    if len(self.s) < self.max_x : self.border_x_limit = True 
                                    else: self.border_x_limit = False 
                                else: self.border_x_limit = False
                            else: pass
                        #delecting char in the str_drop_down string 
                        elif self.char in {8, 127}:
                            if self.border_x_limit is True:
                                sys.stdout.write(bm.clear.screen(pos=0))
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
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break
                        # writing char
                        elif 32 <= self.char <= 126:
                            ######################################
                            # each character has 1 as length     #
                            # have a look on ansi char           #
                            ######################################
                            if self.border_x_limit is True: 
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
                                
                                # fixing the cursor position conditions
                                if len(self.s) < self.max_x : self.border_x_limit = True 
                                else: self.border_x_limit = False 
                            else: pass
                        # moving cursor up, down, left, reight
                        elif self.char == 27:
                            next1, next2 = 91,  _
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
                                if (self.max_x - int(self.pos_x)) >= 4:
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
                                # fixing the cursor position conditions
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
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break
                        # crtl+g
                        elif self.char == 7: # crtl+g
                            self.indicator = self.char               
                        # auto slection mode ctrl+n
                        elif self.char == 14:
                            self.indicator = self.char
                        # End-Of-File Error ctrl+z
                        elif self.char == 26:
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break
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
                            if self.term == 'orion': print(self.main_input + self.bold+bm.words(string=self.s, color=bm.fg.rbg(255,  255, 255)).final())
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
                                #calling the main module TRY 
                                self.loop, self.try_cancel, self.error = eTry.EXTERNAL_TRY(master=self.string, data_base = self.data_base, line=self.if_line,
                                    history=self.history, store_value=self.store_value, space=self.space, 
                                    try_block=self.try_block).TRY(tabulation=self.tabulation,  loop=self.loop, _type_=_type_ , c=c, term=self.term)
                                
                                #break while loop if error is not None
                                if self.error is None: 
                                    if self.try_cancel is True : break 
                                    else: pass
                                else: break
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
                            self.border_x_limit = True 
                            self.pos_x, self.pos_y = cursor_pos.cursor()
                            
                        if self.border_x_limit is True:
                            # move cursor on left
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            # clear entire line
                            sys.stdout.write(bm.clear.line(pos=0))

                            if self.term == 'orion':
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
                                # computing the right position 
                                pos = len(self.s) + self.size + len(self.input) - self.index
                                # putting cursor a the correct position 
                                sys.stdout.write(bm.move_cursor.RIGHT(pos=pos))
                            else: pass

                            if self.max_y > 20:
                                if self.str_drop_down:
                                    if self.key_max_activation is True:
                                        sys.stdout.write(bm.save.save)
                                        if self.indicator is None:
                                            v, self.indicator_max, self.max_size, self.error = PE.DropDown(data_base = self.data_base,line=self.if_line).MENU( self.str_drop_down, 
                                                                        self.s, self.indicator, self.indicator_pos, (self.max_x-len(self.s)-self.size))
                                        else:
                                            sys.stdout.write(bm.clear.screen(pos=0))
                                            v, self.indicator_max, self.max_size, self.error = PE.DropDown(data_base = self.data_base, line=self.if_line).MENU( self.str_drop_down, 
                                                                        self.string, self.indicator, self.indicator_pos, (self.max_x-len(self.s)-self.size))
                                            #if self.error is None: pass 
                                            #else: pass
                                            if self.error is None :
                                                if v is not  None:
                                                    # moving cursor up to 1 if indicator is egal to 7< ctrl+g>
                                                    if self.indicator == 7: sys.stdout.write(bm.move_cursor.UP(pos=1))
                                                    # restoring the lastest saving cursor postion if indicator is egal to 65, 66 <ctrl+up>, <ctrl+down>
                                                    if self.indicator in {65, 66} : sys.stdout.write(bm.save.restore)
                                                    else: pass        
                                                    try:
                                                        if self.indicator not in {65, 66}:
                                                            self.string = self.string[ : len(self.string)-len(self.str_drop_down)] + v 
                                                            # customizing string 
                                                            self.error,  kappa, self.pos, self.get = SB.string( self.string ).build()

                                                            self.input  = kappa[0][0]
                                                            self.index  = kappa[0][1]
                                                            self.s      = kappa[1][0]
                                                            self.I      = kappa[1][1]
                                                            self.string = kappa[2][0]
                                                            self.I_S    = kappa[2][1]

                                                            if self.indicator == 14: self.str_drop_down = v; self.drop = len(v)
                                                            else: pass
                                                            # moving cursor on left
                                                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                                            # clearing entire line
                                                            sys.stdout.write(bm.clear.line(pos=0))
                                                            # re-writing string
                                                            sys.stdout.write(self.main_input+bm.string().syntax_highlight(name=bm.words(string=self.s, color=bm.fg.rbg(255, 255, 255)).final()))
                                                            # saving cursor position
                                                            sys.stdout.write(bm.save.save)
                                                        else: pass
                                                    except  TypeError: pass 
                                                else:
                                                    # moving cursor up to 1
                                                    sys.stdout.write(bm.move_cursor.UP(pos=1))
                                                    if self.index > 0:
                                                        # computing the right postion 
                                                        pos = len(self.s) + self.size + len(self.input) - self.index
                                                        # moving cursor at the correct position 
                                                        sys.stdout.write(bm.move_cursor.RIGHT(pos=pos))
                                                    else: pass
                                                    # erasing entire string 
                                                    sys.stdout.write(bm.clear.line(pos=2))
                                                    # re-writing string
                                                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                                    if self.term == 'orion':
                                                        sys.stdout.write(self.main_input + bm.string().syntax_highlight(
                                                            name=bm.words(string=self.s, color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()))
                                                    else: 
                                                        # any activation keyword & re-writing string
                                                        sys.stdout.write(self.main_input + bm.init.bold+bm.fg.rbg(255, 255, 255) + self.s + bm.init.reset)
                                                    # saving cursor position 
                                                    sys.stdout.write(bm.save.save)
                                            else: break
                                        # restoring cursor position 
                                        sys.stdout.write(bm.save.restore)
                                    else: pass
                                else: pass 
                                if self.indicator in {65, 66}: pass 
                                else:   self.indicator_pos, self.indicator_max = 0, 1
                                self.indicator = None
                            else: pass
                            sys.stdout.flush()
                        else: pass
                    else: pass 
                else: pass
            except KeyboardInterrupt:
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break
            except TypeError:
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break
        """
        #
        return self.loop,  self.error
     