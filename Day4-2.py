# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:58:59 2020

@author: user
"""

t=0
file=open('貓貓.jpg','rb')
img=file.read()
file.close()

while t<10:
    file=open('複製jpg','wb')
    file.write(img)
    t=t+1
    file.close()