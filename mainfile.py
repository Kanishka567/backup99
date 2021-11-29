import os
import shutil
path="/Users/Kanishka Singh/Desktop/C-99"
print('before copying file')
print (os.listdir(path))
source="/Users/Kanishka Singh/Desktop/C-99/move.py"
destination = "/Users/Kanishka Singh/Desktop/C-99/move2.py"
dst=shutil.copy(source,destination)
print("after copying file")
print (os.listdir(path))