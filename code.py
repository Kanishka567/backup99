import os
path='/Users/Kanishka Singh/Desktop/C-99/file.txt'
root_ext=os.path.splitext(path)
print("root part ",root_ext[0])
print ("ext part ",root_ext[1],"\n") 