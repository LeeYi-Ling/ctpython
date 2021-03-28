# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:18:06 2021

@author: Lee 10
"""

keyinnum=int(input('請輸入金額:'))
if keyinnum <= 100000:
    Bonus=keyinnum*0.1
elif 100000 <keyinnum < 200000:
    Bonus=(100000*0.1)+((keyinnum-100000)*0.07)
elif 200000 <keyinnum < 400000:
    Bonus=(100000*0.1)+(100000*0.07)+((keyinnum-200000)*0.03)
print('獎金:',Bonus)
