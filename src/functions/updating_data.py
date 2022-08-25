import numpy as np
from script.PARXER     import numerical_value

class UPDATE_DATA_BASE:
    def __init__(self, 
                values      : any, 
                variables   : any, 
                global_vars : dict
                ):
        
        self.values             = values
        self.variables          = variables
        self.global_vars        = global_vars
        self.num_parxer         = numerical_value

    def UPDATE(self, data_base:dict):
        self.name_without_values = []

        if self.variables:
            for i, vars in enumerate( self.variables ):
                if type(self.values[ i ]) == type(np.array([])):
                    data_base[ 'variables' ][ 'vars' ].append( vars )
                    data_base[ 'variables' ][ 'values'].append( self.values[ i ] )
                else:
                    if self.values[ i ] != '@670532821@656188185@670532821@':
                        data_base['variables']['vars'].append(vars)
                        data_base['variables']['values'].append(self.values[i])
                    else: self.name_without_values.append( (vars, i) )
        else: pass

        self.global_variables   = self.global_vars[ 'vars' ].copy()
        self.global_values      = self.global_vars[ 'values' ].copy()

        if self.global_values:
            for i , value in enumerate( self.global_values ):
                if type(self.values[i]) == type(np.array([])):
                    data_base['variables']['vars'].append(self.global_variables[i])
                    data_base['variables']['values'].append(value)
                else:
                    if value not in [ '@670532821@656188@656188185@' ]:
                        data_base[ 'variables'] [ 'vars' ].append( self.global_variables[ i ] )
                        data_base[ 'variables' ][ 'values' ].append( value )
                    else: pass

        else: pass

        if self.name_without_values: data_base[ 'empty_values' ] = self.name_without_values
        else: pass

        data_base[ 'total_vars' ] = self.variables

    def INITIALIZATION( self, data_base:dict, info:dict ):
        self.values                             = info[ 'values' ]
        self.arguments                          = info[ 'vars' ]

        data_base[ 'variables' ][ 'vars' ]      = self.arguments
        data_base[ 'variables' ][ 'values' ]    = self.values
        data_base[ 'empty_values' ]             = None
        data_base[ 'sub_print' ]                = []