import tarfile 
from tqdm import tqdm 
import time

def decompressed(tar_file, path, members=None):
    # extracts 'tar file and puts the members to path
    # if members if None, all memebers on tar file will be extracted
    
    tar = tarfile.open(tar_file, mode="r:gz")
    
    if members is None: members = tar.getmembers()
    else: pass 
    
    progress = tqdm(members)
    
    for member in progress:
        tar.extract(member, path=path)
        progress.set_description(f"Extracting {member.name}")
        time.sleep(0.1)
    # or use the file 
    # clse the file 
    tar.close()
    
def compressed(tar_file, members):
    # adds files (members) to a tar_file and compress it
    
    # open file fo gzip compressed writing 
    tar = tarfile.open(tar_file, mode='w:gz')
    # with progress 
    # set the progress 
    
    progress = tqdm(members)
    for member in progress:
        # add file/folder/link to the file (compress)
        tar.add(member)
        
        # set the progress description of the progress bar 
        progress.set_description(f"Compressing {member}")
        time.sleep(0.1)
    # close the file
    
    tar.close()
    
# compressed("exemple.tar.gz", ["test.text, "test_folder])
# decompressed("example.tar.gz", "extracted", None)

