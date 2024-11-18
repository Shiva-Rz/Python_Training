class Employee:
    employee_name = "Shiva" # class Attributes
    employee_age = 22
    employee_id = 11947
    
    def works(self):
        print(f"{self.employee_name} is Working")
    
    def leaves(self):
        print(f"{self.employee_name} is Leave today")
    
employee_details = Employee() # Instance of Object - Instantiation
print(employee_details.employee_id)
print(employee_details.employee_name)
employee_details.works()

employee_details_1 = Employee()
employee_details_1.employee_id = 12105
employee_details_1.employee_name = "Kiruba"
# print(employee_details_1.employee_id)
# print(employee_details_1.employee_name)
employee_details_1.leaves()
