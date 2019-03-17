print('It is a prime no check programe')

n=int(input('Enter a number here:'))
if n==1:
    print(n,'is not a prime no.')
elif n>1:
    for i in range(2,n//2):
        if (n%i)==0:
            print(n,'is not a prime number')
            break
    else:
        print(n,'is a prime number')
else:
    print('You enter a invalid no. to check primarity')