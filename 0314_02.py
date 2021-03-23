# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:05:19 2021

@author: Lee 10
"""

'''
作業二
'''
num=int(input('請輸入2~100間的整數:'))

for i in range(2,num+1):
    if i%4==0:
        print(i,'是4的倍數')
print('===程式執行結束===')

for i in range(2,num+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print (i,"是質數")
