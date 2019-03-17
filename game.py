# Play game
import random
n=random.randint(1,101)
m=0
count=0
while m!='exit' and n!=m:
    m=int(input('Enter a number:'))
    if m=='exit':
        break   
    count+=1

    if n>m:
        print('Too low')
    elif n<m:
        print('Too high') 
    else:
        print('You got it')
        print('You got the number', n, 'after',count, 'iteration')