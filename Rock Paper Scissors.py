import random

name = input("Enter your name: ").upper()

while True:
    player_list = []
    computer_list = []
    weapons = ["rock", "paper", "scissor"]
    number_of_points = int(input("Enter the number of points you want in the game: "))

    def first():
        print("---------------------------------------------------")
        computer = random.choice(weapons)
        player = None
        while player not in weapons:
            player = input("Enter rock, paper, or scissor: ").lower()
        if player == computer:
            print(f"{name}: {player}")
            print(f"COMPUTER: {computer}")
            print("DRAW!")
        elif player == "rock":
            if computer == "paper":
                print(f"{name}: {player}")
                print(f"COMPUTER: {computer}")
                print("COMPUTER WINS!")
                computer_list.append(computer)
            elif computer == "scissor":
                print(f"{name}: {player}")
                print(f"COMPUTER: {computer}")
                print(f"{name} WINS!")
                player_list.append(player)
        elif player == "paper":
            if computer == "scissor":
                print(f"{name}: {player}")
                print(f"COMPUTER: {computer}")
                print("COMPUTER WINS!")
                computer_list.append(computer)
            elif computer == "rock":
                print(f"{name}: {player}")
                print(f"COMPUTER: {computer}")
                print(f"{name} WINS!")
                player_list.append(player)
        elif player == "scissor":
            if computer == "rock":
                print(f"{name}: {player}")
                print(f"COMPUTER: {computer}")
                print("COMPUTER WINS!")
                computer_list.append(computer)
            elif computer == "paper":
                print(f"{name}: {player}")
                print(f"COMPUTER: {computer}")
                print(f"{name} WINS!")
                player_list.append(player)

    def check_score():
        print("---------------------------------------------------")
        print(f"{name}'S POINTS: {len(player_list)}")
        print(f"COMPUTER'S POINTS: {len(computer_list)}")

    def declare_winner():
        print("---------------------------------------------------")
        if len(computer_list) > len(player_list):
            print("COMPUTER WINS!")
        elif len(player_list) > len(computer_list):
            print(f"{name} WINS!")
        elif len(player_list) == len(computer_list):
            print("DRAW!")
        print("---------------------------------------------------")

    for i in range(number_of_points):
        first()
    check_score()
    declare_winner()
    
    replay = input("Do you want to play again?: (yes/no): ").lower()

    if replay != "yes":
        print("BYE! WE HOPE TO SEE YOU AGAIN!")
        break
    if replay == "yes":
        print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")