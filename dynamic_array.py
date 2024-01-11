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

    # inserts the item in the array
    def append(self, item):
        # first check if there is vacant space in the array
        if self.n == self.size:
            # increase the size of the array
            self.__resize(self.size*2)

        # append the item in the array
        self.A[self.n] = item
        self.n += 1

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

print(len(L))
