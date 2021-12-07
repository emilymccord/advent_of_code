import numpy as np

filename = '/Users/emccord/code/advent_of_code/day2_input.txt'

with open(filename) as file:
    data = file.readlines()

count=0
horizontal=0
depth=0
aim=0

for x in range(len(data)):
    line = data[x].split(" ")
    x_command = line[0]
    x_number = int(line[1])

    if x_command == 'down':
        aim += x_number
    elif x_command == 'up':
        aim -= x_number
    elif x_command == 'forward':
        horizontal += x_number
        depth += aim*x_number

count = horizontal*depth

print(count)
