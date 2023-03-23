from script                     import control_string
from script.LEXER               import looking_for_bool_operators
from script.LEXER               import looking_for_logical_operators
from script.LEXER               import looking_for_arithmetic_operators
from script.LEXER               import looking_for_init_function
from script.LEXER               import looking_for_module_load
from script.PARXER.LEXER_CONFIGURE import lexer_and_parxer as LP
from script.LEXER               import particular_str_selection
from script.LEXER.FUNCTION      import global_
from script.LEXER.FUNCTION      import return_
from script.LEXER.FUNCTION      import class_
from script.LEXER.FUNCTION      import function
from script.LEXER.FUNCTION      import function_rebuild
from script.LEXER.FUNCTION      import delete
from script.LEXER.FUNCTION      import lambda_
from script.LEXER.FUNCTION      import print_value
from script.LEXER.FUNCTION      import transformation
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from CythonModules.Windows      import fileError    as fe 


class LEXER_ASSEMBLY:
    def __init__(self, master: dict, data_base: dict, line: int):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.boolean                = looking_for_bool_operators
        self.logical                = looking_for_logical_operators
        self.arithmetic             = looking_for_arithmetic_operators

    def ASSEMBLY(self):
        self.error                  = None
        self.store_data             = []
        self.store_bool_op          = []
        self.store_logical_op       = []
        self.store_arithmetic_op    = []

        for value in self.master['value']:
            self.store_data_, self.store_op_, self.error = self.boolean.BOOLEAN_OPERATORS(value, self.data_base,
                                                                                    self.line).BOOLEAN_OPAERATORS()
            if self.error is None:
                if not self.store_op_:
                    self.new_data                   = self.store_data_[ 0 ]
                    self.store_data.append( self.store_data_[ 0 ])
                    self.store_bool_op.append(None)
                    self.master['value']            = self.store_data
                    self.master['bool_operator']    = self.store_bool_op
                else:
                    self.store_data.append( self.store_data_ )
                    self.store_bool_op.append( self.store_op_ )
                    self.master['value']            = self.store_data
                    self.master['bool_operator']    = self.store_bool_op
            else: break

        if self.error is None:
            self.name_in_master = list(self.master.keys())

            if 'bool_operator' in self.name_in_master:
                self.storage_data   = []
                self.value          = self.master['value']

                for i, value in enumerate( self.value ):
                    self._value_, self._op_, self._op__ = [], [], []

                    if type( value ) == type( list() ):
                        for _val_ in value:
                            _val_ = _val_[1 : -1]

                            self.store_data_, self.store_op_, self.error = self.logical.LOGICAL_OPERATORS(_val_,
                                                                self.data_base, self.line).LOGICAL_OPAERATORS_INIT()

                            if self.error is None:
                                if not self.store_op_:
                                    self._op_.append( None )
                                    self.store_data__, self.store_op__, self.error = self.arithmetic.ARITHMETIC_OPERATORS(
                                        self.store_data_[ 0 ], self.data_base, self.line).ARITHMETIC_OPAERATORS_INIT()

                                    if self.error is None:
                                        if self.store_op__:
                                            self._value_.append( self.store_data__)
                                            self._op__.append( self.store_op__ )
                                        else:
                                            self._value_.append( self.store_data__ )
                                            self._op__.append( None )
                                    else: break
                                else:
                                    self._op_.append( self.store_op_ )
                                    self.store_d, self.store_o = [], []

                                    for main_value in self.store_data_:
                                        self.store_data__, self.store_op__, self.error = self.arithmetic.ARITHMETIC_OPERATORS(
                                                main_value, self.data_base, self.line).ARITHMETIC_OPAERATORS_INIT()

                                        if self.error is None:
                                            if self.store_op__:
                                                self.store_d.append( self.store_data__ )
                                                self.store_o.append( self.store_op__ )

                                            else:
                                                self.store_d.append( self.store_data__ )
                                                self.store_o.append( None )
                                        else: break
                                    if self.error is None:
                                        self._value_.append( self.store_d)
                                        self._op__.append( self.store_o )
                                    else: break
                            else: break
                    else:
                        self.store_data_, self.store_op_, self.error = self.logical.LOGICAL_OPERATORS(value,
                                                                self.data_base, self.line).LOGICAL_OPAERATORS_INIT()

                        if self.error is None:
                            if self.store_op_:
                                self._op_       = self.store_op_
                                for main_value in self.store_data_:

                                    self.store_data__, self.store_op__, self.error = self.arithmetic.ARITHMETIC_OPERATORS(
                                                     main_value, self.data_base, self.line).ARITHMETIC_OPAERATORS_INIT()

                                    if self.error is None:
                                        if self.store_op__:
                                            self._value_.append( self.store_data__ )
                                            self._op__.append( self.store_op__ )

                                        else:
                                            self._value_.append( self.store_data__[ 0 ] )
                                            self._op__.append( None )
                                    else: break
                            else:
                                self._op_     = None
                                self.store_data__, self.store_op__, self.error = self.arithmetic.ARITHMETIC_OPERATORS(
                                            self.store_data_[0], self.data_base, self.line).ARITHMETIC_OPAERATORS_INIT()

                                if self.error is None:
                                    if self.store_op__:
                                        self._value_                    = self.store_data__
                                        self._op__                      = self.store_op__
                                    else:
                                        self._value_                    = self.store_data__
                                        self._op__                      = None
                                else: break
                        else:  break

                    if self.error is None:
                        self.storage_data.append( self._value_ )
                        self.store_logical_op.append( self._op_ )
                        self.store_arithmetic_op.append( self._op__ )
                        self.master['value']                    = self.storage_data
                        self.master['logical_operator']         = self.store_logical_op
                        self.master['arithmetic_operator']      = self.store_arithmetic_op
                    else: break
            else:
                self.value                      = self.master['value']
                self.storage_data               = []

                for value in self.value:
                    self.store_data_, self.store_op_, self.error = self.logical.LOGICAL_OPERATORS(value, self.data_base,
                                                                                    self.line).LOGICAL_OPAERATORS_INIT()

                    if self.error is None:
                        self.store_bool_op.append( None )
                        self.master['bool_operator']            = self.store_bool_op

                        if self.store_op_:
                            self.store_logical_op.append( self.store_op_ )
                            self.master['logical_operator']     = self.store_logical_op

                            self.store_main_val                 = []
                            self.store_ar_op                    = []

                            for main_value in self.store_data_:
                                self.store_data__, self.store_op__, self.error = self.arithmetic.ARITHMETIC_OPERATORS(
                                                main_value, self.data_base, self.line).ARITHMETIC_OPAERATORS_INIT()

                                if self.error is None:
                                    if not self.store_op__:
                                        self.store_main_val.append( self.store_data__[0] )
                                        self.store_ar_op.append( None )
                                    else:
                                        self.store_main_val.append( self.store_data__ )
                                        self.store_ar_op.append( self.store_op__ )
                                else:  break
                            if self.error is None:
                                self.storage_data.append( self.store_main_val )
                                self.store_arithmetic_op.append( self.store_ar_op )
                                self.master['value']                = self.storage_data
                                self.master['arithmetic_operator']  = self.store_arithmetic_op
                            else: break
                        else:
                            self.store_logical_op.append( None )
                            self.master['logical_operator']                 = self.store_logical_op

                            self.store_data__, self.store_op__, self.error  = self.arithmetic.ARITHMETIC_OPERATORS(
                                            self.store_data_[ 0 ], self.data_base, self.line).ARITHMETIC_OPAERATORS_INIT()

                            if self.error is None:
                                if not self.store_op__:
                                    self.storage_data.append( self.store_data__[ 0 ] )
                                    self.store_arithmetic_op.append( None )
                                    self.master['value']                    = self.storage_data
                                    self.master['arithmetic_operator']      = self.store_arithmetic_op

                                else:
                                    self.storage_data.append( self.store_data__ )
                                    self.store_arithmetic_op.append( self.store_op__ )

                                    self.master['value']                    = self.storage_data
                                    self.master['arithmetic_operator']      = self.store_arithmetic_op
                            else: break
                    else:  break
        else:  pass

        return self.master, self.error

