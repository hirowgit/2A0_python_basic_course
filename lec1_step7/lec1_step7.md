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
# # @File    : lec1_step7.py 
```


```python
# Practice 3-1 (page 13/29)
# https://www.slideshare.net/tadahirotaniguchi0624/3-46861684
```


```python
# https://note.nkmk.me/python-dict-list-sort/
```


```python
import pprint

l = [{'Name': 'Australia', 'Population': 25680158, 'Capital City': 'Canberra','Points': [-35.28, 149.13]}, 
     {'Name': 'Bangladesh', 'Population': 169468990,'Capital City': 'Dhaka', 'Points': [23.71, 90.41]},
     {'Name': 'Chile', 'Population': 17373831,'Capital City': 'Santiago', 'Points': [-27.37, -70.33]}]
```


```python
pprint.pprint(sorted(l, key=lambda x: x['Name']))
```

    [{'Capital City': 'Canberra',
      'Name': 'Australia',
      'Points': [-35.28, 149.13],
      'Population': 25680158},
     {'Capital City': 'Dhaka',
      'Name': 'Bangladesh',
      'Points': [23.71, 90.41],
      'Population': 169468990},
     {'Capital City': 'Santiago',
      'Name': 'Chile',
      'Points': [-27.37, -70.33],
      'Population': 17373831}]



```python
pprint.pprint(sorted(l, key=lambda x: x['Population']))
```

    [{'Capital City': 'Santiago',
      'Name': 'Chile',
      'Points': [-27.37, -70.33],
      'Population': 17373831},
     {'Capital City': 'Canberra',
      'Name': 'Australia',
      'Points': [-35.28, 149.13],
      'Population': 25680158},
     {'Capital City': 'Dhaka',
      'Name': 'Bangladesh',
      'Points': [23.71, 90.41],
      'Population': 169468990}]



```python
pprint.pprint(sorted(l, key=lambda x: x['Population'], reverse=True))
```

    [{'Capital City': 'Dhaka',
      'Name': 'Bangladesh',
      'Points': [23.71, 90.41],
      'Population': 169468990},
     {'Capital City': 'Canberra',
      'Name': 'Australia',
      'Points': [-35.28, 149.13],
      'Population': 25680158},
     {'Capital City': 'Santiago',
      'Name': 'Chile',
      'Points': [-27.37, -70.33],
      'Population': 17373831}]



```python
# https://note.nkmk.me/python-dict-create/
keys = ['k1', 'k2', 'k3']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)
```

    {'k1': 1, 'k2': 2, 'k3': 3}



```python
Node=[]
keys = ['cost', 'h', 'f']
values = [1, 2, 3]
for i in range(len(keys)):
    d = {k: v for k, v in zip(keys, values)}
    print(d)
```

    {'cost': 1, 'h': 2, 'f': 3}
    {'cost': 1, 'h': 2, 'f': 3}
    {'cost': 1, 'h': 2, 'f': 3}



```python
# A: ascii code 65
chr(65)
```




    'A'




```python
# for i in range(1,10,1):
for i in range(1,10):
    s=chr(i+65-1)
    print(s)
```

    A
    B
    C
    D
    E
    F
    G
    H
    I



```python
# for i in range(1,10,1):
for i in range(65,65+10):
    s=chr(i)
    print(s)
```

    A
    B
    C
    D
    E
    F
    G
    H
    I
    J



```python
Node=[chr(i) for i in range(65,65+10)]
print(Node)
```

    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']



```python
H=list(range(len(Node)))
print(H)
H=list(range(len(Node)))
print(H)
F=3*list(range(len(Node)))
print(F)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
Cost =H
print(Cost)
H=list(map(lambda x: x * 2, Cost))
print(H)
F=list(map(lambda x: x * 3, Cost))
print(F)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]



```python
data1 = [1, 3, 6, 50, 5]
data2 = list(map(lambda x: x * 2, data1))
print(data1)
print(data2)
```

    [1, 3, 6, 50, 5]
    [2, 6, 12, 100, 10]



```python
keys = ['node','cost', 'h', 'f']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)
```

    {'node': 1, 'cost': 2, 'h': 3}



```python
keys = ['node','cost', 'h', 'f']
d_all=[]
for i in range(len(Node)):
    values=[Node[i],Cost[i],H[i],F[i]]
    d = {k: v for k, v in zip(keys, values)}
    d_all.append(d)
print(d_all)
```

    [{'node': 'A', 'cost': 0, 'h': 0, 'f': 0}, {'node': 'B', 'cost': 1, 'h': 2, 'f': 3}, {'node': 'C', 'cost': 2, 'h': 4, 'f': 6}, {'node': 'D', 'cost': 3, 'h': 6, 'f': 9}, {'node': 'E', 'cost': 4, 'h': 8, 'f': 12}, {'node': 'F', 'cost': 5, 'h': 10, 'f': 15}, {'node': 'G', 'cost': 6, 'h': 12, 'f': 18}, {'node': 'H', 'cost': 7, 'h': 14, 'f': 21}, {'node': 'I', 'cost': 8, 'h': 16, 'f': 24}, {'node': 'J', 'cost': 9, 'h': 18, 'f': 27}]



