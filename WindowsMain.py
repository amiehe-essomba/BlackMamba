import sys, os, re
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from script.STDIN.WinSTDIN      import stdin
from script                     import control_string
from script.LEXER.FUNCTION      import main
from script.PARXER              import parxer_assembly
from script.DATA_BASE           import data_base as db

def readchar():
    fd = sys.stdin.fileno()
    ch = ord(sys.stdin.read(1))
    return ch

def syntax_highlight(name: str):
    stripped = name.rstrip()
    return stripped + bm.bg.blue_L + " " * (len(name) - len(stripped)) + bm.init.reset

def ansi_remove_chars(name: str):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', name)

def show(name: str):
    try:
        float_name = float(name)
        print_name = '\n{}[ {}result{} ] : {}{}{}\n'.format(bm.fg.magenta_M, bm.fg.red_L, bm.fg.magenta_M,
                                                            bm.fg.green_L, float_name, bm.init.reset)
        print(print_name)

    except:
        print_name = '\n\n{}[ {}result{} ] : {}{}\n'.format(bm.fg.magenta_M, bm.fg.red_L, bm.fg.magenta_M,
                                                            bm.init.reset, name)
        print(print_name)

def tabular(string: str):
    count = 0
    newString = string

    if string:
        for i, e in enumerate(string):
            if i == 0:
                if e == '\t':
                    count += 1
                else:
                    break
            else:
                if string[i - 1] == '\t':
                    count += 1
                else:
                    break
    else:
        pass
    if count > 0:
        newString = string[count:]
    else:
        pass

    return newString

