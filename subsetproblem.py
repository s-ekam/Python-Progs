import random
Set         = set([-12,-3,-6,7,2,-2,6,3,9,-7,-5,-8,1,11,-9,-4])
SetSize     = 5
ResultList  = set()    # Store Result List i.e. list of sets whose sum is zero
Iterations  = 5000   # Number of Inerations


for i in range(Iterations):
    Chromosome=tuple(random.sample(Set,SetSize))
    
    # Sum the number of elements in the Chromosome
    if sum(Chromosome) == 0:
        ResultList.add((Chromosome))

for r in ResultList:
	print r
print "\nTotal Sets: ", len(ResultList)

