'''Find the indices of non-zero elements in a list.'''
# Input = [1, 2, 0, 0, 4, 0]
# Output = [0, 1, 4]

values = [1, 2, 0, 0, 4, 0]
value_list = []

for value in values:
    if value != 0:
        value_list.append(values.index(value))
print(value_list)
