# primarility test of a number:
import time
start=time.time()
n=int(input('Enter a number:'))
if n==1:
    print('Your enter no',n,'is not a prime no')
for i in range(2,n//2):
    if (n%i)==0:
        print('not prime')
        break
else:
    print('prime')
end=time.time()
print('time:',end-start)