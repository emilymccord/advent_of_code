#!/usr/bin/env python

import time


def calculate_power_consumption(input_data):
    
    sum_array, input_length = calculate_bit_sum(input_data)
    gamma_dec, gamma = calculate_gamma(sum_array, input_length)
    epsilon_dec, epsilon = calculate_epsilon(sum_array, input_length)
    return gamma_dec * epsilon_dec

def calculate_bit_sum(input_data):

    cnt = 0
    array_length = len(input_data[0])
    sum_array = [0] * array_length

    for line in input_data:
        sum_array = update_sum(sum_array, line)
        cnt += 1

    return sum_array, cnt

def update_sum(sum_array, bin_line):
    bit_list = list(bin_line)

    for x_bit in range(len(bit_list)):
        sum_array[x_bit] += int(bit_list[x_bit])

    return sum_array

def calculate_gamma(sum_array, input_length):
    
    gamma = ''
    for x_bit in range(len(sum_array)):
        if sum_array[x_bit] > (input_length/2):
            gamma += '1'
        else: 
            gamma += '0'
    
    gamma_dec = int(gamma, 2)
    return gamma_dec, gamma
    
def calculate_epsilon(sum_array, input_length):
    
    epsilon = ''
    for x_bit in range(len(sum_array)):
        if sum_array[x_bit] < (input_length/2):
            epsilon += '1'
        else: 
            epsilon += '0'
    
    epsilon_dec = int(epsilon, 2)
    return epsilon_dec, epsilon

def calculate_oxygen_generator_rating(input_data):
    
    array_length = len(input_data[0])

    num_list = input_data

    # Look at each bit
    for x_bit in range(array_length):
        
        new_list = []

        # Find most common bit
        sum_array, input_length = calculate_bit_sum(num_list)

        if sum_array[x_bit] >= (input_length/2):
            keep = '1'
        else: 
            keep = '0'

        # Iterate through all numbers in list,
        # add if list is correct
        for x_num in num_list:

            if x_num[x_bit] == keep:
                new_list.append(x_num)

        num_list = new_list

    ox_gen = num_list[0].__str__()
    ox_gen_dec = int(ox_gen, 2)

    return ox_gen_dec, ox_gen


def calculate_co2_scrubber_rating(input_data):
    
    array_length = len(input_data[0])

    num_list = input_data

    # Look at each bit
    for x_bit in range(array_length):
        
        new_list = []

        # Find most common bit
        sum_array, input_length = calculate_bit_sum(num_list)

        if sum_array[x_bit] >= (input_length/2):
            keep = '0'
        else: 
            keep = '1'

        # Iterate through all numbers in list,
        # add if list is correct
        for x_num in num_list:

            if x_num[x_bit] == keep:
                new_list.append(x_num)

        num_list = new_list
        if len(num_list) == 1:
            break

    co2_scrub = num_list[0].__str__()
    co2_scrub_dec = int(co2_scrub, 2)

    return co2_scrub_dec, co2_scrub



def calculate_life_support_rating(input_data):
    
    
    ox_gen = calculate_oxygen_generator_rating(input_data)[0]
    co2_srub = calculate_co2_scrubber_rating(input_data)[0]
    
    return ox_gen * co2_srub


def load_input_data_as_list():
    with open("input") as input_file:
        input_temp = input_file.read()
        input_temp = input_temp.strip()
        input_data = input_temp.split('\n')
    return input_data

def main():

    start_time = time.time()

    input_data = load_input_data_as_list()

    print("Day 3, Part 1")
    print(calculate_power_consumption(input_data))
    
    print("Day 3, Part 2")
    print(calculate_life_support_rating(input_data))

    print("--- %s seconds ---\n" % (time.time() - start_time))

if __name__ == "__main__":
    main()
