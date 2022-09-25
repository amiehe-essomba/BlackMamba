from script.LEXER.FUNCTION      import main
from script.PARXER              import parxer_assembly
from script.DATA_BASE           import data_base as db
from src.modulesLoading         import error as er


class CLASSIFICATION:
    def __init__(self, DataBase: dict, line: int):
        self.DataBase   = DataBase
        self.line       = line
    
    def CLASSIFICATION( self, modules : dict = {}, baseFileName : str = '', locked : bool = True, info : dict = {} ):
        self.db             = db.DATA_BASE().STORAGE().copy()
        self.lineI          = 0
        self.error          = None
        self.key            = True
   
        self.baseFileName   = info['module_main'][0]
          
        if modules[ 'expressions' ]:
            for i in range(0, 1):
                data_from_file = modules[ 'expressions'][ -1 ]
         
                if not data_from_file: pass 
                else:
                    for x, string in enumerate( data_from_file ):
                        self.lineI  += 1
                        
                        if string:
                            if self.db['globalIndex'] is None:
                                try:
                                    self.db['starter'] = x+1
                                    self.lexer, self.normal_string, self.error = main.MAIN(string, self.db, 
                                                                (self.lineI + self.line) ).MAIN( interpreter = True, MainList = data_from_file[x+1: ] )
                                    if self.error is None:
                                        if self.lexer is not None:
                                            
                                            num, self.key, self.error = parxer_assembly.ASSEMBLY(self.lexer, self.db, 
                                                                (self.lineI + self.line) ).GLOBAL_ASSEMBLY_FILE_INTERPRETER(self.normal_string, True,
                                                                MainList = data_from_file[x+1: ], baseFileName = self.baseFileName,
                                                                locked = locked)
                                            if self.error is None: pass
                                            else:  break
                                        else: pass
                                    else:  break
                                except EOFError: break
                            else:
                                if x < self.db['globalIndex']+1: pass 
                                else:
                                    try:
                                        self.db['starter'] = x+1
                                        self.lexer, self.normal_string, self.error = main.MAIN(string, self.db, 
                                                                    (self.lineI + self.line)).MAIN( interpreter = True,
                                                                    MainList = data_from_file[x+1: ] )
                                        if self.error is None:
                                            if self.lexer is not None:
                                                num, self.key, self.error = parxer_assembly.ASSEMBLY(self.lexer, self.db,
                                                                (self.lineI + self.line)).GLOBAL_ASSEMBLY_FILE_INTERPRETER(self.normal_string, 
                                                                True, MainList = data_from_file[x+1: ],  baseFileName = self.baseFileName,
                                                                locked = locked)
                                                if self.error is None: pass
                                                else:  break
                                            else: pass
                                        else: break
                                    except EOFError: break
                        else: pass
        else: pass
        
        self.vars, self._values_ = [], []
         
        if self.error is None:
            if self.db['global_vars']['values']:
                for i, value in enumerate( self.db['global_vars']['values'] ):
                    if value not in [ '@670532821@656188@656188185@' ]:
                        self.vars.append(self.db['global_vars']['vars'][ i ])
                        self._values_.append( value )
                    else: pass
            else: pass
            
            if info['alias'] is None: pass 
            else: info['module_main'] = [info['alias']]
            
            if info['module_main'][ 0 ] not in self.DataBase[ 'modulesImport' ]['modules']:
                self.DataBase[ 'modulesImport' ]['variables']['vars'].append(self.vars)
                self.DataBase[ 'modulesImport' ]['variables']['values'].append(self._values_)
                self.DataBase[ 'modulesImport' ]['modules'].append(info['module_main'][ 0 ])
            else:
                self.index = self.DataBase[ 'modulesImport' ]['modules'].index( info['module_main'][ 0 ] )
                self.DataBase[ 'modulesImport' ]['variables']['vars'][self.index]     = self.vars.copy()
                self.DataBase[ 'modulesImport' ]['variables']['values'][self.index]   = self._values_.copy()
                self.DataBase[ 'modulesImport' ]['modules'][self.index]               = info['module_main'][ 0 ]

            # only classes
            if    self.db[ 'class_names']  and not self.db[ 'func_names' ]  :
                self.star       = False
                if  info['module_load'] is not None:
                    for x, name in enumerate(info['module_main']):
                        self.idd        = 0
                        for mod in info['module_load']:
                            if mod != '*':
                                if mod in self.db[ 'class_names' ]:  self.idd += 1
                                else: 
                                    self.error =  er.ERRORS( self.line ).ERROR9( name, mod )
                                    break
                            else:
                                self.idd += 1
                                self.star = True
                        
                        if self.error is None:
                            if self.idd != 0: pass 
                            else: 
                                self.error =  er.ERRORS( self.line ).ERROR10( name  )
                                break
                        else: break
                    
                    if self.error is None:
                        if info['module_main'][ 0 ] not in self.DataBase[ 'modulesImport' ]['init']:
                            self.DataBase[ 'modulesImport' ][ 'class_names' ].append( self.db[ 'class_names' ] )
                            self.DataBase[ 'modulesImport' ][ 'classes' ].append(self.db[ 'classes' ])
                            self.DataBase[ 'modulesImport' ][ 'func_names' ].append( [] )
                            self.DataBase[ 'modulesImport' ][ 'functions' ].append([])
                                         
                            if self.star is False:
                                if  len(info['module']) != 4:
                                    self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append(info['module_load']) 
                                    self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append([])
                                    self.DataBase[ 'modulesImport' ][ 'alias' ].append({} )
                                else:
                                    self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append([info['alias']]) 
                                    self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append([])
                                    self.DataBase[ 'modulesImport' ][ 'alias' ].append({info['alias'] : info['module_load'][0]})
                            else:
                                self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append(self.db[ 'class_names' ][ : ])
                                self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append([])
                                self.DataBase[ 'modulesImport' ][ 'alias' ].append({} )
                            self.DataBase[ 'modulesImport' ]['init'].append(info['module_main'][ 0 ])
                        else:
                            self.index = self.DataBase[ 'modulesImport' ]['init'].index(info['module_main'][ 0 ])
                            self.DataBase[ 'modulesImport' ][ 'class_names' ][ self.index ]   = self.db[ 'class_names' ]
                            self.DataBase[ 'modulesImport' ][ 'classes' ][ self.index ]       = self.db[ 'classes' ] 
                            self.DataBase[ 'modulesImport' ][ 'functions' ][self.index]       = []
                            self.DataBase[ 'modulesImport' ][ 'func_names' ][self.index]      = []
                                                         
                            if self.star is False:
                                if  len(info['module']) != 4:
                                    self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]     = info['module_load']
                                    self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]      = []
                                    self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]               = {}
                                else:
                                    self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]     = [info['alias']]
                                    self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]               = {info['alias'] : info['module_load'][0]}
                                    self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]      = []
                            else:
                                self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]     = self.db[ 'class_names' ][ : ]
                                self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]      = []
                                self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]               = {}
                    else: pass
                else:
                    self.data = {
                        'class_names'   : self.db[ 'class_names' ].copy(),
                        'classes'       : self.db[ 'classes' ].copy(),
                        }
                        
                    if info['module_main'][ 0 ] not in self.DataBase[ 'modulesImport' ]['init']:
                        self.DataBase[ 'modulesImport' ][ 'modulesLoadC' ].append( self.data)
                        self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append([]) 
                        self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append([])
                        self.DataBase[ 'modulesImport' ][ 'func_names' ].append( [] )
                        self.DataBase[ 'modulesImport' ][ 'functions' ].append([])
                        self.DataBase[ 'modulesImport' ][ 'class_names' ].append( [] )
                        self.DataBase[ 'modulesImport' ][ 'classes' ].append([])
                        self.DataBase[ 'modulesImport' ][ 'alias' ].append({})
                    else:
                        self.index = self.DataBase[ 'modulesImport' ]['init'].index(info['module_main'][ 0 ])
                        self.DataBase[ 'modulesImport' ][ 'modulesLoadC' ][self.index ]      = self.data.copy()
                        self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]    = []
                        self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]   = []
                        self.DataBase[ 'modulesImport' ][ 'functions' ][self.index]         = []
                        self.DataBase[ 'modulesImport' ][ 'func_names' ][self.index]        = []
                        self.DataBase[ 'modulesImport' ][ 'classes' ][self.index]           = []
                        self.DataBase[ 'modulesImport' ][ 'class_names' ][self.index]       = []
                        self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]             = {}
                        
                    self.DataBase[ 'modulesImport' ]['init'].append(info['module_main'][ 0 ])
                    del self.data
            # only functions
            elif  self.db[ 'func_names' ]  and not self.db[ 'class_names' ] :
                self.star       = False
                if  info['module_load'] is not None:
                    
                    for x, name in enumerate(info['module_main']):
                        self.idd        = 0
                        
                        for mod in info['module_load']:
                            if mod != '*':
                                if mod in self.db[ 'func_names' ]:
                                    self.idd += 1
                                else: 
                                    self.error =  er.ERRORS( self.line ).ERROR9( name+".bm", mod )
                                    break
                            else: 
                                self.idd += 1
                                self.star = True
                        
                        if self.error is None:
                            if self.idd != 0: pass 
                            else: 
                                self.error =  er.ERRORS( self.line ).ERROR10( name+".bm"  )
                                break
                        else: break
                    
                    if self.error is None:
                        if info['module_main'][ 0 ] not in self.DataBase[ 'modulesImport' ]['init']:
                            self.DataBase[ 'modulesImport' ][ 'func_names' ].append( self.db[ 'func_names' ][ : ] )
                            self.DataBase[ 'modulesImport' ][ 'functions' ].append(self.db[ 'functions' ][ : ])
                            self.DataBase[ 'modulesImport' ][ 'class_names' ].append( [] )
                            self.DataBase[ 'modulesImport' ][ 'classes' ].append([])
                                                         
                            if self.star is False:
                                if len(info['module']) != 4:
                                    self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append(info['module_load'])
                                    self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append([]) 
                                    self.DataBase[ 'modulesImport' ][ 'alias' ].append({} )
                                else:
                                    self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append([info['alias']])#(info['module_load'])
                                    self.DataBase[ 'modulesImport' ][ 'alias' ].append({info['alias'] : info['module_load'][0]})
                                    self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append([]) 
                            else:
                                self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append(self.db[ 'func_names' ][ : ])
                                self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append([]) 
                                self.DataBase[ 'modulesImport' ][ 'alias' ].append({} )
                            self.DataBase[ 'modulesImport' ]['init'].append(info['module_main'][ 0 ])
                        else:
                            self.index = self.DataBase[ 'modulesImport' ]['modules'].index(info['module_main'][ 0 ])
                            self.DataBase[ 'modulesImport' ][ 'func_names' ][ self.index ]    = self.db[ 'func_names' ] 
                            self.DataBase[ 'modulesImport' ][ 'functions' ][ self.index ]     = self.db[ 'functions' ]
                            self.DataBase[ 'modulesImport' ][ 'classes' ][self.index]         = []
                            self.DataBase[ 'modulesImport' ][ 'class_names' ][self.index]     = []
                                                         
                            if self.star is False:
                                if len(info['module']) != 4:
                                    self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]      = info['module_load'].copy()
                                    self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]     = []
                                    self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]               = {}
                                else:
                                    self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]      = [info['alias']]#info['module_load'].copy()
                                    self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]               = {info['alias'] : info['module_load'][0]}
                                    self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]     = []
                            else:
                                self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]      = self.db[ 'func_names' ].copy()
                                self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]     = []
                                self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]               = {}
    
                    else: pass
                else:
                    self.data = {
                        'func_names'    : self.db[ 'func_names' ].copy(),
                        'functions'     : self.db[ 'functions' ].copy()
                        }
                        
                    if info['module_main'][ 0 ] not in self.DataBase[ 'modulesImport' ]['init']:
                        self.DataBase[ 'modulesImport' ][ 'modulesLoadF' ].append( self.data )
                        self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append([]) 
                        self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append([])
                        self.DataBase[ 'modulesImport' ][ 'func_names' ].append( [] )
                        self.DataBase[ 'modulesImport' ][ 'functions' ].append([])
                        self.DataBase[ 'modulesImport' ][ 'class_names' ].append( [] )
                        self.DataBase[ 'modulesImport' ][ 'classes' ].append([])
                        self.DataBase[ 'modulesImport' ][ 'alias' ].append({})
                    else:
                        self.index = self.DataBase[ 'modulesImport' ]['modules'].index(info['module_main'][ 0 ])
                        self.DataBase[ 'modulesImport' ][ 'modulesLoadF' ][self.index ]      = self.data.copy()
                        self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]    = []
                        self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]   = []
                        self.DataBase[ 'modulesImport' ][ 'functions' ][self.index]         = []
                        self.DataBase[ 'modulesImport' ][ 'func_names' ][self.index]        = []
                        self.DataBase[ 'modulesImport' ][ 'classes' ][self.index]           = []
                        self.DataBase[ 'modulesImport' ][ 'class_names' ][self.index]       = []
                        self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]             = {}
                        
                    self.DataBase[ 'modulesImport' ]['init'].append(info['module_main'][ 0 ])
                    del self.data
            # classes and functions
            elif  self.db[ 'func_names' ]  and  self.db[ 'class_names' ]    :
                self.star = False
                if  info['module_load'] is not None:
                    for x, name in enumerate(info['module_main']):
                        self.idd            = 0
                        self.func           = []
                        self.class_         = []
                        
                        for mod in info['module_load']:
                            if mod != '*':
                                if mod in self.db[ 'func_names' ]:
                                    self.idd += 1       
                                    self.func.append(mod)
                                elif mod in self.db[ 'class_names' ]:
                                    self.idd += 1
                                    self.class_.append(mod)
                                else: 
                                    self.error =  er.ERRORS( self.line ).ERROR9( name+".bm", mod )
                                    break
                            else:
                                self.idd +=1
                                self.star = True 
                                
                        if self.error is None:
                            if self.idd != 0: pass 
                            else: 
                                self.error =  er.ERRORS( self.line ).ERROR10( name+".bm"  )
                                break
                        else: break
                    
                    if self.error is None:
                        if info['module_main'][ 0 ] not in self.DataBase[ 'modulesImport' ]['init']:
                            self.DataBase[ 'modulesImport' ][ 'class_names' ].append( self.db[ 'class_names' ] )
                            self.DataBase[ 'modulesImport' ][ 'classes' ].append(self.db[ 'classes' ])
                            self.DataBase[ 'modulesImport' ][ 'func_names' ].append( self.db[ 'func_names' ] )
                            self.DataBase[ 'modulesImport' ][ 'functions' ].append(self.db[ 'functions' ])
                                                         
                            if self.star is False:
                                if len(info['module']) != 4:
                                    self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append(self.func)
                                    self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append(self.class_) 
                                    self.DataBase[ 'modulesImport' ][ 'alias' ].append({} )
                                else:
                                    if self.class_:  
                                        self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append([info['alias']])
                                        self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append([])
                                    else: 
                                        self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append([info['alias']])
                                        self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append([])
                                    self.DataBase[ 'modulesImport' ][ 'alias' ].append({info['alias'] : info['module_load'][0]})
                            else:
                                self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append(self.db[ 'func_names' ].copy())
                                self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append(self.db[ 'class_names' ].copy())
                                self.DataBase[ 'modulesImport' ][ 'alias' ].append({} )
                            self.DataBase[ 'modulesImport' ]['init'].append(info['module_main'][ 0 ])
                        else:
                            self.index = self.DataBase[ 'modulesImport' ]['modules'].index(info['module_main'][ 0 ])
                            self.DataBase[ 'modulesImport' ][ 'class_names' ][ self.index ]   = self.db[ 'class_names' ].copy()
                            self.DataBase[ 'modulesImport' ][ 'classes' ][ self.index ]       = self.db[ 'classes' ].copy()
                            self.DataBase[ 'modulesImport' ][ 'func_names' ][ self.index ]    = self.db[ 'func_names' ].copy() 
                            self.DataBase[ 'modulesImport' ][ 'functions' ][ self.index ]     = self.db[ 'functions' ].copy()
                                                         
                            if self.star is False:
                                if len(info['module']) != 4:
                                    self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]      = self.func.copy()
                                    self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]     = self.class_.copy()
                                    self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]               = {}
                                else:
                                    if self.class_:
                                        self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]     = [info['alias']]
                                        self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]      = []
                                    else:
                                        self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]      = [info['alias']]
                                        self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]     = []
                                    self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]                   = {info['alias'] : info['module_load'][0]}
                            else:
                                self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]      = self.db[ 'func_names' ].copy()
                                self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]     = self.db[ 'class_names' ].copy()
                                self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]               = {}
                        self.class_, self.func = [], []
                    else: pass
                else:
                    self.data1 = {
                        'class_names'   : self.db[ 'class_names' ].copy(),
                        'classes'       : self.db[ 'classes' ].copy(),
                        }
                    
                    self.data2 = {
                        'func_names'    : self.db[ 'func_names' ].copy(),
                        'functions'     : self.db[ 'functions' ].copy()
                        }
                        
                    if info['module_main'][ 0 ] not in self.DataBase[ 'modulesImport' ]['init']:
                        self.DataBase[ 'modulesImport' ][ 'modulesLoadC' ].append( self.data1)
                        self.DataBase[ 'modulesImport' ][ 'modulesLoadF' ].append( self.data2)
                        self.DataBase[ 'modulesImport' ][ 'mainClassNames' ].append([]) 
                        self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ].append([])
                        self.DataBase[ 'modulesImport' ][ 'func_names' ].append( [] )
                        self.DataBase[ 'modulesImport' ][ 'functions' ].append([])
                        self.DataBase[ 'modulesImport' ][ 'class_names' ].append( [] )
                        self.DataBase[ 'modulesImport' ][ 'classes' ].append([])
                        self.DataBase[ 'modulesImport' ][ 'alias' ].append({})
                    else:
                        self.index = self.DataBase[ 'modulesImport' ]['modules'].index(info['module_main'][ 0 ])
                        self.DataBase[ 'modulesImport' ][ 'modulesLoadC' ][self.index ]  = self.data1.copy()
                        self.DataBase[ 'modulesImport' ][ 'modulesLoadF' ][self.index ]  = self.data2.copy()
                        self.DataBase[ 'modulesImport' ][ 'mainFuncNames' ][self.index ]    = []
                        self.DataBase[ 'modulesImport' ][ 'mainClassNames' ][self.index ]   = []
                        self.DataBase[ 'modulesImport' ][ 'functions' ][self.index]         = []
                        self.DataBase[ 'modulesImport' ][ 'func_names' ][self.index]        = []
                        self.DataBase[ 'modulesImport' ][ 'classes' ][self.index]           = []
                        self.DataBase[ 'modulesImport' ][ 'class_names' ][self.index]       = []
                        self.DataBase[ 'modulesImport' ][ 'alias' ][self.index]             = {}
                        
                    self.DataBase[ 'modulesImport' ]['init'].append(info['module_main'][ 0 ])
                    del self.data1
                    del self.data2
            # if not classes and functions
            else: self.error =  er.ERRORS( self.line ).ERROR11( info['module_main'][0] )

        else: 
            for i, name in enumerate(self.DataBase['modulesImport']['TrueFileNames']['names']):
                if name == info['module_main'][ 0 ]:
                    self.idd = self.DataBase['modulesImport']['TrueFileNames']['names'].index( name )
                    if info['path'] is None:
                        if self.DataBase['modulesImport']['TrueFileNames']['path'][ i ] is None:
                            self.DataBase['modulesImport']['TrueFileNames']['line'][self.idd]   = self.line
                            break
                        else: pass 
                    else:
                        if self.DataBase['modulesImport']['TrueFileNames']['path'][ i ] is not None:
                            self.DataBase['modulesImport']['TrueFileNames']['line'][self.idd]   = self.line
                            break 
                        else: pass
                else: pass
        
        INIT(self.db).INIT()
         
        return self.error 
      
