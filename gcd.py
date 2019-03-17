#GCD of two numbers
n1=int(input('Enter first no.:'))
n2=int(input('Enter second no.:'))
def gcd(n1,n2):
    if(n1==0):
        return n2
    if (n2==0):
        return n1
    if(n1==n2):
        return n1
    if(n1>n2):
        return gcd(n1-n2,n2)
    return gcd(n1,n2-n1)
if(gcd(n1,n2)):
    print('gcd of',n1,'and',n2,'is',gcd(n1,n2))
else:
    print('The given no.',n1,'and',n2,'gcd is not found')
