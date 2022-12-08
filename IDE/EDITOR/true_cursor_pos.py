import sys, re
if (sys.platform == "win32"):
	import ctypes
	from ctypes import wintype
else:
	import termios 
	
def cursor():
	OldStdinMode = termios.tcgetattr(sys.stdin)
	_ = termios.tcgetattr(sys.stdin)
	_[3] = _[3] & ~(termios.ECHO | termios.ICANON)
	termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, _)
	
	try:
		_ = ""
		sys.stdout.write("\x1b[6n")
		sys.stdout.flush()
		
		while not (_ := _+sys.stdin.read(1)).endswith('R'):
			True
		res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R",_)
	finally:
		termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, OldStdinMode)
		
	if (res):
		return (res.group("x"), res.group("y"))
	else: return (-1, -1)

