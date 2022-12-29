import random

print("______           _     ______                       _____      _                    ")
print("| ___ \         | |    | ___ \                     /  ___|    (_)                   ")
print("| |_/ /___   ___| | __ | |_/ /_ _ _ __   ___ _ __  \ `--.  ___ _ ___ ___  ___  _ __ ")
print("|    // _ \ / __| |/ / |  __/ _` | '_ \ / _ \ '__|  `--. \/ __| / __/ __|/ _ \| '__|")
print("| |\ \ (_) | (__|   <  | | | (_| | |_) |  __/ |    /\__/ / (__| \__ \__ \ (_) | |   ")
print("\_| \_\___/ \___|_|\_\ \_|  \__, | .__/ \___|_|    \____/ \___|_|___/___/\___/|_|   ")
print("                               |_|                                                ")

user_wins = 0
computer_wins = 0

while True:
    user_input = int(input("[1] Rock \n[2] Paper \n[3] Scissor \n[4] To Exit \nEnter: "))
    
    if user_input == 4: total()
    elif user_input <1: print("Error, try again")
    elif user_input >3: print("Error, try again")
        
    computer_pick = random.randint(1,3)
    if computer_pick == 1: print("Bot chose Rock")
    if computer_pick == 2: print("Bot chose Paper")
    if computer_pick == 3: print("Bot chose Scissor")
    
    if user_input == 1 and computer_pick == 3:
        print("You won!")
        user_wins += 1
    elif user_input == 2 and computer_pick == 1:
        print("You won!")
        user_wins += 1
    elif user_input == 3 and computer_pick == 2:
        print("You won!")
        user_wins += 1
    elif user_input == 3 and computer_pick == 3: print("DRAW!")
    elif user_input == 1 and computer_pick == 1: print("DRAW!")
    elif user_input == 2 and computer_pick == 2: print("DRAW!")
    else:
        print("You lost!")
        computer_wins += 1
    
    def total():
        print("You won", user_wins, "times")
        print("The computer won", computer_wins, "times")
        print("Goodbye!")
