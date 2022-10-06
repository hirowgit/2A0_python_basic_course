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
# # @File    : lec1_step8.py 


# In[ ]:


# Practice 3-1 (page 13/29)
# https://www.slideshare.net/tadahirotaniguchi0624/3-46861684


# In[1]:


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


# In[39]:


state=[]
OpenList=['S']
ClosedList=[]
while OpenList:
    print(state)
    #print(OpenList)
    state=OpenList[0]  
    del OpenList[0]  
    ClosedList.append(state)
    if state=='G':
        break
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
    OpenList.insert(0, activeNodes)  # the first item
    #s1 = ','.join(OpenList); 
    print('OpenList(1): ',OpenList)
    #pprint.pprint(OpenList)
    OpenList=[item for i in OpenList for item in i if item not in ClosedList]
    print('OpenList(2): ',OpenList)
    print('ClosedList: ',ClosedList)    
print('completed') 


# In[75]:


H = {'S': 0,'A': 5, 'B': 8, 'C': 1, 'D': 2, 'E': 6}
sorted(H)


# In[76]:


sorted(H.keys())


# In[42]:


sorted(H.values())


# In[44]:


sorted(H.items(), key = lambda x:x[0])


# In[74]:


sorted(H.items(), key = lambda x:x[1])


# In[77]:


H2=sorted(H.items(), key = lambda x:x[1])
print(H2)


# In[78]:


sorted(H2, key = lambda x:x[1])


# In[79]:


sorted(H2, key = lambda x:x[0])


# In[80]:


[i[0] for i in H2 ]


# In[69]:


[i[1] for i in H2 ]


# In[81]:


hh1=[i[0] for i in H2 ]
hh2=[i[1] for i in H2 ]


# In[87]:


[(hh1[i],hh2[i]) for i in range(len(hh1)) ]


# In[86]:


[(hh1[i],hh2[i]) for i in range(len(hh1)) ]


# In[5]:


['S','A','B','C','D','E','F','G']


# In[3]:


C=[[0, 2, 6, 0, 0, 0, 0, 0],
      [2, 0, 2, 1, 0, 0, 0, 0] ,
      [6, 2, 0, 0, 0, 5, 4, 0] ,
      [0, 1, 0, 0, 5, 2, 0, 0] ,
      [0, 0, 0, 5, 0, 1, 0, 1] ,
      [0, 0, 5, 2, 1, 0, 0, 5] ,
      [0, 0, 4, 0, 0, 0, 0, 0] ,
      [0, 0, 0, 0, 1, 5, 0, 0]
]


# In[91]:


print(C)


# In[92]:


pprint.pprint(C)


# In[53]:


N=7
Node=[chr(i) for i in range(65,65+N)]
Node=['S']+Node
print(Node)


# In[11]:


OpenList=['B','D']
# Node.index('B')
indexList=[Node.index(L)  for L in OpenList]
indexList


# In[37]:


Node.index(state)


# In[39]:


key=Node.index(state)
Cost=C[key]
Cost


# In[70]:


OpenList=['S','A','E','F']
state='B'
key=Node.index(state)
Cost=C[key]
print(Cost)
print(' ')
indexList=[Node.index(L)  for L in OpenList]
print(indexList)
CList=[C[Node.index(state)][i] for i in indexList]
# a[[0,1]]
print(C[Node.index(state)])
print(CList)
print(sorted(CList))


# In[71]:


LL=[7,6,5,4,3,2,1]
LL.sort(key=lambda x: x)
print(LL)

LL=[7,6,5,4,3,2,1]
LL.sort()
print(LL)


# In[72]:


LL=[7,6,5,4,3,2,1]
aa=['a','b','c','d','e','f','g']
aa.sort(key=LL)
aa


# In[73]:


keys = ['node','cost']
d_all=[]
for i in range(len(Node)):
    values=[Node[i],Cost[i]]
    d = {k: v for k, v in zip(keys, values)}
    d_all.append(d)
print(d_all)
d_all.sort(key=lambda x: x['cost'])
d_all


# In[75]:


keys = ['node','cost']
d_all=[]
for i in range(len(Node)):
    values=[Node[i],Cost[i]]
    d = {k: v for k, v in zip(keys, values)}
    d_all.append(d)
print(d_all)
d_all.sort(key=lambda x: x['cost'], reverse=True)
d_all


# In[77]:


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


# In[122]:


