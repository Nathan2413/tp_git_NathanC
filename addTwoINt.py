#!/bin/python3
import sys

def add(x,y):
	return(x+y)
nbr_arg=len(sys.argv)-1
if (nbr_arg < 2):
    print("Error")

x = int(sys.argv[1])
y = int(sys.argv[2])
print(add(x,y))	
