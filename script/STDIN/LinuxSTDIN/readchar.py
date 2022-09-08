import termios, sys, tty

def readchar():
    fd              = sys.stdin.fileno()
    old_settings    = termios.tcgetattr( fd )
    try:
        tty.setraw(sys.stdin)
        ch = ord( sys.stdin.read(1) )
    finally: termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch