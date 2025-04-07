import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Random Password Generator")
iletters = int(input("How many letter would you like in your password mate ? "))
isymbols = int(input("How many symbols would you like mate ?  "))
inumbers = int(input("How many numbers would you like mate ?  "))

password = []

for i in range(0, iletters):
    random_char = random.choice(letters)
    password += random_char

for i in range(0, isymbols):
    random_char = random.choice(symbols)
    password += random_char

for i in range(0, inumbers):
    random_char = random.choice(numbers)
    password += random_char


random.shuffle(password)

password_r = ""
for i in password:
    password_r += i

print(f"Your password is: {password_r}")
    
