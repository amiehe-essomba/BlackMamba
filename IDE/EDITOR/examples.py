
from script.STDIN.LinuxSTDIN        import bm_configure as bm
from IDE.EDITOR                     import pull_editor as pe

def a(string: str):
    List, max_, L = None, 0, []
    if   string == 'add':
        List = ["# Only used for lists", "[].add( True )", "name = [].add( 'Hello Wold')"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()
        max_ = max(L)
    elif string == "anonymous":
        List = ["# Only used for creating functions", 
                "def iris( anonymous ) -> integer",
                "    Parity = False", 
                "    if (anonymous[0] % 2 == 0) and (anonymous[0] != 0):",
                "        if anonymous[0] / anonymous[0] == 0:",
                "            Parity = True",
                "        else:",
                "            pass",
                "        end:",
                "    end:",    
                "    return anonymous[0] * 5.0", 
                "end:",
                " ",
                "# running iris function",
                "bool_value = iris( 1, 5, 5, 7) ",
                "# anonymous arguments stored values in a list",
                "# in iris function : anonymous[0] = 1, anonymous[1] = 5, ..."
                ]
        for i in range(len(List)):
            L.append(len(List[i]))
            if i in [8, 9]:
                List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final(n=0)
            else: List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final(n=1)
        max_ = max(L)
    else: pass
    
    return List, max_+4, L 

def b( string :str):
    List, max_, L = None, None, []
    if   string == 'begin':
        List = ["# Only used to create comment lines", "beging:", 
                "    Hello here, my name is Black Mamba", 
                "    How can i help you?", 
                "save as cmt:", 
                "end:"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()
        max_ = max(L)
    else: pass
    return List, max_+4, L

def c(string: str): 
    List, max_, L = None, None, []
    if   string == 'capitalize':
        List = ["# Only used for strings", "'Hello World !'.capitalize()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()
        max_ = max(L)
    elif   string == 'clear':
        List = ["# Only used for lists, tuples && dictionaries", "[1,2,2].clear()", "('irene', 'iris').clear()", "'{'name : 5'}'.clear()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()
        max_ = max(L)
    elif   string == 'copy':
        List = ["# Only used for lists && dictionaries", "name = [1,2,2].copy()",  "name = {color : 'green'}.copy()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()
        max_ = max(L)
    elif   string == 'choice':
        List = ["# Only used for lists", "[1,2,2].choice()",  "name = [].random(10).choice()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()
        max_ = max(L)
    elif   string == 'count':
        List = ["# Only used for lists, tuples && strings", "[].random(10).count()",  "'Hello Evryone !'.count('e')" ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()
        max_ = max(L)
    elif   string == 'conj':
        List = ["# Only used for complex numbers",  "name = (2i+3)", "name.conj()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()
        max_ = max(L)
    elif string == "class":
        List = ["# Only used for creating classes", 
                "class run:",
                "    def initialize() -> none",
                "        self.ncol = 10",
                "        self.List = [].random(100)",
                "    end:",
                "    def array( axis : int bool = 0) -> ndarray:",
                "        return List.to_array( ncol ).sum( axis = axis)",
                "    end:",
                "end:",
                " ",
                "# running run class",
                "bool_value = run().array( axis = 1)"
                ]
        for i in range(len(List)):
            L.append(len(List[i]))
            if i in [9]:
                List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final(n=1)
            else: List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final(n=1)
        max_ = max(L)
    else: pass
    return List, max_+4, L

def d( string :str):
    List, max_, L = None, None, []
    if string == "def":
        List = ["# Only used for creating functions && attributes for classes", 
                "def Floor( master : float int bool = 1.0 ) -> integer",
                "    if ? master == ? 1:",
                "        return master",
                "    elif type(master) == type(True):",
                "        return integer(master)",
                "    else:",
                "        master = string(master).split('.')[0]",
                "        return integer(master)",
                "    end:",
                "end:",
                " ",
                "# running Floor function",
                "bool_value = iris(master = 10.2255) ",
                "bool_value = 10",
                ]
        for i in range(len(List)):
            L.append(len(List[i]))
            if i in [9]:
                List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final(n=0)
            else: List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final(n=1)
        max_ = max(L)
    else: pass
    return List, max_+4, L

def e(string: str): 
    List, max_, L = None, None, []
    if   string == 'enumerate':
        List = ["# Only used for strings and lists", "'Hello World !'.enumerate()", "[1, 2, 3, 4].enumerate()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()
        max_ = max(L)
    elif   string == 'endwith':
        List = ["# Only used for strings", "'Hello my name is Black Mamba'.endwith('Mamba')"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()
        max_ = max(L)
    elif   string == 'empty':
        List = ["# Only used for lists, dictionaries, tuple and strings", "name = [1,2,2].empty()",  "name = {}.empty()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final()
        max_ = max(L)
    else: pass 
    return List, max_+4, L

class code_example:
    def __init__(self, char : str, string : str ):
        self.char       = char
        self.string     = string 
    def code(self):
        self.names  = pe.list_of_keys( self.char , {}).list()
        if self.char == 'a':
            self.List, self.max, self.l = a( self.string )
        elif self.char == 'b':
            self.List, self.max, self.l = b( self.string )
        elif self.char == 'c':
            self.List, self.max, self.l = c( self.string )
        elif self.char == 'd':
            self.List, self.max, self.l = d( self.string )
        elif self.char == 'e':
            self.List, self.max, self.l = e( self.string )
            
        return self.List, self.max, self.l
            
        
        
    
    