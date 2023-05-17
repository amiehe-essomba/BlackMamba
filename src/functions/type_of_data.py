import numpy                                                as np
import pandas                                               as pd
from script.LEXER.FUNCTION              import return_
from src.functions                      import error        as er
from script.STDIN.LinuxSTDIN            import bm_configure as bm


class CHECK_TYPE_OF_DATA:
    def __init__(self, value : any ):
        self.value          = value

    def DATA(self):
        self._return_                           = ''
        self.type                               = type( self.value )

        if  self.type  == type( int() )         :       self._return_ = 'int'
        elif self.type == type( float() )       :       self._return_ = 'float'
        elif self.type == type( bool() )        :       self._return_ = 'bool'
        elif self.type == type( complex() )     :       self._return_ = 'cplx'
        elif self.type == type( dict() )        :       self._return_ = 'dict'
        elif self.type == type( list() )        :       self._return_ = 'list'
        elif self.type == type( tuple() )       :       self._return_ = 'tuple'
        elif self.type == type( str() )         :       self._return_ = 'string'
        elif self.type == type( range( 1 ) )    :       self._return_ = 'range'
        elif self.type == type( None )          :       self._return_ = 'none' 
        elif self.type == type(np.array([]))    :       self._return_ = 'ndarray'
        elif self.type == type(pd.DataFrame({'r':[1]}))    :       self._return_ = 'table'

        return self._return_

    def TYPE(self):
        self._return_               = ''
        
        if   self.value == 'int'    :           self._return_ = '{}an integer(){}'.format(bm.fg.red_L, bm.init.reset)
        elif self.value == 'p_int'  :           self._return_ = '{}a positive integer(){}'.format(bm.fg.red_L, bm.init.reset)
        elif self.value == 'n_int'  :           self._return_ = '{}a negative integer(){}'.format(bm.fg.red_L, bm.init.reset)
        elif self.value == 'float'  :           self._return_ = '{}a float(){}'.format(bm.fg.rbg(0,255,0), bm.init.reset)
        elif self.value == 'double' :           self._return_ = '{}a double(){}'.format(bm.fg.rbg(0,255,0), bm.init.reset)
        elif self.value == 'p_float'  :         self._return_ = '{}a positive float(){}'.format(bm.fg.rbg(0,255,0), bm.init.reset)
        elif self.value == 'n_float'  :         self._return_ = '{}a negative float(){}'.format(bm.fg.rbg(0,255,0), bm.init.reset)
        elif self.value == 'p_double' :         self._return_ = '{}a positive double(){}'.format(bm.fg.rbg(0,255,0), bm.init.reset)
        elif self.value == 'n_double' :         self._return_ = '{}a negative double(){}'.format(bm.fg.rbg(0,255,0), bm.init.reset)
        elif self.value == 'bool'   :           self._return_ = '{}a boolean(){}'.format(bm.fg.cyan_L, bm.init.reset)
        elif self.value == 'cplx'   :           self._return_ = '{}a complex(){}'.format(bm.fg.blue, bm.init.reset)
        elif self.value == 'list'   :           self._return_ = '{}a list(){}'.format(bm.fg.rbg(255,255,0), bm.init.reset)
        elif self.value == 'tuple'  :           self._return_ = '{}a tuple(){}'.format(bm.fg.blue_L, bm.init.reset)
        elif self.value == 'dict'   :           self._return_ = '{}a dictionary(){}'.format(bm.fg.magenta_M, bm.init.reset)
        elif self.value == 'string' :           self._return_ = '{}a string(){}'.format(bm.fg.cyan, bm.init.reset)
        elif self.value == 'range'  :           self._return_ = '{}a range(){}'.format(bm.fg.green_L, bm.init.reset)
        elif self.value == 'none'   :           self._return_ = '{}a none(){}'.format(bm.fg.rbg(252, 127, 0 ), bm.init.reset)
        elif self.value == 'ndarray':           self._return_ = '{}ndarray(){}'.format(bm.fg.rbg(255, 165, 0),bm.init.reset)
        elif self.value == 'table'  :           self._return_ = '{}ndarray(){}'.format(bm.fg.rbg(255, 165, 25),bm.init.reset)

        return self._return_ 
    
    def CHECK_TYPE( self, line: int, name: str, func_name: str):
        self.lists      = []
        self.error      = None
        
        if self.value:
            for value in self.value:
                if not self.lists: self.lists.append( value )
                else:
                    if value not in self.lists: self.lists.append( value )
                    else:
                        func        = bm.fg.rbg(0,255,0)+' in {}( )'.format( func_name )+bm.init.reset 
                        self.error  = er.ERRORS( line ).ERROR19( name,  value, func )
                        break
        else: pass
                
        return self.error 
    
    def RETURNING_TYPE(self):
        self._return_, self.s = None, None
        if   self.value == 'none'           : self._return_, self.s = type(None)            , '{}a none(){}'.format(bm.fg.rbg(252, 127, 0 ), bm.init.reset)
        elif self.value == 'integer'        : self._return_, self.s = type(int())           , '{}an integer(){}'.format(bm.fg.red_L, bm.init.reset)
        elif self.value == 'float'          : self._return_, self.s = type(float())         , '{}a float(){}'.format(bm.fg.rbg(0,255,0), bm.init.reset)
        elif self.value == 'complex'        : self._return_, self.s = type(complex())       , '{}a complex(){}'.format(bm.fg.blue, bm.init.reset)
        elif self.value == 'range'          : self._return_, self.s = type(range(1))        , '{}a range(){}'.format(bm.fg.green_L, bm.init.reset)
        elif self.value == 'tuple'          : self._return_, self.s = type(tuple())         , '{}a tuple(){}'.format(bm.fg.blue_L, bm.init.reset)
        elif self.value == 'list'           : self._return_, self.s = type(list())          , '{}a list(){}'.format(bm.fg.rbg(255,255,0), bm.init.reset)
        elif self.value == 'dictionary'     : self._return_, self.s = type(dict())          , '{}a dictionary(){}'.format(bm.fg.magenta_M, bm.init.reset)
        elif self.value == 'boolean'        : self._return_, self.s = type(bool())          , '{}a boolean(){}'.format(bm.fg.cyan_L, bm.init.reset)
        elif self.value == 'string'         : self._return_, self.s = type(str())           , '{}a string(){}'.format(bm.fg.cyan, bm.init.reset)
        elif self.value == 'ndarray'        : self._return_, self.s = type(np.array([1]))   , '{}a ndarray(){}'.format(bm.fg.rbg(255, 165, 0),bm.init.reset)
        elif self.value == 'table'          : self._return_, self.s = type(np.array([1]))   , '{}a table(){}'.format(bm.fg.rbg(255, 165, 25),bm.init.reset)
        
        return self._return_, self.s


def data_checking(s, value, line, args):
    typ   = type(value)
    bool_ = False
    error = None 
    
    if typ == type(int()):
        if   s == 'p_int':
            if value >= 0: bool_ = True
            else: pass 
        elif s == 'n_int':
            if value < 0: bool_ = True
            else: pass 
        else: bool_ = True
    elif typ == type(float()): 
        if   s in ['p_float', 'p_double']:
            if value >= 0: bool_ = True
            else: pass 
        elif s == ['n_float', 'n_double']:
            if value < 0: bool_ = True
            else: pass 
        else: bool_ = True
    else: bool_ = True
        
    if bool_ is True: pass 
    else:
        str_type   = CHECK_TYPE_OF_DATA( s ).TYPE()
        error = er.ERRORS(line).ERROR3(args, str_type)
            
    return error