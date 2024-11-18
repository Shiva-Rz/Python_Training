""" Task 6 : Dictionary Value Update: 
    Write a function that takes a dictionary and a key-value pair. 
    If the key exists, update its value; if not, add the key-value pair to the dictionary."""

person = {'name' : 'shiva', 'age': 20, 'city': 'Madurai'}

new_key = 'age'
new_value = 23

for key, value in person.items():
    if key == new_key:
        person.update({new_key : new_value})

print(person)

if new_key not in person.keys():
    person[new_key] = new_value
print(person)



# for key, value in person.items():
#     print({key : value})

#     if key in person:
#         person.update({key : input("Enter a value")})
#     else:
#         person.update({'number' : 9863876478})

# print(person)

# new_key = 'age'
# new_value = ''

# def add_dict(person):

#     for key, value in person.items():
#         # print(f"{key} : {value}")

#         if new_key in person.keys():
#             new_dic = {}
#             # person['age'] = person.pop('age')
#             new_dic = {new_key : new_value}
#             print(new_dic)
#             break
#             print(f"{new_key} : {value}")
            
    

#     # for key in employee_details:
#     #     if key == search_key:
#     #         employee_details.update(employee_details)
#     #         print(employee_details)
#     #     else:
#     #         employee_details.values(employee_details)
#     # print(employee_details)



# # new_key = 'rank'
# add_dict(person)
