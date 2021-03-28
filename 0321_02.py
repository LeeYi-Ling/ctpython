# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 12:26:16 2021

@author: Lee 10
"""

import random

number=[]
while True:
    if len(number)==7:
        break
    num=random.randint(1,100)
    number.append(num)
number.sort()
print(number)

keyinnum=int(input('請輸入一正整數:'))

while True:
    n=len(number)//2

    if len(number)==1:
        break
    if keyinnum > number[n]:
        del number[:n+1]             
        print(number)
    elif keyinnum < number[n]:
        del number[n:]
        print(number)
    else:
        del number[:n]
        del number[-n:]
        print(number)
        