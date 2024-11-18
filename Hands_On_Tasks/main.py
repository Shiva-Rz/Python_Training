print('shiva')

if 5 > 112:
    print('villa')

else:
    pass

# def add(a, b):
#     """ Add two arguments
#     Arguments:
#         a: an integer
#         b: an integer
#     Returns:
#         The sum of the two arguments
#     """
#     return a + b

# print(add(1,2))


def add(a, b):
    "Return the sum of two arguments"
    return a + b

# help(add)

# def greet(name, message='Hi'):
#     return f"{message} {name}"


# greeting = greet('John', 'Hello')
# print(greeting)

help(add)

# for i in range(0,11,2):
#     print(i)
    
# value = 2
# for i in range(1,11):
#     print(f'{i} X {value} = ' + str(i*2))

# count = 0
# for i in range(1,11):
#     if(i%2==0):
#         count = count+1
# print(count)

# sum = 0
# for i in range(0,101):
#     sum = sum + i
# print(sum)

# n = 100
# sum = n * (n+1)/2
# print(sum)

# number = input("Enter the Number : ")
# counter = 0
# while counter < int(number):
#     print(counter)
#     counter = counter + 1

# command = ''

# while command.lower() != 'quit':
#     command = input('>')
#     print(f"Echo : {command}")

a = []
for i in range(10):
    number = int(input("Number "+str(i+1)))
    a.append(number)
print(a)
    
sum = 0
for i in a:
    sum = sum + i
print(sum)
