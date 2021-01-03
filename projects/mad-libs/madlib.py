import re
file=open('input.txt','r')
file=open('output.txt','w')

st=file.read()
r=re.compile(r'ADJECTIVE|VERB|ADVERB|NOUN')


for f in r.findall(st):
    s=input('Enter substitute for '+f.lower()+':')
    