mergedList[0]
[mergedList[j][0] for j in range(len(mergedList))]
print(mergedList)
print(len(mergedList[0]))


# In[125]:


OpenList=['S','A','E','F']
state='B'
key=Node.index(state)
Cost=C[key]
indexList=[Node.index(L)  for L in OpenList]
# print(Node[[0,1]])
CList=[C[Node.index(state)][i] for i in indexList]
mergedList=[OpenList,indexList,CList]
print(mergedList)

mergedList2=[]
for i in range(len(mergedList[0])):
    mergedList2.append([mergedList[j][i] for j in range(len(mergedList))])
    
    print([i])
    print(mergedList2)


print(mergedList2)
print(' ')

mergedList2.sort(key=lambda x: x[2])
print(mergedList2)
[mergedList2[i][0] for i in range(len(mergedList2))]


# In[102]:


import numpy as np

OpenList=['S','A','E','F']
state='B'
key=Node.index(state)
Cost=C[key]
indexList=[Node.index(L)  for L in OpenList]
# print(Node[[0,1]])
CList=[C[Node.index(state)][i] for i in indexList]
mergedList=[OpenList,indexList,CList]
print(mergedList)

mergedList_np=np.array(mergedList)
print(mergedList_np)
# np.transpose(mergedList_np)
print(mergedList_np.T)
print(' ')
mergedList2=(mergedList_np.T).tolist()
print(mergedList2[0])
print(' ')
mergedList2.sort(key=lambda x: x[2])
print(mergedList2)
[mergedList2[i][0] for i in range(len(mergedList2))]


# In[ ]:





# In[ ]:


# =============================


# In[113]:


[('S','A')]


# In[120]:


g=('S', 'A')
print(g[0])
print(g[1])


# In[118]:


C[1][2]


# In[121]:


g=('S', 'A')
i=[s for s in range(len(Node)) if g[0] in Node[s]][0]
j=[s for s in range(len(Node)) if g[1] in Node[s]][0]
C[i][j]


# In[7]:


def eachCost(Pair,Node,C):
    i=[s for s in range(len(Node)) if Pair[0] in Node[s]][0]
    j=[s for s in range(len(Node)) if Pair[1] in Node[s]][0]
    return C[i][j]

C=[[0, 2, 6, 0, 0, 0, 0, 0],
      [2, 0, 2, 1, 0, 0, 0, 0] ,
      [6, 2, 0, 0, 0, 5, 4, 0] ,
      [0, 1, 0, 0, 5, 2, 0, 0] ,
      [0, 0, 0, 5, 0, 1, 0, 1] ,
      [0, 0, 5, 2, 1, 0, 0, 5] ,
      [0, 0, 4, 0, 0, 0, 0, 0] ,
      [0, 0, 0, 0, 1, 5, 0, 0]
]
N=7
Node=[chr(i) for i in range(65,65+N)]
Node=['S']+Node
print(Node)
g=('S', 'A')
eachCost(g,Node,C)



# In[10]:


# New with the cost calculation
CostList=[]
state=[]
OpenList=['S']
ClosedList=[]
while OpenList: 
    #print(OpenList)
    state=OpenList[0]  
    print(state)
    del OpenList[0]  
    ClosedList.append(state)
    if state=='G':
        break
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
    costM=[(s,state) for s in activeNodes]
    print(costM)
    print(costM[0])
    costMat=[eachCost(costM[i],Node,C) for i in range(len(costM))]
    print(costMat)
    OpenList.insert(0, activeNodes)  # the first item
    CostList.insert(0, costMat)  # the first item
    print('OpenList(1): ',OpenList)
    #OpenList=[item for i in OpenList for item in i if i not in ClosedList]
    OpenList=[item for i in OpenList for item in i]
    key=[k for k in range(len(OpenList)) if OpenList[k] not in ClosedList]
    print('key: ',key)
    print('OpenList(2): ',OpenList)
    print('ClosedList: ',ClosedList)    
print('completed') 


# In[ ]:


