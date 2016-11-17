# Written by Xinjie LU for COMP9021 Assignment2
# student ID:z5101488

import sys
import copy
import os

if __name__ == '__main__':
    command_line = sys.argv
    expect_commands = [['--file'], ['-print', '--file']]
    if not command_line[1:-1] in expect_commands:
        print('I expect --file followed by filename and possibly -print as command line arguments.')
        sys.exit()
    else:
        if len(command_line) == 3:
            check_print = False
        if len(command_line) == 4:
            check_print = True
f = command_line[-1]

try:
    L = []
    file = open(f)
    for line in file:
        l = []
        for c in line:
            if c.isdigit():
                l.append(int(c))
        if l:
            L.append(l)
    if L == []:
        raise ValueError
        sys.exit()

    if len(L)<2 or len(L[0])<2:
        raise ValueError
    for i in range(len(L)-1):
        if len(L[i])!= len(L[i+1]):
            raise ValueError
    for i in range(len(L)):
        for j in range(len(L[0])):
            if i == len(L) -1:
                if L[i][j] in {2,3}:
                    raise ValueError
            if j == len(L[0]) -1:
                if L[i][j] in {1,3}:
                    raise ValueError
    if len(L) >41 or len(L[0]) >31:
        raise ValueError

except IOError:
    print('Incorrect input.')
    sys.exit()
except ValueError:
    print('Incorrect input.')
    sys.exit()
    
        

#################################gate

gate_list = []
file.close()
for i in range(len(L[0])-1):          ##up
    if L[0][i] == 0 or L[0][i] == 2:
        gate_list.append([0,i])
    
for i in range(len(L[0])-1):         ##down
    if L[-1][i] == 0:
        gate_list.append([len(L)-2,i])

for i in range(len(L)-1):            ##left
    if L[i][0] == 0 or L[i][0] == 1:
        gate_list.append([i,0])
             
for i in range(len(L)-1):            ##right
    if L[i][-1] == 0:
        gate_list.append([i,len(L[0])-2])




##############################connected-wall
L1 = copy.deepcopy(L)
def wall_count():
    wall_count = 0
    for i in range(len(L1)):
        for j in range(len(L1[0])):
            if L1[i][j]:
                connected_wall(i,j)
                wall_count += 1
    return wall_count

def connected_wall(i,j):
    
    if not L1[i][j]:
        return
    

    if L1[i][j] == 1:
        L1[i][j] = 0
        if i -1 >= 0:
            if L1[i-1][j] in {2,3}:  
                connected_wall(i-1,j)
        if i -1 >= 0 and j + 1 < len(L1[0]) :   
            if L1[i-1][j+1] in{2,3}: 
                connected_wall(i-1,j+1)
        if j + 1 < len(L1[0]):
            if L1[i][j+1] in {1,2,3}: 
                connected_wall(i,j+1)
        if j -1 >= 0:
            if L1[i][j-1] in{1,3}: 
                connected_wall(i,j-1)

            
    if L1[i][j] == 2:
        L1[i][j] = 0
        if i -1 >= 0:
            if L1[i-1][j] == 2: 
                connected_wall(i-1,j)
            if L1[i-1][j] == 3:
                connected_wall(i-1,j)    
        if i + 1 < len(L1) and j - 1 >= 0:
            if L1[i+1][j-1] == 1: 
                connected_wall(i+1,j-1)
            if L1[i+1][j-1] == 3: 
                connected_wall(i+1,j-1)
        if i + 1 < len(L1):
            if L1[i+1][j] == 1: 
                connected_wall(i+1,j)
            if L1[i+1][j] == 2: 
                connected_wall(i+1,j)
            if L1[i+1][j] == 3: 
                connected_wall(i+1,j)
        if j - 1 >= 0:
            if L1[i][j-1] == 1: 
                connected_wall(i,j-1)
            if L1[i][j-1] == 3: 
                connected_wall(i,j-1)

            
    if L1[i][j] == 3:
        L1[i][j] = 0
        if i - 1 >= 0:
            if L1[i-1][j] == 2: 
                connected_wall(i-1,j)
            if L1[i-1][j] == 3: 
                connected_wall(i-1,j)
        if i + 1 <= len(L1):
            if L1[i+1][j] == 1: 
                connected_wall(i+1,j)
            if L1[i+1][j] == 2: 
                connected_wall(i+1,j)
            if L1[i+1][j] == 3: 
                connected_wall(i+1,j)
        if j - 1 >= 0:
            if L1[i][j-1] == 1: 
                connected_wall(i,j-1)
            if L1[i][j-1] == 3: 
                connected_wall(i,j-1)
        if j + 1 < len(L1[0]):
            if L1[i][j+1] == 1: 
                connected_wall(i,j+1)
            if L1[i][j+1] == 2: 
                connected_wall(i,j+1)
            if L1[i][j+1] == 3: 
                connected_wall(i,j+1)
        if i -1 >= 0 and j + 1 <len(L1[0]):
            if L1[i-1][j+1] == 2: 
                connected_wall(i-1,j+1)
            if L1[i-1][j+1] == 3: 
                connected_wall(i-1,j+1)
        if i + 1 < len(L1) and j -1 >=0:
            if L1[i+1][j-1] == 1: 
                connected_wall(i+1,j-1)
            if L1[i+1][j-1] == 3: 
                connected_wall(i+1,j-1)



