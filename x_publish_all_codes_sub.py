#!/usr/bin/env python
# coding: utf-8

# In[39]:


# import subprocess
# import shutil
# import os
# import time

# originalF='lec1_step1.ipynb';
# originalF='x_publish_all_codes_sub.ipynb';

#ftypes=['asciidoc', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python','slides'];
#ptypes=['asciidoc', 'html', 'tex', 'md', 'ipynb', 'pdf', 'py','slides.html'];
ftypes=['asciidoc', 'html', 'latex', 'markdown', 'pdf', 'python','slides'];
ptypes=['asciidoc', 'html', 'tex', 'md', 'pdf','slides.html'];

cmd0=['jupyter','nbconvert','--to'];
ftag=originalF.split('.')[0];

print(ftag)

for key in ftypes:
  cmd=cmd0+[key]+[originalF];
  Pcmd=' '.join(cmd)
  print(Pcmd)
  subprocess.Popen(cmd)
    
if  not os.path.isdir(ftag):
    print(' '.join(['The target folder \"',ftag,'\" does not exist...']))
    os.mkdir(ftag);
else:
    print(' '.join(['There exists',ftag]));    
    
for key in ptypes:
    target='.'.join([ftag,key]);
    print(target);
    if os.path.isfile(target):
        shutil.move(target,os.path.join(ftag,target));
        
time.sleep(10);
for key in ptypes:
    target='.'.join([ftag,key]);
    print(target);
    if os.path.isfile(target):
        os.remove(target);
        
target='.'.join([ftag,ptypes[0]]);
target2='.'.join([ftag,'txt']);
shutil.copy(os.path.join(ftag,target),os.path.join(ftag,target2));

# print("\n All processes were completed!")


# In[ ]:




