import os, json
def cd(file_path, create=True):
    if not create and os.path.exists(file_path):
        os.remove(file_path)
    if create: 
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump({}, file)