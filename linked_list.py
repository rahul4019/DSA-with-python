class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        # create a empty linked list
        self.head = None
        self.n = 0
    
    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        # create a new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head

        # reassign head
        self.head = new_node

        # increment n
        self.n += 1

L = Linkedlist() 
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
print(len(L))   

 
