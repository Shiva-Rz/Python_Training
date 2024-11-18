# first_value = int(input("Enter 1 : "))
# second_value = int(input("Enter 2 : "))

# # Zero Division Error
# try:
#     sum = (first_value / second_value)
#     print(sum)
# except ZeroDivisionError:
#     print("Facing some TypeError")
# else:
#     print("Nothing went wrong")
# finally:
#     print("Totally Completed")

# # Custom Exception
# x = -1
# if x < 0:
#     raise Exception("The value must be greater than 0")

# # Keyboard Interrupt Error
# try:
#     while True:
#         number = int(input("Enter the Number : "))
#         print(f"The value : {number}")
# except KeyboardInterrupt:
#     print("Program is Terminated by User")

# # Value Error
# try:
#     value = int(input("Enter a number :"))
#     print(value)
# except ValueError:
#     print("The numbers only Acceptable")

# #Type Error
# try:
#     number_list = [1, 2, 3]
#     name = "Babu"
#     print(number_list + name)
# except TypeError:
#     print(f"The {number_list} and {name} won't be added")

# # Attribute Error
# try:
#     number = 10
#     number.append("rank")
#     print(number)
# except AttributeError:
#     print("Can't append number and string")

# Assertion Error
# try:
#     number = 12
#     assert number < 0
#     print(number)
# except AssertionError:
#     print("The Execution is Failed")

# list_value = [1, 2, 3, 4, 5, 6]

# value = 0

# while value < len(list_value):
#     print(list_value[value])
#     value = value + 1
# else:
#     print("the value index is ended")