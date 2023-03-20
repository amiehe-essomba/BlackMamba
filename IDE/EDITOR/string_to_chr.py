def string( main : str ):
    if   main == "enter":                    return 10
    elif main == "space":                    return 32
    elif main == "backspace":                return 8
    elif main == "tab":                      return 8
    elif main in ["bas", 'down']:            return 27
    elif main in ["up", 'haut']:             return 27
    elif main in ["left", 'gauche']:         return 27
    elif main in ["right", 'droite']:        return 27
    else:
        try: return ord( main ) 
        except TypeError : return None 
        
def decoding_string():
    import msvcrt 
    number = None
    s = []
    idd = 0
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            s.append(key)

            if s[0] == b'\x00':
                try: 
                    if s[1] : break
                except IndexError: pass
            else: break    
   
    return s

def convert( ):
    s = decoding_string()
    number = None 

    if len(s) == 1:
        s = s[0].decode("utf-8")
       
        try:
            number =  [ord(s), None]
        except TypeError: 
            if   s == "\x0e":
                number =  [14, None]
            elif s == "\x04":
                number =  [4,  None]
            elif s == "\x01":
                number =  [17, None]
            elif s == "\x0c":
                number =  [12, None]
            else:  
                number =  [None, None]
    else:
        s = s[1].decode("utf-8")
        if   s == "H" : number = [27, 65]
        elif s == "P" : number = [27, 66]
        elif s == "K" : number = [27, 68]
        elif s == "M" : number = [27, 67]
    
    return number
     