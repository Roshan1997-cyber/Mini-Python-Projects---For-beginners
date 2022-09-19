import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors: ").lower()
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You are the winner!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You are the winner!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You are the winner!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw")

    else:
        print("I am the champion and you are the loser!")
        computer_wins += 1
        break

print("You won", user_wins, "matches")
print("The computer finally got ya")
print("Thanks for playing!")