# 2022/10/05
# New with the cost calculation
CostList=[]
state=[]
OpenList=['S']
ClosedList=[]
while OpenList: 
    #print(OpenList)
    state=OpenList[0]  
    print(state)
    del OpenList[0]  
    ClosedList.append(state)
    if state=='G':
        break
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
    costM=[(s,state) for s in activeNodes]
    print(costM)
    print(costM[0])
    costMat=[eachCost(costM[i],Node,C) for i in range(len(costM))]
    print(costMat)
    OpenList.insert(0, activeNodes)  # the first item
    CostList.insert(0, costMat)  # the first item
    print('OpenList(1): ',OpenList)
    #OpenList=[item for i in OpenList for item in i if i not in ClosedList]
    OpenList=[item for i in OpenList for item in i]
    key=[k for k in range(len(OpenList)) if OpenList[k] not in ClosedList]
    print('key: ',key)
    print('OpenList(2): ',OpenList)
    print('ClosedList: ',ClosedList)    
print('completed') 


# In[2]:


OpenList=['S']
ClosedList=[]
while OpenList:
    state=OpenList[0]
    del OpenList[0]
    ClosedList=ClosedList+[state]
    ClosedList=list(set(ClosedList))
    print(['state',state])
    print(['OpenList(1)',OpenList])
    print(['ClosedList',ClosedList])
    if state=='G':
        break
    tmpSt=set(TargetGraph[state]) -set(ClosedList)
    activeNodes=list(tmpSt -set(OpenList))    
    OpenList=OpenList+activeNodes
  #  OpenList=list(set(OpenList))
    print(['OpenList(2)',OpenList])
    print('')
print('Completed') 


# In[ ]:





# In[208]:


# New with the cost calculation
CostList=[]
state=[]
OpenList=['S']
ClosedList=[]
while OpenList: 
    #print(OpenList)
    state=OpenList[0]  
    print(state)
    del OpenList[0]  
    ClosedList.append(state)
    if state=='G':
        break
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
    costM=[(s,state) for s in activeNodes]
    print(costM)
    print(costM[0])
    costMat=[eachCost(costM[i],Node,C) for i in range(len(costM))]
    print(costMat)
    OpenList.insert(0, activeNodes)  # the first item
    CostList=costMat+CostList  # the first item
    print('OpenList(1): ',OpenList)
    print('CostList(1): ',CostList)
    #OpenList=[item for i in OpenList for item in i if i not in ClosedList]
    OpenList=[item for i in OpenList for item in i]
    #CostList=[item for i in CostList for item in i]
    key=[k for k in range(len(OpenList)) if OpenList[k] not in ClosedList]
    OpenList=[OpenList[i] for i in key] 
    #CostList=[CostList[i] for i in key] 
    print('key: ',key)
    print('OpenList(2): ',OpenList)
    print('CostList(2): ',CostList)
    print('ClosedList: ',ClosedList)    
print('completed') 


# In[252]:


# New version with sort
CostList=[]
state=[]
stateC=[]
OpenList=['S']
CostList=[0]
ClosedList=[]
while OpenList: 
    #print(OpenList)
    state=OpenList[0]  
    stateC=CostList[0]
    print(state)
    del OpenList[0]  
    del CostList[0]  
    ClosedList.append(state)
    if state=='G':
        break
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
    costM=[(s,state) for s in activeNodes]
    costMat=[eachCost(costM[i],Node,C) for i in range(len(costM))]
    OpenList=activeNodes+OpenList  # the first item
    CostList=list(map(lambda x: x + stateC, costMat))+CostList  # the first item
    print('OpenList(1): ',OpenList)
    print('CostList(1): ',CostList)
    key=[k for k in range(len(OpenList)) if OpenList[k] not in ClosedList]
    OpenList=[OpenList[i] for i in key] 
    CostList=[CostList[i] for i in key] 
    print('OpenList(2): ',OpenList)
    print('CostList(2): ',CostList)
    mergeM=[(OpenList[i],CostList[i]) for i in range(len(OpenList)) ]
    mergeMs=sorted(mergeM, key = lambda x:x[1])
    OpenList=[i[0] for i in mergeMs]
    CostList=[i[1] for i in mergeMs]
    print('OpenList(sorted): ',OpenList)
    print('CostList(sorted): ',CostList)    
    print('ClosedList: ',ClosedList)    
print('completed') 


# In[214]:


# New version 
CostList=[]
state=[]
OpenList=['S']
ClosedList=[]
while OpenList: 
    #print(OpenList)
    state=OpenList[0]  
    print(state)
    del OpenList[0]  
    ClosedList.append(state)
    if state=='G':
        break
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
    costM=[(s,state) for s in activeNodes]
    #print(costM)
    #print(costM[0])
    costMat=[eachCost(costM[i],Node,C) for i in range(len(costM))]
    print(costMat)
    OpenList=activeNodes+OpenList  # the first item
    CostList=costMat+CostList  # the first item
    print('OpenList(1): ',OpenList)
    print('CostList(1): ',CostList)
    key=[k for k in range(len(OpenList)) if OpenList[k] not in ClosedList]
    OpenList=[OpenList[i] for i in key] 
    CostList=[CostList[i] for i in key] 
    #print('key: ',key)
    print('OpenList(2): ',OpenList)
    print('CostList(2): ',CostList)
    print('ClosedList: ',ClosedList)    