class INIT:
    def __init__(self, db):
        self.db = db
        
    def INIT(self):
        functionNames, functions = db.DATA_BASE().FUNCTIONS()
        
        self.db['global_vars']['vars']                          = []
        self.db['global_vars']['values']                        = []
        self.db['variables']['values']                          = []
        self.db['variables']['vars']                            = []
        self.db['irene']                                        = None 
        self.db['class_names']                                  = []
        self.db['func_names']                                   = []
        self.db['classes']                                      = []
        self.db['functions']                                    = []
        self.db['loop_for']                                     = []
        self.db['loop_while']                                   = []
        self.db['loop_until']                                   = []
        self.db['continue']                                     = None
        self.db['next']                                         = None
        self.db['pass']                                         = None
        self.db['break']                                        = None
        self.db['exit']                                         = None
        self.db['try']                                          = None
        self.db['begin']                                        = None
        self.db['if']                                           = []
        self.db['switch']                                       = []
        self.db['unless']                                       = []
        self.db['return']                                       = None
        self.db['print']                                        = []
        self.db['sub_print']                                    = None
        self.db['current_func']                                 = None
        self.db['current_class']                                = None
        self.db['transformation']                               = None
        self.db['no_print_values']                              = []
        self.db['line']                                         = None
        self.db['encoding']                                     = None
        self.db['importation']                                  = None
        self.db['LIB'] ['func_names']                           = functionNames
        self.db['LIB']['functions']                             = functions
        self.db['LIB']['class_names']                           = []
        self.db['LIB']['classes']                               = []
        self.db['modulesImport']['moduleNames']                 = []
        self.db['modulesImport']['filesNames']                  = []
        self.db['modulesImport']['TrueFileNames']['names']      = []
        self.db['modulesImport']['TrueFileNames']['path']       = []
        self.db['modulesImport']['TrueFileNames']['line']       = []
        self.db['modulesImport']['expressions']                 = []
        self.db['modulesImport']['variables']['vars']           = []
        self.db['modulesImport']['variables']['values']         = []
        self.db['modulesImport']['classes']                     = []
        self.db['modulesImport']['class_names']                 = []
        self.db['modulesImport']['func_names']                  = []
        self.db['modulesImport']['functions']                   = []
        self.db['modulesImport']['mainFuncNames']               = []
        self.db['modulesImport']['mainClassNames']              = []
        self.db['modulesImport']['modules']                     = []
        self.db['modulesImport']['modulesLoad']                 = []
        self.db['modulesImport']['init']                        = []
        self.db[ 'modulesImport' ][ 'alias' ]                   = []
        self.db['globalIndex']                                  = None
        self.db['starter']                                      = 0
        self.db['subFunctionNames']                             = []
        self.db['subclassNames']                                = []
        self.db['open']['name']                                 = []
        self.db['open']['file']                                 = []
        self.db['open']['action']                               = []
        self.db['open']['encoding']                             = []
        self.db['open']['nonCloseKey']                          = []
        self.db['loading']                                      = False
        self.db['matrix']                                       = False
        self.db['historyOfErrors']['fileName']                  = []
        self.db['historyOfErrors']['classes']                   = []
        self.db['historyOfErrors']['functions']                 = []
        self.db['historyOfErrors']['line']                      = []
        self.db['def_return']                                   = False