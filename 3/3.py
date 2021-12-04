import numpy as np

def main():

    # Open File
    with open('input.txt') as f:

        # Read lines of file
        lines = f.read().splitlines()
        
        # Make list into an numpy matrix
        lines = np.asarray([[char for char in word] for word in lines]).astype(int)

        # PART 1: Calculate the gamma and epsilon rate
        gamma_rate = np.where(lines.sum(axis=0) < lines.shape[0]/2, 0, 1)
        epsilon_rate = np.where(lines.sum(axis=0) < lines.shape[0]/2, 1, 0)
        
        # PART 2: Recursive function to calculate oxygen and co2scrubber
        oxygen = oxygen_criteria(lines, 0)
        co2scrubber = co2scrubber_criteria(lines, 0)

        # Return Part1: the product of the gamma_rate and epsilon_rate 
        # Return Part2: the product of oxygen and co2scrubber
        return [(2**np.arange(gamma_rate.shape[0]-1, -1, -1) * gamma_rate).sum() * (2**np.arange(epsilon_rate.shape[0]-1, -1, -1) * epsilon_rate).sum(), 
                (2**np.arange(oxygen.shape[0]-1, -1, -1) * oxygen).sum() * (2**np.arange(co2scrubber.shape[0]-1, -1, -1) * co2scrubber).sum()]

def co2scrubber_criteria(x, d):

    # Calculate the epsilon rate for current input
    epsilon_rate = np.where(x.sum(axis=0) < x.shape[0]/2, 1, 0)

    if(len(x) == 1):

        # Return if length of the current input is onea
        return x[0]

    else:

        # Recursive call of co2scrubber function
        return co2scrubber_criteria(np.delete(x, np.where(x[:,d:d+1] != epsilon_rate[d])[0], axis = 0), d+1)
        


def oxygen_criteria(x, d):

    # Calculate the epsilon rate for current input
    gamma_rate = np.where(x.sum(axis=0) < x.shape[0]/2, 0, 1)

    if(len(x) == 1):

        # Return if length of the current input is onea
        return x[0]

    else:

        # Recursive call of oxygen function
        return oxygen_criteria(np.delete(x, np.where(x[:,d:d+1] != gamma_rate[d])[0], axis = 0), d+1)




if __name__ == "__main__":

    ret = main()
    print("Advent of Code Day 3\nPart 1 Result: ", ret[0], "\nPart 2 Result: ", ret[1])