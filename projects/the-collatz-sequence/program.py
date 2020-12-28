import os,sys,math
def collatz(number):
    if not(number%2):
        a=number//2
    else:
        a=number*3+1
    print(a)
    return a
n=int(input("Enter an integer: "))
while n!=1:
    n=collatz(n)