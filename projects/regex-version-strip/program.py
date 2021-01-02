import re
def strip(st,c='s'):
    robj=re.compile(r'^\{}*(.*?)\{}*$'.format(c,c))
    return robj.search(st).group(1)
s=input()
try:
    ch=input()[0]
    print(strip(s,c=ch))
except IndexError:
    print(strip(s))