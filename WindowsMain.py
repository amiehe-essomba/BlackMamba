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
        self.color = False
        self.tab = 1
        self.c = 0
        self.Input = ''
        self.Index = 0
        self.col = []
        self.delete = []
        self.line = 0

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
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[  self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]

                        self.index += len(name)
                        self.col.append(len(name))
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
                        if self.col:
                            self.input = self.input[: self.index + self.col[-1]] + name + self.input[self.index + self.col[-1]:]
                        else:
                            self.input = self.input[: self.index] + name + self.input[self.index:]
                        self.index += len(name)
                        self.col.append(len(name))
                    self.index += 1

                elif self.char in {10, 13}:  # enter
                    sys.stdout.write(u"\u001b[1000D")
                    self.clear_input = ansi_remove_chars(self.input[self.length:])
                    if self.clear_input:
                        ####################################################################
                        sys.stdout.write(bm.move_cursor.UP(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(self.input)
                        sys.stdout.flush()
                        sys.stdout.write(bm.move_cursor.DOWN(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(bm.move_cursor.LEFT(1000))
                        self.input = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset)
                        sys.stdout.write(self.input)
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

                    self.input = '{}>>> {}'.format(bm.fg.yellow_L, bm.init.reset)
                    self.index = self.length
                    count = 0
                    self.col = []
                    self.delete = []

                elif self.char == 9:  # tabular
                    self.tabular = '\t'
                    self.input = self.input[: self.index] + self.tabular + self.input[self.index:]
                    self.index += 4

                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                sys.stdout.write(bm.clear.line(0))
                sys.stdout.write(syntax_highlight(self.input))
                sys.stdout.write(bm.move_cursor.LEFT(1000))

                if self.index > 0:
                    sys.stdout.write(bm.move_cursor.RIGHT(self.index - self.sub_length))
                else:
                    pass

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
    os.system('cls')
    data_base = db.DATA_BASE().STORAGE()
    windows( data_base).terminal(bm.fg.rbg(255, 255, 255))