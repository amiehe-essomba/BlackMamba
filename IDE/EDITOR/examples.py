
from script.STDIN.LinuxSTDIN        import bm_configure as bm
from IDE.EDITOR                     import pull_editor as pe

def a(string: str):
    List, max_, L = None, 0, []
    color = bm.init.bold + bm.bg.rgb(10, 10, 10) +  bm.fg.rbg(255, 255, 255)
    if   string == 'add':
        List = ["# Only used for lists", "[].add( True )", "name = [].add( 'Hello World')"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="add".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
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
                List[i] = bm.words(string=List[i], color=color).final(n=0)
            else: List[i] = bm.words(string=List[i], color=color).final(n=1)
        max_ = max(L)
        List = [ bm.words(string="anonymous".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    else: 
        L = [len(string), 10]
        max_ = max(L)
        L[0] = max_
        s =  bm.words(string=f"{string}".center(max_), color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final(n=0)
        List = [s, '          ']
    
    return List, max_+4, L 

def b( string :str):
    List, max_, L = None, None, []
    color = bm.init.bold + bm.bg.rgb(10, 10, 10) +  bm.fg.rbg(255, 255, 255)
    if   string == 'begin':
        List = ["# Only used to create comment lines", "beging:", 
                "    Hello here, my name is Black Mamba", 
                "    How can i help you?", 
                "save as cmt:", 
                "end:"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="begin".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    else: 
        L = [len(string), 10]
        max_ = max(L)
        L[0] = max_
        s =  bm.words(string=f"{string}".center(max_), color=color).final(n=0)
        List = [s, '          ']
        
    return List, max_+4, L

def c(string: str): 
    List, max_, L = None, None, []
    color = bm.init.bold + bm.bg.rgb(10, 10, 10) +  bm.fg.rbg(255, 255, 255)

    if     string == 'capitalize':
        List = ["# Only used for strings", "'Hello World !'.capitalize()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="capitilize".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'clear':
        List = ["# Only used for lists, tuples && dictionaries", "[1,2,2].clear()", "('irene', 'iris').clear()", "'{'name : 5'}'.clear()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="clear".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'copy':
        List = ["# Only used for lists && dictionaries", "name = [1,2,2].copy()",  "name = {color : 'green'}.copy()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="copy".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'choice':
        List = ["# Only used for lists", "[1,2,2].choice()",  "name = [].random(10).choice()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="choice".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'count':
        List = ["# Only used for lists, tuples && strings", "[].random(10).count()",  "'Hello Evryone !'.count('e')" ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="count".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'conj':
        List = ["# Only used for complex numbers",  "name = (2j+3)", "name.conj()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=c).final()
        max_ = max(L)
        List = [ bm.words(string="conj".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'complex':
        List = ["# Converting floats, booleans and strings to aa complex", 
            "complex('1.2'+'3.3')",
            "complex(1.358)",
            "complex(True)"
            ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="complex".center(max_), color=color).final(n=0)]+List
        L.insert(0, max_)
    elif   string == "class":
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
                List[i] = bm.words(string=List[i], color=color).final(n=1)
            else: List[i] = bm.words(string=List[i], color=color).final(n=1)
        max_ = max(L)
        List = [ bm.words(string="class".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    else: 
        L = [len(string), 10]
        max_ = max(L)
        L[0] = max_
        s =  bm.words(string=f"{string}".center(max_), color=bm.init.bold+bm.fg.rbg(255, 255, 255)).final(n=0)
        List = [s, '          ']
        
    return List, max_+4, L

def d( string :str):
    List, max_, L = None, None, []
    color = bm.init.bold + bm.bg.rgb(10, 10, 10) +  bm.fg.rbg(255, 255, 255)
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
                List[i] = bm.words(string=List[i], color=color).final(n=0)
            else: List[i] = bm.words(string=List[i], color=color).final(n=1)
        max_ = max(L)
        List = [ bm.words(string="def".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'dictionary':
        List = ["# Only used for dictionary",
                "iris = {",
                "    color : 'green',",
                "    size  : 1.05,",
                "    width : 0.3",
                "    }",
                "iris $ color ",
                "iris $ size = 2.05",
                "# creating a dictionary using dictionary keyword",
                "names = ['iris', 'setosa', 'versicolor', 'virginica'] ",
                "colors= ['green', 'lime', 'blue', 'red']",
                "dic   = dictionary(names, colors)",
                "dic $ colors",
                "dic.get('items')",
                "dic.get('keys')",
                "dic.get('values')"
                ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string='dictionary'.center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    else: 
        L = [len(string), 10]
        max_ = max(L)
        L[0] = max_
        s =  bm.words(string=f"{string}".center(max_), color=color).final(n=0)
        List = [s, '          ']
        
    return List, max_+4, L

def e(string: str): 
    List, max_, L = None, None, []
    color = bm.init.bold + bm.bg.rgb(10, 10, 10) +  bm.fg.rbg(255, 255, 255)
    if   string == 'enumerate':
        List = ["# Only used for strings and lists", "'Hello World !'.enumerate()", "[1, 2, 3, 4].enumerate()"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="enumerate".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'endwith':
        List = ["# Only used for strings", "'Hello my name is Black Mamba'.endwith('Mamba')"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="endith".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'empty':
        List = ["# Only used for lists, dictionaries, tuple and strings", "name = [1,2,2].empty()",  "name = {}.empty()", "' '.empy()'"]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="empty".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    else: 
        L = [len(string), 10]
        max_ = max(L)
        L[0] = max_
        s =  bm.words(string=f"{string}".center(max_), color=color).final(n=0)
        List = [s, '          ']
        
    return List, max_+4, L

def f( string :str):
    List, max_, L = None, None, []
    color = bm.init.bold + bm.bg.rgb(10, 10, 10) +  bm.fg.rbg(255, 255, 255)
    if string == "func":
        List = ["# Only used for creating functions && attributes for classes", 
                "Floor func( master : float int bool = 1.0 ) -> integer",
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
                List[i] = bm.words(string=List[i], color=color).final(n=0)
            else: List[i] = bm.words(string=List[i], color=color).final(n=1)
        max_ = max(L)
        List = [ bm.words(string="func".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif string == "for":
        List = ["# Only used for creating loops for ",
            "index = 0", 
            "for i in range(1, 10):",
            "    index += 1",
            "end:",
            " ",
            "for i, name in [].random(10).enumerate(): ",
            "    index *= 1",
            "end:",
            " ",
            "for (id in [1, 5, 9, 8]) && (i % 2 == 0):",
            "    index -= 1",
            "end:",
            " ",
            "name = [] ",
            "for (id in [1, 5, 9, 8]) and (i % 2 == 1):",
            "    name.add( i )",
            "end:",
            ]
        for i in range(len(List)):
            L.append(len(List[i]))
            if i in [900]:
                List[i] = bm.words(string=List[i], color=color).final(n=0)
            else: List[i] = bm.words(string=List[i], color=color).final(n=1)
        max_ = max(L)
        List = [ bm.words(string="loop for".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif string == "from":
        List = ["# Only used for loading external mudules && functions", 
            "from module matrix load ndarray",
            "array_nd = ndarray([].random(100), ncol=10, nrow=10).array(axis=0)",
            " ",
            "from module matrix load ndarray as nd",
            "array_nd = nd([].random(9), ncol=3, nrow=3).sum( reverse=True, axis=None)",
            " ",
            "from module matrix load *",
            "ndarray([1, 2, 3, 7], ncol = 2, nrow = 2 ).std()",
            " ",
            "from module |external_file|my_file|flours| load  color",
            "color.green"
            ]
        for i in range(len(List)):
            L.append(len(List[i]))
            if i in [900]:
                List[i] = bm.words(string=List[i], color=color).final(n=0)
            else: List[i] = bm.words(string=List[i], color=color).final(n=1)
        max_ = max(L)
        List = [ bm.words(string="from".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif string =="float":
        List = ["# Only used for creating float numbers ", 
                "float(1), float(True), float('2.0')"
                ]
        for i in range(len(List)):
            L.append(len(List[i]))
            if i in [900]:
                List[i] = bm.words(string=List[i], color=color).final(n=0)
            else: List[i] = bm.words(string=List[i], color=color).final(n=1)
        max_ = max(L)
        List = [ bm.words(string="float".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    else: 
        L = [len(string), 10]
        max_ = max(L)
        L[0] = max_
        s =  bm.words(string=f"{string}".center(max_), color=color).final(n=0)
        List = [s, '          ']
    
    return List, max_+4, L

def g(string: str):
    List, max_, L = None, 0, []
    color = bm.init.bold + bm.bg.rgb(10, 10, 10) +  bm.fg.rbg(255, 255, 255)
    if   string == 'global':
        List = ["# Only used to make variables global", 
                "global color, names",
                "color, name = 'green', 'versicolor'",
                " ",
                "# using global variables in functions",
                "setosa = func() -> string:",
                "    return name[0]",
                "end:"
                ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final(n=1)
        max_ = max(L)
        List = [ bm.words(string="global".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'get':
        List = ["# Only used to get items, keys, values from disctionary", 
            "name = {}",
            "name $ array = (1, 2, 7, 9).sored()",
            "name.get('keys'), name.get('items'), name.get('values')"
            ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="get".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    else: 
        L = [len(string), 10]
        max_ = max(L)
        L[0] = max_
        s =  bm.words(string=f"{string}".center(max_), color=color).final(n=0)
        List = [s, '          ']
    
    return List, max_+4, L

def i(string: str):
    List, max_, L = None, 0, []
    color = bm.init.bold + bm.bg.rgb(10, 10, 10) +  bm.fg.rbg(255, 255, 255)
    if     string == 'in':
        List = [" ", 
                "'e' in 'house' ",
                "1 in [1, 5, 6, 7]",
                " ",
                "for i in [1, 9, 7, 2]:",
                "    print * i",
                "end:"
                ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final(n=1)
        max_ = max(L)
        List = [ bm.words(string="in".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'img':
        List = ["# Only used for complex numbers", 
            "name = 2j+4",
            "print * name.img()",
            ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="img".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'if':
        List = ["# Only used for controling structure flow", 
            "name = 1",
            "if name % 2 == 0",
            "    print * True",
            "else:",
            "    print * False",
            "end:"
            ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="if".center(max_), color=color).final(n=0)]+List
        L.insert(0, max_)
    elif   string == 'index':
        List = ["# Only used for lists, tuples and strings", 
            "'house'.index('h')",
            "['r', 'a', 'b', 'c'].index('a')",
            "(1, 3, 5, 9).index(9)"
            ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="index".center(max_), color=color).final(n=0)]+List
        L.insert(0, max_)
    elif   string == 'insert':
        List = ["# Only used for lists and strings", 
            "'ouse'.insert(0, 'H')",
            "['a', 'a', 'c', 'd'].i(1, 'b')"
            ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="insert".center(max_), color=color).final(n=0)]+List
        L.insert(0, max_)
    elif   string == 'initialize':
        List = ["# Only used for creating a constructor method", 
            "class House:",
            "    def initialize():",
            "        self.size = 1.0",
            "    end:",
            "end:",
            " ",
            "class Cost( House ):",
            "    def initialize( prices : string = '10000.0$')",
            "        self.prices = prices",
            "        self.size = size",
            "    end:",
            "end:"
            ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final(n=1)
        max_ = max(L)
        List = [ bm.words(string="initialize".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'init':
        List = ["# Only used for lists, strings, tuples and dictionaries", 
            "[].init(), " ".init(), (1, 5).init(), {name : 'irene'}.init()"
            ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="init".center(max_), color=color).final(n=0)]+List
        L.insert(0, max_) 
    elif   string == 'integer':
        List = ["# Converting floats, booleans and strings to an integer", 
            "integer('1.2'+'3.3')",
            "integer(1.358)",
            "integer(True)"
            ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="integer".center(max_), color=color).final(n=0)]+List
        L.insert(0, max_)
    else: 
        L = [len(string), 10]
        max_ = max(L)
        L[0] = max_
        s =  bm.words(string=f"{string}".center(max_), color=color).final(n=0)
        List = [s, '          ']
    
    return List, max_+4, L

def j(string: str):
    List, max_, L = None, 0, []
    color = bm.init.bold + bm.bg.rgb(10, 10, 10) +  bm.fg.rbg(255, 255, 255)
    if   string == 'join':
        List = ["# Only used for strings", "''.join('H')", 
                " ",
                "'--'.join( ['Python', 'BMamba', 'R', 'C', 'Ruby'] )",
                "'**'.join( master = ('Python', 'BMamba', 'Ruby') )",
                "'_'.join( {Python : True, BMamba : True, Ruby : None] )"
                ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="join".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    else: 
        L = [len(string), 10]
        max_ = max(L)
        L[0] = max_
        s =  bm.words(string=f"{string}".center(max_), color=color).final(n=0)
        List = [s, '          ']
    
    return List, max_+4, L 

def l(string: str):
    List, max_, L = None, 0, []
    color = bm.init.bold + bm.bg.rgb(10, 10, 10) +  bm.fg.rbg(255, 255, 255)
    if     string == 'lambda':
        List = ["# Only used for creating anonymous functions",
                " ", 
                "sum    = lambda a b : a+b -> integer # which means that the output is an integer type",
                "sum    = lambda array max : array[array .gt. max] -> list",
                "# loading function creating with lambda keyword",
                "from module prompt load prompt",
                "prompt( sum(a=4, b=-1) )",
                "print * array( [].random(100) )"
                ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="lambda".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    elif   string == 'lower':
        List = ["# Only used for strings",
                " ", 
                "'HELLO WORLD !'.lower()"
                ]
        for i in range(len(List)):
            L.append(len(List[i]))
            List[i] = bm.words(string=List[i], color=color).final()
        max_ = max(L)
        List = [ bm.words(string="lower".center(max_), color=color).final(n=1)]+List
        L.insert(0, max_)
    else: 
        L = [len(string), 10]
        max_ = max(L)
        L[0] = max_
        s =  bm.words(string=f"{string}".center(max_), color=color).final(n=0)
        List = [s, '          ']
    
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
        elif self.char == 'f':
            self.List, self.max, self.l = f( self.string )
        elif self.char == 'g':
            self.List, self.max, self.l = g( self.string )
        elif self.char == 'i':
            self.List, self.max, self.l = i( self.string )
        elif self.char == 'j':
            self.List, self.max, self.l = j( self.string )
        elif self.char == 'l':
            self.List, self.max, self.l = l( self.string )
        else: self.List, self.max, self.l = ['          '], 10, [10]
        return self.List, self.max, self.l
            
        
        
    
    