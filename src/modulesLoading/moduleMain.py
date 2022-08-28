import os
from os                         import listdir
from os.path                    import isfile
from script                     import control_string
from script.LEXER               import main_lexer
from src.modulesLoading         import error as er

class TREATMENT:
    def __init__(self, 
            master      : dict, 
            data_base   : dict, 
            line        : int 
            ):
        
        # current line in the main IDE
        self.line               = line
        # global module
        self.master             = master
        # main data base 
        self.data_base          = data_base
        # controling string module 
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        # lexer module 
        self.lex                = main_lexer
        # module
        self.module             = self.master['module']
        # path
        self.path               = self.master['path']
        # alias 
        self.alias              = self.master['alias']
        # module_load
        self.module_load        = self.master['module_load']
        # module main 
        self.module_main        = self.master['module_main']
        # getting path from this directory
        self.currently_path     = os.getcwd()
        # BM extension 
        self.termios            = '.bm'
        
        try:
            # case of Linux or macOs 
            # path Library in orthers terms where the Lib is located 
            self.path_library       = '/media/amiehe/KEY/black_mamba/Library'
            # get elements from current directory
            self.currently_listdir  = listdir(self.currently_path)
            # get modules from the library path 
            self.library            = listdir(self.path_library)
        except FileNotFoundError:
            # case of windows
            # path Library
            self.path_library       = 'D:\\black_mamba\\Library'
            # get elements from current directory 
            self.currently_listdir  = listdir(self.currently_path)
            # get modules from the library path 
            self.library            = listdir(self.path_library)

    def MODULE_MAIN(self, mainString: str, baseFileName : str = ''):
        # error init
        self.error                  = None
        # directory key init
        self.key_directory          = []
        # module storage init 
        self.storage_module         = None 
        self.check                  =  []
         
        if self.path is None:
            # if not path 
            if not self.data_base['modulesImport']['TrueFileNames']['names']:
                # adding module main
                self.data_base['modulesImport']['TrueFileNames']['names'].append(self.module_main[0])
                self.data_base['modulesImport']['TrueFileNames']['path'].append(None)
                self.data_base['modulesImport']['TrueFileNames']['line'].append(0)
            else:
                # updating module main
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
                    # just one element 
                    for module in self.module_main:
                        # building the true main file name with the extension 
                        self.module_name    = module + self.termios 
                        # checking if module_name is in current directory
                        if self.module_name in self.currently_listdir:
                            if isfile( self.module_name ) is True: 
                                # current or Lib directory is checking here 
                                if self.module_name != baseFileName:  self.key_directory.append( 'current' )
                                else:
                                    self.error = er.ERRORS( self.line ).ERROR8( self.module_name )
                                    break
                            else: self.error =  er.ERRORS( self.line ).ERROR2( self.module_name )
                        else:
                            # checking  if module_name is in the Lib
                            if self.module_name in self.library:
                                if isfile( path= self.path_library+'/'+self.module_name ) is True: 
                                    # current or Lib directory is checking here 
                                    if self.module_name != baseFileName:  self.key_directory.append( 'library' )
                                    else:
                                        self.error =  er.ERRORS( self.line ).ERROR8( self.module_name )
                                        break
                                else: self.error =  er.ERRORS( self.line ).ERROR2( self.module_name )
                            else:
                                self.error =  er.ERRORS( self.line ).ERROR1( self.module_name )
                                break
                       
                    if self.error is None:
                        # initialisation 
                        self.len_module_main    = len( self.module_main )
                        self.value              = []
                        self.storage_module     = dict()

                        for i in range( self.len_module_main ):
                            self.module_name = ''
                            if not self.check:
                                # building the extension 
                                self.module_name    = self.module_main[ i ] + self.termios
                                self.check.append( self.module_main[ i ] )
                            else:
                                # the BM is canceled when identical modules are in check
                                if  self.module_main[ i ] in self.check:
                                    self.error =  er.ERRORS( self.line ).ERROR5( self.module_main[ i ]+self.termios ) 
                                    del self.check
                                    break
                                else:
                                    # building the extension 
                                    self.module_name    = self.module_main[ i ] + self.termios
                                    self.check.append( self.module_main[ i ] ) 
                            
                            if self.error is None:
                                if self.key_directory[ i ] == 'current':
                                    # case of current directory 
                                    self.data_from_file = []

                                    # reading modules loading and storing theirs values in storage_module
                                    with open(file=self.module_name, mode='r') as file:
                                        for line in file.readlines():
                                            
                                            if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                            else: pass
                                            self.data_from_file.append( line )
                                    self.storage_module[ self.module_main[ i ] ] = self.data_from_file.copy()
                                else:
                                    # case of Lib directory 
                                    self.data_from_file = []
                                    try:
                                        # case of Linux of macOs 
                                        # building path 
                                        self.path_library += '/' + self.module_name
                                        # opening and reading file from Lib 
                                        with open(file=self.path_library, mode='r') as file:
                                            for line in file.readlines():
                                                if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                                else: pass
                                                self.data_from_file.append( line )
                                        self.storage_module[ self.module_main[ i ] ] = self.data_from_file   
                                        self.path_library = '/media/amiehe/KEY/black_mamba/Library'
                                    except FileNotFoundError:
                                        # case of Windows 
                                        # Lib Path 
                                        self.path_library = 'D:\\black_mamba\\Library'
                                        # building path 
                                        self.path_library += '/' + self.module_name
                                        # opening and reading file from Lib 
                                        with open(file=self.path_library, mode='r') as file:
                                            for line in file.readlines():
                                                if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                                else: pass
                                                self.data_from_file.append( line )
                                        
                                        # storing value 
                                        self.storage_module[ self.module_main[ i ] ] = self.data_from_file   
                            else: pass
                    else: pass

                else:
                    for module in self.module_main:
                        # building extension
                        self.module_name = module + self.termios
                        
                        if   self.module_name in self.currently_listdir:
                            if isfile( self.module_name ) == True: 
                                if self.module_name != baseFileName:  self.key_directory = 'current'
                                else: 
                                    self.error =  er.ERRORS( self.line ).ERROR8( self.module_name )
                                    break
                            else: 
                                self.error =  er.ERRORS( self.line ).ERROR2( self.module_name )
                                break
                        elif self.module_name in self.library:
                            if isfile( path= self.path_library+'/'+self.module_name ) is True: 
                                if self.module_name != baseFileName:
                                    self.key_directory = 'library'
                                else:
                                    self.error =  er.ERRORS( self.line ).ERROR8( self.module_name )
                                    break
                            else: 
                                self.error =  er.ERRORS( self.line ).ERROR2( self.module_name )
                                break
                        else:        
                            self.error =  er.ERRORS( self.line ).ERROR1( module )
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
                                    self.error =  er.ERRORS( self.line ).ERROR5( self.module_main[ i ], 'module')
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
                            self.error =  er.ERRORS( self.line ).ERROR2( self.module_name )
                            break
                    elif self.module_name in self.library:
                        if isfile( path= self.path_library+'/'+self.module_name ) is True: self.key_directory = 'library'
                        else: 
                            self.error =  er.ERRORS( self.line ).ERROR2( self.module_name )
                            break
                    else:
                        self.error =  er.ERRORS( self.line ).ERROR1( module )
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
            # 
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
                    # get path Linux and macOs
                    self.listfir_path = listdir( self.path )
                except OSError : 
                    try:
                        # building new path for windows when getting OSError
                        self._sr            = '{}{}'.format('\\','\\')
                        self.newpath        = self.path.replace( '/', self._sr )
                        self.newpath        = self.newpath[ 2 : -2 ]
                        self.listfir_path   = listdir( self.newpath )
                        
                    except OSError: self.error =  er.ERRORS( self.line ).ERROR7( self.path )

                for module in self.module_main:
                    # building file with an extension
                    self.module_name = module + self.termios
                    
                    if   self.module_name in self.currently_listdir:
                        # checking if file in the current directory
                        if isfile( self.path+self.module_name ) == True: self.key_directory = 'current'
                        else: 
                            self.error =  er.ERRORS( self.line ).ERROR2( self.module_name )
                            break
                    elif self.module_name in self.library:
                        # checking if file in the Lib directory
                        if isfile( path= self.path_library+'/'+self.module_name ) is True: self.key_directory = 'library'
                        else: 
                            self.error =  er.ERRORS( self.line ).ERROR2( self.module_name )
                            break
                    else:        
                        self.error =  er.ERRORS( self.line ).ERROR1( module )
                        break
                    
                if self.error is None: 
                    self.len_module_main    = len( self.module_main )
                    self.value              = []
                    # storing module initialized
                    self.storage_module     = dict()

                    for i in range( self.len_module_main ):
                        self.module_name    = self.module_main[ i ] + self.termios
                        if self.key_directory[ i ] == 'current':
                            # current directory
                            self.data_from_file = []
                            self.newPath = self.path+self.module_name
                            # opening , reading and storing values in data_from_file
                            with open(file=self.newPath, mode='r') as file:
                                for line in file.readlines():
                                    if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                    else: pass
                                    self.data_from_file.append( line )
                            
                            # storing values in a dictionary     
                            self.storage_module[ self.module_main[ i ] ] = self.data_from_file
                        else:
                            # Lib directory
                            self.data_from_file = []
                            self.path_library += '/' + self.module_name
                            # opening , reading and storing values in data_from_file
                            with open(file=self.path_library, mode='r') as file:
                                for line in file.readlines():
                                    if line[-1] == '\n': line, _ = self.control.DELETE_SPACE( line[:-1] )
                                    else: pass
                                    self.data_from_file.append( line )
                            
                            # storing values in a dictionary  
                            self.storage_module[ self.module_main[ i ] ] = self.data_from_file.copy()
                else: pass
            except FileNotFoundError: self.error =  er.ERRORS( self.line ).ERROR6( self.path )
            except EOFError: self.error =  er.ERRORS( self.line ).ERROR7( self.path )
        
        # final configuration for loading module
        self.info = {
            'alias'         : self.alias,
            'module_load'   : self.module_load,
            'module_main'   : self.module_main
        }
        
        # updating GteLine() 
        self.data_base['modulesImport']['TrueFileNames']['line'][ 0 ] = self.line
        
        return self.storage_module, self.info, self.error 