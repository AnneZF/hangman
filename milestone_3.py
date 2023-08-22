import random

word_list = ["orange", "apple", "apricot", "pineapple", "kiwi", "prune"]

def random_choice(input_list = word_list):
    return random.choice(input_list)

word = random_choice()

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        ask_for_input()

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()