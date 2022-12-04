from script                     import control_string

class STDIN:

    def __init__(self, 
                data_base   :dict, 
                line        :int
                ):
        
        self.data_base          = data_base
        self.line               = line
        self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)

    def STDIN(self, 
            color   :dict, 
            tab     :int, 
            _type_  :str = '...',
            name    :str ="python"
            ):

        self.string_concatenate = str( input('{}{} {}'.format(color[ '0' ], _type_, color[ '1' ])) )
        self.normal_string      = self.string_concatenate

        self.string_concatenate, self.tab_activate, self.error = self.analyse.BUILD_CON( self.string_concatenate, tab )
        self.normal_string      = self.analyse.BUILD_NON_CON( self.normal_string, tab )

        if name == 'cython':
            if self.error is None: self.error = ""
            else: pass 
        else: pass 
        
        return self.string_concatenate, self.normal_string, self.tab_activate, self.error

    def NORMAL_STDIN(self, color: dict, type = '... '):
        self.string_concatenate = str( input( '{}{}{}'.format( color[ '0' ], type, color[ '1' ] ) ) )

        return self.string_concatenate
    
    def STDIN_FOR_INTERPRETER( self, tab: int, string : str = '' ):
        
        self.string_concatenate = string 
        self.normal_string      = self.string_concatenate
        self.string_concatenate, self.tab_activate, self.error = self.analyse.BUILD_CON( self.string_concatenate, tab )
        self.normal_string      = self.analyse.BUILD_NON_CON( self.normal_string, tab )

        return self.string_concatenate, self.normal_string, self.tab_activate, self.error
       
    def ENCODING( self, string : str ):
        n = 0 # using for counting 
        
        for s in string:
            if s == '\t':  n +=1 
            else: break
        
        return n 
    
    def GROUPBY(self, 
                tabulation  : int    = 1,            # tabulation 
                LIST        : list   = [],           # list of values 
                index       : str    = 'out',        # out if the structure just started else it take int value
                _class_     : bool   = False
                ):
        
        # the index value is the very important parameter for controling how the values are selected 
       
        self.newList = []
        
        if LIST:
            if index == 'out':
                for i, _str_ in enumerate(LIST):
                    self.n = STDIN( self.data_base, self.line).ENCODING( _str_ )
                    if self.n+1 > tabulation:
                        self.newList.append( _str_ )  
                    elif self.n+1 == tabulation:
                        if self.n == 0:
                            if _str_ != 'end:':
                                self.newList.append( _str_ )  
                            else:
                                self.newList.append( _str_ )  
                                break 
                        else:
                            if _str_[tabulation : ] != 'end:':
                                self.newList.append( _str_ )  
                            else:
                                self.newList.append( _str_ )  
                                break
                    else: break
            else:
                for i, _str_ in enumerate(LIST):
                    self.n = STDIN( self.data_base, self.line).ENCODING( _str_ )
                   
                    if self.n >= tabulation:
                        self.newList.append( _str_ ) 
                        if _class_ is False: pass
                        else:
                           
                            if _str_[tabulation : ] == 'end:' : break 
                            else: pass
                    else: break
        else: pass 
        
        return self.newList
    def IF(self, 
            tabulation  : int    = 1,            # tabulation 
            LIST        : list   = [],           # list of values 
            _class_     : bool   = False
            ):
        self.newList = []
        
        if LIST:
            for i, _str_ in enumerate(LIST):
                self.n = STDIN( self.data_base, self.line).ENCODING( _str_ )
                
                if self.n > tabulation:
                    self.newList.append( _str_ ) 
                    #if _class_ is False: pass
                    #else:
                    #    if _str_[tabulation : ] == 'end:' : break 
                    #    else: pass
                else: break
        else: pass 
        
        return self.newList
    
    def FOR_STRING(self, tabulation: int = 1,  LIST: list = []):
        self.newList = []
        
        if LIST:
            for i, _str_ in enumerate(LIST):
                self.n = STDIN( self.data_base, self.line).ENCODING( _str_ )
                if self.n+1 > tabulation:
                    self.newList.append( _str_ )  
                else: break
        else: pass 
        
        return self.newList
        