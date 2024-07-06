class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None
    
    def size(self):
        count = 0
        temp = self.front

        while temp != None:
            count += 1
            temp = temp.next
        return count 
    
    def front_item(self):
        if self.front == None:
            return "Empty"
        else:
            self.front.data

    def rear_item(self):
        if self.rear == None:
            return "Empty"
        else:
            self.rear.data
    
    def enqueue(self, value):
        new_node = Node(value)

        # if queue is empty right now
        if self.front == None and self.rear == None:
            self.front = new_node   
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):

        if self.front == None:
            return "Empty"
        else:
            self.front = self.front.next

    def traverse(self):
        temp = self.front

        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next 

q = Queue()

q.enqueue(4)
q.enqueue(3)
q.enqueue(2)

# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.traverse()

# print(q.isEmpty())
print(q.size())