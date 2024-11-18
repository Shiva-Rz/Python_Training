"""Variable Name and Age"""
name = input("Enter the Name : ")
age = int(input("Enter the Age : "))
address = input("Enter the city : ")

print("\nMy Name is : " +name)
print("My Age is : ",age)
print("My City is : " +address)

"""Multiply and Adding"""
value_1 = int(input("Enter Number 1 : "))
value_2 = int(input("Enter Number 2 : "))
value_3 = int(input("Enter Number 3 : "))

add = value_1 + value_2 + value_3
print("\nAdded values are : ", add)

multiple = value_1 * value_2 * value_3
print("Multiplied values are : ", multiple)

divide = multiple / add
print("Divided values are : ", divide, "\n")


"""Name, Score, Department"""
name = input("Enter the Name :")
score = int(input("Enter the Score :"))
department = input("Enter the Department :")

print("My Name is : ", name)
print(f"My Score is : ", score / 10,"/10")
print("My Department is : ", department)