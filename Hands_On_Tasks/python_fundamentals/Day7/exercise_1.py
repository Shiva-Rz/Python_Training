'''Convert a list of integers to a list of booleans where all non-zero values become True.'''
# Input = [-1, 2, 0, -4, 5]
# Output = [True, True, False, True, True]

numbers = [-1, 2, 0, -4, 5]
boolean_list = []

for number in numbers:
    if number == 0:
        boolean_list.append(False)
    else:
        boolean_list.append(True)
print(boolean_list)

# number_list = [boolean_list.append(False) if number == 0 else boolean_list.append(True) for number in numbers]

