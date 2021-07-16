import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while random_number != guess:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Guess again... Too low')
        elif guess > random_number:
            print("Guess Again... Too High")
    print(f"Congratulations! you guessed the number {random_number}")
        



def computerguess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"I guess your random number of {guess}")

computerguess(1000)
            