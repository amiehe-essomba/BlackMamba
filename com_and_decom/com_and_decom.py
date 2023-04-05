import tarfile 
from tqdm import tqdm

def decompressed(tar_file, path, members=None):
    tar = tarfile.open(tar_file, mode="r:gz")
    
    progress = tqdm(members)
    
    if members is None: members = tar.getmembers()
    else: pass
    
    for member in members:
        tar.extract(member, path=path)
        progress.set_description(f"EXTRACTING {member.name}")
    tar.close() 
    
def compressed(tar_file, members):
    tar = tarfile.open(tar_file, mode="w:gz")
    
    progress = tqdm(members)
    
    for member in members:
        tar.add(member)
        progress.set_description(f'COMPRESSING {member}')
    
    tar.close()
        
 
# compressed("my_tar.tar.gz", ["test.txt, "test_folder"])
# decompressed("my_tar.tar.gz", "extracted", None)
    