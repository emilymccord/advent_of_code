import numpy as np
from numpy.core.fromnumeric import size

filename = '/Users/emccord/code/advent_of_code/day1_input.txt'

with open(filename) as file:
    data = file.readlines()

count=0

for x in range(len(data)-3):
    if (int(data[x+3]) + int(data[x+2]) + int(data[x+1])) - (int(data[x+2])+int(data[x+1])+int(data[x])) > 0:
        count = count+1

print(count)
