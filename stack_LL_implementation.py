class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # tells whether stack is empty or not
    def isempty(self):
        return self.top == None

    # inserts new node in the stack
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top

        self.top = new_node

    # prints items of the stack from top to bottom
    def traverse(self):
        temp = self.top

        while temp != None:
            print(temp.data)
            temp = temp.next

    # returns the data of the top item in the stack
    def peek(self):
        if self.isempty():
            return "Stack Empty"
        return self.top.data

    # removes the top item of the stack
    def pop(self):
        if self.isempty():
            return 'Stack Empty'
        temp = self.top.data
        self.top = self.top.next
        return temp

    # reverses the string
    def reverse_string(self, string):

        s = Stack()

        for i in string:
            s.push(i)

        newStr = ''

        while (not s.isempty()):
            newStr += s.pop()

        print(newStr)

    def text_editor(self, string, operations):
        # s = Stack()
        undo = Stack()
        redo = Stack()

        # creating stack of the given string
        for i in string:
            undo.push(i)

        for i in operations:
            if i == 'u':
                temp = undo.pop()
                redo.push(temp)

            elif i == 'r':
                temp = redo.pop()
                undo.push(temp)

        res = ''

        while not undo.isempty():
            res = undo.pop() + res

        print(res)


s = Stack()


# s.push(2)
# s.push(3)
# s.push(4)
# print(s.isempty())
# s.traverse()
# s.pop()
# s.pop()
# s.pop()
# print(s.pop())
# s.traverse()
# print(s.peek())

# s.reverseString('rahul')
# s.text_editor('hello', 'ururu')
s.text_editor('hello', 'uuur')
