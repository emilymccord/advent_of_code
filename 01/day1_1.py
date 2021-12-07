import numpy as np

filename = '/Users/emccord/code/advent_of_code/day1_input.txt'

#with open(filename) as file:
#    lines = file.readlines()

data = np.loadtxt(filename)

diff_data = np.diff(data)
count=0

for x in diff_data:
    if x > 0:
        count = count+1

print(count)
