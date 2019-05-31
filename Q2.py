# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:03:07 2019

@author: Asus
"""

def func(a , b,*args , **keywords):
    print(a,b)
    for arg in args:
        print(f' arg={arg}')
    for key in keywords:
        print(f'key={key},value={keywords[key]}')