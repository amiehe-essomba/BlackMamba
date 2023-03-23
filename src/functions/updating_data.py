#############################################
# the function Data base is updated here    #
# when global variables are used the code   #
# should takes them account and add them    #
# in the data base                          #
#############################################


import numpy as np

class UPDATE_DATA_BASE:
    def __init__(self, 
                values      : any, 
                variables   : any, 
                global_vars : dict
                ):
        
        self.values             = values
        self.variables          = variables
        self.global_vars        = global_vars
    
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
                try:
                    if type(self.global_variables[i]) == type(np.array([])):
                        data_base['variables']['vars'].append(self.global_variables[i])
                        data_base['variables']['values'].append(value)
                    else:
                        if value not in [ '@670532821@656188@656188185@' ]:
                            data_base[ 'variables'] [ 'vars' ].append( self.global_variables[ i ] )
                            data_base[ 'variables' ][ 'values' ].append( value )
                        else: pass
                except IndexError:
                    if value not in ['@670532821@656188@656188185@']:
                        data_base['variables']['vars'].append(self.global_variables[i])
                        data_base['variables']['values'].append(value)
                    else: pass
            if 'anonymous' in self.global_variables:
                idd_ = self.global_variables.index('anonymous')
                del self.global_variables[idd_]
                del self.global_values[idd_]
                self.global_vars['vars']    = self.global_variables
                self.global_vars['values']  = self.global_values
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

    def UPDATING_IMPORTATION(self, main_data_base:dict, def_data_base : dict):
        self.def_data_base_init = def_data_base.copy()

        self.modules_load   = main_data_base[ 'modulesImport' ]
        self.moduleNames    = self.modules_load[ 'moduleNames' ]
        self.TrueFileNames  = self.modules_load[ 'TrueFileNames' ]
        self.path           = self.TrueFileNames[ 'path' ]
        self.names          = self.TrueFileNames[ 'names' ]
        self.line           = self.TrueFileNames[ 'line' ]
        self.fileNames      = self.modules_load[ 'fileNames' ]
        self.expressions    = self.modules_load[ 'expressions' ]
        self.vars           = self.modules_load[ 'variables' ]['vars']
        self.values         = self.modules_load['variables']['values']
        self.classes        = self.modules_load[ 'classes' ]
        self.class_names    = self.modules_load[ 'class_names' ]
        self.functions      = self.modules_load[ 'functions' ]
        self.func_names     = self.modules_load[ 'func_names' ]
        self.mainFuncNames  = self.modules_load[ 'mainFuncNames' ]
        self.mainClassNames = self.modules_load[ 'mainClassNames' ]
        self.modules        = self.modules_load[ 'modules' ]
        self.modulesLoadC   = self.modules_load[ 'modulesLoadC' ]
        self.modulesLoadF   = self.modules_load[ 'modulesLoadF' ]
        self.init           = self.modules_load[ 'init' ]
        self.alias          = self.modules_load[ 'alias' ]

        if self.moduleNames:
            for m in self.moduleNames:
                def_data_base[ 'modulesImport' ][ 'moduleNames' ].append( m )
        else: pass

        for i in range(len(self.path)):
            def_data_base[ 'modulesImport' ][ 'TrueFileNames' ][ 'path' ].append( self.path[i] )
            def_data_base[ 'modulesImport' ][ 'TrueFileNames' ][ 'names'].append( self.names[i] )
            def_data_base[ 'modulesImport' ][ 'TrueFileNames' ][ 'line' ].append( self.line[i] )

        if self.fileNames:
            for m in self.fileNames:
                def_data_base[ 'modulesImport' ][ 'fileNames' ].append(m)
        else: pass

        if self.expressions:
            for m in self.expressions:
                def_data_base['modulesImport']['expressions'].append(m)
        else: pass

        if self.vars:
            for i in range(len(self.vars)):
                def_data_base['modulesImport']['variables']['vars'].append(self.vars[i])
                def_data_base['modulesImport']['variables']['values'].append(self.values[i])
        else: pass

        if self.class_names:
            for i in range(len(self.class_names)):
                def_data_base['modulesImport']['classes'].append(self.classes[i])
                def_data_base['modulesImport']['class_names'].append(self.class_names[i])
        else: pass

        if self.func_names:
            for i in range( len(self.func_names)):
                def_data_base['modulesImport']['functions'].append(self.functions[i])
                def_data_base['modulesImport']['func_names'].append(self.func_names[i])
        else: pass

        if self.mainFuncNames:
            for m in self.mainFuncNames:
                def_data_base['modulesImport']['mainFuncNames'].append(m)
        else: pass

        if self.mainClassNames:
            for m in self.mainClassNames:
                def_data_base['modulesImport']['mainClassNames'].append(m)
        else: pass

        if self.modules:
            for m in self.modules:
                def_data_base['modulesImport']['modules'].append(m)
        else: pass

        if self.modulesLoadC:
            for m in self.modulesLoadC:
                def_data_base['modulesImport']['modulesLoadC'].append(m)
        else: pass

        if self.modulesLoadF:
            for m in self.modulesLoadF:
                def_data_base['modulesImport']['modulesLoadF'].append(m)
        else: pass

        if self.alias:
            for a in self.alias:
                def_data_base['modulesImport']['alias'].append(a)
        else: pass

        if self.init:
            for i in self.init:
                def_data_base['modulesImport']['init'].append(i)
        else: pass
