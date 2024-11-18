'''Encapsulation - Binding up the datas private methods and variables in a single unit '''

class Company:
 
    def __init__(self, employees, departments, experience, income):
        self.no_of_employees = employees
        self.no_of_departments = departments
        self.years_of_experience = experience
        self.__annual_growth = income

    def details(self):
        print(f"Our company has {self.no_of_employees} Employees\nThere are {self.no_of_employees}+ departments\nand having {self.years_of_experience}+ years of Experience\nOur annual growth : {self.__annual_growth}")

    #getter
    def get_annual_growth(self):
        return self.__annual_growth
    
    #setter
    def set_annual_growth(self, income):
        self.__annual_growth = income
    
# print(company_details.__annual_growth) #Private variable is not accessible outside of class
company_details = Company(1200, 20, 24, 10000000000)
company_details.details()
# print(company_details.get_annual_growth())
company_details.set_annual_growth(90903535670000)
company_details.details()

'''Using getattr()'''
# print(company_details.no_of_employees)
# value = getattr(Company(1200, 20, 24, 10000000000), 'no_of_employees')
# print(value)

