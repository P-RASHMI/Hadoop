#!/usr/bin/env python
"""reducer.py"""
import sys
mat1 ={}
mat2 = {}

for line in sys.stdin:
    line = line.strip()
    key,value = line.split('\t')
    v = value.split(',')
    if key =='A':
        mat1[(int(v[1]),int(v[2]))] = int(v[3])
    elif key =='B':
        mat2[(int(v[1]),int(v[2]))] = int(v[3])
result = 0
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            result = result+mat1[(i,k)]*mat2[(k,j)]
        print('({0},{1})\t{2}'.format(i,j,result))
        result=0
