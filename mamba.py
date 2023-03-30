import sys, os 
import platform
import WindowsMain as WM  
import imp 
import configparser
import logging
from loggerWriter                                       import loggerWriter
from pathlib                                            import Path
from IDE.EDITOR                                         import test
from IDE.EDITOR                                         import header 
from script.DATA_BASE                                   import data_base    as db
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from loop.loop_constructor                              import loop_if_statement
from loop.loop_constructor                              import loop_unless_statement
from script.PARXER.PARXER_FUNCTIONS._FOR_.FOR.WIN       import for_analyze 
from loop                                               import mainFor
from script.PARXER                                      import numerical_value    
from script.PARXER.WINParxer                            import num_val 
from script.MATHS                                       import mathematics
from CythonModules.Windows                              import NumeriCal 
from CythonModules.Windows.PARTIAL_PARSER               import parserError 
from logging.handlers                                   import TimedRotatingFileHandler
from threading                                          import Timer


def run_mamba():
    # get root path 
    root    = os.path.abspath(os.curdir)
    s = Path(__file__).resolve().parents[2]
    # get system name
    system  = platform.system()
    # get arguments 
    arg     = sys.argv
   
    # running code if system is Linux or macOs
    if system not in ['Linux', 'macOs']:
        # run code with pegasus code iditor
        if   len(arg) == 1:
            term = 'pegasus'
            try:
                #imp.reload(sys)
                sys.stdout.write(bm.clear.screen(pos=2))
                os.system('cls')
                sys.stdout.write(bm.save.save)
                max_x, max_y  = test.get_win_ter()
                if max_x >= 100:
                    if term == 'orion': header.header(terminal='orion terminal')
                    else: header.header(terminal='pegasus terminal')
                else: pass 
                
                data_base = db.DATA_BASE().STORAGE().copy()
                WM.windows( data_base=data_base).terminal(c=bm.fg.rbg(255, 255, 255), terminal_name=term)
            except KeyboardInterrupt:  pass
            except IndexError: pass
        # get mamba version && author 
        elif len(arg) == 2:
            # get version of code
            if arg[1] in ['--V', '--Version']:
                s = bm.init.underline+bm.fg.yellow_L + 'Black Mamba' + \
                    bm.init.reset + bm.fg.white_L + ' version ' + \
                    bm.init.reset+bm.fg.cyan_L + '1.0.0'+bm.init.reset
                print(f"\n{s}\n")
            # get author 
            elif arg[1] in ['--Author', '--A']:
                bm.open_graven().author()
            elif arg[1][-3:] in ['.bm'] :pass 
            else: print(bm.mamba_error.error3())
        
        elif len(arg) == 3:
            # runnning code with pegasus of orion editor it depends of the arg[2] value
            if arg[1] == '--T':
                if arg[2] in [ 'pegasus', 'orion']:
                    term = arg[2]
                    try:
                        sys.stdout.write(bm.clear.screen(pos=2))
                        os.system('cls')
                        sys.stdout.write(bm.save.save)
                        max_x, max_y  = test.get_win_ter()
                        if max_x >= 100:
                            if term == 'orion': header.header(terminal='orion terminal')
                            else: header.header(terminal='pegasus terminal')
                        else: pass 
                        
                        data_base = db.DATA_BASE().STORAGE().copy()
                        WM.windows( data_base=data_base).terminal(c=bm.fg.rbg(255, 255, 255), terminal_name=term)
                    except KeyboardInterrupt:  pass
                    except IndexError: pass
                else: print(bm.mamba_error.error2())
            else: print(bm.mamba_error.error2())
    else: print(bm.mamba_error.error1())
    
if __name__ == '__main__':
    run_mamba()