number = int(input("Enter the Number : "))

if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is odd")

"""Using Bitwise"""
# if number & 1:
#     print("odd")
# else:
#     print("even")

"""Recursive"""
# def check_number(number):
#     if (number < 2):
#         return (number % 2 == 0)
#     return(check_number(number - 2))

# if(check_number(number) == True):
#     print(f"{number} is Even")
# else:
#     print(f"{number} is Odd")