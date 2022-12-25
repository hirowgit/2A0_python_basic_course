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
# # @File    : lec1_step5.py 


# In[ ]:


# Practice 2-2 (page 21/28)
# https://www.slideshare.net/tadahirotaniguchi0624/2-46861654


# In[8]:


# open list and closed list


# In[10]:


# first idea
OpenList=[1,2,3,4]


# In[5]:


OpenList[1]


# In[6]:


OpenList[0]  # note array start from [0] like C, C++


# In[10]:


# As you see in Fig 2.9, open list and closed list should be defined at each node. 
# Therefore those lists require multiple open and closed lists for each node.
# It implies dictionary is a good option.
TargetGraph={
    'S':'A','B',
    'A':'S','C','D',
    'B':'S','C',
    'C':'A','B','D',
    'D':'A','C',
#    'G':'unknown now
}


# In[11]:


TargetGraph={
    'S':['A','B'],
    'A':['S','C','D'],
    'B':['S','C'],
    'C':['A','B','D'],
    'D':['A','C']
#    'G':'unknown now
}


# In[111]:


TargetGraph['S']


# In[112]:


TargetGraph['S'][0]


# In[3]:


TargetGraph['S'].append('G')


# In[23]:


print(TargetGraph)


# In[114]:


# If you want to delete the last item
del TargetGraph['S'][-1]
print(TargetGraph)


# In[115]:


tList=[]
if tList: 
    print('Not Empty')
else:
    print('Empty') 


# In[4]:


tList=[1,2,3,4,5]
while tList:
    del tList[0]
    print(tList)
print('completed') 


# In[117]:


OpenList=['S']
OpenList.insert(0,['A','B']) 
print(OpenList)


# In[118]:


sList=['A','B']
[d for d in sList]


# In[119]:


TargetGraph['A']


# In[6]:


OpenList=['S']
sList=['A','B']
OpenList.insert(0, sList[:]) 
OpenList=[d for d in OpenList]
print(OpenList)
OpenList=[item for i in OpenList for item in i]
print(OpenList)


# In[13]:


OpenList=['S']
sList=['A','B']
OpenList.append(sList)
OpenList


# In[12]:


OpenList=['S']
sList=['A','B']
OpenList.insert(0, sList)
OpenList


# In[14]:


OpenList=['S']
sList=['A','B']
OpenList.extend(sList)
OpenList


# In[78]:


if 'A' in ['A', 'B', 'S']: 
    print('Yes')


# In[79]:


if 'A' not in ['A', 'B', 'S']: 
    print('Yes')


# In[88]:


tList=[]
addList=['A', 'B', 'S']
ClosedList=['S']
activeNode=[item for item in addList if item not in ClosedList]
activeNode


# In[134]:


OpenList=['S']
state='S'
OpenList.insert(0, TargetGraph[state]) 
print(OpenList)

OpenList=['S']
ClosedList=['S']
state='S'
print(TargetGraph[state])
activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
OpenList.insert(0, activeNodes) 
OpenList=[item for i in OpenList for item in i if item not in ClosedList]
print(OpenList)


# In[13]:


OpenList=['S']
ClosedList=[]
while OpenList:
    state=OpenList[0]
    del OpenList[0]
    ClosedList.append(state)
    print(state)
    if state=='G':
        break
 #   activeNodes=TargetGraph[state]
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
    OpenList.insert(0, activeNodes)
#    OpenList=[item for i in OpenList for item in i]
    OpenList=[item for i in OpenList for item in i if item not in ClosedList]
print('completed') 


# In[59]:


OpenList=['S']
ClosedList=[]
while OpenList:
    state=OpenList[0]
    del OpenList[0]
    ClosedList.extend(state)
    print(state)
    if state=='G':
        break
 #   activeNodes=TargetGraph[state]
    activeNodes=list(set(TargetGraph[state]) -set(ClosedList))
    OpenList.extend(activeNodes)
#    OpenList=[item for i in OpenList for item in i]
 #   OpenList=set(OpenList) -set(ClosedList)
#    OpenList=[item for i in OpenList for item in i if item not in ClosedList]
#print('completed') 


# In[7]:


# completed version of Depth-first search