class windows:
    def __init__(self, data_base : dict):
        self.data_base  = data_base
        self.analyse    = control_string.STRING_ANALYSE({}, 1)

    def terminal(self, c: str = ''):

        self.input = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset)
        self.length = len(self.input)
        self.index = self.length
        self.sub_length = len('{}{}'.format(bm.fg.yellow_L, bm.init.reset))
        self.color      = False
        self.tab        = 1
        self.c          = 0
        self.Input      = ''
        self.Index      = 0
        self.col        = []
        self.delete     = []
        self.line       = 0
        self.key        = False
        self.funcs      = ['if', 'unless', 'switch', 'try', 'while', 'until', 'for', 'begin', 'def', 'class', 'print'
                           'from', 'load']
        self.func_colors = [ bm.fg.magenta_M,  bm.fg.magenta_M,  bm.fg.magenta_M, bm.fg.magenta_M,  bm.fg.magenta_M,
                             bm.fg.magenta_M,  bm.fg.magenta_M, bm.fg.rbg(0, 255, 0), bm.fg.rbg(0, 255, 225),
                             bm.fg.rbg(225, 225, 0), bm.fg.rbg(195, 20, 195), bm.fg.rbg(20, 195, 125), bm.fg.rbg(20, 195, 125)]
        self.func_len   = [2, 6, 5, 3]

        self.sub_funcs  = ['pass', 'break', 'continue', 'exit', 'next']
        self.sub_colors = bm.fg.green_L
        self.sub_func_len   = [2, 3, 4, 5, 8 ]

        sys.stdout.write(syntax_highlight(self.input))
        sys.stdout.flush()
        while True:
            self.line += 1
            try:
                self.char = readchar()
                if 32 <= self.char <= 126:
                    if self.char in [42, 43, 45, 37, 94, 47]:  # {+, -, *, /, %, ^}
                        name = bm.fg.red_L + chr(self.char) + bm.init.reset
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[ self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
                    elif self.char in [40, 41]:  # ( )
                        name = bm.fg.green_L + chr(self.char) + bm.init.reset
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[  self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
                    elif self.char in [91, 93]:  # { }
                        name = bm.fg.rbg(255, 20, 174)  + chr(self.char) + bm.init.reset
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[  self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
                    elif self.char in [123, 125]:  # [, ]
                        name = bm.fg.rbg(255,170, 100 ) + chr(self.char) + bm.init.reset
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[  self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
                    elif self.char in [33, 38, 60, 61, 62, 63, 124]:  # {=, !, <, >, ?,|, &}
                        name = bm.fg.cyan_L + chr(self.char) + bm.init.reset
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[  self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
                    elif self.char in [36]:  # { $ }
                        name = bm.fg.yellow_L + chr(self.char) + bm.init.reset
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[ self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
                    elif self.char in [35]:  # { # }
                        name = bm.fg.rbg(20, 20, 20) + chr(self.char) + bm.init.reset
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[ self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
                    elif self.char in [64]:  # { @ }
                        name = bm.fg.rbg(225, 225, 0) + chr(self.char) + bm.init.reset
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[ self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
                    elif self.char in [46]:  # { . }
                        name = bm.fg.rbg(0, 255, 0) + chr(self.char) + bm.init.reset
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[ self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
                    elif self.char in [58]:  # { : }
                        name = bm.fg.rbg(0, 200, 0) + chr(self.char) + bm.init.reset
                        if self.col:  self.input = self.input[: self.index + self.col[-1]] + name + self.input[  self.index + self.col[-1]:]
                        else:  self.input = self.input[: self.index] + name + self.input[self.index:]
                        self.col.append(len(name))
                        self.index  += len(name)

                        self.s      = ansi_remove_chars(self.input[self.length:])
                        self.r      = bm.init.reset
                        self.newS   = ''
                        self.cc     = ''

                        for _s_ in [3, 5]:
                            try:
                                if self.s[: _s_] in ['try', 'begin']:
                                    self.idd = self.funcs.index(self.s[: _s_])
                                    self.cc = self.func_colors[self.idd]
                                    if self.s[-1] == ':':
                                        self.newS = self.s[: _s_]
                                        break
                                    else:  pass
                                else:   pass
                            except IndexError:  pass

                        if self.newS:
                            name = ''
                            for _s_ in self.newS:  name += self.cc + _s_ + self.r
                            if self.key is False: self.ss = len(c + bm.init.reset) * len(self.newS) + len(self.newS)
                            else:  self.ss = len(name)

                            self.input  = self.input[: self.length] + name + self.input[self.length + self.ss:]
                            self.index  = len(self.input)
                            self.key    = True
                        else:  pass
                    elif self.char in [32]:
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + chr(self.char) + self.input[ self.index + self.col[-1]:]
                        else:  self.input = self.input[: self.index] + chr(self.char) + self.input[self.index:]
                        self.s      = ansi_remove_chars(self.input[ self.length : ])
                        self.r      = bm.init.reset
                        self.newS   = ''
                        self.cc     = ''

                        for _s_ in self.func_len:
                            try:
                                if self.s[ : _s_] in self.funcs:
                                    self.idd    = self.funcs.index(  self.s[ : _s_] )
                                    self.cc     = self.func_colors[ self.idd ]
                                    if self.s[ _s_ ] in [ ' ' ]:
                                        self.newS = self.s[ : _s_ ]
                                        break
                                    else : pass
                            except IndexError :  pass

                        if not self.newS:
                            for _s_ in self.sub_func_len:
                                try:
                                    if self.s[: _s_] in self.sub_funcs:
                                        self.idd    = self.funcs.index(self.s[: _s_])
                                        self.cc     = self.sub_colors
                                        self.newS = self.s[: _s_]
                                        break
                                except IndexError: pass
                        else: pass

                        if self.newS :
                            name = ''
                            for _s_ in self.newS:
                                name += self.cc + _s_ + self.r
                            if self.key is False: self.ss = len(c + bm.init.reset) * len(self.newS) + len(self.newS)
                            else: self.ss = len(name)
                            self.input = self.input[: self.length] + name + self.input[self.length + self.ss:]
                            self.index = len(self.input)
                            self.key = True
                        else: pass

                        self._, self.l, self.lc = bm.keyword(master=self.s, color=self.col, str_modified=self.input).keyword(n=self.length)
                        if self._ is None: pass
                        else: self.input, self.index, self.col = self._, self.l, self.lc

                    elif self.char in [34, 39]:  # { ", ' }
                        name = bm.fg.rbg(200, 150, 100) + chr(self.char) + bm.init.reset
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
                    elif self.char in [x for x in range(48, 58)]:
                        name = bm.fg.magenta + chr(self.char) + bm.init.reset
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
                    else:
                        name = c + chr(self.char) + bm.init.reset
                        if self.col:  self.input = self.input[ : self.index + self.col[-1]] + name + self.input[self.index + self.col[-1] : ]
                        else:  self.input = self.input[: self.index] + name + self.input[ self.index : ]
                        self.col.append(len(name))
                        self.index += len(name)

                        self.s = ansi_remove_chars(self.input[self.length:])
                        self.r = bm.init.reset
                        self.newS = ''
                        self.cc = ''

                        for _s_ in self.sub_func_len:
                            try:
                                if self.s[: _s_] in self.sub_funcs:
                                    self.idd    = self.funcs.index(self.s[: _s_])
                                    self.cc     = self.sub_colors
                                    self.newS   = self.s[: _s_]
                                    break
                                else:  pass
                            except IndexError:  pass

                        if self.newS:
                            name = ''
                            for _s_ in self.newS:  name += self.cc + _s_ + self.r
                            if self.key is False: self.ss = len(c + bm.init.reset) * len(self.newS) + len(self.newS)
                            else: self.ss = len(name)

                            self.input  = self.input[: self.length] + name + self.input[self.length + self.ss:]
                            self.index  = len(self.input)
                            self.key    = True
                        else:  pass
                    self.index += 1

                elif self.char in {10, 13}:  # enter
                    sys.stdout.write(u"\u001b[1000D")
                    self.clear_input = ansi_remove_chars(self.input[self.length:])
                    f = open('op', 'w')
                    f.write(self.clear_input)
                    f.close()

                    if self.clear_input:
                        ####################################################################
                        sys.stdout.write(bm.move_cursor.UP(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(self.input)
                        sys.stdout.flush()
                        sys.stdout.write(bm.move_cursor.DOWN(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(bm.move_cursor.LEFT(1000))
                        #self.input = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset)
                        #sys.stdout.write(self.input)
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
                                    #sys.stdout.write(bm.move_cursor.DOWN(1))
                                    print('{}\n'.format(self.error))
                                    self.error = None
                            else:  pass
                        else:
                            sys.stdout.write(bm.clear.line(2))
                            sys.stdout.write(bm.move_cursor.LEFT(1000))
                            print('{}\n'.format(self.error))
                            self.error = None
                    else:  pass

                    self.input  = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset)
                    self.index  = self.length
                    count       = 0
                    self.col    = []
                    self.delete = []
                    self.key    = False
                    self.cc     = ''
                    self.newS   = ''

                elif self.char == 9:  # tabular
                    self.tabular = '\t'
                    self.input = self.input[: self.index] + self.tabular + self.input[self.index:]
                    self.index += 4

                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                sys.stdout.write(bm.clear.line(0))
                sys.stdout.write(syntax_highlight(self.input))
                sys.stdout.write(bm.move_cursor.LEFT(1000))

                if self.index > 0:  sys.stdout.write(bm.move_cursor.RIGHT(self.index - self.sub_length))
                else:   pass

                sys.stdout.flush()

            except KeyboardInterrupt:
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                return
            except TypeError:
                self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                print(self._end_of_file_)
                self.input = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset)
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.flush()

if __name__ == '__main__':
    try:
        os.system('cls')
        data_base = db.DATA_BASE().STORAGE()
        windows( data_base).terminal(bm.fg.rbg(255, 255, 255))
    except KeyboardInterrupt:  pass
    except TypeError: pass