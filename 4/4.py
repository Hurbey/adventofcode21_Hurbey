import numpy as np
from itertools import groupby

def main():

    # Open File
    with open('input.txt') as f:

        # Read lines of file
        lines = f.read().splitlines()
        lines = [list(group) for k, group in groupby(lines, lambda x: x == "") if not k]

        # select the numbers, matrizes and make a bingo board
        numbers = np.asarray(lines[0][0].split(",")).astype(int)
        matrizes = np.asarray([[row.split() for row in mat ] for mat in lines[1:]]).astype(int)
        bingo = np.zeros(shape=matrizes.shape)

        # calculate the results
        part1_result = part1_recursive_numberpick(matrizes, bingo, numbers)
        part2_result = part2_recursive_numberpick(matrizes, bingo, numbers)

        return [part1_result,part2_result]


def part2_recursive_numberpick(matrizes, bingo, numbers):

    # save if all matrizes are removed
    tmp_mat = matrizes

    # set chosen bingo value to 1. Needed for possible diagonals
    bingo[matrizes == numbers[0]] = 1
    
    # Check wether columns hit bingo
    if np.where(bingo.sum(axis=1) == 5)[0].size != 0:
        matrizes[bingo == 1] = 0
        matrizes = np.delete(matrizes, np.where(bingo.sum(axis=1) == 5)[0], axis=0)
        bingo = np.delete(bingo, np.where(bingo.sum(axis=1) == 5)[0], axis=0)

    # Check wether rows hit bingo
    elif np.where(bingo.sum(axis=2) == 5)[0].size != 0:
        matrizes[bingo == 1] = 0
        matrizes = np.delete(matrizes, np.where(bingo.sum(axis=2) == 5)[0], axis=0)
        bingo = np.delete(bingo, np.where(bingo.sum(axis=2) == 5)[0], axis=0)

    # diagonals
    # elif np.where(bingo.diagonal(axis1=1, axis2=2).sum(axis=1) == 5)[0].size != 0:
    #     return -1
    # elif np.where(np.fliplr(bingo).diagonal(axis1=1, axis2=2).sum(axis=1) == 5)[0].size != 0:
    #     return -2
    
    # if size is zero, take the first saved one
    if matrizes.size == 0:
        return tmp_mat[0].sum() * numbers[0]

    return part2_recursive_numberpick(matrizes, bingo, numbers[1:])


def part1_recursive_numberpick(matrizes, bingo, numbers):

    # set chosen bingo value to 1. Needed for possible diagonals
    bingo[matrizes == numbers[0]] = 1
    
    # Check wether columns hit bingo
    if np.where(bingo.sum(axis=1) == 5)[0].size != 0:
        matrizes[bingo == 1] = 0
        return matrizes[np.where(bingo.sum(axis=1) == 5)[0][0]].sum() * numbers[0]

    # Check wether rows hit bingo
    elif np.where(bingo.sum(axis=2) == 5)[0].size != 0:
        matrizes[bingo == 1] = 0
        return matrizes[np.where(bingo.sum(axis=2) == 5)[0][0]].sum() * numbers[0]

    # diagonals
    # elif np.where(bingo.diagonal(axis1=1, axis2=2).sum(axis=1) == 5)[0].size != 0:
    #     return -1
    # elif np.where(np.fliplr(bingo).diagonal(axis1=1, axis2=2).sum(axis=1) == 5)[0].size != 0:
    #     return -2

    return part1_recursive_numberpick(matrizes, bingo, numbers[1:])


if __name__ == "__main__":
    
    ret = main()
    print("Advent of Code Day 4\nPart 1 Result: ", ret[0], "\nPart 2 Result: ", ret[1])