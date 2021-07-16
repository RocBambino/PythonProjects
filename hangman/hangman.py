import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(word)

    return word

def hangman():
    word = get_valid_word(words)
    word = word.upper()
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #getting user input
    while len(word_letters) >0:
        print('You have used these letters: ', ' '.join(used_letters))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))
        user_letter = input("Guess A Letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You already used this letter. Try Again")
        else:
            print("Invalid Character. Please Try Again")
    print(f"Congratulations You Guessed The Word {word.upper()}")
# While length of the word letter is greater than 0

hangman()