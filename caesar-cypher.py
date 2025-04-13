alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

art = """
>>==================================================<<
||░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░█░█░█▀█░█░█░█▀▀░█▀▄||
||░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄||
||░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░░▀░░▀░░░▀░▀░▀▀▀░▀░▀||
>>==================================================<<
"""
print(art)

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter)+shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Encoded result: {cipher_text}")
    restart = input("Type 'yes' if you want to go again, Otherwise type 'no':\n").lower()
    if restart == "yes":
        caesar()
    else:
        print("Goodbye")



def decrypt(original_text, shift_amount):
    decipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            decipher_text += letter
        else:
            shifted_position = alphabet.index(letter)-shift_amount
            shifted_position %= len(alphabet)
            decipher_text += alphabet[shifted_position]

    print(f"Decoded result: {decipher_text}")
    restart = input("Type 'yes' if you want to go again, Otherwise type 'no':\n").lower()
    if restart == "yes":
        caesar()
    else:
        print("Goodbye")

def caesar():
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text = input("Type the message:\n").lower()
    shift = int(input("Enter the shift number:\n"))

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Invalid Input")


caesar()
