
from math import exp
from math import e
import numpy as np
import decimal
import pandas as pd




pop = []
x = 0
for a in range(1,10001):
    pop.append((1.2)*e**(-1.2*x))
    x =+0.0001


for k in range(100,10100,100):
    exec(f'S{k} =pop[1:k]')


####################################################################################

import numpy as np

for size in np.arange(100,10100,100):	
    exec(f'S{size} = np.random.exponential(scale=1.2,size=size)')

len(S10000)

####################################################################################
import numpy as np
#another way to do it
#create a dictionary of samples
dict_samples = {} 
for size in np.arange(100,10100,100):	
    dict_samples[size]=np.random.exponential(scale=10/12,size=size)


dict_samples[100]
    
len(dict_samples[200])

1/1.2

pos = 100
for pos in np.arange(100,10100,100):
    sample = dict_samples[pos]
    sample_mean = sample.mean()
    print("The mean for sample {} is {}".format(pos,sample_mean))



    






























