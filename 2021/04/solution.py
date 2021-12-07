#!/usr/bin/env python

import time
import numpy as np
import re

# matrix(board, row, column)




def load_input_data():
    with open("input") as input_file:
        input_temp = input_file.read()
        input_temp = input_temp.strip()
        input_data = input_temp.split('\n')

    # Find number of boards
    n_boards = int((len(input_data)-1)/6)

    bingo_boards = np.empty([n_boards, 5, 5], dtype=float)
    
    board_cnt = -1
    for i_line in range(len(input_data)):

        if i_line == 0:
            bingo_numbers = input_data[i_line].split(',')  

        elif ( (i_line-1) % 6) == 0:
            board_cnt += 1

        else:
            current_row = (i_line-2) % 6
            #row_vals = input_data[i_line].split(' ')
            row_vals = re.split("(?<=\\S) ", input_data[i_line])

            for i_col in range(len(row_vals)):
                bingo_boards[board_cnt, current_row, i_col] = int(row_vals[i_col])

    return bingo_numbers, bingo_boards

def calculate_winning_board(bingo_numbers, bingo_boards):
    
    quit = 0

    # For each input number
    for bingoLetter in bingo_numbers:

        # Set val for for each number
        for bingoCard in range(bingo_boards.shape[0]):
            for row in range(bingo_boards.shape[1]):
                for col in range(bingo_boards.shape[2]):

                    if quit != 1:

                        if bingo_boards[bingoCard, row, col] == float(bingoLetter):
                            bingo_boards[bingoCard, row, col] = np.nan

                            # Determine BINGO!
                            for bingoCard in range(bingo_boards.shape[0]):

                                # Check for rows
                                for row in range(bingo_boards.shape[1]):
                                    if np.all(np.isnan(bingo_boards[bingoCard, row, :])):
                                        winner = bingo_boards[bingoCard, :, :]
                                        bingoNum = float(bingoLetter)
                                        quit = 1
                                        break

                                # Check for cols
                                for col in range(bingo_boards.shape[2]):
                                    if np.all(np.isnan(bingo_boards[bingoCard, :, col])):
                                        winner = bingo_boards[bingoCard, :, :]
                                        bingoNum = float(bingoLetter)
                                        quit = 1
                                        break

    boardSum = np.nansum(winner)   

    return int(boardSum * bingoNum)                
    
def calculate_last_board_to_win(bingo_numbers, bingo_boards):
    
    quit = [1] * bingo_boards.shape[0]
    bingoNum = np.nan

    # For each input number
    for bingoLetter in bingo_numbers:

        # Set val for for each number
        for bingoCard in range(bingo_boards.shape[0]):
            for row in range(bingo_boards.shape[1]):
                for col in range(bingo_boards.shape[2]):

                    if sum(quit) != 0:

                        if bingo_boards[bingoCard, row, col] == float(bingoLetter):
                            bingo_boards[bingoCard, row, col] = np.nan

                            # Determine BINGO!
                            for bingoCard in range(bingo_boards.shape[0]):

                                # Check for rows
                                for row in range(bingo_boards.shape[1]):
                                    if np.all(np.isnan(bingo_boards[bingoCard, row, :])):
                                        quit[bingoCard] = 0

                                        if sum(quit) == 0 and np.isnan(bingoNum):
                                            winner = bingo_boards[bingoCard, :, :]
                                            bingoNum = float(bingoLetter)
                                        
                                        break

                                # Check for cols
                                for col in range(bingo_boards.shape[2]):
                                    if np.all(np.isnan(bingo_boards[bingoCard, :, col])):
                                        
                                        quit[bingoCard] = 0

                                        if sum(quit) == 0 and np.isnan(bingoNum):
                                            winner = bingo_boards[bingoCard, :, :]
                                            bingoNum = float(bingoLetter)

                                        break

    boardSum = np.nansum(winner)   

    return int(boardSum * bingoNum)                  
    

def main():

    start_time = time.time()

    bingo_numbers, bingo_boards = load_input_data()

    print("Day 4, Part 1")
    print(calculate_winning_board(bingo_numbers, bingo_boards))

    print("Day 4, Part 2")
    print(calculate_last_board_to_win(bingo_numbers, bingo_boards))

    print("--- %s seconds ---\n" % (time.time() - start_time))
    
if __name__ == "__main__":
    main()