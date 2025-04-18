import random


def make_guess():
    print("Welcome to the Number Guessing Game! 🔢")
    print("Choose a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    num = random.randint(1,100)

    if difficulty == 'easy':
        guess_attempt = 10
    elif difficulty == 'hard':
        guess_attempt = 5
    else:
        print("Invalid difficulty selected ❌")
        return
    
    while guess_attempt > 0:
        print(f"You have {guess_attempt} attempts remaining to guess the number 💀")
        user_guess = int(input("Make a guess 🤔: "))

        if user_guess == num:
            print("You won 🎆")
            return
        elif user_guess < num:
            print("Too low 🥲")
        else:
            print("Too high 😅")

        guess_attempt -= 1
    
    print("Game Over. You have run out of guesses buddy 😭")
                
make_guess()