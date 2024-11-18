'''Add three given lists using Python map and lambda.'''
# Inputs:	list_one = [1, 2, 3]
	# 		list_two = [4, 5, 6]
	# 		list_three = [7, 8, 9]
			
# Output: [12, 15, 18]

list_one = [1, 2, 3]
list_two = [4, 5, 6]
list_three = [7, 8, 9]

total_list = map(lambda one, two, three : one + two + three, list_one, list_two, list_three )
print(list(total_list))














# value = map(lambda string: ""+ str(string), list_one)
# print(list(value))