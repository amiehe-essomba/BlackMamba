############################################
# Main IDE for windows called when BM      #  
# is running in windows sys                #
############################################
# created by : amiehe-essomba              #
# updating by: amiehe-essomba              #
############################################

import sys, os
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from script                     import control_string
from script.LEXER.FUNCTION      import main
from script.PARXER              import parxer_assembly
from script.DATA_BASE           import data_base as db

class windows:
    def __init__(self, data_base : dict):
        self.data_base  = data_base
        self.analyse    = control_string.STRING_ANALYSE({}, 1)

    def terminal(self, c: str = ''):

        self.input      = '{}>>>{} {}'.format(bm.fg.yellow_L, c, bm.init.reset)
        self.length     = len(self.input)
        self.index      = self.length
        self.sub_length = len('{}{}{}'.format(bm.fg.yellow_L, c, bm.init.reset))
        self.Index      = 0             # index char in Input 
        self.line       = 0             # line 
        self.key        = False         # key
        self.mainString = ''            # String used in BM
        self.mainIndex  = 0             # String index
    
        sys.stdout.write(bm.string().syntax_highlight(name=self.input))
        sys.stdout.flush()
        
        while True:
            try:
                self.char = bm.read().readchar()
                if self.char not in {10, 13}:
                    if self.char != 12:
                        self.input       = self.input[ : self.index ] + chr( self.char ) + self.input[ self.index : ]
                        self.mainString  = self.mainString[ : self.mainIndex ] + chr( self.char ) + self.mainString[ self.mainIndex : ]
                        self.index       += 1
                        self.mainIndex   += 1
                    else: os.system('cls')

                elif self.char in {10, 13}:  # enter
                    self.line += 1
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    if self.mainString:
                        ####################################################################
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
                        
                        ######################################################################

                        # running lexer 
                        self.lexer, self.normal_string, self.error = main.MAIN(self.mainString, self.data_base, self.line).MAIN()
                        if self.error is None :
                            if self.lexer is not None:
                                
                                # running parser 
                                self.num, self.key, self.error = parxer_assembly.ASSEMBLY(self.lexer, self.data_base,
                                                                        self.line).GLOBAL_ASSEMBLY(self.normal_string)
                                if self.error is None:  pass
                                else:
                                    sys.stdout.write(bm.clear.line(2))
                                    sys.stdout.write(bm.move_cursor.LEFT(1000))
                                    print('{}\n'.format(self.error))
                                    self.error = None
                            else:  pass
                        else:
                            sys.stdout.write(bm.clear.line(2))
                            sys.stdout.write(bm.move_cursor.LEFT(1000))
                            print('{}\n'.format(self.error))
                            self.error = None
                    else:  pass

                    # initialization 
                    self.input      = '{}>>>{} {}'.format(bm.fg.yellow_L, c, bm.init.reset)
                    self.index      = self.length
                    self.key        = False
                    self.mainString = ''
                    self.mainIndex  = 0
                    
                elif self.char == 9:  # tabular
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

                # updating cursor position on the line 
                if self.index > 0:  sys.stdout.write(bm.move_cursor.RIGHT(self.index - self.sub_length))
                else:   pass

                # flush
                sys.stdout.flush()

            #keyboardInterrupt
            except KeyboardInterrupt:
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset+bm.init.reset
                print(self._keyboard_)
                return
            # EOF
            except IndentationError:
                self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset+bm.init.reset
                print(self._end_of_file_)
                self.input = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset)
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.flush()

if __name__ == '__main__':

    try:
        os.system('cls')
        bm.head().head(sys='Windows')
        data_base = db.DATA_BASE().STORAGE().copy()
        windows( data_base=data_base).terminal(c=bm.fg.rbg(255, 255, 255))
    except KeyboardInterrupt:  pass
    except IndentationError: pass