OpenList=['S']
ClosedList=[]
while OpenList:
    state=OpenList[-1]
    del OpenList[-1]
    ClosedList.extend(state)
    ClosedList=list(set(ClosedList))
    print(['state',state])
    print(['OpenList(1)',OpenList])
    print(['ClosedList',ClosedList])
    if state=='G':
        break
    tmpSt=set(TargetGraph[state]) -set(ClosedList)
    activeNodes=list(tmpSt -set(OpenList))    
    OpenList.extend(activeNodes)
  #  OpenList=list(set(OpenList))
    print(['OpenList(2)',OpenList])
    print('')
print('Completed') 


# In[13]:


# completed version of Depth-first search

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
  #  OpenList=list(set(OpenList))
    print(['OpenList(2)',OpenList])
    print('')
print('Completed') 


# In[14]:


# completed version of Breadth-first search

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
    OpenList.extend(activeNodes)
  #  OpenList=list(set(OpenList))
    print(['OpenList(2)',OpenList])
    print('')
print('Completed') 


# In[16]:


activeNodes


# In[15]:


# completed version of Breadth-first search

OpenList=['S']
ClosedList=[]
while OpenList:
    state=OpenList[0]
    del OpenList[0]
    ClosedList.extend(state)
    ClosedList=list(set(ClosedList))
    print(['state',state])
    print(['OpenList(1)',OpenList])
    print(['ClosedList',ClosedList])
    if state=='G':
        break
    tmpSt=set(TargetGraph[state]) -set(ClosedList)
    activeNodes=list(tmpSt -set(OpenList))    
    OpenList.extend(activeNodes)
  #  OpenList=list(set(OpenList))
    print(['OpenList(2)',OpenList])
    print('')
print('Completed') 


# In[138]:


tmpL= ['D', 'C',  'A', 'S', 'C', 'A', 'B', 'A', 'B']
tmpL= [ 'A', 'S', 'C', 'A', 'B', 'B', 'A']
list(set(tmpL))


# In[120]:


ClosedList=['S', 'B', 'A', 'C', 'D', 'C', 'D']
set(ClosedList)


# In[116]:


OpenList=['S']
ClosedList=[]
while OpenList:
    state=OpenList[-1]
    del OpenList[-1]
    ClosedList.extend(state)
    print(state)
    if state=='G':
        break
 #   activeNodes=TargetGraph[state]
    activeNodes=list(set(TargetGraph[state]) -set(ClosedList))
    #print(state)
    OpenList.extend(activeNodes)
#    OpenList=[item for i in OpenList for item in i]
 #   OpenList=set(OpenList) -set(ClosedList)
#    OpenList=[item for i in OpenList for item in i if item not in ClosedList]
print('completed') 


# In[114]:


OpenList=['S']
ClosedList=[]
state=OpenList[0]
del OpenList[0]
ClosedList.extend(state)
print(state)
activeNodes=list(set(TargetGraph[state]) -set(ClosedList))
print(activeNodes)
print(OpenList)
OpenList=activeNodes.extend(OpenList)
print(OpenList)


# In[103]:


OpenList=['S']
ClosedList=[]
state=OpenList[0]
del OpenList[0]
ClosedList.extend(state)
print(state)
activeNodes=list(set(TargetGraph[state]) -set(ClosedList))

print('activeNodes')
print(activeNodes)
print('OpenList')
print(OpenList)
print('ClosedList')
print(ClosedList)
OpenList.extend(activeNodes)
print('OpenList')
print(OpenList)


# In[109]:


state=OpenList[0]
del OpenList[0]
ClosedList.extend(state)
print(state)
activeNodes=list(set(TargetGraph[state]) -set(ClosedList))

print('activeNodes')
print(activeNodes)
print('OpenList')
print(OpenList)
print('ClosedList')
print(ClosedList)
OpenList.extend(activeNodes)
print('OpenList')
print(OpenList)


# In[88]:


activeNodes=['B', 'A']
print(activeNodes)
OpenList=[]
print(OpenList)
activeNodes.extend(OpenList)
print(activeNodes)
print(OpenList)
print(activeNodes.extend(OpenList))
#OpenList=activeNodes.extend(OpenList)
activeNodes.extend(OpenList)
print(OpenList)
print(activeNodes)
activeNodes.extend(OpenList)


# In[66]:


