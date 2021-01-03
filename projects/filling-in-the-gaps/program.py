import os,shutil,re
path=input('Enter path of the folder: ')
prefix=input('Enter file prefix: ')
for folder,sub,file in os.walk(path):
    n=[]
    for f in file:
        r=re.compile(r'\d*')
        n.append(int(r.search(f).group(0)))
        