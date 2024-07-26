import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import string 
import random 

a = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + " " + "\n"
a = list(a)




c = []
for i in range(99999999):  
    random.shuffle(a) 
   
    c.append(a)
print(len(c))