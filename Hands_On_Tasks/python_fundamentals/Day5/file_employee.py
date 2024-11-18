employee_details = open('Employees.txt', 'w')
list = []

for index in range(4):
    name = input("Enter the Employee Name: ")
    list.append(name + '\n')

employee_details.writelines(list)

employee_details.close()