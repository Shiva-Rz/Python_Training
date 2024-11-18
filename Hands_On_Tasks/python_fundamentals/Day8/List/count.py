names_list = []
new_list = []
empty_list = []

for index in range(0, 5):
    user_input = input("Enter username :")
    names_list.append(user_input)
print(names_list)

word_count = int(input("Enter the words_count : "))

for name in names_list:    
    if len(name) > word_count:
        new_list.append(name)
    else:
        empty_list.append(name)
        
print("The sorted names : ", new_list)
print("The balance names : ",empty_list)