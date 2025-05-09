import numpy as np
# Numpy Was used to capture the image of blackhole with it's calculation power
# Gravitation waves : numpy was used for it's calcualtion
# For cricket analytics : we use numpy calcualtion
# Even matplotlib and various others library, use numpy for it's fast calculation
# well optimized c code, flexibility of python with speed of compiled code
# Array can hold homogenous set of collection only ([1,2],[2,3],[3,4,5]) error will occur bcoz 3 digit in last set
# i = integer, b=bool, u=unsigned int, f=float, c=complex float,o=object, s=string, M=date time, m= time delta

a3 = np.array(34) # ZERO dimgension array
a2 = np.array((23,43,53,33)) #pass tuple as array       1-DIMENSIONAL ARRAY
a4 = np.array([[10,20],[50,30]]) #pass list as array
a1 = np.array([[10,20,30],[50,30,10],[47,57,67]])
# print(a1)
# print(a2)
a5 = np.array([23,4.5,6])   #converting all values to Float automatically
# print(a5)
# print(a5.dtype)     # check datatype of array

a6 = np.array([1,23,4,5,6], dtype='float32') #we can set dataType exam : 'int32' , 'float32', 'int4' [no. denote byte]
# print(a6.dtype)

a7 = np.array([100,200,'300'])
print(a7.dtype)     # type is U21
a7 = np.array([100,200,300], dtype='S') #string type denoted as 'S'
print(a7.dtype)     # type is S3