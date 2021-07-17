import numpy as np
import random

a = np.random.randn(4,2)
a = np.uint16(a)

print(a)
print("\n Shape of Array = ",np.shape(a))
print("\n Dimension of Array =  ",a.ndim)
print("\n Length in bytes of one array item: "+str(a.itemsize))
