#############################################################
#############################################################
# Black Mamba Windows Interpretor                           #
# This version has currently two code iditors:              #
#                                                           #
#                                                           #
# * pegasus is the default editor                           #
# * orion is the optimized code editor with a syntaxis      #
#   color                                                   #
# basically we can use both without any problems because    #
# they work very well.                                      #
#                                                           #
#                                                           #
# * to select a terminal it's very simple, just do this     #
#                                                           #
#       * mamba --T orion                                   #
#       * mamba --T pegasus                                 #
#############################################################
# **created by : amiehe-essomba                             #
# **updating by: amiehe-essomba                             #
#############################################################


from script                     import control_string
from script.LEXER.FUNCTION      import main
from script.DATA_BASE           import data_base                as db
from script.STDIN.LinuxSTDIN    import bm_configure             as bm
from script.PARXER.WINParxer    import parxer_for_interpreter   as PFI
import os


def mamba_interpretor( string ):
    ke = bm.fg.rbg(255,255, 0)
    we = bm.fg.white_L
    be = bm.fg.blue_L
    data_from_file  = []
    currunt_file    = os.path.basename(__file__) 
    control         = control_string.STRING_ANALYSE( {}, 1 )
    
    path_library    = f"{os.path.abspath(os.curdir)}/{string}"
    
    with open(file=path_library, mode='r') as file:
        for line in file.readlines():  
            if line[-1] == '\n': line = line[:-1]
            else: pass
            data_from_file.append( line  )
            
    data_base   = db.DATA_BASE().STORAGE().copy()
    line        = 0
    error       = None
    key         = True
    historyFile = { 
        'names'     : ['iris'],
        'path'      : [None],
        'line'      : [line]
    }
    data_base['modulesImport']['TrueFileNames']['line'].append(line)
    data_base['modulesImport']['TrueFileNames']['path'].append(None)
    data_base['modulesImport']['TrueFileNames']['names'].append('iris')
    
    
    if not data_from_file: 
        print( bm.mamba_error().ERROR2(string) )
    else:
        for x, string in enumerate( data_from_file ):
            line += 1
            data_base['modulesImport']['TrueFileNames']['line'][0]=line
            if string:
                if data_base['globalIndex'] is None:
                    try:
                        data_base['starter'] = x+1
                        lexer, normal_string, error = main.MAIN(string, data_base, line).MAIN( interpreter = True, MainList = data_from_file[x+1: ] )
                        if error is None:
                            if lexer is not None:
                                num, key, error = PFI.ASSEMBLY(lexer, data_base, line).GLOBAL_ASSEMBLY_FOR_INTERPRETER(normal_string, True,
                                                                                    MainList = data_from_file[x+1: ], baseFileName = currunt_file)
                                
                                if error is None: pass
                                else: 
                                    print('{}\n'.format( error ) )
                                    break
                            else: pass
                        else: 
                            print('{}\n'.format( error ) )
                            break
                    except EOFError: break
                else:
                    if x < data_base['globalIndex']+1: pass 
                    else:
                        try:
                            data_base['starter'] = x+1
                            lexer, normal_string, error = main.MAIN(string, data_base, line).MAIN( interpreter = True, MainList = data_from_file[x+1: ] )
                            if error is None:
                                if lexer is not None:
                                    num, key, error = PFI.ASSEMBLY(lexer, data_base, line).GLOBAL_ASSEMBLY_FOR_INTERPRETER(normal_string, True,
                                                                                    MainList = data_from_file[x+1: ], baseFileName = currunt_file)
                                    
                                    if error is None: pass
                                    else:
                                        print('{}\n'.format( error ) )
                                        break
                                else: pass
                            else: 
                                print('{}\n'.format( error ) )
                                break
                        except EOFError: break
            else: pass
    