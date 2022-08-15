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
            str d,d1, d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12
      
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
            d1 = s + ' {}var_name      {}= {}name of a variable{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d2 = s + ' {}arg_types     {}= {}types of arguments{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d3 = s + ' {}function_name {}= {}name of a function {}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d4 = s + ' {}class_name    {}= {}name of a class{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
            d5 = s + ' {}functions     {}= {}creating of a function{}'.format(bm.fg.cyan_L, bm.fg.rbg(255,255,255), bm.fg.rbg(255,255,0), bm.init.reset)
           
            lists = [d1,d2,d3,d4,d5]
            for d in lists:
                print(d)



        else: pass
                
