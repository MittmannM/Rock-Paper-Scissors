import random

choices = ["rock", "paper", "scissors", "fountain"]

computer = random.choice(choices)
player = None
while player not in choices:
    player = input("rock, paper, fountain, or scissors?: ").lower()

print("Computer: ", computer.upper())
print("Player: ", player.upper())

def computer_wins():
    print("Computer Wins!")


def player_wins():
    print("Player Wins!")


if player == computer:
    print("Tie")
elif player == "rock":
    if computer == "fountain" or computer == "paper":
        computer_wins()
    else:
        player_wins()
elif player == "scissors":
    if computer == "rock" or  computer == "fountain":
        computer_wins()
    else:
        player_wins()
elif player == "fountain":
    if computer == "paper":
        computer_wins()
    else:
        player_wins()
else:
    if computer == "scissors":
        computer_wins()
    else:
        player_wins()




