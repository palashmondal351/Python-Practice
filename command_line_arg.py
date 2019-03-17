#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  run this code go to this file path and type -
# python <filename.py> give 2 integer with space
import sys
print('No of agrument',len(sys.argv))
print('argument list:',str(sys.argv))
x=int(sys.argv[1])
y=int(sys.argv[2])
z=x+y
print("x=",x,'y=',y,'z=',z)