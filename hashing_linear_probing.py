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

            # if there is something else present in the slots array then we will do reahsing
            else:
                new_hash_value = self.rehash(hash_value)
                while (
                    self.slots[new_hash_value] != None
                    and self.slots[new_hash_value] != key
                ):
                    new_hash_value = self.rehash(new_hash_value)

                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value

                # if the same key is present in the slots list
                else:
                    self.data[new_hash_value] = value

    def get(self, key):
        start_position = self.hash_function(key)
        current_position = start_position

        while self.slots[current_position] != None:

            # key found on the current_position
            if self.slots[current_position] == key:
                return self.data[current_position]

            current_position = self.rehash(current_position)

            # key not found
            if current_position == start_position:
                return "Not Found"

        return "Not Found"

    def __str__(self):

        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(f"{self.slots[i]}: {self.data[i]}", end=" ")
        return ""

    # to use dictionary notation
    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def rehash(self, old_hash):
        return (
            old_hash + 1
        ) % self.size  # we have used % so it will never cross the size of list

    def hash_function(self, key):
        return (
            abs(hash(key)) % self.size
        )  # sometimes hash gives -ve value that's why we used abs


D1 = Dictionary(3)

# D1.put("python", 25)
D1.put("python", 789)
D1.put("java", 45)
D1.put("php", 100)

D1["python"] = 9201  # using __setitem__ magic method

print(D1.slots)
print(D1.data)

print(D1.get("python"))
print(D1.get("c"))  # will return "Not Found"

print(D1["python"])

print(D1)
