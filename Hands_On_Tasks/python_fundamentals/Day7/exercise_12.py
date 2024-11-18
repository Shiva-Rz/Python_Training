'''Write a Python program to create a simple number guessing game where the computer thinks of a number between 1 and 100, 
and the user has to guess it within a certain number of attempts, 
with the option to choose the difficulty level ('easy' or 'hard') that determines the number of attempts.'''

import random

print("Welcome to the Number Guessing Game!")
print("Please guess the number what is I'm thinking")

number = random.randint(1, 100)
user_input = 0

def multiple_attempts(level_type):
    
    if level_type == 'easy':
        return 10
    elif level_type == 'hard':
        return 5
    else:
        print("Please the select valid level_type.")

level_type = input("Choose a level ('easy' or 'hard'): ")
attempts = multiple_attempts(level_type)

for attempt in range(attempts):
    
    user_input = int(input("Enter your guess: "))

    if user_input < number:
        print("Too low, try again.")
    elif user_input > number:
        print("Too high, try again.")
    else:
        print(f"Congratulations! You guessed the number {number} correctly!")
        break
else:
    print(f"Sorry, attempts are over. The number I'm thinking {number}.")



# import random

# for index in range(1, 100 + 1):
#     pass

# level_type = ['easy', 'hard']

# print("Choose the level from the below list \n")

# for choose_level in level_type:
#     print(choose_level)

# level = input("Select the level : ")

# if level == 'easy':
#     for value in range (1, 5 + 1):
#         user_input = input("Enter the guessing number")
#         while user_input == random.randrange(index):
#             print("You're correct", user_input)
            
