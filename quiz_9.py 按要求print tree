# Randomly generates a binary search tree with values from 0 up to 9, and displays it growing up.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
from binary_tree import *

def print_tree_growing_down(tree):
    if tree.value == None:
        return
    height = tree.height()
    for n in range(height,-1,-1):
        print_row(tree, 0, n, height)
        print()


def print_row(tree, i, n, height):
    if i == n:
        if tree == None or tree.value == None:
            print(' ' * (2 ** (height - n + 1) - 1), end = '')
        else:
            print(' ' * (2 ** (height - n) - 1), end = '')
            print(tree.value, end = '')
            print(' ' * (2 ** (height - n) - 1), end = '')
    else:
        if tree == None:
            print_row(None, i + 1, n, height)
            print(' ', end = '')
            print_row(None, i + 1, n, height)
        else:
            print_row(tree.left_node, i + 1, n, height)
            print(' ', end = '')
            print_row(tree.right_node, i + 1, n, height)   
    
       

provided_input = input('Enter two integers, with the second one between 0 and 10: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    seed_arg = int(provided_input[0])
    nb_of_nodes = int(provided_input[1])
    if nb_of_nodes < 0 or nb_of_nodes > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
data_pool = list(range(nb_of_nodes))
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = choice(data_pool)
    tree.insert_in_bst(datum)
    data_pool.remove(datum)
print_tree_growing_down(tree)
           
