#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Python basics for novice data scientists, supported by Wagatsuma Lab@Kyutech 
#
# The MIT License (MIT): Copyright (c) 2020 Hiroaki Wagatsuma and Wagatsuma Lab@Kyutech
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. */
#
# # @Time    : 2020-10-14 
# # @Author  : Hiroaki Wagatsuma
# # @Site    : https://github.com/hirowgit/2A_python_basic_course
# # @IDE     : Python 3.7.7 (default, Mar 10 2020, 15:43:27) [Clang 10.0.0 (clang-1000.11.45.5)] on darwin
# # @File    : lec1_step6.py 


# In[ ]:


# Practice 2-3 (page 24/28)
# https://www.slideshare.net/tadahirotaniguchi0624/2-46861654


# In[2]:


TargetGraph={
    'S':['A','B'],
    'A':['S','C','D'],
    'B':['S','C'],
    'C':['A','B','D'],
    'D':['A','C']
#    'G':'unknown now
}


# In[3]:


OpenList=['S']
ClosedList=[]
while OpenList:
    state=OpenList[0]  
    del OpenList[0]  
    ClosedList.extend(state)
    print(state)
    if state=='G':
        break
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
 #   OpenList.insert(-1, activeNodes)  # the first item
    OpenList.append(activeNodes)  # the last item
    OpenList=[item for i in OpenList for item in i if item not in ClosedList]
print('completed') 


# In[52]:


TargetGraph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F','G','H'],
    'D':['B','I'],
    'E':['B'],
    'F':['C'],
    'G':['C','J'],
    'H':['C'],
    'I':['D'],
    'J':['G']
#    'G':'unknown now
}


# In[49]:


OpenList=['A']
ClosedList=[]
k=1
while OpenList:
    state=OpenList[0]  
    del OpenList[0]  
    ClosedList.append(state)
    print(str(k)+": "+state)
    if state=='Goal':
        break
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
    OpenList.append(activeNodes)  # the last item
    OpenList=[item for i in OpenList for item in i if item not in ClosedList]
    k=k+1
print('completed') 


# In[ ]:




