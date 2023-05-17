import re
import imp, sys, os

if (sys.platform == "win32"): pass 
else: import termios, tty 

def cursor():
    # using to get the right cursor position on the screen  at each time (x, y)
    if os.name == "nt": return cursorWin()
    else: return cursorLinux()

def cursorMax():
    if os.name == "nt": return get_win_ter()
    else: return get_linux_ter()

def cursorWin():
    import msvcrt
    imp.reload(sys)
    try:
        sys.stdout.write("\x1b[6n")
        sys.stdout.flush()
        buffer = bytes()
        while msvcrt.kbhit():
            buffer += msvcrt.getch()
        hex_loc = buffer.decode()
        res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R", hex_loc)
    except UnicodeDecodeError: res = None
    except UnicodeWarning : res = None
    
    if (res): return ( int(res.group("x")),  int(res.group("y")) )
    else: return (-1, -1)
    
def cursorLinux():
    OldStdinMode = termios.tcgetattr(sys.stdin)
    _ = termios.tcgetattr(sys.stdin)
    _[3] = _[3] & ~(termios.ECHO | termios.ICANON)
    termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, _)

    try:
        _ = ""
        sys.stdout.write("\x1b[6n")
        sys.stdout.flush()
        
        while not (_ := _+sys.stdin.read(1)).endswith('R'): True
        res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R",_)
    finally: termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, OldStdinMode)
        
    if (res): return ( int(res.group("x")) , int( res.group("y")) ) 
    else: return (-1, -1)
    
def get_win_ter():
    # using to get the size of the screen at each time
    
    from ctypes import windll, create_string_buffer
    
    h = windll.kernel32.GetStdHandle(-12)
    csbi = create_string_buffer(22)
    res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
    if not res: return 80, 25

    import struct
    (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack("11h", csbi.raw)
    width = right-left+1
    height=bottom-top+1

    return ( int(width), int(height) )

def get_linux_ter():
    width = os.popen('tput cols', 'r').readline()
    height= os.popen('tput lines', 'r').readline()
 	
    return ( int(width), int(height) )