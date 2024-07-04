def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
import random
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
yes = 'yes'
no = 'no'
player_score = 0
computer_score = 0
while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else: 
        print("Invalid Input. Try again...")
        continue
    computer_move = ""
    computer_random_number = random.randint(1, 3)

    if computer_random_number == 2:
        computer_move = rock
        prRed("The computer chose rock")
    elif computer_random_number == 3: 
        computer_move = paper
        prYellow("The computer chose paper")
    else: 
        computer_move = scissors
        prCyan("The computer chose scissors")
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        prPurple("You win!")
        player_score += 1

    elif player_move == computer_move:
        prGreen("Draw!")
    else:
        prRed("You lose!")
        computer_score += 1
    player_choose = input("Choose [yes] to continue or [no] to quit: ")
    if player_choose == "no":
        prRed("Thank you for playing!")
        print(f"Your score: {player_score}")
        print(f"Computer's score: {computer_score}")
        break
         