############################## inner point, accessible area
L3 = copy.deepcopy(L)
for i in range(len(L3)):
    for j in range(len(L3[0])):
        L3[i][j] = 0
for m in gate_list:
    L3[m[0]][m[1]] = 5
row = len(L3) -1
col = len(L3[0]) - 1

count_accessible=0
l4 = []



def convert_0_to_5(i,j):  ######convert accessible area to a distinct number    
    if L[i][j] == 0:
        L3[i][j] = 5
        l4.append((i,j))
        if i - 1 >= 0 and (i-1,j) not in l4:
            convert_0_to_5(i-1,j)
        if i + 1 < row and (i+1,j) not in l4:
            if L[i+1][j] == 0 or L[i+1][j] == 2: 
                convert_0_to_5(i+1,j)
        if j - 1 >= 0 and (i,j-1) not in l4:  
            convert_0_to_5(i,j-1)
        if j + 1 < col and (i,j+1) not in l4:
            if L[i][j+1] == 0 or L[i][j+1] == 1:
                convert_0_to_5(i,j+1)

    if L[i][j] == 1:
        L3[i][j] = 5
        l4.append((i,j))
        if i + 1 < row and (i+1,j) not in l4:
            if L[i+1][j] == 0 or L[i+1][j] == 2: 
                convert_0_to_5(i+1,j)
        if j - 1 >= 0 and (i,j-1)not in l4:  
            convert_0_to_5(i,j-1)
        if j + 1 < col and (i,j+1) not in l4:
            if L[i][j+1] == 0 or L[i][j+1] == 1:
                convert_0_to_5(i,j+1)

    if L[i][j] == 2:
        L3[i][j] = 5
        l4.append((i,j))
        if i - 1 >= 0 and (i-1,j) not in l4: 
            convert_0_to_5(i-1,j)
        if i + 1 < row and (i+1,j) not in l4:
           if L[i+1][j] == 0 or L[i+1][j] == 2: 
                convert_0_to_5(i+1,j)
        if j + 1 < col and (i,j+1) not in l4:
           if L[i][j+1] == 0 or L[i][j+1] == 1:
                convert_0_to_5(i,j+1)

    if L[i][j] == 3:
        L3[i][j] = 5
        l4.append((i,j))
        if i + 1 < row and (i+1,j) not in l4:
            if L[i+1][j] == 0 or L[i+1][j] == 2: 
                convert_0_to_5(i+1,j)
        if j + 1 < col and (i,j+1) not in l4:
            if L[i][j+1] == 0 or L[i][j+1] == 1:
                convert_0_to_5(i,j+1)



for i in range(row):         ###accessible
    for j in range(col):
        if L3[i][j] == 5:
            if(i,j) not in l4:
                count_accessible += 1
                convert_0_to_5(i,j)

count_inaccessible = 0
inaccessible = []           ####inaccessible
for i in range(row):
    for j in range(col):
        if L3[i][j] == 0:
            count_inaccessible += 1
            inaccessible.append([i,j])
            

#################################cul-de-sac
row = len(L)
col = len(L[0])
directions = copy.deepcopy(L)

L51 = copy.deepcopy(L)
L52 = copy.deepcopy(L)

