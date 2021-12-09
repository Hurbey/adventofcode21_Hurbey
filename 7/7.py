import numpy as np

def part1():

    # Open File
    with open('input.txt') as f:

        # Read lines of file
        crabs = np.asarray(f.read().splitlines()[0].split(",")).astype(int)

        # Bad initialisation :D
        best_res = 9999999999999999

        for i in range(np.min(crabs), np.max(crabs)):

            res = np.abs(crabs - i).sum()

            if res < best_res:
                best_res = res

        return best_res

def part2():

    # Open File
    with open('input.txt') as f:

        # Read lines of file
        crabs = np.asarray(f.read().splitlines()[0].split(",")).astype(int)

        # Bad initialisation :D
        best_res = 9999999999999999

        for i in range(np.min(crabs), np.max(crabs)):

            res = np.abs(abs((crabs - i)) * (abs(crabs - i) + 1) / 2.).sum()

            if res < best_res:
                best_res = res

        return best_res


if __name__ == "__main__":

    print("Advent of Code Day 7\nPart 1 Result: ", int(part1()), "\nPart 2 Result: ", int(part2()))