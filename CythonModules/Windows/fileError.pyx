from script.STDIN.LinuxSTDIN import bm_configure as bm

cdef class FileErrors:
    cdef public:
        str stringType 
    
    def __init__( self, stringType )    :
        self.stringType         = stringType 

    cpdef Errors( self )                :
        if   self.stringType == 'ValueError'        :               return bm.init.bold + bm.fg.rbg(0, 255, 0   )      + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'NameError'         :               return bm.init.bold + bm.fg.rbg(255, 0, 0   )      + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'TypeError'         :               return bm.init.bold + bm.fg.rbg(255,20, 174 )      + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'SyntaxError'       :               return bm.init.bold + bm.fg.rbg(255, 255, 0 )      + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'AttributeError'    :               return bm.init.bold + bm.fg.rbg(255, 199, 0 )      + f'{self.stringType} : ' + bm.init.reset #
        elif self.stringType == 'DomainError'       :               return bm.init.bold + bm.fg.rbg(199,21, 133 )      + f'{self.stringType} : ' + bm.init.reset #
        elif self.stringType == 'IndexError'        :               return bm.init.bold + bm.fg.rbg(252, 127, 0 )      + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'EOFError'          :               return bm.init.bold + bm.fg.rbg(128, 0, 128 )      + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'ZeroDivisionError' :               return bm.init.bold + bm.fg.rbg(0, 255, 255 )      + f'{self.stringType} : ' + bm.init.reset #
        elif self.stringType == 'ArithmeticError'   :               return bm.init.bold + bm.fg.rbg(255, 0, 255 )      + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'IndentationError'  :               return bm.init.bold + bm.fg.rbg(255, 20, 174)      + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'KeyError'          :               return bm.init.bold + bm.fg.rbg(255,140,100 )      + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'ExceptionNameError':               return bm.init.bold + bm.fg.cyan_L                 + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'OverFlowError'     :               return bm.init.bold + bm.fg.magenta_M              + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'FileNotFoundError' :               return bm.init.bold + bm.fg.yellow_L               + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'FileError'         :               return bm.init.bold + bm.fg.green_L                + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'ModuleLoadError'   :               return bm.init.bold + bm.fg.blue_L                 + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'ModuleError'       :               return bm.init.bold + bm.fg.red_L                  + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'OSError'           :               return bm.init.bold + bm.fg.rbg(255,170, 100 )     + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'DirectoryNotFoundError' :          return bm.init.bold + bm.fg.rbg(0, 255, 100  )     + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'FileModeError'     :               return bm.init.bold + bm.fg.rbg(125, 200, 100)     + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'EncodingError'     :               return bm.init.bold + bm.fg.rbg(50, 20, 200  )     + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'DecodingError'     :               return bm.init.bold + bm.fg.rbg(90, 225, 25  )     + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'UnicodeError'      :               return bm.init.bold + bm.fg.rbg(235, 100, 100  )   + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'CircularLoadingError'      :       return bm.init.bold + bm.fg.rbg(23, 100, 55  )     + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'FileNameError'     :               return bm.init.bold + bm.fg.rbg(230, 15, 55  )     + f'{self.stringType} : ' + bm.init.reset 
        elif self.stringType == 'Warning'           :               return bm.init.bold + bm.fg.rbg(230, 15, 55  )     + f'{self.stringType} : ' + bm.init.reset 
    cpdef initError( self )             :
        cdef list stringSplit

        self.stringType     =  bm.remove_ansi_chars().chars( self.stringType )
        stringSplit         = self.stringType.split( ':' )

        return stringSplit[ 0 ]
        