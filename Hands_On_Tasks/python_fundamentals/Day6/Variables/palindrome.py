'''Check Palindrome'''
# number = int(input("Enter a number :"))
# temp = number
# value = 0
# while(number > 0):
#     digit = number % 10
#     value = value * 10 + digit
#     number = number // 10

# if (temp == value):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

'''Reverse Number'''
# number = int(input("Enter number :"))
# temp = number
# value = 0

# while(number > 0):
#     digit = number % 10
#     value = value * 10 + digit
#     number = number // 10

# print(value)

'''Reverse Number using Slice operator'''
number = int(input("Enter a number : "))
reverse_number = str(number)[::-1]
print(reverse_number)