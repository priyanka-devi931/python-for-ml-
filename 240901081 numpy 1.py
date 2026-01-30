#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.array([[1, 2, 4], [5, 8, 7]])
print ("Array created using passed list:\n", a)


# In[3]:


import numpy as np
b= np.zeros((3,4))
print("\n an array initialised with all zeros:\n",b)


# In[4]:


c = np.full((3, 3), 6)
print ("\nAn array initialized with all 6s.\n", c)


# In[5]:


d = np.random.random((2, 2))
print ("\nA random array:\n", d)


# In[6]:


e = np.arange(0, 30, 5)
print ("\n A sequential array with steps of 5:\n", e)


# In[8]:


#Reshaping 3X4 array to 2X2X3 array
arr = np.array([[1, 2, 3, 4], [5, 2, 4, 2],[1, 2, 0, 1]])
newarr = arr.reshape(4, 3)
print ("\nOriginal array:\n", arr)
print ("Reshaped array[4,3]:\n", newarr)


# In[9]:


#Flatten array
flarr= arr.flatten()
print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)


# In[10]:


# Printing array dimensions (axes)
print("\nNo. of dimensions: ", arr.ndim)


# In[13]:


# Printing shape of array
print("\nShape of array: ", arr.shape)
# Printing size (total number of elements) of array
print("\nSize of array: ", arr.size)
# Printing type of elements in array
print("\nArray stores elements of type: ", arr.dtype)
#converting datatypes from integer to float
newtype=arr.astype('f')
print("\nConverted array elemnets:\n",newtype)
print("Converted array type:",newtype)


# In[ ]:




