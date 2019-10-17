#!/usr/bin/env python
# coding: utf-8

# In[4]:


# map, filter, reduce
#- 아래의 코드들이 모두 동작되도록 `# TODO`가 있는 셀에 함수를 작성하세요.
# Quiz 1
# - map 함수를 map_func 함수의 이름으로 구현하세요.
# - 리스트의 데이터를 아래의 예제와 같이 더하는 함수를 만드는데 따로 함수를 선언해서 사용하지 말고 map의 첫번째 파라미터에 lambda 함수로 구현하세요.

# ```
# ls1 = [1,2,3,4]
# ls2 = [5,6,7]
# ls3 = [9,10,11,12]

# result = [15, 18, 21]
# ```

ls1 = [1,2,3,4]
ls2 = [5,6,7]
ls3 = [9,10,11,12]

# map 함수 사용
list(map(lambda *args : sum(args), ls1, ls2, ls3))

ls1 = [1,2,3,4]
ls2 = [5,6,7]
ls3 = [9,10,11,12]

# TODO
# map_func 이름으로 map 함수를 구현하세요.
def map_func(func, *lis):
    temp = list(zip(*lis))
    #print("zip=",list(temp))
    result = []
    for i in range(len(lis)):
        #print(i,"th loop")
        temp[i] = list(temp[i])
        #print(temp)
        result.append(func(*temp[i]))
        #print("result = ",result)
    return result

# map_func 함수 사용
print(map_func(lambda *args : sum(args), ls1, ls2, ls3))

### Quiz 2
# - filter 함수를 구현하여 1~10까지 숫자에서 홀수만 출력하는 코드를 작성하세요
# ```
# ls = range(1, 11)
# result = [1, 3, 5, 7, 9]
# ```
ls = range(1, 11)
# filter 함수 사용
list(filter(lambda number: number % 2, ls))
# TODO
# filter_func 이름으로 filter 함수를 구현하세요.
def filter_func(func, lis):
    temp=[]
    result=[]
    for i in range(0,len(lis)):
        #print(i)
        #print(True if func(lis[i]) == 0 else False)
        temp.append(True if func(lis[i]) == 0 else False)
        #print(temp)
        #print("j= ",i)
        if temp[i] == False:
            result.append(lis[i])
    return result

# filter_func 함수 사용
print(filter_func(lambda number: number % 2, ls))
        
    
#     Quiz
# reduce 함수를 구현
# ls = [1, 2, 3, 4, 5]
# def reduce_func():
#     #TODO

# reduce_func(lambda num1, num2: num1 + num2, ls)
# result => 15
# 힌트
# ls = [1, 2, 3]
# del ls[0]
# ls => [2, 3]

from functools import reduce
ls = [1, 2, 3, 4, 5]
# reduce 함수 사용
reduce(lambda num1, num2: num1 + num2, ls)

# TODO
# reduce_func 이름으로 reduce 함수를 구현하세요.
def reduce_func(func, lis):
    for i in range(len(lis)-1):
        #print(i)
        #list(lis)
        #print(lis)
        lis[0] = func(lis[0],lis[1])
        del lis[1]
        #print(lis)
    return lis

# reduce_func 함수 사용
print(reduce_func(lambda num1, num2: num1 + num2, ls))


# In[ ]:




