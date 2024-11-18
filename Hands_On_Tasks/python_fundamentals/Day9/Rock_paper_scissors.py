'''Create a simple two-player Rock-Paper-Scissors game where one player is the user and the other is the system. 
    The game should ask the user for their name, their choice (Rock, Paper, or Scissors), system should also consider its choice, 
    compare the choices and determine the winner, 
    print out a congratulatory message to the winner, and ask the user if they want to play again.'''

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

def hands_game():
    game_symbols = ['Rock', 'Paper', 'Scissors']

    user_name = input("Enter the Player Name : ")

    while True:
        
        print("Choose any one from the below options ")
        for symbol in game_symbols:
            print(symbol)

        user_choice = input("Enter your preference : ").lower()

        system_choice = random.choice(game_symbols).lower()
        print(system_choice)
        
        if user_choice == 'paper' and system_choice == 'rock':
            # print(f"Your choice : {user_choice}\n Opponent Choice : {system_choice}")
            print(f"{user_name} , Congratulations! You won the Game.")
        elif user_choice == 'rock' and system_choice == 'scissors':
            print(f"{user_name} , Congratulations! You won the Game.")
        elif user_choice == 'scissors' and system_choice == 'paper':
            print(f"{user_name} , Congratulations! You won the Game.")
        elif user_choice == system_choice:
            print(f"{user_name}, Oops Game is Tie.")
        else:
            print(f"{user_name}, Sorry, Opponent player won")
            
        print("----If you want to play again----")
        condition = input("Enter ('yes' or 'y') to continue and ('no' or 'n') to exit : ")
        
        if condition.lower() == 'no' or condition.lower() == 'n':
            print("You're excited from the Game")
            break
hands_game()