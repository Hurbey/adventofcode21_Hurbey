import numpy as np

def part1():

    # Open File
    with open('input.txt') as f:

        # Read lines of file
        lines = [[line.split(" ")[:-5], line.split(" ")[-4:]] for line in f.read().splitlines()]

        d = 0
        for line in lines:
            for strng in line[1]:
                if len(strng) == 2 or len(strng) == 4 or len(strng) == 3 or len(strng) == 7:
                    d += 1

        
        return d


def part2():

    # Open File
    with open('input.txt') as f:

        # Read lines of file
        lines = [[line.split(" ")[:-5], line.split(" ")[-4:]] for line in f.read().splitlines()]
        d = 0
        dec = decode(lines[0])
        number = []

        for line in lines:
            dec = decode(line)
            lst = []
            for x in line[1]:
                lst.append(dec[''.join(sorted(x))])

            number.append(lst[0]*1000 + lst[1]*100 + lst[2]*10 + lst[3])

        return sum(number)
        

def decode(x):
    dec = ["0","1","2","3","4","5","6","7","8","9"]

    for strng in x[0]:
        if len(strng) == 2:
            dec[1] = strng
        elif len(strng) == 3:
            dec[7] = strng
        elif len(strng) == 4:
            dec[4] = strng
        elif len(strng) == 7:
            dec[8] = strng


    for strng in x[0]:
        if len(strng) == 5 and dec[7][0] in strng and dec[7][1] in strng and dec[7][2] in strng:
            dec[3] = strng
        elif len(strng) == 5:
            d = 0
            if dec[4][0] in strng:
                d += 1
            if dec[4][1] in strng:
                d += 1
            if dec[4][2] in strng:
                d += 1
            if dec[4][3] in strng:
                d += 1
            if d == 3:
                dec[5] = strng
            else:
                dec[2] = strng

    for strng in x[0]:
        if len(strng) == 6 and dec[3][0] in strng and dec[3][1] in strng and dec[3][2] in strng and dec[3][3] in strng and dec[3][4] in strng:
            dec[9] = strng
        elif len(strng) == 6 and dec[5][0] in strng and dec[5][1] in strng and dec[5][2] in strng and dec[5][3] in strng and dec[5][4] in strng:
            dec[6] = strng
        
    for strng in x[0]:
        if strng not in dec:
            dec[0] = strng
    

    return {''.join(sorted(dec[i])) : i for i in range(0, len(dec))}


if __name__ == "__main__":
    print("Advent of Code Day 8\nPart 1 Result: ", int(part1()), "\nPart 2 Result: ", int(part2()))