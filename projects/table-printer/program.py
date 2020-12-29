def printTable(l):
    m=[0]*len(l)
    for x in l:
        for y in x:
            if(len(y)>m[l.index(x)]):
                m[l.index(x)]=len(y)
    for c in range(len(l[0])):
        for r in range(len(l)):
            print(' '*(m[r]-len(l[r][c]))+l[r][c],end=' ')
        print()

printTable([['apples', 'oranges', 'cherries', 'banana'],              ['Alice', 'Bob', 'Carol', 'David'],              ['dogs', 'cats', 'moose', 'goose']])
        