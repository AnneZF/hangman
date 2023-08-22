import random

word_list = ["orange", "apple", "apricot", "pineapple", "kiwi", "prune"]

def random_choice(input_list = word_list):
    return random.choice(input_list)

word = random_choice()

guess = input("Enter a single letter: ")
if (len(guess) == 1 and 'a' <= guess <= 'z' or 'A' <= guess <= 'Z'):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")