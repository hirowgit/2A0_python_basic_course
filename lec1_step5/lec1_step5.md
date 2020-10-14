

```python
# open list and closed list
```


```python
# first idea
OpenList=[1,2,3,4]
```


```python
OpenList[1]
```




    2




```python
OpenList[0]  # note array start from [0] like C, C++
```




    1




```python
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
```


      File "<ipython-input-105-1bf0c221c17f>", line 5
        'S':'A','B',
                   ^
    SyntaxError: invalid syntax




```python
TargetGraph={
    'S':['A','B'],
    'A':['S','C','D'],
    'B':['S','C'],
    'C':['A','B','D'],
    'D':['A','C']
#    'G':'unknown now
}
```


```python
TargetGraph['S']
```




    ['A', 'B']




```python
TargetGraph['S'][0]
```




    'A'




```python
TargetGraph['S'].append("G")
```


```python
print(TargetGraph)
```

    {'S': ['A', 'B', 'G'], 'A': ['S', 'B'], 'B': ['A', 'B'], 'C': ['A', 'B'], 'D': ['A', 'B']}



```python
# If you want to delete the last item
del TargetGraph['S'][-1]
print(TargetGraph)
```

    {'S': ['A', 'B'], 'A': ['S', 'C', 'D'], 'B': ['S', 'C'], 'C': ['A', 'B', 'D'], 'D': ['A', 'C']}



```python
tList=[]
if tList: 
    print('Not Empty')
else:
    print('Empty') 
```

    Empty



```python
tList=[1,2,3,4,5]
while tList:
    del tList[0]
    print(tList)
print('completed') 
```

    [2, 3, 4, 5]
    [3, 4, 5]
    [4, 5]
    [5]
    []
    completed



```python
OpenList=['S']
OpenList.insert(0,['A','B']) 
print(OpenList)
```

    [['A', 'B'], 'S']



```python
sList=['A','B']
[d for d in sList]
```




    ['A', 'B']




```python
TargetGraph['A']
```




    ['S', 'C', 'D']




```python
OpenList=['S']
sList=['A','B']
OpenList.insert(0, sList) 
OpenList=[d for d in OpenList]
print(OpenList)
OpenList=[item for i in OpenList for item in i]
print(OpenList)
```

    [['A', 'B'], 'S']
    ['A', 'B', 'S']



```python
if 'A' in ['A', 'B', 'S']: 
    print('Yes')
```

    Yes



```python
if 'A' not in ['A', 'B', 'S']: 
    print('Yes')
```


```python
tList=[]
addList=['A', 'B', 'S']
ClosedList=['S']
activeNode=[item for item in addList if item not in ClosedList]
activeNode
```




    ['A', 'B']




```python
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
```

    [['A', 'B'], 'S']
    ['A', 'B']
    ['A', 'B']



```python
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
```

    S
    A
    C
    B
    D
    completed



```python

```
