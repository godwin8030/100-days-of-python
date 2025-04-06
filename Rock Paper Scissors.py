import random

moves = ["rock", "paper", "scissors"]

r = random.choice(moves)


p1 = input("rock, paper or scissors ? ")
if p1 == "rock":
    print(r)
    if r == "rock":
        print("Draw")
    elif r == "paper":
        print("Computer Wins!!")
    elif r == "scissors":
        print("Player Wins!!")
    else:
        print("Invalid Input")
elif p1 == "paper":
    print(r)
    if r == "rock":
        print("Draw")
    elif r == "paper":
        print("Computer Wins!!")
    elif r == "scissors":
        print("Player Wins!!")
    else:
        print("Invalid Input")
elif p1 == "scissors":
    print(r)
    if r == "rock":
        print("Draw")
    elif r == "paper":
        print("Computer Wins!!")
    elif r == "scissors":
        print("Player Wins!!")
    else:
        print("Invalid Input")
else:
        print("Invalid Input")


