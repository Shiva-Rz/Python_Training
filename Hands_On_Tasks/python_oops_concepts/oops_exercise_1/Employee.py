'''1. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and 
	methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
	
	Sample Employee Data:
	"Virat", "E7876", 50000, "ACCOUNTING"
	"AB de", "E7499", 45000, "RESEARCH"
	"Gilchrist", "E7900", 50000, "SALES"
	"Jhondy", "E7698", 55000, "OPERATIONS"

	Use 'assign_department' method to change the department of an employee.
	Use 'print_employee_details' method to print the details of an employee.
	Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. 
	If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
		overtime = hours_worked - 50
		Overtime amount = (overtime * (salary / 50))'''

class Employee:
    
    def __init__(self, employee_id, employee_name, employee_salary, employee_department):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_salary = employee_salary
        self.employee_department = employee_department
        
    def employee_assign_department(self, employee_department):
        self.employee_assign_department = employee_department
    
    def calculate_employee_salary(self, employee_salary, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (employee_salary / 50))
            self.employee_salary += overtime_amount
        elif hours_worked < 50:
            # per_day = (employee_salary / 50)
            worked_hours = hours_worked * (employee_salary / 50)
            self.employee_salary = worked_hours 
    
    def print_employee_details(self):
        print(f"Employee Id : {self.employee_id} \nEmployee Name : {self.employee_name} \nEmployee Department : {self.employee_assign_department} \nEmployee Overtime Amount : {self.employee_salary}" )
        
employee_1 = Employee("Virat", "E7876", 50000, "ACCOUNTING" )
employee_2 = Employee("AB de", "E7499", 45000, "RESEARCH" )
employee_3 = Employee("Gilchrist", "E7900", 50000, "SALES" )
employee_4 = Employee("Jhondy", "E7698", 55000, "OPERATIONS" )

employee_1.employee_assign_department("Software Engineer")
employee_1.calculate_employee_salary(50000, 20)
employee_1.print_employee_details()