def String( string : str, index : int=0, char : list=[], key = 'left'):
    new_str = ""
    left, right = "", ""
    if string: 
        if string[index] in char:
            for s in string[ : index]:
                if s in char: left += s
                else: break 
            for s in string[ index : ]:
                if s in char: right += s
                else: break
            new_str = left+right		
        else: pass
    else: pass
	
    if new_str: return new_str, len(new_str)
    else: return new_str, 1