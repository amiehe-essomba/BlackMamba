from script         import control_string
from script.LEXER   import particular_str_selection
from script.MATHS   import integer
from script.MATHS   import real
from script.MATHS   import complex as cplx
from script.MATHS   import string as string_init
from script.MATHS   import boolean
from script.STDIN.LinuxSTDIN               import bm_configure as bm
from CythonModules.Linux                   import fileError as fe 


class TUPLE:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.selection      = particular_str_selection

    def MAIN_TUPLE(self):
        self.value          = None
        self.error          = None
        self._return_       = []

        self.string         = self.master[1 : -1]
        self.string, self.error = self.control.DELETE_SPACE( self.string )
        if self.error is None:
            self.new_data, self.error = self.selection.SELECTION( self.string, self.string, self.data_base,
                                                                  self.line ).CHAR_SELECTION( ',' )
            if self.error is None:
                for i, string in enumerate( self.new_data ):
                    self._string_, self.error = self.control.DELETE_SPACE( string )
                    if self.error is None:
                        if self._string_[ 0 ] in [str(x) for x in range(10)] + ['+', '-']:
                            self.num = None
                            if self._string_[ -1 ] not in [ 'j' ]:
                                self.check, self.error = self.selection.SELECTION( self._string_, self._string_,
                                                            self.data_base, self.line).CHAR_SELECTION('.')
                                if self.error is None:
                                    if len( self.check ) == 1:
                                        self.num, self.error = integer.INTEGER( self._string_ , self.data_base,
                                                                    self.line).INTEGER()
                                        if self.error is None:  pass
                                        else: break
                                    else:
                                        self.num, self.error = real.REAL( self._string_, self.data_base, self.line ).REAL()
                                        if self.error is None: pass
                                        else: break
                                else:
                                    self.error = self.error
                                    break
                            else:
                                self.num, self.error = cplx.COMPLEX( self._string_, self.data_base, self.line).COMPLEX()
                                if self.error is None: pass
                                else:  break

                            self._return_.append( self.num )

                        elif self._string_[ 0 ] in ['"', "'"]:
                            self.num = string_init.STRING( self._string_, self.data_base, self.line ).STRING()
                            self._return_.append( self.num )

                        elif self._string_[ 0 ] in [ '(' ]:
                            self.sub_string = self._string_[1 : -1 ]
                            self.sub_string, self.error = self.control.DELETE_SPACE( self.sub_string )
                            if self.error is None:
                                self.sub_init, self.error = self.selection.SELECTION( self.sub_string, self.sub_string,
                                                                    self.data_base, self.line ).CHAR_SELECTION(',')
                                if self.error is None:
                                    if len( self.sub_init ) == 1:
                                        self.num, self.error = cplx.COMPLEX( self._string_, self.data_base, self.line ).COMPLEX()
                                        if self.error is None:  self._return_.append( self.num )
                                        else: break
                                    else:
                                        self.num, self.error = TUPLE( self._string_, self.data_base, self.line ).TUPLE()
                                        if self.error is None: self._return_.append( self.num )
                                        else:  break
                                else:  break
                            else:
                                self.error = None
                                self._return_.append( () )

                        elif self._string_[ 0 ] in [ '[' ]:
                            self.error = ERRORS( self.line ).ERROR1('a list')
                            break

                        elif self._string_[ 0 ] in [ '{' ]:
                            self.error = ERRORS( self.line ).ERROR1('a dictionary')
                            break

                        elif self._string_ in [ 'True', 'False' ]:
                            self.num = boolean.BOOLEAN(self._string_, self.data_base, self.line).BOOLEAN()
                            self._return_.append( self.num )

                        elif self._string_ in [ 'None' ]:
                            self._return_.append( None )

                        elif self._string_ in [ 'inf' ]:
                            self.num, self.error = real.REAL(self._string_, self.data_base,
                                                                   self.line).REAL()
                            if self.error is None: self._return_.append( self.num )
                            else: break
                        else:
                            self.error = ERRORS( self.line ).ERROR0( self.master )
                            break
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.master )
                        break
            else: pass

        else:
            self.error = None
            self._return_ = self._return_

        return  tuple( self._return_ ), self.error

    def TUPLE(self):
        self.value          = None
        self.error          = None
        self._return_       = []

        self.string         = self.master[1 : -1]
        self.string, self.error = self.control.DELETE_SPACE( self.string )
        if self.error is None:
            self.new_data, self.error = self.selection.SELECTION( self.string, self.string, self.data_base,
                                                                  self.line ).CHAR_SELECTION( ',' )
            if self.error is None:
                for i, string in enumerate( self.new_data ):
                    self._string_, self.error = self.control.DELETE_SPACE( string )
                    if self.error is None:
                        if self._string_[ 0 ] in [str(x) for x in range(10)]+['+', '-']:
                            self.num = None
                            if self._string_[ -1 ] not in [ 'j' ]:
                                self.check, self.error = self.selection.SELECTION( self._string_, self._string_,
                                                            self.data_base, self.line).CHAR_SELECTION('.')
                                if self.error is None:
                                    if len( self.check ) == 1:
                                        self.num, self.error = integer.INTEGER( self._string_ , self.data_base,
                                                                    self.line).INTEGER()
                                        if self.error is None:  pass
                                        else: break
                                    else:
                                        self.num, self.error = real.REAL( self._string_, self.data_base, self.line ).REAL()
                                        if self.error is None: pass
                                        else:  break
                                else: break
                            else:
                                self.num, self.error = cplx.COMPLEX( self._string_, self.data_base, self.line).COMPLEX()
                                if self.error is None: pass
                                else: break

                            self._return_.append( self.num )

                        elif self._string_[ 0 ] in ['"', "'"]:
                            self.num = string_init.STRING( self._string_, self.data_base, self.line ).STRING()
                            self._return_.append( self.num )

                        elif self._string_[ 0 ] in [ '(' ]:
                            self.sub_string = self._string_[1 : -1 ]
                            self.sub_string, self.error = self.control.DELETE_SPACE( self.sub_string )
                            if self.error is None:
                                self.sub_init, self.error = self.selection.SELECTION( self.sub_string, self.sub_string,
                                                                    self.data_base, self.line ).CHAR_SELECTION(',')
                                if self.error is None:
                                    if len( self.sub_init ) == 1:
                                        self.num, self.error = cplx.COMPLEX( self._string_, self.data_base, self.line ).COMPLEX()
                                        if self.error is None:  self._return_.append( self.num )
                                        else:  break
                                    else:
                                        self.num, self.error = TUPLE( self._string_, self.data_base, self.line ).MAIN_TUPLE()
                                        if self.error is None:
                                            self._return_.append( self.num )
                                        else: break    
                                else:  break
                            else:
                                self.error = None
                                self._return_.append( () )

                        elif self._string_[ 0 ] in [ '[' ]:
                            self.error = ERRORS( self.line ).ERROR1('a list')
                            break

                        elif self._string_[ 0 ] in [ '{' ]:
                            self.error = ERRORS( self.line ).ERROR1('a dictionary')
                            break

                        elif self._string_ in [ 'True', 'False' ]:
                            self.num = boolean.BOOLEAN(self._string_, self.data_base, self.line).BOOLEAN()
                            self._return_.append( self.num )

                        elif self._string_ in [ 'inf' ]:
                            self.num, self.error = real.REAL(self._string_, self.data_base,
                                                                                    self.line).REAL()
                            if self.error is None: self._return_.append(self.num)
                            else:   break

                        elif self._string_ in [ 'None' ]:
                            self._return_.append( None )
                        else:
                            self.error = ERRORS( self.line ).ERROR0( self.master )
                            break
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.master )
                        break
            else:  pass
        else:
            self.error = None
            self._return_ = self._return_

        return  tuple( self._return_ ), self.error

class ERRORS:
    def __init__(self, line ):
        self.line           = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str = 'a list'):
        error = '{}{}. {}line: {}{}'.format(self.red, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}tuple {}object cannot contains '.format(self.cyan, self.white) + error

        return self.error+self.reset




