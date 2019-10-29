#!/usr/bin/env python
# coding: utf-8

# In[ ]:


A1 = []
A2 = ["HH"]
A3 = ['HT']
A4 = ['TH']
A5 = ['TT']
A6 = ['HH','HT']
A7 = ['HH','TH']
A8 = ["HH",'TT']
A9 = ["HT",'TH']
A10 = ['HT','TT']
A11 = ['TH','TT']
A12 = ['HH','HT','TH']
A13 = ['HH','HT','TT']
A14 = ['HH','TH','TT']
A15 = ['HT','TH','TT']
A16 = ['HH','HT','TH','TT']


# In[ ]:


B=[]
C=[]
for i in ["HH",' ']:
    for j in ['HT',' ']:
        for ii in ["TH",' ']:
            for jj in ['TT',' ']:
                B.append(i)
                B.append(j)
                B.append(ii)
                B.append(jj)


for i in range(16):                
    C.append(B[4*i:4*i+4:1])
    for _ in range(4):
        if  " " in C[i]:
            C[i].remove(' ')
    
    tuple(C[i])
C

