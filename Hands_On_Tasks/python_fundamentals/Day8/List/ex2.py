numbers_list = range(0, 11)
print(list(numbers_list))

value_list = []
value_list = lambda number: number + sum(list(numbers_list))
print(value_list)