# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:21:45 2020

@author: user
"""

import os.path
if os.path.isfile('my_story.txt'):
    print('file 存在')
else:
    print('file 不存在')
    
X=open('my_story.txt','w')
X.write('ABC')

X=open('my_story.txt','a')
X.write('DEF')

X=open('my_story.txt','r')
Y=X.read()
print(Y)

X.close()