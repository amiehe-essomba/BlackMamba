from script.STDIN.LinuxSTDIN     import bm_configure as bm

class data:
    def __init__(self, master: str ):
        self.master = master 
    def type(self):
        List = ['16', '32', '64', '128', '256', '512']
        int_ = ["int"+x for x in List]
        float_ = ['float'+x for x in List]
        cplx = ['complex'+x for x in List]
        
        key = False 
        string = ""
        for i in range(len(List)):
            if self.master == int_[i]:
                string, key = f"integer( {List[i]}b )", True
                break 
            else: pass 
        if key is False:
            for i in range(len(List)):
                if self.master == float_[i]:
                    string, key = f"float( {List[i]}b )", True
                    break 
                else: pass 

            if key is False:
                for i in range(len(List)):
                    if self.master == cplx[i]:
                        string, key = f"complex( {List[i]}b )", True
                        break 
                    else: pass
            else: pass
        else: pass
         
        return bm.words(string, bm.fg.rbg(255, 255, 255)).final()+bm.init.reset