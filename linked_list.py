class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Linkedlist:
    def __init__(self):
        # create a empty linked list
        self.head = None
        self.n = 0

    # returns length of lined list
    def __len__(self):
        return self.n

    # inserts the value at 1st postion
    def insert_head(self, value):
        # create a new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head

        # reassign head
        self.head = new_node

        # increment n
        self.n += 1

    # prints the LL
    def __str__(self):
        curr = self.head
        result = ''

        while curr != None:
            result += str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

    # adds item at the end of LL
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

    # inserts item next to given item
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
            self.n += 1
        # case 2 -> item not found
        else:
            print('Item not found')
            return

    # makes the LL empty
    def clear(self):
        self.head = None
        self.n = 0

    # deltes head of the LL
    def delete_head(self):
        # in case linked list is empty
        if self.head == None:
            return
        self.head = self.head.next
        self.n -= 1

    # removes the last item of the LL
    def pop(self):
        # case -> empty linked list
        if self.head == None:
            return

        # case -> single item in the linked list
        if self.head.next == None:
            self.delete_head()
            return

        curr = self.head
        while curr.next.next != None:
            curr = curr.next

        # curr is the 2nd last item
        curr.next = None
        self.n -= 1

    # removes the given item from the LL
    def remove(self, value):
        # case1 -> empty linked list
        if self.head == None:
            return

        prev = None
        curr = self.head

        # case2 -> value is in head node
        if prev == None and curr.data == value:
            self.delete_head()
            self.n -= 1
            return

        while curr.next != None:
            if curr.data == value:
                break
            prev = curr
            curr = curr.next

        # case 3 -> item not found
        if curr.next == None:
            return 'Item not found'
        else:
            prev.next = curr.next
            self.n -= 1

    # search the index of passed value and return its index
    def search(self, value):
        index = 0
        curr = self.head

        while curr != None:
            if curr.data == value:
                return index

            index += 1
            curr = curr.next

        return 'Not Found'


L = Linkedlist()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
# print(len(L))
# L.append(5)
# L.insert_after(1, 200)
print(L)
# L.delete_head()
# L.pop()
# L.remove(25)
# print(f'after deletion {L}')
print(L.search(4))
print(L)
