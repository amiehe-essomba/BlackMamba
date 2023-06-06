def case():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = lower_case.upper()
    
    return lower_case+upper_case+"_"

def base(c : str = "", reset : str  ="", key : str = ">>> ", active : bool = True):
    structure = {}
    ##############################################################################
    if active is True:
        # input initialized
        input                                   = f'{c}{chr(9654)*3} {reset}'
    else: input                                 = f'{c}{key}{reset}' 
    #size 
    size                                        = len(key)
    structure['size']                           = size
    structure['input']                          = ""
    structure['main_input']                     = input
    ##############################################################################
    # string used for the code,
    structure['string']                         = ""
    # string used to handling the output that is the must inmportant string
    structure['s']                              = ""
    # initialisation of index associated to the input
    structure['index']                          = 0
    # initialisation of index I associated to the string s value
    structure['I']                              = 0
     # index associated to the string string value
    structure['I_S']                            = 0
    # history of data associated to the string  input
    structure['liste']                          = [""]
    # history of data associated to the value returns by the function readchar
    structure['get']                            = []
    # initialisation of integer idd used to get the next of previous
    # values stored in the different histories of lists
    structure['idd']                            = 0
    # initialization of list associated to the string s
    structure['sub_liste']                      = []
    # the memory contains the history of get value
    structure['memory']                         = [[]]
    # initilization of last
    structure['last']                           = 0
    # initialisation of list associated to the index value
    structure['tabular']                        = [0]
     # initialisation of list associated to I value
    structure['sub_tabular']                    = []
    # initialisation of the list associated to last value
    structure['last_tabular']                   = []
    # storing cursor position
    structure['remove_tab']                     = []
    # storing cursor position
    structure['remove_tabular']                 = []
    # initialization of the list associated to string
    structure['string_tab']                     = [0]
    # initialization of associated to I_S
    structure['string_tabular']                 = [""]
    # drowp
    structure['str_drop_down']                  = ""
    # dropdown index 
    structure['drop']                           = 0
    # dropdown list fo storing
    structure['drop_list_str']                  = []
    # dropdown list of index 
    structure['drop_list_id']                   = []
    # storig identity and last str_drop_down 
    structure['drop_drop']                      = {'id':[], 'str': []}
    # index of drop_drop 
    structure['drop_idd']                       = 0
    # alphabetic char + underscore char
    structure['alpha']                          = case()
    # last cursor position
    structure['x_y']                            = [(0,0)]
    
    return structure
    
def indexation():
    indexation  = {
        0 : {
            'action' : 'FREE',  # [FREE, LOCKED]
            'status' : 'I',     # [I, D] 
            'do'     : 'ADDS',  # [ADD, INSERT, INDEX]
            'cursor' : 'NO',    # [NO, UP, DOWN, ENTER]
            'last'   : ''
            }
        }
    return indexation
      