import sys, re, termios

def CursorPos():
	text=""
	pos = u"\u001b[6n"
	#sys.stdout.write(pos)
	#sys.stdout.flush()
	#text =  sys.stdin.read(1).endswith("R")
	res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R", 'hello'+pos)
        
	if res:	
		return (res.group("x"), res.group("y"))
	else: return (-1 -1)
