""" Task : 3 Create a Dictionary from Two Lists:
    keys = ["name", "age", "city"]
    values = ["Bob", 25, "Los Angeles"]"""
# Write a function that creates a dictionary from the two lists, handling cases where the lists are of different lengths:

# Expected output = {"name": "Bob", "age": 25, "city": "Los Angeles"}

keys = ["name", "age", "city"]
values = ["Bob", 25, "Los Angeles"]
dic = {}

def list_dic(keys, values):
    for key in keys:
        for value in values:
            dic[key] = value
        
            values.remove(value)
            break
    print(dic)
     
list_dic(keys, values)


# names = ["shiva", "bala", "ajay"]
# number = [2, 3, 1]

# dic = {names[index]: number[index] for index in range(len(number))}
# print(dic)


# for keys, values in dic:
#     dic.items()
# print(dic)

# for keys, values in dic:
#     person = dic[keys,values]
#     print(dic)