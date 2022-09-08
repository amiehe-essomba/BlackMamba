############################################
# IF statement IDE                         #
############################################
# created by : amiehe-essomba              #
# updating by: amiehe-essomba              #
############################################


import sys
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS._IF_                import IfError
from script.PARXER.PARXER_FUNCTIONS._FOR_.IF.WINDOWS import externalIF as eIF
from script                                             import control_string

class INTERNAL_IF_WINDOWS:
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
            bool_value  : bool,
            tabulation  : int,  
            c           : str   = '',
            _type_      : str   = 'conditional'
            ):
        
        self.if_line            = 0
        self.error              = None
     
        ##########################################################
        self.space              = 0
        self.active_tab         = None
        self.tabulation         = tabulation
        self.history            = [ 'if' ]
        self.loop               = []
        self.store_value        = []
      
        ##########################################################
        self.color              = bm.fg.rbg(255,255,0)
        self.input              = '{}... {}'.format(self.color, bm.init.reset)
        self.length             = len(self.input)
        self.index              = self.length
        self.sub_length         = len('{}{}'.format( self.color, bm.init.reset))
        # root of input 
        self.main_input         = '{}... {}'.format(self.color, bm.init.reset)
        self.Input              = ''
        self.Index              = 0
        self.max_emtyLine       = 5
        self.c                  = c
        self.mainString         = ''
        self.mainIndex          = 0
        self.if_cancel          = False
        ##########################################################
        
        # struc for sub-function
        self.else_block         = {
            'index_else'            : 0,
            'key_else_activation'   : None
        }
        ##########################################################
        # false if clean line is not activated else true
        self.clear_line = False      
        ##########################################################
        
        sys.stdout.write(bm.clear.line(2))
        sys.stdout.write(bm.move_cursor.LEFT(1000))
        sys.stdout.write(bm.string().syntax_highlight(name = self.input))
        sys.stdout.flush()

        while True :
            try:
                self.char = bm.read().readchar()
                if self.char not in {10, 13}:
                    # clear entire line
                    if self.char == 12:
                        # move cursor left 
                        self.error = IfError.ERRORS(self.if_line).ERROR4()
                        break
                    # clear entire screen
                    elif self.char == 19:
                        self.error = IfError.ERRORS(self.if_line).ERROR4()
                        break
                    # write char
                    else:
                        self.input      = self.input[: self.index] + chr(self.char) + self.input[self.index:]
                        self.mainString = self.mainString[: self.mainIndex] + chr(self.char) + self.mainString[  self.mainIndex:]
                        self.index      += 1
                        self.mainIndex  += 1
                    
                elif self.char in {10, 13}:
                    self.if_line += 1
                    
                    # movin cursor left
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                
                    if self.mainString:
                         ####################################################################
                        if self.term == 'orion':
                            # Syntaxis color 
                            self.input = self.input[: self.length] + bm.words(string=self.mainString, color=bm.fg.white_L).final()
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
                            # moving cursor down
                            sys.stdout.write(bm.move_cursor.DOWN(1))
                            # clear entire line
                            sys.stdout.write(bm.clear.line(2))
                        
                            # movin cursor left
                            sys.stdout.write(bm.move_cursor.LEFT(1000))
                        else:
                            # move cursor left
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            # clear entire line 
                            sys.stdout.write(bm.clear.line(2))
                            # write input 
                            sys.stdout.write(self.input)
                            # move left again 
                            sys.stdout.write(bm.move_cursor.LEFT(1000))
                        ######################################################################
                        
                        #calling the main module DEF 
                        self.loop, self.if_cancel, self.error = eIF.EXTERNAL_IF(master=self.mainString, data_base = self.data_base, line=self.if_line,
                            history=self.history, store_value=self.store_value, space=self.space, 
                            else_block=self.else_block).IF(bool_value=bool_value, tabulation=self.tabulation, 
                            loop=self.loop, _type_=_type_ , c=c, term=self.term)
                        
                        #break while loop if error is not None
                        if self.error is None: 
                            if self.if_cancel is True : break 
                            else: pass
                        else: break
                    else:
                        # if no string
                        if self.space <= self.max_emtyLine:
                            self.space += 1
                            self.mainString = self.analyse.BUILD_NON_CON(string=self.mainString,tabulation=self.tabulation)
                            self.loop.append((self.mainString, False))
                        else:
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break
                    
                    self.input      = self.main_input
                    self.index      = self.length
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
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                # move cusor left again 
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                
                # get cursor position 
                if self.index > 0:  sys.stdout.write(bm.move_cursor.RIGHT(pos=self.index - self.sub_length))
                else:  pass
                sys.stdout.flush()
            
            except KeyboardInterrupt:
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break

            except TypeError:
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break
        
        return self.loop,  self.error