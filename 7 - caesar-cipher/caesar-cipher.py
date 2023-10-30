import string


def caesar_cipher(text, code, cipher):
    output = ""
    if cipher == "decode":
        code *= -1
    for character in text:
        position = alphabet.index(character)
        new_position = position + code
        output += alphabet[new_position]
    return output


alphabet = list(2*string.ascii_lowercase)
cipher = input(
    "Do you would like to 'encode' or 'decode'? (Type your choice)\n").lower()
text = input(f"Type the message you want to {cipher}: \n").lower()
code = int(input("Enter the code number:\n"))

print(caesar_cipher(text, code, cipher))
