import sys
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
len_alphabet = len(alphabet)

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    i = 0
    for letter in original_text:
        # only enters the 'if' if it's on the alphabet
        if original_text[i] in alphabet:
            original_letter_index = alphabet.index(original_text[i])
            new_letter_index = original_letter_index + shift_amount
            if new_letter_index >= len_alphabet:
                new_letter_index = new_letter_index % len_alphabet
            new_letter = alphabet[new_letter_index]
            encrypted_text = encrypted_text + new_letter
        # if it's not a letter print as it is
        else:
            encrypted_text = encrypted_text + original_text[i]
        i += 1
    print(f"Here's the encoded result: {encrypted_text}")

def decrypt(original_text, shift_amount):
    encrypted_text = ""
    i = 0
    for letter in original_text:
        # only enters the 'if' if it's on the alphabet
        if original_text[i] in alphabet:
            original_letter_index = alphabet.index(original_text[i])
            new_letter_index = original_letter_index - shift_amount
            if new_letter_index < 0:
                new_letter_index = new_letter_index % len_alphabet
            new_letter = alphabet[new_letter_index]
            encrypted_text = encrypted_text + new_letter
        # if it's not a letter print as it is
        else:
            encrypted_text = encrypted_text + original_text[i]
        i += 1
    print(f"Here's the decoded result: {encrypted_text}")

def caeser(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "encode":
        encrypt(original_text, shift_amount)
    if encode_or_decode == "decode":
        decrypt(original_text, shift_amount)

game_is_on = True

while game_is_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # accepts only "encode" or "decode"
    if direction not in ("encode", "decode"):
        print("Write 'encode' or 'decode'.\nTry again. Goodbye")
        sys.exit(0)
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # accepts only numbers
    if shift.is_integer():
        shift = shift
    else:
        print("Write only numbers.\nTry again. Goodbye")
        sys.exit(0)
   # handles negative numbers
    if shift < 0:
        shift = abs(shift)
        if direction == "encode":
            direction = "decode"
        elif direction == "decode":
            direction = "encode"
    caeser(original_text=text, shift_amount=shift, encode_or_decode=direction)
    rep = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if rep == "yes":
        game_is_on = True
    else:
        print("Goodbye")
        sys.exit(0)