def nb_of_directions(L6, i, j):     ###how many paths
    if L3[i][j] == 0:
        L6[i][j] = -2



    if L6[i][j] == 0:
        n = 4
        if L6[i+1][j] == 1 or L6[i+1][j] == 3:
            n -= 1
        if L6[i][j+1] == 2 or L6[i][j+1] == 3:
            n -= 1
        L6[i][j] = n

    elif L6[i][j] == 1:
        L6[i][j] = 3
        if L6[i+1][j] == 1 or L6[i+1][j] == 3:
            L6[i][j] -= 1
        if L6[i][j+1] == 2 or L6[i][j+1] == 3:
            L6[i][j] -= 1

    elif L6[i][j] == 2:
        n = 3
        if L6[i+1][j] == 1 or L6[i+1][j] == 3:
            n -= 1
        if L6[i][j+1] == 2 or L6[i][j+1] == 3:
            n -= 1
        L6[i][j] = n

    elif L6[i][j] == 3:
        n = 2
        if L6[i+1][j] == 1 or L6[i+1][j] == 3:
            n -= 1
        if L6[i][j+1] == 2 or L6[i][j+1] == 3:
            n -= 1
        L6[i][j] = n
        

for i in range(row-1):
    for j in range(col-1):
        nb_of_directions(directions, i, j)
del directions[-1]
for i in range(row-1):
    del directions[i][-1]
    
def check_direction(directions):
    for i in range(row-1):
        for j in range(col-1):
            if directions[i][j] == 1:
                return 1
    return 0

while check_direction(directions): ###### neighbor change
    for i in range(row-1):
        for j in range(col-1):
            if directions[i][j] == 1:
                directions[i][j] = -1
                L52[i][j] = -1

                if L51[i][j] == 0:
                    if i>0 and j>0 and L52[i-1][j] == -1 and L52[i][j+1] in {2, 3, -1} and L52[i+1][j] in {1, 3, -1}:
                        directions[i][j-1] -= 1
                    if i>0 and j>0 and L52[i][j-1] == -1 and L52[i][j+1] in {2, 3, -1} and L52[i+1][j] in {1, 3, -1}:
                        directions[i-1][j] -= 1
                    if 1<j+1<col-1 and i>0 and L52[i][j-1] == -1 and L52[i-1][j] == -1 and L52[i+1][j] in {1, 3, -1}:
                        directions[i][j+1] -= 1
                    if 1<i+1<row-1 and j>0 and L52[i-1][j] == -1 and L52[i][j-1] == -1 and L52[i][j+1] in {2, 3, -1}:
                        directions[i+1][j] -= 1

                if L51[i][j] == 1:
                    if j>0 and L52[i+1][j] in {1, 3, -1} and L52[i][j+1] in {2, 3, -1}:
                        directions[i][j-1] -= 1
                    if j>0 and i+1 < row-1 and L52[i][j-1] == -1 and L52[i][j+1] in {2, 3, -1}:
                        directions[i+1][j] -= 1
                    if 1<j+1 < col-1 and L52[i+1][j] in {1, 3, -1} and L52[i][j-1] == -1:
                        directions[i][j+1] -= 1

                if L51[i][j] == 2:
                    if i > 0 and L52[i][j+1] in {2, 3, -1} and L52[i+1][j] in {1, 3, -1}:
                        directions[i-1][j] -= 1
                    if i > 0 and i+1 < row-1 and L52[i-1][j] == -1 and L52[i][j+1] in {2, 3, -1}:
                        directions[i+1][j] -= 1
                    if i > 0 and j+1 < col-1 and L52[i-1][j] == -1 and L52[i+1][j] in {1, 3, -1}:
                        directions[i][j+1] -= 1
                        

                if L51[i][j] == 3:
                    if L52[i][j+1] in {2, 3, -1} and i+1 < row-1:
                        directions[i+1][j] -= 1
                    if L52[i+1][j] in {1, 3, -1} and j+1 <col-1:
                        directions[i][j+1] -= 1
                        


