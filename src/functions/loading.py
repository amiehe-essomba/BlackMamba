class LOAD:
    def __init__(self, 
                moduleLoadNames : list, 
                funcName        : str
                ):
        self.moduleLoadNames        = moduleLoadNames 
        self.funcName               = funcName
        
    def LOAD(self):
        self.key        = False 
        self.id1        = 0
        self.id2        = 0
        
        for i, mod in enumerate(self.moduleLoadNames):
            if self.key is False: pass 
            else: break 
            
            if mod: 
                for j, sub_mod in enumerate(mod):
                    if sub_mod == self.funcName:
                        self.key = True
                        self.id1 = i
                        self.id2 = j
                        break 
                    else: pass
            else: pass
        
        return {'key' : self.key, 'id1' : self.id1, 'id2' : self.id2}

    def INITIALIZE(self, 
                new_data_base   : dict, 
                functions       : list
                ):
        
        for i, name in enumerate(self.moduleLoadNames):
            if name != self.funcName:
                if name in new_data_base['func_names']:
                    self.index = new_data_base['func_names'].index(name)
                    new_data_base['functions'][self.index] = functions[i]
                else:
                    new_data_base['functions'].append(functions[i]) 
                    new_data_base['func_names'].append(name) 
            else: pass
       
    def GLOBAL_VARS(self, 
                    db  : dict, 
                    var : dict, 
                    n   : int, 
                    typ : str = 'def'
                    ):
        try:
            self.vars, self.val = var['vars'][ n ], var['values'][n]
      
            if typ == 'def':
                if self.vars:
                    for i, name in enumerate(self.vars) :
                        if name in db['variables']['vars']: pass 
                        else:
                            db['variables']['vars'].append( name )
                            db['variables']['values'].append(self.val[i])
                else: pass
            else:
                if self.vars:
                    for i, name in enumerate(self.vars) :
                        if name in db['global_vars']['vars']: pass 
                        else:
                            db['global_vars']['vars'].append( name )
                            db['global_vars']['values'].append(self.val[i])
                else: pass
        except IndexError: pass

def GLOBAL_VARS_CLASS(db  : dict, n : int):
    try:
        values_import  = db['modulesImport']['variables'].copy()
        values         = db['variables'].copy() 

        if not values['vars']:
            if values_import['vars'][n]: 
                values['vars']      = values_import['vars'][n].copy()
                values['values']    = values_import['values'][n].copy()
            else: pass 
        else:
            if values_import['vars'][n]: 
                for i, s in enumerate(values_import['vars'][n]):
                    if s in values['vars']:
                        idd = values['vars'].index(s)
                        values['values'][idd] = values_import['values'][n][i]
                    else:
                        values['vars'].append(s)
                        values['values'].append(values_import['values'][n][i])
            else: pass
        db['variables'] = values.copy()
        db['global_vars'] = values.copy()

    except NameError: pass
    
def LOADING(main_list, func_name : str):
    id1, id2, key, func, names = None, None, False, None, None
  
    if main_list:
        for i, item in enumerate(main_list):
            name = item['func_names']
            functions = item['functions']
            if func_name in name:
                id1     = i
                id2     = name.index(func_name)
                func    = functions[id2]
                key     = True
                names   = name
                break
            else: pass 
    else: pass

    return {'key' : key, 'id1' : id1, 'id2' : id2, "func" : func, "names" : names}