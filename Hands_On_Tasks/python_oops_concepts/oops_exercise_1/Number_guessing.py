import random

class Number_guessing:
    
    def start(self):

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

        for attempts in range(attempts):
            
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
            
guess = Number_guessing()
guess.start()