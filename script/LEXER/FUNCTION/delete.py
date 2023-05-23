
from script                                     import control_string
from script.LEXER                               import particular_str_selection
from script.PARXER.VAR_NAME                     import get_var_name
from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from CythonModules.Windows                      import fileError    as fe


class DELETE:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.selection          = particular_str_selection
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.get_val            = get_var_name
        self.variables          = self.data_base[ 'variables' ][ 'vars' ]
        self._values_           = self.data_base[ 'variables' ][ 'values' ]
        self.global_vars        = self.data_base[ 'global_vars' ][ 'vars' ]
        self.global_values      = self.data_base[ 'global_vars' ][ 'values' ]

    def DELETE(self, main_string: str):
        self.error              = None
        self.normal_string      = 'delete ' + self.master
        self.type1              = [ type( list() ), type( str() ),type( int() ),type( float() ),type( complex() ),
                                    type( bool() ), type( dict() ), type( tuple() ), type(None) ]
        self.type2              = [type( tuple())]

        self.list_of_values, self.error = self.selection.SELECTION( self.master, self.master,
                                                            self.data_base, self.line).CHAR_SELECTION( ',' )
        if self.error is None:
            for i, name in enumerate( self.list_of_values ):
                self.name, self.error = self.control.DELETE_SPACE( name )
                if self.error is None:
                    self.name, self.error = self.get_val.GET_VAR(self.name, self.data_base, self.line).GET_VAR()
                    if self.error is None:  self.list_of_values[ i ] = self.name
                    else: break
                else:
                    self.error = ERRORS( self.line ).ERROR0( self.normal_string )
                    break
        else: pass

        if self.error is None:
            for i, name in enumerate( self.list_of_values ):
                if type( name ) == type( str() ):
                    if name in self.variables:
                        self.idd = self.variables.index( name )
                        self.object_value = self._values_[ self.idd ]
                        self.type = type( self.object_value )

                        del self.variables[ self.idd ]
                        del self._values_[ self.idd ]

                        if self.global_vars:
                            if name in self.global_vars:
                                self.idd = self.global_vars.index( name )
                                del self.global_vars[ self.idd ]
                                del self.global_values[ self.idd ]
                            else: pass
                        else:  pass
                    else:
                        self.error = ERRORS( self.line ).ERROR3( name )
                        break

                elif type( name ) == type( list() ):
                    self._name_     = name[ 0 ][ 'name' ]
                    self.info       = name[ 0 ][ 'info' ]
                    self.len        = len( self.info )
                    self.idd        = self.variables.index( self._name_ )
                    self.__values__ = self._values_[ self.idd ]
                    self.type       = type( self.__values__ )

                    if self.len <= 2:
                        if self.len == 1:
                            self.error = FIRST_CASE( self.info[ 0 ], self.data_base, self.line).FIRST( self.__values__ )
                            if self.error is None:  pass
                            else: break
                        else:
                            self.error = SECOND_CASE(self.info , self.data_base, self.line).SECOND_CASE( self.__values__ )
                            if self.error is None: pass
                            else:  break

                        if self.global_vars:
                            if self._name_ in self.global_vars:
                                self._idd_ = self.global_vars.index( self._name_ )
                                self.global_values[ self._idd_ ] = self._values_[ self.idd ]
                            else: pass
                        else: pass
                    else: self.error = ERRORS( self.line ).ERROR0( main_string )
        else: pass

        return self.error

