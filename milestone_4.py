from random import choice as random_choice

word_list = ["orange", "apple", "apricot", "pineapple", "kiwi", "prune"]

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random_choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set([chara for chara in self.word]))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            while True:
                try:
                    index = self.word_guessed.index(guess)
                    self.word_guessed[index] = guess
                except ValueError:
                    break
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.\nYou have {self.num_lives} left.")

    def ask_for_input(self):
        while self.num_letters != 0 and self.num_lives != 0:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You have already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


hangman = Hangman(word_list)
hangman.ask_for_input()