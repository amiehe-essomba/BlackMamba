import sys 
from script.STDIN.LinuxSTDIN    import bm_configure                 as bm


def write(terminal_name='pegasus', string = "", decorator = "", color = "", reset = '', show = False, locked=False, n=0):
    if terminal_name == 'orion':
        # key word activation
        newString = decorator + bm.string().syntax_highlight( name=bm.words(string=string, color= color).final(locked=locked, n=0) )
        if show is False: sys.stdout.write( newString ) 
        else : print(newString)
    else:
        # any activation keyword
        newString = decorator +  color+ string + reset
        if show is False: sys.stdout.write(newString)
        else: print(newString)

def buildingString(Data : dict, a : int, b : int, drop_str : str, typ : str= "input"):
    beta = len( drop_str )
    if typ == 'input':
        Data['input']  = Data['input'][ : a] + drop_str +  Data['input'][b : ]
        Data['index'] += beta-1
        for k in range(beta-1):
            Data['get'].append(1)
    else:
        Data['string'] = Data['string'][ : a] + drop_str +  Data['string'][b : ]
        Data['I_S']   += beta-1
       
def re_write(terminal : str, indicator: int, Data : dict,  color : str ="", x : int = 0, y: int=0):
    if indicator not in {65, 66}:
        # moving cursor left 
        if indicator != 14:
            sys.stdout.write( bm.move_cursor.UP( pos= 1) + 
            bm.move_cursor.LEFT( pos = 1000 ) )
        else: sys.stdout.write( bm.move_cursor.LEFT( pos = 1000 ) )
        # erasing entire line 
        sys.stdout.write( bm.clear.line( pos = 2 ) )
        # writing string 
        write(terminal, Data['input'], Data['main_input'], color, bm.init.reset)
        # move cusror on left egain
    else: pass

def updating_callbacks(data1, data2):
    index = 0
    try:
        if data1['string_tabular']:
            data2['string_tabular']     = data1['string_tabular']   + data2['string_tabular']
            data2['tabular']            = data1['tabular']          + data2['tabular'] 
            data2['liste']              = data1['liste']            + data2['liste'] 
            data2['string_tab']         = data1['string_tab']       + data2['string_tab'] 
            data2['memory']             = data1['memory']           + data2['memory'] 
            data2['x_y']                = data1['x_y']              + data2['x_y']
            index = len(data1['tabular'] )
        else: pass
    except KeyError: pass 
    
    return data2, index