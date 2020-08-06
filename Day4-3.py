# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:38:48 2020

@author: user
"""

d={}
import os.path
def Menu():
    print('******************')
    print('1.匯入成績')
    print('2.列出所有成績')
    print('3.')
    print('4.')
    print('5.離開系統')

if os.path.isfile('scores.txt'):
    new=open('scores.txt','r')
    print('開啟舊檔案')
else:
    new=open('scores.txt','w')
    print('建立新檔案')
    

while True:
    Menu()
    a=int(input('輸入欲執行選項'))
    if a==1:
        name=str(input('請輸入姓名(按+跳回主選單):'))
        score=str(input('請輸入成績(按+跳回主選單):'))
        if name=='+':
           break
        elif name not in d:
            d[name]=score
            for k,v in d.items():
                add=open('scores.txt','a')
                add.write(k)
                add.write(':')
                add.write(v)
                add.write('\n')
        else:
            print('此成績已登入')
     
 
