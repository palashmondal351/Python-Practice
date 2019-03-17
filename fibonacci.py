# Fibonacci number
k=int(input('Enter the no.:'))
n0=0
n1=1
count=0
if k==0 or k<0:
    print('Your enter no. is',k,'Which is worng!!')
else:
    print('\n', k,'Fibonacci series is:')
    while count<k:
        print(n0,end=' ')
        nk=n0+n1
        n0=n1
        n1=nk
        count+=1