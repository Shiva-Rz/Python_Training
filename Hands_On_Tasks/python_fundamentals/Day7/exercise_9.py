'''Map every number from 1-9 to it's perfect square. Output should be dict type
key should be the number and value should be square of the number. Use range function.'''
	
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# number_dict = {}
# list = [index ** 2 for index in range(1, 9)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

square_numbers = {number : number ** 2 for number in numbers}
print(square_numbers)