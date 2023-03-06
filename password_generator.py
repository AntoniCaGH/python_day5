import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

letter_count = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like in your password?\n"))
number_count = int(input("How many numbers would you like in your password?\n"))

password_letters = random.sample(letters, letter_count)
password_symbols = random.sample(symbols, symbol_count)
password_numbers = random.sample(numbers, number_count)

password = password_letters + password_symbols + password_numbers

print(password)

random.shuffle(password)

randomised_password = "".join(password)

print(f"Your password is: {randomised_password}.")
print(len(randomised_password))


