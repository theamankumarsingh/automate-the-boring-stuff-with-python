def toString(l):
    s=''
    for i in range(len(l)):
        if(i==len(l)-1):
            s+='and '+str(l[i])
        else:
            s+=str(l[i])+', '
    return s