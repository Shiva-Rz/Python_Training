"""Task 4 : List of Squares: 
Write a function that takes a list of numbers and returns a new list containing the squares of the even numbers only. 
Use list comprehension."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Squares(numbers):
    new_list = [number**2 for number in numbers if number % 2 == 0]

    print("The Squares of Even numbers :",new_list)

Squares(numbers)

# size_of_list = input("Enter size of List: ")

# for values in size_of_list:
#     number = int(input("Enter : "))
# print(number.append())