#!/usr/bin/python
import math

x = int(input("enter range:"))
y = x+1

for i in range(1,y):
  f=0 
  for j in range(2,i):
      if i%j != 0 :
         continue
      elif i%j == 0 :
         f = 1
         break
  if f == 0 :
      print i
