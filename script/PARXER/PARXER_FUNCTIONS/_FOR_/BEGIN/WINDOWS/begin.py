############################################
# BEGIN statement IDE                      #
############################################
# created by : amiehe-essomba              #
# updating by: amiehe-essomba              #
############################################


import sys
from script                                             import control_string
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import cmtError as ce
from script.PARXER.PARXER_FUNCTIONS._FOR_.BEGIN.WINDOWS import comment as cmt
from script.PARXER.PARXER_FUNCTIONS._IF_                import IfError

class COMMENT_WINDOWS:
    def __init__(self,
                 data_base: dict,
                 line: int,
                 term: str
                 ) -> None:

        # current line
        self.line = line
        # main data base
        self.data_base = data_base
        # terminal name
        self.term = term
        # contriling string
        self.analyse = control_string.STRING_ANALYSE(self.data_base, self.line)

    def COMMENT(self,
                tabulation  : int = 1,
                c           : str = ''
                ):

        ############################################################################
        self.error          = None
        self.string         = ''
        self.normal_string  = ''
        self.store_value    = []
        ############################################################################
        self.space          = 0
        self.tabulation     = tabulation
        self.history        = ['comment']
        self.max            = 100
        self.locked         = False
        self.comment_storage= []
        self.comment_name   = None
        ############################################################################
        self.color          = bm.fg.rbg(255, 0, 255)
        self.main_input     = '{}cmt {}'.format(self.color, bm.init.reset)
        self.input          = self.main_input
        self.length         = len(self.main_input)
        self.index          = self.length
        self.sub_length     = len('{}{}'.format(self.color, bm.init.reset))
        self.Input          = ''
        self.Index          = 0
        self.if_line        = 0
        self.mainString     = ''
        self.mainIndex      = 0
        self.loop           = []
        self.end_comment    = False
        ############################################################################

        sys.stdout.write(bm.clear.line(2))
        sys.stdout.write(bm.move_cursor.LEFT(1000))
        sys.stdout.write(bm.string().syntax_highlight(name=self.input))
        sys.stdout.flush()

        while True:
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
                    else:
                        self.input      = self.input[: self.index] + chr(self.char) + self.input[self.index:]
                        self.mainString = self.mainString[: self.mainIndex] + chr(self.char) + self.mainString[ self.mainIndex:]
                        self.index      += 1
                        self.mainIndex  += 1
                elif self.char in {10, 13}:  # enter
                    self.if_line += 1
                    sys.stdout.write(bm.move_cursor.LEFT(1000))
                    if self.mainString:
                        ####################################################################
                        self.s, self.t, self.err = self.analyse.BUILD_CON(string=self.mainString, tabulation=self.tabulation)
                        if self.err is None:
                            if (self.t - 1) >= 0:  self.end_comment = True
                            else:  self.end_comment = False
                        else: self.end_comment = False

                        if self.term == 'orion':
                            # Syntaxis color
                            self.input = self.input[: self.length] + bm.words(string=self.mainString,  color=c).final(locked=self.end_comment, n=0)
                            # moving cursor left
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

                        self.loop, self.begin_cancel, self.locked, self.error = cmt.COMMENT(master=self.mainString, data_base=self.data_base,
                                    line=self.if_line, space=self.space, history=self.history,  store_value=self.store_value,
                                    save_block=self.locked, comment_storage=self.comment_storage).LINE( loop=self.loop,
                                    tabulation=self.tabulation)

                        if self.error is None:
                            if self.begin_cancel is True : break
                            else: pass
                        else: break

                    else:
                        if self.space <= self.max:
                            self.space += self.max
                            self.mainString = self.analyse.BUILD_NON_CON(string=self.mainString,  tabulation=self.tabulation)
                            self.loop.append((self.mainString, False))
                        else:
                            self.error = ce.ERRORS(self.if_line).ERROR4()
                            break

                    self.input      = self.main_input
                    self.index      = self.length
                    self.mainString = ''
                    self.mainIndex  = 0
                elif self.char == 9:  # tabular
                    self.tabular    = '\t'
                    self.input      = self.input[: self.index] + self.tabular + self.input[self.index:]
                    self.index      += 1

                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                sys.stdout.write(bm.clear.line(pos=0))
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                if self.index > 0: sys.stdout.write(bm.move_cursor.RIGHT(pos=self.index - self.sub_length))
                else: pass
                sys.stdout.flush()

            except TypeError:
                self.error = ce.ERRORS(self.if_line).ERROR4()
                break

            except KeyboardInterrupt:
                self.error = ce.ERRORS(self.if_line).ERROR4()
                break

        #############################################################################

        return self.loop, self.error