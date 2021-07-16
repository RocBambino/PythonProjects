import random

def play():
    user = input("Whats Your choice ? 'r' for Rock, 'p' for Paper, 's' for scissors ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'
    winner = is_winner(user, computer)

    if winner:
        print("You Won!")
    else:
        print("You Loss...")

def is_winner(user, computer):
    if (user == 'r' and computer =='s') or (user == 's' and computer =='p') or (user == 'p' and computer =='r'):
        return True
    else:
        return False

play()