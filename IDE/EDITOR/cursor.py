import sys 
from script.STDIN.LinuxSTDIN  import bm_configure as bm 

class move:
	def __init__(self):
		pass 
	def move( self, text: str, n : int = 1):
		sys.stdout.write(bm.save.save)
		for i in range(n):
			sys.stdout.write(text+'\n')
		sys.stdout.write(bm.save.restore)
		sys.stdout.flush()