class FINAL_LEXER:

    def __init__(self, master:str, data_base: dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.class_             = class_
        self.global_            = global_
        self.return_            = return_
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.function_          = function
        self.mod_module         = looking_for_module_load
        self.mod_function       = looking_for_init_function
        self.rebuild_function   = function_rebuild

    def FINAL_LEXER(self, value: dict, _type_: str = None, _key_:bool=False, def_key:str='direct', class_key:str='direct', term: str = 'orion'):
        self.error              = None
        self.value              = value
        self.list_items         = list( self.value.keys() )
        self.type_accepted      = ['def', 'class', 'loop', 'conditional']

        self.main_lexer_storage = {
            'try'               : None,
            'def'               : None,
            'pass'              : None,
            'next'              : None,
            'exit'              : None,
            'break'             : None,
            'begin'             : None,
            'class'             : None,
            'print'             : None,
            'return'            : None,
            'delete'            : None,
            'global'            : None,
            'lambda'            : None,
            'if_egal'           : None,
            'continue'          : None,
            'all_data'          : None,
            'function'          : None,
            'sub_print'         : None,
            'module_import'     : None,
            'transformation'    : None

        }

        if 'operator' not in self.list_items:

            self.path_and_module, self.error = self.mod_module.FINAL_MODULE_LOAD(self.value, self.data_base,
                                                                                self.line).LOAD( self.master )
            if self.error is None:
                if type( self.path_and_module ) == type( str() ):
                    self.new_data, self.new_function, self.error = self.rebuild_function.FUNCTION(self.value,
                                                                    self.data_base, self.line).FUNCTION( self.master )
                    if self.error is None:
                        if self.new_function:
                            if self.new_function[ 0 ] in [ 'break', 'exit', 'pass', 'continue', 'next', 'try', 'begin' ]:
                                list_ = [ 'pass', 'continue', 'next' ]
                                if self.new_function[ 0 ] not in [ 'pass', 'continue', 'next', 'break', 'exit' ]:
                                    self.main_lexer_storage[ self.new_function[ 0 ] ] = True
                                else:
                                    if self.new_function[ 0 ] in list_ and _type_ in ['conditional'] :
                                        self.main_lexer_storage[ self.new_function[ 0 ] ]   = True
                                    elif self.new_function[ 0 ] in [ 'break', 'exit', 'pass', 'continue', 'next' ] and _type_ in [ 'loop' ]:
                                        self.main_lexer_storage[ self.new_function[ 0 ] ] = True
                                    elif self.new_function[ 0 ] in [ 'pass' ] and _type_ in ['class', 'def', 'conditional', 'loop']:
                                         self.main_lexer_storage[ self.new_function[ 0 ] ] = True
                                    else: self.error = ERRORS( self.line ).ERROR0( self.master )

                            elif self.new_function[ 0 ] in [ 'global' ]:
                                self._global_, self.error = self.global_.GLOBAL( self.master, self.data_base,
                                                                                self.line).GLOBAL( self.new_data[ 0 ] )
                                if self.error is None:
                                    self.main_lexer_storage[ 'global' ] = self._global_
                                else: pass

                            elif self.new_function[ 0 ] in [ 'return' ]:
                                if _type_ in self.type_accepted:
                                    self._return_, self.error = self.return_.RETURN(self.master, self.data_base,
                                                                                    self.line).RETURN( self.new_data[ 0 ] )
                                    
                                    if self.main_lexer_storage[ 'return' ] is None:
                                        if self.error is None: self.main_lexer_storage[ 'return' ] = self._return_
                                        else: pass
                                    else: self.error = ERRORS( self.line ).ERROR3( )
                                else: self.error = ERRORS( self.line ).ERROR0( self.master )

                            elif self.new_function[ 0 ] in [ 'class' ] :
                                self._class_, self.error = self.class_.CLASS( self.new_data, self.data_base,
                                                                              self.line).CLASS_INIT( self.master )
                                if self.error is None: self.main_lexer_storage[ 'class' ] = self._class_
                                else: pass

                            elif self.new_function[ 0 ] in [ 'def' ]   :
                                self._function_, self.error = self.function_.FUNCTION( self.new_data, self.data_base,
                                                            self.line).FUNCTION_INIT( self.master,_type_ = def_key )
                                if self.error is None: self.main_lexer_storage[ 'def' ] = self._function_
                                else: pass

                            elif self.new_function[ 0 ] in [ 'delete' ]:
                                self.error = delete.DELETE( self.new_data[ 0 ], self.data_base,
                                                                                self.line ).DELETE( self.master )
                                if self.error is None: self.main_lexer_storage[ 'delete' ] = True
                                else: pass

                            elif self.new_function[ 0 ] in [ 'print' ] :
                                self.get_values, self.error = print_value.PRINT( self.new_data[ 0 ], self.data_base,
                                                                                self.line ).PRINT( _key_, term)
                                if self.error is None: self.main_lexer_storage[ 'print' ] = self.get_values
                                else: pass

                            elif self.new_function[ 0 ] in [ '_int_', '_float_', '_complex_', '_string_', '_length_',
                                                '_boolean_', '_list_', '_tuple_', '_dictionary_', '_sqrt_', '_sum_',
                                                '_rang_', '__ansii__', '__show__', '__rand__', '_get_line_', '_mean_',
                                                '__scan__','_max_', '_min_', '_var_', '_std_','__open__', '__maths__', '__prompt__' ]:
                                self.get_values, self.error = transformation.C_F_I_S( self.new_data[ 0 ], self.data_base,
                                                                    self.line ).FUNCTION(self.new_function[ 0 ] )
                                if self.error is None:
                                    if self.new_function[ 0 ] in ['__show__']: 
                                        self.main_lexer_storage[ 'sub_print' ]      = self.get_values
                                    else:
                                        self.main_lexer_storage[ 'transformation' ] = self.get_values
                                else: pass
                            elif self.new_function[ 0 ] in [ 'lambda' ]: self.error = ERRORS( self.line ).ERROR0(self.master)
                            else:
                                self.new_data = FINAL_LEXER( self.new_data, self.data_base, self.line).REBUILD()
                                self.value_ = {'value' : self.new_data}

                                self.final_value, self.error = LEXER_ASSEMBLY(self.value_, self.data_base, self.line).ASSEMBLY()
                                if self.error is None:
                                    self.main_lexer_storage[ 'all_data' ] = self.final_value
                                    self.main_lexer_storage[ 'function' ] = self.new_function[0]
                                else: pass

                        else:
                            self.final_value, self.error = LEXER_ASSEMBLY(self.value, self.data_base, self.line).ASSEMBLY()
                            if self.error is None:  self.main_lexer_storage['all_data'] = self.final_value
                            else: pass
                    else: pass
                else:
                    if self.error is None:
                        self.main_lexer_storage[ 'module_import' ]    = self.path_and_module
                    else: pass
            else: pass
        else:
            self.main_lexer_storage, self.error = FINAL_LEXER(self.master, self.data_base,
                                                    self.line).SCANNER( self.value, self.main_lexer_storage )
        return self.main_lexer_storage, self.error

    def REBUILD(self):
        self.string     = ''

        for i, str_ in enumerate( self.master ):
            if len(self.master) == 1: self.string = str_
            else:
                if i < len( self.master ) - 1: self.string = self.string + str_ + ' '
                else: self.string += str_

        return [ self.string ]

    def SCANNER(self, value: dict, main_lexer_storage: dict ):
        self.error                  = None
        self.value                  = value
        self.main_lexer_storage     = main_lexer_storage
       
        self.path_and_module, self.error = self.mod_module.FINAL_MODULE_LOAD(self.value, self.data_base, self.line).LOAD( self.master )
        if self.error is None:
            if type( self.path_and_module ) != type( str() ):
                self.error = ERRORS( self.line ).ERROR0( self.master )

            else:
                self.new_data, self.new_function, self.error = self.rebuild_function.FUNCTION( self.value,
                                                         self.data_base, self.line).FUNCTION( self.master )
                
                if self.error is None:
                    
                    if self.new_function  : 
                        if  self.new_function[0] == "lambda": pass 
                        else: self.error = ERRORS( self.line ).ERROR0( self.master ) 
                    else: pass 
                    
                    if self.error is None:
                        self.func           = 'func'
                        self.lam            = 'lambda'
                        self.fun_value      = self.value[ 'value' ]
                        self.list_items     = self.value[ 'variable' ]
                    
                        self.len            = len( self.func )
                        self.len_lambda     = len( self.lam ) 

                        if len( self.list_items ) == 1:
                            self.string = self.fun_value[ 0 ]
                            if self.string[0] == 'f': pass 
                            else: self.len = self.len_lambda 
                            try:
                                if len( self.string ) > self.len:
                                    self.root = self.string[ : self.len ]
                                    self.nex_root = self.string[self.len:]
                                    self.root, err = self.control.DELETE_SPACE( self.root )
                                    self.nex_root, err = self.control.DELETE_SPACE( self.nex_root )
                                    
                                    if err is None:
                                        if   self.root == self.func:
                                            if self.nex_root[ 0 ] == '(':
                                                if self.string[ -1 ] == ':':

                                                    self.string , err = self.control.DELETE_SPACE( self.string[ : -1 ] )
                                                    self.new_data = [ self.string ]

                                                    self._function_, self.error = self.function_.FUNCTION( self.new_data,
                                                        self.data_base,self.line).FUNCTION_INIT( self.string, method='2nd' )

                                                    if self.error is None:
                                                        self.name, self.error   = self.control.DELETE_SPACE(
                                                                            self._function_[ 'function_name' ] )
                                                        if self.error is None:
                                                            self.name               = self.control.CHECK_NAME( self.name )
                                                            self._function_[ 'function_name' ]      = self.value[ 'variable' ][ 0 ]
                                                            self.data_base[ 'current_func' ]        = self.value[ 'variable' ][ 0 ]
                                                            self.main_lexer_storage[ 'def' ]        = self._function_

                                                            del self.value[ 'variable' ]
                                                            del self.value[ 'operator' ]

                                                        else: self.error = ERRORS( self.line ).ERROR2( self.name )
                                                    else: pass
                                                else: self.error = ERRORS( self.line ).ERROR1( self.master )
                                            else:
                                                if self.string[ self.len + 1] in ['[', '{', '"', "'"]:
                                                    self.error = ERRORS( self.line ).ERROR0( self.master)

                                                else:
                                                    self.final_value, self.error = LEXER_ASSEMBLY( self.value, self.data_base,
                                                                                                        self.line).ASSEMBLY()
                                                    if self.error is None:
                                                        self.main_lexer_storage[ 'if_egal' ]    = True
                                                        self.main_lexer_storage[ 'all_data' ]   = self.final_value
                                                    else: pass
                                        elif self.root == self.lam:
                                            if self.string[self.len] == " ":
                                                self.__str          = particular_str_selection
                                                self.string_select = self.__str.SELECTION(self.master, self.master, self.data_base, self.line)
                                                self.sub_value, self.error = self.string_select.CHAR_SELECTION( '=' )
                    
                                                if self.error is None:
                                                    if len( self.sub_value ) == 2:
                                                        self.name, self.error = self.control.CHECK_NAME(self.sub_value[0])
                                                        if self.error is None:
                                                            self.list_vars_lambda, self.type_return, self.error = lambda_.LAMBDA( self.data_base, self.line).LAMBDA( self.nex_root )         
                                                            if self.error is None:    
                                                                self.new_string =  self.name + " += " + self.list_vars_lambda[1]
                                                                self.lex, self.error = LP.MAIN(self.new_string, self.data_base, self.line).MAIN_LEXER()
                                                                
                                                                if self.error is None: 
                                                                    if self.name not in self.list_vars_lambda[0]:
                                                                        self.range = range( len( self.list_vars_lambda[0] )  )
                                                                        self.my_lambda_function = {
                                                                            f"{self.name}" : {
                                                                                'type'     : [ ['any'] for x in self.range ],
                                                                                'value'    : [ None for x in self.range ],
                                                                                'arguments': [ x for x in self.list_vars_lambda[0] ],
                                                                                'history_of_data'   : [
                                                                                        (f"treturn {self.list_vars_lambda[1]}                        ",True),
                                                                                        ( "end:                                                   ", False )
                                                                                    ],
                                                                                'sub_functions'  : [],
                                                                                'function_info'             : {
                                                                                    'args'                  : None,  
                                                                                    'typeVars'              : None,   
                                                                                    'defaultValues'         : None,   
                                                                                    'description'           : None   
                                                                                    },
                                                                                'type_return'               : self.type_return,  
                                                                                "anonymous"                 : False   
                                                                                }
                                                                            }
                                                                        if self.name in self.data_base['func_names']: 
                                                                            self.index = self.data_base['func_names'].index( self.name )
                                                                            self.data_base['functions'][self.index] = self.my_lambda_function.copy()
                                                                        else: 
                                                                            self.data_base['func_names'].append(self.name)
                                                                            self.data_base['functions'].append(self.my_lambda_function)
                                                                    else: self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                else: pass 
                                                            else: pass 
                                                        else: self.error = ERRORS( self.line ).ERROR4()
                                                    else: self.error = ERRORS( self.line ).ERROR0( self.master )
                                                else: pass
                                            else: self.error = ERRORS( self.line ).ERROR0( self.master )
                                        else:
                                            self.final_value, self.error = LEXER_ASSEMBLY(self.value, self.data_base,
                                                                                        self.line).ASSEMBLY()
                                            if self.error is None:
                                                self.main_lexer_storage[ 'if_egal' ]    = True
                                                self.main_lexer_storage[ 'all_data' ]   = self.final_value
                                            else: pass
                                    else: self.error = ERRORS( self.line ).ERROR0( self.master )
                                else:
                                    self.final_value, self.error = LEXER_ASSEMBLY(self.value, self.data_base,
                                                                                  self.line).ASSEMBLY()
                                    if self.error is None:
                                        self.main_lexer_storage[ 'if_egal' ]        = True
                                        self.main_lexer_storage[ 'all_data' ]       = self.final_value
                                    else: pass

                            except IndexError:
                                self.final_value, self.error = LEXER_ASSEMBLY( self.value, self.data_base,
                                                                              self.line ).ASSEMBLY()
                                if self.error is None:
                                    self.main_lexer_storage[ 'if_egal' ]    = True
                                    self.main_lexer_storage[ 'all_data' ]   = self.final_value
                                else: pass
                        else:
                            self.final_value, self.error = LEXER_ASSEMBLY( self.value, self.data_base,
                                                                                            self.line ).ASSEMBLY()
                            if self.error is None:
                                self.main_lexer_storage[ 'if_egal' ]        = True
                                self.main_lexer_storage[ 'all_data' ]       = self.final_value
                            else: pass
                else: pass
        else: pass

        return  self.main_lexer_storage, self.error

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
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}due to the fact that {}<< : >> {}was not defined at the {}end. {}line: {}{}'.format(self.white, self.red, self.white, self.green,
                                                                                                   self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR2(self, string: str):
        self._str_ = '{}type {}help( {}function_name{} ) {} for more informations. '.format(self.white, self.magenta, self.yellow,
                                                                                            self.magenta, self.white)
        error = '{}in {}<< {} >> .{}line: {}{}.\n{}'.format(self.white, self.red, string, self.white, self.yellow, self.line, self._str_)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}function name {}ERROR '.format(self.white, self.yellow) + error

        return self.error+self.reset
    
    def ERROR3(self):
        error = '{}line: {}{}.'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}return {}was already defined. '.format(self.cyan, self.yellow) + error

        return self.error+self.reset
    
    def ERROR4(self):
        error = '{}line: {}{}.'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}lambda function {}name error. '.format(self.green, self.cyan) + error

        return self.error+self.reset