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

L = Linkedlist() 
print(len(L))   

 
