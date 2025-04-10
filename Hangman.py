import random

word_list = ["apple", "cat", "dog", "tony"]

choosen_word = random.choice(word_list)
print(choosen_word)

placeholder = ""
for i in range(len(choosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
right_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in choosen_word:
        if letter == guess:
            right_letters.append(guess)
            display += letter
        else:
            display += "_"

    print(display)
    
    if "_" not in display:
        game_over = True
        print("****************You win!!!****************")
