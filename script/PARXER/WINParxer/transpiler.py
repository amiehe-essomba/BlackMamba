from doctest import master


class TRansPiler:
    def __init__(self, data_base: dict, line: int, history: list = []):
        self.data_base      = data_base
        self.line           = line
        self.history        = history 
        
    def Transformation(self):
        self.vars = self.data_base['Transpiler_for']['variables'].copy()
        self.head = self.data_base['Transpiler_for']['residus_head'].copy()
        self.string = ""
        if self.vars['vars']:
            f = open('trans.py', 'w')
            f.write('def transpiler_loop(data_base: dict ):'+'\n')
            for i in range(len(self.vars['vars'])):
                f.write('\t'+"{} = {}".format(self.vars['vars'][i], self.vars['values'][i])+'\n')
                if self.vars['vars'][i] == self.head['var']: pass
                else:
                    if i < len(self.vars['vars'])-1: self.string += self.vars['vars'][i] +','
                    else: self.string += self.vars['vars'][i]
                    
            f.write('\n')
            f.write("\t"+"for {} in {}:".format(self.head['var'], self.head['val'][1:])+'\n')
            for val in self.history:
                f.write("\t"+'\t'+f"{val}"+'\n')
                
            f.write('\n')
            self.string += ','+self.head['var']
            
            f.write('\treturn ['+f"{self.string}]"+'\n')
          
        else: pass