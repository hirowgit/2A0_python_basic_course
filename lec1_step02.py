#!/usr/bin/env python
# coding: utf-8

# In[5]:


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
# # @File    : lec1_step2.py 


# In[ ]:


import owlready2


# In[18]:


# A string with double quotation marks

"strawberry"


# In[19]:


# There is no output because of  ';'  for the termination.

'strawberry';


# In[20]:


# Therefore you need to use "print" function.

print('strawberry');
print( 'grape');


# In[21]:


# How to use quotation marks inside the string. 
# Note: double quotation marks displayed at the beginning and end 

'strawberry\'s cake'


# In[22]:


# But if you use double quotation marks inside the string,
# single quotation marks displayed at the beginning and end, as well as the default mode.

'I said \"hello\" to him.'


# In[23]:


# If you use both quotation marks inside the string,
# single quotation marks displayed at the beginning and end.

'I requested Mary\'s mother to say \"Please cook a special cake\".' 


# In[24]:


# Even both quotation marks are included with a different order,
# single quotation marks displayed at the beginning and end consistently.

'I said \"Please cook a special cake\" to Mary\'s mother.' 

