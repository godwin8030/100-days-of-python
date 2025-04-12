
def calculate_love_score(l1,l2):
    total_truel1= 0
    total_lovel1= 0
    total_truel2= 0
    total_lovel2= 0

    for letter in l1.lower():
        if letter in "true":
            total_truel1 += 1
        if letter in "love":
            total_lovel1 += 1

    for letter in l2.lower():
        if letter in "true":
            total_truel2 += 1
        if letter in "love":
            total_lovel2 += 1

    true = total_truel1 + total_truel2
    love = total_lovel1 + total_lovel2

    print(f"{true}{love}")

calculate_love_score("Romeo", "Juliet")


