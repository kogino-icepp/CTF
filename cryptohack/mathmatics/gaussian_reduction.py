import numpy as np
import math
v = np.array([846835985, 9834798552])
u = np.array([87502093, 123094980])

def gaus_reduc(v1,v2):
    for i in range(10000):
        if np.dot(v1,v1) > np.dot(v2,v2):
            v1,v2 = v2,v1
        m = math.floor(np.dot(v1,v2)/np.dot(v1,v1))
        print(m)
        if m == 0:
            return np.dot(v1,v2)
        v2 = v2 - m*v1

print(gaus_reduc(v,u))