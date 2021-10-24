#!/usr/bin/env python
"""mapper.py"""
import sys

for line in sys.stdin:
    line = line.strip()
    entry = line.split(',')
    key = entry[0]
    value = line[1:]
    if key =='A':
        print('{0}\t{1}'.format(key,value))
    elif key =='B':
        print('{0}\t{1}'.format(key,value))
