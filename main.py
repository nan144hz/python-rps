from colorama import Fore, init
import random

init(autoreset=True)

print(Fore.BLUE+"Welcome to Rock Paper Scissors!")
print(Fore.YELLOW+"Starting the game... \n")

while True:
    choices = ['rock', 'paper', 'scissors']
    user_choice = input('> Enter your choice: ')
    
    while len(user_choice) == 0:
        user_choice = input('> Enter your choice: ')
    
    while (user_choice!="rock") and (user_choice!="paper") and (user_choice!="scissors"):
        user_choice = input('> Enter your choice: ')
    
    ai_choice = random.choice(choices)

    print("\nUser Choice: {}".format(user_choice))
    print("Computer Choice: {}".format(ai_choice))

    if user_choice == ai_choice:
        print(Fore.LIGHTYELLOW_EX+"Tie!")
    elif user_choice == "rock":
        if ai_choice == "paper":
            print(Fore.LIGHTRED_EX+"You lose! Try again")
        elif ai_choice == "scissors":
            print(Fore.LIGHTGREEN_EX+"You won!")
    elif user_choice == "paper":
        if ai_choice == "scissors":
            print(Fore.LIGHTRED_EX+"You lose! Try again")
        elif ai_choice == "rock":
            print(Fore.LIGHTGREEN_EX+"You won!")
    elif user_choice == "scissors":
        if ai_choice == "rock":
            print(Fore.LIGHTRED_EX+"You lose! Try again")
        elif ai_choice == "paper":
            print(Fore.LIGHTGREEN_EX+"You won!")
        
    break