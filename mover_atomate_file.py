from os import listdir
import os, time
import shutil

formatSet = {
    'aif': 'Audio',
    'cda': 'Audio',
    'mp3': 'Audio',
    'mpa': 'Audio',
    'ogg': 'Audio',
    'wav': 'Audio',
    'wma': 'Audio',

    '7Z': 'Compressed',
    'pkg': 'Compressed',
    'zip': 'Compressed',
    'rar': 'Compressed',
    'tag.gz': 'Compressed',
    'bin': 'Compressed',
    'dmg': 'Compressed',
    'iso': 'Compressed',
    'tar': 'Compressed',

    'ai': 'Image',
    'bmp': 'Image',
    'svg': 'Image',
    'png': 'Image',
    'jpg': 'Image',
    'jpeg': 'Image',
    'tif': 'Image',
    'raw': 'Image',
    'psd': 'Image',

    'other': 'Other',

    'py': 'Script',
    'java': 'Script',
    'c': 'Script',
    'cpp': 'Script',
    'html': 'Script',
    'css': 'Script',
    'js': 'Script',
    'ts': 'Script',

    'pdf': 'Documents',
    'ebpu': 'Documents',
}

# add the source path of the files
source_path = './source folder'

# add here the destination directory
destination_path = '/Users/subhasis/DAA/project/Auto_mover/destination'


# move all the files from  one folder to other folder
def movetodestination(paths: str, source_dir: str, destination_dir: str):
    for f in paths:

        fileExtension = f.split('.')[-1]
        if fileExtension not in formatSet:
            fileExtension = 'other'

        if f != '.DS_Store':
            destination_path = str(destination_dir) + '/' + str(formatSet[fileExtension]) + '/'
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            print(destination_path)
            shutil.move(os.path.join(source_dir, f), os.path.join(destination_path, f))

            # except IOError as io_err:
            #
            #     print(destination_path)
            #     os.makedirs(os.path.dirname(destination_path))
            #     shutil.move(os.path.join(source_dir, f), os.path.join(destination_path, f))


# access all the files from the source folder
source_path_files = listdir(source_path)[1:]
# moveToDestination(source_path_files, source_path, destination_path)

# check if any change is done on the directory

path_to_watch = './source folder'
before = dict([(f, f.split('.')[-1]) for f in os.listdir(path_to_watch)])
print(before)

while True:
    time.sleep(20)
    after = dict([(f, f.split('.')[-1]) for f in os.listdir(path_to_watch)])

    # add the newly added file to the previous list
    added = []
    for file in after:
        if file != '.DS_Store':
            added.append(file)

    if len(after) == 0:
        continue

    if before != after:
        print(after)
        # call the mover function
        source_path_files += added
        movetodestination(source_path_files, path_to_watch, destination_path)
        # if any mismatch happen dont break
        # make it continue

        continue

    else:
        # if mismatch happen
        # then transfer the existing file to the destination directory 
        movetodestination(source_path_files, path_to_watch, destination_path)
        continue
