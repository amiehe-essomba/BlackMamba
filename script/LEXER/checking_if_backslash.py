from script                     import control_string
from script.STDIN.WinSTDIN      import stdin
from script.LEXER               import segmentation
from script.STDIN.LinuxSTDIN    import bm_configure as bm
try:
    from CythonModules.Windows  import fileError as fe 
except ImportError:
    from CythonModules.Linux    import fileError as fe 


ie = bm.fg.blue_L
ve = bm.fg.rbg(0, 255, 0)
te = bm.fg.magenta_M

class BACKSSLASH:

    def __init__(self, master, data_base, line):
        self.master             = master
        self.data_base          = data_base
        self.line               = line
        self.analyze            = control_string.STRING_ANALYSE(self.data_base, self.line)

    def BACKSLASH(self, _id_: int = 1):
        self.error              = None
        self.string_line        = 0
        self.space              = 0
        self.backend            = None
        self.data_storage       = []
        self.normal_string      = ' '
        self.string             = ''
        self.new_string         = ''
        self._string_count      = 0
        self.type_of_backslash  = None
        self.locked             = False
        self.last_char          = None

        self.master, self.error = self.analyze.DELETE_SPACE( self.master )

        if self.error is None:
            for str_ in self.master:
                if str_ in ['"', "'"]:
                    self.backend = str_
                    break
                else: pass
            self.last_char = self.master[ -1 ]

            for i,  str_ in enumerate( self.master ):
                if str_ in ['\{}'.format('')]:

                    if self.backend is not None:
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

                                            if self.error is None:
                                                if self.active_tab == True:
                                                    self.string         = self.string[ _id_ : ]                                                    # removing '\t' due to tab
                                                    self.normal_string  = self.normal_string[ _id_ : ]

                                                    try:
                                                        self.string_rebuild             = ''
                                                        self.string, self.error         = control_string.STRING_ANALYSE(self.data_base,
                                                                            (self.line + self.string_line)).DELETE_SPACE(self.string)
                                                        self.normal_string, self.error  = control_string.STRING_ANALYSE(self.data_base,
                                                            (self.line + self.string_line)).DELETE_SPACE( self.normal_string )

                                                        if self.error is None:

                                                            for w in self.normal_string:
                                                                if w in ['\{}'.format('')]:
                                                                    self.error = ERRORS( (self.line+self.string_line)).ERROR1( self.normal_string )
                                                                    break
                                                                else: pass

                                                            if self.error is None:
                                                                if self.backend not in self.normal_string :
                                                                    self.string_check, self.error = segmentation.SEGMENTATION(
                                                                        self.string, self.normal_string, self.data_base,
                                                                        (self.line+self.string_line) ).TREATEMENT( _id_+1, te )

                                                                    if self.error is None:
                                                                        self.data_storage.append( self.string_check )

                                                                    else: break

                                                                else:
                                                                    if self.normal_string.count( self.backend ) == 1:
                                                                        if len( self.normal_string ) != 1:
                                                                            if self.normal_string[ -1 ] != self.backend:
                                                                                self.data_split = self.normal_string.split( self.backend )
                                                                                self.string_add = ''

                                                                                for i, __string__ in enumerate( self.data_split ):
                                                                                    self.string_check, self.error = segmentation.SEGMENTATION(
                                                                                        __string__, __string__,self.data_base,
                                                                                                    (self.line+self.string_line)
                                                                                                    ).TREATEMENT(_id_ + 1, te)

                                                                                    if self.error is None:
                                                                                        if i == 0: self.string_add += self.string_check
                                                                                        else:
                                                                                            self.backend    += self.string_check
                                                                                            self.string_add += self.backend
                                                                                    else: break
                                                                                if self.error is None:
                                                                                    self.data_storage.append( self.string_add )
                                                                                    break
                                                                                else: break
                                                                            else:
                                                                                self.string_check, self.error = segmentation.SEGMENTATION(
                                                                                    self.normal_string[: -1], self.normal_string[: -1],
                                                                                    self.data_base, (self.line+self.string_line)
                                                                                    ).TREATEMENT(_id_ + 1, te)

                                                                                if self.error is None:
                                                                                    self.data_storage.append(self.string_check+self.backend)
                                                                                    break
                                                                                else:break
                                                                        else:
                                                                            self.data_storage.append( self.backend )
                                                                            break
                                                                    else:
                                                                        self.error = ERRORS( (self.line+self.string_line) ).ERROR0( self.normal_string )
                                                                        break
                                                            else: break
                                                        else:  self.error = None
                                                    except IndexError :
                                                        if self.space <= 5: self.space += 1
                                                        else:
                                                            self.error = ERRORS((self.line + self.string_line)).ERROR2()
                                                            break
                                                else:
                                                    self.error = ERRORS((self.line + self.string_line)).ERROR3()
                                                    break

                                            else:
                                                break

                                        except KeyboardInterrupt:
                                            self.error = ERRORS( self.line ).ERROR3()
                                            break
                                        except EOFError:
                                            self.error = ERRORS(self.line).ERROR3()
                                            break
                                else:
                                    self.error = ERRORS(self.line).ERROR1(self.master)
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
                                                    self.data_base, (self.line + self.string_line)).STDIN({'0': ie, '1': ve}, _id_)

                                                if self.error is None:
                                                    if self.active_tab == True:
                                                        self.string = self.string[_id_:]  # removing '\t' due to tab
                                                        self.normal_string = self.normal_string[_id_:]

                                                        try:
                                                            self.string_rebuild = ''
                                                            self.string, self.error = control_string.STRING_ANALYSE(
                                                                self.data_base,
                                                                (self.line + self.string_line)).DELETE_SPACE(self.string)
                                                            self.normal_string, self.error = control_string.STRING_ANALYSE(
                                                                self.data_base,
                                                                (self.line + self.string_line)).DELETE_SPACE(self.normal_string)

                                                            if self.error is None:
                                                                for w in self.normal_string:
                                                                    if w in ['\{}'.format('')]:
                                                                        self.error = ERRORS( (self.line + self.string_line)
                                                                            ).ERROR1(self.normal_string)
                                                                        break
                                                                    else: pass
                                                                if self.error is None:
                                                                    if self.backend not in self.normal_string:
                                                                        self.string_check, self.error = segmentation.SEGMENTATION(
                                                                            self.string, self.normal_string,
                                                                            self.data_base,
                                                                            (self.line + self.string_line)).TREATEMENT(
                                                                            _id_ + 1, te)

                                                                        if self.error is None: self.data_storage.append(self.string_check)
                                                                        else:break

                                                                    else:
                                                                        if self.normal_string.count( self.backend ) == 1:
                                                                            if len( self.normal_string ) != 1:
                                                                                if self.normal_string[-1 ] != self.backend:
                                                                                    self.data_split = self.normal_string.split(
                                                                                        self.backend)
                                                                                    self.string_add = ''

                                                                                    for i, __string__ in enumerate(self.data_split):
                                                                                        self.string_check, self.error = segmentation.SEGMENTATION(
                                                                                            __string__, __string__,
                                                                                            self.data_base,
                                                                                            (self.line + self.string_line)
                                                                                            ).TREATEMENT(_id_ + 1, te)

                                                                                        if self.error is None:
                                                                                            if i == 0: self.string_add += self.string_check
                                                                                            else:
                                                                                                self.backend += self.string_check
                                                                                                self.string_add += self.backend
                                                                                        else: break
                                                                                    if self.error is None:
                                                                                        self.data_storage.append(  self.string_add)
                                                                                        break
                                                                                    else:break
                                                                                else:
                                                                                    self.string_check, self.error = segmentation.SEGMENTATION(
                                                                                        self.normal_string[: -1], self.normal_string[: -1],
                                                                                        self.data_base, (self.line + self.string_line) ).TREATEMENT(_id_ + 1, te)

                                                                                    if self.error is None:
                                                                                        self.data_storage.append( self.string_check + self.backend)
                                                                                        break
                                                                                    else:break
                                                                            else:
                                                                                self.data_storage.append(self.backend)
                                                                                break
                                                                        else:
                                                                            self.error = ERRORS( (self.line + self.string_line)).ERROR0(self.normal_string)
                                                                            break
                                                                else:break
                                                            else: self.error = None
                                                        except IndexError:
                                                            if self.space <= 5: self.space += 1
                                                            else:
                                                                self.error = ERRORS((self.line + self.string_line)).ERROR2()
                                                                break
                                                    else:
                                                        self.error = ERRORS( (self.line + self.string_line) ).ERROR3()
                                                        break
                                                else: break

                                            except KeyboardInterrupt:
                                                self.error = ERRORS(self.line).ERROR3()
                                                break
                                            except EOFError:
                                                self.error = ERRORS(self.line).ERROR3()
                                                break

                                    else:
                                        if self.last_char == self.backend and len( self.master ) > 1:
                                            try:
                                                if self.master[i + 1] in ['n', 't']:
                                                    self.type_of_backslash  = self.master[ i + 1]
                                                    self.data_storage.append( self.master[ : i ] )
                                                    self._master_, self.error = DEEP_CHECKING( self.master[ i + 2 : ],
                                                            self.data_base, self.line ).BACKSLASH( self.master )
                                                    self.data_storage.append (self._master_ )
                                                    self.locked             = True
                                                    break
                                            except IndexError:
                                                self.error = ERRORS(self.line).ERROR0(self.master)
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                else:
                                    self.error = ERRORS(self.line).ERROR1(self.master)
                                    break
                            else: pass
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.master )
                        break
                else:
                    if i == len( self.master ) - 1:
                        if self.locked is False: self.data_storage.append( self.master )
                        else:  pass
                    else:
                        if str_ == self.master[ 0 ]: self._string_count += 1
                        else: pass
            if self.error is None:
                if self.type_of_backslash is None:
                    for str_ in self.data_storage:
                        self.new_string += str_
                else:
                    for i, str_ in enumerate( self.data_storage ):
                        if i < len( self.data_storage ) - 1:
                            if self.type_of_backslash == 'n':
                                self.new_string += '{}\n'.format(str_)
                            else:
                                self.new_string += '{}\t'.format(str_)
                        else: self.new_string += str_

                self.master = self.new_string
            else: self.error  = self.error
        else:  pass
        
        return self.new_string, self.error

