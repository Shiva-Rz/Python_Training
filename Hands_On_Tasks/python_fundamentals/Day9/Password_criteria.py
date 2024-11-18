'''A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users. Following are the criteria for checking the password:

		At least 1 letter between [a-z]
		At least 1 number between [0-9]
		At least 1 letter between [A-Z]
		At least 1 character from [$#@]
		Minimum length of transaction password: 6
		Maximum length of transaction password: 12 

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma. 
Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, 
the output of the program should be: ABd1234@1'''


user_password = input("Enter your Passwords : ")
pattern = '$#@!%^&*'

def password_criteria(user_password):
        
    password_length = len(user_password) >= 6 and len(user_password) <= 12
    lower_case = any(password_lower.islower() for password_lower in user_password)
    upper_case = any(password_upper.isupper() for password_upper in user_password)
    password_alphabets = any(password_alpha.isalpha() for password_alpha in user_password)
    password_number = any(password_number.isdigit() for password_number in user_password)
    patterns = any(password_pattern for password_pattern in pattern)

    return all([password_length, lower_case, upper_case, patterns, password_alphabets, password_number])

for password in user_password.split(','):
    if password_criteria(password):
        print(password)