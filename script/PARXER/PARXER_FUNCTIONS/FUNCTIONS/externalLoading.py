class UPDATING:
    def __init__(self, db1: dict, db2: dict):
        self.new_data_base  = db1 
        self.data_base      = db2
    def UPDATING(self, name: str ):
        
        if self.data_base['modulesImport'][ 'moduleLoading' ]['names']:
            self.id             = self.data_base['modulesImport'][ 'moduleLoading' ]['names'].index(name)
            try:
                if self.data_base['modulesImport'][ 'moduleLoading' ]['loading'][self.id]['class_names']:
                    self.class_name1    = self.new_data_base['class_names']
                    self.classes1       = self.new_data_base['classes']
                    self.class_name2    = self.data_base['modulesImport'][ 'moduleLoading' ]['loading'][self.id]['class_names'][0].copy()
                    self.classes2       = self.data_base['modulesImport'][ 'moduleLoading' ]['loading'][self.id]['classes'][0].copy()
                    self.mainClasscNames= self.data_base['modulesImport'][ 'moduleLoading' ]['loading'][self.id]['mainClasscNames'][0].copy()
                    
                    for name in self.mainFuncNames:
                        self.index = self.class_name2.index(name)
                        if name not in self.class_name1:
                            self.class_name1.append(name)
                            self.classes1.append( self.classes2[self.index].copy())
                        else:
                            self.idd = self.class_name1.index(name)
                            self.classes1[self.idd] = self.classes2[self.index].copy()
                else: pass
            except IndexError: pass
            except KeyError: pass
            try:
                if self.data_base['modulesImport'][ 'moduleLoading' ]['loading'][self.id]['func_names']:
                    self.func_name2         = self.data_base['modulesImport'][ 'moduleLoading' ]['loading'][self.id]['func_names'][0].copy()
                    self.functions2         = self.data_base['modulesImport'][ 'moduleLoading' ]['loading'][self.id]['functions'][0].copy()
                    self.mainFuncNames      = self.data_base['modulesImport'][ 'moduleLoading' ]['loading'][self.id]['mainFuncNames'][0].copy()
                    self.func_name1         = self.new_data_base['func_names']
                    self.functions1         = self.new_data_base['functions']
                    
                    for name in self.mainFuncNames:
                        self.index = self.func_name2.index( name )
                        if name not in self.func_name1:
                            self.func_name1.append( name )
                            self.functions1.append( self.functions2[self.index].copy())
                        else:
                            self.idd = self.func_name1.index(name)
                            self.functions1[self.idd] = self.functions2[self.index].copy()
                else: pass
            except IndexError: pass
            except KeyError: pass
        else: pass