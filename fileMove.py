import os,shutil
directory='/home/jahir/Desktop/'
makedir=raw_input("Choice your folder name = ")
file=raw_input("Choice your file name = ")
if not os.path.exists(directory+makedir):
    os.mkdir(directory+makedir)
x=next(os.walk(directory+makedir))[2]
if file not in x:
    if os.path.exists(directory+file):
        shutil.move(directory+'/'+file,directory+makedir+'/'+file)
    else:
        os.mknod(directory+makedir+"/"+file)


