from script.STDIN.LinuxSTDIN                import bm_configure as bm
from CythonModules.Linux                    import fileError as fe

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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}due to {}<< . >> .{}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white,self.cyan, string) + error

        return self.error+self.reset

    def ERROR2(self, string: str):
        error = '{}was not found. line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors()+'{}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR3(self, string: str, _char_ = 'an integer()', func = '' ):
        error = '{}is not {}{} {}type. {}line: {}{}'.format(self.white, self.blue, _char_, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error+self.reset

    def ERROR4(self, string: str, _char_ = 'an integer'):
        error = '{}to  {}{}() {}type. {}line: {}{}'.format(self.white, self.blue, _char_, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}impossible to convert {}<< {} >> '.format(self.white,self.cyan, string) + error

        return self.error+self.reset

    def ERROR5(self, string: str, key: str):
        error = '{}was not found in {}<< {} >>. {}line: {}{}'.format(self.white, self.red, string, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'KeyError' ).Errors()+'{}<< {} >> '.format(self.cyan, key) + error

        return self.error+self.reset

    def ERROR6(self, value):
        error = '{}a tuple(), {}or a string(), {}type. {}line: {}{}'.format(self.blue, self.cyan, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> {}is not {}a list(), '.format(self.cyan, value, self.white, self.yellow) + error
        return self.error+self.reset

    def ERROR7(self, op, ob1, ob2):
        error = '{}<< {}{} >>, {} and {}<< {}{} >>. {}type. {}line: {}{}'.format(self.white, ob1, self.white, 
                                                self.white, self.white, ob2, self.whie, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {}{}{} >> {}not supported between '.format(self.cyan, self.yellow,
                                                                                                             op, self.cyan, self.white) + error
        return self.error+self.reset

    def ERROR8(self, value):
        error = '{}<< EMPTY >>. {}line: {}{}'.format( self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'SyntaxError' ).Errors()+'{}<< {} >> {}is '.format(self.cyan, value, self.white) + error
        return self.error+self.reset

    def ERROR9(self, string: str = 'float' ):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'OverFlowError' ).Errors()+'infinity {}{} {}number. '.format(self.magenta, string, self.white) + error
        return self.error+self.reset

    def ERROR10(self):
        self.error =  fe.FileErrors( 'IndentationError' ).ErrorIden()
        return self.error

    def ERROR11(self, string: str, key: str): #
        error = '{}has not {}<< {} >> {}as argument. {}line: {}{}'.format(self.white, self.red, key, self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'KeyError' ).Errors()+'{}<< {}( ) >> '.format(self.cyan, string ) + error
        return self.error+self.reset

    def ERROR12(self, string: str, pos1: int):
        char = ''
        if pos1 > 1:
            char = 'arguments'
        else:
            char = 'argument'

        error = '{}takes {}<< {} >> {}{}. {}line: {}{}'.format(self.white, self.red, pos1, self.yellow, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}<< {}( ) >> '.format(self.cyan, string ) + error
        return self.error+self.reset

    def ERROR13(self, string:str, name = 'class'): #
        self.error = None 
        
        if name == 'class':
            error = '{}was not found. {}line: {}{}'.format(self.green,  self.white, self.yellow, self.line )
            self.error = fe.FileErrors( 'NameError' ).Errors()+'{}{} name {}ERROR. {}<< {} >> '.format(self.white,
                                                                            name, self.yellow, self.cyan, string) + error
        else:
            error = '{}has not {}<< {} >> {} as a function. {}line: {}{}'.format( self.white, self.red, name, self.yellow, self.white,
                                                                                 self.yellow, self.line )
            self.error = fe.FileErrors( 'NameError' ).Errors()+'{}class {}<< {} >> '.format(self.white, self.cyan, string) + error
                                                                           
        
        return self.error+self.reset

    def ERROR14(self, string: str, typ = ''): #
        error = '{}takes {}no arguments. {}line: {}{}'.format(self.white, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}{}( ) {}{} '.format(self.cyan, string, self.red, typ) + error

        return self.error+self.reset

    def ERROR15(self, string: str, value: list): #
        self.list = []
        self.len = len( value )
        if self.len <= 1:
            self._string_ = 'argument'
        else:
            self._string_ = 'arguments'

        for _value_ in value:
            self.list.append( _value_[ 0 ] )

        error = '{}missing {}<< {} >> {}required {}: {}{}. {}line: {}{}'.format(self.green, self.red, self.len, self.white, self._string_, self.blue,
                                                                            self.list,  self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}in {}<< {}( ) >>, '.format(self.white, self.cyan, string) + error
        return self.error+self.reset 

    def ERROR16(self, string: str,key: str):
        error = '{}duplicated keyword argument {}<< {} >>. {}line: {}{}'.format(self.white, self.red, key, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{} in {}<< {}( ) >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR17(self, string):
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format(self.green, self.white, self.cyan, string, self.white,
                                                                                            self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. '.format( self.white ) + error
        return self.error+self.reset
    
    def ERROR18(self, string: str, func: str = ''):
        error = '{}with {}{}. {}line: {}{}'.format(self.white, self.cyan, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors()+'{}could not associate {}any() {}type '.format( self.white, self.yellow, 
                                                                                                              self.white ) + error + func
        return self.error+self.reset


    def ERROR19(self, name: str, key: str, func : str = ''):
        error = '{}duplicated {}<< {} >> {}type {}for the argument {}{}. {}line: {}{}'.format(self.white, self.red, key, self.green, self.white, self.cyan, name,
                                                                                          self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ error + func

        return self.error+self.reset
    
    def ERROR20(self, func: str = '' ):
        error = '{}{} {}cannot be defined in {}intialize( ) {}function. {}line: {}{}'.format(self.red, func, self.white, self.red, self.green,
                                                                                             self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ error 

        return self.error+self.reset
     
    def ERROR21(self, string: str, name: str  ): #
        error = '{}has not {}<< {} >> {}as argument. {}line: {}{}'.format(self.white, self.blue, name, self.yellow, 
                                                                          self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'AttributeError' ).Errors()+'{}{} {}class '.format(self.cyan, string, self.red) + error

        return self.error+self.reset

    def ERROR22(self, string: str, name = 'string()'): #
        error = '{}has not {}<< {} >> {}as a function. {}line: {}{}'.format(self.white, self.green, string, self.red,
                                                                             self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors()+'{}{} {}type '.format(self.cyan, name, self.yellow) + error

        return self.error+self.reset
    
    def ERROR23(self, string: str): #
        error = '{}is not in the list {}[ {}keys{}, {}items {}]. {}line: {}{}'.format(self.white, self.green, self.red, self.white, self.magenta, self.green,
                                                                             self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}{} '.format(self.cyan, string) + error

        return self.error+self.reset 
    
    def ERROR24(self, string: str = 'dictionary'): #
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line )                                   
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}EMPTY {}{} .'.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR25(self,  key: str): #
        error = '{}was not found in the {}dictionary(). {}line: {}{}'.format(self.white, self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'KeyError' ).Errors()+'{}<< {} >> '.format(self.cyan, key) + error

        return self.error+self.reset

    def ERROR26(self, string: str, char: str): #
        error = '{}due to {}<< {} >>. {}line: {}{}'.format(self.white, self.red, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan , string) + error

        return self.error+self.reset 
    
    def ERROR27(self, string: str, s : str='list' ): #
        error = '{}was not found in the {}{}. {}line: {}{}'.format(self.white, self.yellow, s, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}<< {} >> '.format(self.cyan , string) + error

        return self.error+self.reset
    
    def ERROR28(self, func = 'list', c:str = ''): #
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'IndexError' ).Errors()+'{}{} {}index {}out of range. '.format(self.yellow, func, self.red, self.white) + error

        return self.error+self.reset
    
    def ERROR29(self, s : str = 'master'): #
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}length( {}{}{} ) {}!= {}2. '.format(self.cyan, self.red, s, self.cyan, self.white, 
                                                                self.cyan) + error

        return self.error+self.reset
    
    def ERROR30(self, s : str = 'numeric'): #
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}abs( {}{}{} ) {}is lower than {}0. '.format(self.cyan, self.red, s, self.cyan, self.white, 
                                                                self.cyan) + error

        return self.error+self.reset
    
    def ERROR31(self, value): #
        error = '{}a tuple(), {} a dictionary() {}or a string(), {}type. {}line: {}{}'.format(self.blue, self.magenta, self.cyan, self.yellow, 
                                                                                            self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> {}is not {}a list(), '.format(self.cyan, value, self.white, self.yellow) + error
        return self.error+self.reset
    
    def ERROR32(self, value: list): #
        falseValue = None
        for v in value :
            if type( v ) != type( str() ):
                falseValue = v 
                break 
        
        self.error = ERRORS( self.line ).ERROR3( falseValue, 'a string()')
      
        return self.error+self.reset

    def ERROR33(self, value: str): #
        error = '{}was not found in the {}string. {}line: {}{}.'.format(self.white, self.magenta, 
                                                                            self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}<< {} >> '.format(self.cyan, value) + error
        return self.error+self.reset
    
    
    def ERROR34(self, value: str): #
        error = '{}cannot be negative. {}line: {}{}.'.format(self.white, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}{} '.format(self.cyan, value) + error
        return self.error+self.reset
    
    def ERROR35(self, value: int): #
        error = '{}is not a{}boolean(), {}a float() or {}an integer() {}type. {}line: {}{}.'.format(self.white, self.magenta, self.green, 
                                                                    self.red, self.yellow,self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}list index {}<< {} >> '.format(self.white, self.cyan, value) + error
        return self.error+self.reset
    
    def ERROR36(self, string: str): #
        error = '{}was not found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileNotFoundError' ).Errors() + '{}file {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR37(self, string: str, mode: str): #
        if mode == 'w': mode = 'write'
        else: mode = 'read'
        
        error = '{}is {}{} only {}mode. {}line: {}{}'.format(self.white, self.red, mode, self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileModeError' ).Errors() + '{}file {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR38(self, idd : int): #
        
        error = '{}is not a {}a string() {}type. {}line: {}{}'.format(self.white, self.magenta, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}list index {}{} '.format( self.white, self.cyan, idd) + error

        return self.error+self.reset
    
    def ERROR39(self): #
        
        error = '{}line: {}{}'.format( self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'EncodingError' ).Errors() + '{}got an encoding {}ERROR '.format( self.white, self.yellow ) + error

        return self.error+self.reset
    
    def ERROR40(self): #
        
        error = '{}line: {}{}'.format( self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'DecodingError' ).Errors() + '{}got a decoding {}ERROR '.format( self.white, self.yellow ) + error

        return self.error+self.reset
    
    def ERROR41(self): #
        
        error = '{}line: {}{}'.format( self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'UnicodeError' ).Errors() + '{}got a unicode {}ERROR '.format( self.white, self.yellow ) + error

        return self.error+self.reset
    
    def ERROR42(self, string: str, name: str): #
        
        error = '{}as {}function {}or {}class. {}line: {}{}'.format( self.white, self.cyan, self.white, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors() + '{}{} {}has not {}{} '.format( self.red, string, self.white, self.green, name ) + error

        return self.error+self.reset
    
    def ERROR43(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleError' ).Errors() +'{}The module {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR44(self, string: str, name: str):
        error = '{}has not {}{} {}as class. {}line: {}{}'.format(self.white, self.red, name, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}The class {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR45(self, string: str, name: str):
        error = '{}has not {}{} {}as class. {}line: {}{}'.format(self.white, self.red, name, self.yellow,
                                                                                 self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}The module {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR46(self, string: str, name: str):
        error = '{}has not {}{} {}as function. {}line: {}{}'.format(self.white, self.red, name,  self.blue,
                                                                                 self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}The module {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR47(self, s: str = 'max_step'):
        error = '{}cannot be {}<= 0. {}line: {}{}'.format(self.white, self.red,  self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() +'{}{} '.format(self.cyan, s) + error

        return self.error+self.reset

    def ERROR48(self, s1: str = 'max_num1', s2 : str = 'max_num2'):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() +'{}{} {}== {}{} '.format(self.cyan, s1, self.red, self.cyan, s2) + error

        return self.error+self.reset

    def ERROR49(self, value : str = 'master'):
        error = '{}a tuple(), {}or {}an integer(), {}type. {}line: {}{}'.format(self.blue, self.white, self.red, self.yellow, self.white,
                                                                                self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> {}is not '.format(self.cyan, value, self.white) + error
        return self.error+self.reset
    
    def ERROR50(self, value : str = 'master'):
        error = '{}a tuple(), {}or {}a list(), {}type. {}line: {}{}'.format(self.blue, self.white, self.yellow, self.yellow, self.white,
                                                                                self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> {}is not '.format(self.cyan, value, self.white) + error
        return self.error+self.reset
    
    def ERROR51(self, value : str = 'a boolean()', s : str = "reverse"):
        error = '{}{} {}type. {}line: {}{}'.format(self.blue, value, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}The first value of {}{} {}is not a '.format(self.white, self.green, s, self.white) + error
        return self.error+self.reset
    
    def ERROR52(self, s : str = 'reverse'):
        error = '{}!=  {}2. {}line: {}{}'.format(self.red, self.cyan, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}length( {}{}{} ) '.format(self.white, self.green, s, self.white) + error
        return self.error+self.reset
    
    def ERROR53(self, value : str = ['keys', 'values'], s : str = "reverse"):
        error = '{}{}. {}line: {}{}'.format(self.blue, str(value), self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}The first value of {}{} {}is not in '.format(self.white, self.green, s, self.white) + error
        return self.error+self.reset
    
    def ERROR54(self):
        error = '. {}line: {}{}'.format(  self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}Sorting impossible '.format( self.cyan ) + error
        return self.error+self.reset
    
    def ERROR55(self, ncol : int = 0):
        error = '. {}line: {}{}'.format(  self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}axis {}cannot be higher than {}{}'.format( self.cyan, self.white, self.red, ncol-1 ) + error
        return self.error+self.reset
    
    def ERROR56(self, name: str = "round"):
        error = 'as a function. {}line: {}{}'.format(  self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'NameError' ).Errors()+'{}ndarray {}has not {}{} {}'.format( self.cyan, self.white, self.red, name,  self.white) + error
        return self.error+self.reset
    
    def ERROR57(self, name: str = "ncol", max_ : int = 0):
        error = '{}line: {}{}'.format(  self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}{} not in {}]0, {}[ '.format( self.cyan, name,  self.red, max_) + error
        return self.error+self.reset

    def ERROR58(self, name: str = "ncol", max_ : int = 0):
        error = '{}to create {}nrow .{}line: {}{}'.format(self.white, self.green, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}{} % {}{} {}is not an {}ineter() {}type '.format( self.cyan, max_, self.green, name, 
                                                                                                self.white, self.red, self.yellow) + error
        return self.error+self.reset