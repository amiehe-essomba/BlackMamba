from script.PARXER.PARXER_FUNCTIONS.CLASSES         import convert
from script.DATA_BASE                               import data_base 

def Loading(info: dict, DataBase: dict, db: dict, line : int = 1, locked : bool = False, error : str=None):
    if info['module_main'][0] in DataBase['modulesImport']['moduleLoading']['names']:
        idd = DataBase['modulesImport']['moduleLoading']['names'].index(info['module_main'][0])
        DataBase['modulesImport']['moduleLoading']['loading'][idd] = db['modulesImport' ].copy()
    else: 
        DataBase['modulesImport']['moduleLoading']['names'].append(info['module_main'][0])
        DataBase['modulesImport']['moduleLoading']['loading'].append(db['modulesImport'].copy())
    traceback(db, DataBase)

    _names_ = DataBase[ 'modulesImport' ][ 'moduleLoading' ]['names'].copy()
    
    if error is None:
        for i, nm in enumerate( _names_ ):
            my_data_base = data_base.DATA_BASE().STORAGE().copy()
            fileNames = DataBase[ 'modulesImport' ][ 'moduleLoading' ]['loading'][i]['fileNames']
            
            if fileNames:
                for j in range(len(fileNames)):
                    data = DataBase[ 'modulesImport' ][ 'moduleLoading' ]['loading'][i]['expressions'][j]
                    my_data_base, error = convert.convert(my_data_base.copy(), line).convert(data, True)
                    
                    if error is None:
                        if my_data_base['class_names']:
                            for w, name in enumerate(my_data_base['class_names']):
                                if name in DataBase['class_names']:
                                    idd = DataBase['class_names'].index( name ) 
                                    DataBase['classes'][idd] = my_data_base['classes'][w].copy()
                                else:
                                    DataBase['class_names'].append( name )
                                    DataBase['classes'].append( my_data_base['classes'][w].copy() )
                        else: pass 

                        if my_data_base['func_names']:
                            for w, name in enumerate(my_data_base['func_names']):
                                if name in DataBase['func_names']:
                                    idd = DataBase['func_names'].index(name) 
                                    DataBase['functions'][idd] = my_data_base['functions'][w].copy()
                                else:
                                    DataBase['func_names'].append(name)
                                    DataBase['functions'].append( my_data_base['functions'][w].copy() )
                        else: pass 
                    
                        traceback(my_data_base, DataBase)
                    else: break 

        del my_data_base
    else: pass
    
    return DataBase, error


def traceback(data : dict, main : dict):
    if data['modulesImport']['TrueFileNames']['path']:
        l = len(data['modulesImport']['TrueFileNames']['path'])

        try:
            for i in range(l):
                s = data['modulesImport']['TrueFileNames'].copy() 
                p = main['modulesImport']['TrueFileNames'].copy()
                if s['path'][i] in p['path']: 
                    if s['names'][i] in p['names']: pass
                    else : 
                        main['modulesImport']['TrueFileNames']['path'].append(s['path'][i])
                        main['modulesImport']['TrueFileNames']['line'].append(s['line'][i])
                        main['modulesImport']['TrueFileNames']['names'].append(s['names'][i])
                else: 
                    main['modulesImport']['TrueFileNames']['path'].append(s['path'][i])
                    main['modulesImport']['TrueFileNames']['names'].append(s['names'][i])
                    main['modulesImport']['TrueFileNames']['line'].append(s['line'][i])

            if data['all_modules_load']:
                for s in data['all_modules_load']:
                    if s not in main['all_modules_load'] : main['all_modules_load'].append(s)
                    else: pass
            else : pass 
        except NameError: pass
    else: pass