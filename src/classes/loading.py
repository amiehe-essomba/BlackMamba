
class LOAD:
    def __init__(self, moduleLoadNames : list, className: str):
        self.moduleLoadNames        = moduleLoadNames 
        self.className              = className
        
    def LOAD(self, typ : str = 'func_names'):
        self.key        = False 
        self.id1        = 0
        self.id2        = 0
        
        for i, mod in enumerate(self.moduleLoadNames):
            if self.key is False: pass 
            else: break 
            if mod: 
                for j, sub_mod in enumerate(mod[typ]):
                    if sub_mod == self.className:
                        self.key = True
                        self.id1 = i
                        self.id2 = j
                        break 
                    else: pass
            else: pass
        
        return {'key' : self.key, 'id1' : self.id1, 'id2' : self.id2}

    def INITIALIZE(self, new_data_base: dict, classes : list):
        self.n = 0
        for i, name in enumerate(self.moduleLoadNames):
            
            if name != self.funcName:
                if name in new_data_base['class_names']:
                    self.index = new_data_base['class_names'].index(name)
                    new_data_base['classes'][self.index] = classes[i]
                else:
                    self.n += 1
                    new_data_base['classes'].append(classes[i]) 
                    new_data_base['class_names'].append(name) 
            else: pass