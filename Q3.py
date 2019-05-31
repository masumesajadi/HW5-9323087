# -*- coding: utf-8 -*-
"""
Created on Fri May 31 00:23:59 2019

@author: Asus
"""

A0=dict(zip(('a','b','c','d','e'),('1','2','3','4','5')))
A1=range(10)
for n in A1:
    print(n)
A2=[i for i in A1 if i in A0]
A3=sorted(A0[i] for i in A0)
A4=[[i,i*i]for i in A1]