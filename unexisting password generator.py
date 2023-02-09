import random

# Have you ever wondered that when we are to make an account on a website, and we choose a password for our account that is already given to another user, 
# the website tells us that we cannot choose that password, and gives suggestions of passwords that are not existing. How does it do that.

# Let's first make a list of passwords that are already existing.
existing_passwords = ["noser", "bee", "ghost-rider", "killer"]

# Now make a list of characters that a password consists of.
password_characters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '_', '#']

user = input("Enter a password: ")

def give_suggestions():
    for i in range(8):
        print(random.choice(password_characters_list), end="")

if user in existing_passwords:
    print("You cannot use that password. You may choose one of these passwords.")
    for i in range(8):
        give_suggestions()
        print("\n")
