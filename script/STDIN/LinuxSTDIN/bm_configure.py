import             datetime
import             webbrowser
import             re, os, sys
from   sys         import stdout, stdin
from   time        import sleep
from   datetime    import datetime
from   tkinter     import *
from script        import control_string

class fg:
    black       = u"\u001b[30m"
    red         = u"\u001b[31m"
    green       = u"\u001b[32m"
    yellow      = u"\u001b[33m"
    blue        = u"\u001b[34m"
    magenta     = u"\u001b[35m"
    cyan        = u"\u001b[36m"
    white       = u"\u001b[37m"

    black_L     = u"\u001b[30;1m"
    red_L       = u"\u001b[31;1m"
    green_L     = u"\u001b[32;1m"
    yellow_L    = u"\u001b[33;1m"
    blue_L      = u"\u001b[34;1m"
    magenta_M   = u"\u001b[35;1m"
    cyan_L      = u"\u001b[36;1m"
    white_L     = u"\u001b[37;1m"

    def rbg(r, g, b): 
        return f"\u001b[38;2;{r};{g};{b}m"

class bg:
    black       = u"\u001b[40m"
    red         = u"\u001b[41m"
    green       = u"\u001b[42m"
    yellow      = u"\u001b[43m"
    blue        = u"\u001b[44m"
    magenta     = u"\u001b[45m"
    cyan        = u"\u001b[46m"
    white       = u"\u001b[47m"

    black_L     = u"\u001b[40;1m"
    red_L       = u"\u001b[41;1m"
    green_L     = u"\u001b[42;1m"
    yellow_L    = u"\u001b[43;1m"
    blue_L      = u"\u001b[44;1m"
    magenta_L   = u"\u001b[45;1m"
    cyan_L      = u"\u001b[46;1m"
    white_L     = u"\u001b[47;1m"

    def rgb(r, g, b): 
        return f"\u001b[48;2;{r};{g};{b}m"

class init:
    reset       = u"\u001b[0m"
    bold        = u"\u001b[1m"
    underline   = u"\u001b[4m"
    reverse     = u"\u001b[7m"

class clear:
    clear       = u"\u001b[2J"
    def line( pos : int ):
        # 2 = entire line
        # 1 = from the cursor to start of line
        # 0 = from the cursor to begenning of line
        clearline   = u"\u001b[" + f"{pos}" + "K"
        return clearline

class move_cursor:
    move = u"\u001b[?12h"

    def __init__(self):
        pass

    def UP( pos: int ):
        up          = u"\u001b[" + str( pos ) + "A"
        return up

    def DOWN( pos: int ):
        down        = u"\u001b[" + str( pos ) + "B"
        return down  
    
    def RIGHT( pos: int ):
        right       = u"\u001b[" + str( pos ) + "C"
        return right

    def LEFT(pos: int):
        left        = u"\u001b[" + str( pos ) + "D"
        return left

class cursor_pos:
    def to(self, x:int, y:int):
        return f"\u001b[{y};{x}H"

class line:
    nextline = "\u001b[1E"
    prevline = "\u001b[1F"

class head:
    
    def head( self, sys : str = 'Linux' ):
        block = [
                '\n',
                'Black Mamba programming language -version- 1.0.0. MIT License.',
                f'[ {sys} version ] type help( arg ), License() for more informations.',
                '>> ',
                'written by amiehe-essomba',
                'email: ibamieheessomba@unistra.fr',
                '\n',
                ''
                ]

        wait    = 0.0005

        head().tip(block[ 0 ], 0, wait)
        head().tip(block[ 1 ], 1, wait, sys)
        head().tip(block[ 2 ], 2, wait, sys)
        #head().tip(block[ 3 ], 3, wait)
        #head().tip(block[ 4 ], 4, wait)
        #head().tip(block[ 5 ], 5, wait)
        head().tip(block[ 6 ], 6, wait)

    
    def tip( self, text : str , n : int, wait : float, sys: str='Linux' ):
        string      = ''
        nString1    = f'{fg.rbg(255,255,0)}{init.underline}Black Mamba{init.reset} {fg.rbg(255,255,255)}programming language ' \
                  f'{fg.rbg(255,0,255)}-version- 1.0.0. {fg.rbg(255,255,255)}{chr(169)} 2022 {fg.rbg(0,255,255)}MIT License.{init.reset}'
        nString2    = f'{fg.rbg(255,255,255)}[ {fg.rbg(0,255,0)}{sys} version {fg.rbg(255,255,255)}] ' \
                      f'{fg.rbg(255,255,255)}type help( {fg.rbg(255,0,0)}arg{fg.rbg(255,255,255)} ), ' \
                      f'License() for more informations.{init.reset}'
        for i, char in enumerate( text ):
            string += char 
            stdout.write(char )
            if i < len( text ) - 1:  pass
            else:
                if n in [ 1 ]:
                    stdout.write( move_cursor.LEFT( 1000 ) )
                    print( nString1 )
                if n in [ 2 ]:
                    stdout.write( move_cursor.LEFT( 1000 ) )
                    print( nString2 )
                elif n in [ 3 ]:
                    stdout.write( move_cursor.LEFT( 1000 ) )
                    print( '{}{}{}{}'.format( fg.white_L, text, datetime.now(), init.reset) )
                elif n in [ 4 ]:
                    stdout.write( move_cursor.LEFT( 1000 ) )
                    print( '{}{}{}'.format( fg.white_L, text, init.reset) )
                elif n in [ 5 ]:
                    stdout.write( move_cursor.LEFT( 1000 ) )
                    print( '{}{}{}'.format( fg.cyan_L, text, init.reset) )

            stdout.flush()
            sleep( wait )

