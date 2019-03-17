#!/usr/bin/env python3
# -*- coding: utf-8
## FIBONACCI
n=int(input('Enter the number of fibonacci series:'))
def fibo(n):
    s,a,b=0,0,1
    while s<n:
        print(a,end=' ')
        new_ab=a+b
        a=b
        b=new_ab
        s+=1
fibo(n)
    
        
        
    