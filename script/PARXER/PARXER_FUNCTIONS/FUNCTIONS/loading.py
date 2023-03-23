def Loading(info: dict, DataBase: dict, db: dict):
    if info['module_main'][0] in DataBase['modulesImport']['moduleLoading']['names']:
        idd = DataBase['modulesImport']['moduleLoading']['names'].index(info['module_main'][0])
        DataBase['modulesImport']['moduleLoading']['loading'][idd] = db['modulesImport' ].copy()
    else: 
        DataBase['modulesImport']['moduleLoading']['names'].append(info['module_main'][0])
        DataBase['modulesImport']['moduleLoading']['loading'].append(db['modulesImport'].copy())

    return DataBase.copy()