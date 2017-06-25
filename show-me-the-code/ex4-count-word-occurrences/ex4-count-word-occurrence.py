# -*- coding: utf-8 -*-
"""
Generate some random numbers and store them to sqlite;
coupon format [3 digits + 10 alphabets]
each run wil store 2 more coupon as rows in a sqlite file named 'ex2.db'
tested under Spyder (Python 3.5)
@author: sqr
"""
#%%

import re

fin = open('ex4.txt', 'r')
str = fin.read()

reObj = re.compile('\b?(\w+)\b?')
words = reObj.findall(str)

wordDict = dict()

for word in words:
    if word.lower() in wordDict:
        wordDict[word.lower()] += 1
    else:
        wordDict[word] = 1

for key, value in wordDict.items():
    print('%s: %s' % (key, value))


#%%

