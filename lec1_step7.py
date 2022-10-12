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
# # @File    : lec1_step7.py 


# In[ ]:


# Practice 3-1 (page 13/29)
# https://www.slideshare.net/tadahirotaniguchi0624/3-46861684


# In[ ]:


# https://note.nkmk.me/python-dict-list-sort/


# In[7]:


import pprint

l = [{'Name': 'Australia', 'Population': 25680158, 'Capital City': 'Canberra','Points': [-35.28, 149.13]}, 
     {'Name': 'Bangladesh', 'Population': 169468990,'Capital City': 'Dhaka', 'Points': [23.71, 90.41]},
     {'Name': 'Chile', 'Population': 17373831,'Capital City': 'Santiago', 'Points': [-27.37, -70.33]}]


# In[19]:


pprint.pprint(sorted(l, key=lambda x: x['Name']))


# In[20]:


pprint.pprint(sorted(l, key=lambda x: x['Population']))


# In[21]:


pprint.pprint(sorted(l, key=lambda x: x['Population'], reverse=True))


# In[8]:


# https://note.nkmk.me/python-dict-create/
keys = ['k1', 'k2', 'k3']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)


# In[10]:


Node=[]
keys = ['cost', 'h', 'f']
values = [1, 2, 3]
for i in range(len(keys)):
    d = {k: v for k, v in zip(keys, values)}
    print(d)


# In[28]:


# A: ascii code 65
chr(65)


# In[32]:


# for i in range(1,10,1):
for i in range(1,10):
    s=chr(i+65-1)
    print(s)


# In[30]:


# for i in range(1,10,1):
for i in range(65,65+10):
    s=chr(i)
    print(s)


# In[12]:


Node=[chr(i) for i in range(65,65+10)]
print(Node)


# In[83]:


H=list(range(len(Node)))
print(H)
H=list(range(len(Node)))
print(H)
F=3*list(range(len(Node)))
print(F)


# In[85]:


Cost =H
print(Cost)
H=list(map(lambda x: x * 2, Cost))
print(H)
F=list(map(lambda x: x * 3, Cost))
print(F)


# In[56]:


data1 = [1, 3, 6, 50, 5]
data2 = list(map(lambda x: x * 2, data1))
print(data1)
print(data2)


# In[17]:


keys = ['node','cost', 'h', 'f']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)


# In[86]:


keys = ['node','cost', 'h', 'f']
d_all=[]
for i in range(len(Node)):
    values=[Node[i],Cost[i],H[i],F[i]]
    d = {k: v for k, v in zip(keys, values)}
    d_all.append(d)
print(d_all)


# In[75]:


Node


# In[19]:


pprint.pprint(sorted(d_all, key=lambda x: x['node']))


# In[71]:


pprint.pprint(sorted(d_all, key=lambda x: x['cost']))


# In[72]:


pprint.pprint(sorted(d_all, key=lambda x: x['h']))


# In[73]:


pprint.pprint(sorted(d_all, key=lambda x: x['f']))


# In[24]:


list_0 = [
        [9, 8, 5],
        [0, 8, 3],
        [1, 6, 5],
        [9, 0, 0],
        [4, 9, 3],
        [1, 4, 8],
        [4, 0, 6],
        [0, 3, 5],
        [1, 3, 1],
        [5, 2, 7],
    ]
print(list_0[2])
list_0.sort(key=lambda x: x[:][0])
print(list_0)


# In[31]:


list_0 = [
        [9, 8, 5],
        [0, 8, 3],
        [1, 6, 5],
        [9, 0, 0],
        [4, 9, 3],
        [1, 4, 8],
        [4, 0, 6],
        [0, 3, 5],
        [1, 3, 1],
        [5, 2, 7],
    ]
print(list_0[2])
list_0.sort(key=lambda x: x[0])
print(list_0)


# In[47]:


list_0 = [
        [1, 3, 2],
        [2, 2, 1],
        [3, 1, 3]
    ]
stag=1
print(list_0[:][stag])
list_0.sort(key=lambda x: x[stag])
print(list_0)


# In[67]:


list_0 = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
stag=1
print(list_0[:][0])
print(list_0[0][:])
print(list_0[0])
print(' ')

list_0.sort(key=lambda x: x[stag])
print(list_0)


# In[62]:


[list_0[i][0] for i in range(len(list_0))]


# In[71]:


list_0 = [
        [9, 8, 5],
        [0, 8, 3]
    ]
print(list_0[1])
list_0.sort(key=lambda x: x[2])
print(list_0)