def new_directions(L6, i, j):   #########convert cul-de-sac to 0 and get new paths
    if i == row-1 or j == col-1:
        return
    
    if L6[i][j] == 0 and directions[i][j] == -1:
        L6[i][j] = -1
        directions[i][j] = 0
        if row == 2:
            if L6[i][j+1] in{0, 1}:
                new_directions(L, i, j+1)
        if i + 1 < row-1:
            if col == 2:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L, i+1, j)
            if 0<j<col-1:
                if L6[i+1][j] in{0, 2}:
                    new_directions(L6, i+1, j)
                new_directions(L6, i, j-1)
            if j + 1 < col-1:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j)
                if L6[i][j+1] in {0, 1}:
                    new_directions(L, i, j+1)
        if 0<i<row-1:
            if col == 2:
                if L6[i+1][j] in{0, 2}:
                    new_directions(L6, i+1, j)
            if 0<j<col-1:
                new_directions(L6, i-1, j)
                new_directions(L6, i, j-1)
            if j + 1 < col-1:
                new_directions(L, i-1, j)
                if L6[i][j+1] in {0, 1}:
                    new_directions(L6, i, j+1)
                    
    if L6[i][j] == 1 and directions[i][j] == -1:
        L6[i][j] = -1
        directions[i][j] = 0
        if row == 2:
            if L6[i][j+1] in {0, 1}:
                new_directions(L6, i, j+1)
        if i + 1 < row-1:
            if col == 2:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j)
            if 0<j<col-1:
                new_directions(L6, i, j-1)
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j)
            if j + 1 < col-1:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j)
                if L6[i][j+1] in {0, 1}:
                    new_directions(L6, i, j+1)
        if 0<i<row-1:
            if col == 2:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j)
            if 0<j<col-1:
                new_directions(L6, i, j-1)
            if j + 1 < col-1:
                if L6[i][j+1] in {0, 1}:
                    new_directions(L, i, j+1)
            
    if L6[i][j] == 2 and directions[i][j] == -1:
        L6[i][j] = -1
        directions[i][j] = 0
        if row == 2:
            if L6[i][j+1] in {0, 1}:
                new_directions(L, i, j+1)
        if i + 1 < row-1:
            if col == 2:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j)
            if 0<j<col-1:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j) 
            if j + 1 < col-1:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j)
                if L6[i][j+1] in {0, 1}:
                    new_directions(L6, i, j+1)
        if 0<i<row-1:
            if col == 2:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j)
            if 0<j<col-1:
                new_directions(L6, i-1, j)
            if j + 1 < col-1:
                new_directions(L6, i-1, j)
                if L6[i][j+1] in {0, 1}:
                    new_directions(L6, i, j+1)
                      
    if L6[i][j] == 3 and directions[i][j] == -1:
        L6[i][j] = -1
        directions[i][j] = 0
        if row == 2:
            if L6[i][j+1] in {0, 1}:
                new_directions(L6, i, j+1)
        if i + 1 < row-1:
            if col == 2:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j)
            if 0<j<col-1:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L, i+1, j) 
            if j + 1 < col:
                if L6[i][j+1] in {0, 1}:
                    new_directions(L6, i, j+1)
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j) 
                
        if 0<i<row-1:
            if col == 2:
                if L6[i+1][j] in {0, 2}:
                    new_directions(L6, i+1, j)
            if j + 1 < col-1:
                if L6[i][j+1] in {0, 1}:
                    new_directions(L6, i, j+1)

nb_of_cul = 0
for i in range(row-1):
    for j in range(col-1):
        if directions[i][j] == -1:
            nb_of_cul += 1
            new_directions(L51, i, j)


############################path
def path_count():
    global gate_list1
    gate_list1 = []
    global count_path
    count_path = 0
    for i in range(len(directions)):
        for j in range(len(directions[0])):
            if [i,j] in gate_list:
                if [i,j] not in gate_list1:
                    if directions[i][j] >2:
                        continue
                    if directions[i][j] == 0:
                        continue
                    if directions[i][j] == -2:
                        continue
                    else:
                        count_path += 1
                        path(i,j)
    return count_path


