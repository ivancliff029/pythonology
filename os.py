import os

currentDir = os.getcwd()
folder = 'ghost'

path = os.path.join(currentDir, folder)

os.mkdir(path)
print("directory '%s' was created" %folder)