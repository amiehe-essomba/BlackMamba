from script                     import control_string 
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from CythonModules.Windows      import fileError    as fe 


class MODULE_LOAD:
    def __init__(self, master: str, data_base: dict, line: int):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.control        = control_string.STRING_ANALYSE(self.data_base, self.line)

    def MODULE_LOAD(self):

        self.string         = ''
        self.key            = ['from', 'load', 'module', 'as']
        self.info           = []
        self.data           = []
        self.error          = None
        self.final          = None
        self.active_key     = None
        self.alias          = None
        self._s_            = "|"

        for i, str_ in enumerate( self.master ):
            if i != len( self.master ) - 1:
                if str_ in [' ']:
                    if self.string in self.key:
                        try:
                            if not self.info:
                                if self.string in [ 'from', 'load' ]:
                                    if not self.data:
                                        self.info.append( self.string )
                                        self.string = ''
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                                else:
                                    self.data.append( self.string )
                                    self.string = ''
                            else:
                                if   len( self.info ) == 1:
                                    if self.info[ 0 ] in [ 'load', 'from' ]:
                                        if self.string in [ 'module' ]:
                                            self.info.append( self.string )
                                            self.string = ''
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                                elif len( self.info ) == 2:
                                    if self.info[-1] in [ 'module' ] and self.info[ 0 ] in [ 'from' ]:
                                        if self.string in [ 'load' ]:
                                            self.info.append( self.string )
                                            self.string     = ''
                                            self.active_key = None
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break

                                    elif self.info[ - 1] in [ 'module' ] and self.info[ 0 ] in [ 'load' ]:
                                        if self.string in [ 'as' ]:
                                            self.info.append( self.string )
                                            self.string         = ''
                                            self.active_key     = None
                                        else:
                                            self.error = ERRORS(self.line).ERROR0(self.master)
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                                elif len( self.info ) == 3:
                                    if self.info[ 0 ] in [ 'from' ] and self.info[ 1 ]  in [ 'module' ]:
                                        if self.info[ 2 ] in [ 'load' ]:
                                            if self.string == 'as' :
                                                self.info.append( self.string )
                                                self.string     = ''
                                                self.active_key = None
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                        except IndexError:
                            self.error = ERRORS( self.line ).ERROR0( self.master )
                            break
                    else:
                        if self.string:
                            if self.info:
                                self.string, self.err           = self.control.DELETE_SPACE( self.string )
                                self.new                        = []
                                if self._s_ in self.string:
                                    if len( self.info ) == 2:
                                        if self.info[ -1 ] == 'module' and self.info[ 0 ] == 'from':
                                            if self.active_key != 'locked':
                                                if self._s_ == self.string[ 0 ] and self._s_ == self.string[ -1 ]:
                                                    if self.string.count( self._s_ ) > 2:
                                                        self.mul                    = self.string.split( self._s_ )
                                                        self.t                      = ''
                                                        for w, val in enumerate( self.mul ):
                                                            if val == '':
                                                                if w in [0, len(self.mul)-1]:
                                                                    pass
                                                                else:
                                                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                    break
                                                            else:
                                                                if w == len( self.mul ) - 2:
                                                                    self.string, self.err = self.control.DELETE_SPACE( val )
                                                                    self.string, self.error = self.control.CHECK_NAME( self.string )
                                                                    if self.error is None: self.new.append( self.string )
                                                                    else:
                                                                        self.error = self.error = ERRORS( self.line ).ERROR1( self.string )
                                                                        break
                                                                else:  self.t += val + self._s_

                                                        if self.error is None:
                                                            self.t = self._s_ + self.t
                                                            self.new.append( self.t )
                                                            self.data.append( self.new[1] )
                                                            self.data.append( self.new[0] )
                                                            self.active_key = 'locked'
                                                        else: break
                                                    else:
                                                        self.error = ERRORS( self.line ).ERROR0( self.string )
                                                        break
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR0( self.string )
                                                    break
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                                else:
                                    if self.active_key != 'locked':
                                        if   len( self.info ) == 2 and self.info[ -1 ] == 'module'          : self.active_key = 'locked'
                                        elif len( self.info ) == 3 and self.info[ -1 ] in [ 'load', 'as' ]  : self.active_key = 'locked'
                                        elif len( self.info ) == 4 and self.info[ -1 ] == 'as'              : self.active_key = 'locked'
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break

                                        if self.error is None:
                                            self.string_, self.error     = self.control.CHECK_NAME( self.string )
                                            if self.error is None: self.data.append( self.string_ )
                                            else:
                                                self.error = ERRORS( self.line ).ERROR1( self.string )
                                                break
                                        else: break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                                if self.error is None:  self.string     = ''
                                else:  break
                            else:
                                self.data.append( self.string )
                                self.string     = ''
                        else:  pass
                else: self.string += str_
            else:
                self.string     += str_
                if self.string not in self.key:
                    if self.info:
                        if self.string == str_:
                            if self.active_key != 'locked':
                                if str_ in self.control.LOWER_CASE()+self.control.UPPER_CASE()+[ '*' ]:
                                    if self.string in [ '*' ]:
                                        if len( self.info ) == 3:
                                            if self.info[ -1 ] in [ 'load' ] and self.info[ 0 ] in [ 'from' ]: self.data.append( self.string )
                                            else:
                                                self.error  = ERRORS( self.line ).ERROR0( self.master )
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                    else:
                                        if len( self.info ) >= 2:
                                            if self.info[ -1 ] in [ 'load', 'module', 'as' ]: self.data.append( self.string )
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                break
                                        else:
                                            self.error  = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self. master )
                                    break
                            else:
                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                break
                        else:
                            self.string, self.err   = self.control.DELETE_LEFT( self.string )
                            if self._s_ in self.string:
                                self.error = ERRORS( self.line ).ERROR1( self.string )
                                break
                            else:
                                if self.active_key != 'locked':
                                    if   len( self.info ) == 2 and self.info[ -1 ] == 'module'  : pass
                                    elif len( self.info ) == 3 and self.info[ -1 ]  == 'load'   : pass
                                    elif len( self.info ) == 3 and self.info[ -1 ]  == 'as'     : pass
                                    elif len( self.info ) == 4 and self.info[ -1 ]  == 'as'     : pass
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break

                                    if self.error is None:
                                        if self.info[ -1 ] in ['module', 'load', 'as']:
                                            self.string_, self.error = self.control.CHECK_NAME( self.string )
                                            if self.error is None:
                                                if len(self.info) >= 2: self.data.append( self.string_ )
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                                    break
                                            else:
                                                self.error = ERRORS( self.line ).ERROR1( self.string )
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                    else: break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                    else:  self.data.append( self.string )
                else:
                    self.error = ERRORS( self.line ).ERROR0( self.master )
                    break

        if self.error is None:
            if not self.info: return self.master, self.error
            else:
                if len( self.info ) >= 2:
                    if len( self.info ) == 2:
                        if self.info[ 0 ] in [ 'load' ] and self.info[ 1 ] in [ 'module' ]: pass
                        else: self.error  = ERRORS( self.line ).ERROR0( self.master )
                    elif len( self.info ) == 3:
                        if self.info[ 0 ] in [ 'from' ] and self.info[ 1 ] in [ 'module' ] :
                            if self.info[ 2 ] in [ 'load' ] : pass
                            else: self.error = ERRORS(self.line).ERROR0(self.master)
                        elif self.info[ 0 ] in [ 'load' ]and self.info[ 1 ] in [ 'module' ]:
                            if self.info[ 2 ] in [ 'as' ]:
                                if len(self.data) == 2:
                                    self.alias = self.data[-1]
                                    del self.data[-1]
                                else:  self.error = ERRORS(self.line).ERROR0(self.master)
                            else: self.error = ERRORS(self.line).ERROR0(self.master)
                        else:  self.error = ERRORS( self.line ).ERROR0( self.master )

                    elif len( self.info ) == 4:
                        if self.info[ 0 ] in [ 'from' ] and self.info[ 1 ] in [ 'module' ] :
                            if self.info[ 3 ] in [ 'as' ] and self.info[ 2 ] in [ 'load' ] :
                                self.alias  = self.data[ -1 ]
                                del self.data[ -1 ]
                            else: self.error  = ERRORS( self.line ).ERROR0( self.master )
                        else: self.error = ERRORS( self.line ).ERROR0( self.master )
                    else: self.error  = ERRORS( self.line ).ERROR0( self.master )
                else: self.error  = ERRORS( self.line ).ERROR0( self.master ) 
                
                return {'path': self.data, 'module' : self.info, 'alias' : self.alias}, self.error
        else:
            if self.info: return {'path': self.data, 'module': self.info, 'alias' : None}, self.error
            else: return self.master, self.error

