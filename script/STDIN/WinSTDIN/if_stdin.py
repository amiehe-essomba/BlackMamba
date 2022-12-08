from script                     import control_string

class STDIN:
	def __init__(self, data_base:dict,line:int):
		self.data_base          = data_base
		self.line               = line
		self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)	
	
	def ENCODING( self, string : str):
		n = 0 # using for counting 
		
		for s in string:
			if s == '\t':  n +=1 
			else: break
		return n
		
	def STRUCT(self, 
		tabulation  : int    = 1,            # tabulation 
		LIST        : list   = [],           # list of values 
		_class_     : bool   = False
		):
		
		self.newList = []
		
		if LIST:
			for i, _str_ in enumerate(LIST):
				self.n = STDIN( self.data_base, self.line).ENCODING( _str_ ) 
				              
				if self.n >= tabulation : self.newList.append( _str_ ) 
				else: break
		else: pass 
		
		return self.newList
