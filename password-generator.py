import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How Many Letters Would You Like: "))
nr_symbols = int(input("How Many Symbols Would You Like: "))
nr_numbers = int(input("How Many Numbers Would You Like: "))

password_list = []
for char in range(1, nr_letters +1):
    password_list += random.choice(letters)

for char in range(1, nr_symbols +1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers +1):
    password_list += random.choice(numbers)

#IN ORDER
#print(password_list)

#SHUFFLE
#random.shuffle(password_list)

#PRINTING IT SHUFFLED
#print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
