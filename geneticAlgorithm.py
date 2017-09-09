
import random

Popsize =10
pop =[]        # store population with fitness
D =5           #problem dimension
LB =-30
UB = 30
class Individual:
    def _init_(self, C,F):
        self.Chromosome =C
        self.Fitness =F
def Init():
    for i in range (0,Popsize):
        Chromosome =[round(random.uniform(LB,UB),2) for j in range(0,D)]
        Fitness =FitnessFunction(Chromosome)
        NewIndividual =Individual(Chromosome,Fitness)
        pop.append(NewIndividual)
def FitnessFunction(x):
    s = (x[4]-x[3]**2)**2+(x[3]-x[2]**2)**2+(x[3]-x[2]**2)**2+(x[2]-x[1]**2)**2+(x[1]-x[0]**2)**2
    return round(s,2)
init()
for p in pop:
    print "Chromosome ",p.Chromosome ,"\t Fitness :",p.Fitness
    print "\n"
