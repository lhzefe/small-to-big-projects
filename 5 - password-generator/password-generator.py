import random
import string

number_letters = int(input("Enter the number of letters you want: "))
number_specials = int(input("Enter the number of special you want: "))
number_numbers = int(input("Enter the number of numbers you want: "))

password = []
for letter in range(number_letters):
    password.append(random.choice(string.ascii_letters))
for special in range(number_specials):
    password.append(random.choice(string.punctuation))
for number in range(number_numbers):
    password.append(random.choice(string.digits))
random.shuffle(password)
password = "".join(password)
print(f"The password generated was: {list(password)} or united {password}")
