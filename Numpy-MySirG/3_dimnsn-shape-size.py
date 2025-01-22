import numpy as np
a1 = np.array([ [1,2,3], [2,3,4], [5,6,7], [7,8,9]])
# print(type(a1))
# print(a1.size)      #size means : No of element
# print(a1.dtype)
# print(a1.ndim) # ndim - to find Number of dimension

a2 = np.array([[1,2,3],[2,3,4]], ndmin=3) #to set dimension , use {ndmin = 0} or {ndmin = 1} this is Minimum
print(a2.ndim)
print(a2)
print(a2.shape)