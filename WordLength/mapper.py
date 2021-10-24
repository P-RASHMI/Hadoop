#!/usr/bin/env python
import sys

for line in sys.stdin:
	# to remove whitespace
	line = line.strip()
	# split the line into words
	words = line.split()
	for word in words:
		print ('%s\t%s' % (word, len(word)))
