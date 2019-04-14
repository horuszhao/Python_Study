import math
import os
import random
import re
import sys

def getOneBits(n):
    # Write your code here
    binStr = bin(n).replace('0b','')
    binArr = list(binStr)
    i=1
    r=[]
    for b in binArr:
        if b=='1':
            r.append(str(i))
        i+=1
    r.insert(0,str(len(r)))
    print('\n'.join(r))

getOneBits(9)
