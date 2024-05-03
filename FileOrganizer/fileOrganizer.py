# import modules
import os
import shutil

# create variables
path = input("Enter Folder Path: ") # directory path
files = os.listdir(path)  # list of files

# loop through all files
for file in files:
    filename,extension = os.path.splitext(file) # split name and extension
    extensions = extension[1:] # remove the '.' in the extension

    # If extension folder exists, move folder there
    if os.path.exists(path + '/' + extension):
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

    # Else make the folder, then move the file
    else:
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

