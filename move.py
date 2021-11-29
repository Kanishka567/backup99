import os
import shutil
path="/Users/Kanishka Singh/Desktop/C-99"
print('before moving file')
print (os.listdir(path))
source="/Users/Kanishka Singh/Desktop/C-99/file.txt"
destination = "/Users/Kanishka Singh/Desktop/C-99/newfolder"
dst=shutil.move(source,destination)
print("after moving file")
print (os.listdir(path))