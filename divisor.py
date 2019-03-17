#Divisor
import time
start=time.time()
def divisor(no):
    for i in range(1,no):
        if no%i==0:           
            print(i,' ',end='') 
        else:
            pass
no=int(input('Enter number to find divisors:'))
divisor(no)
end=time.time()
print('\n Time takes:',end-start,'ns')