def path(i,j):          ###########get path without intersections
    global gate_list1
    global count_path
    
    if L[i][j] == 0:
        gate_list1.append([i,j])
        if j + 1 < len(directions[0])and L[i][j+1] in {0,1} and directions[i][j+1] != 0 and [i,j+1] not in gate_list1:
            if directions[i][j+1] >2:
                count_path -=1
                return
            else:
                path(i,j+1)
                
        elif i+1 < len(directions)and L[i+1][j] in {0,2} and directions[i+1][j] != 0 and [i+1,j] not in gate_list1:
            if directions[i+1][j] >2:
                count_path -=1
                return
            else:
                path(i+1,j)
        elif i-1 >= 0 and L[i-1][j] in {0,1,2,3} and directions[i-1][j] != 0 and [i-1,j] not in gate_list1:
            if directions[i-1][j] >2:
                count_path -=1
                return
            else:
                path(i-1,j)
                
        elif j-1 >= 0 and  L[i][j-1] in {0,1,2,3} and directions[i][j-1] != 0 and [i,j-1] not in gate_list1:
            if directions[i][j-1] >2:
                count_path -=1
                return
            else:
                path(i,j-1)




    elif L[i][j] == 1:
        gate_list1.append([i,j])
        if j + 1 < len(directions[0])and L[i][j+1] in {0,1} and directions[i][j+1]!= 0 and [i,j+1] not in gate_list1:
            if directions[i][j+1] >2:
                count_path -=1
                return
            else:
                path(i,j+1)
                
        elif i+1 < len(directions)and L[i+1][j] in {0,2} and directions[i+1][j] != 0 and [i+1,j] not in gate_list1:
            if directions[i+1][j] >2:
                count_path -=1
                return
            else:
                path(i+1,j)
                
        elif j-1 >= 0 and L[i][j-1] in {0,1,2,3} and directions[i][j-1] != 0 and [i,j-1] not in gate_list1:
            if directions[i][j-1] >2:
                count_path -=1
                return
            else:
                path(i,j-1)


    elif L[i][j] == 2:
        gate_list1.append([i,j])
        if j + 1 < len(directions[0])and L[i][j+1] in {0,1} and directions[i][j+1] != 0 and [i,j+1] not in gate_list1:
            if directions[i][j+1] >2:
                count_path -=1
                return
            else:
                path(i,j+1)
                
        elif i+1 < len(directions)and L[i+1][j] in {0,2} and directions[i+1][j] != 0 and [i+1,j] not in gate_list1:
            if directions[i+1][j] >2:
                count_path -=1
                return
            else:
                path(i+1,j)
                
        elif i-1 >=0 and L[i-1][j] in {0,1,2,3} and directions[i-1][j] != 0 and [i-1,j]  not in gate_list1:
              if directions[i-1][j] >2:
                count_path -=1
                return
              else:
                path(i-1,j)

                
        
    elif L[i][j] == 3:
        gate_list1.append([i,j])
        if j + 1 < len(directions[0])and L[i][j+1] in {0,1} and directions[i][j+1] != 0 and [i,j+1] not in gate_list1:
            if directions[i][j+1] >2:
                count_path -=1
                return
            else:
                path(i,j+1)
        elif i+1 <len(directions)and L[i+1][j] in {0,2} and directions[i+1][j] != 0 and [i+1,j] not in gate_list1:
            if directions[i+1][j] >2:
                count_path -=1
                return
            else:
                path(i+1,j)


if check_print == False:
    count_gate = len(gate_list)
    if count_gate == 0:
        print('The maze has no gate.')
    if count_gate == 1:
        print('The maze has a single gate.')
    if count_gate>1:
        print('The maze has {} gates.'.format(count_gate))

    wall_count = wall_count()
    if wall_count == 0:
        print('The maze has no wall.')
    if wall_count == 1:
        print('The maze has a single wall that are all connected.')
    if wall_count >1:
        print('The maze has {} sets of walls that are all connected.'.format(wall_count))

    if count_inaccessible == 0:
        print('The maze has no inaccessible inner point.')
    if count_inaccessible == 1:
        print('The maze has a unique inaccessible inner point.')
    if count_inaccessible > 1:
        print('The maze has {} inaccessible inner points.'.format(count_inaccessible))


    if count_accessible == 0:
        print('The maze has no accessible area.')
    if count_accessible == 1:
        print('The maze has a unique accessible area.')
    if count_accessible >1:
        print('The maze has {} accessible areas.'.format(count_accessible))

    if nb_of_cul == 0:
        print('The maze has no accessible cul-de-sac.')
    if nb_of_cul == 1:
        print('The maze has accessible cul-de-sacs that are all connected.')
    if nb_of_cul > 1:
        print('The maze has {} sets of accessible cul-de-sacs that are all connected.'.format(nb_of_cul))

    count_path = path_count()
    if count_path == 0:
        print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
    if count_path == 1:
        print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
    if count_path > 1:
        print('The maze has {} entry-exit paths with no intersections not to cul-de-sacs.'.format(count_path))

