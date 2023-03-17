import numpy as np
from src.transform                      import error as er
from src.transform                      import matrix_modules as mm
from src.transform                      import statistics as st
from script.STDIN.LinuxSTDIN            import bm_configure as bm
try: from CythonModules.Linux           import making_stat as ms
except ImportError:
    from CythonModules.Windows          import making_stat as ms


class R:
    def __init__(self, master : list, _value_ : list, line : int):
        self.master     = master
        self.line       = line
        self._value_    = _value_
    def R(self):
        self.error      = None
        self.type       = [type(list()), type(tuple()), type(range(1))]
        self.func       = bm.fg.rbg(0, 255, 0) + ' in {}( ).'.format(self._value_[4]) + bm.init.reset
        self.master_inv = None
        self.master_v   = []

        if   self._value_[4] in ['sum']:
            if self._value_[5] is None:
                for x, _value_ in enumerate(self.master):
                    if type(_value_) in self.type:
                        self._, self.error = ms.GetValue(list(_value_), self.line).sum()
                        if not self.error:
                            self.error = None
                            self.master[x] = self._
                        else:  break
                    else:
                        self.error = er.ERRORS(self.line).ERROR13(_value_, self.func)
                        break
                if self.error is None:  self.master = np.array(self.master)
                else:  pass
            else:  self.master, self.error = ms.GetValue(self.master, self.line).sum()
        elif self._value_[4] in ['ndim']:
            self.master = list(np.array(self.master).shape)
        elif self._value_[4] in ['std', 'var']:
            if self._value_[5] is None:
                for x, _value_ in enumerate(self.master):
                    if type(_value_) in self.type:
                        self._, self.error = ms.GetValue(list(_value_), self.line).var_std(
                            self._value_[4], _type_='sam', ob_type='list')
                        if not self.error:
                            self.error = None
                            self.master[x] = self._
                        else:  break
                    else:
                        self.error =  er.ERRORS(self.line).ERROR13(_value_, self.func)
                        break
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self.master, self.error = ms.GetValue(self.master, self.line).var_std(
                    self._value_[4], _type_='sam', ob_type='list')
        elif self._value_[4] in ['pstd', 'pvar']:
            if self._value_[5] is None:
                for x, _value_ in enumerate(self.master):
                    if type(_value_) in self.type:
                        self._, self.error = ms.GetValue(list(_value_), self.line).var_std(
                            self._value_[4], _type_='pop', ob_type='list')
                        if not self.error:
                            self.error = None
                            self.master[x] = self._
                        else:  break
                    else:
                        self.error =  er.ERRORS(self.line).ERROR13(_value_, self.func)
                        break
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self.master, self.error = ms.GetValue(self.master, self.line).var_std(
                    self._value_[4], _type_='pop', ob_type='list')
        elif self._value_[4] in ['mean']:
            if self._value_[5] is None:
                for x, _value_ in enumerate(self.master):
                    if type(_value_) in self.type:
                        self._, self.error = ms.GetValue(list(_value_), self.line).mean(len(_value_))
                        if not self.error:
                            self.error = None
                            self.master[x] = self._
                        else:  break
                    else:
                        self.error =  er.ERRORS(self.line).ERROR13(_value_, self.func)
                        break
                if self.error is None:  self.master = np.array(self.master)
                else:  pass
            else:  self.master, self.error = ms.GetValue(self.master, self.line).mean(len(self.master))
        elif self._value_[4] in ['min', 'max']:
            if self._value_[5] is None:
                for x, _value_ in enumerate(self.master):
                    if type(_value_) in self.type:
                        self._, self.error = ms.GetValue(list(_value_), self.line).min_max(self._value_[4])
                        if not self.error:
                            self.error = None
                            self.master[x] = self._
                        else:  break
                    else:
                        self.error =  er.ERRORS(self.line).ERROR13(_value_, self.func)
                        break
                if self.error is None:  self.master = np.array(self.master)
                else:  pass
            else:  self.master, self.error = ms.GetValue(self.master, self.line).min_max(self._value_[4])
        elif self._value_[4] in ['cov', 'cor', 'linearR']:
            if self._value_[3] is True: self._value_[3] = False
            else: self._value_[3] = True

            self.ss = []
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self.master_inv, self.error = mm.MATRIX(self._value_[0], self._value_[1], self._value_[2],
                                        self._value_[3], self.line).MATRIX(x, ctype=self._value_[4])
                    self.master_v   = []
                    for y in range(len(self.master_inv)):
                        self._val_ = [self.master_inv, self.master[y], self._value_[4], "pop", self._value_[4]]
                        self.s, self.error = st.STAT(self._val_, '', self.line).COV_CORR_LINEAR()
                        if self.error is None: self.master_v.append(self.s)
                        else: break
                    if self.error is None: self.ss.append(self.master_v)
                    else: break
                if self.error is None: self.master = np.array(self.ss)
                else: pass
            else:
                self._value_ = [self.master, self.master_inv, self._value_[4], "pop", self._value_[4]]
                self.master, self.error = st.STAT(self._value_, '', self.line).COV_CORR_LINEAR()     
        elif self._value_[4] in ['quantile']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], self._value_[6], self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).QUANTILE()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, self._value_[6], self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).QUANTILE()        
        elif self._value_[4] in ['iquantile']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], 'pop', self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).IQUANTILE()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, "pop", self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).IQUANTILE()
        elif self._value_[4] in ['kurtosis']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], 'pop', self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).KURTOSIS()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, "pop", self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).KURTOSIS()
        elif self._value_[4] in ['sum_square']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).SUM_SQUARE()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).SUM_SQUARE()      
        elif self._value_[4] in ['grouped']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).GROUPED()
    
                    if self.error is None: self.master[x] =self.s
                    else: break
                    
                if self.error is None:
                    try:   self.master = np.array(self.master, dtype=object)
                    except FutureWarning: pass
                else: pass
            else:
                self._val_ = [self.master, self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).GROUPED()
        elif self._value_[4] in ['Q1', 'Q3']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], self._value_[4], self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).Q1_Q3()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, self._value_[4], self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).Q1_Q3()         
        elif self._value_[4] in ['round']:
            if self._value_[5] is None:
                
                for x in range(len(self.master)):
                    if self.master[x]:
                        for y in range(len(self.master[x])):
                            if type(self.master[x][y]) in [type(float())]:
                                self.master[x][y] = round(self.master[x][y], self._value_[6])
                            else: pass
                    else: break
                
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:  
                for x in range(len(self.master)):
                    if type(self.master[x]) in [type(float())]:
                        self.master[x] = round(self.master[x],self._value_[6]) 
                    else: pass
                
                self.master = np.array(self.master)
        elif self._value_[4] in ['mad']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).MAD()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).MAD()  
        elif self._value_[4] in ['rms']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).RMS()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).RMS() 
        elif self._value_[4] in ['rsd']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], "pop", self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).RSD()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, "pop", self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).RSD() 
        elif self._value_[4] in ['upper_fence', 'lower_fence']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], "pop", self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).LOWER_UPPER_FENCE()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, "pop", self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).LOWER_UPPER_FENCE()       
        elif self._value_[4] in ['std_error']:
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], "pop", self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).STD_ERRPR()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, "pop", self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).STD_ERRPR()
        elif self._value_[4] in ['midrange']:                      
            if self._value_[5] is None:
                for x in range(len(self.master)):
                    self._val_ = [self.master[x], self._value_[4]]
                    self.s, self.error = st.STAT( self._val_, "", self.line ).MIDRANGE()
                    
                    if self.error is None: self.master[x] = self.s
                    else: break
                    
                if self.error is None: self.master = np.array(self.master)
                else: pass
            else:
                self._val_ = [self.master, self._value_[4]]  
                self.master, self.error = st.STAT( self._val_, "", self.line ).MIDRANGE()
                
        return self.master, self.error