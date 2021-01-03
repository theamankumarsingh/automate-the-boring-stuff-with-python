import os,shutil
path=input('Enter path to be walked: ')
pathn=input('Enter path of new folder: ')
for folder,sub,file in os.walk(path):
    for f in file:
        if f[len(f)-4:len(f)]=='.pdf' or f[len(f)-3:len(f)]=='.jpg':
            shutil.copy(folder+'/'+f,pathn)