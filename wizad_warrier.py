#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

#캐릭터 생성
warriors = []
wizades = []
ii = 0
jj = 0
for value in range(0, 100):
    for vlaue in range(1,5 + 1):
        warriors.append([random.choice(range(5,10 + 1)) ,50])

    for vlaue in range(1,4 + 1):
        wizades.append([random.choice(range(5,20 + 1)) ,30])

        i=len(warriors)
        j=len(wizades)    
    #print(warriors,wizades,1)

    while i != 0 and j != 0:
        i=len(warriors)
        j=len(wizades)

        #전사 마법사 죽었는지 확인  
        #if i != 0:
        for value in range(0, len(warriors)):
            if warriors[value][1]==0:
                i-=1

        #if j != 0:
        for value in range(0, len(wizades)):
            if wizades[value][1]==0:
                j-=1

        #승부 표현
        if i<=0:
            ii += 1
            #print("wizade Win!")
        elif j<=0:
            jj += 1
            #print("warrior Win!")


        #싸우기    
            # 선택
        select_warriors = random.randint(1,len(warriors))
        select_wizades = random.randint(1,len(wizades))
        #

        #대전
        candi_warriors = warriors[select_warriors-1]
        candi_wizades = wizades[select_wizades-1]    

        #지우기
        warriors.remove(candi_warriors)
        wizades.remove(candi_wizades)

        #print(warriors,wizades)

        while candi_warriors[1] > 0:
            candi_warriors[1] -= candi_wizades[0]

            if candi_warriors[1]<0:
                candi_warriors[1]=0 

        while candi_wizades[1] > 0:
            candi_wizades[1] -= candi_wizades[0]

            if candi_wizades[1]<0:
                candi_wizades[1]=0

        warriors.append(candi_warriors)
        wizades.append(candi_wizades)


    #print(candi_warriors,candi_wizades)
print("warriors:wizades = {}     : {} ".format(ii,jj))


# In[ ]:




