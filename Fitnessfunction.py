#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 07:15:50 2017

@author: deep
"""
import math as m
import random
D=50
def FitnessFunction(x):
    s=0
    for i in range (0,D):
        a = (- x[i+1]+47)*m.sin(m.sqrt(abs(x[i+1] + (x[i]*0.5) +47)))
        b = x[i]*m.sin(m.sqrt(abs(x[i] - x[i+1] -47)))
        s+= a-b
    return s
x=[]
for j in range(0,D):
        x.append(random.randint(-512,512))
Fitness=FitnessFunction(x)
print "x = ", x , "Fitness: ", Fitness
