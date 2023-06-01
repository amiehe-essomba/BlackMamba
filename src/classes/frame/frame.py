import sys
import numpy as np
import pandas as pd 

from src.classes                                    import error as er 
from src.transform                                  import error as er_
from script.LEXER                                   import main_lexer       
from script.LEXER                                   import particular_str_selection
from script.PARXER                                  import numerical_value
from script.LEXER                                   import check_if_affectation
from CythonModules.Windows                          import frame
from script.STDIN.LinuxSTDIN                        import bm_configure as bm
from CythonModules.Windows                          import fileError    as fe 

class DATA:
    def __init__(self, 
        DataBase        : dict, 
        line            :int, 
        master          : str, 
        function        : str, 
        FunctionInfo    : list
        ) -> None:

        self.master         = master
        self.function       = function
        self.FunctionInfo   = FunctionInfo[ 0 ]
        self.line           = line
        self.DataBase       = DataBase
        self.lexer          = main_lexer
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        
    def FRAME( self, 
            mainName    : str, 
            mainString  : str,
            name        : str = 'column' 
            ):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.value          = self.FunctionInfo[ self.function ][ 'value' ] 
        self.main_dict      = mainString 
        
        if   self.function in [ 'keys' ]                :
            if None in self.arguments:  self._return_ = list( self.master.keys() )
            else: self.error = er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in [ 'tail', "head" ]        : 
            if None in self.arguments: 
                if self.function == 'tail': 
                    self._return_, s, ss, self.error  = frame.FRAME({"s":self.master, 'id':list(self.master.index)}, 
                                    self.line).FRAME(Frame=False,  _typ_='DataFrame', show_index=True, Tail=True)
                else : 
                    self._return_, s, ss, self.error  = frame.FRAME({"s":self.master, 'id':list(self.master.index)}, 
                                    self.line).FRAME(Frame=False,  _typ_='DataFrame', show_index=True, Head=True)
            else : self.error = er.ERRORS( self.line ).ERROR14( self.function )
        elif self.function in ['set_id', 'select' ]     :
            self._return_, self.error = DATA(self.DataBase, self.line, self.master, self.function, 
                            [self.FunctionInfo]).SUB_FRAME(mainName, mainString, name)
        elif self.function in ['update' ]               :
            self._return_, self.error = DATA(self.DataBase, self.line, self.master, self.function, 
                            [self.FunctionInfo]).SUB_FRAME(mainName, mainString, name="master")
        elif self.function in ['filter' ]               :
            self._return_, self.error = DATA(self.DataBase, self.line, self.master, self.function, 
                            [self.FunctionInfo]).SUB_FRAME(mainName, mainString, name="mask")

        return self._return_, self.error
    
    def SUB_FRAME(self, mainName: str, mainString: str, name: str = 'show_id' ):
        self.error          = None 
        self._return_       = ''
        self.arguments      = self.FunctionInfo[ self.function ][ 'arguments' ] 
        self.values         = self.FunctionInfo[ self.function ][ 'value' ]
        self.main_dict      = mainString 
        
        if len( self.arguments ) == 1:
            if self.arguments[ 0 ] == name: 
                if self.values[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name]] ) 
                else: 
                    self.dict_value, self.error = self.affectation.AFFECTATION( self.values[ 0 ],
                                                                    self.values[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                    if self.error is None:
                        if 'operator' not in list( self.dict_value.keys() ): 
                            self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                            if self.error is None: 
                                self.all_data = self.lex[ 'all_data' ]
                                if self.all_data is not None:
                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                    self.DataBase,self.line).ANALYSE( mainString )
                                    if self.error is None:
                                        self.newValues = self.final_val[ 0 ]
                                        func = bm.fg.rbg(0, 255, 0   )+f' in {self.function}( ).' +bm.fg.rbg(255,255,255)+\
                                                            ' / '+bm.fg.rbg(255, 255, 0)+"class " +bm.fg.rbg(0, 0, 255) +"data"+ bm.init.reset 
                                        
                                        if name == "column"  :  
                                            self.show, s, ss, self.error  = frame.FRAME({"s":self.master, 'id':list(self.master.index)}, 
                                                                                self.line).FRAME(False, 'DataFrame', True)
                                            if self.error is None:
                                                self.keys  = list(self.show.keys())
                                                self._return_, self.error = SelectSet(
                                                    DataBase = self.DataBase, newValues=self.newValues, keys=self.keys, shows=self.show,
                                                    line=self.line ).get(  mainName=mainName , function=self.function, 
                                                                            name=name, func=func, master=self.master )
                                            else: pass
                                        elif name == "mask": 
                                            self._return_, self.error = SelectSet(
                                                    DataBase = self.DataBase, newValues=self.newValues, shows=[], keys=(),
                                                    line=self.line ).get(  mainName=mainName , function=self.function, 
                                                                            name=name, func=func, master=self.master )
                                        
                                        elif name == "master": 
                                            self._return_, self.error = SelectSet(
                                                    DataBase = self.DataBase, newValues=self.newValues, shows=[], keys=(),
                                                    line=self.line ).get(  mainName=mainName , function=self.function, 
                                                                            name=name, func=func, master=self.master )
                                        else: self.error = er.ERRORS(self.line).ERROR13( name )
                                    else: pass 
                                else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                            else: pass
                        else: 
                            self.operator = self.dict_value[ 'operator' ]
                            self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                    else: pass
            else:
                if self.arguments[ 0 ] is None: self.error = er.ERRORS( self.line ).ERROR15( self.function, [[name]] )
                else:
                    if self.values[ 0 ] is None:
                        if list( self.master.keys() ):
                            self.dict_value, self.error = self.affectation.AFFECTATION( self.arguments[ 0 ],
                                                                    self.arguments[ 0 ], self.DataBase, self.line ).DEEP_CHECKING()
                            if self.error is None:
                                if 'operator' not in list( self.dict_value.keys() ): 
                                    self.lex, self.error = self.lexer.FINAL_LEXER( mainString, self.DataBase,
                                                                                self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                    if self.error is None: 
                                        self.all_data = self.lex[ 'all_data' ]
                                        if self.all_data is not None:
                                            self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                            self.DataBase, self.line).ANALYSE( mainString )
                                            if self.error is None:
                                                self.newValues = self.final_val[ 0 ]
                                                func = bm.fg.rbg(0, 255, 0 )+f' in {self.function}( ).' +bm.fg.rbg(255,255,255)+\
                                                            ' / '+bm.fg.rbg(255, 255, 0)+"class " +bm.fg.rbg(0, 0, 255) +"data"+ bm.init.reset 
                                                
                                                if name == "column"   : 
                                                    self.show, s, ss, self.error  = frame.FRAME({"s":self.master, 'id':list(self.master.index)}, 
                                                                                self.line).FRAME(False, 'DataFrame', True) 
                                                    if self.error is None:
                                                        self.keys  = list(self.show.keys())
                                                        self._return_, self.error = SelectSet(
                                                            DataBase = self.DataBase, newValues=self.newValues, shows=self.show, keys=self.keys,
                                                            line=self.line ).get(  mainName=mainName , function=self.function, 
                                                                                 name=name, func=func, master=self.master )
                                                    else: pass
                                                elif name == "mask": 
                                                    self._return_, self.error = SelectSet(
                                                            DataBase = self.DataBase, newValues=self.newValues, shows=[], keys=(),
                                                            line=self.line ).get(  mainName=mainName , function=self.function, 
                                                                                 name=name, func=func, master=self.master )
                                                
                                                elif name == "master": 
                                                    self._return_, self.error = SelectSet(
                                                            DataBase = self.DataBase, newValues=self.newValues, shows=[], keys=[],
                                                            line=self.line ).get(  mainName=mainName , function=self.function, 
                                                                                 name=name, func=func, master=self.master )
                                                    
                                                else: self.error = er.ERRORS(self.line).ERROR13(name)
                                            else: pass 
                                        else: self.error = er.ERRORS( self.line ).ERROR0( mainString ) 
                                    else: pass
                                else: 
                                    self.operator = self.dict_value[ 'operator' ]
                                    self.error = er.ERRORS( self.line ).ERROR26(self.main_dict, self.operator )
                            else: pass
                        else: self.error = er.ERRORS( self.line ).ERROR24( 'table()' )
                    else: self.error = er.ERRORS( self.line ).ERROR11( self.function, self.arguments[ 0 ] )
        else: self.error = er.ERRORS( self.line ).ERROR12( self.function, 1)
        
        return self._return_, self.error
    
class SelectSet:
    def __init__(self, 
            DataBase    : dict, 
            newValues   : any, 
            shows       : any , 
            keys        : list , 
            line        : int
            ) -> None:
        
        self.DataBase       = DataBase 
        self.newValues      = newValues
        self.shows          = shows
        self.keys           = keys
        self.line           = line 

    def get(self, 
            mainName    : str , 
            function    : str, 
            name        : str="", 
            func        : str="", 
            master      : any = ""
            ) -> tuple:
        
        self.function   = function 
        self._return_   = None 
        self.error      = None 
        self.master     = master

        if   self.function == "set_id": 
            if type( self.newValues ) in [type(int())]: 
                if self.newValues < len(self.keys):
                    self._return_ = None
                    self.show.set_index(self.keys[self.newValues], inplace=True)    
                    if  mainName in self.DataBase[ 'variables' ][ 'vars' ]:
                        self.idd =  self.DataBase[ 'variables' ][ 'vars' ].index( mainName )
                        self.DataBase[ 'variables' ][ 'values' ][ self.idd ] =  self.shows
                    else: pass
                else: self.error = er_.ERRORS( self.line ).ERROR45( func=func )
            else:  self.error = er.ERRORS( self.line ).ERROR3( name , 'a integer()') 
        elif self.function == "select": 
            try: 
                if   type( self.newValues ) in [type(int())]:
                    if self.newValues < len(self.keys):
                        self._return_ = self.shows.iloc[:, [self.newValues]].values.reshape((-1,))
                    else : self.error = er_.ERRORS( self.line ).ERROR45( func=func )
                elif type( self.newValues ) in [type(list()), type(tuple())]:
                    if self.newValues:
                        self.newkeys = []
                        for w, ss in enumerate(self.newValues):
                            if   type(ss) == type(int()):
                                try:
                                    s = self.keys[ss]
                                    if ss not in self.newkeys : self.newkeys.append(ss)
                                    else: pass
                                except IndexError: 
                                    self.error = er_.ERRORS( self.line ).ERROR45( func=func, s=ss ) 
                                    break
                            elif type(ss) == type(str()):
                                if ss in self.keys:
                                    if w not in self.newkeys: self.newkeys.append(w)
                                    else: pass
                                else: 
                                    self.error = er_.ERRORS( self.line 
                                        ).ERROR49( func=func, string=self.keys, key=ss )
                                    break
                            else:
                                self.error = er_.ERRORS( self.line ).ERROR47( func=func, string=ss ) 
                                break
                        if self.error is None:
                            self._return_ = self.shows.iloc[:, self.newkeys].values
                        else : pass
                    else: self.error= er_.ERRORS( self.line ).ERROR28( string=name )
                else: self.error = er_.ERRORS( self.line ).ERROR48( func=func, string=name )
            except IndexError : self.error = er_.ERRORS( self.line ).ERROR45( func=func )
        elif self.function == "update":
            if list( self.master.keys() ):
                if list(self.shows.keys()):
                    shape1 = self.master.iloc[:, [0]].values.shape[0]
                    shape2 = self.show.iloc[:, [0]].values.shape[0]
                    if shape1 == shape2: 
                        _keys_ = list(self.shows.keys())
                        for i, _key_ in enumerate(_keys_):
                            self.master[_keys_] = self.shows.iloc[:, [i]].values 
                    else: self.error = ERRORS(self.line).ERROR0(shape1, shape2)
                else: self.error = ERRORS(self.line).ERROR1(n=2)
            else: self.error = ERRORS(self.line).ERROR1(n=1)
        elif self.function == "filter":
            if list( self.master.keys() ):
                if type( self.newValues ) == type(np.array([1])):
                    if self.newValues.size != 0:
                        shape2 = self.newValues.shape
                        if len(shape2) <= 2:
                            shape1 = self.master.values.shape
                            if len(shape2) == 1: 
                                self.newValues = self.newValues.reshape((-1,))
                                mask   = self.newValues
                                self.show = self.master.values[mask, ]
                                self._return_ = pd.DataFrame( self.show, columns=list(self.master.keys()) )
                            elif len(shape2) == 2:
                                if shape1[0] == shape2[0]: 
                                    if shape2[1] == 1:
                                        self.newValues = self.newValues.reshape((-1,))
                                        mask   = self.newValues
                                        self.show = self.master.values[mask, ]
                                        self._return_ = pd.DataFrame( self.show, columns=list(self.master.keys()) )
                                    else: self.error = ERRORS(self.line).ERROR5(ncol=1)
                                else: self.error = ERRORS(self.line).ERROR4(nrow=shape1[1])
                            else: self.error = ERRORS(self.line).ERROR3()
                        else: self.error = ERRORS(self.line).ERROR3()
                    else: self.error = ERRORS(self.line).ERROR2()
                else: self.error = ERRORS(self.line).ERROR3()
            else: self.error = ERRORS(self.line).ERROR1(n=1)
        else: pass 

        return self._return_, self.error

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
        self.reset      = bm.init.reset 

    def ERROR0(self, shape1, shape2):
        error = '{}tabel_1 = {}{}, {}tabel_2 = {}{}. {}line: {}{}'.format(self.white, self.red, shape1, self.white, self.red, shape2,
            self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}tables {}dimension error'.format(self.cyan, self.white) + error 
        
        return self.error + self.reset 
    
    def ERROR1(self, n : int):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}table_{} {}is EMPTY. '.format(self.cyan, n, self.green) + error 
        
        return self.error + self.reset 
    
    def ERROR2(self):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}mask {}cannot be EMPTY. '.format(self.cyan, self.white) + error 
        
        return self.error + self.reset 
    
    def ERROR3(self):
        error = '{}2darray() {}type {}of dimension {}[n, m] .{}line: {}{}'.format(self.blue, self.yellow, self.white, self.red,
                                                                self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}mask {}should be a not null  '.format(self.cyan, self.whiten) + error 
        
        return self.error + self.reset 
    
    def ERROR4(self, nrow : int, string = "nrow" ):
        error = '{}should be {}{} = {}{} .{}line: {}{}'.format(self.white, self.red, string, self.green, nrow,
                                                                self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}mask {}{} '.format(self.cyan, self.red, string) + error 
        
        return self.error + self.reset 
    
    def ERROR5(self, nrow : int, string = "ncol" ):
        error = '{}should be {}{} <= {}{} .{}line: {}{}'.format(self.white, self.red, string, self.green, nrow,
                                                                self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors() + '{}mask {}{} '.format(self.cyan, self.red, string) + error 
        
        return self.error + self.reset 