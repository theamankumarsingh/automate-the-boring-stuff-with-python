import re
def isStrong(st):
    robj=re.compile(r'\w{8}\w*')
    if robj.search(st)==None:
        return 0
    robj=re.compile(r'[A-Z]')
    if robj.search(st)==None:
        return 0
    robj=re.compile(r'[a-z]')
    if robj.search(st)==None:
        return 0
    robj=re.compile(r'[0-9]')
    if robj.search(st)==None:
        return 0
    return 1
    
password=input()
if isStrong(password):
    print("The password is strong.")
else:
    print("The password is weak.")
