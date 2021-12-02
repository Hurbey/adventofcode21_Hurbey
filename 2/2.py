import numpy as np
import pandas as pd

def part1():
    # Read txt file as csv
    df = pd.read_csv("input.txt", sep = " ", header=None)

    # Return [sum of forward steps * (sum of down steps - sum of up steps)]
    return df.loc[df[0] == "forward"][1].sum() *(df.loc[df[0] == "down"][1].sum() - df.loc[df[0] == "up"][1].sum())

def part2():
    # Read txt file as csv
    df = pd.read_csv("input.txt", sep = " ", header=None)

    # Change sign of up direction
    df.loc[df[0] == "up"] = df.loc[df[0] == "up"] * -1

    # Add column of current aim
    df["aim"] = df.loc[df[0] != "forward"][1].cumsum()

    # Fill the NaN with the current aim
    df.fillna(method='ffill', inplace=True)

    # calculate the current depths
    df["depth"] = df.loc[df[0] == "forward"][1] * df.loc[df[0] == "forward"]["aim"]

    # Return the product of final horizontal position and final depth
    return df["depth"].sum() * df.loc[df[0] == "forward"][1].sum()


if __name__ == "__main__":
    print("Advent of Code Day 2 Part 1 Result: ", part1())
    print("Advent of Code Day 2 Part 2 Result: ", part2())