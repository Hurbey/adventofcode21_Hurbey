import numpy as np

def part1():

    # Open File
    with open('input.txt') as f:
        x = np.asarray([[char for char in line] for line in f.read().splitlines()]).astype(int)

        up = np.roll(x, -1, axis=0)
        down = np.roll(x, 1, axis=0)
        right = np.roll(x, 1, axis=1)
        left = np.roll(x, -1, axis=1)

        up = np.subtract(x,up)
        down = np.subtract(x,down)
        right = np.subtract(x,right)
        left = np.subtract(x,left)

        up[-1] = -1
        down[0] = -1
        right[:,0] = -1
        left[:,-1] = -1

        up = np.where(up < 0, -1, 0)
        down = np.where(down < 0, -1, 0)
        right = np.where(right < 0, -1, 0)
        left = np.where(left < 0, -1, 0)

        mask = np.where((up+down+right+left) == -4, 1, 0)

        return np.sum(mask*(x+1))

def part2():

    # Open File
    with open('input.txt') as f:
        x = np.asarray([[char for char in line] for line in f.read().splitlines()]).astype(int)

        up = np.roll(x, -1, axis=0)
        down = np.roll(x, 1, axis=0)
        right = np.roll(x, 1, axis=1)
        left = np.roll(x, -1, axis=1)

        up = np.subtract(x,up)
        down = np.subtract(x,down)
        right = np.subtract(x,right)
        left = np.subtract(x,left)

        up[-1] = -1
        down[0] = -1
        right[:,0] = -1
        left[:,-1] = -1

        up = np.where(up < 0, -1, 0)
        down = np.where(down < 0, -1, 0)
        right = np.where(right < 0, -1, 0)
        left = np.where(left < 0, -1, 0)

        mask = np.where((up+down+right+left) == -4, 1, 0)

        indexes = np.where(mask==1)

        res = []
        for i in range(len(indexes[0])):
            res.append(len(recursive_test([[indexes[0][i], indexes[1][i]]], x, 0, 0)))

        return np.prod(np.sort(np.asarray(res))[-3:])

def recursive_test(index, x, d, a):
    if d >= len(index):
        return
    # up
    if index[d][0] != 0 and x[index[d][0]-1][index[d][1]] != 9 and not [index[d][0]-1, index[d][1]] in index:
        index.append([index[d][0]-1, index[d][1]])

    # down
    if index[d][0] != len(x)-1 and x[index[d][0]+1][index[d][1]] != 9 and not [index[d][0]+1, index[d][1]] in index:
        index.append([index[d][0]+1, index[d][1]])

    # right
    if index[d][1] != len(x[0])-1 and x[index[d][0]][index[d][1]+1] != 9 and not [index[d][0], index[d][1]+1] in index:
        index.append([index[d][0], index[d][1]+1])

    # left
    if index[d][1] != 0 and x[index[d][0]][index[d][1]-1] != 9 and not [index[d][0], index[d][1]-1] in index:
        index.append([index[d][0], index[d][1]-1])

    d += 1
    recursive_test(index, x, d, a)


    return index




if __name__ == "__main__":
    # part2()
    print("Advent of Code Day 9\nPart 1 Result: ", int(part1()), "\nPart 2 Result: ", int(part2()))