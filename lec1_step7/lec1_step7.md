

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
for i in 
d = {k: v for k, v in zip(keys, values)}
print(d)
```


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
H=list(range(1,len(Node)))
print(H)
H=list(range(1,len(Node)))
print(H)
F=3*list(range(1,len(Node)))
print(F)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
print(Cost)
H=list(map(lambda x: x * 2, Cost))
print(H)
F=list(map(lambda x: x * 3, Cost))
print(F)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [2, 4, 6, 8, 10, 12, 14, 16, 18]
    [3, 6, 9, 12, 15, 18, 21, 24, 27]



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
values = [1, 2, 3]
d_all=[]
for i in range(0,len(Node)-1):
    values=[Node[i],Cost[i],H[i],F[i]]
    d = {k: v for k, v in zip(keys, values)}
    d_all.append(d)
print(d_all)
```

    [{'node': 'A', 'cost': 1, 'h': 2, 'f': 3}, {'node': 'B', 'cost': 2, 'h': 4, 'f': 6}, {'node': 'C', 'cost': 3, 'h': 6, 'f': 9}, {'node': 'D', 'cost': 4, 'h': 8, 'f': 12}, {'node': 'E', 'cost': 5, 'h': 10, 'f': 15}, {'node': 'F', 'cost': 6, 'h': 12, 'f': 18}, {'node': 'G', 'cost': 7, 'h': 14, 'f': 21}, {'node': 'H', 'cost': 8, 'h': 16, 'f': 24}, {'node': 'I', 'cost': 9, 'h': 18, 'f': 27}]



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

```
