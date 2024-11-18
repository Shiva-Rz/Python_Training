'''Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].'''

numbers_list = range(1, 11)
print(list(numbers_list))

def even_number(number):
    return number % 2 == 0

def squares(number):
    return number ** 2

value = map(squares ,filter(even_number, numbers_list))

print(list(value))