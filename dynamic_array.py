import ctypes  # It provides C compaitable data types


class MyList:
    def __init__(self):  # constructor
        self.size = 1
        self.n = 0

        # create a C type array with size = self.size
        self.A = self.__make_array(self.size)

    # returns lenght
    def __len__(self):
        return self.n

    def __make_array(self, capacity):
        # creates a C type array(static, referential) with size capacity
        return (capacity * ctypes.py_object)()


L = MyList()
print(type(L))
print(L)  # will pring memory address of L

print(len(L))