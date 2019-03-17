# Find the character friquencies in a string 
# which is match character of another string

# This code is very important to fine anything from  given list or string 

s1=input('Enter the first string:')
s2=input('Enter the second string:')
l=[each for each in s1 if each in s2]
l=[x.strip(' ') for x in l]
print('\n',l)

import collections
counter=collections.Counter(l)
print('\n',counter.most_common(10))