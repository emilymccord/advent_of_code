#!/usr/bin/env python

import time
import numpy as np
import re

# REMINDER: matrix(board, row, column)

def load_input_data_as_list():
    with open("input") as input_file:
        input_temp = input_file.read()
        input_temp = input_temp.strip()
        input_data = input_temp.split('\n')
    
        cnt = 0
        x1, x2, y1, y2 = ([0] * len(input_data) for i in range(4))
        for line in input_data:
            split_line = re.split(' -> |,', line)

            x1[cnt] = int(split_line[0])
            y1[cnt] = int(split_line[1])
            x2[cnt] = int(split_line[2])
            y2[cnt] = int(split_line[3])
            cnt += 1
    
    return x1, y1, x2, y2
    

def load_input_data_as_array():

    with open("input") as input_file:
        input_temp = input_file.read()
        input_temp = input_temp.strip()
        input_temp = re.split(' -> |,|\n',input_temp)
        rows = len(input_temp)/4
        
        input_data = input_temp

        int_map = map(int, input_data)
        input_data = list(int_map)
        print(input_data)

    return input_data

def calculate_overlap(x1, y1, x2, y2, diagonal):

    maxX = max(max(x1), max(x2))
    maxY = max(max(y1), max(y2))

    grid = np.zeros((maxX+1, maxY+1))

    for nLine in range(len(x1)):

        x1v = min(x1[nLine], x2[nLine])
        y1v = min(y1[nLine], y2[nLine])
        x2v = max(x1[nLine], x2[nLine])
        y2v = max(y1[nLine], y2[nLine])

        dx = x2v - x1v + 1
        dy = y2v - y1v + 1

        if x2[nLine] ==  x1[nLine]:
            xIncrease = 0
            xSame = 1

        elif x2[nLine] - x1[nLine] > 0:
            xIncrease = 1
            xSame = 0

        else:
            xIncrease = 0
            xSame = 0

        if y2[nLine] ==  y1[nLine]:
            yIncrease = 0
            ySame = 1

        elif y2[nLine] - y1[nLine] > 0:
            yIncrease = 1
            ySame = 0

        else:
            yIncrease = 0
            ySame = 0


        if xSame == 1:
            grid[y1v:(y2v+1), x1v] += 1

        elif ySame == 1:
            grid[y1v, x1v:(x2v+1)] += 1

        elif diagonal == 1:
            xVal = x1[nLine]
            yVal = y1[nLine]

            cnt = 0
            while cnt < dx:
                
                grid[yVal, xVal] += 1
                
                if xIncrease == 1:
                    xVal += 1
                else:
                    xVal -= 1

                if yIncrease == 1:
                    yVal += 1
                else:
                    yVal -= 1

                cnt += 1

    numOverThresh = (grid >= 2).sum()
    return numOverThresh
    

def main():

    start_time = time.time()

    x1, y1, x2, y2 = load_input_data_as_list()

    print("Day 5, Part 1")
    print(calculate_overlap(x1, y1, x2, y2, 0))
    print("Day 5, Part 2")
    print(calculate_overlap(x1, y1, x2, y2, 1))

    print("--- %s seconds ---\n" % (time.time() - start_time))
    
if __name__ == "__main__":
    main()