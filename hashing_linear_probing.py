class Dictionary:

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size  # array of passed intialized with None
        self.data = [None] * self.size  # array of passed intialized with None

    def put(self, key, value):
        hash_value = self.hash_function(key)

        # if array at calculated value is empty then insert
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value

        else:
            # if the same key is present there then insert new value to correponding index of data array
            if self.slots[hash_value] == key:
                self.data[hash_value] = value

            else:
                new_hash_value = self.rehash(hash_value)
                while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
                    new_hash_value = self.rehash(new_hash_value)

                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value

                else:
                    self.data[new_hash_value] = value
            

    # to use dictionary notation
    def __setitem__(self, key, value):
        self.put(key, value)

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def hash_function(self, key):
        return abs(hash(key)) % self.size
    

D1 = Dictionary(3)

# D1.put("python", 25)
D1.put("python", 789)
D1.put("java", 45)
D1.put("php", 100)

D1['python'] = 9201  # using __setitem__ magic method

print(D1.slots)
print(D1.data)

