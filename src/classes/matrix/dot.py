import numpy as np
from src.classes                                    import error as er 
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation

class DOT:
    def __init__(self, DataBase: dict, line:int, master: np.ndarray, function, FunctionInfo : list ):
        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        self.lexer          = main_lexer
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        
    def DOT( self,  mainString: str = '', typ = 'dot') :
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.values         = self.FunctionInfo[ self.function ][ 'value' ] 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == 'master': 
                if self.values[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [['master']] ) 
                else: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.values[ 0 ],
                                                                    self.values[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        if   typ == 'dot'   : 
                                            if type( self.newValues ) == type(np.array([1])):
                                                if list(self.master): 
                                                    try: self._return_ =  self.master.dot(self.newValues)
                                                    except ValueError:
                                                        shape1, shape2 = list(self.master.shape), list(self.newValues)
                                                        self.error = er.ERRORS( self.line ).ERROR65( shape1, shape2 ) 
                                                    except TypeError: self.error = er.ERRORS( self.line ).ERROR72()
                                                else: self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                                            else:  self.error = er.ERRORS( self.line ).ERROR3( "master", "ndarray()" ) 
                                        elif typ == "redim" :
                                            if list(self.master):
                                                if type( self.newValues ) == type(tuple()):
                                                    try: self._return_ =  self.master.reshape(self.newValues)
                                                    except ValueError: 
                                                        self.error = er.ERRORS( self.line ).ERROR66( self.master.shape, self.newValues)
                                                    except TypeError : self.error = er.ERRORS( self.line ).ERROR72('interger')
                                                else:  self.error = er.ERRORS( self.line ).ERROR3( "master", "tuple()" ) 
                                            else: self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                                        elif typ == "solve" :
                                            if list(self.master):
                                                if type( self.newValues ) == type(np.array([1])):
                                                    try: 
                                                        if self.newValues.shape[0] in self.master.shape:
                                                            if self.master.shape[0] == self.master.shape[1]:
                                                                self._return_ =  np.linalg.solve(self.master, self.newValues)
                                                            else:
                                                                self._return_, _,_,_ = np.linalg.lstsq(self.master, self.newValues, rcond=None)
                                                        else:
                                                            shape1, shape2 =  self.master.shape, self.newValues.shape
                                                            self.error = er.ERRORS( self.line ).ERROR65( shape1, shape2)
                                                    except (TypeError, ValueError):
                                                        self.error = er.ERRORS( self.line ).ERROR67("master")
                                                    except IndexError:
                                                        shape1, shape2 =  self.master.shape, self.newValues.shape
                                                        self.error = er.ERRORS( self.line ).ERROR65( shape1, shape2)
                                                    except np.linalg.LinAlgError:
                                                        self.error = er.ERRORS( self.line ).ERROR69()
                                                else:  self.error = er.ERRORS( self.line ).ERROR3( "master", "ndarray()" ) 
                                            else: self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                                        elif typ == "merge" :
                                            if list(self.master):
                                                if type( self.newValues ) == type(np.array([1])):
                                                    try: 
                                                        if self.master.shape[0] == self.newValues.shape[0]:
                                                            self._return_ = np.column_stack((self.master, self.newValues))
                                                        else: self.error = er.ERRORS( self.line ).ERROR66( self.master.shape, self.newValues.shape)
                                                    except ValueError: 
                                                        self.error = er.ERRORS( self.line ).ERROR66( self.master.shape, self.newValues.shape)
                                                else:  self.error = er.ERRORS( self.line ).ERROR3( "master", "ndarray()" ) 
                                            else: self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                                        elif typ == "norm"  :
                                            if type( self.newValues ) in [type(int()), type(None)]:
                                                if list(self.master): 
                                                    try:
                                                        if self.newValues is None:  self._return_ =  np.linalg.norm(self.master)
                                                        else:
                                                            if self.newValues in [0, 1]:
                                                                self._return_ =  np.linalg.norm(self.master, axis=self.newValues)
                                                            else: self.error = er.ERRORS( self.line ).ERROR68("master", [0, 1])
                                                    except (TypeError, ValueError): 
                                                        self.error = er.ERRORS( self.line ).ERROR67("main matrix")
                                                else : self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                                            else: self.error = er.ERRORS( self.line ).ERROR3( "master", "integer()" ) 
                                        elif typ == "axis"  :
                                            self._return_, self.error = axis(self.master, self.newValues, self.line)
                                        else: pass
                                    else: pass 
                                else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            else:
                if self.arguments[ 0 ] is None:
                    if typ == 'norm' : 
                        if list( self.master): 
                            try: self._return_ =  np.linalg.norm(self.master)
                            except (TypeError, ValueError):  self.error = er.ERRORS( self.line ).ERROR67( "main matrix" )
                        else : self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                    else: self.error = er.ERRORS( self.line ).ERROR3( "master", "ndarray()" ) 
                else:
                    if self.values[ 0 ] is None:
                        if list(self.master):
                            self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                    self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase,self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues = self.final_val[ 0 ]
                                                if   typ == 'dot'   : 
                                                    if type( self.newValues ) == type(np.array([1])):
                                                        if list(self.master): 
                                                            try: self._return_ =  self.master.dot(self.newValues)
                                                            except ValueError:
                                                                shape1, shape2 = list(self.master.shape), list(self.newValues)
                                                                self.error = er.ERRORS( self.line ).ERROR65( shape1, shape2 )
                                                            except TypeError: self.error = er.ERRORS( self.line ).ERROR72() 
                                                        else: self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                                                    else:  self.error = er.ERRORS( self.line ).ERROR3( "master", "ndarray()" ) 
                                                elif typ == "redim" :
                                                    if list(self.master):
                                                        if type( self.newValues ) == type(tuple()):
                                                            try: 
                                                                self._return_ =  self.master.reshape(self.newValues)
                                                            except ValueError: 
                                                                self.error = er.ERRORS( self.line ).ERROR66( self.master.shape, self.newValues) 
                                                            except TypeError: self.error = er.ERRORS( self.line ).ERROR72('interger')
                                                        else:  self.error = er.ERRORS( self.line ).ERROR3( "master", "tuple()" ) 
                                                    else: self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                                                elif typ == "solve" :
                                                    if list(self.master):
                                                        if type( self.newValues ) == type(np.array([1])):
                                                            try: 
                                                                if self.newValues.shape[0] in self.master.shape:
                                                                    if self.master.shape[0] == self.master.shape[1]:
                                                                        self._return_ =  np.linalg.solve(self.master, self.newValues)
                                                                    else:
                                                                        self._return_, _,_,_ = np.linalg.lstsq(self.master, self.newValues, rcond=None)
                                                                else:
                                                                    shape1, shape2 =  self.master.shape, self.newValues.shape
                                                                    self.error = er.ERRORS( self.line ).ERROR65( shape1, shape2)
                                                            except (TypeError, ValueError): 
                                                                self.error = er.ERRORS( self.line ).ERROR67("master")
                                                            except IndexError:
                                                                shape1, shape2 =  self.master.shape, self.newValues.shape
                                                                self.error = er.ERRORS( self.line ).ERROR65( shape1, shape2)
                                                            except np.linalg.LinAlgError:
                                                                self.error = er.ERRORS( self.line ).ERROR69()
                                                        else:  self.error = er.ERRORS( self.line ).ERROR3( "master", "ndarry()" ) 
                                                    else: self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                                                elif typ == "merge" :
                                                    if list(self.master):
                                                        if type( self.newValues ) == type(np.array([1])):
                                                            try: 
                                                                if self.master.shape[0] == self.newValues.shape[0]:
                                                                    self._return_ = np.column_stack((self.master, self.newValues))
                                                                else: self.error = er.ERRORS( self.line ).ERROR66( self.master.shape, self.newValues.shape)
                                                            except ValueError: 
                                                                self.error = er.ERRORS( self.line ).ERROR66( self.master.shape, self.newValues.shape)
                                                        else:  self.error = er.ERRORS( self.line ).ERROR3( "master", "ndarray()" ) 
                                                    else: self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                                                elif typ == "norm"  :
                                                    if type( self.newValues ) in [type(int()), type(None)]:
                                                        if list( self.master): 
                                                            try:
                                                                if self.newValues is None:  self._return_ =  np.linalg.norm(self.master)
                                                                else:
                                                                    if self.newValues in [0, 1]:
                                                                        self._return_ =  np.linalg.norm(self.master, axis=self.newValues)
                                                                    else: self.error = er.ERRORS( self.line ).ERROR68("master", [0, 1])
                                                            except (TypeError, ValueError): 
                                                                self.error = er.ERRORS( self.line ).ERROR67("main matrix")
                                                        else : self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                                                    else: self.error = er.ERRORS( self.line ).ERROR3( "master", "integer()" )
                                                elif typ == "axis"  :
                                                    self._return_, self.error = axis(self.master, self.newValues, self.line)
                                                else: pass
                                            else: pass 
                                        else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass
                        else: self.error = er.ERRORS( self.line ).ERROR24( 'ndarray' )
                    else: self.error = er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = er.ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error
    

def axis(master, newValues, line):
    error, _return_ = None, None 
    
    if type( newValues ) in [type(list())]:
        if master.size != 0 : 
            try: 
                shape = master.shape 
                idd = []
                if newValues:
                    for s in newValues :
                        if type(s) == type(int()):
                            if s not in idd : idd.append(s)
                            else: 
                                error = er.ERRORS( line ).ERROR73( newValues)
                                break
                        else:
                            error = er.ERRORS(  line ).ERROR70( newValues)
                            break
                    if error is None:
                        if idd :
                            if len(idd) <= len( master.shape):
                                for ii, x in enumerate(idd):
                                    if x <  master.shape[ii] : pass 
                                    else: 
                                        error = er.ERRORS( line ).ERROR71( x )
                                        break 
                                if error is None:
                                    idd = np.array(idd)
                                    max_ = idd.max()
                                    if max_ < shape[0] : _return_ = master[ idd ]
                                    else: error = er.ERRORS( line ).ERROR71( max_)
                                else: pass 
                            else:
                                shape1, shape2 =  list(master.shape)
                                error = er.ERRORS( line ).ERROR65( shape1, shape2 )
                        else: _return_ = master.copy()
                    else: pass
                else:  error = er.ERRORS( line ).ERROR24( 'list' )
            except (TypeError, ValueError): 
                error = er.ERRORS( line ).ERROR67("main matrix")
        else : error = er.ERRORS( line ).ERROR24( 'ndarray' )
    elif type( newValues ) in [type(int()), type( bool()) ]:
        if master.size != 0 : 
            try:
                if newValues < master.shape[1]: _return_ = master[ :, newValues, ]
                else: error = er.ERRORS( line ).ERROR71( newValues )
            except IndexError: error = er.ERRORS( line ).ERROR71( newValues )
        else: error = er.ERRORS( line ).ERROR24( 'ndarray' )
    else: error = er.ERRORS( line ).ERROR3( "master", "list()" )

    return _return_, error 