####################################draw
if check_print == True:
    x_axis = []
    y_axis = []

    file = f.replace(".txt",".tex")
    f = open(file,'w')

    for i in range(row):
        for j in range(col):
            if L[i][j] == 1 or L[i][j] == 3:
                x_axis.append([(i,j),(i,j+1)])

    for i in range(row):
        for j in range(col):
            if L[i][j] == 2 or L[i][j] == 3:
                y_axis.append([(i,j),(i+1,j)])

    beginword = "\\documentclass[10pt]{article}\n"\
            "\\usepackage{tikz}\n"\
            "\\usetikzlibrary{shapes.misc}\n"\
            "\\usepackage[margin=0cm]{geometry}\n"\
            "\\pagestyle{empty}\n"\
            "\\tikzstyle{every node}=[cross out, draw, red]\n"\
            "\n"\
            "\\begin{document}\n"\
            "\n"\
            "\\vspace*{\\fill}\n"\
            "\\begin{center}\n"\
            "\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n"\
            "\% Walls\n"
    f.write(beginword)


    x_1 = []                 ##########horizontal wall
    x_2 = []
    for i in range(len(x_axis)):
        x_before = x_axis[i]
        a = 0
        if x_before not in x_2:
            if x_axis[i][1][1]< col:
                if i < len(x_axis)-1:
                    for j in range(i+1,len(x_axis)):
                        x_after = x_axis[j]
                        if x_before[1] == x_after[0]:
                            before = x_before[0]
                            after = x_after[1]
                            x_2.append(x_after)
                            a = 1
                            x_before = [x_before[0],x_after[1]]
                            if j == len(x_axis)-1:
                                f.write('     \\draw ({},{}) -- ({},{});\n'.format(before[1],before[0],after[1],after[0]))
                        else:
                            if a == 0:
                                f.write('     \\draw ({},{}) -- ({},{});\n'.format(x_axis[i][0][1],x_axis[i][0][0],x_axis[i][1][1],x_axis[i][1][0]))
                            else:
                                f.write('     \\draw ({},{}) -- ({},{});\n'.format(before[1],before[0],after[1],after[0]))
                            break
                else:
                    f.write('     \\draw ({},{}) -- ({},{});\n'.format(x_axis[i][0][1],x_axis[i][0][0],x_axis[i][1][1],x_axis[i][0][0]))
            else:
                f.write('     \\draw ({},{}) -- ({},{});\n'.format(x_axis[i][0][1],x_axis[i][0][0],x_axis[i][1][1],x_axis[i][0][0]))
                     

    x_1 = []             ############vertical wall
    x_2 = []
    for i in range(col+1):
        for j in range(len(y_axis)):
            if y_axis[j][0][1] == i:
                y_before = y_axis[j]
                if y_before not in x_2:
                    b = 0
                    a = 0
                    if j < len(y_axis)-1:
                        for m in range(j+1,len(y_axis)):
                            y_after = y_axis[m]
                            if y_before[1] == y_after[0]:
                                before = y_before[0]
                                after = y_after[1]
                                x_2.append(y_after)
                                a = 1
                                y_before = [y_before[0],y_after[1]]
                                if y_after[1][0] == row:
                                    b = 1
                                    f.write('     \\draw ({},{}) -- ({},{});\n'.format(before[1],before[0],after[1],after[0]))
                        if a == 0:
                             f.write('     \\draw ({},{}) -- ({},{});\n'.format(y_axis[j][0][1],y_axis[j][0][0],y_axis[j][1][1],y_axis[j][1][0]))
                        else:
                            if b == 0:
                                f.write('     \\draw ({},{}) -- ({},{});\n'.format(before[1],before[0],after[1],after[0]))
                    else:
                        f.write('     \\draw ({},{}) -- ({},{});\n'.format(y_axis[j][0][1],y_axis[j][0][0],y_axis[j][1][1],y_axis[j][1][0]))
                        

    pillars = []            ########pillars
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == 0:
                if L[i][j-1] in {0,2}:
                    if L[i-1][j] in {0,1}:
                        pillars.append([j,i])

    f.write('\% Pillars\n')
    for i in range(len(pillars)):
        f.write('     \\fill[green] ({},{}) circle(0.2);\n'.format(pillars[i][0],pillars[i][1]))


                            
    inner = []             #########cul-de-sacs
    for i in range(len(directions)):
        for j in range(len(directions[0])):
            if directions[i][j] == 0:
                inner.append([j,i])
        f.write('\% Inner points in accessible cul-de-sacs\n')

    for i in range(len(inner)):
        inner[i][0] += 0.5
        inner[i][1] += 0.5
        f.write('     \\node at ({},{})  '.format(inner[i][0],inner[i][1]) +  '''{}; \n''')



    end = "\\end{tikzpicture}\n"\
      "\\end{center}\n"\
      "\\vspace*{\\fill}\n"\
      "\n"\
      "\\end{document}\n"
    f.write(end)
    f.close()

        
            

    

            
            
    
    
    
    




                
                
                
            
            



        

    
    
            
        
        
        

