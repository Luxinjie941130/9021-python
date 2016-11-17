import re
import string
import copy
from itertools import product

text = ''.join(open(input('Which text file do you want to use for the puzzle?')).readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

####sentences
L = []
for i in sentences:
    l = []
    l.append(i)
    L.append(l)   

####sentences without \n
L2 = [] 
for i in L:
    l2 = []
    for j in i:
        x = j.replace("\n"," ")
        l2.append(x)
        L2.append(l2)

####sentences without punctuation
L21 = []  
for i in L2:
    l21 = []
    for j in i:
        for c in string.punctuation:
            j = j.replace(c," ")
        l21.append(j)
        L21.append(l21)

####split sentences to words
L3 = [] 
for i in L21:
    for j in i:
        x = j.split()
        L3.append(x)
        
####name 
l4 = []
for i in range(len(L3)):
    for j in range(len(L3[i])):
        if L3[i][j] == 'Sir':
            if L3[i][j+1] not in l4:
                l4.append(L3[i][j+1])
        if L3[i][j] == 'Sirs':
            while L3[i][j+1] != 'and':
                if L3[i][j+1] not in {'I','Sir'}:
                    if L3[i][j+1] not in l4:
                        l4.append(L3[i][j+1])
                if L3[i][j+2] == 'and':
                    if L3[i][j+3] not in {'I','Sir'}:
                        if L3[i][j+1] not in l4:
                            l4.append(L3[i][j+3])
                j += 1

l4.sort()
print('The Sirs are:', end = ' ')
for i in l4:
    print(i , end = ' ' )


####useful sentences
L5 = []
for i in L2:
    l5 = []
    for j in i :
        for c in j:
            if c == '"'and j.count(c) == 2 and j not in l5:
                l5.append(j)
            if c == '"' and j.count(c) == 1 and j not in l5:
                j += c
                l5.append(j)
    L5.append(l5)
for i in L5:
    if len(i) == 0:
        L5.remove(i)

####words with quotation mark
L6 = [] 
for i in L5:
    l6 = []
    for j in i:
        l6 = re.findall(r"[\w']+|[.,!?;\"]", j)
    L6.append(l6)

####useful sentences word with quatation
l61 = []
l63 = copy.deepcopy(L6)
for i in range(len(L6)):
    l62 = []
    x = 0
    for j in range(len(L6[i])):
        if L6[i][j] == '"':
            l62.append(L6[i][j])
            x += 1
        if x % 2 == 1:
            l62.append(L6[i][j+1])
    l61.append(l62)
for i in l61:
    if i != []:
        i = i.pop()


####Sir name who said the sentence
l63 = copy.deepcopy(L6)
l65 = []
for i in range(len(l63)):
    l64 = []
    x = 0
    y = 0
    for j in range(len(l63[i])):
        if l63[i][j] == '"':
            x += 1
        if l63[i][j] == 'Sir':
            y = 1
            if x % 2 == 0:
                l64.append(l63[i][j+1])
    l65.append(l64)

####[(['name1'],['word1']),([name2],[word2])]
l7 = [] 
for name in range(len(l65)):
    if name != []:
        l7.append((l65[name],l61[name]))


####truth table:all possibility
l8 = []
l82 = list(product((0,1),repeat = len(l4)))
for i in l82:
    l8.append(list(i))

        
####truth table1:index unchange
####truth table2:remove unsuitable possibility
l81 = copy.deepcopy(l8)
l82 = copy.deepcopy(l8) 

####for every possibility in truth talbe
for possibility in l81:
    for i in range(len(l7)):
        if l7[i][0] != []:
####get the index of speaker
            c  = l4.index(l7[i][0][0])
####get the index of mentioned name
        temp = []
####if 'us' in sentence
        if 'us' in l7[i][1]:
            for name in l4:
                temp.append(l4.index(name))
####if some people in sentence
        else:
            for word in l7[i][1]:
                if word in l4:
                    temp.append(l4.index(word)) 
                if word == 'I': 
                    temp.append(c)

####get the true of false of mentiond people
        temp1 = [] 
        for index in temp:
            temp1.append(possibility[index])
            
#####################################At/at least one of ###############################              
        if 'least' in l7[i][1]: 
            if 'Knight' in l7[i][1]: 
                if possibility[c] == 1:
                    if temp1.count(1) < 1:
                        if possibility in l82:
                            l82.remove(possibility)
                if possibility[c] == 0:
                    if temp1.count(1) >= 1:
                        if possibility in l82:
                            l82.remove(possibility)
            if 'Knave' in l7[i][1]: 
                if possibility[c] == 1:
                    if temp1.count(0) < 1:
                        if possibility in l82:
                            l82.remove(possibility)
                if possibility[c] == 0:
                    if temp1.count(0) >= 1:
                        if possibility in l82:
                            l82.remove(possibility)
                            
#####################################At/at most one of ################################ 
        elif 'most' in l7[i][1]:
            if 'Knight' in l7[i][1]:
                if possibility[c] == 1:
                    if temp1.count(1) > 1:
                        if possibility in l82:
                            l82.remove(possibility)
                if possibility[c] == 0:
                    if temp1.count(1) <= 1:
                        if possibility in l82:
                            l82.remove(possibility)
            if 'Knave' in l7[i][1]:
                if possibility[c] == 1:
                    if temp1.count(0) > 1:
                        if possibility in l82:
                            l82.remove(possibility)
                if possibility[c] == 0:
                    if temp1.count(0) <= 1:
                        if possibility in l82:
                            l82.remove(possibility)
                            
#####################################Exactly/exactly one of ############################
        elif 'exactly' in l7[i][1] or 'Exactly' in l7[i][1]:
            if 'Knight' in l7[i][1]:
                if possibility[c] == 1:
                    if temp1.count(1) != 1:
                        if possibility in l82:
                            l82.remove(possibility)
                if possibility[c] == 0:
                    if temp1.count(1) == 1:
                        if possibility in l82:
                            l82.remove(possibility)
            if 'Knave' in l7[i][1]:
                if possibility[c] == 1:
                    if temp1.count(0) != 1:
                        if possibility in l82:
                            l82.remove(possibility)
                if possibility[c] == 0:
                    if temp1.count(0) == 1:
                        if possibility in l82:
                            l82.remove(possibility)

######################################All/all of us #####################################
        elif 'all' in l7[i][1] or 'All' in l7[i][1]:
            if 'Knights' in l7[i][1]:
                if possibility[c] == 1:
                    if temp1.count(0) != 0:
                        if possibility in l82:
                            l82.remove(possibility)
                if possibility[c] == 0:
                    if temp1.count(0) == 0:
                        if possibility in l82:
                            l82.remove(possibility)
            if 'Knaves' in l7[i][1]:
                if possibility[c] == 1:
                    if temp1.count(1) != 0:
                        if possibility in l82:
                            l82.remove(possibility)
                if possibility[c] == 0:
                    if temp1.count(1) == 0:
                        if possibility in l82:
                            l82.remove(possibility)

#######################################I am ##############################################
        elif 'am' in l7[i][1]:
            if 'Knight' in l7[i][1]:
                if possibility[c] == 1:
                    if temp1[0] != 1:
                        if possibility in l82:
                            l82.remove(possibility)
                if possibility[c] == 0:
                    if temp1[0] != 0:
                        if possibility in l82:
                            l82.remove(possibility)            
            if 'Knave' in l7[i][1]:
                if possibility[c] == 1:
                    if temp1[0] != 0:
                        if possibility in l82:
                            l82.remove(possibility)
                if possibility[c] == 0:
                    if temp1[0] != 1:
                        if possibility in l82:
                            l82.remove(possibility)

#########################################Sir.. or Sir.. is ###############################
        elif 'Knight' in l7[i][1]: 
            if possibility[c] == 1:
                if temp1.count(1) < 1:
                    if possibility in l82:
                        l82.remove(possibility)
            if possibility[c] == 0:
                if temp1.count(1) >= 1:
                    if possibility in l82:
                        l82.remove(possibility)
        elif 'Knave' in l7[i][1]: 
            if possibility[c] == 1:
                if temp1.count(0) < 1:
                    if possibility in l82:
                        l82.remove(possibility)
            if possibility[c] == 0:
                if temp1.count(0) >= 1:
                    if possibility in l82:
                        l82.remove(possibility)
                        
#########################################Sirs are #########################################
        elif 'Knights' in l7[i][1]:
            if possibility[c] == 1:
                if temp1.count(0) != 0:
                    if possibility in l82:
                        l82.remove(possibility)
            if possibility[c] == 0:
                if temp1.count(0) == 0:
                    if possibility in l82:
                        l82.remove(possibility)
        elif 'Knaves' in l7[i][1]:
            if possibility[c] == 1:
                if temp1.count(1) != 0:
                    if possibility in l82:
                        l82.remove(possibility)
            if possibility[c] == 0:
                if temp1.count(1) == 0:
                    if possibility in l82:
                        l82.remove(possibility)


nb_of_answer = len(l82)
if nb_of_answer == 0 or l8 == [[]]:
    print('\nThere is no solution.')
elif nb_of_answer > 1:
    print('\nThere are {} solutions.'.format(nb_of_answer))
elif nb_of_answer == 1:
    print('\nThere is a unique solution:')
    for i in range(len(l82)):
        for j in range(len(l82[i])):
            if l82[i][j] == 1:
                print('Sir {} is a Knight.'.format(l4[j]))
            if l82[i][j] == 0:
                print('Sir {} is a Knave.'.format(l4[j]))
            
                    

                    
                    
                
                
                
                
                
                  
