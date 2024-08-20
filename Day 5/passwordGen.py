#Password Generator Project
from random import randint, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

len_pswd = nr_letters + nr_symbols + nr_numbers
pswd = []

for letter in range(nr_letters):
    pswd.append(letters[randint(0, len(letters) - 1)])
for symbol in range(nr_symbols):
    pswd.append(symbols[randint(0, len(symbols) - 1)])
for number in range(nr_numbers):
    pswd.append(numbers[randint(0, len(numbers) - 1)])

print(pswd)

shuffle(pswd)

print("".join(pswd))
