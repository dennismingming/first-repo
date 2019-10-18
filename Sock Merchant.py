#!/usr/bin/env python
# coding: utf-8

# In[40]:


n = 9
ar = [10,20,20,10,10,30,50,10,20]


# In[41]:


import math
import os
import random
import re
import sys


# In[42]:


def sockMerchant(n, ar):
    num = n
    a = 0
    result = 0
    for j in range(n):
        num = len(ar)
        a +=1
        if a>=num:
            a=0
        for i in range(num):
            if a!=i and ar[a] == ar[i]:
                del ar[i]
                if i>a:
                    del ar[a]
                elif i<a:
                    del ar[a-1]
                result +=1
                break
                
            else:
                if a>=num:
                    a=0

    
    
    return result


# In[ ]:





# In[43]:


sockMerchant(n, ar)


# In[ ]:




