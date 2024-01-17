import ctypes  # It provides C compaitable data types


class MyList:
    def __init__(self):  # constructor
        self.size = 1
        self.n = 0

        # create a C type array with size = self.size
        self.A = self.__make_array(self.size)

    # returns length
    def __len__(self):
        return self.n

    # returns a string containing all the items in the array
    def __str__(self):
        result = ''
        for i in range(self.n):
            # if(i == self.n -1):
            #     result += str(self.A[i])
            # else:
            #     result += str(self.A[i]) + ','
            result += str(self.A[i]) + ','

        # slicing result string to remove last comma
        return '[' + result[:-1] + ']'

    # increases the capacity of the array and copy-paste the items of first array to the new array
    def __resize(self, new_capacity):
        # create a new array with new capacity
        self.B = self.__make_array(new_capacity)
        self.size = new_capacity

        # copy the content of A to B
        for i in range(self.n):
            self.B[i] = self.A[i]

        # reassign A
        self.A = self.B

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'

    # inserts the item in the array
    def append(self, item):
        # first check if there is vacant space in the array
        if self.n == self.size:
            # increase the size of the array
            self.__resize(self.size*2)

        # append the item in the array
        self.A[self.n] = item
        self.n += 1

    # removes the last element from the array
    def pop(self):
        if (self.n == 0):
            return 'Empty List'
        print(self.A[self.n-1])
        self.n -= 1

    # clears the array
    def clear(self):
        self.n = 0
        self.size = 1

    # finds the index of given value
    def find(self, val):
        for i in range(self.n):
            if self.A[i] == val:
                return i
        return 'ValueError - not in the list'

    # inserts given value at given index
    def insert(self, index, val):
        if self.size == self.n:
            self.__resize(self.size*2)

        for i in range(self.n, index, -1):
            self.A[i] = self.A[i-1]

        self.A[index] = val
        self.n += 1

    def __delitem__(self, index):
        # check if the given in index in the range
        if (0 <= index < self.n):
            for i in range(index, self.n):
                self.A[i] = self[i+1]
            self.n -= 1
        else:
            print('ValueError - out of range')

    def __make_array(self, capacity):
        # creates a C type array(static, referential) with size capacity
        return (capacity * ctypes.py_object)()


L = MyList()
# print(type(L))
# print(L)  # will pring memory address of L


L.append('Hello')
L.append(3.4)
L.append(True)
L.append(100)
L.append('Rahul')

# print(L[22])
# print(L)
# print(len(L))
# L.pop()
# L.clear()
print(L)
# print(L.find('Rahuls'))
# L.insert(0, 0)
# L.delete(2)
del L[0]
print(L)
