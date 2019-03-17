# finding the value of lcm of two numbers
n1=int(input('Enter the first value:'))
n2=int(input('Enter the second value:'))
def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
        
    while(True):
        if ((greater%x==0) and (greater%y==0)):
            lcm=greater
            break
        greater+=1
    return lcm
print('The LCM of',n1,'and',n2,'is', lcm(n1,n2))
lcm(n1,n2)

