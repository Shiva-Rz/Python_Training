# *args and **kwargs

"""def person_details(name, *details, **skills):
    print(f" Hi I'm {name} ")

    for detail in details:
        print(f'- {detail}')

    for key, value in skills.items():
        print(f"> {key} : {value}")

person_details('Shiva', 'Software Engineer', 'Relevantz', skills = 'Java, Angular, MySQL, Springboot')"""

# # Arguments and parameters

# # Default Argument
def book (name, published_date = '09-10-2024'):
    print("The Book Name : " + name + "\nThe Book published on" + published_date)

book('The Footprint')

def day_date(day, date):
    print(day)
    print(date)

#positional Argument
day_date('Wednesday','09-10-2024') 

#keyword Argument
day_date(date = '09-10-2024', day = 'Wednesday') 

# Variable Lenght Argument
def sum(a,*b):
    c = a

    for i in b:
        c = c + i
    print(c)

sum(1, 20, 30, 40)


# #Recursive Function
def factorial(x):

    "This is the factorial for the number"
    
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)

# print(factorial.__doc__)
fact = int(input("Factorial : enter number"))
print(factorial(fact))

# print(fact.__doc__)

'''------Different types of Scopes in Python-------'''

# # Global Scope
message = "Welcome to Our"

def web_application():
    app_name = "Corporate Communication Platform"
    print(message,app_name)

web_application()
# print(app_name) # Local variable so it's not accessible

def mobile_application(app_name):
    print("Welcome to Our",app_name) 
    print(message,app_name) # Global variable is accessible

mobile_application("Cric & Coffee")


# # Enclosing or Non Local scope
place_to_buy = 'Supreme Mobiles'

def mobile():
    price = 59000
    print(price)

    def mobile_model():
        global model
        model = 'Iphone 15'
        print(f"The price of {model} : ",price, "@", place_to_buy)

        def mobile_storage_capacity(storage):
            print(f"The price of {model} : ",price, "in", place_to_buy, "and\nit has", storage, "GB")

        mobile_storage_capacity(256)
    mobile_model()
mobile()
# print(model) # we can access the variable by changing it as a global variable


# Built in Scope


# Modify Variables 

name_list = ['sankar', 'satha', 'sivam']
print(name_list)
def names():
    name_list[0] = 'sankara'
    print(name_list)
names()



# def project(): 
#     if 1 < 5:
#         x = 24 
#         print("success")
#     else:
#         print("fail")

# def project():
#     print(x)

# project()

#local variable outside the if statement
a = 3

#checks for an expression
if(a==3):
    #local variable declared inside if block
    x = 3
else:
    print("none")
#returns error
print(x)

def person_height_weight(*,height, weight = 56):
    return height, weight

# print(person_height_weight(175,56))
print(person_height_weight(weight = 75, height = 156))