#!/usr/bin/env python

import time
import numpy as np
import re
from collections import Counter

from numpy.lib.function_base import gradient
  

def load_input_data():
    with open("/Users/emccord/code/git/advent_of_code/2021/14/input") as input_file:
        input_temp = input_file.read()
        input_temp = input_temp.strip()
        input_data = input_temp.split('\n')
    return input_data


def process_input_data(input_data):

    n_lines = len(input_data)-2

    keys = [-1] * n_lines
    values = [-1] * n_lines

    cnt = 0
    for line_num in range(len(input_data)):

        if line_num == 0:
            input_polymer = input_data[line_num]

        elif line_num > 1:
            x, y = input_data[line_num].split(' -> ')

            keys[cnt] = x
            values[cnt] = y
            cnt += 1

    lookup = dict(zip(keys, values))

    return input_polymer, lookup 

def insert_new_polymers(polymer, lookup):

    new_polymer_chain = ''

    for x in range(len(polymer)):
        new_polymer_chain += polymer[x]

        if x < (len(polymer)-1):
            new_polymer_chain += lookup[polymer[x:x+2]]

    return new_polymer_chain

def calculate_difference(input_data, iterations):

    polymer, lookup = process_input_data(input_data)
    print('Data loaded')

    for z in range(iterations):

        it_time = time.time()
        polymer = insert_new_polymers(polymer, lookup)
        #print("--- %s iteration ---\n" % z)
        #print("--- %s polymer length ---\n" % len(polymer))
        #print("--- %s seconds ---\n" % (time.time() - it_time))
        
    stats = Counter(polymer)
    
    max = stats.most_common(1)[0][1]
    min = stats.most_common()[-1][1]

    print(stats)
    print(max-min)
    return (max-min)




def main():

    start_time = time.time()

    input_data = load_input_data()

    print("Day 14, Part 1")
    print(calculate_difference(input_data, 10))
    
    print("Day 14, Part 2")
    #print(calculate_difference(input_data, 40))

    print("--- %s seconds ---\n" % (time.time() - start_time))
    
if __name__ == "__main__":
    main()