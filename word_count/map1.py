# import sys because we need to read and write data to STDIN and STDOUT
import sys
# to read line by line
for line in sys.stdin:
        line = line.strip()  #to remove spaces
        words = line.split() #to split based on spaces lines into words
        for word in words:   #these results will be input to reducer
                print('%s\t%s' %(word,1))
