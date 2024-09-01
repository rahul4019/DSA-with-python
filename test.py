# val = hash(23)
val = abs(hash('python')) % 5
# val = hash(6.1)
# val = hash([1, 2, 3]) // unhashable type error
# val = hash((1, 2, 3))

print(val)