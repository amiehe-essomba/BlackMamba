import os
from os                         import listdir
from os.path                    import isfile, join

from requests import delete

from script.LEXER.FUNCTION      import main
from script.PARXER              import parxer_assembly
from script                     import control_string
from script.LEXER               import main_lexer
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from script.DATA_BASE           import data_base as db
try:
    from CythonModules.Windows  import fileError as fe 
except ImportError:
    from CythonModules.Linux    import fileError as fe 

class TREATMENT:
    def __init__(self, 
                master      : dict, 
                data_base   : dict, 
                line        : int 
                ):
        self.line               = line
        self.master             = master
        self.data_base          = data_base

        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex                = main_lexer
        self.control            = control_string.STRING_ANALYSE( {}, self.line )
        self.module             = self.master['module']
        self.path               = self.master['path']
        self.alias              = self.master['alias']
        self.module_load        = self.master['module_load']
        self.module_main        = self.master['module_main']
        self.currently_path     = os.getcwd()
        self.termios            = '.bm'
        
        try:
            self.path_library       = '/media/amiehe/KEY/black_mamba/Library'
            self.currently_listdir  = listdir(self.currently_path)
            self.library            = listdir(self.path_library)
        except FileNotFoundError:
            self.path_library       = 'D:\\black_mamba\\Library'
            self.currently_listdir  = listdir(self.currently_path)
            self.library            = listdir(self.path_library)

    def MODULE_MAIN(self, mainString: str, baseFileName : str = ''):
        self.error                  = None
        self.key_directory          = []
        self.storage_module         = None 
        self.check                  =  []
         
        if self.path is None:
            if not self.data_base['modulesImport']['TrueFileNames']['names']:
                self.data_base['modulesImport']['TrueFileNames']['names'].append(self.module_main[0])
                self.data_base['modulesImport']['TrueFileNames']['path'].append(None)
                self.data_base['modulesImport']['TrueFileNames']['line'].append(0)
            else:
                if self.module_main[0] in self.data_base['modulesImport']['TrueFileNames']['names']:
                    self.idd = self.data_base['modulesImport']['TrueFileNames']['names'].index(self.module_main[0])
                    if self.data_base['modulesImport']['TrueFileNames']['path'][self.idd] is None: pass 
                    else:
                        self.data_base['modulesImport']['TrueFileNames']['names'].append(self.module_main[0])
                        self.data_base['modulesImport']['TrueFileNames']['path'].append(None)
                        self.data_base['modulesImport']['TrueFileNames']['line'].append(0)
                else: 
                    self.data_base['modulesImport']['TrueFileNames']['names'].append(self.module_main[0])
                    self.data_base['modulesImport']['TrueFileNames']['path'].append(None)
                    self.data_base['modulesImport']['TrueFileNames']['line'].append(0)
            
            if self.alias is None:
                if self.module_load is None:
                    for module in self.module_main:
                        self.module_name    = module + self.termios
                        if self.module_name in self.currently_listdir:
                            if isfile( self.module_name ) is True: 
                                if self.module_name != baseFileName:
                                    self.key_directory.append( 'current' )
                                else:
                                    self.error = ERRORS( self.line ).ERROR8( self.module_name )
                                    break
                            else: self.error = ERRORS( self.line ).ERROR2( self.module_name )
                        else:
                            if self.module_name in self.library:
                                if isfile( path= self.path_library+'/'+self.module_name ) is True: 
                                    if self.module_name != baseFileName:
                                        self.key_directory.append( 'library' )
                                    else:
                                        self.error = ERRORS( self.line ).ERROR8( self.module_name )
                                        break
                                else: self.error = ERRORS( self.line ).ERROR2( self.module_name )
                            else:
                                self.error = ERRORS( self.line ).ERROR1( self.module_name )
                                break
                       
                    if self.error is None:
                        self.len_module_main    = len( self.module_main )
                        self.value              = []
                        self.storage_module     = dict()

                        for i in range( self.len_module_main ):
                            self.module_name = ''
                            if not self.check:
                                self.module_name    = self.module_main[ i ] + self.termios
                                self.check.append( self.module_main[ i ] )
                            else:
                                if  self.module_main[ i ] in self.check:
                                    self.error = ERRORS( self.line ).ERROR5( self.module_main[ i ]+self.termios ) 
                                    del self.check
                                    break
                                else:
                                    self.module_name    = self.module_main[ i ] + self.termios
                                    self.check.append( self.module_main[ i ] ) 
                            
                            if self.error is None:
                                if self.key_directory[ i ] == 'current':
                                    self.data_from_file = []
                            
                                    with open(file=self.module_name, mode='r') as file:
                                        for line in file.readlines():
                                            
                                            if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                            else: pass
                                            self.data_from_file.append( line )
                                    self.storage_module[ self.module_main[ i ] ] = self.data_from_file.copy()
                                else:
                                    self.data_from_file = []
                                    try:
                                        self.path_library += '/' + self.module_name
                                        with open(file=self.path_library, mode='r') as file:
                                            for line in file.readlines():
                                                if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                                else: pass
                                                self.data_from_file.append( line )
                                        self.storage_module[ self.module_main[ i ] ] = self.data_from_file   
                                        self.path_library = '/media/amiehe/KEY/black_mamba/Library'
                                    except FileNotFoundError:
                                        self.path_library = 'D:\\black_mamba\\Library'
                                        self.path_library += '/' + self.module_name
                                        with open(file=self.path_library, mode='r') as file:
                                            for line in file.readlines():
                                                if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                                else: pass
                                                self.data_from_file.append( line )
                                               
                                        self.storage_module[ self.module_main[ i ] ] = self.data_from_file   
                            else: pass
                    else: pass

                else:
                    for module in self.module_main:
                        self.module_name = module + self.termios
                        
                        if   self.module_name in self.currently_listdir:
                            if isfile( self.module_name ) == True: 
                                if self.module_name != baseFileName:
                                    self.key_directory = 'current'
                                else: 
                                    self.error = ERRORS( self.line ).ERROR8( self.module_name )
                                    break
                            else: 
                                self.error = ERRORS( self.line ).ERROR2( self.module_name )
                                break
                        elif self.module_name in self.library:
                            if isfile( path= self.path_library+'/'+self.module_name ) is True: 
                                if self.module_name != baseFileName:
                                    self.key_directory = 'library'
                                else:
                                    self.error = ERRORS( self.line ).ERROR8( self.module_name )
                                    break
                            else: 
                                self.error = ERRORS( self.line ).ERROR2( self.module_name )
                                break
                        else:        
                            self.error = ERRORS( self.line ).ERROR1( module )
                            break
                        
                    if self.error is None: 
                        self.len_module_main    = len( self.module_main )
                        self.value              = []
                        self.storage_module     = dict()

                        for i in range( self.len_module_main ):
                            self.module_name = ''
                            if not self.check:
                                self.module_name    = self.module_main[ i ] + self.termios
                                self.check.append( self.module_main[ i ] )
                            else:
                                if self.module_main[ i ] not in self.check:
                                    self.module_name    = self.module_main[ i ] + self.termios
                                    self.check.append( self.module_main[ i ] )
                                else: 
                                    self.error = ERRORS( self.line ).ERROR5( self.module_main[ i ], 'module')
                                    del self.check
                                    break
                            
                            if self.error is None:
                                if self.key_directory[ i ] == 'current':
                                    self.data_from_file = []
                            
                                    with open(file=self.module_name, mode='r') as file:
                                        for line in file.readlines():
                                            if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                            else: pass
                                            self.data_from_file.append( line )
                                            
                                    self.storage_module[ self.module_main[ i ] ] = self.data_from_file
                                else:
                                    self.data_from_file = []
                                    self.path_library += '/' + self.module_name
                                    with open(file=self.path_library, mode='r') as file:
                                        for line in file.readlines():
                                            if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                            else: pass
                                            self.data_from_file.append( line )
                                            
                                    self.storage_module[ self.module_main[ i ] ] = self.data_from_file      
                            else: pass          
                    else: pass
            else:
                for module in self.module_main:
                    self.module_name = module + self.termios
                    
                    if   self.module_name in self.currently_listdir:
                        if isfile( self.module_name ) == True: self.key_directory = 'current'
                        else: 
                            self.error = ERRORS( self.line ).ERROR2( self.module_name )
                            break
                    elif self.module_name in self.library:
                        if isfile( path= self.path_library+'/'+self.module_name ) is True: self.key_directory = 'library'
                        else: 
                            self.error = ERRORS( self.line ).ERROR2( self.module_name )
                            break
                    else:
                        self.error = ERRORS( self.line ).ERROR1( module )
                        break
                    
                if self.error is None: 
                    self.len_module_main    = len( self.module_main )
                    self.value              = []
                    self.storage_module     = dict()

                    for i in range( self.len_module_main ):
                        self.module_name    = self.module_main[ i ] + self.termios
                        if self.key_directory[ i ] == 'current':
                            self.data_from_file = []
                        
                            with open(file=self.module_name, mode='r') as file:
                                for line in file.readlines():
                                    if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                    else: pass
                                    self.data_from_file.append( line )
                            self.storage_module[ self.module_main[ i ] ] = self.data_from_file
                        else:
                            self.data_from_file = []
                            self.path_library += '/' + self.module_name
                            with open(file=self.path_library, mode='r') as file:
                                for line in file.readlines():
                                    if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                    else: pass
                                    self.data_from_file.append( line )
                                    
                            self.storage_module[ self.module_main[ i ] ] = self.data_from_file
                else: pass
        
        else:
            self.path           = self.path[ 0 ]
            self.listfir_path   = None
            
            if not self.data_base['modulesImport']['TrueFileNames']['names']:
                self.data_base['modulesImport']['TrueFileNames']['names'].append(self.module_main[0])
                self.data_base['modulesImport']['TrueFileNames']['path'].append(self.path)
                self.data_base['modulesImport']['TrueFileNames']['line'].append(0)
            else:
                if self.module_main[0] in self.data_base['modulesImport']['TrueFileNames']['names']:
                    self.idd = self.data_base['modulesImport']['TrueFileNames']['names'].index(self.module_main[0])
                    if self.data_base['modulesImport']['TrueFileNames']['path'][self.idd] is not None: pass 
                    else:
                        self.data_base['modulesImport']['TrueFileNames']['names'].append(self.module_main[0])
                        self.data_base['modulesImport']['TrueFileNames']['path'].append(self.path)
                        self.data_base['modulesImport']['TrueFileNames']['line'].append(0)
                else: 
                    self.data_base['modulesImport']['TrueFileNames']['names'].append(self.module_main[0])
                    self.data_base['modulesImport']['TrueFileNames']['path'].append(self.path)
                    self.data_base['modulesImport']['TrueFileNames']['line'].append(0)
            
            try:
                try:
                    self.listfir_path = listdir( self.path )
                except OSError : 
                    try:
                        self._sr            = '{}{}'.format('\\','\\')
                        self.newpath        = self.path.replace( '/', self._sr )
                        self.newpath        = self.newpath[ 2 : -2 ]
                        self.listfir_path   = listdir( self.newpath )
                        
                    except OSError: self.error = ERRORS( self.line ).ERROR7( self.path )

                for module in self.module_main:
                    self.module_name = module + self.termios
                    
                    if   self.module_name in self.currently_listdir:
                        if isfile( self.path+self.module_name ) == True: self.key_directory = 'current'
                        else: 
                            self.error = ERRORS( self.line ).ERROR2( self.module_name )
                            break
                    elif self.module_name in self.library:
                        if isfile( path= self.path_library+'/'+self.module_name ) is True: self.key_directory = 'library'
                        else: 
                            print(isfile(self.module_name))
                            self.error = ERRORS( self.line ).ERROR2( self.module_name )
                            break
                    else:        
                        self.error = ERRORS( self.line ).ERROR1( module )
                        break
                    
                if self.error is None: 
                    self.len_module_main    = len( self.module_main )
                    self.value              = []
                    self.storage_module     = dict()

                    for i in range( self.len_module_main ):
                        self.module_name    = self.module_main[ i ] + self.termios
                        if self.key_directory[ i ] == 'current':
                            self.data_from_file = []
                            self.newPath = self.path+self.module_name
                            with open(file=self.newPath, mode='r') as file:
                                for line in file.readlines():
                                    if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                    else: pass
                                    self.data_from_file.append( line )
                                    
                            self.storage_module[ self.module_main[ i ] ] = self.data_from_file
                        else:
                            self.data_from_file = []
                            self.path_library += '/' + self.module_name
                            with open(file=self.path_library, mode='r') as file:
                                for line in file.readlines():
                                    if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                    else: pass
                                    self.data_from_file.append( line )
                                    
                            self.storage_module[ self.module_main[ i ] ] = self.data_from_file.copy()
                             
                else: pass
            except FileNotFoundError: self.error = ERRORS( self.line ).ERROR6( self.path )
            except EOFError: self.error = ERRORS( self.line ).ERROR7( self.path )
                
        self.info = {
            'alias'         : self.alias,
            'module_load'   : self.module_load,
            'module_main'   : self.module_main
        }
        
        self.data_base['modulesImport']['TrueFileNames']['line'][ 0 ] = self.line
        return self.storage_module, self.info, self.error 

