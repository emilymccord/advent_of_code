#!/usr/bin/env python

import time
import numpy as np
import re
  
def load_input_data_as_array():

    with open("input") as input_file:
        input_temp = input_file.read()
        input_temp = input_temp.strip()
        input_temp = input_temp.split(',')

        input_data = input_temp

        int_map = map(int, input_data)
        input_data = list(int_map)

    return input_data

def calculate_min_fuel(input_data):

    localDiff = [0] * len(input_data)
    fuel = [0] * max(input_data)

    for xVal in range(min(input_data), max(input_data)):

        localDiff = [0] * len(input_data)
        for x in range(len(input_data)):
            localDiff[x] = abs(input_data[x] - xVal)

        fuel[xVal] = sum(localDiff)

    return min(fuel)

def calculate_min_fuel_part2(input_data):

    localDiff = [0] * len(input_data)
    fuel = [0] * max(input_data)

    fuel_table = calculate_table_of_fuel(input_data)

    for xVal in range(min(input_data), max(input_data)):

        localDiff = [0] * len(input_data)
        for x in range(len(input_data)):
            localDiff[x] = fuel_table[abs(input_data[x] - xVal)]

        fuel[xVal] = sum(localDiff)

    return min(fuel)

def calculate_table_of_fuel(input_data):

    fuel_table = [0] * (max(input_data)+1)
    for x in range(1, len(fuel_table)):

        fuel_amt = 0
        for y in range(1, x+1):
            fuel_amt += y

        fuel_table[x] = fuel_amt

    return fuel_table

def main():

    start_time = time.time()

    input_data = load_input_data_as_array()

    print("Day 7, Part 1")
    print(calculate_min_fuel(input_data))
    
    print("Day 7, Part 2")
    print(calculate_min_fuel_part2(input_data))

    print("--- %s seconds ---\n" % (time.time() - start_time))
    
if __name__ == "__main__":
    main()