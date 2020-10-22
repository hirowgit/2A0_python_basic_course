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


# In[38]:


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


# In[90]:


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


# In[99]:


N=7
Node=[chr(i) for i in range(65,65+N)]
Node=['S']+Node
print(Node)


# In[110]:


[s for s in range(len(Node)) if 'E' in Node[s]][0]


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


# In[129]:


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


# In[142]:


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


# In[243]:


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


# In[253]:


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




