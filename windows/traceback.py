import sys
from script.STDIN.LinuxSTDIN    import ascii
from IDE.EDITOR                 import test
from script.STDIN.LinuxSTDIN    import bm_configure      as bm

class traceback:
    def write(string: str, v: str, key : bool = False):
        max_x, max_y    = test.get_win_ter()
        LEN             = max_x - len( bm.remove_ansi_chars().chars(string)) - 2 
        co              = bm.init.bold + bm.init.italic + bm.fg.rbg(255, 0, 255)
        r               = bm.init.reset
        w               = bm.init.bold + bm.fg.rbg(255, 255, 255) 

        
        if LEN >= 0:
            if key is False: string = v + string + " " * LEN + v
            else:string = v + co + string + r +" " * LEN + v
            sys.stdout.write( string + "\n" )
            sys.stdout.flush() 

        else:
            if key is True:
                data, str_, L = [], str_ =  bm.remove_ansi_chars().chars(string), len( str_ )
                while (max_x - L - 2) < 0 : 
                    L //= 2
                    data.append(str_[ : L])
                    str_ = str_[L : ]
                    L = len(str_)
                left    = "........... "
                right   = " ----->"

                for i, s in enumerate(data):
                    if i == 0:
                        string = v + co + s + w + right+ " " * (max_x - len(s) - len(right)) + v 
                    if i < len(data) - 1:
                        string = v + w + left + co + s + r + " " * (max_x - len(s) - len(left)) + v 

                    sys.stdout.write( string + "\n" )
                    sys.stdout.flush()
            else:
                string = v + string + " " * LEN + v
                sys.stdout.write( string + "\n" )
                sys.stdout.flush()

    def trace(List : list, error):
        max_x, max_y    = test.get_win_ter()
        acs             = ascii.frame(True)
        string          = "traceback".upper().center(max_x-2)
        up1             = acs['ul'] + acs['h'] * (max_x-2) + acs['ur']
        up2             = acs['v'] + bm.init.bold + bm.fg.rbg(255, 0, 255) + string + bm.init.reset + acs['v']
        up3             = acs['vl'] + acs['h'] * (max_x-2) + acs['vr']
        up4             = acs['v'] + " " * (max_x-2) + acs['v']
        down            = acs['dl'] + acs['h'] * (max_x-2) + acs['dr']

        sys.stdout.write(bm.move_cursor.LEFT(1000))
        sys.stdout.write(bm.clear.line(2))
        sys.stdout.write('\n' + 
            up1 + '\n' + up2 + '\n' + up3
            )
        if List:
            for s in List:
                traceback.write(string=s, v=acs['v'], key=True)
            traceback.write(string=error, v=acs['v'], key=False)
        else: traceback.write(string=error, v=acs['v'], key=False)

        sys.stdout.write(up4 + "\n" + down+"\n\n")
        sys.stdout.flush()

    def init(data_base, histoty_tracback, error):
        if data_base['all_modules_load']:
            if histoty_tracback['all_modules_load']:
                data_base['all_modules_load'] += histoty_tracback['all_modules_load']
            else: pass 
        else: pass 

        traceback.trace(List = data_base['all_modules_load'], error=error)
    
        error                                                    = None
        data_base['all_modules_load']                            = []
        histoty_tracback                                         = {
        'TrueFileNames'                                          : None,
        "all_modules_load"                                       : None,
        "modules"                                                : None
        }
        data_base['modulesImport']['TrueFileNames']['names']     = []
        data_base['modulesImport']['TrueFileNames']['path']      = []
        data_base['modulesImport']['TrueFileNames']['line']      = []

        return None