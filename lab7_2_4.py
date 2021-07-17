import numpy as np

ar1 = np.array([[34,43,73],[82,22,12],[53,94,66]])

print(ar1)

print("\n=======================================================")
print("\n The amax of axis 0 : \n",np.amax(ar1,axis=0))
print("\n=======================================================")
print("\n The amin of axis 1 : \n",np.amin(ar1,axis=1))