print('completed') 


# In[3]:


# New version 
CostList=[]
state=[]
stateC=[]
OpenList=['S']
CostList=[0]
ClosedList=[]
while OpenList: 
    #print(OpenList)
    state=OpenList[0]  
    stateC=CostList[0]
    print(state)
    del OpenList[0]  
    del CostList[0]  
    ClosedList.append(state)
    if state=='G':
        break
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
    #activeNodes=[item for item in TargetGraph[state] ]
    costM=[(s,state) for s in activeNodes]
    print(costM)
    #print(costM[0])
    costMat=[eachCost(costM[i],Node,C) for i in range(len(costM))]
    print(costMat)
    OpenList=activeNodes+OpenList  # the first item
    #print(stateC*costMat)
    #CostList=stateC*costMat+CostList  # the first item
    CostList=list(map(lambda x: x + stateC, costMat))+CostList  # the first item
    print('OpenList(1): ',OpenList)
    print('CostList(1): ',CostList)
    key=[k for k in range(len(OpenList)) if OpenList[k] not in ClosedList]
    OpenList=[OpenList[i] for i in key] 
    CostList=[CostList[i] for i in key] 
    #print('key: ',key)
    print('OpenList(2): ',OpenList)
    print('CostList(2): ',CostList)
    print('ClosedList: ',ClosedList)    
print('completed') 


# In[257]:


stateC=2
costMat=[2,4]
CostList=[1,2,3]
CostList=stateC*costMat+CostList  # the first item
print(stateC*costMat)
print(CostList)


# In[259]:


stateC=2
costMat=[2,4]
CostList=[1,2,3]
CostList=list(map(lambda x: x + stateC, costMat))+CostList  # the first item
print(list(map(lambda x: x + stateC, costMat)))
print(CostList)


# In[2]:


# New version with sort
CostList=[]
state=[]
stateC=[]
OpenList=['S']
CostList=[0]
ClosedList=[]
while OpenList: 
    #print(OpenList)
    state=OpenList[0]  
    stateC=CostList[0]
    print(state)
    del OpenList[0]  
    del CostList[0]  
    ClosedList.append(state)
    if state=='G':
        break
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
    costM=[(s,state) for s in activeNodes]
    costMat=[eachCost(costM[i],Node,C) for i in range(len(costM))]
    OpenList=activeNodes+OpenList  # the first item
    CostList=list(map(lambda x: x + stateC, costMat))+CostList  # the first item
    print('OpenList(1): ',OpenList)
    print('CostList(1): ',CostList)
    key=[k for k in range(len(OpenList)) if OpenList[k] not in ClosedList]
    OpenList=[OpenList[i] for i in key] 
    CostList=[CostList[i] for i in key] 
    #print('OpenList(2): ',OpenList)
    #print('CostList(2): ',CostList)
    mergeM=[(OpenList[i],CostList[i]) for i in range(len(OpenList)) ]
    mergeMs=sorted(mergeM, key = lambda x:x[1])
    OpenList=[i[0] for i in mergeMs]
    CostList=[i[1] for i in mergeMs]
    print('OpenList(sorted): ',OpenList)
    print('CostList(sorted): ',CostList)    
    print('ClosedList: ',ClosedList)    
print('completed') 


# In[246]:


import itertools

CostList=[[2, 1], [2, 6]]
print(CostList)
print([item  for i in CostList for item in [i] ])
print([item  for i in CostList for item in i if type(i)==list])
print([item for i in CostList for item in [i] if type(i)!=list])


#list(itertools.chain.from_iterable(CostList))
print(CostList)


# In[247]:


import itertools

l_2d = [[0, 1], 2, 3]

print(list(itertools.chain.from_iterable(l_2d)))
# [0, 1, 2, 3]


# In[151]:


keyT=[1,4,5]
[Node[i] for i in keyT] 


# In[168]:


type(1)
type([1])
i=[1]
type(i)==list
type(i)!=list


# In[ ]:




