from src.functions                      import error as er

class SET_OPEN_FILE:
    def __init__(self,
                master      : dict, 
                DataBase    : dict, 
                line        : int
                ):
        self.DataBase       = DataBase 
        self.master         = master 
        self.line           = line 
        
    def SET_OPEN(self):
        self.name           = self.master['name'][0]
        self.file           = self.master['file'][0]
        self.action         = self.master['action'][0]
        self.status         = self.master['status'][0]
        self.encoding       = self.master['encoding'][0]
        self.nonCloseKey    = self.master['nonCloseKey'][0]
        self.error          = None
        
        if not self.DataBase['open']['name']:
            self.DataBase['open']['name'].append( self.name )
            self.DataBase['open']['file'].append( self.file )
            self.DataBase['open']['action'].append( self.action )
            self.DataBase['open']['status'].append( self.status )
            self.DataBase['open']['encoding'].append( self.encoding )
            self.DataBase['open']['nonCloseKey'].append( self.nonCloseKey )
        else:
            if self.name in self.DataBase['open']['nonCloseKey']: self.error = er.ERRORS( self.line ).ERROR21( self.name )
            else:
                self.DataBase['open']['name'].append( self.name )
                self.DataBase['open']['file'].append( self.file )
                self.DataBase['open']['action'].append( self.action )
                self.DataBase['open']['status'].append( self.status )
                self.DataBase['open']['encoding'].append( self.encoding )
                self.DataBase['open']['nonCloseKey'].append( self.name )
        
        return self.error
