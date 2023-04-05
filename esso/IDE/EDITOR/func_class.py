class F_C:
    def __init__(self, data_base : dict):
        self.data_base      = data_base 
        self.global_vars    = self.data_base['global_vars']['vars']
        self.func_names     = self.data_base['func_names' ]  
        self.vars           = self.data_base['variables']['vars']
        self.class_names    = self.data_base['class_names']
        self.lib            = self.data_base['LIB']
    
    def F_C(self, my_list : list, char: str, idd: int):
        self.c,self.f, self.v = [], [], []
    
        if self.global_vars: 
            for s in self.global_vars:
                if s[:idd] == char: 
                    if s not in my_list: my_list.append(s)
                    else: pass
                else: pass  
        else: pass
        
        if self.vars: 
            for s in self.vars:
                if s[:idd] == char: 
                    if s not in my_list: my_list.append(s)
                    else: pass 
                    self.v.append(s)
                else: pass  
        else: pass
        
        if self.func_names: 
            for s in self.func_names:
                if s[:idd] == char: 
                    if s not in my_list : my_list.append(s)
                    else: pass 
                    self.f.append(s)
                else: pass  
        else: pass
        if self.class_names: 
            for s in self.class_names:
                if s[:idd] == char: 
                    if s not in my_list : my_list.append(s)
                    else: pass 
                    self.c.append(s)
                else: pass  
        else: pass
        
        if self.lib['func_names']: 
            for s in self.lib['func_names']:
                if s[:idd] == char: 
                    if s not in my_list: my_list.append(s)
                    else: pass 
                    self.f.append(s)
                else: pass  
        else: pass
        
        return self.v, self.f, self.c