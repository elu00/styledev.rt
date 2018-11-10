import os
path_to_dumped_textures = ''
path_to_actual_textures = ''

 # FILL THE ABOVE IN

def recurisveGetFullPath(walk):
    list_of_stuff = []
    for dir in walk:
        for file in dir[2]:
            list_of_stuff += [dir[0] + '/' + file]
    return list_of_stuff


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None

print(recurisveGetFullPath(os.walk('.')))

