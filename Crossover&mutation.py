#2!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 23:23:56 2017

@author: deep
"""

import random 
from copy import deepcopy

D =10
LB=-30
UB=30

def FitnessFunction(x):
    s =sum(x)
    return round(s,2)
pt1 =random.randint(1,D/2)
pt2 =random.randint(D/2,D-2)
#choose parents 
p1 =[6,-2 ,11,-8,-6,6,-2,11,-8,-6]
p2 =[-7,11,7,-2,8,-7,1,-2,9]
p1Fitness =FitnessFunction(p1)
p2Fitness =FitnessFunction(p2)
#generate new childs
c1 =p1[0:pt1]+p2[pt1:pt2]+p1[pt2:]
c2 =p2[0:pt1]+p1[pt1:pt2]+p2[pt2:]
c1Fitness =FitnessFunction(c1)
c2Fitness =FitnessFunction(c2)
print "****crossover *****"
print "pt :", pt1," ,", pt2
print "\n p1: ",p1 ,"\t Fitness: ", p1Fitness
print "p2 :", p2,"\Fitness: ",p2Fitness
print "\nc1: ",c1,"\t Fitness: ", c1Fitness
print "c2: ",c2, "\t Fitness: ", c2Fitness
pt1 =random.randint(0,D-1)
pt2 =random.randint(0,D-1)
p =[-7,11,7,-2,8,-7]
pFitness =FitnessFunction(p)
print "P fitness :", pFitness
c =deepcopy(p)
c[pt1] =random.uniform(LB,UB)
c[pt2] =random.uniform(LB,UB)
cFitness =FitnessFunction(c)
print "****Mutation *******"
print "pt1: ",pt1 ," ,",pt2
print "\n p: ", p, "\t Fitness :",pFitness
print "c: ",c,"\t Fitness :",cFitness
print "\n"

