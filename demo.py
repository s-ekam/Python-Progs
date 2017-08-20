import string
import random
f=open('output.txt', 'w')
j=0
for i in range (10, 15):
    while(j<100):
    #print random.sample(string.ascii_letters, i)
        f.write("".join(random.sample(string.ascii_letters, i))+"\n")
        j=j+1
f.close()
