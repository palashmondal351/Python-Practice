# List comprehension to find even no from a list
import time
start=time.time()
l=[7,8,9,2,5,4,3,0,6]
ll=[each for each in l if each%2==0]
print('original List', l)
print('even List', ll)
end=time.time()
print('\nTime Taken:',end-start)