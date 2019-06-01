import os
import shutil

#folder
def create_dir(name , address ):
    os.mkdir(address+"\\"+name);

#file
def create_file(name , address ):
    path = address+"\\"+name
    with open(path, 'a') as f:
        f.write()
        
#remove folder
def delete_folder(name , address ):
    shutil.rmtree(address)
    
#remove file
def delete(name , address ): 
    for file_object in os.listdir(address):
        file_object_path = os.path.join(address+"\\"+name)
        if os.path.isfile(file_object_path):
            os.unlink(file_object_path)
       
#find file
def find(name , address ): 
    path = address
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result
    
