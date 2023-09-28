# Password Generator Project

# import the random module to use in the password generator
import random

# the list of letters to use in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z','A','B','C','D','E','F','G','H','I','J','K',
           'L','M','N','O', 'P','Q','R','S','T','U','V','W','X','Y','Z']

# the list of numbers to use in the password
numbers = ['0','1','2','3','4','5','6','7','8','9']

# the list of symbols to use in the password
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']

# print the welcome message and ask the user how many letters, numbers, and symbols they want in their password
print("Welcome to the Password Generator!")
value_letters = int(input("How many letters would you like in your password?\n"))
value_numbers = int(input("How many numbers would you like in your password?\n"))
value_symbols = int(input("How many symbols would you like in your password?\n"))

# create an empty list to store the password
password_list = []

# create a for loop to add the letters to the password list
for letter in range(1, value_letters + 1):
    password_list.append(random.choice(letters))

# create a for loop to add the numbers to the password list
for number in range(1, value_numbers + 1):
    password_list.append(random.choice(numbers))

# create a for loop to add the symbols to the password list
for symbol in range(1, value_symbols + 1):
    password_list.append(random.choice(symbols))

# shuffle the password list
random.shuffle(password_list)

# create an empty string to store the password
password = ""

# create a for loop to add the password list to the password string
for character in password_list:
    password += character

# print the password
print(f"Your password is: {password}")

# end of program
