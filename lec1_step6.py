#!/usr/bin/env python
# coding: utf-8

# In[1]:


TargetGraph={
    'S':['A','B'],
    'A':['S','C','D'],
    'B':['S','C'],
    'C':['A','B','D'],
    'D':['A','C']
#    'G':'unknown now
}


# In[4]:


OpenList=['S']
ClosedList=[]
while OpenList:
    state=OpenList[-1] # the last item
    del OpenList[-1] # the last item
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


# In[ ]:




