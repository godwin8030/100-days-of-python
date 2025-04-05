print("Hi! Welcome to Python Pizza.")
size = input("What size pizza do you want? S, M or L: ")
peppo = input("Do you want pepperoni on your pizza: Y or N: ")
cheese = input("Do you want extra cheese on your pizza: Y or N: ")
bill = 0
S = 15
M = 20
L = 25
PS = 2
P = 3
C = 1

if(size=="S"):
    bill = S
elif(size=="M"):
    bill = M
elif(size=="L"):
    bill = L
else:
    print("Invalid Size selection.")
    bill = 0

if peppo=="Y":
    if size=="S":
        bill += PS
    else:
        bill += P

if cheese=="Y":
    bill += C

if bill > 0:
    print(f"Your Final Bill is ${bill}")

