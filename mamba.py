from platform import python_version
from site import abs_paths
import sys, os   
import LinuxMain_in_testing as LM
from script.DATA_BASE             import data_base as db
from script.STDIN.LinuxSTDIN      import bm_configure as bm
from pathlib                      import Path
from IDE.EDITOR                   import header
from IDE.EDITOR                                         import test
from script.PARXER.PARXER_FUNCTIONS._FOR_.FOR.WIN       import for_analyze 
from loop                                               import mainFor
from script.PARXER                                      import numerical_value    
from script.PARXER.WINParxer                            import num_val 
from script.MATHS                                       import mathematics
from CythonModules.Linux                                import NumeriCal 
from CythonModules.Linux.PARTIAL_PARSER                 import parserError 
from logging.handlers                                   import TimedRotatingFileHandler
from threading                                          import Timer
from script.PARXER.PARXER_FUNCTIONS._IF_                import loop_if_statement
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import loop_unless_statement 
from script.PARXER.WINParxer                            import transpiler 
from script                                             import control_string as CS   
from numba                                              import njit, jit, cfunc
from BM_ERRORS                                          import errors
import BlackMamba

def run_mamba():
    # get root path 
    root    = os.path.abspath(os.curdir)
    s = Path(__file__).resolve().parents[1]
    # get system name
    system  = os.uname()[0]
    # get arguments 
    arg     = sys.argv
    
    # running code if system is Linux or macOs
    if system in ['Linux']:
        python_version = sys.version.split()[0].split('.')
        python_version = [int(x) for x in python_version]
        if python_version[0] >= 3:
            if python_version[1] >=8 :
                # run code with pegasus code iditor
                if len(arg) == 1:
                    try:
                        terminal = 'pegasus'
                        os.system('clear')
                        sys.stdout.write(bm.save.save)
                        max_x, max_y = test.get_linux_ter()
                        if max_x >= 100: header.header(terminal = 'pegasus terminal')
                        else: pass
                        data_base = db.DATA_BASE().STORAGE().copy()
                        LM.linux( data_base=data_base).terminal(c=bm.fg.rbg(255, 255, 255), terminal_name=terminal)
                        print(s,'\n', root)
                    except KeyboardInterrupt:  pass
                    except SyntaxError: pass
                # get mamba version && author 
                elif len(arg) == 2:
                    # get version of code
                    if arg[1] in ['--V', '--Version']:
                        s = bm.init.underline+bm.fg.yellow_L + 'Black Mamba' + \
                            bm.init.reset + bm.fg.white_L + ' version ' + \
                            bm.init.reset+bm.fg.cyan_L + '1.01.01'+bm.init.reset
                        print(f"\n{s}\n")
                    # get author 
                    elif arg[1] in ['--Author', '--A']:
                        bm.open_graven().author()
                    elif arg[1][-3:] in ['.bm'] :
                        if '/'in arg[1] : 
                            path = arg[1].split('/')
                            name = path[-1]
                            if path[:-1]:
                                str_ = '/'
                                n = len(path[:-1])
                                for i in range(n):
                                    str_ += path[i]+'/'
                                abs_path = root + str_ 
                                string = path[-1]
                                try:
                                    check_path = os.listdir(abs_path)
                                    check_file = os.path.isfile(abs_path+f"{string}/")
                                    if check_file is True:
                                        string, err = CS.STRING_ANALYSE({}, 0).CHECK_NAME(string, True)
                                        if err is None: return BlackMamba.mamba_interpretor(string)
                                        else: print(errors.mamba_error().ERROR3(string))
                                    else: print(errors.mamba_error().ERROR7(string))
                                except FileNotFoundError: print(errors.mamba_error().ERROR8(abs_path))
                            else: print(errors.mamba_error().ERROR6()) 
                        else:
                            string = arg[1][ : -3]
                            string, err = CS.STRING_ANALYSE({}, 0).CHECK_NAME(string, True)
                            if err is None: return BlackMamba.mamba_interpretor(f"{arg[1]}")
                            else: print(errors.mamba_error().ERROR3(string))
                    else: print(errors.mamba_error().ERROR3(string))
                elif len(arg) == 3:
                    # runnning code with pegasus of orion editor it depends of the arg[2] value
                    if arg[1] == '--T':
                        if arg[2] in [ 'pegasus', 'orion']:
                            terminal = arg[2]+" terminal"
                            try:
                                os.system('clear')
                                sys.stdout.write(bm.save.save)
                                max_x, max_y = test.get_linux_ter()
                                if max_x >= 100: header.header(terminal = terminal)
                                else: pass
                                data_base = db.DATA_BASE().STORAGE().copy()
                                LM.linux( data_base=data_base).terminal(c=bm.fg.rbg(255, 255, 255), terminal_name=arg[2])
                            except KeyboardInterrupt:  pass
                            except SyntaxError: pass
                        else: print(errors.mamba_error().ERROR4(arg[2]))
                    else: print(errors.mamba_error().ERROR5(arg[1]))
                else : print(errors.mamba_error().ERROR6()) 
            else:print(errors.mamba_error().ERROR9())
        else: print(errors.mamba_error().ERROR9())
    else: print(errors.mamba_error().ERROR1(system))
    
if __name__ == '__main__':
    os.system('clear')
    sys.stdout.write(bm.save.save)
    run_mamba()
