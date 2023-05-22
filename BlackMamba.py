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
from CythonModules.Windows      import fileError                as fe
from script.STDIN.LinuxSTDIN    import bm_configure             as bm
from script.PARXER.WINParxer    import parxer_for_interpreter   as PFI
import os
import numpy as np

def B_PATH(system, file_name):
    current_file = os.path.abspath(os.curdir)

    if system == 'Windows': abs_path_plus_file_name = current_file + f"\\{file_name}"
    else: abs_path_plus_file_name = current_file + f"/{file_name}"

    return abs_path_plus_file_name

def read_file(path):
    data_from_file = []
    
    with open(file=path, mode='r') as file:
        for line in file.readlines():
            if line[-1] == '\n': line = line[:-1]
            else: pass
            data_from_file.append( line.rstrip() )

    return data_from_file

def break_file(file, typ="\\"):
    file_name = file.split('\\')
    true_name, idd, dir_ = "", -1, ""
    
    if len(file_name) == 1:  return file, dir_ 
    else:
        for i in range(len(file_name)):
            try:
                if file_name[idd] :
                    true_name = file_name[idd]
                    break 
                else: id -= 1
            except IndexError: break 

        if true_name:
            rest = file_name[:-idd]
            if rest:
                for r in rest:
                    if s == '' : s =typ 
                    else: pass 
                    dir_ += s 
            else: pass 
        else: dir_ = file

        return true_name, dir_

def SubMain( system = 'Windows', file_name : str = '' ):
    data_from_file, error = None, None

    # checking if bm file was detected 
    if file_name:
        # building the enitire path of the file 
        abs_path_plus_file_name = B_PATH(system, file_name)
        try:
            # checking if the file is not empty
            if os.stat(abs_path_plus_file_name).st_size != 0:
                data_from_file = read_file(abs_path_plus_file_name)
            else: 
                F, D = break_file(abs_path_plus_file_name)
                error  =ERRORS(1).ERROR2(F) 
        except FileNotFoundError:
            F, D = break_file(abs_path_plus_file_name)
            if F: error  =ERRORS(1).ERROR0(F) 
            else: error  =ERRORS(1).ERROR1(D) 
    else: error  =ERRORS(1).ERROR3()

    return data_from_file, error 

def MAIN(system = 'Windows', file_name : str = ''):
    # initialize the data base 
    data_base   = db.DATA_BASE().STORAGE().copy()
    # line 
    line        = 0
    # error 
    error       = None
    # key activation 
    key         = True
    ind         = 0
    # traceback history 
    historyFile = { 
        'names'     : [""],
        'path'      : [None],
        'line'      : [line]
    }
    # reading the input file 
    data_from_file, error = SubMain(system, file_name)

    # checking first is the input exists or is not empty 
    if error is None:
        # current main input abs path
        current_file    = B_PATH(system, file_name)
        # his name and location 
        NAME, DIR       = break_file(file_name)
        # initialization
        historyFile["names"][0], historyFile["path"][0] = NAME, current_file

        # initialization
        data_base['modulesImport']['TrueFileNames']['line'].append(line)
        data_base['modulesImport']['TrueFileNames']['path'].append(current_file)
        data_base['modulesImport']['TrueFileNames']['names'].append(NAME)
        data_base['all_modules_load'].append(current_file)

        if not data_from_file: pass 
        else:
            for x, string in enumerate( data_from_file ):
                line += 1
                data_base['modulesImport']['TrueFileNames']['line'][0]=line
                if string:
                    if data_base['globalIndex'] is None:
                        try:
                            data_base['starter'] = x+1
                            if x >= ind :
                                lexer, normal_string, error = main.MAIN(
                                            master = string, 
                                            data_base = data_base, 
                                            line = line
                                            ).MAIN( 
                                                interpreter = True, 
                                                MainList = data_from_file[x+1: ] 
                                                )
                                if error is None:
                                    if lexer is not None:
                                        if data_base['globalIndex'] is None: 
                                            new_array, ind = data_from_file[x + 1 : ], 0
                                        else:
                                            ind                     = data_base['globalIndex']
                                            data_base['starter']    = ind
                                            new_array               = data_from_file[ind + 1 : ]

                                        num, key, error = PFI.ASSEMBLY(
                                                master=lexer, 
                                                data_base=data_base, 
                                                line=line
                                                ).GLOBAL_ASSEMBLY_FOR_INTERPRETER(
                                                        main_string = normal_string, 
                                                        interpreter = True,
                                                        MainList = new_array, 
                                                        baseFileName = current_file
                                                        )
                                        
                                        if error is None: pass
                                        else: 
                                            print('{}\n'.format( error ) )
                                            break
                                    else: pass
                                else: 
                                    print('{}\n'.format( error ) )
                                    break
                            else: pass
                        except EOFError: break
                    else:
                        if x < data_base['globalIndex']+1: pass 
                        else:
                            try:
                                before = data_base['globalIndex']
                                data_base['starter'] = x+1
                                lexer, normal_string, error = main.MAIN(
                                            master=string, 
                                            data_base = data_base, 
                                            line = line).MAIN( 
                                                    interpreter = True, 
                                                    MainList = data_from_file[x+1: ] 
                                                    )
                                if error is None:
                                    if lexer is not None:
                                        ind = np.abs(before -  data_base['globalIndex'])
                                        if ind == 0: new_array, ind = data_from_file[x + 1 : ], 0
                                        else:
                                            ind                     = data_base['globalIndex']
                                            data_base['starter']    = ind
                                            new_array               = data_from_file[ind + 1 : ]

                                        num, key, error = PFI.ASSEMBLY(
                                                master = lexer, 
                                                data_base = data_base, 
                                                line= line
                                                ).GLOBAL_ASSEMBLY_FOR_INTERPRETER(
                                                    main_string = normal_string, 
                                                    interpreter = True,
                                                    MainList = new_array, 
                                                    baseFileName = current_file
                                                    )
                                        
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
    else: print('{}\n'.format( error ) )
    

class ERRORS:
    def __init__(self, line):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}not found. {}line: {}{}'.format(self.green, self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'FileNotFoundError' ).Errors()+'{}{} '.format(self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR1(self, string: str):
        error = '{}not found. {}line: {}{}'.format(self.green, self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'DirectoryNotFoundError' ).Errors()+'{}{} '.format(self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR2(self, string: str):
        error = '{}is empty. {}line: {}{}'.format(self.green, self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'FileError' ).Errors()+'{}{} '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR3(self):
        error = '{}Not input. {}line: {}{}'.format(self.green, self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ error

        return self.error+self.reset
