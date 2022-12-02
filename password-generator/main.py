#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""

# for char in range(1, nr_letters + 1):
#   random_char = random.choice(letters)
#   password += random_char

# for char in range(1, nr_numbers + 1):
#   random_char = random.choice(numbers)
#   password += random_char

# for char in range(1, nr_symbols + 1):
#   random_char = random.choice(symbols)
#   password += random_char


# print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# works as total chars only, but not with selections
# all_lists = letters + symbols + numbers
# total_chars = nr_letters + nr_symbols + nr_numbers

# password = ""
# char_count = 0

# for char in range(1, total_chars + 1):
#     random_char = random.choice(all_lists)
#     password += random_char

# print(password)
# print(all_lists)
# print(total_chars)

# SOLUTION

password_list = []

for char in range(1, nr_letters + 1):
  random_char = random.choice(letters)
  password_list += random_char

for char in range(1, nr_numbers + 1):
  random_char = random.choice(numbers)
  password_list += random_char

for char in range(1, nr_symbols + 1):
  random_char = random.choice(symbols)
  password_list += random_char

random.shuffle(password_list)

password = ""
for char in password_list:
  password = password + char


#print(password_list)
print(f"Your password is: {password}")