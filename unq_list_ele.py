#!/usr/bin/env python3
# -*- coding: utf-8 
## UNIQUE LIST ELEMENT
l=[k for k in input('Enter element with space:').split( )]
ll=set(l)
lll=list(ll)
print(lll)

#using function
L=[]
def dup_list(l):
    for e in l:
        if e not in L:
            L.append(e)
    print(L)
dup_list(l)