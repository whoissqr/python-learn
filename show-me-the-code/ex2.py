# -*- coding: utf-8 -*-
"""
第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
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
        data = '%03d' % i                    ##数字编码放在最前面，保证验证码唯一性
        data += get_coupon(digit)
        coupons.append(data)
    return coupons

def save2DB():
    #TODO: check if table already exist
    conn = sqlite3.connect('ex2.db')
    conn.execute('''CREATE TABLE coupons (coupon_num text)''')
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