class FIRST_CASE:
    def __init__(self, master: any, data_base:dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.te                 = bm.init.bold + bm.fg.rbg(255,0,255)

    def FIRST(self, value: any):
        self.error              = None
        self.value              = value
        self.type               = type( self.value )

        if type( self.master ) == type( int() ):
            if self.type == type(list()):
                try: del self.value[ self.master ]
                except IndexError:
                    self.error = ERRORS(self.line).ERROR2()
            else: self.error = ERRORS(self.line).ERROR1(self.value, 'a list()')

        elif type( self.master ) == type( str() ):
            if self.type == type( dict() ):
                try: del self.value[ self.master ]
                except KeyError:
                    self.error = ERRORS(self.line).ERROR4(self.__values__, self.info[0])
            else: self.error = ERRORS(self.line).ERROR1( self.value, 'a dictionary()' )

        elif type( self.master ) == type( list() ):
            self.master = sorted(self.master, reverse = True )
            print( self.master)

            for _value_ in self.master :
                try: del self.value[ _value_ ]
                except IndexError:
                    self.type = type( self.value )
                    if self.type == type( tuple() ):
                        self.error = ERRORS( self.line ).ERROR2( 'tuple', self.te )
                        break
                    elif self.type == type( list() ):
                        self.error = ERRORS(self.line).ERROR2()
                        break
                    else:
                        self.error = ERRORS(self.line).ERROR2()
                        break
                except TypeError:
                    self.error = ERRORS(self.line).ERROR1(self.value, 'a list()')
                    break
        else: self.error = ERRORS( self.line ).ERROR0( self.value )

        return self.error

class SECOND_CASE:
    def __init__(self, master: any, data_base:dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.te                 = bm.init.bold + bm.fg.rbg(255,0,255)

    def SECOND_CASE(self, value: any):
        self.error              = None
        self.value              = value
        self.type               = type( self.value )
        self.master1            = self.master[ 0 ]
        self.master2            = self.master[ 1 ]

        self.list_selection = []

        if type( self.master1 ) == type( int() ):
            if self.type == type( list() ):
                try: self.list_selection.append(self.value[ self.master1 ])
                except IndexError:
                    self.error = ERRORS(self.line).ERROR2()
            else: self.error = ERRORS(self.line).ERROR1(self.value, 'a list()')

        elif type(self.master1 ) == type( str() ):
            try:
                self.list_selection.append(self.value[ self.master1 ])
            except KeyError:
                self.error = ERRORS( self.line ).ERROR4(self.value, self.master1 )
            except TypeError:
                self.error = ERRORS( self.line ).ERROR1(self.value, 'a dictionary()')

        elif type(self.master1 ) == type( list() ):
            for _value_ in self.master1:
                try:
                    self.list_selection.append(self.value[ _value_ ])
                except TypeError:
                    self.error = ERRORS( self.line ).ERROR1(self.value, 'a list()')
                    break
                except IndexError:
                    self.type = type( self.value )
                    if self.type == type( list() ):
                        self.error = ERRORS(self.line).ERROR2()
                        break
                    elif self.type == type( tuple() ):
                        self.error = ERRORS(self.line).ERROR2('tuple', self.te)
                        break
                    else:
                        self.error = ERRORS(self.line).ERROR2()
                        break

        if self.error is None:
            for j, _value_ in enumerate( self.list_selection ):

                if type( self.master2 ) in [ type(list()) ]:
                    self.master2 = sorted(self.master2, reverse = True )
                else:
                    self.master2 = self.master2
                    if type( self.master2 ) == type( int() ):
                        if type( _value_ ) == type( list() ):
                            try:
                                del _value_[ self.master2 ]
                            except IndexError:
                                self.error = ERRORS( self.line ).ERROR2()
                                break
                        else:
                            self.error = ERRORS(self.line).ERROR1(self.value, 'a list()')
                            break

                    elif type( self.master2 ) == type( str() ):
                        try:
                            del _value_[ self.master2 ]
                        except KeyError:
                            self.error = ERRORS( self.line ).ERROR4( _value_, self.master2 )
                        except TypeError:
                            self.error = ERRORS( self.line) .ERROR1( _value_, 'a dictionary()')

                    elif type( self.master2 ) == type( list() ):
                        for w in self.master2:
                            try:
                                del _value_[ w ]
                            except TypeError:
                                self.error = ERRORS(self.line).ERROR1(_value_, 'a list()')
                                break
                            except IndexError:
                                self.type = type( _value_ )
                                if self.type == type(list()):
                                    self.error = ERRORS(self.line).ERROR2()
                                    break
                                elif self.type == type(tuple()):
                                    self.error = ERRORS(self.line).ERROR2('tuple', self.te)
                                    break
                                else:
                                    self.error = ERRORS(self.line).ERROR2()
                                    break
        else: pass

        return  self.error

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

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError').Errors()+'{} invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error
        return self.error+self.reset

    def ERROR1(self, string: str, _char_ = 'an integer()' ):
        error = '{}is not {}{} {}type. {}line: {}{}'.format(self.white, self.blue, _char_, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError').Errors()+'{}<< {} >> '.format(self.cyan, string) + error
        return self.error+self.reset

    def ERROR2(self, func = 'list', c:str = ""):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'IndexError').Errors()+'{}{} {}index {}out of range. '.format(self.yellow,
                                                func, self.cyan, self.white) + error
        return self.error+self.reset

    def ERROR3(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError').Errors()+'{}{} '.format(self.cyan,  string) + error
        return self.error+self.reset
    
    def ERROR4(self, string: str, key: str):
        error = '{}was not found in {}<< {} >>. {}line: {}{}'.format(self.white, self.red, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'KeyError').Errors()+'{}{} '.format(self.cyan,  key) + error
        return self.error+self.reset