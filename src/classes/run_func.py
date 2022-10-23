from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS           import functions                as func
from src.classes                                        import error                    as er 
from src.functions                                      import type_of_data             as tod
from src.functions                                      import error                    as err
from src.functions                                      import updating_data
from script.LEXER.FUNCTION                              import print_value


class RUN_FUNCTION:
    def __init__(self, 
        DataBase        : dict, 
        line            : int, 
        new_data_base   : dict, 
        _new_data_base_ : dict 
        ) :
        
        self.DataBase           = DataBase
        self.line               = line 
        self.new_data_base      = new_data_base
        self._new_data_base_    = _new_data_base_
        
    def RUN( self, 
            all_data_analyses   : list, 
            functionName        : str, 
            tabulation          : int =2, 
            _type_              : str = None
            ) :
        
        self.all_data_analyses  = all_data_analyses
        self.error              = None
        self.initialize_values  = None
        self.functionName       = functionName
        self.final_values       = None
        self.vars               = None 
        self._values_           = None
        
        
        self.new_data_base[ 'classes' ]         = self.DataBase[ 'classes' ]
        self.new_data_base[ 'class_names' ]     = self.DataBase[ 'class_names' ]
        self.new_data_base[ 'func_names' ]      = self.DataBase[ 'func_names' ]
        self.new_data_base[ 'functions' ]       = self.DataBase[ 'functions' ]
        
        self.new_data_base[ 'print' ]   = []
        updating_data.UPDATE_DATA_BASE(None, None, None).UPDATING_IMPORTATION(self.DataBase, self.new_data_base)

        if self.new_data_base[ 'empty_values' ] is None:
            
            self.error = func.EXTERNAL_DEF_LOOP_STATEMENT( None, self.new_data_base,
                                        self.line ).DEF_STATEMENT( tabulation, self.all_data_analyses )
            if self.error is None:
                self.vars                   = self.new_data_base[ 'variables' ]['vars'][:]
                self._values_               = self.new_data_base[ 'variables' ]['values'][:]
                self.initialize_values      = self.new_data_base[ 'variables' ]
                self.DataBase[ 'irene' ]    = self.new_data_base[ 'irene' ]
                self.keyActivation          = False

                if self.new_data_base[ 'return' ] is not None:
                    self.DataBase['def_return'] = True
                    
                    if _type_ != 'None':
                        if len( self.new_data_base[ 'return' ] ) == 1:
                            self.final_values = self.new_data_base[ 'return' ][ 0 ]
                            if _type_ in [None, 'any']: pass 
                            else:
                                self.typ = tod.CHECK_TYPE_OF_DATA(value=_type_).RETURNING_TYPE()
                                if type(self.final_values) == self.typ[0] : pass
                                else: 
                                    self.false = tod.CHECK_TYPE_OF_DATA(value=self.final_values).DATA()
                                    self.false = tod.CHECK_TYPE_OF_DATA(value=self.false).TYPE()
                                    self.error = err.ERRORS(self.line).ERROR24(self.false, self.typ[1] )
                        else: 
                            self.final_values = tuple( self.new_data_base[ 'return' ] )
                            if _type_ in [None, 'any']: pass
                            else:
                                self.typ = tod.CHECK_TYPE_OF_DATA(value='tuple').RETURNING_TYPE()
                                if _type_ == 'tuple': pass
                                else: 
                                    self.false = tod.CHECK_TYPE_OF_DATA(value=self.final_values).DATA()
                                    self.false = tod.CHECK_TYPE_OF_DATA(value=self.false).TYPE()
                                    self.error = err.ERRORS(self.line).ERROR24(self.false, self.typ[1] )
                    else:self.error= er.ERRORS(self.line).ERROR25(name=self.function_name )
                    
                    if self.error is None:
                        if self.new_data_base[ 'print' ] is not None:
                            self.print_values   = True
                            self.list_of_values = self.new_data_base[ 'print' ]
                            for i, value in enumerate( self.list_of_values ):
                                print_value.PRINT_PRINT( value, self.DataBase ).PRINT_PRINT( key = False )

                            self.new_data_base[ 'print' ]   = []
                        else: pass
                    else: pass
                    
                    updating_data.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,
                                                            self._new_data_base_ )
                else:
                    if _type_ in [None, 'None']:
                        if self.new_data_base[ 'sub_print' ] is None:
                            if self.new_data_base[ 'transformation' ] is None:
                                if self.new_data_base[ 'return' ] is not None:
                                    self.final_values   = self.new_data_base[ 'return' ]
                                    self.keyActivation  = True
                                else: pass
                                self.DataBase['def_return'] = False
                            else:
                                self.final_values = self.new_data_base[ 'transformation' ]
                                self.new_data_base[ 'transformation' ]      = None
                                self.keyActivation                          = True
                                self.DataBase['def_return']                 = True
                                
                            if self.new_data_base[ 'print' ] :
                                self.print_values   = True
                                self.list_of_values = self.new_data_base[ 'print' ]

                                for i, value in enumerate( self.list_of_values ):
                                    print_value.PRINT_PRINT( value, self.DataBase ).PRINT_PRINT( key = False )

                                self.new_data_base[ 'print' ]       = []
                            else: 
                                if self.keyActivation is True: pass 
                                else: 
                                    if self.functionName == 'initialize': pass 
                                    else: self.DataBase[ 'no_printed_values' ].append( None )
                                
                            updating_data.UPDATE_DATA_BASE( None, None, None ).INITIALIZATION( self.new_data_base,
                                                                self._new_data_base_ )
                        else:
                            self.DataBase[ 'no_printed_values' ].append( self.new_data_base[ 'sub_print' ] )
                            updating_data.UPDATE_DATA_BASE(None, None, None).INITIALIZATION(self.new_data_base,
                                                            self._new_data_base_)
                    else: 
                        self.typ = tod.CHECK_TYPE_OF_DATA(value=_type_).RETURNING_TYPE()
                        self.false = tod.CHECK_TYPE_OF_DATA(value=self.final_values).DATA()
                        self.false = tod.CHECK_TYPE_OF_DATA(value=self.false).TYPE()
                        self.error = err.ERRORS(self.line).ERROR24(self.typ[1], self.false)
            else: pass
        else:   
            self.empty_values   = self.new_data_base[ 'empty_values' ]
            self.error          = er.ERRORS( self.line ).ERROR15( self.functionName , self.empty_values )

        self.initialize_values  = {
            'vars'              : self.vars,
            'values'            : self._values_
        }
      
        return self.final_values, self.DataBase[ 'no_printed_values' ], self.initialize_values, self.error