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

fin=open("ex4.txt","r")
fout=open("result.txt","w")
str=fin.read()
#匹配正则表达式
reObj=re.compile("\b?([a-zA-Z]+)\b?")
words=reObj.findall(str)
#建立空字典
word_dict={}

#以单词的小写作为键值进行统计，同时要
if __name__ == '__main__':
    for word in words:
        if(word_dict.has_key(word)):
            word_dict[word.lower()]=max(word_dict[word.lower()],words.count(word.lower())+words.count(word.upper())+words.count(word))
        else:
            word_dict[word.lower()]=max(0,words.count(word.lower())+words.count(word.upper())+words.count(word))       
    for(word,number) in word_dict.items():
        fout.write(word+":%d\n"%number)
    


#%%

