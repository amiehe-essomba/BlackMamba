import sys, os, re
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from script.STDIN.WinSTDIN      import stdin
from script                     import control_string
from script.LEXER.FUNCTION      import main
from script.PARXER              import parxer_assembly
from script.DATA_BASE           import data_base as db

class windows:
    def __init__(self, data_base : dict):
        self.data_base  = data_base
        self.analyse    = control_string.STRING_ANALYSE({}, 1)

    def terminal(self, c: str = ''):

        self.input      = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset)
        self.length     = len(self.input)
        self.index      = self.length
        self.sub_length = len('{}{}'.format(bm.fg.yellow_L, bm.init.reset))
        self.tab        = 1
        self.Input      = ''
        self.Index      = 0
        self.line       = 0
        self.key        = False
        self.mainString = ''
        self.mainIndex  = 0

        sys.stdout.write(bm.string().syntax_highlight(name=self.input))
        sys.stdout.flush()
        while True:
            try:
                self.char = bm.read().readchar()
                if self.char not in {10, 13}:
                    self.input       = self.input[ : self.index ] + chr( self.char ) + self.input[ self.index : ]
                    self.mainString  = self.mainString[ : self.mainIndex ] + chr( self.char ) + self.mainString[ self.mainIndex : ]
                    self.index       += 1
                    self.mainIndex   += 1
                elif self.char in {10, 13}:  # enter
                    self.line += 1
                    sys.stdout.write(u"\u001b[1000D")
                    self.clear_input = self.mainString
                    if self.clear_input:
                        ####################################################################
                        self.input = self.input[: self.length] + bm.words(string=self.mainString, color=bm.fg.white_L).final()
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        sys.stdout.write(bm.move_cursor.UP(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(self.input)
                        sys.stdout.flush()
                        sys.stdout.write(bm.move_cursor.DOWN(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(bm.move_cursor.LEFT(1000))
                        ######################################################################

                        self.lexer, self.normal_string, self.error = main.MAIN(self.clear_input, self.data_base, self.line).MAIN()
                        if self.error is None :
                            if self.lexer is not None:
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

                    self.input      = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset)
                    self.index      = self.length
                    self.key        = False
                    self.mainString = ''
                    self.mainIndex  = 0
                elif self.char == 9:  # tabular
                    self.tabular = '\t'
                    self.input = self.input[: self.index] + self.tabular + self.input[self.index:]
                    self.index += 1

                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                sys.stdout.write(bm.clear.line(0))
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.write(bm.move_cursor.LEFT(1000))

                if self.index > 0:  sys.stdout.write(bm.move_cursor.RIGHT(self.index - self.sub_length))
                else:   pass

                sys.stdout.flush()

            except KeyboardInterrupt:
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                return
            except IndexError:
                self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                print(self._end_of_file_)
                self.input = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset)
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.flush()

if __name__ == '__main__':

    try:
        os.system('cls')
        bm.head().head(sys='Windows')
        data_base = db.DATA_BASE().STORAGE()
        windows( data_base=data_base).terminal(c=bm.fg.rbg(255, 255, 255))
    except KeyboardInterrupt:  pass
    except IndexError: pass