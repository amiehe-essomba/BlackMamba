from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from CythonModules.Windows                      import fileError    as fe

def write(  string : str = ""  ):
    color = bm.init.bold + bm.fg.rbg(255, 255, 255)
    _string_ = bm.words(string=string, color= color).final()

    return _string_

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

    def ERROR0(self, string: str, data : str):
        data = write(string=data)
        error = '{} {}line: {}{}'.format(data, self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}{} {}not in '.format(self.cyan, string, self.white) + error
        return self.error+self.reset
    
    def ERROR1(self, shape1 : list, shape2 : list): 
        error = '{}X = {}{} <---> {}Y = {} . {}line: {}{}.'.format( self.green, shape1, self.white, self.red, shape2,
                                                                    self.white, self.yellow, self.line)
        self.error =  fe.FileErrors(  'ValueError' ).Errors()+'{}dimension Error '.format( self.cyan ) + error
        return self.error+self.reset
    
    def ERROR2(self, string: str): 
        error = '{}{} {}should be 1D. {}line: {}{}.'.format( self.green, string, self.white, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{} dimension Error '.format( self.cyan ) + error 
        return self.error+self.reset
       
    def ERROR3(self): 
        error = '{}line: {}{}.'.format(self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}figure size dimension Error '.format( self.cyan ) + error
        return self.error+self.reset
    
    def ERROR4(self, data : str, index ): 
        data = write(string=data)
        error = '{}{} {}is not an {}integer() {}type. {}line: {}{}.'.format(self.green, index, self.white,
                                                            self.red, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}in {}{} '.format( self.white, self.cyan, data ) + error
        return self.error+self.reset
    
    def ERROR5(self, string : str ): 
        error = '{}are not {}integer(). {}line: {}{}.'.format( self.white, self.red, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}all the elements of {}{} '.format( self.white, self.cyan, string ) + error
        return self.error+self.reset
    
    def ERROR6(self, shape1 : list, shape2 : list): 
        error = '{}X = {}{} <---> {}color = {} . {}line: {}{}.'.format( self.green, shape1, self.white, self.red, shape2,
                                                                    self.white, self.yellow, self.line)
        self.error =  fe.FileErrors(  'ValueError' ).Errors()+'{}dimension Error '.format( self.cyan ) + error
        return self.error+self.reset
    
    def ERROR7(self, string :str): 
        error = '{}cannot be empty. {}line: {}{}.'.format(self.green, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors(  'ValueError' ).Errors()+'{}{} '.format( self.cyan, string ) + error
        return self.error+self.reset
    
    def ERROR8(self, string :str): 
        error = '{}dimension error. {}line: {}{}.'.format(self.green, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors(  'ValueError' ).Errors()+'{}{} '.format( self.cyan, string ) + error
        return self.error+self.reset
    
    def ERROR9(self, data : str, index ): 
        data = write(string=data)
        error = '{}{} {}is not an {}integer() {}or {}float() {}type. {}line: {}{}.'.format(self.green, index, self.white,
                                self.red, self.white, self.blue, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}in {}{} '.format( self.white, self.cyan, data ) + error
        return self.error+self.reset
    
    def ERROR10(self, index : int, string : str = "marker" ): 
        error = '{}out of the {}range {}[0,{}]. {}line: {}{}.'.format(self.white, self.green, self.red, index, 
                                                                      self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}{} '.format(self.cyan, string) + error
        return self.error+self.reset
    
    def ERROR11(self, data : list, name : str ): 
        error = '{}not in the list {}{}. {}line: {}{}.'.format(self.white, self.green, data, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}{} '.format(self.cyan, name) + error
        return self.error+self.reset
    
    def ERROR12(self, data : list,): 
        error = '{}xmin {}>= xmax{}. {}line: {}{}.'.format(self.red, self.white, self.red, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}in {}{} '.format(self.cyan, data) + error
        return self.error+self.reset
    
    def ERROR13(self,  string : str = 'Y'): 
        error = '{}should be {}[m, n] {}dimension. {}line: {}{}.'.format(self.white, self.red, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}{} {}matrix '.format(self.cyan, string, self.white) + error
        return self.error+self.reset
    
    def ERROR14(self,  string, idd): 
        error = '{}is not an {}integer() {}type. {}line: {}{}.'.format(self.white, self.red, self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}in {}{} {}{} '.format(self.white, self.cyan, string, self.green, idd) + error
        return self.error+self.reset
    
    def ERROR15(self,  idd): 
        error = '{}in color list is not a {}list() {}or {}string() {}type. {}line: {}{}.'.format(self.white, self.red, self.white, self.blue, 
                                                                                                 self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}the element {}{} '.format(self.white, self.green, idd) + error
        return self.error+self.reset
    
    def ERROR16(self,  idd): 
        error = '{}in the color list. {}line: {}{}.'.format(self.white, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}redim the element {}{} '.format(self.white, self.green, idd) + error
        return self.error+self.reset
    
    def ERROR17(self,  idd): 
        error = '{}of color list all elements are not {}integer() {}type. {}line: {}{}.'.format(self.white,  self.red, 
                                                                                                 self.yellow, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'TypeError' ).Errors()+'{}in the element {}{} '.format(self.white, self.green, idd) + error
        return self.error+self.reset
    
    
   



