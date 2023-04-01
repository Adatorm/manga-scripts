from os import walk
from os import path
from os import rename
read_path = "ren"



def get_files(folder_path):
    f = []
    for (dirpath, dirnames, filenames) in walk(folder_path):
        f.extend(filenames)
        break
    return f
    
    
def name_updater(file_name):
    return file_name[7:]
    
    
def change_name(folder_path, file_list):
    for file_name in file_list:
    
        new_file_name = name_updater(file_name)
        
        old_name = path.join(folder_path, file_name)
        new_name = path.join(folder_path, new_file_name)
        rename(old_name, new_name)
        print(f"{old_name} -> {new_name}")


def run():
    files = get_files(read_path)
    change_name(read_path, files)

if __name__ == "__main__":
    run()