##############################################
# modules importation                        #
# ############################################
# from module iris load iris as i            #
#                                            #
# **created by :  amiehe-essomba**           #
# **updating by : amiehe-essomba**           #
##############################################

import os
from os                         import listdir
from os.path                    import isfile
from pathlib                    import Path
from script                     import control_string
from script.LEXER               import main_lexer
from src.modulesLoading         import error as er
from src.modulesLoading         import build_abs_Lib_path as bpath

class TREATMENT:
    def __init__(self, 
            master      : dict, 
            data_base   : dict, 
            line        : int,
            system      : str = 'windows'
            ) -> None:
        
        # current line in the main IDE
        self.line               = line
        # global module
        self.master             = master
        # main data base 
        self.data_base          = data_base
        # system name
        self.system             = system
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
        os.path.join(os.environ.get("_MEIPASS", self.currently_path), "")
        # BM extension 
        self.termios            = '.bm'
        # get relative path
        self.relative_path      = Path(__file__).resolve().parents[2]
        os.path.join(os.environ.get("_MEIPASS", self.relative_path), "")
        # path Library in orthers words where the Lib is located
        self.path_library  = bpath.Lib_Path( root = self.relative_path, sys = self.system).getPath()
        # get elements from current directory
        self.currently_listdir = listdir(self.currently_path)
        # get modules from the library path
        self.library = listdir(self.path_library)

    def MODULE_MAIN(self,
                mainString: str,
                baseFileName : str = ''
                ) -> tuple:

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
                                self.lib_path = bpath.Lib_Path( root = self.relative_path,
                                              sys = self.system).getFile_in_Path( self.module_name)

                                if isfile( path=self.lib_path ) is True:
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
                                            if line[-1] == '\n': line = line[ : -1 ]
                                            else: pass
                                            self.data_from_file.append( line )
                                    self.storage_module[ self.module_main[ i ] ] = self.data_from_file.copy()
                                else:
                                    # case of Lib directory 
                                    self.data_from_file = []
                                    self.lib_path = bpath.Lib_Path(root=self.relative_path,
                                                                   sys=self.system).getFile_in_Path(self.module_name)
                                    # reading the opening file
                                    with open(file=self.lib_path, mode='r') as file:
                                        for line in file.readlines():
                                            if line[ -1 ] == '\n':  line = line[ : -1]
                                            else:  pass
                                            # storing each line in data_from_file
                                            self.data_from_file.append( line )
                                    self.storage_module[ self.module_main[ i ] ] = self.data_from_file
                            else: pass
                    else: pass
                else:
                    for module in self.module_main:
                        # building extension
                        self.module_name = module + self.termios
                        
                        if   self.module_name in self.currently_listdir:
                            if isfile( self.module_name ) == True: 
                                if self.module_name != baseFileName:  self.key_directory.append( 'current' )
                                else: 
                                    self.error =  er.ERRORS( self.line ).ERROR8( self.module_name )
                                    break
                            else: 
                                self.error =  er.ERRORS( self.line ).ERROR2( self.module_name )
                                break
                        elif self.module_name in self.library:
                            self.lib_path = bpath.Lib_Path(root=self.relative_path,
                                                           sys=self.system).getFile_in_Path(self.module_name)
                            if isfile( path= self.lib_path) is True:
                                if self.module_name != baseFileName:
                                    self.key_directory.append('library')
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
                                            if line[-1] == '\n': line = line[ : -1 ]
                                            else: pass
                                            self.data_from_file.append( line )
                                    self.storage_module[ self.module_main[ i ] ] = self.data_from_file
                                else:
                                    self.data_from_file = []
                                    self.lib_path = bpath.Lib_Path(root=self.relative_path,
                                                                   sys=self.system).getFile_in_Path(self.module_name)
                                    with open(file=self.lib_path, mode='r') as file:
                                        for line in file.readlines():
                                            if line[-1] == '\n': line = line[ : -1]
                                            else: pass
                                            self.data_from_file.append( line )
                                    self.storage_module[ self.module_main[ i ] ] = self.data_from_file      
                            else: pass          
                    else: pass
            else:
                for module in self.module_main:
                    self.module_name = module + self.termios
                    
                    if   self.module_name in self.currently_listdir:
                        if isfile( self.module_name ) == True: self.key_directory.append( 'current' )
                        else: 
                            self.error =  er.ERRORS( self.line ).ERROR2( self.module_name )
                            break
                    elif self.module_name in self.library:
                        self.lib_path = bpath.Lib_Path(root=self.relative_path,
                                                       sys=self.system).getFile_in_Path(self.module_name)
                        if isfile( path= self.lib_path ) is True: self.key_directory.append( 'library' )
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
                                    if line[-1] == '\n': line = line[ : -1]
                                    else: pass
                                    self.data_from_file.append( line )
                            self.storage_module[ self.module_main[ i ] ] = self.data_from_file
                        else:
                            self.data_from_file = []
                            self.lib_path = bpath.Lib_Path(root=self.relative_path,
                                                           sys=self.system).getFile_in_Path(self.module_name)
                            with open(file=self.lib_path, mode='r') as file:
                                for line in file.readlines():
                                    if line[-1] == '\n': line = line[ : -1 ]
                                    else: pass
                                    self.data_from_file.append( line )
                            self.storage_module[ self.module_main[ i ] ] = self.data_from_file
                else: pass
        else:
            self.path           = self.path[ 0 ]
            self.listfir_path   = None
            # if any modules were not defined 
            if not self.data_base['modulesImport']['TrueFileNames']['names']:
                # module name 
                self.data_base['modulesImport']['TrueFileNames']['names'].append(self.module_main[0])
                # module location
                self.data_base['modulesImport']['TrueFileNames']['path'].append(self.path)
                # line 
                self.data_base['modulesImport']['TrueFileNames']['line'].append(0)
            else:
                # if module_main[0] is not found 
                if self.module_main[0] in self.data_base['modulesImport']['TrueFileNames']['names']:
                    # updationg the module already load 
                    self.idd = self.data_base['modulesImport']['TrueFileNames']['names'].index(self.module_main[0])
                    if self.data_base['modulesImport']['TrueFileNames']['path'][self.idd] is not None: pass 
                    else:
                        self.data_base['modulesImport']['TrueFileNames']['names'].append(self.module_main[0])
                        self.data_base['modulesImport']['TrueFileNames']['path'].append(self.path)
                        self.data_base['modulesImport']['TrueFileNames']['line'].append(0)
                # if module_main[0] is found 
                else: 
                    # storing the module name
                    self.data_base['modulesImport']['TrueFileNames']['names'].append(self.module_main[0])
                    # storing the module mocation 
                    self.data_base['modulesImport']['TrueFileNames']['path'].append(self.path)
                    # storing the line 
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
                        if isfile( self.path+self.module_name ) == True: self.key_directory.append( 'current' )
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
                                    if line[-1] == '\n': line = line[ : -1]
                                    else: pass
                                    self.data_from_file.append( line )
                            # storing values in a dictionary
                            self.storage_module[ self.module_main[ i ] ] = self.data_from_file
                        else:
                            self.error = er.ERRORS(self.line).ERROR2(self.module_name)
                            break
                else: pass
            except FileNotFoundError: self.error =  er.ERRORS( self.line ).ERROR6( self.path )
            except EOFError: self.error =  er.ERRORS( self.line ).ERROR7( self.path )
        
        # final configuration for loading modules which contains
        # * the alias for connecting main module to an alias
        # * the modules load which come from the main module
        # * the main module name

        self.info = {
            'alias'         : self.alias,
            'module_load'   : self.module_load,
            'module_main'   : self.module_main
        }
        
        # updating GteLine() 
        self.data_base['modulesImport']['TrueFileNames']['line'][ 0 ] = self.line
        
        return self.storage_module, self.info, self.error 