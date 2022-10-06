```python
## Python basics for novice data scientists, supported by Wagatsuma Lab@Kyutech 
#
# The MIT License (MIT): Copyright (c) 2020 Hiroaki Wagatsuma and Wagatsuma Lab@Kyutech
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. */
#
# # @Time    : 2020-4-20 
# # @Author  : Hiroaki Wagatsuma
# # @Site    : https://github.com/hirowgit/2A_python_basic_course
# # @IDE     : Python 3.7.7 (default, Mar 10 2020, 15:43:27) [Clang 10.0.0 (clang-1000.11.45.5)] on darwin
# # @File    : lec1_step4.py 
```


```python
# Different types of loading methods 
import math 

pi=math.pi

print(pi)
```

    3.141592653589793



```python
# module loading with an abbreviation i.e. short name
import math as mm

pi=mm.pi

print(pi)
```

    3.141592653589793



```python
# How to use various functions in the module
import math 

pi=math.pi
x1=math.sin(pi/2)

print(pi)
print(x1)
```

    3.141592653589793
    1.0



```python
# Different types of loading methods 
import math 

pi=math.pi
x1=math.sin(pi/2)
x2=math.cos(0)
x3=math.tan(pi/4)

print(pi)
print(x1)
print(x2)
print(x3)
```

    3.141592653589793
    1.0
    1.0
    0.9999999999999999



```python
# Different types of loading methods 
from math import pi 
from math import sin 
from math import cos
from math import tan

#pi=math.pi
x1=sin(pi/2)
x2=cos(0)
x3=tan(pi/4)

print(pi)
print(x1)
print(x2)
print(x3)
```

    3.141592653589793
    1.0
    1.0
    0.9999999999999999



```python
# Different types of loading methods 
from math import *

#pi=math.pi
x1=sin(pi/2)
x2=cos(0)
x3=tan(pi/4)

print(pi)
print(x1)
print(x2)
print(x3)
```

    3.141592653589793
    1.0
    1.0
    0.9999999999999999



```python
import math
import numpy as np

pi=math.pi
x1=math.sin(pi/4)
x2=np.sin(pi/4)
x3=np.sin([0,pi/4,pi/2,3*pi/4])

print(x1)
print(x2)
print(x3)
```

    0.7071067811865475
    0.7071067811865475
    [0.         0.70710678 1.         0.70710678]



```python
x1=math.sin([0,pi/4,pi/2,3*pi/4])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-c47a2d0560bb> in <module>()
    ----> 1 x1=math.sin([0,pi/4,pi/2,3*pi/4])
    

    TypeError: must be real number, not list



```python

```