class MODULES:
    def __init__(self, DataBase: dict, line : int, values: dict, modulesLoad : dict ):
        self.DataBase           = DataBase
        self.modulesLoad        = modulesLoad
        self.values             = values
        self.line               = line
    
    def LOAD(self):
        self.error              = None
        self.alias              = self.modulesLoad[ 'alias' ]
        self.moduleMain         = self.modulesLoad[ 'module_main' ]
        self.modules            = self.modulesLoad[ 'module_load' ]
        
        self.fileNames          = self.DataBase[ 'modulesImport' ][ 'fileNames' ]
        self.expressions        = self.DataBase[ 'modulesImport' ][ 'expressions' ]
        self.moduleNames        = self.DataBase[ 'modulesImport' ][ 'moduleNames' ]
        self.check              = []
        
        if self.alias is None:
            if self.modules is None:
                if not self.fileNames:
                    for name in self.moduleMain:
                        self.expressions.append( self.values[ name ] )
                        self.fileNames.append( name )
                else:
                    for name in self.moduleMain:
                        if name not in self.moduleNames:
                            self.expressions.append( self.values[ name ] )
                            self.fileNames.append( name )
                        else: 
                            self.idd = self.fileNames.index( name )
                            self.expressions[ self.idd ] = self.values[ name ] 
                
            else:
                for v in self.modules:
                    if not self.check: self.check.append(v)
                    else:
                        if v in self.check:
                            self.error = ERRORS( self.line ).ERROR5( v, 'module' )
                            break
                        else: self.check.append(v)
                        
                if self.error is None:          
                    if not self.fileNames:
                        self.fileNames.append( self.moduleMain[ 0 ] )
                        self.moduleNames.append( self.modules )
                        self.expressions.append( self.values[ self.moduleMain[ 0 ] ] )
                    else:
                        if self.moduleMain[ 0 ] in self.fileNames:
                            self.idd = self.fileNames.index( self.moduleMain[ 0 ] )
                            self.moduleNames[ self.idd ] = self.modules
                            self.expressions[ self.idd ] = self.values[ self.moduleMain[ 0 ]  ] 
                        else:
                            self.fileNames.append( self.moduleMain[ 0 ] )
                            self.moduleNames.append( self.modules )
                            self.expressions.append( self.values[ self.moduleMain[ 0 ] ] )
                else: pass
        else:
            if self.modules is None:
                if not self.fileNames:
                    self.expressions.append( self.values[ self.moduleMain[ 0 ]  ] )
                    self.fileNames.append( self.alias )
                else:
                    if self.alias not in self.moduleNames:
                        self.expressions.append( self.values[ self.moduleMain[ 0 ]  ] )
                        self.fileNames.append( self.alias )
                    else: 
                        self.idd = self.fileNames.index( self.alias )
                        self.expressions[ self.idd ] = self.values[ self.moduleMain[ 0 ]  ] 
           
            else:
                if not self.fileNames:
                    self.fileNames.append( self.alias )
                    self.moduleNames.append( self.modules )
                    self.expressions.append( self.values[ self.moduleMain[ 0 ]  ] )
                else:
                    if self.alias in self.fileNames:
                        self.idd = self.fileNames.index( self.alias )
                        self.moduleNames[ self.idd ] = self.modules
                        self.expressions[ self.idd ] = self.values[ self.moduleMain[ 0 ]  ] 
                    else:
                        self.fileNames.append( self.alias )
                        self.moduleNames.append( self.modules )
                        self.expressions.append( self.values[ self.moduleMain[ 0 ]  ] )

        self.DataBase['modulesImport']['TrueFileNames']['line'][ 0 ] = self.line
        return self.error 
   
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
                                
            if    self.db[ 'class_names']  and not self.db[ 'func_names' ]  :
                self.star       = False
                if  info['module_load'] is not None:
                    
                    for x, name in enumerate(info['module_main']):
                        self.idd        = 0
                        for mod in info['module_load']:
                            if mod != '*':
                                if mod in self.db[ 'class_names' ]:  self.idd += 1
                                else: 
                                    self.error = ERRORS( self.line ).ERROR9( name, mod )
                                    break
                            else:
                                self.idd += 1
                                self.star = True
                        
                        if self.error is None:
                            if self.idd != 0: pass 
                            else: 
                                self.error = ERRORS( self.line ).ERROR10( name  )
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
                                    self.error = ERRORS( self.line ).ERROR9( name+".bm", mod )
                                    break
                            else: 
                                self.idd += 1
                                self.star = True
                        
                        if self.error is None:
                            if self.idd != 0: pass 
                            else: 
                                self.error = ERRORS( self.line ).ERROR10( name+".bm"  )
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
                                    self.error = ERRORS( self.line ).ERROR9( name+".bm", mod )
                                    break
                            else:
                                self.idd +=1
                                self.star = True 
                                
                        if self.error is None:
                            if self.idd != 0: pass 
                            else: 
                                self.error = ERRORS( self.line ).ERROR10( name+".bm"  )
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
            
            else: self.error = ERRORS( self.line ).ERROR11( info['module_main'][0] )

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
      
