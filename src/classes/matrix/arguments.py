
class arg:
    def __init__(self, func_name : str = "std") :
        self.func_name = func_name 
        
    def arguments(self):
        name  = ['reverse', 'axis' ]
        name2 = ['numeric','reverse', 'axis']
        name3 = ['max_float', 'reverse', 'axis']
        
        if    self.func_name in ["quantile"]: return name2
        elif  self.func_name in ['round']   : return name3 
        else: return name 
            