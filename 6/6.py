import numpy as np

def main():

    # Open File
    with open('input.txt') as f:

        # Read lines of file
        fish = np.asarray(f.read().splitlines()[0].split(",")).astype(int)

        # make a numpy array with the amount of fish and their timer value as index
        values, count = np.unique(fish, return_counts=True)
        fish = np.zeros(9)
        fish[values] = count

        return(lanternfish(fish, 0, 80), lanternfish(fish, 0, 256))


def lanternfish(fish, day, end):
    
    if day == end:
        return fish.sum()

    # check how many new fish shall be created
    new_fish = fish[0] 

    # have to set first value to zero because fish who create new fish reset timer to 6 (and not to 8/end of array)
    fish[0] = 0

    # shift the fish
    fish = np.roll(fish, -1)

    # set amount of fish to the 6th(fish who creates new ones) and 8th place(new created fish)
    fish[6] += new_fish
    fish[8] += new_fish

    day += 1

    return lanternfish(fish, day, end)


if __name__ == "__main__":

    ret = main()
    print("Advent of Code Day 6\nPart 1 Result: ", int(ret[0]), "\nPart 2 Result: ", int(ret[1]))