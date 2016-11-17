# Creates 3 classes, Point, Line and Parallelogram.
# A point is determined by 2 coordinates (int or float).
# A line is determined by 2 distinct points.
# A parallelogram is determined by 4 distint lines,
# two of which having the same slope, the other two having the same slope too.
# The Parallelogram has a method, divides_into_two_parallelograms(), that determines
# where a line, provide as arguments, can split the object into two smaller parallelograms.
#
# Written by *** for COMP9021


from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Line:
    def __init__(self, pt_1,pt_2):
        self.pt_1 = Point(pt_1.x, pt_1.y)
        self.pt_2 = Point(pt_2.x, pt_2.y)
        if pt_1.x == pt_2.x and pt_1.y == pt_2.y:
            print('Cannot create line')
        else:
            if pt_2.x - pt_1.x == 0:
                self.a = None
                self.b = None   
            else:
                self.a = (pt_2.y - pt_1.y) / (pt_2.x - pt_1.x)
                self.b = pt_1.y - self.a * pt_1.x

            
            

class Parallelogram:
    def __init__(self,l1,l2,l3,l4):
        self.l1 = Line(l1.pt_1,l1.pt_2)
        self.l2 = Line(l2.pt_1,l2.pt_2)
        self.l3 = Line(l3.pt_1,l3.pt_2)
        self.l4 = Line(l4.pt_1,l4.pt_2)

        if self.get_ds() == False:
            print('Cannot creat parallelogram')
        
            
    def get_ds(self):
        d1 = []
        d2 = []
        d3 = []
        d4 = []
        if self.l1.a == self.l2.a and self.l3.a == self.l4.a and self.l1.a != self.l3.a and self.l1.b != self.l2.b and self.l3.b != self.l4.b:
            d1.append(self.l1.a)
            d1.append(self.l1.b)
            d2.append(self.l2.a)
            d2.append(self.l2.b)
            d3.append(self.l3.a)
            d3.append(self.l3.b)
            d4.append(self.l4.a)
            d4.append(self.l4.b)
            return d1, d2, d3, d4
        if self.l1.a == self.l2.a == None and self.l3.a == self.l4.a and self.l1.a != self.l3.a and  self.l3.b != self.l4.b:
            d1.append(self.l1.a)
            d1.append(self.l1.b)
            d2.append(self.l2.a)
            d2.append(self.l2.b)
            d3.append(self.l3.a)
            d3.append(self.l3.b)
            d4.append(self.l4.a)
            d4.append(self.l4.b)
            return d1, d2, d3, d4
        if self.l1.a == self.l3.a and self.l2.a == self.l4.a and self.l1.a != self.l2.a and self.l1.b != self.l3.b and self.l2.b != self.l4.b:
            d1.append(self.l1.a)
            d1.append(self.l1.b)
            d2.append(self.l3.a)
            d2.append(self.l3.b)
            d3.append(self.l2.a)
            d3.append(self.l2.b)
            d4.append(self.l4.a)
            d4.append(self.l4.b)
            return d1, d2, d3, d4
        if self.l1.a == self.l3.a == None and self.l2.a == self.l4.a and self.l1.a != self.l2.a and  self.l2.b != self.l4.b:
            d1.append(self.l1.a)
            d1.append(self.l1.b)
            d2.append(self.l3.a)
            d2.append(self.l3.b)
            d3.append(self.l2.a)
            d3.append(self.l2.b)
            d4.append(self.l4.a)
            d4.append(self.l4.b)
            return d1, d2, d3, d4
        if self.l1.a == self.l4.a and self.l2.a == self.l3.a and self.l1.a != self.l2.a and self.l1.b != self.l4.b and self.l2.b != self.l3.b:
            d1.append(self.l1.a)
            d1.append(self.l1.b)
            d2.append(self.l4.a)
            d2.append(self.l4.b)
            d3.append(self.l3.a)
            d3.append(self.l3.b)
            d4.append(self.l2.a)
            d4.append(self.l2.b)
            return d1, d2, d3, d4
        if self.l1.a == self.l4.a == None and self.l2.a == self.l3.a and self.l1.a != self.l2.a and self.l2.b != self.l3.b:
            d1.append(self.l1.a)
            d1.append(self.l1.b)
            d2.append(self.l4.a)
            d2.append(self.l4.b)
            d3.append(self.l3.a)
            d3.append(self.l3.b)
            d4.append(self.l2.a)
            d4.append(self.l2.b)
            return d1, d2, d3, d4
        if self.l2.a == self.l3.a == None and self.l1.a == self.l4.a and self.l2.a != self.l1.a and self.l1.b != self.l4.b:
            d1.append(self.l2.a)
            d1.append(self.l2.b)
            d2.append(self.l3.a)
            d2.append(self.l3.b)
            d3.append(self.l1.a)
            d3.append(self.l1.b)
            d4.append(self.l4.a)
            d4.append(self.l4.b)
            return d1,d2,d3,d4
        if self.l2.a == self.l4.a == None and self.l1.a == self.l3.a and self.l2.a != self.l1.a and self.l1.b != self.l3.b:
            d1.append(self.l2.a)
            d1.append(self.l2.b)
            d2.append(self.l4.a)
            d2.append(self.l4.b)
            d3.append(self.l1.a)
            d3.append(self.l1.b)
            d4.append(self.l3.a)
            d4.append(self.l3.b)
            return d1,d2,d3,d4
        if self.l3.a == self.l4.a == None and self.l1.a == self.l2.a and self.l3.a != self.l1.a and self.l1.b != self.l2.b:
            d1.append(self.l3.a)
            d1.append(self.l3.b)
            d2.append(self.l4.a)
            d2.append(self.l4.b)
            d3.append(self.l1.a)
            d3.append(self.l1.b)
            d4.append(self.l2.a)
            d4.append(self.l2.b)
            return d1,d2,d3,d4
        
        else:
            print('Cannot create parallelogram')
        
    # Replace pass above with your code

    def divides_into_two_parallelograms(self, line):

        ds= self.get_ds()
        #print(line.a)
        #print(line.b)
        d1 = ds[0]
        d2 = ds[1]
        d3 = ds[2]
        d4 = ds[3]
        if line.a == d1[0] != None and line.b > min(d1[1],d2[1]) and line.b < max(d1[1],d2[1]):
            print('True')
        elif line.a == d1[0] == None and line.pt_1.x > min(l1.pt_1.x,l2.pt_1.x) and line.pt_1.x < max(l1.pt_1.x,l2.pt_1.x):
            print('True')
        elif line.a == d1[0] == None and line.pt_1.x > min(l1.pt_1.x,l3.pt_1.x) and line.pt_1.x < max(l1.pt_1.x,l3.pt_1.x):
            print('True')
        elif line.a == d1[0] == None and line.pt_1.x > min(l1.pt_1.x,l4.pt_1.x) and line.pt_1.x < max(l1.pt_1.x,l4.pt_1.x):
            print('True')
        elif line.a == d1[0] == None and line.pt_1.x > min(l2.pt_1.x,l3.pt_1.x) and line.pt_1.x < max(l2.pt_1.x,l3.pt_1.x):
            print('True')
        elif line.a == d1[0] == None and line.pt_1.x > min(l2.pt_1.x,l4.pt_1.x) and line.pt_1.x < max(l2.pt_1.x,l4.pt_1.x):
            print('True')
        elif line.a == d1[0] == None and line.pt_1.x > min(l3.pt_1.x,l4.pt_1.x) and line.pt_1.x < max(l3.pt_1.x,l4.pt_1.x):
            print('True')
        elif line.a == d3[0] and line.b > min(d3[1],d4[1]) and line.b < max(d3[1],d4[1]):
            print('True')
        else:
            print('False')

