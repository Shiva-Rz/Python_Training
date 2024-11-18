'''Given a string, split the string by a delimeter and join it using another delimiter'''

string_value = input("Enter String Value : \n")
join_value = []

value = string_value.split()
print(value)

new_value = '*'.join(character for character in value if character.isalpha())
print(new_value)