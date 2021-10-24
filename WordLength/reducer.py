#!/usr/bin/env python
import sys

current_word = None
word_len = 0
for line in sys.stdin:
    line = line.strip()
    word,length = line.split('\t')
    if current_word == word:
        word_len == length
    else:
        if current_word:
            print('%s\t%s' % (current_word, word_len))
        word_len = length
        current_word = word
if current_word == word:
    print('%s\t%s' % (current_word, word_len))
