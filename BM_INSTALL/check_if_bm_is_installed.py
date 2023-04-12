import os 

def mamba(path_destination_folder):
    root_path  = path_destination_folder+"/BlackMamba" #os.path.abspath(os.curdir)
    
    if os.path.isdir(root_path) is True:
        name  = 'black_mamba_location'
        direct_access = root_path+f"/BM_INSTALL/{name}/path.bm"
        indirect_access = root_path+f"/BM_INSTALL/{name}/install.bm"
        list_dir = os.listdir(root_path+"/BM_INSTALL/")
        
        if name in list_dir:
            if os.path.isfile(direct_access) is True:
                __bool__ = os.stat(direct_access)==0
                if __bool__ is False:
                    ___bool___ = os.stat(indirect_access)==0
                    if ___bool___ is False:
                        with open(direct_access, 'r') as f:
                            abs_path = f.readline().rstrip()
                        f.close()
                        return abs_path
                    else: return None
                else: return None
            else: return None
        else: return None
    else: return None