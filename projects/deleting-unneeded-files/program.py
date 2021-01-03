import os,shutil
path=input('Enter path to be walked: ')
d=0
for folder,sub,file in os.walk(path):
    for f in file:
        p=folder+'/'+f
        n=os.path.getsize(p)
        if(n>100*1024*1024):
            print(p,'| size:',n)
            if d:
                os.unlink(p)