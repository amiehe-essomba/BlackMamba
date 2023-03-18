def size(max_x, max_y, pos_x, pos_y):
    
    key_max_activation = False
    
    if   (int(max_y)-int(pos_y)) > 10 : key_max_activation = True
    else: key_max_activation = False
    
    if key_max_activation  is False: pass
    else:
        if (int(max_x)-int(pos_x)) > 10 : key_max_activation = True
        else: key_max_activation = False
        
    return key_max_activation