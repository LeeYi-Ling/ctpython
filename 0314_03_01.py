# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:34:29 2021

@author: Lee 10
"""

import random

ans=random.randint(1, 100)
guessnum=0
minnum=1
maxnum=100
count=0

if guessnum!=ans:
    for i in range(5):
        print()
        print('只能猜5次')
        guessnum=int(input('請輸入1~100的整數:'))
        count+=1
        if guessnum>ans:
            maxnum=guessnum-1
            print('猜小點:',minnum,'~',maxnum)
            print('已猜',count,'次')
        elif guessnum<ans:
            minnum=guessnum+1
            print('猜大點:',minnum,'~',maxnum)
            print('已猜',count,'次')
        else:
            print('猜對了!!')
            break
print('正確答案:',ans)