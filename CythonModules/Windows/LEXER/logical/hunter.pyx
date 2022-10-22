from CythonModules.Windows.LEXER.logical        import logicalError as LE

cdef class HUNTER:
    cdef public:
        unsigned long long int line 
        str master 
    cdef:
        str error , _str_
        bint active_op

    def __cinit__(self, master, line):
        self.master         = master
        self.line           = line 
        self.error          = ""
        self.active_op      = False
        self._str_          = ""


    cdef str HUNTER_OPERATORS(self, str string):
        cdef:
            str str_
            unsigned long long int i, j, k
            list operators = ['<', '>', '!']

        for i, str_ in enumerate( string ):
            if str_ in operators:
                j, k = i - 1, i + 1
                self.active_op = True
                try:
                    if string[ k ] in [ '=' ]:
                        self._str_ = str_+'='
                        j, k = i - 1 , i + 2
                        if string[j] in [' ']:
                            if string[ k + 1 ] in [' ']:  pass
                            else:
                                self.error = LE.ERRORS(self.line).ERROR3(self.master, self._str_, string[ k + 1 ])
                                break
                        else:
                            self.error = LE.ERRORS(self.line).ERROR3(self.master, string[j], self._str_)
                            break
                    else:
                        if str_ == '!':
                            self.error = LE.ERRORS(self.line).ERROR0(self.master)
                            break
                        else:
                            if string[ j ] in [' ']:
                                if string[ k ] in [' ']:  pass
                                else:
                                    self.error = LE.ERRORS(self.line).ERROR3(self.master, str_, string[ k ])
                                    break
                            else:
                                self.error = LE.ERRORS(self.line).ERROR3(self.master, string[ j ], str_)
                                break
                except IndexError:
                    self.error = LE.ERRORS(self.line).ERROR0(self.master)
                    break
            elif str_ in [ '?' ]:
                j, k = i-1, i + 1

                try:
                    if string[j] in [' ']:
                        if string[k] in [' ']:  pass
                        else:
                            self.error = LE.ERRORS(self.line).ERROR3(self.master, str_, string[k])
                            break
                    else:
                        self.error = LE.ERRORS(self.line).ERROR3(self.master, string[j], str_)
                        break
                except IndexError:
                    self.error = LE.ERRORS(self.line).ERROR0(self.master)
                    break
            elif str_ in [ '=' ]:
                if self.active_op is True:  self.active_op = False
                else:
                    self.active_op  = True
                    j, k = i -1 , i + 1
                    try:
                        if string[ k ] in [ '=' ]:
                            self._str_ = '=='
                            if string[ j ] in [' ']:
                                if string[ k + 1 ] in [' ']:  pass
                                else:
                                    self.error = LE.ERRORS(self.line).ERROR3(self.master, self._str_, string[ k + 1 ])
                                    break
                            else:
                                self.error = LE.ERRORS(self.line).ERROR3(self.master, string[ j ], self._str_)
                                break
                        else:
                            self.error = LE.ERRORS(self.line).ERROR0(self.master)
                            break
                    except:
                        self.error = LE.ERRORS(self.line).ERROR0(self.master)
                        break
            else:  pass

        return self.error