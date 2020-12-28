import os,sys,math
def collatz(number):
    if not(number%2):
        a=number//2
    else:
        a=number*3+1
    print(a)
    return a
k=1
while k:
    try:    
        n=int(input("Enter an integer: "))
        k=0
    except ValueError:
        print('Wrong input!')
while n!=1:
    n=collatz(n)