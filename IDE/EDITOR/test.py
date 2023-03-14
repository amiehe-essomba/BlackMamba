import os

def get_win_ter():
    from ctypes import windll, create_string_buffer
    h = windll.kernel32.GetStdHandle(-12)
    csbi = create_string_buffer(22)
    res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
    if not res: return 80, 25

    import struct
    #print(struct.pack("hhhhhhhhhhh", 184, 17, 0, 0, 7, 0, 0, 183, 16, 184, 17))
    (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy)=struct.unpack("11h", csbi.raw)
    width = right-left+1
    height=bottom-top+1

    return width, height
	
def get_linux_ter():
	width = os.popen('tput cols', 'r').readline()
	height= os.popen('tput lines', 'r').readline()	
	return int(width), int(height)

#if os.name == 'posix' : print( get_linux_ter())
#else: print( get_win_ter())