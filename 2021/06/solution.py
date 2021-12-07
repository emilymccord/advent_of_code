#!/usr/bin/env python

import csv, time

def increment_fish(fish_list):

    new_list = [0] * 9

    for x_fish in range(len(fish_list)):

        if x_fish == 0:
            new_list[6] += fish_list[x_fish]
            new_list[8] += fish_list[x_fish]
        else:
            new_list[x_fish-1] += fish_list[x_fish] 

    return new_list
    
def get_spawn_sums(fish_list):

    spawn_sums = [0] * 9
    for x_fish in fish_list:
        fish_num = int(x_fish)
        spawn_sums[fish_num] += 1
    return spawn_sums

def calculate_fish_quantity(input_data, days):

    new_list = get_spawn_sums(input_data)

    for i_day in range(days):
        new_list = increment_fish(new_list)
    return sum(new_list)


def load_input_data_as_list():
    with open("input") as input_file:
        input_temp = input_file.read()
        input_temp = input_temp.strip()
        input_data = input_temp.split('\n')
    return input_data

def load_input_data_as_array():

    with open("input") as input_file:
        input_temp = input_file.read()
        input_temp = input_temp.strip()
        input_data = input_temp.split(',')
        int_map = map(int, input_data)
        input_data = list(int_map)
    return input_data


def main():

    start_time = time.time()

    input_data = load_input_data_as_array()
    print("Day 6, Part 1")
    print(calculate_fish_quantity(input_data, 80))

    print("Day 6, Part 2")
    print(calculate_fish_quantity(input_data, 256))
    
    print("--- %s seconds ---\n" % (time.time() - start_time))

if __name__ == "__main__":
    main()