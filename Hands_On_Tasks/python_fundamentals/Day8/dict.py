person = {'name' : 'shiva', 'name' : 'shiva' , 'name' : 'Tamil'}
count = 0
# search = 'shiva'
search = {'name' : 'shiva'}

print(person.keys() == search.keys())

for key, value in person.items():
    for values in search.values():    
        if person.values() == search.values():
            # search[value] = [key]
            count += 1
            print(person)
        else:
            # search[value].append(key)
            print("No values found")
            
# print(search)
