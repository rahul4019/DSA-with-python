class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LL:

    def __init__(self):
        self.head = None

    def add(self, key, value):
        new_node = Node(key, value)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    def delete_head(self):

        if self.head == None:
            return "Empty"
        else:
            self.head = self.head.next

    def remove(self, key):
        if self.head is None:
            return "Empty"

        if self.head.key == key:
            self.delete_head()
            return

        if self.head == None:
            return "Empty"
        else:

            temp = self.head

            while temp.next != None:
                if temp.next.key == key:
                    break
                temp = temp.next

            if temp.next == None:
                return "Not Found"
            else:
                temp.next = temp.next.next

    def traverse(self):

        temp = self.head

        while temp != None:

            print(temp.key, "-->", temp.value, " ", end=" ")
            temp = temp.next

    def size(self):

        temp = self.head
        counter = 0

        while temp != None:

            counter += 1
            temp = temp.next

        return counter

    def search(self, key):

        temp = self.head
        pos = 0

        while temp != None:

            if temp.key == key:
                return pos

            temp = temp.next
            pos += 1

        return -1

    def get_node_at_index(self, index):

        temp = self.head
        counter = 0

        while temp is not None:

            if counter == index:
                return temp
            temp = temp.next
            counter += 1

