import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def rand_str(n, list_xters):
    rand_str = ''
    for i in range(0, n):
        rand_i = random.randint(0, len(list_xters) - 1)
        rand_str += list_xters[rand_i]
    return rand_str


print("Welcome to the PyPassword Generator!")
pass_str = ''
nr_letters = int(input("How many letters would you like in your password?\n"))
pass_str += rand_str(nr_letters, letters)

nr_symbols = int(input(f"How many symbols would you like?\n"))
pass_str += rand_str(nr_symbols, symbols)

nr_numbers = int(input(f"How many numbers would you like?\n"))
pass_str += rand_str(nr_numbers, numbers)


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password1 = pass_str
print('password1 ==>', password1)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pass_xters = [x for x in pass_str]
random.shuffle(pass_xters)
password2 = "".join(pass_xters)

print('password2 ==>', password2)

