# def number_function(number):
    
#     print(number)
    
#     if number == 0:
#         print("Stop")
#     else:
#         number_function(number - 1)
    
# number_function(10)   

def calculate(number):
    
    if number == 1:
        return 1
    else:
        return number + calculate(number - 1)

result = calculate(10)
print(result)