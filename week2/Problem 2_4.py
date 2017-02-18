"""
"""
#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    lis=[]
    random.seed(70)
    for i in range(10):
        
        n=random.random()*5+30
        lis.append(n)
    print(lis)



#%%

