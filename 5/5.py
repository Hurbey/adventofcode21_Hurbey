import numpy as np

def main():

    # Open File
    with open('input.txt') as f:

        # Read lines of file
        lines = f.read().splitlines()

        # Split the Strings and make list into an numpy matrix
        lines = np.asarray([[segments.split(",") for segments in line.split(" -> ")] for line in lines]).astype(int)

        # Make the hydrothermal vents board as numpy matrix
        mat = np.zeros(shape=(np.amax(np.amax(lines, axis=0), axis=0)[1]+1,np.amax(np.amax(lines, axis=0), axis=0)[0]+1))
        
        return [part1(mat, lines), part2(mat, lines)]

def part1(mat, lines):

    for line in lines:

        # only horizontal or vertical
        if 0 in line[:1,:]-line[1:2,:]:

            # add diagonals to matrix
            mat[np.min(line[:,1:2]):np.max(line[:,1:2])+1,np.min(line[:,:1]):np.max(line[:,:1])+1] += 1
            
    # return the amount of values greater 1
    return len(mat[mat > 1])


def part2(mat, lines):

    for line in lines:

        # only diagonals (horizontal and vertical is done in part 1)
        if 0 not in line[:1,:]-line[1:2,:]:

            # Check the direction of diagonals
            if line[1,1] - line[0,1] > 0:
                x = np.arange(line[0,1], line[1,1]+1)
            else:
                x = np.arange(line[0,1], line[1,1]-1, -1)
            if line[1,0] - line[0,0] > 0:
                y = np.arange(line[0,0], line[1,0]+1)
            else:
                y = np.arange(line[0,0], line[1,0]-1, -1)
            
            # add diagonals to matrix
            for i in range(len(x)):
                mat[x[i],y[i]] += 1

    # return the amount of values greater 1
    return len(mat[mat > 1])


if __name__ == "__main__":
    
    ret = main()
    print("Advent of Code Day 5\nPart 1 Result: ", ret[0], "\nPart 2 Result: ", ret[1])