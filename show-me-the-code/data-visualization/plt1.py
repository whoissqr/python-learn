# -*- coding: utf-8 -*-
"""
Generate some random numbers and plot them;
tested under Spyder (Python 3.5)
@author: sqr
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
 

# evenly sampled time at 200ms intervals
t = np.arange(0, 10, 1)

plt.xlabel('x')
plt.xlabel('y')

plt.plot(t, t, 'r-.')
plt.plot(t, np.sin(t)*4, 'b--')
plt.plot(t, np.cos(t)*4, 'g-')
plt.show()

#%%
