#Find the odd no inbetween any particular no 
# and print the odd number including the number itselt if it is odd
n1=int(input('Enter first no:'))
n2=int(input('Enter last no:'))
l=[]
def oddno(n1,n2):
    for i in range(n1,n2+1):
        if i%2!=0:
            l.append(i)
    print(l)
oddno(n1,n2)
