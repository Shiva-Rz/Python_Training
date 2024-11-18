"""--Collections (List, Tuple, Set, Dictionary)--"""

"""List (Using Strings)"""
'''bikes = ['Enfield', 'R15', 'V3', 'Mt15', 'Rx100']'''
# bikes = ["Enfield", "R15", "V3", "Mt15", "Rx100"]
# # bikes = []
# print("\n")
# print(bikes)
# print("-->",*bikes) # By using this the list will be unpacked

# print("\n")

# fruits = [['apple', 'red'], ['banana', 'yellow'], ['watermelon', 'green'],[]]
# print(fruits)

# fruits[0] = ['orange']

# fruits[3] = fruits[0]
# fruits[0] = ['apple', 'red']

# print(fruits)

# for fruit in fruits:
#     print(fruit)
# else:
#     print(bikes)

"""Using numbers"""

# numbers = [1, 2, 4, 6, 8, 10]
# print(numbers)

# numbers[1] = numbers[1] * 20
# print("\nMultiplying the index 1 into 20 :",numbers)

# numbers[2] = numbers[2] / 2
# print("\nDivide the index value 2 :",numbers)

# numbers.append(100)
# print("\nAppending 100 :",numbers)

# numbers.insert(3,3)
# print("\ninserting value 3 in the index of 3",numbers)

# del numbers[3]
# print("\nDeleting the value from index 3",numbers)

# print("\npopping the last number",numbers.pop())
# print(numbers)

# print("\nremoving the value by passing the value :",numbers.remove(1)) # None will be return
# print(numbers)


numbers = [1, 2, 3, 4, 5, 6]

even_list = []
odd_list = []

for number in numbers:

    if (number % 2 == 0):
        even_list.append(number)
        print(even_list)