from script.STDIN.WinSTDIN                  import stdin
from CythonModules.Windows.LEXER.seg        import segmentation
from script                                 import control_string   as CS
from script.LEXER.error.CythonWIN           import backslashError   as BE
from script.STDIN.LinuxSTDIN                import bm_configure     as bm
from CythonModules.Windows.LEXER.backslash  import bs_deep_checking as BSDC

cdef class BACKSSLASH:
    cdef public:
        str master 
        dict data_base 
        unsigned long long int line
    
    cdef:
        str error , string, new_string, normal_string, backend
        str opposite_backend , string_check
        signed long int string_line, space, _string_count, max_emty_line
        list data_storage 
        bint locked, active_tab
        str type_of_backslash, last_char

       
    def __cinit__(self, master, data_base, line):
        self.master             = master
        self.data_base          = data_base
        self.line               = line
        self.error              = ""
        self.string_line        = 0
        self.space              = 0
        self.data_storage       = []
        self.normal_string      = ' '
        self.string             = ''
        self.new_string         = ''
        self._string_count      = 0
        self.locked             = False
        self.backend            = ""
        self.last_char          = ""
        self.opposite_backend   = ""
        self.active_tab         = False
        self.string_check       = ""
        self.max_emty_line      = 5
        self.type_of_backslash  = ""

    cdef BACKSLASH(self,  unsigned long int _id_ = 1):
        cdef:
            char str_ 
            str ie, ve, te, __string__
            signed long long int i
            str w, string_add = ''
            list data_split

        ie = bm.fg.blue_L
        ve = bm.fg.rbg(0, 255, 0)
        te = bm.fg.magenta_M

        self.master, self.error = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( self.master, name="cython" )

        if not self.error:
            for str_ in self.master:
                if str_ in ['"', "'"]:
                    self.backend = str_
                    break
                else: pass
            
            self.last_char = self.master[ -1 ]

            for i, str_ in enumerate( self.master ):
                if self.master[i] in ['\{}'.format('')]:

                    if self.backend :
                        if self.backend == '"': self.opposite_backend   = "'"
                        else: self.opposite_backend   = '"'

                        if i == len( self.master ) - 1:
                            if self.locked is False :
                                if self._string_count % 2 == 1:
                                    self.data_storage.append(self.master[: - 1])

                                    while True:
                                        self.string_line += 1
                                        try:
                                            self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                            (self.line + self.string_line)).STDIN({'0': ie, '1': ve }, _id_)

                                            if not self.error:
                                                if self.active_tab is True:
                                                    self.string         = self.string[ _id_ : ]                                                    # removing '\t' due to tab
                                                    self.normal_string  = self.normal_string[ _id_ : ]

                                                    try:
                                                        self.string_rebuild             = ''
                                                        self.string, self.error         = CS.STRING_ANALYSE(self.data_base,
                                                                            (self.line + self.string_line)).DELETE_SPACE(self.string, name="cython")
                                                        self.normal_string, self.error  = CS.STRING_ANALYSE(self.data_base,
                                                            (self.line + self.string_line)).DELETE_SPACE( self.normal_string, name="cython" )

                                                        if not self.error:
                                                            for w in self.normal_string:
                                                                if w in ['\{}'.format('')]:
                                                                    self.error = BE.ERRORS( (self.line+self.string_line)).ERROR1( self.normal_string )
                                                                    break
                                                                else: pass

                                                            if not self.error:
                                                                if self.backend not in self.normal_string :
                                                                    self.string_check, self.error = segmentation.SEGMENTATION(self.string, self.normal_string,
                                                                                self.data_base, (self.line + self.string_line)).TREATEMENT( _id_ + 1, te)

                                                                    if not self.error is None: self.data_storage.append( self.string_check )
                                                                    else: break

                                                                else:
                                                                    if self.normal_string.count( self.backend ) == 1:
                                                                        if len( self.normal_string ) != 1:
                                                                            if self.normal_string[ -1 ] != self.backend:
                                                                                data_split = self.normal_string.split( self.backend )
                                                                                string_add = ''

                                                                                for i, __string__ in enumerate( data_split ): 
                                                                                    self.string_check, self.error = segmentation.SEGMENTATION(__string__, __string__,
                                                                                        self.data_base, (self.line + self.string_line)).TREATEMENT( _id_ + 1, te)
                                                                                  
                                                                                    if not self.error:
                                                                                        if i == 0: string_add += self.string_check
                                                                                        else:
                                                                                            self.backend    += self.string_check
                                                                                            string_add      += self.backend
                                                                                    else: break
                                                                                if not self.error:
                                                                                    self.data_storage.append(string_add )
                                                                                    break
                                                                                else: break
                                                                            else:
                                                                                self.string_check, self.error = segmentation.SEGMENTATION(self.normal_string[: -1], self.normal_string[: -1],
                                                                                    self.data_base, (self.line + self.string_line)).TREATEMENT( _id_ + 1, te)
                                                                              
                                                                                if not self.error:
                                                                                    self.data_storage.append(self.string_check+self.backend)
                                                                                    break
                                                                                else:break
                                                                        else:
                                                                            self.data_storage.append( self.backend )
                                                                            break
                                                                    else:
                                                                        self.error = BE.ERRORS( (self.line+self.string_line) ).ERROR0( self.normal_string )
                                                                        break
                                                            else: break
                                                        else:  self.error = ""
                                                    except IndexError :
                                                        if self.space <= self.max_emty_line: self.space += 1
                                                        else:
                                                            self.error = BE.ERRORS((self.line + self.string_line)).ERROR2()
                                                            break
                                                else:
                                                    self.error = BE.ERRORS((self.line + self.string_line)).ERROR3()
                                                    break

                                            else:  break

                                        except KeyboardInterrupt:
                                            self.error = BE.ERRORS( self.line ).ERROR3()
                                            break
                                        except EOFError:
                                            self.error = BE.ERRORS(self.line).ERROR3()
                                            break
                                else:
                                    self.error = BE.ERRORS(self.line).ERROR1(self.master)
                                    break
                            else: pass
                        else:
                            if self.master[ i + 1] in ['n', 't']:
                                if self._string_count % 2 == 1:
                                    if i + 1 == len( self.master ) - 1:
                                        self.type_of_backslash  = self.master[ i + 1 ]
                                        self.data_storage.append( self.master[ : -2])
                                        self.locked             = True

                                        while True:
                                            self.string_line += 1
                                            try:
                                                self.string, self.normal_string, self.active_tab, self.error = stdin.STDIN(
                                                    self.data_base, (self.line + self.string_line)).STDIN({'0': ie, '1': ve}, _id_, name='cython')

                                                if not self.error:
                                                    if self.active_tab is True:
                                                        self.string         = self.string[ _id_ : ]
                                                        self.normal_string  = self.normal_string[ _id_ : ]
                                                        try:
                                                            self.string_rebuild = ''
                                                            self.string, self.error = CS.STRING_ANALYSE(
                                                                self.data_base,  (self.line + self.string_line)).DELETE_SPACE(self.string, name="cython")
                                                            self.normal_string, self.error = CS.STRING_ANALYSE(
                                                                self.data_base, (self.line + self.string_line)).DELETE_SPACE(self.normal_string, name="cython")

                                                            if not self.error:
                                                                for w in self.normal_string:
                                                                    if w in ['\{}'.format('')]:
                                                                        self.error = BE.ERRORS( (self.line + self.string_line)).ERROR1(self.normal_string)
                                                                        break
                                                                    else: pass
                                                                if not self.error:
                                                                    
                                                                    if self.backend not in self.normal_string:
                                                                        self.string_check, self.error = segmentation.SEGMENTATION(self.string, self.normal_string,
                                                                                self.data_base, (self.line + self.string_line)).TREATEMENT( _id_ + 1, te)

                                                                        if not self.error: self.data_storage.append(self.string_check)
                                                                        else:break
                                                                    else:
                                                                        if self.normal_string.count( self.backend ) == 1:
                                                                            if len( self.normal_string ) != 1:
                                                                                if self.normal_string[-1 ] != self.backend:
                                                                                    data_split = self.normal_string.split( self.backend)
                                                                                    string_add = ''

                                                                                    for i, __string__ in enumerate(data_split):
                                                                                        self.string_check, self.error = segmentation.SEGMENTATION(__string__, __string__,
                                                                                                self.data_base, (self.line + self.string_line)).TREATEMENT( _id_ + 1, te)

                                                                                        if not self.error:
                                                                                            if i == 0: string_add += self.string_check
                                                                                            else:
                                                                                                self.backend += self.string_check
                                                                                                string_add += self.backend
                                                                                        else: break
                                                                                    if self.error is None:
                                                                                        self.data_storage.append(string_add)
                                                                                        break
                                                                                    else:break
                                                                                else:
                                                                                    self.string_check, self.error = segmentation.SEGMENTATION(self.normal_string[: -1], 
                                                                                        self.normal_string[: -1],  self.data_base, (self.line + self.string_line)).TREATEMENT( _id_ + 1, te)
                                                                                    
                                                                                    if not self.error:
                                                                                        self.data_storage.append( self.string_check + self.backend)
                                                                                        break
                                                                                    else:break
                                                                            else:
                                                                                self.data_storage.append(self.backend)
                                                                                break
                                                                        else:
                                                                            self.error = BE.ERRORS( (self.line + self.string_line)).ERROR0(self.normal_string)
                                                                            break
                                                                else: break
                                                            else: self.error = ""
                                                        except IndexError:
                                                            if self.space <= self.max_emty_line: self.space += 1
                                                            else:
                                                                self.error = BE.ERRORS((self.line + self.string_line)).ERROR2()
                                                                break
                                                    else:
                                                        self.error = BE.ERRORS( (self.line + self.string_line) ).ERROR3()
                                                        break
                                                else: break
                                            except KeyboardInterrupt:
                                                self.error = BE.ERRORS(self.line).ERROR3()
                                                break
                                            except EOFError:
                                                self.error = BE.ERRORS(self.line).ERROR3()
                                                break
                                    else:
                                        if self.last_char == self.backend and len( self.master ) > 1:
                                            try:
                                                if self.master[i + 1] in ['n', 't']:
                                                    self.type_of_backslash  = self.master[ i + 1]
                                                    self.data_storage.append( self.master[ : i ] )
                                                    __string__, self.error = BSDC.DEEP_CHECKING( self.master[ i + 2 : ],
                                                            self.data_base, [None] ).BACKSLASH( self.master )
                                                    self.data_storage.append (__string__ )
                                                    self.locked             = True
                                                    break
                                            except IndexError:
                                                self.error = BE.ERRORS(self.line).ERROR0(self.master)
                                                break
                                        else:
                                            self.error = BE.ERRORS( self.line ).ERROR0( self.master )
                                            break
                                else:
                                    self.error = BE.ERRORS(self.line).ERROR1(self.master)
                                    break
                            else: pass
                    else:
                        self.error = BE.ERRORS( self.line ).ERROR0( self.master )
                        break
                else:
                    if i == len( self.master ) - 1:
                        if self.locked is False: self.data_storage.append( self.master )
                        else:  pass
                    else:
                        if str_ == self.master[ 0 ]: self._string_count += 1
                        else: pass

            if not self.error :
                if not self.type_of_backslash:
                    for i in range(len(self.data_storage)):
                        self.new_string += self.data_storage[i]
                else:
                    for i in range(len(self.data_storage)):
                        if i < len( self.data_storage ) - 1:
                            if self.type_of_backslash == 'n':
                                self.new_string += '{}\n'.format(self.data_storage[i])
                            else:  self.new_string += '{}\t'.format(self.data_storage[i])
                        else: self.new_string += self.data_storage[i]
            else: pass
        else:  pass
        
        return self.new_string, self.error