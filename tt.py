from windows.windows import IDE 
import sys, os
from script.STDIN.LinuxSTDIN    import bm_configure                 as bm
from IDE.EDITOR                 import header, string_to_chr 
from IDE.EDITOR                 import test
from script.DATA_BASE           import data_base                    as db

if __name__ == "__main__":
    term, color = 'orion', bm.init.bold + bm.fg.rbg(255, 255, 255)
    try:
        sys.stdout.write(bm.clear.screen(pos=2))
        os.system('cls')
        sys.stdout.write(bm.save.save)
        max_x, max_y  = test.get_win_ter()
        if max_x >= 100:
            if term == 'orion': 
                header.header(terminal='orion terminal')
                color = bm.init.bold + bm.fg.rbg(255, 255, 0)
            else: header.header(terminal='pegasus terminal')
        else: pass 
        
        data_base = db.DATA_BASE().STORAGE().copy()
        IDE( data_base=data_base).terminal(c=color, terminal_name=term)
    except KeyboardInterrupt:  pass
    except IndexError: pass