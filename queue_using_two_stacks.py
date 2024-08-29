from stack_LL_implementation import Stack, Node

stack1 = Stack()
stack2 = Stack()

# check if queue is empty
def isEmpty():
    return stack1.size() + stack2.size() == 0

def size():
    return stack1.size() + stack2.size()


def front_item():
    if isEmpty():
        return 'Empty queue'

    if stack2.isempty():
        while not stack1.isempty():
            stack2.push(stack1.pop())

    return stack2.peek()


def rear_item():
    if isEmpty():
        return 'Empty queue'

    return stack1.peek()

def enqueue(value):
    stack1.push(value)

def dequeue():
    if isEmpty():
        return 'Empty queue'

    if stack2.size() == 0:
        while stack1.size() > 0:
            stack2.push(stack1.pop())

    return stack2.pop()


def traverse():
    if isEmpty():
        return 'Empty queue'
    
    # First read from stack2
    temp1 = stack2.top()
    while temp1 is not None:
        print(temp1.data)
        temp1 = temp1.next

    # Then read from stack1
    temp2 = stack1.top()
    while temp2 is not None:
        print(temp2.data)
        temp2 = temp2.next

# print(isEmpty())
# print(size())


print("Queue operations:")
print("Is empty:", isEmpty())
enqueue(1)
enqueue(2)
enqueue(3)
print("Size:", size())
print("Front item:", front_item())
print("Rear item:", rear_item())
print("Dequeued:", dequeue())
print("Traverse:")
traverse()
print("Is empty after dequeue:", isEmpty())