class open_graven:
    def __init__(self):
        self.name = 1
    def openG(self):
        self.window = Tk()
        self.window.title('Main Help')
        self.window.geometry("600x120")
        self.window.minsize(600, 120)
        self.window.maxsize(600, 120)

        self.main_menu = Menu(self.window, background='ivory', font=('Arila', 8), relief=FLAT)
        self.window.config(menu=self.main_menu)

        self.main1 = Menu(self.main_menu, tearoff=0)
        self.help = ['function_name', 'class_name', 'var_name']
        for name in self.help:
            self.main1.add_checkbutton(label=name, command=self.window.quit, state='active')
        self.main1.add_separator()

        self.main_menu.add_cascade(label='Names', menu=self.main1)
        self.main_menu.add_command(label='License', command= lambda : open_graven().open_graven_web())
        self.main_menu.add_command(label='Quit', command=self.window.destroy)

        self.window.mainloop()

    def open_graven_web(self):
        webbrowser.open(url='https://github.com/amiehe-essomba/BlackMamba/blob/BlackMamba/LICENSE')

class remove_ansi_chars:
    def chars( self, name : str ):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub ('', name) 

class read:
    def readchar(self):
        try:
            fd  = sys.stdin.fileno()
            ch = ord( sys.stdin.read( 1 ) )
            return ch
        except TypeError: pass

class string:
    def __init__(self):
        pass
    def syntax_highlight( self, name : str ):
        self.stripped = name.rstrip()
        return self.stripped + bg.blue_L + " " * ( len( name ) - len( self.stripped ) ) + init.reset

