# -*- coding: utf-8 -*-
"""
Generate some random numbers and store them to sqlite;
tested under Spyder (Python 3.5)
@author: sqr
"""
#%%
import random
import string
import sqlite3

words = string.ascii_letters + string.digits
coupons = []

def  get_coupon(digit):
    conpon = ''
    for i in range(digit):
        conpon += random.choice(words)
    return conpon

def two_hundred_coupons():
#    conpons = set()
    digit = 10
    for i in range(2):
        #prepend the coupon with a number to ensure it is unique
        data = '%03d' % i                    
        data += get_coupon(digit)
        coupons.append(data)
    return coupons

def save2DB():
    conn = sqlite3.connect('ex2.db')
    conn.execute('''create table if not exists coupons (coupon_num text)''')
    for coupon in coupons:
        conn.execute("INSERT INTO coupons VALUES (?)", (coupon,))
    conn.commit()
    conn.close()
    
def readFromDB():
    conn = sqlite3.connect('ex2.db')
    for row in conn.execute('SELECT * FROM coupons'):
        print(row)
    
two_hundred_coupons()
save2DB()
readFromDB()
#%%

