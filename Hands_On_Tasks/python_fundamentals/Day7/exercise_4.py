'''Given a string, find out if the given string contains any'''
	# - alphanumeric characters
	# - alphabetical characters
	# - digits

user_input = input("Enter any String Value : \n")

if user_input.isalpha():
    print("Alphabetical Characters")
elif user_input.isdigit():
    print("Digits")
else:
    print("Alphanumeric Characters")