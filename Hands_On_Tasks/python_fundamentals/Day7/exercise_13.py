'''Write a Python program to generate personalized letters for a list of names stored in a file named "names.txt" 
by replacing a placeholder "[name]" in a template letter stored in a file named "birthday_invite.txt" and 
saving each generated letter as a separate file.'''


names_file = open('names.txt', 'r').read().split()

# read_names = names_file.read().split()

invite_file = open('birthday_invite.txt', 'r').read()
    
for line in names_file:    
    with open(f'{line}.txt', 'w') as new_file:
        new_file.write(invite_file.replace("[name]", line))
    
# value = range(0, 10)
    
# print(list(value))

# print(any(value))