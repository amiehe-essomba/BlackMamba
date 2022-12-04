from script.STDIN.LinuxSTDIN    import bm_configure     as bm

class mamba:
    def __init__(self):
        self.r      = bm.init.bold + bm.fg.red_L
        self.b      = bm.init.bold + bm.fg.black_L
        self.c      = bm.init.bold + bm.fg.cyan_L
        self.g      = bm.init.bold + bm.fg.green_L
        self.w      = bm.init.bold + bm.fg.white
        self.re     = bm.init.reset
        self.s      = f"{self.c}${self.re}"
        self.hb6    = f"{self.c}______{self.re}"
        self.hb2    = f"{self.c}__{self.re}" 
        self.car    = f"{self.r}[{self.g}+{self.r}]{self.re}" 
        self.vb5    = f"{self.c}{chr(124)}\n{chr(124)}\n{chr(124)}\n{chr(124)}\n{chr(124)}{self.re}"
        self.vb2    = f"{self.c}{chr(124)}\n{chr(124)}{self.re}"
        self.ss     = self.w+f" _\n{chr(40)}{chr(186)})"+self.re
        self.top    = self.s*6
        self.ab     = "\{}".format("")
        self.h      = f"{self.c}/  {self.ab}    /   |{self.re}"
        self.hs5    = f"{self.c}$$  {self.ab}  / $$ |\n$$$  {self.ab}/ $$$ |\n$$$$ / $$$$ |\n$$ $$ $$ $$ |\n$$ |$$$  $$ |\n$$ | $   $$ |\n$$/      $$/{self.re}"

    def m(self): 
        m = f" {self.hb2}      {self.hb2}\n{self.h}\n{self.hs5}"
        print(f"{m}")
        

if __name__ == '__main__':
    mamba().m()