```python
Node
```




    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']




```python
pprint.pprint(sorted(d_all, key=lambda x: x['node']))
```

    [{'cost': 1, 'f': 3, 'h': 2, 'node': 'A'},
     {'cost': 2, 'f': 6, 'h': 4, 'node': 'B'},
     {'cost': 3, 'f': 9, 'h': 6, 'node': 'C'},
     {'cost': 4, 'f': 12, 'h': 8, 'node': 'D'},
     {'cost': 5, 'f': 15, 'h': 10, 'node': 'E'},
     {'cost': 6, 'f': 18, 'h': 12, 'node': 'F'},
     {'cost': 7, 'f': 21, 'h': 14, 'node': 'G'},
     {'cost': 8, 'f': 24, 'h': 16, 'node': 'H'},
     {'cost': 9, 'f': 27, 'h': 18, 'node': 'I'}]



```python
pprint.pprint(sorted(d_all, key=lambda x: x['cost']))
```

    [{'cost': 1, 'f': 3, 'h': 2, 'node': 'A'},
     {'cost': 2, 'f': 6, 'h': 4, 'node': 'B'},
     {'cost': 3, 'f': 9, 'h': 6, 'node': 'C'},
     {'cost': 4, 'f': 12, 'h': 8, 'node': 'D'},
     {'cost': 5, 'f': 15, 'h': 10, 'node': 'E'},
     {'cost': 6, 'f': 18, 'h': 12, 'node': 'F'},
     {'cost': 7, 'f': 21, 'h': 14, 'node': 'G'},
     {'cost': 8, 'f': 24, 'h': 16, 'node': 'H'},
     {'cost': 9, 'f': 27, 'h': 18, 'node': 'I'}]



```python
pprint.pprint(sorted(d_all, key=lambda x: x['h']))
```

    [{'cost': 1, 'f': 3, 'h': 2, 'node': 'A'},
     {'cost': 2, 'f': 6, 'h': 4, 'node': 'B'},
     {'cost': 3, 'f': 9, 'h': 6, 'node': 'C'},
     {'cost': 4, 'f': 12, 'h': 8, 'node': 'D'},
     {'cost': 5, 'f': 15, 'h': 10, 'node': 'E'},
     {'cost': 6, 'f': 18, 'h': 12, 'node': 'F'},
     {'cost': 7, 'f': 21, 'h': 14, 'node': 'G'},
     {'cost': 8, 'f': 24, 'h': 16, 'node': 'H'},
     {'cost': 9, 'f': 27, 'h': 18, 'node': 'I'}]



```python
pprint.pprint(sorted(d_all, key=lambda x: x['f']))
```

    [{'cost': 1, 'f': 3, 'h': 2, 'node': 'A'},
     {'cost': 2, 'f': 6, 'h': 4, 'node': 'B'},
     {'cost': 3, 'f': 9, 'h': 6, 'node': 'C'},
     {'cost': 4, 'f': 12, 'h': 8, 'node': 'D'},
     {'cost': 5, 'f': 15, 'h': 10, 'node': 'E'},
     {'cost': 6, 'f': 18, 'h': 12, 'node': 'F'},
     {'cost': 7, 'f': 21, 'h': 14, 'node': 'G'},
     {'cost': 8, 'f': 24, 'h': 16, 'node': 'H'},
     {'cost': 9, 'f': 27, 'h': 18, 'node': 'I'}]



```python
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
```

    [1, 6, 5]
    [[0, 8, 3], [0, 3, 5], [1, 6, 5], [1, 4, 8], [1, 3, 1], [4, 9, 3], [4, 0, 6], [5, 2, 7], [9, 8, 5], [9, 0, 0]]



```python
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
```

    [1, 6, 5]
    [[9, 0, 0], [1, 3, 1], [0, 8, 3], [4, 9, 3], [9, 8, 5], [1, 6, 5], [0, 3, 5], [4, 0, 6], [5, 2, 7], [1, 4, 8]]



```python
list_0 = [
        [1, 3, 2],
        [2, 2, 1],
        [3, 1, 3]
    ]
stag=1
print(list_0[:][stag])
list_0.sort(key=lambda x: x[stag])
print(list_0)
```

    [2, 2, 1]
    [[3, 1, 3], [2, 2, 1], [1, 3, 2]]



```python
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
```

    [1, 4, 7]
    [1, 4, 7]
    [1, 4, 7]
     
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]



```python
[list_0[i][0] for i in range(len(list_0))]
```




    [1, 2, 3]




```python
list_0 = [
        [9, 8, 5],
        [0, 8, 3]
    ]
print(list_0[1])
list_0.sort(key=lambda x: x[2])
print(list_0)
```

    [0, 8, 3]
    [[0, 8, 3], [9, 8, 5]]

