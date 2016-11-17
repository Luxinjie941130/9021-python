# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randint

from array_queue import *


dim = 10
grid = [[0] * dim for i in range(dim)]

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()

def leftmost_longest_path_from_top_left_corner():
    x = 0
    y = 0
    
    L = grid
    start = L[x][y]
    ans = []
    if start == 0:
        return None
    
    l = []
    l.append((x, y))
    paths = ArrayQueue()
    paths.enqueue(l)
    while not paths.is_empty():
        t = list(paths.peek_at_front())
        x = t[-1][0]
        y = t[-1][1]
        if len(t) > 1:
            x1 = t[-2][0]
            y1 = t[-2][1]
        else:
            x1 = -1
            y1 = 0
        p = paths.dequeue()
        check = []

        if x - x1 == 1: # direction is down, the leftmost is right, down, left
            # right
            if y+1 < dim and L[x][y+1] == 1:
                temp = t.copy()
                if (x, y+1) not in temp:
                    temp.append((x, y+1))
                    paths.enqueue(temp)
                    check.append('r')
            # down
            if x+1 < dim and L[x+1][y] == 1:
                temp = t.copy()
                if (x+1, y) not in temp:
                    temp.append((x+1, y))
                    paths.enqueue(temp)
                    check.append('d')
            # left
            if y-1 >= 0 and L[x][y-1] == 1:
                temp = t.copy()
                if (x, y-1) not in temp:
                    temp.append((x, y-1))
                    paths.enqueue(temp)
                    check.append('l')
        
        if x1 - x == 1: # direction is up, the leftmost is left, up, right
            # left
            if y-1 >= 0 and L[x][y-1] == 1:
                temp = t.copy()
                if (x, y-1) not in temp:
                    temp.append((x, y-1))
                    paths.enqueue(temp)
                    check.append('l')
            # up
            if x-1 >= 0 and L[x-1][y] == 1:
                temp = t.copy()
                if (x-1, y) not in temp:
                    temp.append((x-1, y))
                    paths.enqueue(temp)
                    check.append('u')
            # right
            if y+1 < dim and L[x][y+1] == 1:
                temp = t.copy()
                if (x, y+1) not in temp:
                    temp.append((x, y+1))
                    paths.enqueue(temp)
                    check.append('r')
        
        if y - y1 == 1: # direction is right, the leftmost is up, right, down
            # up
            if x-1 >= 0 and L[x-1][y] == 1:
                temp = t.copy()
                if (x-1, y) not in temp:
                    temp.append((x-1, y))
                    paths.enqueue(temp)
                    check.append('u')
            # right
            if y+1 < dim and L[x][y+1] == 1:
                temp = t.copy()
                if (x, y+1) not in temp:
                    temp.append((x, y+1))
                    paths.enqueue(temp)
                    check.append('r')           
            # down
            if x+1 < dim and L[x+1][y] == 1:
                temp = t.copy()
                if (x+1, y) not in temp:
                    temp.append((x+1, y))
                    paths.enqueue(temp)
                    check.append('d')
        if y1 - y == 1: # direction is left, the leftmost is down, left, up          
            # down
            if x+1 < dim and L[x+1][y] == 1:
                temp = t.copy()
                if (x+1, y) not in temp:
                    temp.append((x+1, y))
                    paths.enqueue(temp)
                    check.append('d')
            # left
            if y-1 >= 0 and L[x][y-1] == 1:
                temp = t.copy()
                if (x, y-1) not in temp:
                    temp.append((x, y-1))
                    paths.enqueue(temp)
                    check.append('l')
            # up
            if x-1 >= 0 and L[x-1][y] == 1:
                temp = t.copy()
                if (x-1, y) not in temp:
                    temp.append((x-1, y))
                    paths.enqueue(temp)
                    check.append('u')

        if check == []:
            if len(p) > len(ans):
               ans = p
    return ans
    

provided_input = input('Enter one integer: ')
try:
    seed_arg = int(provided_input)
except:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/2 to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = randint(0, 1)
print('Here is the grid that has been generated:')
display_grid()

path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner')
else:
    print('The leftmost longest path from the top left corner is {}'.format(path))
           
