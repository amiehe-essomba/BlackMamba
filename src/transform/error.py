from script.STDIN.LinuxSTDIN        import bm_configure as bm
from script.PARXER                  import numerical_value
from CythonModules.Windows          import fileError    as fe 

class ERRORS:
    def __init__(self, line: int):
        self.line       = line
        self.cyan       = bm.init.bold + bm.fg.rbg(0,255,255)
        self.red        = bm.init.bold + bm.fg.rbg(255,0,0)
        self.green      = bm.init.bold + bm.fg.rbg(0,255,0)
        self.yellow     = bm.init.bold + bm.fg.rbg(255,255,0)
        self.magenta    = bm.init.bold + bm.fg.rbg(255,0,255)
        self.white      = bm.init.bold + bm.fg.rbg(255,255,255)
        self.blue       = bm.init.bold + bm.fg.rbg(0,0,255)
        self.reset      = bm.init.resett 

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() + '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error 
        
        return self.error + self.reset 

    def ERROR1(self, string: str, char:str):
        error = '{}<< * >> {}was not defined at beginning of {}<< {} >>. {}line: {}{}'.format(self.green, self.white, 
                                                                                self.cyan, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() + '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error 
        
        return self.error + self.reset 

    def ERROR2(self, string: str, _char_ = 'an integer', func = ''):
        error = '{}to  {}{}() {}type. {}line: {}{}.'.format(self.white, self.red, _char_, self.yellow, self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}impossible to convert {}<< {} >> '.format(self.white, self.cyan, string) + error + func
        
        return self.error + self.reset

    def ERROR3(self, string: str):
        type = '{}a complex(), {}a float(), {}an integer() {}or a string() {}type'.format(self.blue, self.green, self.red, 
                                                                                            self.magenta, self.yellow)
        error = '{}is not {}. {}line: {}{}'.format(self.white, type, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format( self.cyan, string) + error
        
        return self.error+self.reset

    def ERROR4(self, string: str):
        error = '{}line: {}{}'.format( self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        
        return self.error+self.reset

    def ERROR5(self, string: str, _char_ = 'a string', func: str = ''):
        error = '{}is not  {}{}() {}type. {}line: {}{}'.format(self.white, self.yellow, _char_, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format( self.cyan, string) + error + func
        
        return self.error+self.reset 

    def ERROR6(self, string: str, key: str, func : str = ''):
        error = '{}and {}<< {} >> {}have not the same {}length. {}line: {}{}'.format(self.white, self.magenta, key, self.yellow, self.white, self.white, 
                                                                                   self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format( self.cyan, string) + error + func
        
        return self.error+self.reset 

    def ERROR7(self, value: str, func : str = ''):
        error = '{} is negative. {}line: {}{}'.format(self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'DomainError' ).Errors() + '{}<< {} >>'.format(self.cyan, value) + error + func
        
        return self.error+self.reset

    def ERROR8(self, string: str, func: str = ''):
        error = '{}is not  {}a float(), {}a boolean() {}or an integer() {}type. {}line: {}{}'.format(self.white, self.green, self.blue, 
                                                                self.red, self.yellow, self.white, self.yellow, self.line)
      
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error+self.reset

    def ERROR9(self, string: str, func: str = ''):
        error = '{}is not  {}a list(), {}a tuple(), {}a range() {}or a string() {}type. {}line: {}{}'.format(self.white, self.yellow, self.blue,
                                                         self.green, self.magenta, self.yellow, self.white, self.yellow, self.line)  
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error+self.reset

    def ERROR10(self, type1: any, type2: any, func :str = ''):
        typ11 = numerical_value.FINAL_VALUE( type1, {}, self.line, None ).CONVERSION()
        typ22 = numerical_value.FINAL_VALUE( type2, {}, self.line, None ).CONVERSION()

        typ1, typ2 = ERRORS(self.line).ERROR34(type1, type2)

        self.error = '{}unsupported operand between {}<< {}{} : {} >> {} and {}<< {}{} : {} >>. {}line: {}{}'.format(
                        self.yellow, self.white, typ11, self.white, typ1, self.yellow, self.white, typ22, self.white, typ2,
                        self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ArithmeticError').Errors() + self.error + func

        return self.error+self.reset 

    def ERROR11(self, string: str, func:str = ''):
        error = '{}is {}EMPTY. {}line: {}{}'.format( self.white, self.yellow, self.white, self.yellow, self.line)      
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error+self.reset

    def ERROR12(self, first: str, last: str):
        error = '{}<< {} >> {}is lower than {}<< {} >> . {}line: {}{}'.format(self.red, last, self.white, self.green, first,
                                                                        self.white, self.yellow, self.line) 
        self.error = fe.FileErrors( 'DomainError' ).Errors() + error
        return self.error+self.reset

    def ERROR13(self, string: str, func:str = ''):
        error = '{}is not  {}a list(), {} a range() {}or a tuple() {}type. {}line: {}{}'.format(self.white, self.yellow, self.green,
                                                                    self.blue, self.yellow, self.white, self.yellow, self.line)        
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error+self.reset

    def ERROR14(self, string: str, _type_ = 'string()', c = bm.fg.blue_L, func : str= ''):
        error = '{}is not  {}{} {}type. {}line: {}{}'.format(self.white, c, _type_, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func
        return self.error+self.reset

    def ERROR15(self, string: str, num:int = 2, func :str = ''):
        error = '{}is not lower than {}{}. {}line: {}{}'.format(self.white, self.red, num, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format(self.cyan, string) + error + func

        return self.error+self.reset

    def ERROR16(self, string: str, num:int = 2):
        error = '{}is not egal to {}{}. {}line: {}{}'.format(self.white, self.red, num, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}length( {} ) '.format(self.cyan, string) + error + error

        return self.error+self.reset

    def ERROR17(self):
        error = '{}is bigger than {}input[ {}1{} ]. {}line: {}{}'.format(self.white, self.cyna, self.red, self.cyan, 
                                                                         self.white, self.yellow, self.line)        
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}input[ {}0{} ] '.format(self.cyan, self.red, self.cyan) + error

        return self.error+self.reset
    
    def ERROR18(self, name: str):
        error = '{}before {}new opening. {}line: {}{}'.format(self.white, self.cyan, self.white, self.yellow, self.line)        
        self.error = fe.FileErrors( 'FileError' ).Errors() + '{}close {}{} '.format(self.white, self.red, name) + error

        return self.error+self.reset
    
    def ERROR19(self, string: str):
        error = '{}is not a file. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileError' ).Errors() +'{}{} '.format(self.cyan, string) + error
        
        return self.error+self.reset
    
    def ERROR20(self, string: str):
        error = '{}is incorrect. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'OSError' ).Errors() + '{}directory path {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR21(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileNotFoundError' ).Errors() + '{}file {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR22(self):
        error = '{}is not in the list {}[ {}new{}, {}old {}]. {}line: {}{}'.format(self.white, self.red, self.green, self.white, self.magenta, self.red,
                                                                                  self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}status '.format( self.cyan) + error

        return self.error+self.reset
    
    def ERROR23(self):
        error = '{}is not in the list {}[ {}read{}, {}write{} ]. {}line: {}{}'.format(self.white, self.red, self.green, 
                                        self.white, self.magenta, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}action '.format( self.cyan ) + error

        return self.error+self.reset
    
    def ERROR24(self):
        s = '{}[ {}utf-8  {}ascii  {}latin-1  {}cp1252  {}utf-16  {}utf-32{} ]'.format(self.red, self.green, self.magenta,
                                                                           self.yellow, self.red, self.blue, self.cyan, self.red)
        error = '{}Making your choice in {}. {}line: {}{}'.format(self.white, s, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}bad encoding value. '.format( self.cyan ) + error

        return self.error+self.reset
    
    def ERROR25(self, num: any, func :str = ''):
    
        error = '{}cannot be negative or egal to 0. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format(self.cyan, num) + error + func

        return self.error+self.reset
        
    def ERROR26(self, num: any, func :str = ''):
        
        error = '{}cannot be bigger than 1.0. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format(self.cyan, num) + error + func

        return self.error+self.reset
    
    def ERROR27(self, num: any, func :str = ''):
        
        error = '{}cannot be negative. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}<< {} >> '.format(self.cyan, num) + error + func

        return self.error+self.reset

    def ERROR28(self,):
        error = '{}is {}EMPTY. {}line: {}{}'.format(self.white, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}master '.format(self.cyan) + error

        return self.error + self.reset

    def ERROR29(self, string : str = 'nrow'):
        error = '{}should be {}positive {}or {}-1. {}line: {}{}'.format(self.white, self.yellow, self.white, self.red,
                                                                        self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}{} '.format(self.cyan, string) + error

        return self.error + self.reset

    def ERROR30(self, string : str = 'ncol'):
        error = '{}cannot be {}negative {}when {}nrow {}is negative. {}line: {}{}'.format(self.white, self.yellow, self.white, self.cyan,
                                        self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}{} '.format(self.cyan, string) + error

        return self.error + self.reset

    def ERROR31(self, s= '>'):
        error = '{}line: {}{}'.format( self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}nrow * ncol {} length( master ) '.format(self.cyan, s) + error

        return self.error + self.reset

    def ERROR32(self, s= 'nrow'):
        error = '{}and {}reverse is True {}line: {}{}'.format(self.white, self.yellow,  self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}{} {}is {}-1 '.format(self.cyan, s, self.white, self.red) + error

        return self.error + self.reset

    def ERROR33(self, s= 'axis', ss = ''):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}{} {}>= {}{} '.format(self.cyan, s, self.white, self.red, ss) + error

        return self.error + self.reset

    def ERROR34(self, object1 : any, object2: any):

        if type(object1) in [type(list()), type(tuple())]:
            if len(object1) < 4:  result1 = object1
            else:
                if type(object1) in [type(list())]:
                    result1 = f'[{object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]}]'
                else:
                    result1 = f'({object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]})'
        elif type(object1) == type(str()):
            if object1:
                if len(object1) < 6: result1 = object1
                else:  result1 = object1[: 2] + ' ... ' + object1[-2:]
            else:  result1 = object1
        else:  result1 = object1

        if type(object2) in [type(list()), type(tuple())]:
            if len(object2) < 4:  result2 = object2
            else:
                if type(object2) in [type(list())]:
                    result2 = f'[{object2[0]}, {object2[1]}, ....., {object2[-2]}, {object2[-1]}]'
                else:
                    result2 = f'({object2[0]}, {object2[1]}, ....., {object2[-2]}, {object2[-1]})'
        elif type(object2) == type(str()):
            if object2:
                if len(object2) < 6:  result2 = object2
                else:
                    result2 = object2[: 2] + ' ... ' + object2[-2:]
            else:  result2 = object2
        else: result2 = object2

        return result1, result2
    
    def ERROR35(self):
        self.error = fe.FileErrors( 'ZeroDivisionError' ).Errors() +'{}division by zero. {}line: {}{}'.format(self.yellow, self.white, 
                                                                                                            self.yellow, self.line)
        return self.error+self.reset
    
    def ERROR36(self, string: str ="", func: str = ""):
        error = '{}dictionary. {}line: {}{}'.format(self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('KeyError').Errors() + 'The key {}{} {}is already defined in the'.format(self.white, self.cyan, string, self.white) + error + func

        return self.error + self.reset
    
    def ERROR37(self, func: str = ""):
        error = '{}[{}"orion"{}, {}"pegasus"{}]. {}line: {}{}'.format(self.white, self.cyan, self.white, self.cyan ,self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}Terminal name not in '.format(self.white) + error + func

        return self.error + self.reset
    
    def ERROR38(self, func: str = "", lists: list = []):
        s=['white', 'blue', 'black', 'red', 'cyan', 'magenta', 'orange', 'green', 'yellow']
        s=self.white+'['+self.reset
        for i, w in enumerate(lists):
            if i < len(lists)-1: s += self.cyan+w+self.white+", "
            else: s += self.cyan+w+self.white+"]"+self.reset
        error = '{}. {}line: {}{}'.format(s, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}fg {}not in '.format(self.red, self.white) + error + func

        return self.error + self.reset
    
    def ERROR39(self, func: str = ""):
        error = '{}string length sould be {}1. {}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}char {}argument is defined on {}True '.format(self.red, self.white, self.cyan) + error + func

        return self.error + self.reset
    
    def ERROR40(self, func: str = "", s: str="r"):
        error = '{}not in {}[{}0{}:{}256{}]. {}line: {}{}'.format(self.white, self.cyan, self.red, self.white, self.red, self.cyan,
                                                        self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}{} '.format(self.red, s) + error + func

        return self.error + self.reset
    
    def ERROR41(self, func: str = ""):
        error = ', {}but string found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('TypeError').Errors() + '{}expected a {}char'.format(self.white, self.cyan) + error + func

        return self.error + self.reset
    
    def ERROR42(self, func: str = ""):
        error = '{}entry. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError').Errors() + '{}ansi '.format(self.cyan) + error + func

        return self.error + self.reset
    
    def ERROR43(self, func: str = ""):
        error = '{}entry. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('OverFlowError').Errors() + '{}ansi '.format(self.cyan) + error + func

        return self.error + self.reset
    
    def ERROR44(self, func: str = ""):
        error = '{}Bad entry use{}\u001b[. {}line: {}{}'.format(self.red, self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('UnicodeError').Errors() + error + func

        return self.error + self.reset
    
    def ERROR45(self, func: str = "", s = 'column'):
        error = '{}{} {}out of range. {}line: {}{}'.format(self.red, s, self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('IndexError').Errors() + error + func

        return self.error + self.reset