class words:
    def __init__(self, string : str, color : str):
        self.string     = string
        self.color      = color
        self.analyse    = control_string.STRING_ANALYSE({}, 1)

    def alphabetic(self):
        return list('abcdefghijklmnopqrstuvwxyzTFN')

    def keywords(self, n:int=0):
        self.newString  = ''
        self.stringKey  = ''
        self.active     = False
        self.ss         = ''
        self.count      = 0
        self.k          = []

        if      self.string in ['in', 'not']:
            self.newString  += fg.rbg(255,128,128)+self.string+init.reset
        elif      self.string in ['True', 'False', 'None']:
            self.newString  += fg.rbg(204,153,255)+self.string+init.reset
        elif    self.string in ['pass', 'break', 'continue', 'exit', 'next']:
            self.newString += fg.rbg(153,204,0) + self.string + init.reset
        elif    self.string in ['if', 'unless', 'else', 'elif', 'for', 'switch', 'case', 'default',
                                   'try', 'except', 'finally', 'while', 'until', 'begin', 'save']:
            self.newString +=  fg.rbg(51, 102, 255) + self.string + init.reset
        elif    self.string == 'end':
            if n == 0: self.newString +=  fg.rbg(51, 102, 255) + self.string + init.reset
            else: self.newString +=  fg.rbg(255,165,0) + self.string + init.reset
        elif    self.string in ['int', 'float', 'cplx', 'list', 'tuple', 'none', 'range', 'str',
                                'bool', 'dict', 'any']:
            self.newString += fg.rbg(240,128,128) + self.string + init.reset
        elif    self.string in ['from', 'load', 'module', 'as']:
            self.newString += fg.rbg(225, 50, 20) + self.string + init.reset
        elif    self.string in ['def', 'class']:
            self.newString += fg.rbg(255,165,0) + self.string + init.reset
        else:
            for i, s in enumerate(self.string):

                if self.count % 2 == 0:
                    if self.active is False:
                        if s in {'+', '-', '*', '^', '%', '/'}:
                            self.newString += fg.rbg(255, 0, 0) + s + init.reset
                        elif s in [str(x) for x in range(10)]:
                            if i == 0:
                                try:
                                    if self.string[ 1 ] in self.analyse.LOWER_CASE()+self.analyse.UPPER_CASE():
                                        self.newString += self.color + s + init.reset
                                    else: self.newString += fg.rbg(255, 0, 255) + s + init.reset
                                except IndexError: self.newString += fg.rbg(255, 0, 255) + s + init.reset
                            else:
                                if self.string[i - 1] in self.analyse.LOWER_CASE() + self.analyse.UPPER_CASE():
                                    self.newString += self.color + s + init.reset
                                else: self.newString +=fg.rbg(255, 0, 255) + s + init.reset

                        elif s in {'(', ')'}:
                            self.newString += fg.rbg(0, 255, 0) + s + init.reset
                        elif s in {'{', '}'}:
                            self.newString += fg.rbg(186,85,211) + s + init.reset
                        elif s in {'[', ']'}:
                            self.newString += fg.rbg(255, 255, 0) + s + init.reset
                        elif s in {'<', '>', '=', '!', '|', '&', '?'}:
                            self.newString += fg.rbg(255, 102, 0) + s + init.reset
                        elif s in {':'}:
                            self.newString += fg.rbg(255, 255, 153) + s + init.reset
                        elif s in {'.'}:
                            self.newString += fg.rbg(0, 102, 204) + s + init.reset
                        elif s in {'$'}:
                            self.newString += fg.rbg(255, 204, 0) + s + init.reset
                        elif s in {'#'}:
                            self.newString += fg.rbg(153, 153, 255) + s + init.reset
                            if self.string[ 0 ] not in [ "'", '"']: self.active = True
                            else: self.active = False
                        elif s in {'@'}:
                            self.newString += fg.rbg(255, 255, 255) + s + init.reset
                        elif s in {"'", '"'}:
                            self.newString += fg.rbg(255, 153, 204) + s + init.reset
                            self.k.append(s)
                            self.count += 1
                        else:  self.newString += self.color + s + init.reset
                    else: self.newString += fg.rbg(153, 153, 255) + s + init.reset
                else:
                    self.newString += fg.rbg(255, 153, 204) + s + init.reset
                    if self.k[0] == s:
                        self.count = 0
                        self.k = []
                    else: pass

        return self.newString

    def final(self, n:int=0):
        self.newS       = ''
        self.ss         = ''
        self.active     = False

        for i, s in enumerate( self.string) :
            if s not in [ ' ' ]:
                if s in self.analyse.UPPER_CASE()+self.analyse.LOWER_CASE()+[str(x) for x in range(10)]:
                    self.ss += s
                    if i < len( self.string)-1: pass
                    else:
                        if self.ss: self.newS   += words(self.ss, self.color).keywords()
                        else: pass
                else:
                    if s in [ '#' ]:
                        self.ss += s
                        if i < len(self.string) - 1:  pass
                        else:
                            if self.ss:  self.newS += words(self.ss, self.color).keywords()
                            else:  pass
                    elif s in ['"', "'"]:
                        self.ss += s
                        if i < len(self.string) - 1:  pass
                        else:
                            if self.ss:  self.newS += words(self.ss, self.color).keywords()
                            else:  pass
                    else:
                        if self.ss:
                            self.newS   += words(self.ss, self.color).keywords()
                            self.newS   += words(s, self.color).keywords()
                            self.ss     = ''
                        else :
                            self.newS   += words(s, self.color).keywords()
                            self.ss     = ''
            else:
                if self.ss :
                    if '#' in self.ss: self.ss += ' '
                    else:
                        self.newS   += words(self.ss, self.color).keywords()
                        self.newS   += ' '
                        self.ss     = ''
                else:
                    self.newS   += ' '
                    self.ss      = ''

        return self.newS

class chars:
    def ansi_remove_chars( self, name : str ):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub ('', name)

class timer:
    def timer():
        def updateClock():
            now = datetime.now().strftime('%H:%M:%S')
            sleep(1)
            return now
        
        while True: 
            stdout.write( move_cursor.LEFT( 1000 ) )
            stdout.write( updateClock() )
            stdout.flush()

    #updateClock()