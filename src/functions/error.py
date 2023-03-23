from script.STDIN.LinuxSTDIN            import bm_configure as bm
from CythonModules.Windows              import fileError as fe 

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
        error = '{}a tuple(), {}or a string(), {}type. {}line: {}{}'.format(self.blue, self.cyan, self.yellow, self.white, self.yeloow, self.line)
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
        self.error =  fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                                        self.white, self.yellow, self.line )
        return self.error+self.reset

    def ERROR11(self, string: str, key: str):
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

    def ERROR13(self, string:str):
        error = '{}was not found. {}line: {}{}'.format(self.green,  self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'NameError' ).Errors()+'{}function name {}ERROR. {}<< {} >> '.format(self.white, self.yellow, self.cyan, string) + error

        return self.error+self.reset

    def ERROR14(self, string: str):
        error = '{}takes {}no arguments. {}line: {}{}'.format(self.white, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}<< {}( ) >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR15(self, string: str, value: list):
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}<< {}( ) >> '.format(self.cyan, string) + error

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
    
    def ERROR21(self, name: str):
        error = '{}before {}new opening. {}line: {}{}'.format(self.white, self.cyan, self.white, self.yellow, self.line)        
        self.error = fe.FileErrors( 'FileError' ).Errors() + '{}close {}{} '.format(self.white, self.red, name) + error

        return self.error+self.reset
    
    def ERROR22( self, string ):
        error = '{}already exits. {}line: {}{}'.format(self.yellow, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('NameError').Errors() + '{}the function name {}{} '.format(self.white, self.red, string,) + error
        return self.error + self.reset
    
    def ERROR23( self, string ):
        error = '{}cannot be {}a function. {}line: {}{}'.format(self.white, self.yellow, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}The subfunction {}{} '.format(self.white,  self.red, string) + error
        return self.error + self.reset
    
    def ERROR24( self, string1, string2 ):
        error = '{}instead {} {}type. {}line: {}{}'.format(self.white, string2, self.white, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('TypeError').Errors() + '{}returning type error. got {} '.format(self.white,  string1) + error
        return self.error + self.reset
    
    def ERROR25( self, name: str  ):
        error = '{}cannot return any values. {}line: {}{}'.format(self.yellow, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}{} '.format(self.cyan,  name) + error
        return self.error + self.reset
    
    def ERROR26( self ):
        error = '{}function is used you cannot assigned any value to a variable. {}line: {}{}'.format(self.white, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('AttributeError').Errors() + '{}anonymous '.format(self.red) + error
        return self.error + self.reset
    
    def ERROR27( self, name ):
        error = '{}function {}{} {}cannot be empty. {}line: {}{}'.format(self.white, self.green, name, self.white, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('AttributeError').Errors() + '{}anonymous '.format(self.red) + error
        return self.error + self.reset