class DEEP_CHECKING:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base

    def BACKSLASH(self, main_string: str):
        self.error              = None
        self.backend            = 0
        self.frontend            = 0
        self.line               = None
        self.string             = ''
        self.data_backend       = []
        self.data_frontend      = []
        self.master_rebuild     = ''

        for i, str_ in enumerate( self.master ):
            if self.line is None:
                if str_ in ['\{}'.format('')]:
                    try:
                        if self.master[ i + 1 ] in ['n']:
                            self.frontend += 1
                            self.line = True
                            if self.string:
                                self.data_frontend.append( self.string )
                                self.master_rebuild += '{}\n'.format(self.string)
                                self.string = ''
                            else: self.master_rebuild += '{}\n'.format(self.string)

                        elif self.master[ i + 1] in ['t']:

                            self.backend += 1
                            self.line = True
                            if self.string:
                                self.data_backend.append( self.string )
                                self.master_rebuild += '{}\t'.format(self.string)
                                self.string = ''
                            else: self.master_rebuild += '{}\n'.format(self.string)
                        else: pass
                            #self.error = ERRORS( self.line ).ERROR4( main_string )
                            #break
                    except IndexError:
                        self.error = ERRORS( self.line ).ERROR0( main_string )
                        break

                else:
                    self.string += str_
                    if i == len( self.master ) - 1:  self.master_rebuild += '{}'.format(self.string)
                    else: pass
            else: self.line = None

        return  self.master_rebuild, self.error

