from script.STDIN.LinuxSTDIN   import ascii as a

cdef list build( list s,  unsigned int style=0, unsigned long int length=1 ):
    cdef:
        unsigned long int i, j, len_, l, n
        list list_ = []
        str str_ = ""
        list paren = a.parenthesis(style)
        list left = paren[:3]
        list right= paren[-3:]
        list return_ = []
        list INT_
    
    len_ = len(s)
    l = 0
    
    for i in range( len_):
        n = len( s[i] )
        for j in range( n ):
            if len( s[i][j] ) > l: l = len(s[i])
        list_.append( l )
    
    for j in range(n):
        INT_ = []
        for i in range(len_):
            l = len( s[i][n] )
            str_ = left[1] + " " + " " * (length-l) + s[i][n]+" "+right[0]
            str_ = " " * (length-len(str_)) + str_
            INT_.append( str_ )
        return_.append( INT_ )

    return return_

cdef sym(unsigned int n):
    return a.parenthesis(n)

cdef class handling:
    cdef public:
        list master
    def __cinit__(self, master):
        self.master     = master
    cdef lists(self, unsigned int style = 0):
        cdef:
            unsigned long int i, j, length, m, l, w, p, n
            str string = ""
            list typ = [type( list()), type( tuple())]
            list typ_= [type(int()), type(float()), type(bool()), type(None), type(str())]
            unsigned long int len_
            list data_len = []
            str str_ = ""
            str string_ = ""
            list paren = a.parenthesis(style)
            list left = paren[:3]
            list right= paren[-3:]
            unsigned long int nraw, ncol, IN, IM, ncol_, nraw_
            list index_list = []
            tuple idd 
            list INT, IMT, max_col
            list index_data = []
        
        if self.master:
            length = len( self.master )
            for i in range(length):
                len_ = 0
                ncol = 1
                if type( self.master[i] ) in typ:
                    m = len( self.master[i] )
                    for j in range(m):
                        if type( self.master[i][j] ) in typ_:
                            ncol_ = 1
                            if len( str( self.master[i][j] ) ) > len_ : len_ = len( str( self.master[i][j] ) ) 
                            if ncol > ncol_ : ncol = ncol_

                        elif type( self.master[i][j]) in typ:
                            str_, nraw__, ncol_ = handling( self.master[i][j] ).sublist()
                            index_data.append(j)
                            
                            if nraw_ > len_: len_ = nraw_ 
                            if ncol_ > ncol: ncol = ncol_
                    data_len.append( (len_, ncol) )
                else: pass 
            
            for j in range(m):
                INT = []
                max_col = []
                for i in range(length):
                    idd = data_len[i]
                    if type( self.master[i][j]) in typ_:
                        l = len( self.master[i][j])
                        str_ = left[1] + " " + ( idd[0]-l) + str( self.master[i][j]) + " " + right[1]
                        INT.append([str_])
                    else:
                        max_col.append( self.master[i][j][0])
                        INT.append( build( self.master[i][j], style, idd[0] ))
                
                n = max( max_col )
                for i in range( length ):
                    if len( INT[i] ) < n:
                        if type(INT[i][0]) == type( str()):
                            for p in range(1, n):
                                INT[i].append( " " * len( INT[i][0] ) )
                        else:
                            for p in range(0, n):
                                INT[i].append([" " * len( INT[i][0][0]), " "*len(INT[i][0][1])])
                    else: pass 

                    for w in range(n):
                        if type( INT[i][n] ) == type( str()):
                            string += INT[i][n]+"\n"
                        else:
                            for p in range( len(INT[i][n])):
                                string += INT[i][n][p]
                            string += "\n"

        else: pass

        return string
     
    cdef sublist(self, unsigned long int style = 0):
        cdef:
            unsigned long int i, j, m,l, length
            str string = ""
            str string_= ""
            list typ = [type( list()), type( tuple())]
            list typ_= [type(int()), type(float()), type(bool()), type(None), type(str())]
            unsigned long int len_
            list data_len = []
            list paren = a.parenthesis(style)
            list left = paren[:3]
            list right= paren[-3:]

        if self.master:
            length = len( self.master )
            for i in range( length ):
                len_ = 0
                if type(self.master[i]) in typ:
                    if len( self.master[i] ) == len( self.master[0]):
                        m = len( self.master[i] )
                        for j in range(m):
                            if type( self.master[i][j] ) in typ_:
                                l = len( str( self.master[i][j] ))
                                if l > len_ : len_ = l
                                else: pass
                            else: pass
                        data_len.append( len_ )
                    else: pass
                else: pass

            for j in range(m):
                for i in range( length ):
                    l = len(self.master[i][j])
                    string += left[1] + " " * (data_len[i]-l) + str( self.master[i][j] ) + " " + right[1]+" \n"
            
            string_ = left[0] + " " + " " * (length-1) + " " * sum( data_len) + " " + right[0]+"\n"
            string = string_+string
            string_ = left[-1] + " " + " " * (length-1) + " " * sum( data_len) + " " + right[-1]+"\n"
            string += string

        else: pass
        
        l = (length-1)+sum( data_len )+4

        return string, l, m

