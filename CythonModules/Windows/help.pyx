from script.STDIN.LinuxSTDIN    import bm_configure as bm

cdef class HELP:
    cdef public:
        str argument
    def __init__(self, argument ):
        self.argument   = argument 
    
    cpdef HELP(self):
        cdef:
            list string
            str ss, s, color, s0, s1, s2
      
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
                    s1 = s + " " + bm.fg.rbg(255,165,0)+"def "+bm.init.reset+ bm.words(string=ss, color=color).final()
                    print(f"{s1}")

                print(chr(151) * 5)
                print(chr(151) * 5)
                s       = bm.fg.rbg(255,0,0)+chr(149)+bm.init.reset
                s       += " " +  "The name of functions always start with an\n alphabetic character."
                print(chr(151) * 5)
                print(chr(151) * 5)
            
            elif self.argument == 'class_name':
                string = ["name:",  "Name:", "name( Name ):"]
                for ss in string:
                    s += " " + bm.fg.rbg(255,165,0)+"class "+bm.init.reset+ bm.words(string=ss, color=color).final()
                    print(f"{s}")

                print(chr(151) * 5)
                print(chr(151) * 5)
                s       = bm.fg.rbg(255,0,0)+chr(149)+bm.init.reset
                s       += " " + "The name of classes always start with an\n alphabetic character."
                print(chr(151) * 5)
                print(chr(151) * 5)
        else: pass
                
