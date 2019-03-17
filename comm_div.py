# Common divisor of two numbers 
import os
n1=int(input('Enter the first no.:'))
# Alt+UP/DOWN arrow to up or down and line will be secected just copy it.
n2=int(input('Enter the second no.:'))
print('\nYour enterd first no. is:',n1,'and second no is:',n2)


def divisorf(m):
    l1=[1]
    for i in range(2,n1+1):
        
        if n1%i==0:
            l1.append(i)
            
    print(n1,'divisor is',l1)
    
divisorf(n1)


def divisors(m):
    l2=[1]
    for j in range(2,n2+1):
        
        if n2%j==0:
            l2.append(j)
    print(n2,'divisor is',l2)    
divisors(n2)

#def common(l1,l2):
#    l=[each for each in l1 if each in l2]
#    print(l)
#common(l1,l2)