state=OpenList[0]
del OpenList[0]
ClosedList.extend(state)
print(state)
activeNodes=list(set(TargetGraph[state]) -set(ClosedList))
print(activeNodes)
#OpenList.extend(activeNodes)
OpenList=activeNodes.extend(OpenList)
OpenList


# In[57]:


OpenList
activeNodes


# In[51]:


OpenList=['S']
del OpenList[0]
activeNodes
OpenList=activeNodes.extend(OpenList)


# In[44]:


activeNodes=list(set(TargetGraph[state]) -set(ClosedList))
activeNodes
OpenList=activeNodes.extend(OpenList)
OpenList


# In[25]:


OpenList=['S']
ClosedList=[]
state=OpenList[0]
del OpenList[0]
ClosedList.extend(state)
ClosedList
TargetGraph[state]
OpenList


# In[29]:


set(['S','A','B'])-set(['C','A','B'])


# In[28]:


set([1,2,3,4,5])-set([2,4])


# In[136]:


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


# In[143]:


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
 #   activeNodes=TargetGraph[state]
    activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
    OpenList.insert(0, activeNodes)
#    OpenList=[item for i in OpenList for item in i]
    OpenList=[item for i in OpenList for item in i if item not in ClosedList]
    k=k+1
print('completed') 


# In[140]:


activeNodes=[item for item in TargetGraph[state] if item not in ClosedList]
activeNodes


# In[144]:


TargetG=['A','B','C','D','E','F']
ClosedList=['C','F']
OpenList=['A']
activeNodes=[item for item in TargetG if item not in ClosedList]
activeNodes
print('activeNodes',activeNodes) 
OpenList.insert(0, activeNodes)
print('OpenList',OpenList) 


# In[145]:


TargetG=['A','B','C','D','E','F']
ClosedList=['C','F']
OpenList=['A']
activeNodes=[item for item in TargetG if item not in ClosedList]
activeNodes
print('activeNodes',activeNodes) 
OpenList.append(activeNodes)
print('OpenList',OpenList) 


# In[146]:


TargetG=['A','B','C','D','E','F']
ClosedList=['C','F']
OpenList=['A']
activeNodes=[item for item in TargetG if item not in ClosedList]
activeNodes
print('activeNodes',activeNodes) 
OpenList.extend(activeNodes)
print('OpenList',OpenList) 


# In[148]:


TargetG=['A','B','C','D','E','F']
ClosedList=['C','F']
OpenList=['A']
activeNodes=[item for item in TargetG if item not in ClosedList]
print('activeNodes',activeNodes) 


# In[149]:


TargetG=['A','B','C','D','E','F']
ClosedList=['C','F']
OpenList=['A']
activeNodes=list(set(TargetG)-set(ClosedList))
print('activeNodes',activeNodes) 


# In[154]:


import numpy as np
from pytictoc import TicToc 
t = TicToc() #create instance of class 
t.tic() #Start timer 
t.toc() #Time elapsed since t.tic() Elapsed time is 2.612231 seconds.


# In[167]:


t = TicToc() #create instance of class 
loopN=100
NofD_target=10000
NofD_clist=5000
t.tic() #Start timer 
for i in range(0,loopN):
    rD_target=np.random.randint(0,NofD_target,size=NofD_target)
    rD_clist=np.random.randint(0,NofD_target,size=NofD_clist)
    rDL_target=rD_target.tolist()
    rDL_clist=rD_clist.tolist()
    activeNodes=[item for item in rDL_target if item not in rDL_clist]

    # print(rDL_target)
    # print(rDL_clist)
    
t.toc()


# In[168]:


t = TicToc() #create instance of class 
loopN=100
NofD_target=10000
NofD_clist=5000
t.tic() #Start timer 
for i in range(0,loopN):
    rD_target=np.random.randint(0,NofD_target,size=NofD_target)
    rD_clist=np.random.randint(0,NofD_target,size=NofD_clist)
    rDL_target=rD_target.tolist()
    rDL_clist=rD_clist.tolist()
    activeNodes=list(set(rD_target)-set(rD_clist))
    # print(rDL_target)
    # print(rDL_clist)
    
t.toc()


# In[171]:


sD = np.arange(10).reshape(2, 5)
sD = sD/2
print(sD)
np.savetxt('csv_data_d.csv', sD, delimiter=',', fmt='%d') 
np.savetxt('csv_data_f.csv', sD, delimiter=',', fmt='%.5f')

