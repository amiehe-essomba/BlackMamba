import datetime
import re, os, sys
from   sys         import stdout, stdin
from   time        import sleep
from   datetime    import datetime

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
                'Black Mamba programming language -version- 1.0.0. MIT License',
                f'[ {sys} version ] type help( arg ) for more informations.',
                '>> ',
                'written by amiehe-essomba',
                'email: ibamieheessomba@unistra.fr',
                '\n',
                ''
                ]

        wait    = 0.005

        head().tip(block[ 0 ], 0, wait)
        head().tip(block[ 1 ], 1, wait)
        head().tip(block[ 2 ], 2, wait)
        head().tip(block[ 3 ], 3, wait)
        head().tip(block[ 4 ], 4, wait)
        head().tip(block[ 5 ], 5, wait)
        head().tip(block[ 6 ], 6, wait)

    
    def tip( self, text : str , n : int, wait : float ):
        string = ''
        for i, char in enumerate( text ):
            string += char 
            stdout.write(char )
            if i < len( text ) - 1:
                pass 
            else:
                if n in [1, 2]:
                    stdout.write( move_cursor.LEFT( 1000 ) )
                    print( '{}{}{}'.format( fg.red_L, text, init.reset) )
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

class remove_ansi_chars:
    def chars( self, name : str ):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub ('', name) 

class read:
    def readchar(self):
        fd  = sys.stdin.fileno()
        ch = ord( sys.stdin.read( 1 ) )
        return ch

class string:
    def __init__(self):
        pass
    def syntax_highlight( self, name : str ):
        self.stripped = name.rstrip()
        return self.stripped + bg.blue_L + " " * ( len( name ) - len( self.stripped ) ) + init.reset

class chars:
    def ansi_remove_chars( self, name : str ):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub ('', name)

class clean_print:
    def clean_print(self, string : str):
        sys.stdout.write(bm.clear.line(2))
        sys.stdout.write(bm.move_cursor.LEFT(1000))
        sys.stdout.write(bm.move_cursor.DOWN(1))
        print('{}\n'.format(string))

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