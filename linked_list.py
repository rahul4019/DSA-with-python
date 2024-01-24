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

    def insert_head(self, value):
        # create a new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head

        # reassign head
        self.head = new_node

        # increment n
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''

        while curr != None:
            result += str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

    def append(self, value):
        new_node = Node(value)

        # in case the Linked list is empty
        if self.head == None:
            self.head = new_node
            self.n += 1
            return

        curr = self.head
        while curr.next != None:
            curr = curr.next

        # you are at the last node
        curr.next = new_node
        self.n += 1

    def insert_after(self, after, value):
        new_node = Node(value)

        curr = self.head

        while (curr != None):
            if curr.data == after:
                break
            curr = curr.next

        # case 1 -> item not found
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
        # case 2 -> item not found
        else:
            print('Item not found')
            return 


L = Linkedlist()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
print(len(L))
# L.append(5)
L.insert_after(1, 200)
print(L)
