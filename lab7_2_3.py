import numpy as np

ar1 = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57,60]])

for i in range(len(ar1)):
    if (i % 2 == 0):
        print(ar1[i,:])

