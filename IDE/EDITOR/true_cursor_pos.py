import sys, msvcrt, re


def cursor():
    sys.stdout.write("\x1b[6n")
    sys.stdout.flush()
    buffer = bytes()
    while msvcrt.kbhit():
        buffer += msvcrt.getch()
    hex_loc = buffer.decode()
    res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R", hex_loc)
    
    if (res):
        return res.group("x"), res.group("y")
    else: return (-1, -1)
    
    