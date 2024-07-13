import os

def del_audiofiles(path):
    dir_name = os.path.dirname(path)
    file_name = os.path.basename(path)

    all_entries = os.listdir(dir_name)
    files = [entry for entry in all_entries if os.path.isfile(os.path.join(dir_name, entry))]
    for file in files:
        if file_name[2:-4] in file:
            os.remove(dir_name + "/" + file)