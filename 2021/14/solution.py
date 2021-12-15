#!/usr/bin/env python

import time

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

    # Go through input file
    for line_num in range(len(input_data)):

        # First line is polymer
        if line_num == 0:
            input_polymer = input_data[line_num]

        # Rest of file is pairs
        elif line_num > 1:
            x, y = input_data[line_num].split(' -> ')

            keys[cnt] = x
            values[cnt] = y
            cnt += 1

    # Create dictionary for lookup table
    lookup = dict(zip(keys, values))

    # Fill pair_totals from initial polymer
    pair_totals = dict()
    for pair in range(len(keys)):
        pair_totals[keys[pair]] = 0

    for x in range(len(input_polymer)-1):
        k = input_polymer[x:x+2]
        pair_totals[k] += 1

    # Keep track of first and last piece in 
    # polymer chain
    first = input_polymer[0]
    last = input_polymer[-1]

    return input_polymer, lookup, pair_totals, first, last


def insert_new_polymers(pair_totals, lookup):

    # Declare empty dictionary
    new_pair_totals = dict()
    for k, v in lookup.items():
        new_pair_totals[k] = 0

    for k, v in lookup.items():

        # Find total for current pair
        pair_total = pair_totals[k]

        # Figure out new pairs with splice
        p1 = k[0] + v
        p2 = v + k[1]

        # Find number of new pairs from old pair
        new_pair_totals[p1] += pair_total
        new_pair_totals[p2] += pair_total

    return new_pair_totals

def calculate_difference(input_data, iterations):

    input_polymer, lookup, pair_totals, first_letter, last_letter = process_input_data(input_data)

    # Initialize dictionary for letter sums
    letter_totals = dict()
    for k, v in lookup.items():
        letter_totals[v] = 0

    # Iterate through # of steps
    for z in range(iterations):
        pair_totals = insert_new_polymers(pair_totals, lookup)

    # Find totals
    for k1, v1 in pair_totals.items():

        rk1 = k1[0]
        rk2 = k1[1]

        # Since every pair is kept, letters are 
        # duplicated, divide by 2
        letter_totals[rk1] += (v1/2)
        letter_totals[rk2] += (v1/2)

    # Account for first pair
    letter_totals[first_letter] += .5
    letter_totals[last_letter] += .5

    # Find min/max
    min_letter = min(letter_totals, key=letter_totals.get)
    min_value = letter_totals[min_letter]

    max_letter = max(letter_totals, key=letter_totals.get)
    max_value = letter_totals[max_letter]

    return(max_value - min_value)

def main():

    start_time = time.time()

    input_data = load_input_data()

    print("Day 14, Part 1")
    print(calculate_difference(input_data, 10))
    
    print("Day 14, Part 2")
    print(calculate_difference(input_data, 40))

    print("--- %s seconds ---\n" % (time.time() - start_time))
    
if __name__ == "__main__":
    main()