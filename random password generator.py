# This code will not exactly generate your wi-fi password or something; it justs generates random passwords.

import random

password_characters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '_', '#']

user = int(input("Enter the number of characters in the password: "))

for i in range(user):
    print(random.choice(password_characters_list), end="")
