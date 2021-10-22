import sys

word_name = None
count_taken = 0
for line in sys.stdin:
    line = line.strip()
    word,count = line.split('\t') #splits with tab provided in mapper 
    count = int(count)   #typecasting  into int
    if word_name == word:
        count_taken += count
    else:
        if word_name:
            print('%s\t%s' %(word_name,count_taken)) #results into stdout 
        count_taken = count
        word_name = word
if word_name == word:
        print('%s\t%s' %(word_name,count_taken))
