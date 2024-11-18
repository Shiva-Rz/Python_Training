'''You are given two data structures:
users - A list of forum users' names along with their nationalities (i.e. a list of tuples).
nationality_to_continents - A dictionary in which nationalities are keys and continents are values
		
Create a dictionary and use it to store the number of users for each continent'''

users = [
('Maria', 'Greek'), ('Jean', 'Maltese'),
('Juan', 'Spanish'), ('Dima', 'Ukrainian'),
('Agata', 'Thai'), ('Rafal', 'Polish'),
('Diego', 'Turkish'), ('Stan', 'Panamanian'),
('John', 'Australian'), ('Frank', 'Belgian'),
('Jane', 'Canadian'), ('Paul', 'Argentinian'),
('Taylor', 'Danish'), ('Kate', 'American'),
('Mark', 'Sri Lankan'), ('Jane', 'Japanese'),
('Ted', 'Indian'), ('Jean', 'Egyptian')]
 
nationality_to_continents = {
'Greek': 'Europe', 'Maltese': 'Europe',
'Spanish': 'Europe', 'Ukrainian': 'Europe',
'Thai': 'Asia', 'Polish': 'Europe',
'Turkish': 'Asia', 'Panamanian': 'Central America',
'Australian': 'Australia', 'Belgian': 'Europe',
'Canadian': 'North America', 'Argentinian': 'South America',
'Danish': 'Europe', 'American': 'North America',
'Sri Lankan': 'Asia', 'Japanese': 'Asia',
'Indian': 'Asia', 'Egyptian': 'Africa'}


user = dict(users)

users_count = {}

for user, value in user.items():
    for city, country in nationality_to_continents.items():
        if value == city:
            if country in users_count:
                users_count[country] = users_count[country] + 1 
            else:
                users_count[country] =  1
print(users_count)
        

# no_of_users = zip(users, nationality_to_continents.values())
# print(dict(no_of_users))

# count = 0
# for keys in user.keys():
#     for values in nationality_to_continents.values():
#         if user.keys() == nationality_to_continents.values():
#             count = count + 1
#             print(count)
#         else:
#             print("exit")
#             break