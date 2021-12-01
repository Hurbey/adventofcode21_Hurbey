import numpy as np

def part1():
    # Open File
    with open('input.txt') as f:

        # Read lines of file
        lines = f.readlines()

        # rewrite read lines to numpy array as integers
        lines = np.asarray([int(line.rstrip('\n')) for line in lines])

        # return the sum of positive differences of the windows with the shifted windows
        return ((lines - np.roll(lines, 1))[1:] > 0).sum()


def part2():
    # Open File
    with open('input.txt') as f:

        # Read lines of file
        lines = f.readlines()

        # rewrite read lines to numpy array as integers
        lines = np.asarray([int(line.rstrip('\n')) for line in lines])

        # calculate the three-measurement windows
        lines = (lines + np.roll(lines,1) + np.roll(lines,2))[2:]

        # return the sum of positive differences of the three-measurement windows with the shifted windows
        return ((lines - np.roll(lines, 1))[1:] > 0).sum()


if __name__ == "__main__":
    print("Advent of Code Day 1 Part 1 Result: ", part1())
    print("Advent of Code Day 1 Part 2 Result: ", part2())