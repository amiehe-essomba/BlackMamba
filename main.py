from script.LEXER.FUNCTION      import main
from script.PARXER              import parxer_assembly
from script.DATA_BASE           import data_base as db
from script.STDIN.WinSTDIN      import stdin
from script.STDIN.LinuxSTDIN    import bm_configure as bm
import os

ke = bm.fg.rbg(255,255, 0)
we = bm.fg.white_L
be = bm.fg.blue_L


if __name__ == '__main__':
    line = 0
    color = {'0': ke, '1': we}
    _type_ = '>>> '
    error = None
    data_base = db.DATA_BASE().STORAGE()
    
    os.system( 'cls' )
    #bm.head().head( 'Windows')
    
    while True:
        line += 1

        try:
            string = stdin.STDIN(data_base, line).NORMAL_STDIN(color, _type_)
            if string:
                lexer, normal_string, error = main.MAIN(string, data_base, line).MAIN()
                if error is None:
                    if lexer is not None:
                        num, key, error = parxer_assembly.ASSEMBLY(lexer, data_base,
                                                                   line).GLOBAL_ASSEMBLY(normal_string)
                        if error is None:
                            pass
                        else:
                            print('{}\n'.format( error ) )
                    else:
                        pass
                else:
                    print('{}\n'.format( error ) )
            else:
                pass
        except KeyboardInterrupt:
            break
        except EOFError:
            break
