############################################
# DEF function IDE                         #
############################################
# created by : amiehe-essomba              #
# updating by: amiehe-essomba              #
############################################


import os, sys
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS._IF_                import IfError
from src.functions.windows                              import updatingDef as UD
from src.functions.windows                              import internalDef as ID
from script                                             import control_string

class INTERNAL_DEF_WINDOWS:
    def __init__(self, 
                data_base   : dict, 
                line        : int
                ):
    
        self.line               = line
        self.data_base          = data_base
        #contriling string
        self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)

    def TERMINAL( self, 
            tabulation  : int,  
            class_name  : str   = '' , 
            class_key   : bool  = False,
            c           : str   = '',
            function    : str   = 'def',
            _type_      : str   = 'def'
            ):
        
        self.if_line            = 0
        self.error              = None
     
        ##########################################################
        self.space              = 0
        self.active_tab         = None
        self.tabulation         = tabulation
        self.history            = [ 'def' ]
        self.def_starage        = []
        self.store_value        = []
      
        ##########################################################
        self.color              = bm.fg.rbg(255,255,0)
        self.input              = '{}... {}'.format(self.color, bm.init.reset)
        self.length             = len(self.input)
        self.index              = self.length
        self.sub_length         = len('{}{}'.format( self.color, bm.init.reset))
        self.Input              = ''
        self.Index              = 0
        self.max_emtyLine       = 5
        self.c                  = c
        self.previous_c         = c
        self.mainString         = ''
        self.mainIndex          = 0
        self.subFunc            = {}
        self.def_cancel         = False
        ##########################################################
               
        sys.stdout.write(bm.clear.line(2))
        sys.stdout.write(bm.move_cursor.LEFT(1000))
        sys.stdout.write(bm.string().syntax_highlight(name = self.input))
        sys.stdout.flush()

        while True :
            try:
                self.char = bm.read().readchar()
                if self.char not in {10, 13}:
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
                        # syntaxis color 
                        self.input = self.input[: self.length] + bm.words(string=self.mainString, color=self.c).final(n=1)
                        
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
                        ######################################################################
                        
                        #calling the main module DEF 
                        self.def_cancel, self.error = ID.INTERNAL_DEF(master=self.mainString, data_base = self.data_base, line=self.if_line,
                            history=self.history, store_value=self.store_value, space=self.space).DEF(  tabulation=self.tabulation, 
                            def_starage=self.def_starage, class_name=class_name, class_key=class_key, c=c, function=function,
                            _type_=_type_ )
                            
                        #break while loop if error is not None
                        if self.error is None: 
                            if self.def_cancel is True: break 
                            else: pass
                        else: break
                    else:
                        # if no string
                        if self.space <= self.max_emtyLine:
                            self.space += 1
                            self.mainString = self.analyse.BUILD_NON_CON(string=self.mainString,tabulation=self.tabulation)
                            self.def_starage.append((self.mainString, False))
                        else:
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break
                    
                    self.input      = '{}... {}'.format(self.color, bm.init.reset)
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
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break

            except TypeError:
                self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break
        
        # updating function 
        UD.UPDATING(self.data_base ).UPDATE_FUNCTION( self.def_starage, self.subFunc )
        
        return self.error