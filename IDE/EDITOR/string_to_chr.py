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
        number =  [ord(s), None]
    else:
        s = s[1].decode("utf-8")
        if   s == "H" : number = [27, 65]
        elif s == "P" : number = [27, 66]
        elif s == "K" : number = [27, 68]
        elif s == "M" : number = [27, 67]
    
    return number
     
"""       
if __name__ == "__main__":
    s= decoding_string()
    if len(s) == 1:
        s = s[0].decode("utf-8")
        number = ord(s)
    else:
        s = s[1].decode("utf-8")
        if   s == "H" : number = {27, 65}
        elif s == "P" : number = {27, 66}
        elif s == "K" : number = {27, 68}
        elif s == "M" : number = {27, 67}
            
    print(number)
"""