#!/usr/bin/python
import math

x = int(input("enter range:"))
y=x+1
m=0
n=1
print m
print n

for i in range(2,y):
    v=m+n
    print v
    m=n
    n=v
 