class DB:
    functionNames, functions = db.DATA_BASE().FUNCTIONS()
  
    globalDataBase          = {
        'global_vars'       : {
            'vars'          : [],
            'values'        : []
            },
        'variables'         : {
            'vars'          : [],
            'values'        : []
            },
        'irene'             : None,
        'functions'         : [],
        'classes'           : [],
        'class_names'       : [],
        'func_names'        : [],
        'loop_for'          : [],
        'loop_while'        : [],
        'loop_until'        : [],
        'continue'          : None, 
        'next'              : None,
        'pass'              : None,
        'break'             : None,
        'exit'              : None,
        'try'               : None,
        'begin'             : None,
        'if'                : [],
        'switch'            : [],
        'unless'            : [],
        'return'            : {
            'def'           : [],
            'class'         : []
            },
        'print'             : [],
        'sub_print'         : None,
        'current_func'      : None,
        'current_class'     : None,
        'transformation'    : None,
        'no_printed_values' : [],
        'line'              : None,
        'encoding'          : None,
        'importation'       : None,
        'LIB'               : {
            'func_names'    : functionNames,
            'functions'     : functions,
            'class_names'   : [],
            'classes'       : []
            },
        'modulesImport'     : {
            'moduleNames'   : [],
            'fileNames'     : [],
            'expressions'   : [],
            'variables'     : {
                'vars'      : [],
                'values'    : []
            },
            'classes'       : [],
            'class_names'   : [],
            'functions'     : [],
            'func_names'    : [],
            'mainFuncNames' : [],
            'mainClassNames': [],
            'modules'       : [],
            'modulesLoadC'  : [],
            'modulesLoadF'  : [],
            'init'          : []
        },
        'open'              : {        
            'name'          : [],          
            'file'          : [],          
            'action'        : [],         
            'status'        : [],       
            'encoding'      : [],     
            'nonCloseKey'   : []
        },
        'globalIndex'       : None,
        'starter'           : 0,
        'subFunctionNames'  : [],
        'subclassNames'     : []
    }

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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() + '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleLoadError' ).Errors() + '{}module {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR2(self, string: str):
        error = '{}is not a file. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileError' ).Errors() +'{}{} '.format(self.cyan, string) + error
        
        return self.error+self.reset
        
    def ERROR3(self, string: str):
        error = '{}is not {} a BLACK MAMBA {}file. {}line: {}{}'.format(self.white, self.red,
                                                                        self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleError' ).Errors() +'{}{} '.format(self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR4(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileNotFoundError' ).Errors() + '{}file {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR5(self, string: str, typ = 'file'):
        error = '{}{}. {}line: {}{}'.format(self.red, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() + '{}duplicated {}{} '.format( self.white, self.cyan, typ) + error

        return self.error+self.reset

    def ERROR6(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'DirectoryNotFoundError' ).Errors() + '{}directory {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR7(self, string: str):
        error = '{}is incorrect. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'OSError' ).Errors() + '{}directory path {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR8(self, string: str):
        error = '{}is not already {}open. {}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleError' ).Errors() +'{}The module {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR9(self, string: str, mod: str):
        error = '{}has not {}{} {}as a module. {}line: {}{}'.format(self.white, self.red, mod, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleLoadError' ).Errors() +'{}The file {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR10(self, string: str):
        error = '{}have been found in the file {}{}. {}line: {}{}'.format(self.white, self.red, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleLoadError' ).Errors() +'{}Any modules '.format(self.white ) + error

        return self.error+self.reset
    
    def ERROR11(self, mod: list):
        error = '{}has not any modules to load. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleLoadError' ).Errors() +'{}The file {}{} '.format(self.white, self.cyan, mod ) + error

        return self.error+self.reset
    
    def ERROR12(self, string: str):
        error = '{}is already {}open. {}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleLoadError' ).Errors() + '{}The module {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    