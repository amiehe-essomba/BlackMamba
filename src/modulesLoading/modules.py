##############################################
# modules importation                        #
# ############################################
# from module iris load iris as i            #
#                                            #
# created by :  amiehe-essomba               #
# updating by : amiehe-essomba               #
############################################## 

from src.modulesLoading             import error as er

class MODULES:
    def __init__(self,
            DataBase    : dict,
            line        : int,
            values      : dict,
            modulesLoad : dict
            ) -> None:

        # main data base
        self.DataBase           = DataBase
        # dictionary from moduleMain
        self.modulesLoad        = modulesLoad
        # value
        self.values             = values
        # current line
        self.line               = line
    
    def LOAD(self) -> str :
        # error
        self.error              = None
        # when alias is created
        self.alias              = self.modulesLoad[ 'alias' ]
        # main module name 
        self.moduleMain         = self.modulesLoad[ 'module_main' ]
        # functions or classes loading 
        self.modules            = self.modulesLoad[ 'module_load' ]
        # file name 
        self.fileNames          = self.DataBase[ 'modulesImport' ][ 'fileNames' ]
        # expression 
        self.expressions        = self.DataBase[ 'modulesImport' ][ 'expressions' ]
        # and modules
        self.moduleNames        = self.DataBase[ 'modulesImport' ][ 'moduleNames' ]
        self.check              = []
        
        # not alias 
        if self.alias is None:
            if self.modules is None:
                # new module loading, when module is None it means that (*) was used to load all functions or classes 
                # from the module main
                if not self.fileNames:
                    for name in self.moduleMain:
                        self.expressions.append( self.values[ name ] )
                        self.fileNames.append( name )
                else:
                    # updating module loading before 
                    for name in self.moduleMain:
                        if name not in self.moduleNames:
                            self.expressions.append( self.values[ name ] )
                            self.fileNames.append( name )
                        else: 
                            self.idd = self.fileNames.index( name )
                            self.expressions[ self.idd ] = self.values[ name ]
            else:
                # in this case, modules were selected
                for v in self.modules:
                    if not self.check: self.check.append(v)
                    else:
                        if v in self.check:
                            self.error = er.ERRORS( self.line ).ERROR5( v, 'module' )
                            break
                        else: self.check.append(v)
                        
                if self.error is None:   
                    # new modules        
                    if not self.fileNames:
                        self.fileNames.append( self.moduleMain[ 0 ] )
                        self.moduleNames.append( self.modules )
                        self.expressions.append( self.values[ self.moduleMain[ 0 ] ] )
                    else:
                        # updating old module loading before 
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
            # case of aliases 
            if self.modules is None:
                # new modules 
                if not self.fileNames:
                    self.expressions.append( self.values[ self.moduleMain[ 0 ]  ] )
                    self.fileNames.append( self.alias )
                else:
                    # adding new alias
                    if self.alias not in self.moduleNames:
                        self.expressions.append( self.values[ self.moduleMain[ 0 ]  ] )
                        self.fileNames.append( self.alias )
                    else: 
                        # updating alias already load before 
                        self.idd = self.fileNames.index( self.alias )
                        self.expressions[ self.idd ] = self.values[ self.moduleMain[ 0 ]  ] 
           
            else:
                # updating modules
                if not self.fileNames:
                    self.fileNames.append( self.alias )
                    self.moduleNames.append( self.modules )
                    self.expressions.append( self.values[ self.moduleMain[ 0 ]  ] )
                else:
                    # adding new alias
                    if self.alias in self.fileNames:
                        self.idd = self.fileNames.index( self.alias )
                        self.moduleNames[ self.idd ] = self.modules
                        self.expressions[ self.idd ] = self.values[ self.moduleMain[ 0 ]  ] 
                    else:
                        # updating alias already load before 
                        self.fileNames.append( self.alias )
                        self.moduleNames.append( self.modules )
                        self.expressions.append( self.values[ self.moduleMain[ 0 ]  ] )

        # initialize line for GetLine() function 
        self.DataBase['modulesImport']['TrueFileNames']['line'][ 0 ] = self.line
        
        return self.error 