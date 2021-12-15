#!/usr/bin/env python

import time
import numpy as np
import re

from numpy.lib.function_base import gradient
  

def load_input_data():
    with open("/Users/emccord/code/git/advent_of_code/2021/13/input") as input_file:
        input_temp = input_file.read()
        input_temp = input_temp.strip()
        input_data = input_temp.split('\n')
    return input_data


def load_grid(input_data):

    n_lines = len(input_data)

    x_vals = [-1] * n_lines
    y_vals = [-1] * n_lines

    for line in range(n_lines):

        if len(input_data[line]) == 0:
            new_start = line
            break
        elif(input_data[line][0].isnumeric()):
            x, y = input_data[line].split(',')
            x_vals[line] = int(x)
            y_vals[line] = int(y)
        else:
            print('What is happening here???')

    max_x = max(x_vals)
    max_y = max(y_vals)

    grid = np.zeros([ max_y+1, max_x+1])

    cnt = 0
    while(x_vals[cnt] >= 0):
        grid[y_vals[cnt], x_vals[cnt]] = 1
        cnt += 1

    return grid


def load_folds(input_data):

    n_lines = len(input_data)

    instructions = [''] * n_lines
    folds = [-1] * n_lines

    cnt = 0
    for line in range(n_lines):

        #print(input_data[line])
        #print(len(input_data[line]))
        if len(input_data[line]) == 0:
            new_start = line
            continue
        elif(input_data[line][0].isnumeric()):
            continue
        else:
            part1, part2 = input_data[line].split('=')

            if 'x' in part1:
                instructions[cnt] = 'x'
            elif 'y' in part1:
                instructions[cnt] = 'y'

            
            folds[cnt] = int(part2)

            #print(input_data[line])
            #print('What is happening here???')
            cnt += 1


    return instructions[0:cnt], folds[0:cnt]


def fold_data(grid, instruction, fold_val):



    if instruction == 'x':
        #print('x')
        new_grid = grid[:, 0:fold_val]

        for x in range(fold_val+1, len(grid[0])):

            diff_x = x - fold_val
            new_x = fold_val - diff_x

            for y in range(len(grid)):
                if grid[y, x] == 1:
                    new_grid[y, new_x] = 1



    elif instruction == 'y':
        #print('y')
        new_grid = grid[0:fold_val, :]

        for y in range(fold_val+1, len(grid)):

            diff_y = y - fold_val
            new_y = fold_val - diff_y

            for x in range(len(grid[0])):
                if grid[y, x] == 1:
                    new_grid[new_y, x] = 1


    #print('Done folding')
    return new_grid

def calculate_number_of_dots(input_data):

    grid = load_grid(input_data)
    instructions, folds = load_folds(input_data)


    for fold in range(len(folds)):
        grid = fold_data(grid, instructions[fold], folds[fold])
        print("--- Fold %d dots ---\n" % sum(sum(grid)))


    grid_sum = sum(sum(grid))
    return grid, grid_sum


def main():

    start_time = time.time()

    input_data = load_input_data()

    print("Day 13, Part 1")
    print(calculate_number_of_dots(input_data))
    
    print("Day 13, Part 2")
    #print(calculate_sum_of_digits(input_data))

    print("--- %s seconds ---\n" % (time.time() - start_time))
    
if __name__ == "__main__":
    main()