'''Sum of digits'''
list = []

def sum_digits(number):
    if(number == 0):
        return list
    digit = number % 10
    list.append(digit)
    sum_digits(number // 10)

value = int(input("Enter a Number"))
sum_digits(value)
print(sum(list))