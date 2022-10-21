import sys, os   
from   script.STDIN.LinuxSTDIN    import bm_configure as bm
from   pathlib import Path
import LinuxMain as LM  
import WindowsMain as WM


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
            bm.head().head(sys=system)
            LM.run(syst=system).run()
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
                    bm.head().head(sys=system, term = arg[2])
                    LM.run(term=arg[2], syst=system).run()
                else: print(bm.mamba_error.error2())
            else: print(bm.mamba_error.error2())
    else: print(bm.mamba_error.error1())
    
if __name__ == '__main__':
    os.system('clear')
    sys.stdout.write(bm.save.save)
    run_mamba()