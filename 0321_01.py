# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 12:14:30 2021

@author: Lee 10
"""

import random
number=[]
while True:
    if len(number)==6:
        break
    num=random.randint(1,49)
    if number.count(num)==0:
        number.append(num)
number.sort()
print(number)
