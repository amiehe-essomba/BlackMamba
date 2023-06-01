def case():
    lower_case = "abcdefghijklmnopqrstuvwxyz_"
    upper_case = lower_case.upper()
    
    return lower_case+upper_case

def string(string : str = "", idd : int = 0):
    str_ = ""
   
    try:
        # checking if string exists
        if string: 
            # checking if the char idd of string is contained in 
            # the acceptable chars 
            if string[idd] in case(): 
                # initialization
                _id_        = idd 
                is_break    = False
                # building the string situated on the left where the cursor position
                while _id_ > 0:
                    if string[_id_] in case(): 
                        _id_ -= 1 
                    else: 
                        is_break = True
                        break
                    
                # checking the second condition 
                # if the cursor is not at the end of the string we can build de right string
                if len(string)-1 == idd: 
                    if is_break is True:str_, a, b = string[_id_+1: idd+1], _id_+1, idd+1  
                    else: str_, a, b = string[_id_ : idd+1], _id_, idd+1
                else:
                    # left cursor string 
                    if is_break is True: str_l, a, b = string[_id_+1: idd+1] , _id_+1, idd+1 
                    else: str_l, a, b = string[_id_ : idd+1], _id_, idd+1
                    # building the right cursor string 
                    _id_ = idd 
                    while _id_ < len(string):
                        _id_ += 1
                        if string[_id_] in case(): pass 
                        else: break
                    # right cusror string 
                    str_r   = string[idd+1 : _id_]
                    # total string 
                    str_, b    = str_l+str_r, _id_
                return (len(str_), str_, a, b)
            else: return (0, "", None, None)
        else: return (0, "", None, None)
    except IndexError: return (0, "", None, None)