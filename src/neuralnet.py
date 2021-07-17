from mnist import MNIST
import random 
import sys
from math import *

stdprint = sys.stdout.write
mndata = MNIST('samples')

#images, labels = mndata.load_training()
# or
#
images, labels = mndata.load_testing()


def printimage(index):
    pal = [". ", "░░", "▒▒", "▓▓", "██"]
    for j in range(len(images[index])):
        if j%28==0:
            stdprint("\n")
        val = images[index][j]
        stdprint(pal[floor((val/256)*5)])
    print("\n", labels[index])

for i in range(10):
    index = random.randrange(0, len(images)) 
    printimage(index)
    #print(mndata.display(images[index]))
    
    
    
    
    
    