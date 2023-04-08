import random

print("\n>>>>>>>>>>>>>>>>>>> welcome to Rock paper & scissors game <<<<<<<<<<<<<<<<<<<<<<<")

print("lets go \n")

for i in range(5):

    user_choice = input(">>> ")

    user_score = 0
    computer_score = 0

    moves = ["ROCK", "SCISSORS", "PAPER"]

    computers_move = random.choice(moves)
    print(computers_move)

    if (user_choice == computers_move):
        print(" \n DRAW ")

    if (user_choice == "rock" and computers_move == "PAPER"):
        print("\n YOU LOSE")
        user_score -= 2
        computer_score += 10
    if(user_choice == "paper" and computers_move == "ROCK"):
        print("\n YOU Win ")
        user_score -= 2
        computer_score += 10

    if (user_choice == "scissors" and computers_move == "PAPER"):
        print("\n YOU WIN")
        user_score += 10
        computer_score -= 2
    if(user_choice == "paper" and computers_move == "SCISSORS"):
        print("\n YOU LOSE ")
        user_score -= 2
        computer_score += 10

    if (user_choice == "rock" and computers_move == "SCISSORS"):
        print("\n YOU WIN")
        user_score += 10
        computer_score -= 2
    if(user_choice == "scissors" and computers_move == "ROCK"):
        print("\n YOU LOSE ")
        user_score -= 2
        computer_score += 10


# print("final Score >>> " + "\n YOU " +
#       str(user_score) + "\n ME "+str(computer_score))