class BACKSSLASH_FOR_INTERPRETER:
    
    def __init__(self, master, data_base, line):
        self.master             = master
        self.data_base          = data_base
        self.line               = line
        self.analyze            = control_string.STRING_ANALYSE(self.data_base, self.line)

    def BACKSLASH(self, _id_: int , MainList : list = []):
        self.error              = None
        self.string_line        = 0
        self.space              = 0
        self.backend            = None
        self.data_storage       = []
        self.normal_string      = ' '
        self.string             = ''
        self.new_string         = ''
        self._string_count      = 0
        self.type_of_backslash  = None
        self.locked             = False
        self.last_char          = None
        self.isBreak            = False
        self.loopActivation     = False
        self.initLine           = self.line

        self.master, self.error = self.analyze.DELETE_SPACE( self.master )

        if self.error is None:
            for str_ in self.master:
                if str_ in ['"', "'"]:
                    self.backend = str_
                    break
                else: pass
            self.last_char = self.master[ -1 ]

            for i,  str_ in enumerate( self.master ):
                if str_ in ['\{}'.format('')]:
                    if self.backend is not None:
                        if self.backend == '"': self.opposite_backend   = "'"
                        else: self.opposite_backend   = '"'

                        if i == len( self.master ) - 1:
                            if self.locked is False :
                                if self._string_count % 2 == 1:
                                    self.data_storage.append(self.master[: - 1])

                                    if MainList:
                                        self.NewLIST                = stdin.STDIN(self.data_base, self.line ).FOR_STRING(_id_, MainList)
                                        for x, _string_ in enumerate( self.NewLIST ):
                                            self.loopActivation = True
                                            self.string_line    += 1
                                            try:
                                                self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                (self.line + self.string_line)).STDIN_FOR_INTERPRETER( _id_, _string_ )
                                                
                                                if self.error is None:
                                                    if self.active_tab == True:
                                                        self.string         = self.string[ _id_ : ]                                                    # removing '\t' due to tab
                                                        self.normal_string  = self.normal_string[ _id_ : ]

                                                        try:
                                                            self.string_rebuild             = ''
                                                            self.string, self.error         = control_string.STRING_ANALYSE(self.data_base,
                                                                                (self.line + self.string_line)).DELETE_SPACE(self.string)
                                                            self.normal_string, self.error  = control_string.STRING_ANALYSE(self.data_base,
                                                                (self.line + self.string_line)).DELETE_SPACE( self.normal_string )

                                                            if self.error is None:

                                                                for w in self.normal_string:
                                                                    if w in ['\{}'.format('')]:
                                                                        self.error = ERRORS( (self.line+self.string_line) ).ERROR1( self.normal_string )
                                                                        break
                                                                    else: pass

                                                                if self.error is None:
                                                                    if self.backend not in self.normal_string :
                                                                        self.string_check, self.error = segmentation.SEGMENTATION(
                                                                            self.string, self.normal_string, self.data_base,
                                                                            (self.line+self.string_line) ).TREATEMENT( _id_+1, te )

                                                                        if self.error is None:
                                                                            self.data_storage.append( self.string_check )

                                                                        else: break

                                                                    else:
                                                                        if self.normal_string.count( self.backend ) == 1:
                                                                            if len( self.normal_string ) != 1:
                                                                                if self.normal_string[ -1 ] != self.backend:
                                                                                    self.data_split = self.normal_string.split(
                                                                                        self.backend )
                                                                                    self.string_add = ''

                                                                                    for i, __string__ in enumerate( self.data_split ):
                                                                                        self.string_check, self.error = segmentation.SEGMENTATION(
                                                                                            __string__, __string__,self.data_base,
                                                                                                        (self.line+self.string_line)
                                                                                                        ).TREATEMENT(_id_ + 1, te)

                                                                                        if self.error is None:
                                                                                            if i == 0: self.string_add += self.string_check
                                                                                            else:
                                                                                                self.backend    += self.string_check
                                                                                                self.string_add += self.backend
                                                                                        else: break
                                                                                    if self.error is None:
                                                                                        self.data_storage.append( self.string_add )
                                                                                        self.isBreak                    = True
                                                                                        self.data_base['globalIndex']   = x+self.data_base['starter']
                                                                                        break
                                                                                    else: break
                                                                                else:
                                                                                    self.string_check, self.error = segmentation.SEGMENTATION(
                                                                                        self.normal_string[: -1], self.normal_string[: -1],
                                                                                        self.data_base, (self.line+self.string_line)
                                                                                        ).TREATEMENT(_id_ + 1, te)

                                                                                    if self.error is None:
                                                                                        self.data_storage.append(self.string_check+self.backend)
                                                                                        self.isBreak                    = True
                                                                                        self.data_base['globalIndex']   = x+self.data_base['starter']
                                                                                        break
                                                                                    else:break
                                                                            else:
                                                                                self.isBreak                    = True
                                                                                self.data_base['globalIndex']   = x+self.data_base['starter']
                                                                                self.data_storage.append( self.backend )
                                                                                break
                                                                        else:
                                                                            self.error = ERRORS( (self.line+self.string_line)
                                                                                                    ).ERROR0( self.normal_string )
                                                                            break
                                                                else: break
                                                            else:  self.error = None
                                                        except IndexError :
                                                            if self.space <= 5: self.space += 1
                                                            else:
                                                                self.error = ERRORS((self.line + self.string_line)).ERROR2()
                                                                break
                                                    else:
                                                        self.error = ERRORS((self.line + self.string_line)).ERROR3()
                                                        break
                                                else: break
                                            except KeyboardInterrupt:
                                                self.error = ERRORS( self.line ).ERROR3()
                                                break
                                            except EOFError:
                                                self.error = ERRORS(self.line).ERROR3()
                                                break
                                    
                                    else:
                                        self.error = ERRORS(self.line ).ERROR3()
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR1(self.master)
                                    break
                            else: pass
                        else:
                            if self.master[ i + 1] in ['n', 't']:
                                if self._string_count % 2 == 1:
                                    if i + 1 == len( self.master ) - 1:
                                        self.type_of_backslash  = self.master[ i + 1 ]
                                        self.data_storage.append( self.master[ : -2])
                                        self.locked             = True
                                        
                                        if MainList:
                                            self.NewLIST                = stdin.STDIN(self.data_base, self.line ).FOR_STRING(_id_, MainList)
                                            for x, _string_ in enumerate( self.NewLIST ):
                                                self.loopActivation = True
                                                self.string_line    += 1
                                                try:
                                                    self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                (self.line + self.string_line)).STDIN_FOR_INTERPRETER( _id_, _string_ )

                                                    if self.error is None:
                                                        if self.active_tab == True:
                                                            self.string = self.string[_id_:]  # removing '\t' due to tab
                                                            self.normal_string = self.normal_string[_id_:]

                                                            try:
                                                                self.string_rebuild = ''
                                                                self.string, self.error = control_string.STRING_ANALYSE(
                                                                    self.data_base,
                                                                    (self.line + self.string_line)).DELETE_SPACE(self.string)
                                                                self.normal_string, self.error = control_string.STRING_ANALYSE(
                                                                    self.data_base,
                                                                    (self.line + self.string_line)).DELETE_SPACE(self.normal_string)

                                                                if self.error is None:
                                                                    for w in self.normal_string:
                                                                        if w in ['\{}'.format('')]:
                                                                            self.error = ERRORS( (self.line + self.string_line)
                                                                                ).ERROR1(self.normal_string)
                                                                            break
                                                                        else: pass
                                                                    if self.error is None:
                                                                        if self.backend not in self.normal_string:
                                                                            self.string_check, self.error = segmentation.SEGMENTATION(
                                                                                self.string, self.normal_string, self.data_base,
                                                                                (self.line + self.string_line)).TREATEMENT( _id_ + 1, te)

                                                                            if self.error is None: self.data_storage.append(self.string_check)
                                                                            else:break

                                                                        else:
                                                                            if self.normal_string.count( self.backend ) == 1:
                                                                                if len( self.normal_string ) != 1:
                                                                                    if self.normal_string[-1] != self.backend:
                                                                                        self.data_split = self.normal_string.split(
                                                                                            self.backend)
                                                                                        self.string_add = ''

                                                                                        for i, __string__ in enumerate(self.data_split):
                                                                                            self.string_check, self.error = segmentation.SEGMENTATION(
                                                                                                __string__, __string__,
                                                                                                self.data_base, (self.line + self.string_line) ).TREATEMENT(_id_ + 1, te)

                                                                                            if self.error is None:
                                                                                                if i == 0: self.string_add += self.string_check
                                                                                                else:
                                                                                                    self.backend += self.string_check
                                                                                                    self.string_add += self.backend
                                                                                            else: break
                                                                                        if self.error is None:
                                                                                            self.data_storage.append( self.string_add)
                                                                                            self.data_base['globalIndex']   = x+self.data_base['starter']
                                                                                            self.isBreak                    = True
                                                                                            break
                                                                                        else:break
                                                                                    else:
                                                                                        self.string_check, self.error = segmentation.SEGMENTATION(
                                                                                            self.normal_string[: -1], self.normal_string[: -1], self.data_base,
                                                                                            (self.line + self.string_line) ).TREATEMENT(_id_ + 1, te)

                                                                                        if self.error is None:
                                                                                            self.data_storage.append( self.string_check + self.backend)
                                                                                            self.data_base['globalIndex']   = x+self.data_base['starter']
                                                                                            self.isBreak                    = True
                                                                                            break
                                                                                        else:break
                                                                                else:
                                                                                    self.isBreak                    = True
                                                                                    self.data_base['globalIndex']   = x + self.data_base['starter']
                                                                                    self.data_storage.append(self.backend)
                                                                                    break
                                                                            else:
                                                                                self.error = ERRORS( (self.line + self.string_line) ).ERROR0(self.normal_string)
                                                                                break
                                                                    else:break
                                                                else: self.error = None
                                                            except IndexError:
                                                                if self.space <= 5: self.space += 1
                                                                else:
                                                                    self.error = ERRORS((self.line + self.string_line)).ERROR2()
                                                                    break
                                                        else:
                                                            self.error = ERRORS( (self.line + self.string_line) ).ERROR3()
                                                            break
                                                    else: break

                                                except KeyboardInterrupt:
                                                    self.error = ERRORS(self.line).ERROR3()
                                                    break
                                                except EOFError:
                                                    self.error = ERRORS(self.line).ERROR3()
                                                    break
                                        else: 
                                            self.error = ERRORS(self.line ).ERROR3()
                                            break
                                    else:
                                        if self.last_char == self.backend and len( self.master ) > 1:
                                            try:
                                                if self.master[i + 1] in ['n', 't']:
                                                    self.type_of_backslash  = self.master[ i + 1]
                                                    self.data_storage.append( self.master[ : i ] )
                                                    self._master_, self.error = DEEP_CHECKING( self.master[ i + 2 : ],
                                                            self.data_base, self.line ).BACKSLASH( self.master )
                                                    self.data_storage.append (self._master_ )
                                                    self.locked             = True
                                                    break
                                            except IndexError:
                                                self.error = ERRORS(self.line).ERROR0(self.master)
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                else:
                                    self.error = ERRORS(self.line).ERROR1(self.master)
                                    break
                            else: pass
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.master )
                        break
                else:
                    if i == len( self.master ) - 1:
                        if self.locked is False: self.data_storage.append( self.master )
                        else:  pass
                    else:
                        if str_ == self.master[ 0 ]: self._string_count += 1
                        else: pass
            if self.error is None:
                if self.type_of_backslash is None:
                    for str_ in self.data_storage:
                        self.new_string += str_
                else:
                    for i, str_ in enumerate( self.data_storage ):
                        if i < len( self.data_storage ) - 1:
                            if self.type_of_backslash == 'n':
                                self.new_string += '{}\n'.format(str_)
                            else:
                                self.new_string += '{}\t'.format(str_)
                        else: self.new_string += str_

                self.master = self.new_string
            else: pass
        else:  pass
        
        if self.error is None:
            if self.loopActivation is True:
                if self.isBreak is True: pass 
                else: 
                    if self.backend: self.error = ERRORS( self.initLine ).ERROR5( self.master, self.backend )
                    else: self.error = ERRORS( self.initLine ).ERROR0( self.master  )
            else: pass
        else: pass
        
        return self.new_string, self.error

class ERRORS:
    def __init__(self, line):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    def ERROR0(self, string: str):
        error = ' {}line: {}{}'.format( self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>.'.format(self.white, self.cyan, string)+error

        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}due to bad {}backslash {}<< \ >> {}position . {}line: {}{}'.format(self.white, self.red, self.magenta,
                                                                                      self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string)+error

        return self.error+self.reset

    def ERROR2(self):
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}syntax error, {}EMPTY {}value was detected. {}line : {}{}'.format(self.white, 
                                                                                self.white, self.yellow, self.white, self.yellow, self.line)
        return  self.error+self.reset

    def ERROR3(self):
        self.error = fe.FileErrors( 'IndentationError' ).Errors() + '{}unexpected an indented block. {}line : {}{}'.format(self.yellow, 
                                                self.white, self.yellow, self.line)
        return  self.error+self.reset

    def ERROR4(self, string: str):
        error = '{}due to bad char {}after {}<< \ >>. {}line: {}{}'.format(self.white, self.red, self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string)+error

        return  self.error+self.reset
    
    def ERROR5(self, string: str, _open_: str):
        error       = '{}close the {}opening {}<< {} >>. {}line: {}{}'.format( self.white, self.red, self.blue, _open_,self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

