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


# In[13]:


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


# In[25]:


# https://note.nkmk.me/python-dict-create/
keys = ['k1', 'k2', 'k3']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)


# In[ ]:


Node=[]
keys = ['cost', 'h', 'f']
values = [1, 2, 3]
for i in 
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


# In[2]:


Node=[chr(i) for i in range(65,65+10)]
print(Node)


# In[5]:


H=list(range(1,len(Node)))
print(H)
H=list(range(1,len(Node)))
print(H)
F=3*list(range(1,len(Node)))
print(F)


# In[6]:


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


# In[64]:


keys = ['node','cost', 'h', 'f']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)


# In[66]:


keys = ['node','cost', 'h', 'f']
values = [1, 2, 3]
d_all=[]
for i in range(0,len(Node)-1):
    values=[Node[i],Cost[i],H[i],F[i]]
    d = {k: v for k, v in zip(keys, values)}
    d_all.append(d)
print(d_all)


# In[70]:


pprint.pprint(sorted(d_all, key=lambda x: x['node']))


# In[71]:


pprint.pprint(sorted(d_all, key=lambda x: x['cost']))


# In[72]:


pprint.pprint(sorted(d_all, key=lambda x: x['h']))


# In[73]:


pprint.pprint(sorted(d_all, key=lambda x: x['f']))


# In[ ]:




