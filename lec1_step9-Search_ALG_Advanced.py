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
# # @Time    : 2022-10-6 
# # @Author  : Hiroaki Wagatsuma
# # @Site    : https://github.com/hirowgit/2A_python_basic_course
# # @IDE     : Python 3.9
# # @File    : lec1_step9.py 


# In[ ]:


# Practice 3-2 (page 11/29)
# https://www.slideshare.net/tadahirotaniguchi0624/3-46861684


# In[4]:


TargetGraph={
    'S':['A','B'],
    'A':['S','B','C'],
    'B':['S','A','E' ,'F'],
    'C':['A','E','D'],
    'D':['C','E' ,'G'],
    'E':['B','C' ,'D' ,'G'],
    'F':['B'],
    'G':['D','E']
}


# In[5]:


N=7
Node=[chr(i) for i in range(65,65+N)]
Node=['S']+Node
print(Node)


# In[6]:


C=[[0, 2, 6, 0, 0, 0, 0, 0],
      [2, 0, 2, 1, 0, 0, 0, 0] ,
      [6, 2, 0, 0, 0, 5, 4, 0] ,
      [0, 1, 0, 0, 5, 2, 0, 0] ,
      [0, 0, 0, 5, 0, 1, 0, 1] ,
      [0, 0, 5, 2, 1, 0, 0, 5] ,
      [0, 0, 4, 0, 0, 0, 0, 0] ,
      [0, 0, 0, 0, 1, 5, 0, 0]
]


# In[15]:


OpenList=['S','A','E','F']
state='B'
key=Node.index(state)
Cost=C[key]
indexList=[Node.index(L)  for L in OpenList]
CList=[C[Node.index(state)][i] for i in indexList]
print(indexList)
print(CList)


# In[11]:


print(OpenList)
print(CList)
print(' ')
keys = ['node','cost']
# keys2 = ['node','cost','h']
d_all=[]
for i in range(len(OpenList)):
    values=[OpenList[i],CList[i]]
    d = {k: v for k, v in zip(keys, values)}
    d_all.append(d)
print(d_all)
d_all.sort(key=lambda x: x['cost'])
print(d_all)
print([d['node'] for d in d_all])


# In[16]:


# incompleted version of cost-first search (not summation)

OpenList=['S']
ClosedList=[]
while OpenList:
    state=OpenList[0]
    del OpenList[0]
    ClosedList=[state]+ClosedList
    ClosedList=list(set(ClosedList))
    print(['state',state])
    print(['OpenList(1)',OpenList])
    print(['ClosedList',ClosedList])
    if state=='G':
        break
    tmpSt=set(TargetGraph[state]) -set(ClosedList)
    activeNodes=list(tmpSt -set(OpenList))    
    OpenList.extend(activeNodes)
    
    # cost-first sorting 
    indexList=[Node.index(L)  for L in OpenList]
    CList=[C[Node.index(state)][i] for i in indexList]
    
    keys = ['node','cost']
    d_all=[]
    for i in range(len(OpenList)):
        values=[OpenList[i],CList[i]]
        d = {k: v for k, v in zip(keys, values)}
        d_all.append(d)
    d_all.sort(key=lambda x: x['cost'])
    OpenList=[d['node'] for d in d_all]
    # ---
    
    print(['OpenList(2)',OpenList])
    print('')
print('Completed') 


# In[23]:


CList=[]
len(CList)


# In[25]:


CList=[]
C2=[0]*len(C[0])
print(C2)
C2[1]=1
print(C2)


# In[28]:


C[Node.index(state)][i]+C[1][2]


# In[29]:


d_all


# In[33]:


CList=[0]*len(C[0])
CList


# In[47]:


print(indexList)
# [CList[i]+C[Node.index(state)][i] for i in indexList]
CList

Node.index(state)


# In[92]:


connN


# In[95]:


# completed version of cost-first search ( summation)

OpenList=['S']
ClosedList=[]
CList=[]
C2=[0]*len(C[0])
connN=['']*len(C[0])
Path=[]

while OpenList:
    state=OpenList[0]
    del OpenList[0]
    ClosedList=[state]+ClosedList
    ClosedList=list(set(ClosedList))
    print(['state',state])
    print(['OpenList(1)',OpenList])
    print(['ClosedList',ClosedList])
    if state=='G':
        Path.append(pre_state)
        Path.append('G')
        break
    tmpSt=set(TargetGraph[state]) -set(ClosedList)
    activeNodes=list(tmpSt -set(OpenList))    
    OpenList.extend(activeNodes)
    
    # cost-first sorting 
    indexList=[Node.index(L)  for L in OpenList]
    if len(CList)==0:
        CList=[C[Node.index(state)][i] for i in indexList]
    else:
        print(indexList)
        CList=[C2[Node.index(state)]+C[Node.index(state)][i] for i in indexList]
        
    keys = ['node','cost']
    d_all=[]
    flagU1=False
    flagU2=True
    for i in range(len(OpenList)):
        values=[OpenList[i],CList[i]]
        d = {k: v for k, v in zip(keys, values)}
        if (C[Node.index(state)][Node.index(values[0])]>0) and ( C2[Node.index(values[0])]>values[1] or C2[Node.index(values[0])]==0):
            # connected node                                                        and  (not larger than before                           or    blank )
            C2[Node.index(values[0])]=values[1]
            connN[Node.index(values[0])]=state
            flagU1=True
        if   C2[Node.index(values[0])]<values[1]:
            flagU2=False
        d_all.append(d)
    if flagU1 and flagU2:
        Path.append(state)
    d_all.sort(key=lambda x: x['cost'])
    OpenList=[d['node'] for d in d_all]
    print(OpenList)
    print(C2) 
    print(['Path',Path])
    # ---
    pre_state=state
    print(['OpenList(2)',OpenList])
    print('')

connN2=[connN,Node]
print('Completed') 
print(' ') 
print(C2) 
print(['Path',Path])
connN2


# In[13]:


CList


# In[20]:


H =[4,4,2,3,1,1,0,0]


# In[100]:


# completed version of best-first search

OpenList=['S']
ClosedList=[]
Path=[]

while OpenList:
    state=OpenList[0]
    del OpenList[0]
    ClosedList=[state]+ClosedList
    ClosedList=list(set(ClosedList))
    print(['state',state])
    print(['OpenList(1)',OpenList])
    print(['ClosedList',ClosedList])
    if state=='G':
        Path.append('G')
        break
    tmpSt=set(TargetGraph[state]) -set(ClosedList)
    activeNodes=list(tmpSt -set(OpenList))    
    OpenList.extend(activeNodes)
    
    # heuristic value sorting 
    indexList=[Node.index(L)  for L in OpenList]
    HList=[H[i] for i in indexList]
    
    keys = ['node','h']
    d_all=[]
    for i in range(len(OpenList)):
        values=[OpenList[i],HList[i]]
        d = {k: v for k, v in zip(keys, values)}
        d_all.append(d)
    d_all.sort(key=lambda x: x['h'])
    OpenList=[d['node'] for d in d_all]
    Path.append(state)
    # ---
    
    print(['OpenList(2)',OpenList])
    print('')
print('Completed') 
print(' ') 
print(['Path',Path])


# In[99]:


# completed version of A* search 

OpenList=['S']
ClosedList=[]
CList=[]
C2=[0]*len(C[0])
connN=['']*len(C[0])
Path=[]

while OpenList:
    state=OpenList[0]
    del OpenList[0]
    ClosedList=[state]+ClosedList
    ClosedList=list(set(ClosedList))
    print(['state',state])
    print(['OpenList(1)',OpenList])
    print(['ClosedList',ClosedList])
    if state=='G':
#         Path.append(pre_state)
        Path.append('G')
        break
    tmpSt=set(TargetGraph[state]) -set(ClosedList)
    activeNodes=list(tmpSt -set(OpenList))    
    OpenList.extend(activeNodes)

    # heuristic value sorting 
    indexList=[Node.index(L)  for L in OpenList]
    HList=[H[i] for i in indexList]
    
    # cost-first sorting 
    if len(CList)==0:
        CList=[C[Node.index(state)][i] for i in indexList]
    else:
        print(indexList)
        CList=[C2[Node.index(state)]+C[Node.index(state)][i] for i in indexList]
        
    keys = ['node','cost','h','f']
    d_all=[]
    flagU1=False
    flagU2=True
    for i in range(len(OpenList)):
        values=[OpenList[i],CList[i],HList[i],CList[i]+HList[i]]
        d = {k: v for k, v in zip(keys, values)}
        if (C[Node.index(state)][Node.index(values[0])]>0) and ( C2[Node.index(values[0])]>values[1] or C2[Node.index(values[0])]==0):
            # connected node                                                        and  (not larger than before                           or    blank )
            C2[Node.index(values[0])]=values[1]
            connN[Node.index(values[0])]=state
            flagU1=True
        if   C2[Node.index(values[0])]<values[1]:
            flagU2=False
        d_all.append(d)
    if flagU1 and flagU2:
        Path.append(state)
    d_all.sort(key=lambda x: x['f'])
    OpenList=[d['node'] for d in d_all]
    print(OpenList)
    print(C2) 
    print(['Path',Path])
    # ---
    pre_state=state
    print(['OpenList(2)',OpenList])
    print('')

connN2=[connN,Node]
print('Completed') 
print(' ') 
print(C2) 
print(['Path',Path])
connN2

