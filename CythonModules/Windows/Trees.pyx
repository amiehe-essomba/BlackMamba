from CythonModules.Windows        import show
from script.STDIN.LinuxSTDIN      import bm_configure as bm

cdef dots():
    return bm.init.bold+bm.fg.rgb(0,255,0)+chr(8942)+bm.init.reset

cdef sym( unsigned int n = 0):
    if   n == 0 : return chr(9475) # |
    elif n == 1 : return chr(9495) # L
    elif n == 2 : return chr(9507) #
    elif n == 3 : return chr(9473) # _

cdef class Trees:
    cdef public:
        dict master

    def __cinit__(self, master):
        self.master     = master
    
    cpdef Trees(self, str main = "Trees", unsigned int m = 0):
        cdef:
            list values, keys
            unsigned long int i, length, len_
            str string , s, _str_
            list _key_ = []
            unsigned long int max_ = 6

        if m == 0 :
            string = " " * m + bm.init.bold+bm.fg.rbg(255,0,0)+"{}\n".format(main)+bm.init.reset+"{}\n".format(sym(0))
        else:
            string  = "{}\n".format(main)
            string += " " * m + "{}\n".format(sym(0))

        if self.master:
            values  = list(self.master.values())
            keys    = list(self.master.keys())
            length  = len(keys)
            len_    = 0

            for i in range( length):
                _str_ =bm.words(keys[i], bm.fg.rbg(255, 255, 255)).final()

                if len(keys[i]) > len_: len_ = len(keys[i])
                else: pass

            for i in range( length ):
                s = bm.words(" " * (len_-len(keys[i]))+'= ', bm.fg.rbg(255, 255, 255)).final()+bm.init.reset + show.show([[ values[i] ]]).Print()[0]
                if i < max_:
                    if type( values[i] ) == type( dict()):
                        if m == 0: string += "{}{} {}".format(sym(1), sym(3), Trees( values[i].copy() ).subTrees( keys[i], m+2 ))
                        else: string += "{}{} {}".format(sym(1), sym(3), Trees( values[i].copy() ).subTrees( keys[i], m+2 ))
                    else:
                        if i < (length - 1): string += " " * m + "{}{} {} {}\n".format(sym(2), sym(3), keys[i], s)
                        else: string += " " * m + "{}{} {} {}\n".format(sym(1), sym(3), keys[i], s)
                elif i == length - 1: 
                    if i != max_+1: string += f"{dots()}\n"*2 
                    else: pass

                    if type( values[i] ) == type( dict()):
                        if m == 0: string += "{}{} {}".format(sym(1), sym(3), Trees( values[i].copy() ).subTrees( keys[i], m+2 ))
                        else: string += "{}{} {}".format(sym(1), sym(3), Trees( values[i].copy() ).subTrees( keys[i], m+2 ))
                    else:
                        if i < (length - 1): string += " " * m + "{}{} {} {}\n".format(sym(2), sym(3), keys[i], s)
                        else: string += " " * m + "{}{} {} {}\n".format(sym(1), sym(3), keys[i], s)
                else: pass
        else: pass 

        return string 
        
    cdef subTrees(self, str main, unsigned int m):
        cdef:
            list values, keys
            unsigned long int i, length_, len_
            str string_, s 
            list _keys_ = []
            unsigned long int max_ = 6

        len_ = 0
        string_ = bm.init.bold+bm.fg.rbg(255, 255, 0)+"{}\n".format(main)+bm.init.reset
        string_+= " " * m + "{}\n".format(sym(0))


        if self.master:
            values_ = list(self.master.values())
            keys_   = list(self.master.keys())
            length_ = len(keys_)

            for i in range( length_):
                _keys_.append(bm.words(keys_[i], bm.fg.rbg(255, 255, 255)).final())
                if len(keys_[i]) > len_: len_ = len(keys_[i])
                else: pass


            for i in range( length_ ):
                if i < max_:
                    if type( values_[i] ) == type( dict()): 
                        string_ +=  " " * m + "{}{} {}".format(sym(1), sym(3), Trees( values_[i].copy() ).subTrees_( keys_[i], m+2 ))
                    else:
                        s = bm.words(" "*(len_-len(keys_[i]))+'= ', bm.fg.rbg(255, 255, 255)).final()+bm.init.reset + show.show([[ values_[i] ]]).Print()[0]
                        if i < (length_ - 1): string_ += " " * m + "{}{} {} {}\n".format(sym(2), sym(3), _keys_[i], s)
                        else: string_ += " " * m + "{}{} {} {}\n".format(sym(1), sym(3), _keys_[i], s)
                elif i == (length_ - 1):
                    if i != max_+1: string_ += "{}\n".format(dots())
                    else: pass 
                    if type( values_[i] ) == type( dict()): 
                        string_ +=  " " * m + "{}{} {}".format(sym(1), sym(3), Trees( values_[i].copy() ).subTrees_( keys_[i], m+2 ))
                    else:
                        s = bm.words(" "*(len_-len(keys_[i]))+'= ', bm.fg.rbg(255, 255, 255)).final()+bm.init.reset + show.show([[ values_[i] ]]).Print()[0]
                        if i < (length_ - 1): string_ += " " * m + "{}{} {} {}\n".format(sym(2), sym(3), _keys_[i], s)
                        else: string_ += " " * m + "{}{} {} {}\n".format(sym(1), sym(3), _keys_[i], s)
                else: pass

        else: pass

        return string_


    cdef subTrees_(self, str main, unsigned int m):
        cdef:
            list values, keys
            unsigned long int i, length_, len_
            str string_, s
            list _keys_ = []
            unsigned long int max_ = 6

        string_ = bm.init.bold+bm.fg.rbg(255, 0, 255)+"{}\n".format(main)+bm.init.reset
        string_+= " " * m + "{}\n".format(sym(0))
        len_ = 0

        if self.master:
            values_ = list(self.master.values())
            keys_   = list(self.master.keys())
            length_ = len(keys_)
            
            for i in range( length_):
                _keys_.append(bm.words(keys_[i], bm.fg.rbg(255, 255, 255)).final())
                if len(keys_[i]) > len_: len_ = len(keys_[i])
                else: pass

            for i in range( length_ ):
                if i < max_:
                    s = bm.words(" " * (len_-len(keys_[i]))+'= ', bm.fg.rbg(255, 255, 255)).final()+bm.init.reset + show.show([[ values_[i] ]]).Print()[0]
                    if type( values_[i] ) == type( dict()):
                        string_ += " " * m + "{}{} {}".format(sym(1), sym(3), Trees( values_[i].copy() ).subTrees( keys_[i], m+2 ))
                    else:
                        if i < (length_ - 1): string_ += " " * m + "{}{} {} {}\n".format(sym(2), sym(3), _keys_[i], s)
                        else: string_ += " " * m + "{}{} {} {}\n".format(sym(1), sym(3), _keys_[i], s)
                elif i == (length_ - 1):
                    if i != max_+1: string_ += "{}\n".format(dots()) 
                    else: pass 
                    s = bm.words(" " * (len_-len(keys_[i]))+'= ', bm.fg.rbg(255, 255, 255)).final()+bm.init.reset + show.show([[ values_[i] ]]).Print()[0]
                    if type( values_[i] ) == type( dict()):
                        string_ += " " * m + "{}{} {}".format(sym(1), sym(3), Trees( values_[i].copy() ).subTrees( keys_[i], m+2 ))
                    else:
                        if i < (length_ - 1): string_ += " " * m + "{}{} {} {}\n".format(sym(2), sym(3), _keys_[i], s)
                        else:  string_ += " " * m + "{}{} {} {}\n".format(sym(1), sym(3), _keys_[i], s)
                else: pass 
        else: pass

        return string_