class FINAL_MODULE_LOAD:
    def __init__(self, master:dict, data_base: dict, line: int):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def LOAD(self, main_string: str):
        
        self.main_string    = main_string
        self.error          = None
        
        try: self.master         = self.master[ 'value' ]
        except KeyError: self.error = ERRORS( self.line ).ERROR0( main_string )

        if self.error is None:
            self.data_storage   = []
            self.modules        = []
            self.count          = 0

            for value in self.master:
                self.path_and_module, self.error = MODULE_LOAD( value, self.data_base, self.line ).MODULE_LOAD()
                if   type( self.path_and_module ) == type( str() )  :
                    self.error == None
                elif type( self.path_and_module ) == type( dict() ) :
                    if self.error is None : pass
                    else:  break

                if self.error is None:
                    if type( self.path_and_module ) == type( str() ):
                        if self.data_storage:
                            self.path_and_module, self.error = self.control.CHECK_NAME( self.path_and_module )
                            if self.error is None: self.modules.append( self.path_and_module )
                            else:
                                self.error = ERRORS( self.line ).ERROR1( value )
                                break
                        else: self.count += 1

                    else:
                        if not self.data_storage:
                            if self.count == 0: self.data_storage.append( self.path_and_module )
                            else:
                                self.error = ERRORS( self.line ).ERROR0( main_string )
                                break
                        else:
                            self.error = ERRORS( self.line ).ERROR0( self.main_string )
                            break
                else: break

            if self.error is None:
                if not self.data_storage: self.main_string  = self.main_string
                else:
                    if self.modules:
                        self.main_string                            = self.data_storage[ 0 ]
                        self.init                                   = self.main_string[ 'path' ]
                        self.alias                                  = self.main_string[ 'alias' ]

                        if   len( self.main_string[ 'module' ]) == 2:
                            if len( self.init ) == 1:
                                self.modules.append( self.init[ 0 ] )
                                self.main_string[ 'path' ]            = None
                                self.main_string[ 'module_load' ]     = None
                                self.main_string[ 'module_main' ]     = self.modules
                            else: self.error = ERRORS( self.line ).ERROR0( main_string )
                        elif len( self.main_string[ 'module' ]) == 3:
                            if self.main_string[ 'module' ][ -1 ] == 'load':
                                if len( self.init ) == 2:
                                    if self.init[ -1 ] != '*':
                                        self.modules.append( self.init[ 1 ] )
                                        self.main_string[ 'module_main' ]     = [ self.init[ 0 ] ]
                                        self.main_string[ 'path' ]            = None
                                        self.main_string[ 'module_load' ]     = self.modules
                                        self.main_string[ 'alias' ]           = None
                                    else: self.error = ERRORS( self.line ).ERROR0( main_string )

                                elif len( self.init ) == 3:
                                    if self.init[ 2 ] != '*':
                                        self.modules.append( self.init[ 2 ] )
                                        self.main_string[ 'path' ]              = [ self.init[ 0 ] ]
                                        self.main_string[ 'module_load' ]       = self.modules
                                        self.main_string[ 'module_main' ]       = [ self.init[ 1 ] ]
                                        self.main_string[ 'alias' ]             = None
                                    else: self.error = ERRORS( self.line ).ERROR0( main_string )
                                else: self.error = ERRORS( self.line ).ERROR0( main_string )

                            elif self.main_string[ 'module' ][ -1 ] == 'as':
                                if self.init[ -1 ] != '*':
                                    if len( self.init ) <= 1:
                                        self.modules.append( self.init[ 1 ] )
                                        self.main_string[ 'module_main' ]     = [ self.init[ 0 ] ]
                                        self.main_string[ 'path' ]            = None
                                        self.main_string[ 'module_load' ]     = self.modules
                                        self.main_string[ 'alias' ]           = self.alias
                                    else: self.error = ERRORS( self.line ).ERROR0( main_string )
                                else: self.error = ERRORS( self.line ).ERROR0( main_string )
                            else: self.error = ERRORS( self.line ).ERROR0( main_string )
                        else: self.error = ERRORS( self.line ).ERROR0( main_string )
                    else:
                        self.main_string    = self.data_storage[ 0 ]
                        self.init           = self.main_string[ 'path' ]
                        self.alias          = self.main_string[ 'alias' ]

                        if   len( self.main_string[ 'module' ] ) == 2:
                            if len( self.init ) == 1:
                                self.main_string[ 'path' ]            = None
                                self.main_string[ 'module_load' ]     = None
                                self.main_string[ 'module_main' ]     = self.init
                            else: self.error = ERRORS( self.line ).ERROR0( main_string )
                        elif len( self.main_string[ 'module' ] ) == 3:
                            if self.main_string[ 'module' ][ -1 ] == 'load':
                                if len( self.init ) == 2:
                                    self.main_string[ 'module_main' ]   = [ self.init[ 0 ] ]
                                    self.main_string[ 'path' ]          = None
                                    self.main_string[ 'module_load' ]   = [ self.init[ 1 ] ]
                                    self.main_string['alias']           = self.alias
                                elif len( self.init ) == 3:
                                    self.main_string[ 'path' ]          = [ self.init[ 0 ] ]
                                    self.main_string[ 'module_load' ]   = [ self.init[ 2 ] ]
                                    self.main_string[ 'module_main' ]   = [ self.init[ 1 ] ]
                                    self.main_string['alias']           = self.alias
                                else: self.error = ERRORS( self.line ).ERROR0( main_string )

                            elif self.main_string[ 'module' ][ -1 ] == 'as':
                                if len( self.init ) <= 1:
                                    self.main_string['module_main']     = [ self.init[ 0 ] ]
                                    self.main_string['path']            = None
                                    self.main_string['module_load']     = None
                                    self.main_string['alias']           = self.alias
                                else: self.error = ERRORS( self.line ).ERROR0( main_string )
                            else: self.error = ERRORS( self.line ).ERROR0( main_string )
                        elif len( self.main_string[ 'module' ] ) == 4:
                            if  self.main_string[ 'module' ][ -1 ] == 'as':
                                if len( self.init ) == 3:
                                    if self.init[ 2 ] != '*':
                                        self.main_string['path']             = [ self.init[ 0 ] ]
                                        self.main_string['module_load']      = [ self.init[ 2 ] ]
                                        self.main_string['module_main']      = [ self.init[ 1 ] ]
                                        self.main_string['alias']            = self.alias
                                    else: self.error = ERRORS( self.line ).ERROR0( main_string )

                                elif len( self.init ) == 2:
                                    self.main_string['path']             = None
                                    self.main_string['module_load']      = [ self.init[ 1 ] ]
                                    self.main_string['module_main']      = [ self.init[ 0 ] ]
                                    self.main_string['alias']            = self.alias
                                else: self.error = ERRORS( self.line ).ERROR0( main_string )
                            else: self.error = ERRORS( self.line ).ERROR0( main_string )
                        else: self.error = ERRORS( self.line ).ERROR0( main_string )
            else: pass
        else: pass 
        
        return self.main_string, self.error

    def REBUILD(self):
        self.string = ''

        for i, str_ in enumerate( self.master ):
            if len(self.master) == 1: self.string = str_
            else:
                if i < len(self.master) - 1:  self.string = self.string + str_ + ' '
                else:  self.string += str_

        return self.string

class ERRORS:
    def __init__(self, line):
        self.line       = line
        self.cyan       = bm.init.bold + bm.fg.rbg(0,255,255)
        self.red        = bm.init.bold + bm.fg.rbg(255,0,0)
        self.green      = bm.init.bold + bm.fg.rbg(0,255,0)
        self.yellow     = bm.init.bold + bm.fg.rbg(255,255,0)
        self.magenta    = bm.init.bold + bm.fg.rbg(255,0,255)
        self.white      = bm.init.bold + bm.fg.rbg(255,255,255)
        self.blue       = bm.init.bold + bm.fg.rbg(0,0,255)
        self.reset      = bm.init.reset
        self._str_      = '{}type {}help( {}var_name{} ) {}for more informations. '.format(self.white, self.magenta, self.yellow, 
                                                                                           self.magenta, self.white)

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}ERROR. {}line: {}{}. \n{}'.format(self.yellow, self.white, self.yellow, self.line, self._str_)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}<< {} >> {}module name '.format(self.cyan, string, self.white) + error

        return self.error+self.reset