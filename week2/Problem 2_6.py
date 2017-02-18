"""
"""
#%%
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """

    random.seed(82) 
    for i in range(100):
        print(random.randint(1,6) + random.randint(1,6))

   
#%%


