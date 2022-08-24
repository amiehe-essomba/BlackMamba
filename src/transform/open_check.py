import os 
from os                             import listdir
from os.path                        import isfile
from src.transform                  import error as er
from script                         import control_string

class OPEN_CHECK:
    def __init__(self, master: list, DataBase: dict, line: int) :
        self.master         = master 
        self.DataBase       = DataBase
        self.line           = line
        self.control        = control_string.STRING_ANALYSE( self.DataBase, self.line )
        
    def CHECK( self ):
        self.error          = None 
        self.name           = self.master[ 0 ]
        self.file           = self.master[ 1 ]
        self.action         = self.master[ 2 ]
        self.status         = self.master[ 3 ]
        self.encoding       = self.master[ 4 ]
        self.currently_path = os.getcwd()
        self.CurrentFiles   = listdir( self.currently_path)
        
        self.name, self.error = self.control.CHECK_NAME( self.name )
        
        if self.error is None: 
            if self.action in [ 'read', 'write']:
                if   self.action == 'read'      :
                    self.action = 'r'
                elif self.action == 'write'     :
                    self.action = 'w'
                    
                if self.status in [ 'new', 'old']: 
                    
                    if self.encoding is None: pass
                    else: 
                        if self.encoding in [ 'utf-8', 'ascii', 'utf-16', 'latin-1', 'cp1252'] : pass 
                        else: self.error = er.ERRORS( self.line ).ERROR24()
                    
                    if self.error is None:
                        if "/" in self.file: pass
                        elif "\\" in self.file: 
                            try:
                                self.s = '{}{}'.format('\\','\\')
                                self.path = self.file.split(self.s)
                                if self.path[ -1 ] == '':
                                    if len( self.path ) > 3:
                                        self.name = self.path[ -2 ]
                                        self.string = ''
                                        
                                        for v in self.path[: -2]:
                                            if v != '': self.string += v 
                                            else: self.string += self.s
                                            
                                        self.path = self.string
                                        self.listfir_path = listdir( self.path )
                                        
                                        if self.name in self.self.listfir_path:
                                            if isfile( self.name ): pass 
                                            else: self.error = er.ERRORS( self.line ).ERROR19( self.name )
                                        else: self.error = er.ERRORS( self.line ).ERROR21( self.name )
                                    else: self.error = er.ERRORS( self.line ).ERROR20( self.file )
                                else: self.error = er.ERRORS( self.line ).ERROR20( self.file )
                            except OSError:
                                self.error = er.ERRORS( self.line ).ERROR20( self.path )
                            except FileNotFoundError: 
                                self.error = er.ERRORS( self.line ).ERROR21( self.name )
                        else: 
                            if self.status == 'old':
                                if self.file in self.CurrentFiles :
                                    if isfile( self.file ): pass
                                    else: self.error = er.ERRORS( self.line ).ERROR19( self.file ) 
                                else: self.error = er.ERRORS( self.line ).ERROR21( self.file)
                            else: pass
                    else: pass
                else: self.error = er.ERRORS( self.line ).ERROR22()
            else: self.error = er.ERRORS( self.line ).ERROR23()
        else: pass
        
        return [ self.name, self.file, self.action, self.status, self.encoding ], self.error 