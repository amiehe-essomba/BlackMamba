import sys, os   
from script.DATA_BASE             import data_base as db
from   script.STDIN.LinuxSTDIN    import bm_configure as bm
from   pathlib import Path
from IDE.EDITOR                   import header
import WindowsMain as WM
import LinuxMain_in_testing as LM

def run_mamba():
    # get root path 
    root    = os.path.abspath(os.curdir)
    s = Path(__file__).resolve().parents[2]
    # get system name
    system  = os.uname()[0]
    print(system)
    # get arguments 
    arg     = sys.argv
    
    # running code if system is Linux or macOs
    if system in ['Linux', 'macOs']:
        # run code with pegasus code iditor
        if len(arg) == 1:
            try:
                os.system('clear')
                sys.stdout.write(bm.save.save)
                header.header()
                data_base = db.DATA_BASE().STORAGE().copy()
                LM.linux( data_base=data_base).terminal(c=bm.fg.rbg(255, 255, 255))
            except KeyboardInterrupt:  pass
            except SyntaxError: pass

        # get mamba version && author 
        elif len(arg) == 2:
            # get version of code
            if arg[1] in ['--V', '--version']:
                s = bm.init.underline+bm.fg.yellow_L + 'Black Mamba' + \
                    bm.init.reset + bm.fg.white_L + ' version ' + \
                    bm.init.reset+bm.fg.cyan_L + '1.0.0'+bm.init.reset
                print(f"\n{s}\n")
            # get author 
            elif arg[1] in ['--author', '--A']:
                bm.open_graven().author()
            elif arg[1][-3:] in ['.bm'] :pass 
            else: print(bm.mamba_error.error3())
        elif len(arg) == 3:
            # runnning code with pegasus of orion editor it depends of the arg[2] value
            if arg[1] == '--T':
                if arg[2] in [ 'pegasus', 'orion']:
                    terminal = arg[2]+" terminal"

                    try:
                        os.system('clear')
                        sys.stdout.write(bm.save.save)
                        header.header(terminal=terminal)
                        data_base = db.DATA_BASE().STORAGE().copy()
                        LM.linux( data_base=data_base).terminal(c=bm.fg.rbg(255, 255, 255), terminal_name=terminal)
                    except KeyboardInterrupt:  pass
                    except SyntaxError: pass
                else: print(bm.mamba_error.error2())
            else: print(bm.mamba_error.error2())
    else: print(bm.mamba_error.error1())
    
if __name__ == '__main__':
    os.system('clear')
    sys.stdout.write(bm.save.save)
    run_mamba()
