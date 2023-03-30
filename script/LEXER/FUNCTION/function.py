from script                     import control_string
from script.LEXER               import particular_str_selection
from script.LEXER.segmentation  import ERROR
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from CythonModules.Windows      import fileError    as fe

class FUNCTION:
    def __init__(self, master: list, data_base: dict, line: int):
        self.__str          = particular_str_selection
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.accepted_chars = self.control.LOWER_CASE()+self.control.LOWER_CASE()+['_']
    
    def FUNCTION_INIT(self, main_string: str, method = '1st', _type_ = 'direct'):
        self.type           = ['none', 'integer', 'float', 'boolean', 'complex', 'list', 'tuple', 
                               'dictionary', 'string', 'range', "None", 'any', 'ndarray', 'table']
        self.master         = self.master[ 0 ]
        self.master, _e_    = self.control.DELETE_SPACE( self.master )
        self.error          = None
        self.left           = 0
        self.right          = 0
        self.key            = None
        self.string         = ''
        self.tru_string     = ''
        self.function_name  = None
        self.args           = None
        self.index          = 0
        self.count          = 0
        self.data_storage   = []
        self.variable       = []
        self._type_         = []
        self.last_parent    = 0
        self.anonymous      = False
        self._sep_          = " "
        self._sep_1         = ":"
        self.function_info  = {
            'type'                      : 'any', # items type
            'value'                     : None,  # default values issigned 
            'arguments'                 : None,  # item names
            'function_name'             : None,  # function name
            'history_of_data'           : None,  # history of commands typed
            'sub_functions'             : [],    # list to stored a sub-function 
            'function_info'             : {
                'args'                  : None,  # function items
                'typeVars'              : None,  # items type
                'defaultValues'         : None,  # defualt values
                'description'           : None   # description of function using <begin> inside function
            },
            'type_return'               : None,  # type returning, default value None( for any type)
            "anonymous"                 : False  # anonymous function
        }

        self.string_type  = self.__str.SELECTION(self.master, self.master, self.data_base, self.line)
        self.function_type, self.error  = self.string_type.CHAR_SELECTION( '->' )
        if   len(self.function_type) == 1: pass
        elif len(self.function_type) == 2: 
            self._types_, self.err = self.control.DELETE_SPACE( self.function_type[ 1 ] )
            if self.err is None:
                self.master, self.err = self.control.DELETE_SPACE( self.function_type[ 0 ] )
                if self.err is None: 
                    if self._types_ in self.type: self.function_info['type_return'] = self._types_
                    else: self.error = ERRORS(self.line).ERROR6()
                else: self.error = ERRORS(self.line).ERROR0( main_string )
            else: self.error = ERRORS(self.line).ERROR0( main_string )
        else:self.error = ERRORS(self.line).ERROR0( main_string )
        
        if self.error is None:
            if self.master[ -1 ] == ')':
                for i, str_ in enumerate( self.master ):
                    self.left, self.right = self.left + str_.count('('), self.right + str_.count(')')

                    if self.left != self.right:
                        if self.count == 0:
                            if self.string:
                                self.index  = i
                                self.string = ''
                        else:
                            self.error =  ERRORS( self.line ).ERROR0( main_string )
                            break
                    elif self.left == self.right and str_ == ')': 
                        self.count += 1
                        self.last_parent = i
                    elif self.left == self.right :
                        if self.count == 0:
                            self.string     += str_
                            self.tru_string = self.string
                        else:
                            self.error = ERRORS( self.line ).ERROR0( main_string )
                            break
                
                self.string = self.tru_string

                if self.error is None:
                    if not self.string: self.error = ERRORS( self.line ).ERROR0( main_string )
                    else:
                        self.name, self.error = self.control.CHECK_NAME( self.string )
                        if self.error is None:
                            if self.name == "initialize":
                                if self.function_info['type_return']:
                                    if self.function_info['type_return']  in ["None", "none"]: pass 
                                    else: self.error = ERRORS( self.line ).ERROR7( )
                                else: pass
                            else: pass 
                            if self.error is None:
                                self.function_name                      = self.name
                                self.function_info[ 'function_name' ]   = self.function_name
                                self.data_base[ 'current_func' ]        = self.function_name
                            else: pass
                        else: self.error = ERRORS( self.line ).ERROR1( self.string )

                    if self.error is None:
                        self.master_right       = self.master[self.index : ]
                        self.main_              = self.master_right[1 : -1]
                        self.main_, self.error  = self.control.DELETE_SPACE( self.main_ )

                        if self.error is None:
                            self.string_select  = self.__str.SELECTION(self.main_, self.main_, self.data_base, self.line)
                            self.value, self.error  = self.string_select.CHAR_SELECTION( ',' )
                            if self.error is None:
                                if len(self.value) == 1  and self.value[0] == "anonymous": self.anonymous = True
                                else:
                                    for val in self.value:
                                        self.string_select = self.__str.SELECTION(val, val, self.data_base, self.line)
                                        self.sub_value, self.error = self.string_select.CHAR_SELECTION( '=' )

                                        if self.error is None:
                                            if len( self.sub_value ) == 2:
                                                self.arg_ , self.error = self.control.DELETE_SPACE( self.sub_value [ 0 ] )
                                                if self.error is None:
                                                    self.sub_value_, self.error = self.__str.SELECTION( self.arg_, self.arg_,
                                                                            self.data_base, self.line).CHAR_SELECTION( ':' )
                                                    
                                                    if self.error is None:
                                                        if   len( self.sub_value_ ) == 1:
                                                            self.name, self.error = self.control.DELETE_SPACE( self.sub_value_[ 0 ] )
                                                            if self.error is None:
                                                                self.name, self.error = self.control.CHECK_NAME( self.name )
                                                                if self.error is None:
                                                                    self.variable.append( self.name )
                                                                    self._type_.append( [ 'any' ] )
                                                                else:
                                                                    self.name = self.sub_value_[ 0 ]
                                                                    self.error = self.error = ERRORS( self.line ).ERROR4( self.name )
                                                                    break
                                                            else:
                                                                self.error = ERRORS(self.line ).ERROR0( val )
                                                                break
                                                        elif len( self.sub_value_ ) == 2:
                                                            if _type_ in [ 'direct' ]:
                                                                self.name, self.error = self.control.DELETE_SPACE(
                                                                                                            self.sub_value_[ 0 ])
                                                                if self.error is None:
                                                                    self.name, self.error = self.control.CHECK_NAME( self.name )
                                                                    if self.error is None:
                                                                        self.type, self.error = self.control.DELETE_SPACE( self.sub_value_[ 1 ] )
                                                                        if self.error is None:
                                                                            self.type, self.error = self.__str.SELECTION( self.type, self.type,
                                                                                            self.data_base, self.line).CHAR_SELECTION( self._sep_ )
                                                                           
                                                                            if self.error is None:
                                                                                self.is_true, self.new_type = [], []
                                                                                for s, typ in enumerate( self.type ):
                                                                                    if typ:
                                                                                        self.is_true.append(True)
                                                                                        typ, self.error = self.control.DELETE_SPACE( typ )
                                                                                        if self.error is None:
                                                                                            w, self.error = FUNCTION( val, self.data_base,
                                                                                                                    self.line ).TYPE( typ )
                                                                                            self.new_type.append(w)
                                                                                            if self.error is None: pass 
                                                                                            else: break 
                                                                                        else:
                                                                                            self.error = ERRORS( self.line ).ERROR0( val )
                                                                                            break
                                                                                    else: pass
                                                                                if self.error is None:
                                                                                    if self.is_true:
                                                                                        self.type = self.new_type.copy()
                                                                                        self.variable.append( self.name )
                                                                                        self._type_.append( self.type )
                                                                                    else:
                                                                                        self.error = ERRORS( self.line ).ERROR0( main_string )
                                                                                        break
                                                                                else: break
                                                                            else: break
                                                                        else:
                                                                            self.error = ERRORS( self.line ).ERROR0( val )
                                                                            break
                                                                    else:
                                                                        self.name = self.sub_value_[ 0 ]
                                                                        self.error = self.error = ERRORS( self.line ).ERROR4( self.name )
                                                                        break
                                                                else:
                                                                    self.error = ERRORS( self.line ).ERROR0( val )
                                                                    break
                                                            else:
                                                                self.error = ERRORS( self.line ).ERROR5( val )
                                                                break
                                                        else:
                                                            self.error = ERRORS( self.line ).ERROR0( val )
                                                            break

                                                        if self.error is None:
                                                            self.val_, self.error = self.control.DELETE_SPACE( self.sub_value[ 1 ] )
                                                            if self.error is None: self.data_storage.append( self.val_ )
                                                            else:
                                                                self.error = ERRORS( self.line ).ERROR0( val )
                                                                break
                                                        else: break
                                                    else:
                                                        self.error = ERRORS( self.line ).ERROR0( val )
                                                        break
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR0( val )
                                                    break

                                            elif len( self.sub_value ) == 1:
                                                self.arg_   = None
                                                self.val_, self.error = self.control.DELETE_SPACE( self.sub_value[ 0 ] )

                                                if self.error is None:
                                                    self.string_select_ = self.__str.SELECTION(self.val_, self.val_,
                                                                                                    self.data_base, self.line)
                                                    self.sub_value_, self.error = self.string_select_.CHAR_SELECTION( ':' )

                                                    if self.error is None:
                                                        if len( self.sub_value_ ) == 1:
                                                            self.val_, self.error = self.control.DELETE_SPACE( self.sub_value_[ 0 ] )
                                                            if self.error is None:
                                                                if _type_ in [ 'direct' ]:        
                                                                    self.name, self.error = self.control.CHECK_NAME( self.val_ )
                                                                elif _type_ in [ 'indirect' ]:
                                                                    self.name   = self.val_
                                                                    self.error  = None

                                                                if self.error is None:
                                                                    self.data_storage.append( None )
                                                                    self.variable.append( self.name )
                                                                    self._type_.append( [ 'any' ] )
                                                                else:
                                                                    self.error = ERRORS( self.line ).ERROR4( self.val_ )
                                                                    break
                                                            else:
                                                                self.error = ERRORS( self.line ).ERROR0( val )
                                                                break

                                                        elif len( self.sub_value_ ) == 2:
                                                            if _type_ in [ 'direct' ]:
                                                                self.type, self.error = self.control.DELETE_SPACE( self.sub_value_[ 1 ])
                                                                
                                                                if self.error is None:
                                                                    self._typ_  = self.__str.SELECTION(self.type, self.type, self.data_base, self.line)
                                                                    self.type, self.error = self._typ_.CHAR_SELECTION( self._sep_ )
                                                                    
                                                                    if self.error is None:
                                                                        self.is_true, self.new_type = [], []
                                                                        for s, typ in enumerate( self.type ):
                                                                            if typ:
                                                                                self.is_true.append(True)
                                                                                typ, self.error = self.control.DELETE_SPACE( typ )
                                                                                if self.error is None:
                                                                                    w, self.error = FUNCTION(val, self.data_base, self.line ).TYPE( typ )
                                                                                    self.new_type.append(w)
                                                                                    if self.error is None: pass 
                                                                                    else: break
                                                                                else:
                                                                                    self.error  = ERRORS( self.line ).ERROR0( val )
                                                                                    break
                                                                            else: pass  
                                                                        if self.error is None:
                                                                            if self.is_true:
                                                                                self.type = self.new_type.copy()
                                                                                self.val_, self.error = self.control.DELETE_SPACE( self.sub_value_[ 0 ])
                                                                                if self.error is None:    
                                                                                    self.name, self.error = self.control.CHECK_NAME( self.val_ )
                                                                                                                                
                                                                                    if self.error is None:
                                                                                        self.data_storage.append( None )
                                                                                        self.variable.append( self.name )
                                                                                        self._type_.append( self.type )
                                                                                    else:
                                                                                        self.error = self.error = ERRORS( self.line ).ERROR4( self.val_ )                                      
                                                                                        break
                                                                                else:
                                                                                    self.error  = ERRORS( self.line ).ERROR0( val )
                                                                                    break
                                                                            else: 
                                                                                self.error  = ERRORS( self.line ).ERROR0( main_string )
                                                                                break
                                                                        else: break
                                                                    else: break
                                                                else: 
                                                                    self.error = ERRORS( self.line ).ERROR0( val )
                                                                    break
                                                            else:
                                                                self.error = ERRORS( self.line ).ERROR5( val )
                                                                break
                                                        else:
                                                            self.error = ERRORS( self.line ).ERROR0( val )
                                                            break
                                                    else:
                                                        self.error  = ERRORS( self.line ).ERROR0( val )
                                                        break
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR0( val )
                                                    break
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( val )
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( val )
                                            break
                            else: pass
                        else:
                            self.error = None
                            self.data_storage.append( None )
                            self.variable.append( None )
                            self._type_.append( 'any' )
                    else: pass

                    if self.anonymous is False:
                        self.function_info[ 'value' ]       = self.data_storage
                        self.function_info[ 'type' ]        = self._type_
                        self._variable_                     = []
                        
                        self.function_info[ 'function_info' ]['VarsType']       = self._type_.copy()
                        self.function_info[ 'function_info' ]['defaultValues']  = self.data_storage.copy()
                        
                        if _type_ in [ 'direct' ]:
                            for name in self.variable:
                                if name in self._variable_:
                                    if name == None: self._variable_.append( name )
                                    else:
                                        self.error = ERRORS( self.line ).ERROR3( main_string, name )
                                        break
                                else: self._variable_.append( name )
                            if self.error is None: self.function_info[ 'arguments' ]   = self._variable_
                            else: self.error = self.error
                        else: self.function_info[ 'arguments' ] = self.variable

                        try:  self.function_info[ 'function_info' ]['args']  = self.function_info[ 'arguments' ].copy()
                        except AttributeError:  self.function_info[ 'function_info' ]['args']   = self.function_info[ 'arguments' ]
                    else:
                        self.function_info['anonymous']     = self.anonymous 
                        self.function_info[ 'arguments' ]   = [None]
                        self.function_info['value']         = [None]
                else: pass
            else: self.error = ERRORS( self.line).ERROR0( main_string )

            if self.error is None:
                if self.function_info[ 'function_name' ] in [ 'function', 'func' ]:
                    if method == '1st':
                        self.error = ERRORS( self.line ).ERROR1( self.function_info[ 'function_name' ])
                    else: pass
                else: pass
            else:pass
        else: pass 
            
        return self.function_info, self.error

    def TYPE(self, string: str):
        self.string, self.error = self.control.DELETE_SPACE( string )
        self.type   = ['int', 'float', 'list', 'tuple', 'bool', 'cplx', 'dict', 'string', 'any', 'none', 'range', 'ndarray', 'table',
                       'p_int', 'n_int', 'p_float', 'n_float', 'double', 'p_double', 'n_double']
        self.error  = None

        if self.error is None :
            if self.string in self.type: pass
            else: self.error = ERRORS( self.line ).ERROR2( self.master )
        else:self.error = ERRORS( self.line ).ERROR0( self.master )

        return self.string, self.error

    def LAST_CHECK(self, main_string: str):

        self.error      = None
        self.value      = self.master[ 'value' ]
        self.key        = False
        self.count      = 0

        for val in self.value:
            if val == None: self.key = True
            else: self.count += 1

            if self.key == True and val != None:
                self.error = ERRORS( self.line ).ERROR0( main_string )
                break
            else: pass

        return self.master, self.error

