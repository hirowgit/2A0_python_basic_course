

```python
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
```


```python
# Practice 2-2 (page 21/28)
# https://www.slideshare.net/tadahirotaniguchi0624/2-46861654
```


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
```


```python
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
```

    1: A
    2: B
    3: D
    4: I
    5: E
    6: C
    7: F
    8: G
    9: J
    10: H
    completed



```python

```
