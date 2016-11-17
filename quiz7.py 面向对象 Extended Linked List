# Written by *** for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):

        L = LinkedList.duplicate(self)
        LL = ExtendedLinkedList()
        le = LinkedList.__len__(self)
        head_value = LinkedList.value_at(self,le//2)
        head_index = le // 2
        LL.append(head_value)


        for i in range(1,le//2 +1):
            l = L.__len__()
            head_index = l // 2
            left_node_index = head_index - 1
            left_node_value = L.value_at(left_node_index)
            LL.append(left_node_value)
            right_node_index = head_index + 1
            right_node_value = L.value_at(right_node_index)
            LL.append(right_node_value)
            L.delete_value(left_node_value)
            L.delete_value(right_node_value)


        n = LL.head
        n1 = self.head
        for i in range(self.__len__()):
            n1.value = n.value
            n1 = n1.next_node
            n = n.next_node
            
            
            

                
        




        



    
    
    
    
