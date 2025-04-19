from higher_lower_data import data
import random

def compare_followers(A, B):
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    return guess

continue_game = True
score = 0

A = random.choice(data)
B = random.choice(data)

while continue_game:
    while B == A:
        B = random.choice(data)

    guess = compare_followers(A, B)

    if guess == 'A' and A['follower_count'] > B['follower_count']:
        score += 1
        print(f"You're correct! Current Score: {score}.")
    elif guess == 'B' and B['follower_count'] > A['follower_count']:
        score += 1
        print(f"You're correct! Current Score: {score}.")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final Score: {score}.")

    A = B
    B = random.choice(data)