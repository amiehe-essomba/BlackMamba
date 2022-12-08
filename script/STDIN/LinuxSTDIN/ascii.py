def ascii(char :str ):
	#print(char)
	if   char == '<=' : return chr(8804)
	elif char == '>=' : return chr(8805)
	elif char == '/'  : return chr(247)
	elif char == '!=' : return chr(8800)
	elif char == '->' : return chr(8594)
	elif char == '||' : return chr(9553)
	elif char == '==' : return chr(9552)*2
	else: return char 
 
	#elif char == '*'  : return chr(10006)
	

def math_ensemble(char: str):
	if   char == 'n' : return chr(8469)
	elif char == 'z' : return chr(8484) 
	elif char == 'r' : return chr(8477)
	elif char == 'p' : return chr(8473)
	elif char == 'q' : return chr(8474)
	elif char == 'h' : return chr(8461)
	
def parenthesis( char : str = '1'):
	if   char == '1' : return [chr(i) for i in [9115, 9116, 9117, 9118, 9119, 9120]]
	elif char == '2' : return [chr(i) for i in [9121, 9122, 9123, 9124, 9125, 9126]]
	elif char == '3' : return [chr(i) for i in [9127, 9128, 9129, 9131, 9132, 9133]]
	
def dot(char : str ='h'):
	if char == 'h' : return chr(8230)


def frame(n:int):
    up_l, up_r = chr(9555), chr(9559)
    down_l, down_r = chr(9562), chr(9565)
    med1, med2, med3 = chr(9574), chr(9577), chr(9580)
    ver, hor = chr(9553), chr(9552)
    
    f = {'ul':up_l, 'ur':up_r, 'dl':down_l, 'dr':down_r, 'm1':med1,'m2':med2, 'm3':med3, 'v':ver, 'h':hor}
    
    up_l
    return f