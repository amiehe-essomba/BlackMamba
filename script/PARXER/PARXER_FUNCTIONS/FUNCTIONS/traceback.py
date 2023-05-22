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