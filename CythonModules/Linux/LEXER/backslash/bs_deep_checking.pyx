from script.LEXER.error.CythonWIN           import backslashError   as BE

cdef class DEEP_CHECKING:
    cdef public:
        str master 
        dict data_base 
        list line
    
    cdef:
        str error , string, master_rebuild
        signed long long int backend, frontend
        list data_backend, data_frontend
       
    def __cinit__(self, master, data_base, line):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.error              = ""
        self.string             = ""
        self.master_rebuild     = ""
        self.backend            = 0
        self.frontend           = 0
        self.data_backend       = []
        self.data_frontend      = []

    cdef BACKSLASH(self, str main_string):
        cdef :
            char str_
            signed long long int i

        for i, str_ in enumerate( self.master ):
            if self.line[0] is None:
                if self.master[i] in ['\{}'.format('')]:
                    try:
                        if self.master[ i + 1 ] in ['n']:
                            self.frontend += 1
                            self.line[0] = True
                            if self.string:
                                self.data_frontend.append( self.string )
                                self.master_rebuild += '{}\n'.format(self.string)
                                self.string = ''
                            else: self.master_rebuild += '{}\n'.format(self.string)

                        elif self.master[ i + 1] in ['t']:

                            self.backend += 1
                            self.line[0] = True
                            if self.string:
                                self.data_backend.append( self.string )
                                self.master_rebuild += '{}\t'.format(self.string)
                                self.string = ''
                            else: self.master_rebuild += '{}\n'.format(self.string)
                        else: pass
                    except IndexError:
                        self.error = BE.ERRORS( self.line ).ERROR0( main_string )
                        break
                else:
                    self.string += str_
                    if i == len( self.master ) - 1:  self.master_rebuild += '{}'.format(self.string)
                    else: pass
            else: pass 
        return  self.master_rebuild, self.error