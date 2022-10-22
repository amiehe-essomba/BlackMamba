from script                                         import control_string as CS
from CythonModules.Windows.LEXER.particular         import particular_str_selection as PSS
from CythonModules.Windows.LEXER.arr                import arrError as AE


cdef class BRACKET:
    cdef public:
        unsigned long long int line 
        dict data_base
    cdef:
        str error, string, _string
        dict key
        list value, left, right,
        unsigned long long count

    def __cinit__(self, data_base, line):
        self.error          = ""
        self.string         = ""
        self._string        = ""
        self.left           = ['(', '{', '[', "'", '"']
        self.right          = [')', '}', ']', "'", '"']
        self.key            = dict(s=False)
        self.value          = []
        self.count          = 0
    
    
    cdef BRACKET_ANALYSES(self, str String):
        cdef:
            unsigned long int get_opposite, r, l
            bint if_comma
            str str_, s 
        
        self.string, self.error = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( String, name="cython" )

        if not self.error:
            if self.string[ 0 ] not in self.left: self._string = self.string
            else:
                self.value, self.error = PSS.SELECTION(self.string, self.string, self.data_base,
                                                                    self.line).CHAR_SELECTION( '.' )
                if not self.error:
                    if len( self.value ) == 1:
                        get_opposite = self.left.index( self.string[ 0 ] )
                        if self.string[ -1 ] == self.right[ get_opposite ]:
                            if self.string[ 0 ] == '(':
                                l, r            = 0, 0
                                self.count      = 0
                                if_comma        = False

                                for str_ in self.string:
                                    if str_ != ',':
                                        l, r = l + str_.count('('), r + str_.count(')')
                                        if l == r:
                                            if self.count <= 1:
                                                self.count += 1
                                                l, r  = 0, 0
                                            else:
                                                self.error = AE.ERRORS( self.line ).ERROR0( self.string )
                                                break
                                        else: pass
                                    else:
                                        if_comma = True
                                        break
                                
                                if not self.error:
                                    if if_comma is False:
                                        self.key['s']               = True
                                        s, self.error               = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( 
                                                                            self.string[1 : -1], name="cython" )
                                        if not self.error: self._string = s
                                        else:
                                            self.error              = ""
                                            self._string            = self.string
                                            self.key['s']           = 'tuple'
                                    else:
                                        s, self.error               = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE(
                                                                        self.string[1: -1], name="cython")
                                        self.key['s']               = 'tuple' 
                                        self._string                = self.string
                                else: pass
                            else: self._string    = self.string
                        else: self.error = AE.ERRORS( self.line ).ERROR0( self.string )
                    else:  self._string    = self.string
                else: pass
        else: self.error = ""

        return self._string, self.key, self.error
    
    cdef CHECK_CHAR(self, str master):
        cdef :
            list chars 
            str str_

        chars = ['<', '>', '!', '?', '|', '&']

        for str_ in master :
            if str_ in chars:
                self.error = AE.ERRORS( self.line ).ERROR0( self.master )
                break
            else: pass

        return master, self.error