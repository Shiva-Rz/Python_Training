'''1. abs() - parameter = number(-, real_img) and return type Absolute Number'''
real_img = 2 + 4j
print(real_img)
print(type(real_img))

number = -10.354654
print(abs(number))  # use instead abs(-10.437573) 
print(type(number))

'''2. all() and any() - parameter = iterable and return type is boolean'''
list_1 = [0, -1, 1, 2]
print(all(list_1))
print(type(all(list_1)))

list_one = ["shiva", "", 0, "Zara"]
print(all(list_one))
print(type(all(list_one)))

'''3. ascii() - parameter = any object(str, coll) and return type is string'''
name = ascii('a')
print(name)
print(type(name))

'''4. bin() - parameter = integer and return type str'''
value = bin(34)
print(value)
print(type(value))

name = bool(None) # None - False if any value present it will be true
print(name)

'''5. bytearray() and bytes() - parameter = any object(integer, string, coll) and return array of bytes'''
value = bytearray("Kiruba", 'utf-16')
print(value)
print(type(value))

'''6. dict() - parameter = keyword arguments and return type is dictionary'''
new = dict(name = 'shiva', age = 20)
print(new)
print(type(new))

'''7. enumerate() - parameter = (iterable, start) and return type '''
fruits = ('apple', 'banana', 'grapes')
values = enumerate(fruits)
print(list(values))