class ERRORS:
    def __init__(self, line: int):
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
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ ': invalid syntax in {}<< {} >>. '.format(self.cyan, string) + error
        return self.error+self.reset

    def ERROR1(self, string: str):
        self._str_ = '{}type {}help( {}function_name{} ) {} for more informations. '.format(self.white, self.magenta, self.yellow, self.magenta,
                                                                                            self.white)
        error = '{}in {}<< {} >> .{}line: {}{}.\n{}'.format(self.white, self.green, string, self.white, self.yellow, self.line, self._str_)
        self.error = fe.FileErrors( 'NameError' ).Errors()+ '{}function name {}ERROR '.format(self.white, self.yellow) + error
        return self.error+self.reset

    def ERROR2(self, string: str):
        self._str_ = '{}type {}help( {}var_type{} ) {} for more informations. '.format(self.white, self.magenta, self.yellow, self.magenta,
                                                                                            self.white)
        error = '{}in {}<< {} >> .{}line: {}{}.\n{}'.format(self.white, self.green, string, self.white, self.yellow, self.line, self._str_)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}variable type {}ERROR '.format(self.white, self.yellow) + error

        return self.error+self.reset

    def ERROR3(self, string: str, name: str):
        error = '{}due to {} duplicated argument {}<< {} >>. {}line: {}{}.'.format(self.white, self.magenta, self.red, name, self.white,
                                                                                   self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'invalid syntax in {}<< {} >> '.format(self.cyan, string) + error
        
        return self.error+self.reset

    def ERROR4(self, string: str):
        self._str_ = '{}type {}help( {}arg_name{} ) {} for more informations. '.format(self.white, self.magenta, self.yellow, self.magenta,
                                                                                            self.white)
        error = '{}in {}<< {} >> .{}line: {}{}.\n{}'.format(self.white, self.green, string, self.white, self.yellow, self.line, self._str_)
        self.error = fe.FileErrors( 'NameError' ).Errors()+'{}argument name {}ERROR '.format(self.white, self.yellow) + error
        
        return self.error+self.reset

    def ERROR5(self, string: str):
        error = '{}due to {}<< : >>. {}line: {}{}'.format(self.white, self.green, self.white, self.yellow, self.line) 
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'invalid syntax in {}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR6(self):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line) 
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}returning {}type error. '.format(self.white, self.cyan) + error

        return self.error+self.reset
    
    def ERROR7(self):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line) 
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}Constructor {}type error. '.format(self.green, self.cyan) + error

        return self.error+self.reset