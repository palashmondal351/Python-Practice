#!/usr/bin/env python3
# -*- coding: utf-8
# PASSWORD Generator 
n='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQURSTUVWXYZ0123456789!@#$%&*'
import random
passW=input('Which type of password do you want? Sort Medium Strong:')
if passW=='Sort':
    passW=5
elif passW=='Medium':
    passW=7
elif passW=='Strong':
    passW=13
else:
    print('!!Invalid input ')
    
if passW in [5,7,13]:
    
    def password(passW):
        p=1
        print('\nYour recommanded password is:')
        while p<passW:   
            k=random.choice(n)
            L=''.join(k)
            p+=1
            print(L,end='')
    password(passW)

