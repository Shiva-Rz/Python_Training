class Mobile: # class is also considered as Object
    
    '''Every class has
    attributes and methods'''
    
    brand_name = "vivo"
    price_amount = 18000
    mobile_color = "green"
    
mobile = Mobile()
print(mobile.brand_name)
print(mobile.price_amount)

temp = getattr(Mobile, 'color', 'text')
print(temp)

# print(mobile) '''returns memory address'''
# print(id(mobile)) '''returns the integer value of the memory address'''
# print(hex(id(mobile))) '''returns hex'''
# print(isinstance(mobile, Mobile)) '''isinstance(object, type) returns boolean'''


