# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the number of blocks
# in the largest block construction, determined by rows of 1s that can be stacked
# on top of each other. 
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()


def size_of_largest_construction():

    L = grid
    
    L1 = []
    L2 = []
    count = 0

    for m in range(len(L)-1,-1,-1):
        i = m
        for j in range(len(L)):
            while L[i][j] > 0:
                count += 1
                i -= 1
                if i == -1:
                    break
            L2.append(count)
            count = 0
            i = m
        L1.append(L2)
        L2 = []
    #print(L1)


    L3 = []
    L4 = []
    x = 0
    for n in range(len(L)):
        for m in range(len(L1)):
            if L1[n][m] != 0:
                x += L1[n][m]
                if m == len(L) - 1:
                    L4.append(x)
                    x = 0
            else:
                L4.append(x)
                x = 0
        L3.append(L4)
        L4 = []
        #print(L3)


    y = 0
    z = 0
    L5 = []
    for y in L3:
        L5.append(max(y))
    #print(L5)
    #print(max(L5))
    size_of_largest_construction = max(L5)
    return(size_of_largest_construction)

    
        

    # Replace pass above with your code


# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
def construction_size(i, j1, j2):
    pass
    # Replace pass above with your code

            
try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) for _ in range(dim)] for _ in range(dim)]
#print(grid)
print('Here is the grid that has been generated:')
display_grid()
print('The largest block construction has {} blocks.'.format(size_of_largest_construction()))  
