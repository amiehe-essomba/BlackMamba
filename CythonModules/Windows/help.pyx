from script.STDIN.LinuxSTDIN    import bm_configure as bm

cdef class HELP:
    cdef public:
        str argument
    def __init__(self, argument ):
        self.argument   = argument 
    
    
    cpdef HELP(self):
        cdef:
            list string, lists
            str ss, s, color, s0, s1, s2, s3, s4
            str d,d1, d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d0,d15,d16,d17, d18
      
        if self.argument in [ 'var_name', 'class_name', 'function_name']:
            s      = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            color  = bm.fg.rbg(255,255,255)
            if self.argument == 'var_name':
                string = ["name = 10",  "Name = True"]
                for ss in string:
                    s0 = s + " " + bm.words(string=ss, color=color).final()
                    print(f"{s0}")

                
               
                s1      = "| " + "The name of variables always start with an  |"
                s2      = "| " + "alphabetic character.                       |"
                print(chr(45) * len(s1))
                print(f"{s1}")
                print(f"{s2}")
                print(chr(45) * len(s1))

            elif self.argument == 'function_name':
                string = ["name():",  "Name():"]
                for ss in string:
                    s0 = s + " " + bm.fg.rbg(255,165,0)+"def "+bm.init.reset+ bm.words(string=ss, color=color).final()
                    print(f"{s0}")

        
                s1       = "| " + "The name of functions always start with an  |"
                s2       = "| " + "alphabetic character.                       |"
                print(chr(45) * len(s1))
                print(f"{s1}")
                print(f"{s2}")
                print(chr(45) * len(s1))
            
            elif self.argument == 'class_name':
                string = ["name:",  "Name:", "name( Name ):"]
                for ss in string:
                    s0 = s + " " + bm.fg.rbg(255,165,0)+"class "+bm.init.reset+ bm.words(string=ss, color=color).final()
                    print(f"{s0}")

                s1       = "| " + "The name of classes always start with an  |"
                s2       = "| " + "alphabetic character.                     |"
                print(chr(45) * len(s1))
                print(f"{s1}")
                print(f"{s2}")
                print(chr(45) * len(s1))
        elif self.argument == 'functions':
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " how can i do to create a function  |"
            s2 = s + ' ' + 'choosing the name of the function. Type help( {} ) for more details'.format(bm.words(string="'function_name'", color=bm.fg.rbg(255,255,255)).final())
            s3 = s + ' ' + 'using the keywords'+ bm.fg.rbg(255,165,0)+' def'+bm.init.reset+' or '+bm.fg.rbg(255,165,0)+'func'+bm.init.reset
            s4 = s + ' ' + 'defining the arguments and argument types. Type help( {} ) for more details'.format(bm.words(string="'arg_types'", color=bm.fg.rbg(255,255,255)).final())
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            print(s2)
            print(s3)
            print(s4)
            s1 = '| ' + " example 1  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            print(bm.words(string="def iris():", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="         .......    ", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="end :", color=bm.fg.rbg(255,255,255)).final(n=1))

            s1 = '| ' + " example 2  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))

            print(bm.words(string="iris = func():", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="         .......    ", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="end :", color=bm.fg.rbg(255,255,255)).final(n=1))

            s1 = '| ' + " example 3  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))

            print(bm.words(string="def iris( color : string):", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="         .......    ", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="end :", color=bm.fg.rbg(255,255,255)).final(n=1))

            s1 = '| ' + " example 4  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))

            print(bm.words(string="def iris( color : string, size :int/bool/float = 1.05 ):", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="         .......    ", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     < instruction >", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="end :", color=bm.fg.rbg(255,255,255)).final(n=1))
           
        elif self.argument == 'arg_types':
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " argument types  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            d1 = s + ' {}int      {}= {}integer type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d2 = s + ' {}float    {}= {}flaot type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d3 = s + ' {}cplx     {}= {}complex type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d4 = s + ' {}string   {}= {}string type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d5 = s + ' {}list     {}= {}list type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d6 = s + ' {}tuple    {}= {}tuple type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d7 = s + ' {}dict     {}= {}dictionary type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d8 = s + ' {}bool     {}= {}boolean type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d9 = s + ' {}none     {}= {}None type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d10= s + ' {}range    {}= {}range type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d11= s + ' {}ndarray  {}= {}matrix type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d12= s + ' {}any      {}= {}any type{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            

            lists = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]
            for d in lists:
                print(d)

            s1 = '| ' + " The default value is  |"
            s2 = '| ' + " The default value is {} |".format(bm.words(string="any", color=bm.fg.rbg(255,255,255)).final())
            print(chr(45) * (len(s1)+3))
            print(f'{s2}')
            print(chr(45) * (len(s1)+3))

        elif self.argument == 'arguments':
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " arguments  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            d1 = s + ' {}var_name           {}= {}name of a variable{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d2 = s + ' {}arg_types          {}= {}types of arguments{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d3 = s + ' {}function_name      {}= {}name of a function {}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d4 = s + ' {}class_name         {}= {}name of a class{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d5 = s + ' {}functions          {}= {}creating of a function{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d6 = s + ' {}dictionary         {}= {}creating a dictionary{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d7 = s + ' {}dict_functions     {}= {}dictionary functions{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d8 = s + ' {}list               {}= {}creating a list{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d9 = s + ' {}list_functions     {}= {}list functions{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d10= s + ' {}tuple              {}= {}creating a tuple{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d11= s + ' {}tuple_functions    {}= {}tuple functions{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d12= s + ' {}string             {}= {}creating a string{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d13= s + ' {}str_functions      {}= {}string functions{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d14= s + ' {}random             {}= {}random function{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d15= s + ' {}string_format      {}= {}random function{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)

            lists = [d1,d2,d3,d4,d5, d6,d7,d8,d9,d10,d11, d12,d13,d14, d15]
            for d in lists:
                print(d)

        elif self.argument == 'dictionary':
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " creating a dictionary  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            print(' ')
            d1 = s + ' ' + '{}using{} {}'.format(bm.fg.rbg(255,255,255), bm.init.reset, bm.words(string="{}", color=bm.fg.rbg(255,255,255)).final())
            print(d1)
            print(' ')
            print(bm.words(string="name = {", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     countries = ['US', 'UK', 'France', 'Cameroon'],", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     cities    = ['London', 'California', 'Yaounde']  ", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     }", color=bm.fg.rbg(255,255,255)).final())
            print(' ')
            d1 = s + ' ' + '{}using the character {}{}.'.format(bm.fg.rbg(255,255,255), bm.init.reset,bm.words(string="$", color=bm.fg.rbg(255,255,255)).final())
            print(d1)
            print(' ')
            print(bm.words(string="iris = {}", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="iris $ color = 'green' ", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="iris $ size  = 1.05 ", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="iris $ width = 0.5 ", color=bm.fg.rbg(255,255,255)).final())
            print(' ')
            d1 = s + ' ' + '{}using {} function.{}'.format(bm.fg.rbg(255,255,255), bm.words(string="dictionary()", color=bm.fg.rbg(255,255,255)).final(),bm.init.reset )
            print(d1)
            print(' ')
            print(bm.words(string="countries = ['US', 'UK', 'France', 'Cameroon']", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="cities    = ['London', 'California', 'Yaounde']", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="name      = dictionary(countries, cities)", color=bm.fg.rbg(255,255,255)).final())

        elif self.argument == 'dict_functions':
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " dictionary functions  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            d1 = '{}'.format(bm.words(string="{}.get( type = 'items' )", color=bm.fg.rbg(255,255,255)).final())
            d2 = '{}'.format(bm.words(string="{}.get( type = 'keys' )", color=bm.fg.rbg(255,255,255)).final())
            s1 = '{}'.format(bm.words(string="{}.get( type = 'values' )", color=bm.fg.rbg(255,255,255)).final())
            d3 = s + ' {}get           {}: {} , {}, {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, d2, s1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="{}.init()", color=bm.fg.rbg(255,255,255)).final())
            d4 = s + ' {}init          {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="{}.copy()", color=bm.fg.rbg(255,255,255)).final())
            d5 = s + ' {}copy          {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="{}.clear()", color=bm.fg.rbg(255,255,255)).final())
            d6 = s + ' {}clear         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="{}.remove( key = 'KeyName')", color=bm.fg.rbg(255,255,255)).final())
            d7 = s + ' {}remove        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="{}.empty()", color=bm.fg.rbg(255,255,255)).final())
            d8 = s + ' {}empty         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            

            lists = [d3, d7, d8, d6, d5, d4 ]
            for d in lists:
                print(d)
        
        elif self.argument == 'list':
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " creating a list  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            print(' ')
            d1 = s + ' ' + '{}using{} {}'.format(bm.fg.rbg(255,255,255), bm.init.reset, bm.words(string="[]", color=bm.fg.rbg(255,255,255)).final())
            print(d1)
            print(' ')
            print(bm.words(string="name = [", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     ['US', 'UK', 'France', 'Cameroon'], 0.5, False,", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     ['London', 'California', 'Yaounde'], True, None,", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     {color : 'green', size : 1.2}, 'Car', (1,2,3,4,5)", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     ]", color=bm.fg.rbg(255,255,255)).final())
            print(' ')
            
            d1 = s + ' ' + '{}using {} function.{}'.format(bm.fg.rbg(255,255,255), bm.words(string="list()", color=bm.fg.rbg(255,255,255)).final(),bm.init.reset )
            print(d1)
            print(' ')
            print(bm.words(string="countries = ('US', 'UK', 'France', 'Cameroon')", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="name      = list( countries )", color=bm.fg.rbg(255,255,255)).final())

        elif self.argument == 'tuple':
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " creating a tuple  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            print(' ')
            d1 = s + ' ' + '{}using{} {}'.format(bm.fg.rbg(255,255,255), bm.init.reset, bm.words(string="()", color=bm.fg.rbg(255,255,255)).final())
            print(d1)
            print(' ')
            print(bm.words(string="name = (", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="      0.5, False,", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="      True, None ", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="     )", color=bm.fg.rbg(255,255,255)).final())
            print(' ')
            
            d1 = s + ' ' + '{}using {} function.{}'.format(bm.fg.rbg(255,255,255), bm.words(string="tuple()", color=bm.fg.rbg(255,255,255)).final(),bm.init.reset )
            print(d1)
            print(' ')
            print(bm.words(string="countries = ['US', 'UK', 'France', 'Cameroon']", color=bm.fg.rbg(255,255,255)).final())
            print(bm.words(string="name      = tuple( countries )", color=bm.fg.rbg(255,255,255)).final())
            print(' ')
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " Remarks :  A tuple object cannot caintain  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            print(' ')
            d1 = s + ' ' + '{}'.format(bm.words(string="a dictionary()", color=bm.fg.rbg(255,255,255)).final(),bm.init.reset )
            d2 = s + ' ' + '{}'.format(bm.words(string="a list()", color=bm.fg.rbg(255,255,255)).final(),bm.init.reset )
            print(d2)
            print(d1)

        elif self.argument == 'list_functions':
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " list functions  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            d1 = '{}'.format(bm.words(string="[].insert( pos = 0, master = [1, 2, 5] )", color=bm.fg.rbg(255,255,255)).final())
            d0 = s + ' {}insert        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].add( master = 1 )", color=bm.fg.rbg(255,255,255)).final())
            d2 = s + ' {}add           {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].count( master = 'string' )", color=bm.fg.rbg(255,255,255)).final())
            d3 = s + ' {}count         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].round( master = 5 )", color=bm.fg.rbg(255,255,255)).final())
            d4 = s + ' {}round         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].index( master = 's' )", color=bm.fg.rbg(255,255,255)).final())
            d5 = s + ' {}index         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].remove( master = -1 )", color=bm.fg.rbg(255,255,255)).final())
            d6 = s + ' {}remove        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].random( numeric = 100 ), [].random(numeric = (max_step, max_num))", color=bm.fg.rbg(255,255,255)).final())
            d7 = s + ' {}random        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].rand( numeric = 100 )", color=bm.fg.rbg(255,255,255)).final())
            d8 = s + ' {}rand          {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].enumerate()", color=bm.fg.rbg(255,255,255)).final())
            d9 = s + ' {}enumerate     {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].sorted( reverse = True )", color=bm.fg.rbg(255,255,255)).final())
            d10= s + ' {}sorted        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].init()", color=bm.fg.rbg(255,255,255)).final())
            d11= s + ' {}init          {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].copy()", color=bm.fg.rbg(255,255,255)).final())
            d12= s + ' {}copy          {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].clear()", color=bm.fg.rbg(255,255,255)).final())
            d13= s + ' {}clear         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].empty()", color=bm.fg.rbg(255,255,255)).final())
            d14= s + ' {}empty         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].size()", color=bm.fg.rbg(255,255,255)).final())
            d15= s + ' {}size          {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="[].choice()", color=bm.fg.rbg(255,255,255)).final())
            d16= s + ' {}choice        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            
            lists = [d0,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16 ]
            for d in lists:
                print(d)

        elif self.argument == 'string_functions':
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " string functions  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            d1 = '{}'.format(bm.words(string="''.replace( oldStr = 'a', newStr = 'b')", color=bm.fg.rbg(255,255,255)).final())
            d0 = s + ' {}replace       {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.split( master = 'a' )", color=bm.fg.rbg(255,255,255)).final())
            d2 = s + ' {}split         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.count( master = 'a' )", color=bm.fg.rbg(255,255,255)).final())
            d3 = s + ' {}count         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.index( master = 'a' )", color=bm.fg.rbg(255,255,255)).final())
            d4 = s + ' {}index         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.endwith( master = 'a' )", color=bm.fg.rbg(255,255,255)).final())
            d5 = s + ' {}endwith       {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.startwith( master = 'a' )", color=bm.fg.rbg(255,255,255)).final())
            d6 = s + ' {}startwith     {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.join( master = ('a', 'b') )", color=bm.fg.rbg(255,255,255)).final())
            d7 = s + ' {}join          {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.format(master = {'1':1, '2':6})", color=bm.fg.rbg(255,255,255)).final())
            d17= s + ' {}format        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.lower()", color=bm.fg.rbg(255,255,255)).final())
            d8 = s + ' {}lower         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.upper( )", color=bm.fg.rbg(255,255,255)).final())
            d9 = s + ' {}upper         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.enumerate()", color=bm.fg.rbg(255,255,255)).final())
            d10= s + ' {}enumerate     {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.capitalize()", color=bm.fg.rbg(255,255,255)).final())
            d11= s + ' {}capitalize    {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.init()", color=bm.fg.rbg(255,255,255)).final())
            d12= s + ' {}init          {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.size()", color=bm.fg.rbg(255,255,255)).final())
            d13= s + ' {}size          {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.empty()", color=bm.fg.rbg(255,255,255)).final())
            d14= s + ' {}empty         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.rstrip()", color=bm.fg.rbg(255,255,255)).final())
            d15= s + ' {}rstrip        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.lstrip()", color=bm.fg.rbg(255,255,255)).final())
            d16= s + ' {}lstrip        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="''.center()", color=bm.fg.rbg(255,255,255)).final())
            d18= s + ' {}center        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            
            lists = [d0,d2,d3,d4,d5,d6,d7, d17, d8,d9,d10,d11,d12,d13,d14,d15, d16, d18 ]
            for d in lists:
                print(d)

        elif self.argument == 'tuple_functions':
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " tuple functions  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            d1 = '{}'.format(bm.words(string="().count( master = 'string' )", color=bm.fg.rbg(255,255,255)).final())
            d3 = s + ' {}count         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="().index( master = 's' )", color=bm.fg.rbg(255,255,255)).final())
            d5 = s + ' {}index         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="().enumerate()", color=bm.fg.rbg(255,255,255)).final())
            d9 = s + ' {}enumerate     {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="().init()", color=bm.fg.rbg(255,255,255)).final())
            d11= s + ' {}init          {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="().empty()", color=bm.fg.rbg(255,255,255)).final())
            d14= s + ' {}empty         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="().size()", color=bm.fg.rbg(255,255,255)).final())
            d15= s + ' {}size          {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            d1 = '{}'.format(bm.words(string="().choice()", color=bm.fg.rbg(255,255,255)).final())
            d16= s + ' {}choice        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            
            lists = [d3,d5,d9,d11,d15,d16 ]
            for d in lists:
                print(d)
        
        elif self.argument == 'complex_functions':
            s  = bm.fg.rbg(255,0,0)+chr(176)+bm.init.reset
            s1 = '| ' + " complex functions  |"
            print(chr(45) * len(s1))
            print(f'{s1}')
            print(chr(45) * len(s1))
            d0 = '{}'.format(bm.words(string="c = 1+2j", color=bm.fg.rbg(255,255,255)).final())
            d2 = ' '
            d1 = '{}'.format(bm.words(string="c.norm()", color=bm.fg.rbg(255,255,255)).final())
            d3 = s + ' {}norm        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="c.img()", color=bm.fg.rbg(255,255,255)).final())
            d5 = s + ' {}img         {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="c.real()", color=bm.fg.rbg(255,255,255)).final())
            d9 = s + ' {}real        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255),  d1, bm.init.reset)
            d1 = '{}'.format(bm.words(string="c.conj()", color=bm.fg.rbg(255,255,255)).final())
            d11= s + ' {}conj        {}: {}{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), d1,  bm.init.reset)
            
            lists = [d0, d2, d3,d5,d9,d11]
            for d in lists:
                print(d)


        else: pass
                
