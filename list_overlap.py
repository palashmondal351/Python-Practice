# list overlap to find the common element
import random
n1=random.sample(range(1,20),6)
n2=random.sample(range(1,25),8)
l=[each for each in n1 if each in n2]
print('\n First list is:',n1)
print('\n Second list is:',n2)
print('\nCommonelement in the list is:',l)
